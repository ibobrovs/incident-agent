from app.incident_classifier import classify_incident_type, classify_severity
from app.schemas import IncidentAnalysisResponse, IncidentRequest
from app.tools import check_recent_deployments, check_service_health, search_known_issues, suggest_remediation


def build_fallback_response(request: IncidentRequest) -> IncidentAnalysisResponse:
    health = check_service_health(request.service_name)
    known_issues = search_known_issues(request.incident)
    deployment = check_recent_deployments(request.service_name)

    incident_type = classify_incident_type(request)
    severity = classify_severity(request, incident_type)
    actions = suggest_remediation(incident_type)

    return IncidentAnalysisResponse(
        service_name=request.service_name,
        severity=severity,
        incident_type=incident_type,
        summary=f"{request.service_name} has errors in {request.environment} environment.",
        likely_cause=(
            f"Health status is {health['status']}. "
            f"Known issues include: {known_issues[0]}. "
            f"Last deployment status: {deployment['status']}."
        ),
        tools_used=[
            "check_service_health",
            "search_known_issues",
            "check_recent_deployments",
            "suggest_remediation",
        ],
        recommended_actions=actions,
        needs_human_review=True,
    )