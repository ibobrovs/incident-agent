from fastapi import APIRouter

from app.schemas import IncidentAnalysisResponse, IncidentRequest
from app.services.incident_service import analyze_incident
from app.settings import settings

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.get("/version")
def version() -> dict:
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "model_name": settings.model_name,
        "llm_enabled": bool(settings.openai_api_key),
    }


@router.post("/analyze-incident", response_model=IncidentAnalysisResponse)
def analyze_incident_endpoint(request: IncidentRequest) -> IncidentAnalysisResponse:
    return analyze_incident(request)
