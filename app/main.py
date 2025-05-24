from fastapi import FastAPI, UploadFile, File, HTTPException
from app.nlp import preprocess_text, compute_similarity
from app.utils import extract_text_from_pdf
from app.models import SimilarityResponse

app = FastAPI()

job_description_text = None  # Store uploaded job description in-memory

@app.post("/upload-job-description")
async def upload_job_description(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files supported for job description.")
    contents = await file.read()
    with open("app/data/job_descriptions/job_description.pdf", "wb") as f:
        f.write(contents)
    global job_description_text
    job_description_text = extract_text_from_pdf("app/data/job_descriptions/job_description.pdf")
    job_description_text = preprocess_text(job_description_text)
    return {"message": "Job description uploaded and processed."}

@app.post("/score-resume", response_model=SimilarityResponse)
async def score_resume(file: UploadFile = File(...)):
    if not job_description_text:
        raise HTTPException(status_code=400, detail="Upload job description first.")
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes supported.")
    contents = await file.read()
    with open("app/data/resumes/resume.pdf", "wb") as f:
        f.write(contents)
    resume_text = extract_text_from_pdf("app/data/resumes/resume.pdf")
    resume_text = preprocess_text(resume_text)
    score = compute_similarity([job_description_text, resume_text])
    return SimilarityResponse(similarity_score=score)
