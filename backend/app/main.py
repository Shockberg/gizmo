from fastapi import FastAPI

from backend.app.api.status import router as status_router
from backend.app.core.settings import settings

app = FastAPI(
    title="Gizmo",
    description="The invisible butler of our home.",
    version=settings.version,
)

app.include_router(status_router)
