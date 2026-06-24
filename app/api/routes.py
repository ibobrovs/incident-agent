from fastapi import APIRouter

from app.schemas import IncidentAnalysisResponse, IncidentRequest
from app.services.incident_service import analyze_incident


router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.post("/analyze-incident", response_model=IncidentAnalysisResponse)
def analyze_incident_endpoint(request: IncidentRequest) -> IncidentAnalysisResponse:
    return analyze_incident(request)