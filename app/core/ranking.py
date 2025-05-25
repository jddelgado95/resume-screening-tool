from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')

except Exception as e:
    print(f"Warning: Could not load SentenceTransformer: {e}")
    model = None # Small & fast model

def rank_resumes(job_description: str, resumes: list[str]) -> list[tuple[str, float]]:
    """
    Compute cosine similarity between a job description and multiple resumes.

    Args:
        job_description (str): The job description text.
        resumes (list[str]): List of resume texts.

    Returns:
        List of tuples (resume_text, similarity_score), sorted by score descending.
    """
    embeddings = model.encode([job_description] + resumes)
    job_embedding = embeddings[0]
    resume_embeddings = embeddings[1:]

    similarities = cosine_similarity([job_embedding], resume_embeddings)[0]
    ranked = sorted(zip(resumes, similarities), key=lambda x: x[1], reverse=True)
    
    return ranked