from pydantic import BaseModel


class Settings(BaseModel):
    name: str = "Gizmo"
    version: str = "0.1.0"
    environment: str = "development"


settings = Settings()
