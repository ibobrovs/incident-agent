from dataclasses import dataclass

from app.schemas import IncidentType


@dataclass(frozen=True)
class IncidentRule:
    incident_type: IncidentType
    keywords: tuple[str, ...]


INCIDENT_TYPE_RULES: tuple[IncidentRule, ...] = (
    IncidentRule(
        incident_type=IncidentType.database_timeout,
        keywords=(
            "database",
            "postgres",
            "postgresql",
            "sql",
            "db",
            "database timeout",
            "postgres timeout",
            "postgresql timeout",
            "connection pool",
            "slow query",
            "lock contention",
        ),
    ),
    IncidentRule(
        incident_type=IncidentType.deployment_failure,
        keywords=(
            "deployment",
            "deploy",
            "release",
            "rollback",
            "migration",
            "version",
        ),
    ),
    IncidentRule(
        incident_type=IncidentType.network_issue,
        keywords=(
            "network",
            "dns",
            "gateway",
            "gateway timeout",
            "load balancer",
            "connection refused",
        ),
    ),
    IncidentRule(
        incident_type=IncidentType.auth_issue,
        keywords=(
            "auth",
            "token",
            "login",
            "permission",
            "unauthorized",
            "forbidden",
            "401",
            "403",
        ),
    ),
)


CRITICAL_KEYWORDS: tuple[str, ...] = (
    "critical",
    "outage",
    "service down",
    "system down",
    "all users",
    "unavailable",
    "complete failure",
)
