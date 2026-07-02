#!/usr/bin/with-contenv bashio

export GIZMO_LOG_LEVEL=$(bashio::config 'log_level')
export GIZMO_TIMEZONE=$(bashio::config 'timezone')

bashio::log.info "Starting Gizmo..."
bashio::log.info "Gizmo version 0.2.0"
bashio::log.info "Phase: Foundation Core"
bashio::log.info "Timezone: ${GIZMO_TIMEZONE}"
bashio::log.info "Listening on port 8000"

cd /app
exec uvicorn main:app --host 0.0.0.0 --port 8000
