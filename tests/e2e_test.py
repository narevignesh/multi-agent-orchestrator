from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_e2e_workflow():
    # Step 1: Initialize agents
    response = client.post("/api/v1/agents/init")
    assert response.status_code == 200
    assert response.json() == {"status": "agents initialized"}

    # Step 2: Send a request to the orchestrator
    response = client.post("/api/v1/orchestrate", json={"task": "example task"})
    assert response.status_code == 200
    assert "result" in response.json()

    # Step 3: Validate the result
    result = response.json()["result"]
    assert result == "expected result"

    # Step 4: Check logs for the task
    response = client.get("/api/v1/logs")
    assert response.status_code == 200
    logs = response.json()
    assert len(logs) > 0
    assert "example task" in logs[-1]["task"]  # Check if the last log contains the task

    # Step 5: Clean up agents
    response = client.post("/api/v1/agents/cleanup")
    assert response.status_code == 200
    assert response.json() == {"status": "agents cleaned up"}