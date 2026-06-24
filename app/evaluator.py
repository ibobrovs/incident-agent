from app.schemas import IncidentAnalysisResponse


def _actions_contain_keywords(actions: list[str], keywords: list[str]) -> bool:
    combined_actions = " ".join(actions).lower()
    return all(keyword.lower() in combined_actions for keyword in keywords)


def evaluate_incident_response(
    response: IncidentAnalysisResponse,
    expected: dict,
) -> dict:
    severity_passed = response.severity == expected["severity"]
    incident_type_passed = response.incident_type == expected["incident_type"]

    actions_passed = _actions_contain_keywords(
        response.recommended_actions,
        expected.get("must_include_actions", []),
    )

    passed = severity_passed and incident_type_passed and actions_passed

    return {
        "passed": passed,
        "checks": {
            "severity": severity_passed,
            "incident_type": incident_type_passed,
            "recommended_actions": actions_passed,
        },
    }