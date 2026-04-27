---
name: calendar
description: Canonical anchor for in-game time. Week 0 = indeterminate spring, 1502 DR.
---

# Calendar

## Anchor

- **Week 0** — indeterminate early spring, **1502 DR**. All `week_N` references in this repo are offsets from this anchor.
- Source dossiers (`raw-ingest/cloaks-and-conspiracies/dossier-*.docx`) are dated 1502 DR; week 0 corresponds to their "present."

## Conventions

- Years are written `YYYY DR` (Dale Reckoning).
- In-game time advances in week-sized buckets. A `week_N` folder may contain multiple days' events; sub-day precision is recorded in the file body, not the folder name.
- Sessions reference the in-game week they cover via metadata in `50-Sessions/session_N/README.md`.
