from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_returns_application_metadata():
    response = client.get("/version")
    data = response.json()

    assert response.status_code == 200
    assert data["app_name"] == "ai-incident-agent"
    assert data["app_version"] == "0.1.0"
    assert data["model_name"] == "gpt-4o-mini"
    assert data["llm_enabled"] is False


def test_analyze_incident_returns_structured_response():
    payload = {
        "service_name": "payment-api",
        "environment": "production",
        "incident": (
            "Payment API returns 500 after deployment. "
            "Logs show database timeout and increased latency."
        ),
    }

    response = client.post("/analyze-incident", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["service_name"] == "payment-api"
    assert data["severity"] == "high"
    assert data["incident_type"] == "database_timeout"
    assert data["needs_human_review"] is True
    assert "check_service_health" in data["tools_used"]
    assert isinstance(data["recommended_actions"], list)
