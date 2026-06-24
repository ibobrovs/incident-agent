import pytest
from pydantic import ValidationError

from app.schemas import IncidentAnalysisResponse, IncidentRequest


def test_incident_request_accepts_valid_data():
    result = IncidentRequest(
        service_name="payment-api",
        environment="production",
        incident="Payment API returns 500 after deployment. Logs show database timeout.",
    )

    assert result.service_name == "payment-api"
    assert result.environment == "production"


def test_incident_request_rejects_invalid_environment():
    with pytest.raises(ValidationError):
        IncidentRequest(
            service_name="payment-api",
            environment="prod",
            incident="Payment API returns 500 after deployment. Logs show database timeout.",
        )


def test_incident_request_rejects_short_incident():
    with pytest.raises(ValidationError):
        IncidentRequest(
            service_name="payment-api",
            environment="production",
            incident="too short",
        )


def test_incident_analysis_response_accepts_valid_data():
    result = IncidentAnalysisResponse(
        service_name="payment-api",
        severity="high",
        incident_type="database_timeout",
        summary="Payment API has errors in production.",
        likely_cause="Database timeout after deployment.",
        tools_used=["check_service_health"],
        recommended_actions=["Check database connection pool"],
        needs_human_review=True,
    )

    assert result.severity == "high"
    assert result.incident_type == "database_timeout"
    assert result.needs_human_review is True