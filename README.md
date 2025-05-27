# Resume screening tool

Automatically evaluate and rank resumes based on how well they match a given job description using NLP techniques

## Tech Stack:

- Backend: FastAPI (recommended for async and performance) or Flask
- NLP Libraries: SpaCy (easier for named entity recognition and parsing) or NLTK
- Similarity Metric: Cosine similarity using TF-IDF or sentence embeddings
- Data Format: PDF or plain text resumes

### Features:

- Upload Job Description and Resumes:
- Input: Text or PDF
- Parse and clean data

### Text Preprocessing:

- Tokenization, lemmatization
- Remove stopwords
- Vectorization (TF-IDF or word embeddings)

### Similarity Scoring:

- Compare each resume to the job description
- Compute cosine similarity
- Output ranking scores

### Classification (Optional):

- Pretrained model to classify resumes by role (e.g., Data Engineer, Backend Developer)
- REST API Endpoints (with FastAPI/Flask):

```bash
/upload-job-description
/upload-resume
/get-ranking
/classify-resume
```

### UI (Optional):

- Simple frontend with file upload & ranking display (can use Streamlit or React)

```bash
Job Description → [Preprocess → Vectorize]
↑
↓
Resume 1 → [Preprocess → Vectorize → Cosine Similarity Score]
Resume 2 → ...
```

## Milestones:

1. Set up FastAPI project
2. Create endpoints for uploading JD and resumes
3. Integrate PDF/text parsing
4. Implement preprocessing with SpaCy
5. Compute cosine similarity scores
6. Return ranked results via API
7. (Optional) Add resume role classification using a trained classifier
8. (Optional) Add frontend or Streamlit interface

## Folder structure:

```bash
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

```

## How to run:

Run a venv:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m spacy download en_core_web_sm
$ uvicorn app.main:app --reload

```

Post the job description:

```bash
$ curl -X POST "http://localhost:8000/upload-job-description" -F "file=@/Users/juandiegodelgado/learning-sw/ai/resume-screening-tool/app/data/job_descriptions/senior_support_engineer_chronicle.pdf"
```

Output:

```bash
{"message":"Job description uploaded and processed."}%
```

Score a resume:

```bash
$ curl -X POST "http://localhost:8000/score-resume" -F "file=@/Users/juandiegodelgado/learning-sw/ai/resume-screening-tool/app/data/resumes/SW\_\_Engineer_JuanDiego_Delgado_CV.pdf"
```

Outpu:

```bash
{"similarity_score":0.052825601517136014}%
```

Exit the venv:

```
$deactivate
```

## To run with classification:

```bash
conda create --name myenv python=3.11
conda activate myenv
```

you can download it from here:

```bash
https://www.anaconda.com/docs/getting-started/miniconda/install#mac-os
```

Run conda with pytorch:

```bash
conda create -n torch-env python=3.10
```

Within the venv:

```bash
pip install numpy==1.25.0 --force-reinstall
pip uninstall torch torchvision torchaudio
pip cache purge # optional, clears cache to force re-download
conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install torch==2.2.0
pip install transformers==4.31.0
pip install --force-reinstall sentence-transformers==2.2.2
```
