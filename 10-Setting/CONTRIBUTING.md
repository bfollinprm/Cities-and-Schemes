---
name: setting-contributing
description: Layout convention for the Setting folder.
---

# Contributing — Setting

The Setting folder holds *evergreen* setting matter — cosmic structure, planar geography, regional concepts, and macro-political bodies — kept distinct from the **physical** geography in `30-Places/` and the **acting** organizations in `20-Factions/`.

## Layout

```
cosmology/      # planar physics, cosmic powers, fey courts, the Weave, the Far Realm
  realms/       # non-Material planes treated as places (Feywild, Shadowfell, etc.)
history/        # dated world-visible events; chronology lives in 40-Timeline
polities/       # alliance-, kingdom-, and city-government frameworks (Lords' Alliance, Sword Coast Hansa, Worshipful Company system)
regions/        # region-scale geographic features (Sea of Swords, mountain ranges)
peoples/        # diasporas and demographic groups
economy/        # cost-of-living and commercial reference
```

Only create the subfolders you need.

## What goes where

- **cosmology/** — cosmic powers, planar physics, court structures of the immortal/extraplanar. Entities here shape the world but don't usually act on the Sword Coast directly.
- **cosmology/realms/** — non-Material planes as *settings* (history, climate, who rules, what it costs to enter). If a single site within a realm matters as a *place*, it can also be linked from `30-Places/` once it intersects the Material Plane.
- **history/** — story-level analysis of dated events (causes, structure, consequences). The chronological index lives in `40-Timeline/`; this folder holds the *story*.
- **polities/** — institutional frameworks: trade alliances, government systems, guild structures. Their local embassies and trading houses live in `20-Factions/` (e.g. `amnian-kontor`).
- **peoples/** — diasporas and demographic groups whose identity, history, and politics span beyond a single place.
- **economy/** — cost-of-living and commercial reference. The thematic *what money does in this world* belongs in `00-Campaign-Frame/`.

## Boundary with neighbors

- **40-Timeline/** owns the canonical chronology and per-week event files. `10-Setting/history/` holds the *story* of an event; `40-Timeline/` holds the *date* and the one-line summary.
- **30-Places/** owns geography. Setting describes the institution; Places describes the building it occupies.
- **20-Factions/** owns prose for a faction. Setting describes the *system* a faction belongs to (e.g., the Worshipful Company framework lives here; each WC's character lives in its faction folder).

## Cross-references

- A cosmic power that gets a mortal-side agent → cross-link from `cosmology/<entity>.md` to `20-Factions/<faction>/summary.md`.
- A planar realm with a Material-Plane crossing → cross-link from `cosmology/realms/<realm>.md` to `30-Places/<region>/<location>.md`.

## File shape

- Frontmatter (`name`, `description`) on every content file.
- Under 500 words. Split when a topic outgrows that.
- Each folder carries a `README.md` index.
