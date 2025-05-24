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

resume-screening-tool/
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── endpoints.py
│ ├── core/
│ │ ├── ranking.py
│ │ ├── classification.py
│ ├── models/
│ │ ├── resume_classifier.pkl
│ ├── utils/
│ │ ├── parser.py
│ │ ├── nlp_utils.py
│ ├── data/
│ │ ├── resumes/
│ │ ├── job_descriptions/
│ └── templates/
│ └── index.html (optional for frontend)
├── requirements.txt
├── .gitignore
└── .github/
└── workflows/
└── python-app.yml

To run:
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m spacy download en_core_web_sm
$uvicorn app.main:app --reload

Post the job description:
$ curl -X POST "http://localhost:8000/upload-job-description" -F "file=@/Users/juandiegodelgado/learning-sw/ai/resume-screening-tool/app/data/job_descriptions/senior_support_engineer_chronicle.pdf"

Output:
{"message":"Job description uploaded and processed."}%

Score a resume:
$ curl -X POST "http://localhost:8000/score-resume" -F "file=@/Users/juandiegodelgado/learning-sw/ai/resume-screening-tool/app/data/resumes/SW\_\_Engineer_JuanDiego_Delgado_CV.pdf"
{"similarity_score":0.052825601517136014}%
$deactivate
