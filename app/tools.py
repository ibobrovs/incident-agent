from app.diagnostic_data import (
    DEFAULT_DEPLOYMENT,
    DEFAULT_SERVICE_HEALTH,
    KNOWN_ISSUES,
    RECENT_DEPLOYMENTS,
    REMEDIATION_ACTIONS,
    SERVICE_HEALTH_DATA,
)
from app.schemas import IncidentType


def check_service_health(service_name: str) -> dict:
    health = SERVICE_HEALTH_DATA.get(service_name, DEFAULT_SERVICE_HEALTH)

    return {
        "service_name": service_name,
        **health,
    }


def search_known_issues(query: str) -> list[str]:
    query_words = set(query.lower().split())

    matched_issues = [
        issue for issue in KNOWN_ISSUES
        if query_words.intersection(issue.lower().split())
    ]

    return matched_issues or KNOWN_ISSUES[:3]


def suggest_remediation(incident_type: IncidentType) -> list[str]:
    return REMEDIATION_ACTIONS[incident_type]


def check_recent_deployments(service_name: str) -> dict:
    deployment = RECENT_DEPLOYMENTS.get(service_name, DEFAULT_DEPLOYMENT)

    return {
        "service_name": service_name,
        **deployment,
    }