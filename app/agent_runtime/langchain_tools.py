from langchain.tools import tool

from app.schemas import IncidentType
from app.tools import check_recent_deployments, check_service_health, search_known_issues, suggest_remediation


@tool
def check_service_health_tool(service_name: str) -> dict:
    """Check mocked health status, latency and error rate for a service."""
    return check_service_health(service_name)


@tool
def search_known_issues_tool(query: str) -> list[str]:
    """Search mocked known technical issues related to an incident."""
    return search_known_issues(query)


@tool
def suggest_remediation_tool(incident_type: str) -> list[str]:
    """Suggest remediation actions for a classified incident type."""
    try:
        parsed_incident_type = IncidentType(incident_type)
    except ValueError:
        parsed_incident_type = IncidentType.unknown

    return suggest_remediation(parsed_incident_type)


@tool
def check_recent_deployments_tool(service_name: str) -> dict:
    """Check mocked recent deployment information for a service."""
    return check_recent_deployments(service_name)


langchain_tools = [
    check_service_health_tool,
    search_known_issues_tool,
    suggest_remediation_tool,
    check_recent_deployments_tool,
]