# Gizmo Architecture

Project started: 2026-07-02

## Mission

Gizmo is the invisible butler of our home.

Gizmo takes care of the people living in the house, their needs, and the running matters of everyday life.

Gizmo remembers, records, organizes, reminds, and maintains long-term information.

Gizmo does not automate the house.

## Responsibility split

### Gizmo

Gizmo takes care of people.

Examples:

- subscriptions
- wine cellar
- notes
- decisions
- routines
- reminders
- warranties
- maintenance records
- important household knowledge

### Home Assistant

Home Assistant takes care of the house.

Examples:

- lights
- heating
- sensors
- alarms
- devices
- automations
- real-time state

### Alexa

Alexa is the primary voice interface.

Alexa communicates with Home Assistant and, later, Gizmo.

### ChatGPT

ChatGPT is a conversational interface.

ChatGPT does not own Gizmo's data.

## Core architecture

```text
Gizmo
├── Gizmo Core
├── MariaDB
├── REST API
├── Modules
│   ├── Subscriptions
│   ├── Wine Cellar
│   ├── Notes
│   ├── Calendar
│   └── Instructions
└── Integrations
    ├── ChatGPT
    ├── Home Assistant
    ├── Alexa
    └── Google Calendar
```

## Primary datastore

MariaDB is Gizmo's primary datastore.

Google Sheets and Google Drive may be used as views, exports, or transitional tools, but they are not the primary source of truth.

## First target

The first technical milestone is:

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
