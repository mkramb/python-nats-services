from uvicorn import run
from loguru import logger
from pydantic import BaseModel
from fastapi import FastAPI, status

from publisher.logger import LogRequestsMiddleware, configure_logging

app = FastAPI()
app.add_middleware(LogRequestsMiddleware)


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
    run(app, host="0.0.0.0", port=3000, access_log=False)
