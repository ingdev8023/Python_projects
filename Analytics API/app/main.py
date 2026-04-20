from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class LogRequest(BaseModel):
    logs: list[str]

@app.get("/")
def root():
    return {"message":"API is running"}

def count_logs(logs: list[str]):
    logs_dict = {"INFO":0, "WARNING":0,"ERROR":0, "duplicates":0}
    seen_logs = set()
    pattern = re.compile(r"(ERROR|INFO|WARNING)")
    for log in logs:       
        match = pattern.search(log)
        if match:
            if log in seen_logs:
                logs_dict['duplicates'] += 1
            else:
                level = match.group(0)
                logs_dict[level] += 1
        seen_logs.add(log)    
            
    return logs_dict

@app.post('/analyze')
def analyze_logs(payload: LogRequest):
    return count_logs(payload.logs)