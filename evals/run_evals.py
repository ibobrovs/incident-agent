import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from app.agent import analyze_incident_with_agent
from app.evaluator import evaluate_incident_response
from app.schemas import IncidentRequest


def load_cases() -> list[dict]:
    cases_path = Path(__file__).parent / "cases.json"
    return json.loads(cases_path.read_text(encoding="utf-8"))


def run_evals() -> bool:
    cases = load_cases()
    passed_count = 0

    for case in cases:
        request = IncidentRequest(**case["input"])
        response = analyze_incident_with_agent(request, request_id=f"eval-{case['name']}")
        result = evaluate_incident_response(response, case["expected"])

        if result["passed"]:
            passed_count += 1

        print(
            {
                "case": case["name"],
                "passed": result["passed"],
                "checks": result["checks"],
            }
        )

    print(f"Passed {passed_count}/{len(cases)} eval cases")
    return passed_count == len(cases)


if __name__ == "__main__":
    success = run_evals()
    raise SystemExit(0 if success else 1)