from app.utils import extract_text_from_pdf
from app.nlp import compute_similarity
import os

def rank_resumes():
    job_path = "app/data/job_descriptions"
    resumes_path = "app/data/resumes"

    job_text = extract_text_from_pdf(os.path.join(job_path, os.listdir(job_path)[0]))
    scores = []

    for resume in os.listdir(resumes_path):
        resume_path = os.path.join(resumes_path, resume)
        resume_text = extract_text_from_pdf(resume_path)
        score = compute_similarity(job_text, resume_text)
        scores.append((resume, round(score, 2)))

    return sorted(scores, key=lambda x: x[1], reverse=True)