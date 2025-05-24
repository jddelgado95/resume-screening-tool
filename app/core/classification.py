import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load pre-trained model (train separately and store as resume_classifier.pkl)
model = joblib.load("app/models/resume_classifier.pkl")
vectorizer = joblib.load("app/models/vectorizer.pkl")

def classify_resume(text: str) -> str:
    X = vectorizer.transform([text])
    return model.predict(X)[0]