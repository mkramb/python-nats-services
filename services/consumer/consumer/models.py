from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"


class Incoming(BaseModel):
    message: str