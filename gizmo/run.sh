#!/usr/bin/with-contenv bashio

export GIZMO_LOG_LEVEL=$(bashio::config 'log_level')
export GIZMO_TIMEZONE=$(bashio::config 'timezone')

export GIZMO_DB_HOST=$(bashio::config 'database.host')
export GIZMO_DB_PORT=$(bashio::config 'database.port')
export GIZMO_DB_NAME=$(bashio::config 'database.name')
export GIZMO_DB_USERNAME=$(bashio::config 'database.username')
export GIZMO_DB_PASSWORD=$(bashio::config 'database.password')

bashio::log.info "Starting Gizmo..."
bashio::log.info "Gizmo version 0.3.0"
bashio::log.info "Phase: Database Core"
bashio::log.info "Timezone: ${GIZMO_TIMEZONE}"
bashio::log.info "Database host: ${GIZMO_DB_HOST}:${GIZMO_DB_PORT}"
bashio::log.info "Database name: ${GIZMO_DB_NAME}"
bashio::log.info "Listening on port 8000"

cd /app
exec uvicorn main:app --host 0.0.0.0 --port 8000
