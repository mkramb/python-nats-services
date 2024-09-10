from uvicorn import run
from loguru import logger
from asyncio import create_task
from pydantic import BaseModel
from fastapi import FastAPI, status

from consumer.logger import configure_logging
from consumer.router import router


app = FastAPI()
app.include_router(router)


class HealthCheck(BaseModel):
    status: str = "OK"


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


if __name__ == "__main__":
    configure_logging()
    run(app, host="0.0.0.0", access_log=False, port=3000)
