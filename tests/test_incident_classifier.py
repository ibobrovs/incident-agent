from app.incident_classifier import classify_incident_type, classify_severity
from app.schemas import IncidentRequest, IncidentType, Severity


def test_classifies_database_timeout_incident():
    request = IncidentRequest(
        service_name="payment-api",
        environment="production",
        incident="Logs show PostgreSQL timeout and database connection pool errors.",
    )

    incident_type = classify_incident_type(request)

    assert incident_type == IncidentType.database_timeout


def test_classifies_deployment_failure_incident():
    request = IncidentRequest(
        service_name="catalog-api",
        environment="production",
        incident="Service started failing immediately after deployment of version 1.4.2.",
    )

    incident_type = classify_incident_type(request)

    assert incident_type == IncidentType.deployment_failure


def test_classifies_network_issue_incident():
    request = IncidentRequest(
        service_name="gateway-api",
        environment="staging",
        incident="Requests fail because of DNS resolution errors and gateway timeout.",
    )

    incident_type = classify_incident_type(request)

    assert incident_type == IncidentType.network_issue


def test_classifies_auth_issue_incident():
    request = IncidentRequest(
        service_name="auth-api",
        environment="production",
        incident="Users receive 401 unauthorized errors after token validation changes.",
    )

    incident_type = classify_incident_type(request)

    assert incident_type == IncidentType.auth_issue


def test_classifies_unknown_incident():
    request = IncidentRequest(
        service_name="reporting-api",
        environment="development",
        incident="Unexpected behavior was reported but there are no clear technical symptoms.",
    )

    incident_type = classify_incident_type(request)

    assert incident_type == IncidentType.unknown


def test_production_known_incident_is_high_severity():
    request = IncidentRequest(
        service_name="payment-api",
        environment="production",
        incident="Logs show database timeout and increased latency.",
    )

    incident_type = classify_incident_type(request)
    severity = classify_severity(request, incident_type)

    assert severity == Severity.high


def test_production_outage_is_critical_severity():
    request = IncidentRequest(
        service_name="payment-api",
        environment="production",
        incident="Complete outage. Service down for all users.",
    )

    incident_type = classify_incident_type(request)
    severity = classify_severity(request, incident_type)

    assert severity == Severity.critical


def test_staging_known_incident_is_medium_severity():
    request = IncidentRequest(
        service_name="gateway-api",
        environment="staging",
        incident="DNS resolution errors and gateway timeout.",
    )

    incident_type = classify_incident_type(request)
    severity = classify_severity(request, incident_type)

    assert severity == Severity.medium