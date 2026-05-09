# Contributing — Timeline

## Layout

```
calendar.md          # canonical week_0 anchor
week_N/
  paper.md   OR  paper/      # paper/ when split per-section (front page, corrections, city pages, etc.)
  events.md  OR  events/     # events/ when split per-section
```

A week's `events.md` may be split into a subfolder once the topic outgrows a single file:

```
week_N/events/
  README.md            # frontmatter, lede, ## Sections index, ## See also
  <slug>.md            # one file per ## section in the original events.md
  from-pc-actions.md   # always this slug for the "From PC actions" section
```

## Slug rules for split sections

- Lowercase, dash-separated, derived from the section heading.
- Drop em-dash subclauses ("Foo — bar baz" → `foo`).
- Drop apostrophes; collapse non-alphanumeric runs to a single dash.
- The "From PC actions" section is always `from-pc-actions.md`.

## File size

- Per the root `CONTRIBUTING.md`, target ~500 words / ~2,000 chars per file; ~5,000 chars is a soft limit.
- Per-week `from-pc-actions.md` files may run over the soft limit when the in-session narrative does not have a clean internal seam — splitting mid-scene is worse than running long.
