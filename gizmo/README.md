# Gizmo Home Assistant Add-on

Gizmo is the invisible butler of our home.

This first add-on version only provides a `/status` endpoint.

## Endpoint

```http
GET /status
```

Expected response:

```json
{
  "name": "Gizmo",
  "version": "0.1.0",
  "status": "running"
}
```
