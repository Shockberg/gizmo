from datetime import datetime, timezone
import os

from fastapi import FastAPI

GIZMO_NAME = "Gizmo"
GIZMO_VERSION = "0.2.0"
GIZMO_PHASE = "Foundation Core"
GIZMO_MISSION = "The invisible butler of our home."

STARTED_AT = datetime.now(timezone.utc)

app = FastAPI(
    title=GIZMO_NAME,
    description=GIZMO_MISSION,
    version=GIZMO_VERSION,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def uptime_seconds() -> int:
    return int((datetime.now(timezone.utc) - STARTED_AT).total_seconds())


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "message": "Gizmo is running. See /status, /health, or /about.",
    }


@app.get("/status")
def get_status() -> dict[str, object]:
    return {
        "name": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "phase": GIZMO_PHASE,
        "status": "running",
        "started_at": STARTED_AT.isoformat(),
        "uptime_seconds": uptime_seconds(),
        "environment": "home-assistant-addon",
        "database": "not_configured",
        "calendar": "not_configured",
    }


@app.get("/health")
def get_health() -> dict[str, object]:
    return {
        "status": "healthy",
        "service": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "timestamp": utc_now_iso(),
        "uptime_seconds": uptime_seconds(),
    }


@app.get("/about")
def get_about() -> dict[str, object]:
    return {
        "name": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "phase": GIZMO_PHASE,
        "mission": GIZMO_MISSION,
        "role": "Gizmo takes care of people. Home Assistant takes care of the house.",
        "interfaces": [
            "Home Assistant",
            "ChatGPT",
            "Alexa",
            "Google Calendar"
        ],
        "modules": {
            "subscriptions": "planned",
            "wine_cellar": "planned",
            "notes": "planned",
            "calendar": "planned",
            "instructions": "planned"
        },
        "configuration": {
            "timezone": os.getenv("GIZMO_TIMEZONE", "Europe/Helsinki"),
            "log_level": os.getenv("GIZMO_LOG_LEVEL", "info")
        }
    }
