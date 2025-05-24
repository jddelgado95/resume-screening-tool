# resume-screening-tool

Automatically evaluate and rank resumes based on how well they match a given job description using NLP techniques

Tech Stack:
Backend: FastAPI (recommended for async and performance) or Flask
NLP Libraries: SpaCy (easier for named entity recognition and parsing) or NLTK
Similarity Metric: Cosine similarity using TF-IDF or sentence embeddings
Data Format: PDF or plain text resumes

Features:
Upload Job Description and Resumes:
Input: Text or PDF
Parse and clean data

Text Preprocessing:
Tokenization, lemmatization
Remove stopwords
Vectorization (TF-IDF or word embeddings)

Similarity Scoring:
Compare each resume to the job description
Compute cosine similarity
Output ranking scores

Classification (Optional):
Pretrained model to classify resumes by role (e.g., Data Engineer, Backend Developer)
REST API Endpoints (with FastAPI/Flask):
/upload-job-description
/upload-resume
/get-ranking
/classify-resume

UI (Optional):
Simple frontend with file upload & ranking display (can use Streamlit or React)

Job Description → [Preprocess → Vectorize]
↑
↓
Resume 1 → [Preprocess → Vectorize → Cosine Similarity Score]
Resume 2 → ...

Milestones:
Set up FastAPI project
Create endpoints for uploading JD and resumes
Integrate PDF/text parsing
Implement preprocessing with SpaCy
Compute cosine similarity scores
Return ranked results via API
(Optional) Add resume role classification using a trained classifier
(Optional) Add frontend or Streamlit interface
