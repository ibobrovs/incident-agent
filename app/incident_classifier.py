from app.incident_rules import CRITICAL_KEYWORDS, INCIDENT_TYPE_RULES
from app.schemas import IncidentRequest, IncidentType, Severity


def classify_incident_type(request: IncidentRequest) -> IncidentType:
    text = _combined_text(request)
    best_incident_type = IncidentType.unknown
    best_score = 0

    for rule in INCIDENT_TYPE_RULES:
        score = _count_keyword_matches(text, rule.keywords)

        if score > best_score:
            best_score = score
            best_incident_type = rule.incident_type

    return best_incident_type


def classify_severity(request: IncidentRequest, incident_type: IncidentType) -> Severity:
    text = _combined_text(request)

    if request.environment == "production" and _contains_any(text, CRITICAL_KEYWORDS):
        return Severity.critical

    if request.environment == "production" and incident_type != IncidentType.unknown:
        return Severity.high

    if request.environment == "staging" and incident_type != IncidentType.unknown:
        return Severity.medium

    return Severity.low


def _combined_text(request: IncidentRequest) -> str:
    return f"{request.service_name} {request.environment} {request.incident}".lower()


def _count_keyword_matches(text: str, keywords: tuple[str, ...]) -> int:
    return sum(1 for keyword in keywords if keyword in text)


def _contains_any(text: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in text for keyword in keywords)