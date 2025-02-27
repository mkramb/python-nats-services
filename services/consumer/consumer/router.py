import json
from loguru import logger

from faststream.nats import PullSub, JStream
from faststream.nats.fastapi import NatsRouter, NatsMessage
from faststream.exceptions import ValidationError
from faststream import ExceptionMiddleware

from consumer.settings import NATS_URL
from consumer.models import Incoming


class RpcValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return json.dumps({"message": self.message})


def rpc_error_handler(exception: RpcValidationException) -> None:
    logger.error("Error processing testing.command")
    return str(exception)


def create_rpc_error_handler():
    return {
        RpcValidationException: rpc_error_handler,
    }


exception_middleware = ExceptionMiddleware(
    publish_handlers={**create_rpc_error_handler()}
)

router = NatsRouter(NATS_URL, logger=logger, middlewares=[exception_middleware])
stream = JStream(name="events", declare=False)


@logger.catch()
@router.subscriber(
    stream=stream,
    durable="events-consumer",
    subject="events.*.*",
    pull_sub=PullSub(),
)
async def handler_events(body: Incoming, msg: NatsMessage):
    logger.info(f"Message received: {body}")

    await msg.ack()


@logger.catch()
@router.subscriber("testing.command")
async def handler_receiver(message: NatsMessage):
    logger.info(f"Received message")

    decoded = await message.decode()
    logger.info(f"Decoded contents: {decoded}")

    if 42 in decoded:
        raise RpcValidationException("Error processing testing.command")

    return decoded
