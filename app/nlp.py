import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def compute_similarity(texts: list[str]) -> list[float]:
    """
    Expects a list with 2 strings: [job_description, resume_text]
    Returns cosine similarity score between them.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return score[0][0]