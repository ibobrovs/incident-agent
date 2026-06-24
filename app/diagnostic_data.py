from app.schemas import IncidentType


SERVICE_HEALTH_DATA = {
    "payment-api": {
        "status": "degraded",
        "latency_ms": 1200,
        "error_rate": 0.18,
    },
    "auth-api": {
        "status": "healthy",
        "latency_ms": 180,
        "error_rate": 0.01,
    },
    "gateway-api": {
        "status": "degraded",
        "latency_ms": 850,
        "error_rate": 0.08,
    },
}


DEFAULT_SERVICE_HEALTH = {
    "status": "unknown",
    "latency_ms": 0,
    "error_rate": 0.0,
}


KNOWN_ISSUES = [
    "Database connection pool exhausted after deployment",
    "Migration caused slow queries",
    "Service timeout due to PostgreSQL lock contention",
    "Gateway timeout caused by upstream service latency",
    "Authentication failures after token validation changes",
]


RECENT_DEPLOYMENTS = {
    "payment-api": {
        "last_deployment": "2026-06-12T10:15:00Z",
        "version": "1.4.2",
        "status": "completed",
    },
    "auth-api": {
        "last_deployment": "2026-06-11T08:30:00Z",
        "version": "2.1.0",
        "status": "completed",
    },
    "gateway-api": {
        "last_deployment": "2026-06-10T16:45:00Z",
        "version": "3.0.7",
        "status": "completed",
    },
}


DEFAULT_DEPLOYMENT = {
    "last_deployment": None,
    "version": "unknown",
    "status": "unknown",
}


REMEDIATION_ACTIONS = {
    IncidentType.database_timeout: [
        "Check database connection pool configuration",
        "Review recent deployment changes",
        "Review slow queries",
        "Check recent migrations",
        "Inspect PostgreSQL locks",
    ],
    IncidentType.deployment_failure: [
        "Review recent deployment changes",
        "Check deployment logs",
        "Verify environment variables",
        "Rollback deployment if errors continue",
    ],
    IncidentType.network_issue: [
        "Check network latency",
        "Verify DNS resolution",
        "Inspect load balancer status",
        "Check firewall rules",
    ],
    IncidentType.auth_issue: [
        "Check authentication provider availability",
        "Review token validation errors",
        "Verify recent permission changes",
        "Inspect failed login logs",
    ],
    IncidentType.unknown: [
        "Collect more logs",
        "Check service health",
        "Review recent changes",
        "Escalate to human operator",
    ],
}