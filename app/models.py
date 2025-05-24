from pydantic import BaseModel

class JobDescription(BaseModel):
    text: str

class ResumeText(BaseModel):
    text: str

class SimilarityResponse(BaseModel):
    similarity_score: float