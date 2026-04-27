# Contributing — Setting

The Setting folder holds *evergreen* setting matter — cosmic structure, planar geography, regional concepts, and macro-political bodies — kept distinct from the **physical** geography in `30-Places/` and the **acting** organizations in `20-Factions/`.

## The four splits

```
cosmology/      # planar physics, cosmic powers, fey courts, the Weave, the Far Realm
  realms/       # non-Material planes treated as places (Feywild, Shadowfell, etc.)
regions/        # the *concept* of a region (the Sword Coast as a setting, not a map)
polities/       # kingdom- and alliance-level powers (Lords' Alliance, Sembia, Amn)
```

Only create the subfolders you need; the four are presented together so every new entry has an obvious home.

## What goes where

- **cosmology/** — cosmic powers, planar physics, court structures of the immortal/extraplanar. Entities here are *not* factions in the campaign sense; they shape the world but don't usually act on the Sword Coast directly.
- **cosmology/realms/** — non-Material planes as *settings* (history, climate, who rules, what it costs to enter). If a single site within a realm matters as a *place*, it can also be linked from `30-Places/` once it intersects the Material Plane.
- **regions/** — the Sword Coast (or another macro-region) as a *concept*: its history, its psyche, its sustained conflicts. Distinct from `30-Places/sword-coast/`, which holds the geography.
- **polities/** — kingdom-tier powers that aren't acting *in* Baldur's Gate or Waterdeep day-to-day. Their local embassies and trading houses live in `20-Factions/` (e.g. `amnian-kontor`).

## Cross-references

- A cosmic power that gets a mortal-side agent → cross-link from `cosmology/<entity>.md` to `20-Factions/<faction>/summary.md`.
- A planar realm with a Material-Plane crossing → cross-link from `cosmology/realms/<realm>.md` to `30-Places/<region>/<location>.md`.

## File shape

- Frontmatter (`name`, `description`) on every content file.
- Under 500 words. Split when a topic outgrows that.
- Each folder carries a `README.md` index.
