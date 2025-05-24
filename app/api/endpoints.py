from fastapi import APIRouter, File, UploadFile, HTTPException
from app.core.ranking import rank_resumes
from app.core.classification import classify_resume
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "app/data"

@router.post("/upload-job-description")
async def upload_job_description(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, "job_descriptions", file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, "resumes", file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}

@router.get("/get-ranking")
def get_ranking():
    scores = rank_resumes()
    return {"ranking": scores}

@router.post("/classify-resume")
def classify(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")
    prediction = classify_resume(content)
    return {"role": prediction}