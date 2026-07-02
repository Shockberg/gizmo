from datetime import datetime, timezone
import os
from typing import Any

import pymysql
from fastapi import FastAPI

GIZMO_NAME = "Gizmo"
GIZMO_VERSION = "0.3.0"
GIZMO_PHASE = "Database Core"
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


def database_config() -> dict[str, Any]:
    return {
        "host": os.getenv("GIZMO_DB_HOST", "core-mariadb"),
        "port": int(os.getenv("GIZMO_DB_PORT", "3306")),
        "database": os.getenv("GIZMO_DB_NAME", "gizmo"),
        "user": os.getenv("GIZMO_DB_USERNAME", "gizmo"),
        "password": os.getenv("GIZMO_DB_PASSWORD", ""),
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
        "connect_timeout": 3,
        "read_timeout": 3,
        "write_timeout": 3,
    }


def check_database() -> dict[str, Any]:
    cfg = database_config()

    if not cfg["password"]:
        return {
            "status": "not_configured",
            "host": cfg["host"],
            "port": cfg["port"],
            "database": cfg["database"],
            "message": "Database password is not configured.",
        }

    try:
        connection = pymysql.connect(**cfg)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE() AS database_name, VERSION() AS server_version")
                row = cursor.fetchone()
            return {
                "status": "connected",
                "host": cfg["host"],
                "port": cfg["port"],
                "database": row.get("database_name"),
                "server_version": row.get("server_version"),
            }
        finally:
            connection.close()
    except Exception as exc:
        return {
            "status": "error",
            "host": cfg["host"],
            "port": cfg["port"],
            "database": cfg["database"],
            "error": str(exc),
        }


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "message": "Gizmo is running. See /status, /health, /about, or /database/status.",
    }


@app.get("/status")
def get_status() -> dict[str, object]:
    db = check_database()

    return {
        "name": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "phase": GIZMO_PHASE,
        "status": "running",
        "started_at": STARTED_AT.isoformat(),
        "uptime_seconds": uptime_seconds(),
        "environment": "home-assistant-addon",
        "database": db["status"],
        "calendar": "not_configured",
    }


@app.get("/health")
def get_health() -> dict[str, object]:
    db = check_database()

    return {
        "status": "healthy" if db["status"] in ["connected", "not_configured"] else "degraded",
        "service": GIZMO_NAME,
        "version": GIZMO_VERSION,
        "timestamp": utc_now_iso(),
        "uptime_seconds": uptime_seconds(),
        "database": db["status"],
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
            "log_level": os.getenv("GIZMO_LOG_LEVEL", "info"),
            "database_host": os.getenv("GIZMO_DB_HOST", "core-mariadb"),
            "database_name": os.getenv("GIZMO_DB_NAME", "gizmo"),
        }
    }


@app.get("/database/status")
def get_database_status() -> dict[str, object]:
    return check_database()
