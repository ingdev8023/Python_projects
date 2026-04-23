from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.log_models import LogRequest
from app.services.analyzer import count_logs

router = APIRouter()

@router.post("/analyze")
def analyze_logs(payload: LogRequest):
    return count_logs(payload.logs)

@router.post("/analyze-file")
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