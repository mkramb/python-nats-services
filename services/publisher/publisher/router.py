from uuid import uuid4
from loguru import logger
from fastapi import status
from faststream.nats.fastapi import NatsRouter

from publisher.settings import NATS_URL
from publisher.models import Outgoing

router = NatsRouter(NATS_URL, logger=logger)


@router.get("/emit")
async def publish():
    random_id = str(uuid4())
    message = Outgoing(message=random_id)

    await router.broker.publish(
        message, stream="events", subject=f"events.message.{random_id}"
    )

    logger.info(f"Emitted new message id: {random_id}")

    return status.HTTP_201_CREATED
