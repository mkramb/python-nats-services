import sys

from loguru import logger
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


def format_record(record):
    record["level"] = record["level"].no
    return '{{"message": "{message}","timestamp": "{time}", level": "{level}"}}\n'


def configure_logging():
    # Remove default logger
    logger.remove()

    # Add custom handler for stdout
    # with JSON formatting
    logger.add(sys.stdout, format=format_record, level="INFO")
