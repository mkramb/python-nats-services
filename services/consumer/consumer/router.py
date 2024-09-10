from loguru import logger
from faststream.nats import PullSub
from faststream.nats.fastapi import NatsRouter, NatsMessage

from consumer.settings import NATS_URL
from consumer.models import Incoming

router = NatsRouter(NATS_URL, logger=logger)


@router.subscriber(
    stream="events",
    durable="events-consumer",
    subject="events.*.*",
    pull_sub=PullSub(),
)
async def handler(body: Incoming, msg: NatsMessage):
    logger.info(f"Message received: {body}")

    await msg.ack()
