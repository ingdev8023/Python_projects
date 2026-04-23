from pydantic import BaseModel

class LogRequest(BaseModel):
    logs: list[str]