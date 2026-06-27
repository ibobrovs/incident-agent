from app.evaluator import evaluate_incident_response
from app.schemas import IncidentAnalysisResponse


def test_evaluator_passes_valid_database_timeout_response():
    response = IncidentAnalysisResponse(
        service_name="payment-api",
        severity="high",
        incident_type="database_timeout",
        summary="Payment API returns 500 after deployment.",
        likely_cause="Database timeout after deployment.",
        tools_used=["check_service_health", "suggest_remediation"],
        recommended_actions=[
            "Check database connection pool configuration",
            "Review recent deployment changes",
        ],
        needs_human_review=True,
    )

    expected = {
        "severity": "high",
        "incident_type": "database_timeout",
        "must_include_actions": ["database", "deployment"],
    }

    result = evaluate_incident_response(response, expected)

    assert result["passed"] is True
    assert result["checks"]["severity"] is True
    assert result["checks"]["incident_type"] is True
    assert result["checks"]["recommended_actions"] is True


def test_evaluator_fails_wrong_incident_type():
    response = IncidentAnalysisResponse(
        service_name="payment-api",
        severity="high",
        incident_type="network_issue",
        summary="Payment API returns 500 after deployment.",
        likely_cause="Network issue.",
        tools_used=["check_service_health"],
        recommended_actions=["Check network latency"],
        needs_human_review=True,
    )

    expected = {
        "severity": "high",
        "incident_type": "database_timeout",
        "must_include_actions": ["database"],
    }

    result = evaluate_incident_response(response, expected)

    assert result["passed"] is False
    assert result["checks"]["incident_type"] is False


def test_evaluator_fails_missing_required_action_keyword():
    response = IncidentAnalysisResponse(
        service_name="payment-api",
        severity="high",
        incident_type="database_timeout",
        summary="Payment API returns 500 after deployment.",
        likely_cause="Database timeout after deployment.",
        tools_used=["check_service_health"],
        recommended_actions=["Check logs"],
        needs_human_review=True,
    )

    expected = {
        "severity": "high",
        "incident_type": "database_timeout",
        "must_include_actions": ["database"],
    }

    result = evaluate_incident_response(response, expected)

    assert result["passed"] is False
    assert result["checks"]["recommended_actions"] is False
