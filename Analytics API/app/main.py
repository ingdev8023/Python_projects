from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()

class LogRequest(BaseModel):
    logs: list[str]

@app.get("/")
def root():
    return {"message":"API is running"}

def count_logs(logs: list[str]) -> dict[str,int]:
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

@app.post('/analyze-file')
async def analyze_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    if not file.filename.endswith((".log",",txt")):
        raise HTTPException(status_code=400,detail="Only .log or .txt files are allowed")
    
    contents = await file.read()

    if not contents:
        raise HTTPException(status_code=400, detail="File is empty")
    
    try:             
        text = contents.decode('utf-8')
    except:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded text")
    
    logs = text.splitlines()
    return count_logs(logs)
        