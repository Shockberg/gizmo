# Gizmo Home Assistant Add-on

Gizmo is the invisible butler of our home.

## Version

0.3.0 - Database Core

## Endpoints

```http
GET /
GET /status
GET /health
GET /about
GET /database/status
```

## Purpose

This version adds MariaDB connection configuration and a database status check.

It does not yet create tables or store household data.
