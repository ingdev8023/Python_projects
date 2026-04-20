from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class LogRequest(BaseModel):
    logs: list[str]

@app.get("/")
def root():
    return {"message":"API is running"}

@app.post('/analyze')
def analyze_logs(payload: LogRequest):
    logs_dict = {}
    pattern = re.compile(r"(ERROR|INFO|WARNING)")

    for log in payload.logs:        
        match = pattern.search(pattern, log)
        if match:
            level = match.group(0)
            if level not in logs_dict:
                logs_dict[level] = 0
            logs_dict[level] += 1
    
    return logs_dict


""" logs = {
  "logs": [
    "INFO: User login",
    "ERROR: DB timeout",
    "ERROR: DB timeout"
  ]
} """