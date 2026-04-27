"""Wire up plain-text mentions of place names to their canonical files.

For each (entity name, target path) pair, walks the corpus and replaces the
**first** unlinked mention of the entity name in each file with a markdown link
to the target. Skips occurrences that are:

- Already inside a markdown link (`[Name]` or `](Name`)
- Inside a heading line (`# Name`)
- Inside the target file itself

Intended to run after triage of `90-Stubs/places/` to resolve the proper-noun
references the auto-stub generator surfaced.

Usage:
    uv run python src/ingest/wire_place_refs.py
"""

from __future__ import annotations

import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Search these top-level directories for mentions.
SEARCH_DIRS: tuple[str, ...] = (
    "00-Campaign-Frame",
    "10-Setting",
    "20-Factions",
    "30-Places",
    "40-Timeline",
    "50-Sessions",
    "60-Threads",
    "70-Handouts",
)

# (entity name as it appears in prose, target path relative to repo root)
TARGETS: list[tuple[str, str]] = [
    # Existing places (Bucket B)
    ("Gray Harbour", "30-Places/sword-coast/baldurs-gate/lower-city/gray-harbour.md"),
    ("Outer City", "30-Places/sword-coast/baldurs-gate/outer-city/README.md"),
    ("Upper City", "30-Places/sword-coast/baldurs-gate/upper-city/README.md"),
    ("Lower City", "30-Places/sword-coast/baldurs-gate/lower-city/README.md"),
    ("Wyrm's Crossing", "30-Places/sword-coast/baldurs-gate/outer-city/wyrms-crossing.md"),
    ("Temples District", "30-Places/sword-coast/baldurs-gate/upper-city/temples-district.md"),
    ("Undercellar", "30-Places/sword-coast/baldurs-gate/undercity/the-undercellar.md"),
    # New places (Bucket C)
    ("Blushing Mermaid", "30-Places/sword-coast/baldurs-gate/lower-city/blushing-mermaid.md"),
    ("Counting House", "30-Places/sword-coast/baldurs-gate/lower-city/counting-house.md"),
    ("Elfsong Tavern", "30-Places/sword-coast/baldurs-gate/lower-city/elfsong-tavern.md"),
    ("Sorcerous Sundries", "30-Places/sword-coast/baldurs-gate/lower-city/sorcerous-sundries.md"),
    ("Open Hand Temple", "30-Places/sword-coast/baldurs-gate/outer-city/open-hand-temple.md"),
    ("Wyrm's Rock", "30-Places/sword-coast/baldurs-gate/outer-city/wyrms-rock.md"),
    ("Wyrm's Bend Market", "30-Places/sword-coast/baldurs-gate/outer-city/wyrms-bend-market.md"),
    ("Hamhock's Vault", "30-Places/sword-coast/baldurs-gate/undercity/hamhocks-vault.md"),
    ("Hlath Estate", "30-Places/sword-coast/baldurs-gate/upper-city/hlath-estate.md"),
    ("Watchful Shield Shrine", "30-Places/sword-coast/baldurs-gate/upper-city/watchful-shield-shrine.md"),
    ("Whisperwood Copse", "30-Places/sword-coast/baldurs-gate/hinterlands/whisperwood-copse.md"),
    ("Virgin's Square", "30-Places/sword-coast/waterdeep/trades-ward/virgins-square.md"),
    # Faction enclaves (Bucket B → faction summaries)
    ("Gold-Gable Hall", "20-Factions/amnian-kontor/summary.md"),
    ("Gable Hall", "20-Factions/amnian-kontor/summary.md"),
    ("Cogwork Quay", "20-Factions/lantaner-concession/summary.md"),
    ("Splendid Yard", "20-Factions/waterdhavian-kontor/summary.md"),
    # Regional / cosmic places promoted from single-mention name-drops
    ("Ardeep Forest", "30-Places/sword-coast/ardeep-forest.md"),
    ("Misty Forest", "30-Places/sword-coast/misty-forest.md"),
    ("Neverwinter Wood", "30-Places/sword-coast/neverwinter-wood.md"),
    ("Moonshae Isles", "30-Places/sword-coast/moonshae-isles.md"),
    ("Sea of Swords", "10-Setting/regions/sea-of-swords.md"),
    ("House of Wonder", "30-Places/sword-coast/waterdeep/sea-ward/house-of-wonder.md"),
    ("Vault of Dragons", "30-Places/sword-coast/waterdeep/vault-of-dragons.md"),
    ("Astral Sea", "30-Places/astral-sea.md"),
]


def relpath_to_target(source: Path, target_abs: Path) -> str:
    """POSIX-style relative path from source's parent to target."""
    return os.path.relpath(target_abs, start=source.parent).replace(os.sep, "/")


def wire_one_file(source: Path, name: str, target_abs: Path) -> bool:
    """Add a markdown link for the first unlinked mention of *name* in *source*.

    Returns True if the file was modified.
    """
    if source.resolve() == target_abs.resolve():
        return False

    text = source.read_text(encoding="utf-8")

    # Build a regex matching the literal name as a word (not inside an existing
    # markdown link). We look for the name preceded by something that is not
    # `[` (already inside a link label) and not followed by `](` (link label
    # close + URL start).
    escaped = re.escape(name)
    # Negative lookbehind for `[`, negative lookahead for `](`.
    pattern = re.compile(rf"(?<!\[)\b{escaped}\b(?!\]\()")

    lines = text.splitlines(keepends=True)
    rel = relpath_to_target(source, target_abs)
    replacement = f"[{name}]({rel})"

    changed = False
    for i, line in enumerate(lines):
        # Skip headings — don't link inside `# Name` etc.
        if line.lstrip().startswith("#"):
            continue
        # Skip lines that already have a link to this target (idempotency).
        if f"]({rel})" in line:
            continue
        # Skip the first link's already-linked variant (this entity already linked).
        if f"[{name}]" in line:
            continue
        new_line, n = pattern.subn(replacement, line, count=1)
        if n:
            lines[i] = new_line
            changed = True
            break

    if changed:
        source.write_text("".join(lines), encoding="utf-8")
    return changed


def main() -> None:
    total_files = 0
    for name, target_rel in TARGETS:
        target_abs = REPO_ROOT / target_rel
        if not target_abs.exists():
            print(f"SKIP  {name!r}: target {target_rel} does not exist yet")
            continue

        modified: list[Path] = []
        for top in SEARCH_DIRS:
            base = REPO_ROOT / top
            if not base.exists():
                continue
            for path in base.rglob("*.md"):
                if wire_one_file(path, name, target_abs):
                    modified.append(path)

        total_files += len(modified)
        print(f"WIRED {name!r} → {target_rel}: {len(modified)} file(s)")
        for m in modified:
            print(f"   - {m.relative_to(REPO_ROOT)}")

    print(f"\nTotal: {total_files} file(s) modified across {len(TARGETS)} target(s)")


if __name__ == "__main__":
    main()
