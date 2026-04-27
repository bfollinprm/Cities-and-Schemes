# Contributing

Conventions for adding to this knowledge store.

## File organization

- Store new information in well-organized markdown files.
- Each folder contains a `README.md` that states the folder's theme and carries an index of its contents, with a short (~120 character) summary per entry. Update the index when files are added, renamed, or deleted.
- Each folder may also contain a `CONTRIBUTING.md` describing its layout conventions (slug rules, per-entry file shape, etc.). Consult it before adding new files.

## File size

- Each markdown file should be under 500 words.
- Consider ways to break larger files apart as you write into them, preserving connections through hyperlinks.

### When a file bloats, promote it to a subfolder

If a topic page or `README.md` index grows past ~500 words because the topic itself is growing, **promote it to a subfolder** rather than letting the file bloat:

- A topic file `foo.md` becomes `foo/README.md` plus child files (`foo/<aspect>.md`) split along the topic's natural seams.
- An index `README.md` whose entry list is the source of bloat is a signal to **group entries**: introduce a child subfolder for the most numerous category and move those entries into its own `README.md` index.
- Keep cross-references working: every link in the old file should resolve to the new path after the split.

Index files (`README.md`) may run a little over 500 words when the index itself is the content (one-line entries per item). Topic prose files should not.

## Places

- Higher-level geographic concepts are first-class subjects, not just container folders. Regions, cities, districts, and individual sites can each have their own markdown files alongside nested subfolders.

## Proper-noun landing pages

**Every proper noun gets a landing page in the right place.** When you mention a named person, faction, or location for the first time — or import one from a dossier — create its page before merging. Don't ship references that point at nothing.

Choose the home by *what kind of thing it is*, not by where it was first mentioned:

- **Factions (`20-Factions/<slug>/`)** — for important people, organizations, or entities whose agency spans locations. Major NPCs (Open Lord, Archduke, faction leaders, recurring antagonists) live under `20-Factions/<faction>/people/` because they belong to a faction first; the faction is the structural home. A drow mercenary company that operates in three cities goes here, not under any one city.
- **Places (`30-Places/<region>/<city>/...`)** — for locations and geography: regions, cities, wards, districts, individual sites. Standalone locations get their own file or folder; sites inside a parent location nest underneath it.
- **NPCs under places** — minor characters introduced in a specific location (a tavern keeper, a dock-ward fence, a one-scene Magister) live alongside the location that introduced them: e.g., `30-Places/<region>/<city>/<district>/<site>/<npc-slug>.md`. If a minor NPC turns out to span locations, promote them to a faction's `people/` folder.

Rule of thumb: **if the entity is most naturally referenced by what it does**, it's a faction or faction-person. **If it's most naturally referenced by where it is**, it's a place or place-NPC. When in doubt, prefer a faction home — promotion from place to faction is easy; the reverse loses cross-cutting context.

Cross-link, don't duplicate. The landing page is the single source of truth; everything else references it. When you create a new page, update the parent folder's `README.md` index and add backlinks from any pre-existing prose that named the entity.
