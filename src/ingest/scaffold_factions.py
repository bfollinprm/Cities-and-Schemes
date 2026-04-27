"""Scaffold 20-Factions/<slug>/ folders with stub summary.md and rebuild the index.

Idempotent: existing summary.md files are left untouched, only missing folders
and stubs are created. The README index is always rewritten from FACTIONS.

Usage:
    uv run python src/ingest/scaffold_factions.py
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTIONS_DIR = REPO_ROOT / "20-Factions"

# (slug, display name, group, aka, one-line description)
FACTIONS: list[tuple[str, str, str, str, str]] = [
    # Foreign Kontors
    ("amnian-kontor", "Amnian Kontor", "Foreign Kontors", "The Gold-Gable Hall",
     "Slice of a mighty mercantile empire dominating Baldur's Gate through banking, debt, and southern luxuries."),
    ("waterdhavian-kontor", "Waterdhavian Kontor", "Foreign Kontors", "The Splendid Yard",
     "Lords' Alliance embassy controlling trade in northern goods and magical items; espionage hub."),
    ("sembian-kontor", "Sembian Kontor", "Foreign Kontors", "The Iron Ledger",
     "Ruthlessly utilitarian Sembian trading house brokering bulk goods and mercenary contracts."),
    ("lantaner-concession", "Lantaner Concession", "Foreign Kontors", "The Cogwork Quay",
     "Secretive gnomish enclave with a state-sanctioned monopoly on smokepowder."),
    # Native Consortiums
    ("chionthar-consortium", "Chionthar Consortium", "Native Consortiums", "",
     "Old-money Baldurian merchant bloc controlling river trade along the Chionthar."),
    ("western-gate-trading-company", "Western Gate Trading Company", "Native Consortiums", "",
     "Patriar-backed consortium controlling overland routes and hinterland resources; led by the sitting Archduke."),
    # Government / Legislature
    ("council-of-four", "Council of Four", "Government", "",
     "Plutocratic executive branch; a boardroom of capitalists led by the Archduke."),
    ("parliament-of-peers", "Parliament of Peers", "Government", "",
     "Bicameral legislature comprising the Peerage of Coin and the Peerage of Blood."),
    ("peerage-of-coin", "Peerage of Coin", "Government", "",
     "New-money house where corporate entities buy seats and laws are drafted on economic self-interest."),
    ("peerage-of-blood", "Peerage of Blood", "Government", "",
     "Old-money house representing patriar families fighting to preserve traditional rights."),
    ("flaming-fist", "Flaming Fist", "Government", "",
     "Diminished and corrupt city military and police force, struggling for relevance."),
    # Watch
    ("watch", "The Watch", "Watch", "Upper City Watch",
     "Patriar-funded watch policing the Upper City; chronically stretched thin."),
    # Worshipful Companies
    ("wc-shipwrights-calkers", "Worshipful Company of Shipwrights & Calkers", "Worshipful Companies", "",
     "Most powerful guild, controlling the city's vital shipbuilding and repair industry."),
    ("wc-masons-sculptors", "Worshipful Company of Masons & Sculptors", "Worshipful Companies", "",
     "Wealthy guild that rebuilt Baldur's Gate post-crisis; near-monopoly on construction."),
    ("wc-vintners-brewers", "Worshipful Company of Vintners & Brewers", "Worshipful Companies", "",
     "Guild controlling alcohol trade from cheap ale to imported wine; key to social life."),
    ("wc-mercers-clothiers", "Worshipful Company of Mercers & Clothiers", "Worshipful Companies", "",
     "Arbiters of fashion and status; fine clothing for the city's elite."),
    ("wc-goldsmiths-jewelers", "Worshipful Company of Goldsmiths & Jewelers", "Worshipful Companies", "",
     "Regulators of precious metals and gems; the city's unofficial mint and assay office."),
    ("wc-alchemists-apothecaries", "Worshipful Company of Alchemists & Apothecaries", "Worshipful Companies", "",
     "Secretive guild controlling potions, antitoxins, and other exotic substances."),
    ("wc-fishmongers", "Worshipful Company of Fishmongers", "Worshipful Companies", "",
     "Ancient guild controlling Gray Harbour fishing fleets; food supply leverage."),
    ("wc-smiths-armorers", "Worshipful Company of Smiths & Armorers", "Worshipful Companies", "",
     "Guild forging arms and armor for the city's guards, soldiers, and adventurers."),
    ("wc-cartographers-surveyors", "Worshipful Company of Cartographers & Surveyors", "Worshipful Companies", "",
     "Essential guild whose seal is required on every land deed; closely guarded sewer maps."),
    ("wc-butchers-tanners", "Worshipful Company of Butchers & Tanners", "Worshipful Companies", "",
     "Wealthy but socially disdained guild controlling food and leather production."),
    ("wc-chandlers-lamplighters", "Worshipful Company of Chandlers & Lamplighters", "Worshipful Companies", "",
     "Provides oil, candles, and torches; lamplighter crews know the city's nightly rhythms."),
    ("wc-sorcerous-sodality", "Sorcerous Sodality", "Worshipful Companies", "Sorcerous Sundries",
     "Reformed Sorcerous Sundries; regulates magical goods and licenses public spellcasting."),
    # Societies / Underworld
    ("guild", "The Guild", "Societies", "",
     "Sophisticated criminal syndicate evolved into the de facto government of the common folk."),
    ("zhentarim", "Zhentarim", "Societies", "Black Network",
     "Ruthless profit-driven criminal network seeking to supplant the Guild."),
    ("harpers", "The Harpers", "Societies", "",
     "Semi-secret balance-keepers gathering intelligence and subtly intervening against corrupt powers."),
    ("circle-of-the-inner-grove", "Circle of the Inner Grove", "Societies", "",
     "Druidic sect protecting the Chionthar from the city's pollution and industrial expansion."),
    ("bibliophile", "The Bibliophile", "Societies", "",
     "Information broker (Nansi Gretta) selling intel to the highest bidder."),
    # Smuggler Cells
    ("river-rats", "River-Rats", "Smuggler Cells", "",
     "Sewer-and-river smuggling crew operating beneath the Brampton district under Silas the Eel."),
    ("wharf-rats", "Wharf Rats", "Smuggler Cells", "",
     "Dockside smuggling crew under One-Eyed Jack, working the Gray Harbour."),
    # Refugee / Frontier
    ("hellriders-of-new-elturel", "Hellriders of New Elturel", "Refugee / Frontier", "",
     "Volunteer militia and informal government of the New Elturel refugee district."),
    ("unchained", "The Unchained", "Refugee / Frontier", "K'liir",
     "Githyanki exiles loyal to Prince Orpheus, training in the Outer City for war against Vlaakith."),
    ("free-traders-of-the-outskirts", "Free Traders of the Outskirts", "Refugee / Frontier", "",
     "Independent caravan masters of the Outer City under 'Mad' Meggan; mutual-protection pact."),
    # Remnant Costers
    ("iron-throne", "Iron Throne", "Remnant Costers", "",
     "Remnant coster with shadowy, anonymous leadership; clinging to relevance after consortium ascendance."),
    ("seven-suns", "Seven Suns", "Remnant Costers", "",
     "Remnant coster led by the Jhasso family; fortunes dwindling after Calimshan trade losses."),
    ("high-moon-coster", "High Moon Coster", "Remnant Costers", "",
     "Remnant coster led by the Oberon family; bankrolling adventurers in hopes of restoring fortunes."),
    # Patriar Bloc
    ("patriar-heritage-society", "Patriar Heritage Society", "Patriar Bloc", "",
     "Nativist patriar club organizing the Peerage of Blood as a unified voting bloc."),
    ("knights-of-the-shield", "Knights of the Shield", "Patriar Bloc", "",
     "Resurgent diabolist secret society recruiting dispossessed patriars in exchange for infernal pacts."),
    # Press
    ("baldurs-mouth", "Baldur's Mouth", "Press", "",
     "The city's broadsheet, edited by Ettvard Needle; for-hire front-page coverage."),
    # Conspiracy Cells
    ("unveiled", "The Unveiled", "Conspiracy Cells", "",
     "Conspiracy-paladin cell convinced the Absolute Crisis was a doppelganger false-flag."),
    ("elturel-remembrance-society", "Elturel Remembrance Society", "Conspiracy Cells", "",
     "Elturian-survivor support group radicalized into hunting 'infernal' Baldurian merchants."),
    ("purified", "The Purified", "Conspiracy Cells", "",
     "Paranoid cell convinced Lantaner gnomes are pacifying the city through clockwork nano-organisms."),
    ("society-of-baldurian-integrity", "Society of Baldurian Integrity", "Conspiracy Cells", "",
     "Cultural-purity zealots warring against 'memetic contamination' from foreign art and architecture."),
    # Cults
    ("gilded-vein", "The Gilded Vein", "Cults", "",
     "Cult of economic assassins worshipping 'Axiom,' purifying the economy through targeted chaos."),
    ("plague-of-remembrance", "The Plague of Remembrance", "Cults", "",
     "Xenophobic death cult of Baldurian purists framing Elturian refugees to start a civil war."),
    ("hands-of-the-absolute", "Hands of the Absolute", "Cults", "",
     "Splinter cult listening for the 'Echo' of the Netherbrain in the city's psychic substrate."),
    ("carnival-of-whispers", "The Carnival of Whispers", "Cults", "",
     "Fey-pact cult using illusion and abduction to harvest emotional residue for their patron."),
    ("takers-of-the-tithe", "The Takers of the Tithe", "Cults", "",
     "Reaper-cult assassins claiming master artisans as a 'tithe' to their patron."),
    ("cult-of-the-returning-lord", "Cult of the Returning Lord", "Cults", "Bhaal",
     "Bhaal-worshipping death cult consecrating sewer altars with the blood of 'nobodies'."),
    ("silent-shroud", "The Silent Shroud", "Cults", "Shar",
     "Sharran cult seeking the lost sanctums of the Lady of Loss beneath the city."),
    ("followers-of-the-phoenix", "Followers of the Phoenix", "Cults", "",
     "Karlach-worshipping cult of righteous fury, growing among tieflings and outcasts in New Elturel."),
    ("gravekeepers", "The Gravekeepers", "Cults", "",
     "Undead-cleansing cult under Hemlock, warding the city's graveyards against psychic intrusions."),
    # Party
    ("party", "The Party", "Party", "",
     "The player characters."),
]


SUMMARY_STUB = dedent("""\
    ---
    name: {slug}
    description: {desc}
    ---

    # {display}{aka_line}

    _(stub — fill from `raw-ingest/cloaks-and-conspiracies/factions.docx` and the public-factions paste at `.context/attachments/`.)_

    ## Ideology

    ## Membership

    ## Methods

    ## Hooks and Relationships

    ## See also
    """)


def render_readme(folder: Path, display: str, aka: str, desc: str) -> str:
    """Build a per-folder README that indexes the files actually present."""
    aka_line = f" *(aka {aka})*" if aka else ""
    lines = [f"# {display}{aka_line}", "", desc, "", "## Index", ""]
    entries: list[tuple[str, str]] = []

    summary = folder / "summary.md"
    if summary.exists():
        entries.append(("summary.md", "Faction overview: ideology, membership, methods, hooks."))

    people = folder / "people"
    if people.is_dir():
        names = sorted(p.stem for p in people.glob("*.md") if p.name != "README.md")
        if names:
            entries.append(("people/", f"Named figures: {', '.join(names)}."))
        else:
            entries.append(("people/", "Named figures (empty)."))

    associations = folder / "associations"
    if associations.is_dir():
        names = sorted(p.stem for p in associations.glob("*.md") if p.name != "README.md")
        label = ", ".join(names) if names else "empty"
        entries.append(("associations/", f"Items, holdings, vehicles ({label})."))

    activity = folder / "activity"
    if activity.is_dir():
        weeks = sorted(p.name for p in activity.iterdir() if p.is_dir())
        label = ", ".join(weeks) if weeks else "empty"
        entries.append(("activity/", f"Ongoing actions by week ({label})."))

    for path, summary_line in entries:
        lines.append(f"- [{path}]({path}) — {summary_line}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    FACTIONS_DIR.mkdir(exist_ok=True)
    slugs = [f[0] for f in FACTIONS]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    for slug, display, _group, aka, desc in FACTIONS:
        folder = FACTIONS_DIR / slug
        folder.mkdir(exist_ok=True)
        summary = folder / "summary.md"
        if not summary.exists():
            aka_line = f" *(aka {aka})*" if aka else ""
            summary.write_text(
                SUMMARY_STUB.format(slug=slug, desc=desc, display=display, aka_line=aka_line),
                encoding="utf-8",
            )
            print(f"  stub  {slug}/summary.md")
        # README is always rebuilt to reflect current file inventory.
        (folder / "README.md").write_text(
            render_readme(folder, display, aka, desc), encoding="utf-8"
        )
        rebuild_subfolder_readmes(folder, display)

    rebuild_readme()


SUBFOLDER_THEMES = {
    "people": ("Named figures", "Named figure"),
    "associations": ("Items, holdings, and vehicles the faction guards", "Holding"),
    "activity": ("Ongoing actions, organized by in-game week", "Week"),
}


def rebuild_subfolder_readmes(folder: Path, display: str) -> None:
    for sub, (theme, _label) in SUBFOLDER_THEMES.items():
        sub_path = folder / sub
        if not sub_path.is_dir():
            continue
        lines = [f"# {display} — {sub}", "", theme + ".", "", "## Index", ""]
        if sub == "activity":
            weeks = sorted(p for p in sub_path.iterdir() if p.is_dir())
            for w in weeks:
                actions = sorted(p.stem for p in w.glob("*.md") if p.name != "README.md")
                label = ", ".join(actions) if actions else "empty"
                lines.append(f"- [{w.name}/]({w.name}/) — {label}.")
                # week-level README
                w_lines = [f"# {display} — activity — {w.name}", "", f"Actions taken in {w.name}.", "", "## Index", ""]
                for a in actions:
                    w_lines.append(f"- [{a}.md]({a}.md)")
                w_lines.append("")
                (w / "README.md").write_text("\n".join(w_lines), encoding="utf-8")
        else:
            entries = sorted(p.stem for p in sub_path.glob("*.md") if p.name != "README.md")
            for e in entries:
                lines.append(f"- [{e}.md]({e}.md)")
            if not entries:
                lines.append("_(empty)_")
        lines.append("")
        (sub_path / "README.md").write_text("\n".join(lines), encoding="utf-8")


def rebuild_readme() -> None:
    by_group: dict[str, list[tuple[str, str, str, str]]] = {}
    for slug, display, group, aka, desc in FACTIONS:
        by_group.setdefault(group, []).append((slug, display, aka, desc))

    group_order = [
        "Foreign Kontors", "Native Consortiums", "Government", "Watch",
        "Worshipful Companies", "Societies", "Smuggler Cells",
        "Refugee / Frontier", "Remnant Costers", "Patriar Bloc",
        "Press", "Conspiracy Cells", "Cults", "Party",
    ]

    body = [
        "# Factions",
        "",
        "Powerful people or groups acting on their own machinations. The party lives here too.",
        "",
        "See [CONTRIBUTING.md](CONTRIBUTING.md) for the per-faction file layout and slug rules.",
        "",
        "## Index",
        "",
    ]
    for group in group_order:
        if group not in by_group:
            continue
        body.append(f"### {group}")
        body.append("")
        for slug, display, aka, desc in sorted(by_group[group]):
            aka_part = f" *({aka})*" if aka else ""
            body.append(f"- [{display}{aka_part}]({slug}/summary.md) — {desc}")
        body.append("")

    (FACTIONS_DIR / "README.md").write_text("\n".join(body), encoding="utf-8")
    print(f"  rewrote {FACTIONS_DIR / 'README.md'}")


if __name__ == "__main__":
    main()
