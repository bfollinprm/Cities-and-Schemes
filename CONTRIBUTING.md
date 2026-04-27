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
