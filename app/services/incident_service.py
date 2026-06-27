from time import perf_counter
from uuid import uuid4

from app.agent import analyze_incident_with_agent
from app.logging_config import get_logger
from app.schemas import IncidentAnalysisResponse, IncidentRequest

logger = get_logger(__name__)


def analyze_incident(request: IncidentRequest) -> IncidentAnalysisResponse:
    request_id = str(uuid4())
    started_at = perf_counter()

    logger.info(
        "request_received",
        extra={
            "request_id": request_id,
            "service_name": request.service_name,
            "environment": request.environment,
            "incident_length": len(request.incident),
        },
    )

    response = analyze_incident_with_agent(request, request_id)
    processing_time_ms = int((perf_counter() - started_at) * 1000)

    logger.info(
        "request_completed",
        extra={
            "request_id": request_id,
            "service_name": request.service_name,
            "environment": request.environment,
            "processing_time_ms": processing_time_ms,
            "validation_success": True,
        },
    )

    return response
