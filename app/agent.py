from app.agent_runtime.fallback import build_fallback_response
from app.agent_runtime.langchain_agent import run_langchain_agent
from app.logging_config import get_logger
from app.schemas import IncidentAnalysisResponse, IncidentRequest
from app.settings import settings

logger = get_logger(__name__)


def analyze_incident_with_agent(
    request: IncidentRequest, request_id: str
) -> IncidentAnalysisResponse:
    logger.info(
        "agent_started",
        extra={
            "request_id": request_id,
            "service_name": request.service_name,
            "environment": request.environment,
            "incident_length": len(request.incident),
        },
    )

    if _should_use_fallback():
        response = build_fallback_response(request)
        _log_agent_finished(request, request_id, response)
        return response

    try:
        response = run_langchain_agent(request)
    except Exception as exc:
        logger.exception(
            "agent_failed_using_fallback",
            extra={
                "request_id": request_id,
                "service_name": request.service_name,
                "environment": request.environment,
                "error_message": str(exc),
            },
        )
        response = build_fallback_response(request)

    _log_agent_finished(request, request_id, response)
    return response


def _should_use_fallback() -> bool:
    return not settings.openai_api_key or settings.openai_api_key == "your_real_key_here"


def _log_agent_finished(
    request: IncidentRequest,
    request_id: str,
    response: IncidentAnalysisResponse,
) -> None:
    logger.info(
        "agent_finished",
        extra={
            "request_id": request_id,
            "service_name": request.service_name,
            "environment": request.environment,
            "tools_called": response.tools_used,
            "validation_success": True,
        },
    )
