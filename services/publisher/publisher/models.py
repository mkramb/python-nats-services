from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"

class Outgoing(BaseModel):
    message: str