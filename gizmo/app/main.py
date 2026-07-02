from fastapi import FastAPI

app = FastAPI(
    title="Gizmo",
    description="The invisible butler of our home.",
    version="0.1.0",
)


@app.get("/status")
def get_status() -> dict[str, str]:
    return {
        "name": "Gizmo",
        "version": "0.1.0",
        "status": "running",
    }
