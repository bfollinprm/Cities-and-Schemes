# Contributing — Threads

A thread is one dangling arc. One file per thread, one row per thread in [README.md](README.md). Files are flat under `60-Threads/` — no subfolders.

## File shape

```
---
name: <thread-slug>
description: <one-line summary — who owes what to whom, or what's unanswered>
status: open | dormant | resolved
introduced: session_<N> / week_<W>
owed_by: <faction or NPC slug>
owed_to: <faction or NPC slug>
due: <when it likely matures — week, condition, or "open">
---

# <Thread title>

<2-4 sentences of context. Link to the canonical pages where the thread originated and any subsequent appearances. Do not restate detail that already lives on those pages — link out.>

## See also
- <links to the canonical session, faction `activity/`, or place `events.md` files>
```

Slugs use kebab-case and should make the thread identifiable from the index alone (`fey-bargains-elia-bror`, not `bargains`).

## Index

[README.md](README.md) is a single table — one row per thread. Add or remove rows as threads open or resolve. Keep `Owed by` / `Owed to` / `Status` / `Due` aligned with the file's frontmatter.

## When to open a thread

When something concrete is left unresolved that a future scene might pick up: a debt owed, a question the party asked that has no answer yet, an NPC's hidden knowledge of the party, a piece of intel the party holds that hasn't been spent. Threads are not for prose flavor or generic future possibilities — only for items the party (or an NPC against the party) could plausibly cash in.

## Graduation

A thread graduates when it resolves: the resolution lands in `40-Timeline/`, `20-Factions/<faction>/activity/`, or `30-Places/<location>/events.md` as appropriate. Mark the thread `status: resolved` and link the resolution from `## See also`, or delete the file and remove its row from the index. Either is fine; prefer deletion for routine resolutions, prefer the resolved-with-link form when the thread shaped multiple weeks.
