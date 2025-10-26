from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Multi-Agent Orchestrator!"}

def test_create_agent():
    response = client.post("/api/v1/agents/", json={"name": "Test Agent"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Agent"

def test_get_agents():
    response = client.get("/api/v1/agents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_agent_creation():
    response = client.post("/api/v1/agents/", json={"invalid_field": "Test Agent"})
    assert response.status_code == 422  # Unprocessable Entity for invalid input

def test_agent_not_found():
    response = client.get("/api/v1/agents/999")
    assert response.status_code == 404  # Not Found for non-existing agent