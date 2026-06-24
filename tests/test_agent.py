from app.agent import analyze_incident_with_agent
from app.schemas import IncidentRequest
from app.settings import settings


def test_agent_returns_fallback_response_without_api_key(monkeypatch):
    monkeypatch.setattr(settings, "openai_api_key", None)

    request = IncidentRequest(
        service_name="payment-api",
        environment="production",
        incident="Payment API returns 500 after deployment. Logs show database timeout and increased latency.",
    )

    response = analyze_incident_with_agent(request, request_id="test-request")

    assert response.service_name == "payment-api"
    assert response.severity == "high"
    assert response.incident_type == "database_timeout"
    assert response.needs_human_review is True
    assert "check_service_health" in response.tools_used
    assert len(response.recommended_actions) > 0