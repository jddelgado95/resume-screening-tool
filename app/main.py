from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.nlp import preprocess_text, compute_similarity
from app.utils import extract_text_from_pdf
from app.core.classification import classify_resume
from app.models import SimilarityResponse
from app.api.endpoints import router

app = FastAPI()

job_description_text = None
resumes = []  # List of (filename, text)

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


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes supported.")
    contents = await file.read()
    save_path = f"app/data/resumes/{file.filename}"
    with open(save_path, "wb") as f:
        f.write(contents)
    resume_text = extract_text_from_pdf(save_path)
    resume_text = preprocess_text(resume_text)
    resumes.append((file.filename, resume_text))
    return {"message": f"Uploaded and parsed resume: {file.filename}"}


@app.get("/get-ranking")
async def get_ranking():
    if not job_description_text or not resumes:
        raise HTTPException(status_code=400, detail="Upload job description and resumes first.")
    
    resume_texts = [r[1] for r in resumes]
    ranking = compute_similarity(job_description_text, resume_texts)
    
    # Re-map to filenames
    name_to_text = {r[1]: r[0] for r in resumes}
    result = [{"filename": name_to_text[res], "score": round(score, 4)} for res, score in ranking]
    return {"ranking": result}


@app.post("/classify-resume")
async def classify(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes supported.")
    contents = await file.read()
    with open("app/data/resumes/temp_resume.pdf", "wb") as f:
        f.write(contents)
    resume_text = extract_text_from_pdf("app/data/resumes/temp_resume.pdf")
    resume_text = preprocess_text(resume_text)
    predicted_role = classify_resume(resume_text)
    return {"predicted_role": predicted_role}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)