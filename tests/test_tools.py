from app.schemas import IncidentType
from app.tools import check_recent_deployments, check_service_health, search_known_issues, suggest_remediation


def test_check_service_health_returns_expected_structure():
    result = check_service_health("payment-api")

    assert result["service_name"] == "payment-api"
    assert result["status"] == "degraded"
    assert isinstance(result["latency_ms"], int)
    assert isinstance(result["error_rate"], float)


def test_search_known_issues_returns_list():
    result = search_known_issues("database timeout after deployment")

    assert isinstance(result, list)
    assert len(result) > 0
    assert "Database connection pool exhausted after deployment" in result


def test_suggest_remediation_returns_actions_for_database_timeout():
    result = suggest_remediation(IncidentType.database_timeout)

    assert isinstance(result, list)
    assert "Check database connection pool configuration" in result


def test_check_recent_deployments_returns_expected_structure():
    result = check_recent_deployments("payment-api")

    assert result["service_name"] == "payment-api"
    assert result["status"] == "completed"
    assert "last_deployment" in result
    assert "version" in result