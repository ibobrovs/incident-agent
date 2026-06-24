from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


ShortText = Annotated[str, Field(min_length=1, max_length=300)]
LongText = Annotated[str, Field(min_length=10, max_length=3000)]
ActionText = Annotated[str, Field(min_length=3, max_length=300)]
ToolName = Annotated[str, Field(min_length=3, max_length=100)]


class Environment(StrEnum):
    production = "production"
    staging = "staging"
    development = "development"


class Severity(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class IncidentType(StrEnum):
    database_timeout = "database_timeout"
    deployment_failure = "deployment_failure"
    network_issue = "network_issue"
    auth_issue = "auth_issue"
    unknown = "unknown"


class IncidentRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    service_name: ShortText
    environment: Environment
    incident: LongText


class IncidentAnalysisResponse(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    service_name: ShortText
    severity: Severity
    incident_type: IncidentType
    summary: LongText
    likely_cause: LongText
    tools_used: list[ToolName] = Field(min_length=1, max_length=10)
    recommended_actions: list[ActionText] = Field(min_length=1, max_length=10)
    needs_human_review: bool