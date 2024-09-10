from os import getenv

NATS_URL = getenv("NATS_URL", "nats://localhost:4222")