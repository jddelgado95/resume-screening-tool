from sklearn.metrics.pairwise import cosine_similarity

# Map roles to example descriptions (you can improve this with labeled data later)
ROLE_DESCRIPTIONS = {
    "Data Engineer": "Builds pipelines, handles ETL, and works with big data tools like Spark and Airflow.",
    "Backend Developer": "Develops server-side applications using Python, FastAPI, databases, and APIs.",
    "Machine Learning Engineer": "Develops ML models, works with sklearn, TensorFlow, and deploys models.",
}

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')

except Exception as e:
    print(f"Warning: Could not load SentenceTransformer: {e}")
    model = None

def classify_resume(resume_text):
    if model is None:
        return {
            "label": "Not classified",
            "score": 0.0
        }

def classify_resume(resume_text: str) -> str:
    resume_embedding = model.encode([resume_text])
    role_embeddings = model.encode(list(ROLE_DESCRIPTIONS.values()))

    similarities = cosine_similarity(resume_embedding, role_embeddings)[0]
    best_match_idx = similarities.argmax()
    predicted_role = list(ROLE_DESCRIPTIONS.keys())[best_match_idx]

    return predicted_role