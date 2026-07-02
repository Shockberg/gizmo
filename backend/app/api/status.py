from fastapi import APIRouter

from backend.app.core.settings import settings

router = APIRouter()


@router.get("/status")
def get_status() -> dict[str, str]:
    return {
        "name": settings.name,
        "version": settings.version,
        "status": "running",
    }
