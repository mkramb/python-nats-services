from loguru import logger
from faststream.nats.fastapi import NatsRouter
from faststream.nats import PullSub

from consumer.models import Incoming

router = NatsRouter("nats://nats:4222", logger=logger)


@router.subscriber(
    stream="events",
    durable="events-consumer",
    subject="events.*.*",
    pull_sub=PullSub(),
)
async def handler(body: Incoming):
    logger.info(f"Message received: {body.message}")
