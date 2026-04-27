---
name: setting-contributing
description: Layout convention for the Setting folder.
---

# Contributing — Setting

## Layout

```
history/         # dated events at world-visible scale; per-event files when warranted
polities/        # institutional frameworks (alliances, government systems)
peoples/         # demographic groups and diasporas
economy/         # cost-of-living, market mechanics, commercial reference
cosmology.md     # planar / divine framework when needed
```

## Boundary with neighbors

- **40-Timeline/** owns the canonical chronology and per-week event files. `10-Setting/history/` holds the *story* of an event (causes, consequences, structure); `40-Timeline/` holds the *date* and the one-line summary.
- **30-Places/** owns geography. Setting describes the institution; Places describes the building it occupies.
- **20-Factions/** owns prose for a faction. Setting describes the *system* a faction belongs to (e.g., the Worshipful Company framework lives here; each WC's character lives in its faction folder).

## Conventions

- Each markdown file under 500 words.
- Frontmatter on every content file: `name` + `description`.
- Per-folder `README.md` indexes its contents.
