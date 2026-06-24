from app.agent_runtime.langchain_tools import langchain_tools
from app.agent_runtime.prompts import SYSTEM_PROMPT
from app.schemas import IncidentAnalysisResponse, IncidentRequest
from app.settings import settings


def run_langchain_agent(request: IncidentRequest) -> IncidentAnalysisResponse:
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI

    model = ChatOpenAI(
        model=settings.model_name,
        api_key=settings.openai_api_key,
        temperature=0,
    )

    agent = create_agent(
        model=model,
        tools=langchain_tools,
        system_prompt=SYSTEM_PROMPT,
        response_format=IncidentAnalysisResponse,
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": _build_user_message(request),
                }
            ]
        }
    )

    return result["structured_response"]


def _build_user_message(request: IncidentRequest) -> str:
    return (
        "Analyze this incident report. "
        f"service_name={request.service_name}; "
        f"environment={request.environment}; "
        f"incident={request.incident}"
    )