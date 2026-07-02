FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml /app/
RUN pip install --no-cache-dir fastapi "uvicorn[standard]" pydantic

COPY backend /app/backend

EXPOSE 8000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
