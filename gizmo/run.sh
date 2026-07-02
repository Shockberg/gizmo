#!/usr/bin/with-contenv bashio

bashio::log.info "Starting Gizmo..."
bashio::log.info "Gizmo version 0.1.0"
bashio::log.info "Listening on port 8000"

cd /app
exec uvicorn main:app --host 0.0.0.0 --port 8000
