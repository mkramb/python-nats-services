from uvicorn import run
from fastapi import FastAPI, status

from consumer.logger import configure_logging
from consumer.models import HealthCheck
from consumer.router import router


app = FastAPI()
app.include_router(router)


@app.get(
    "/health",
    tags=["healthcheck"],
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


if __name__ == "__main__":
    configure_logging()
    run(app, host="0.0.0.0", access_log=False, port=3000)
