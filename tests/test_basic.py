from fastapi.testclient import TestClient
from app.main import app  # adjust if your main app file has a different path

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200