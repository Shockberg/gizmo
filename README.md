# Gizmo

The invisible butler of our home.

Gizmo remembers, records, organizes, reminds, and maintains long-term household information.

Gizmo does not automate the house. Home Assistant takes care of the house. Gizmo takes care of the people.

## First milestone

Run the backend and open:

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
