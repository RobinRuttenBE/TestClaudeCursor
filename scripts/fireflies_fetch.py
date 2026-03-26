#!/usr/bin/env python3
"""
Fireflies.ai Transcript Fetcher voor Sempertex Europe Knowledge Base
=====================================================================
Dit script haalt meeting transcripts op via de Fireflies GraphQL API,
verwerkt ze en slaat ze op als markdown-bestanden in de kennisbase.

Gebruik:
  python fireflies_fetch.py                    # Haal nieuwe transcripts op (laatste 7 dagen)
  python fireflies_fetch.py --days 30          # Laatste 30 dagen
  python fireflies_fetch.py --id <transcript_id>  # Specifiek transcript
  python fireflies_fetch.py --list             # Toon beschikbare transcripts
  python fireflies_fetch.py --all              # Alles ophalen

Vereisten:
  - pip install requests python-dateutil
  - FIREFLIES_API_KEY environment variable (of in .env bestand)

Setup:
  1. Ga naar https://app.fireflies.ai/integrations
  2. Klik op "Fireflies API"
  3. Kopieer je API key
  4. export FIREFLIES_API_KEY="jouw_api_key_hier"
"""

import requests
import json
import os
import sys
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ============================================================
# CONFIGURATIE
# ============================================================

API_URL = "https://api.fireflies.ai/graphql"
API_KEY = os.environ.get("FIREFLIES_API_KEY", "")

# Output directory - pas aan naar jouw kennisbase pad
OUTPUT_DIR = Path("kennis/content/transcripts")

# Optioneel: pad naar een samenvattingen-map
SUMMARIES_DIR = Path("kennis/content/meeting-summaries")


# ============================================================
# GRAPHQL QUERIES
# ============================================================

QUERY_LIST_TRANSCRIPTS = """
query ListTranscripts($limit: Int, $skip: Int) {
  transcripts(limit: $limit, skip: $skip) {
    id
    title
    date
    duration
    organizer_email
    participants
    host_email
  }
}
"""

QUERY_TRANSCRIPT_DETAIL = """
query GetTranscript($id: String!) {
  transcript(id: $id) {
    id
    title
    date
    duration
    organizer_email
    host_email
    participants
    transcript_url
    sentences {
      index
      speaker_name
      speaker_id
      text
      raw_text
      start_time
      end_time
    }
    summary {
      keywords
      action_items
      outline
      shorthand_bullet
      overview
    }
  }
}
"""


# ============================================================
# API HELPER
# ============================================================

def fireflies_request(query: str, variables: dict = None) -> dict:
    """Stuur een GraphQL request naar Fireflies API."""
    if not API_KEY:
        print("❌ FIREFLIES_API_KEY niet gevonden.")
        print("   Stel in met: export FIREFLIES_API_KEY='jouw_key'")
        print("   Of maak een .env bestand aan.")
        sys.exit(1)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "errors" in data:
            print(f"❌ GraphQL errors: {json.dumps(data['errors'], indent=2)}")
            sys.exit(1)

        return data.get("data", {})

    except requests.exceptions.RequestException as e:
        print(f"❌ API request mislukt: {e}")
        sys.exit(1)


# ============================================================
# TRANSCRIPT VERWERKING
# ============================================================

def format_duration(seconds: float) -> str:
    """Converteer seconden naar leesbaar formaat."""
    if not seconds:
        return "onbekend"
    minutes = int(seconds) // 60
    secs = int(seconds) % 60
    if minutes >= 60:
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours}u {mins}m"
    return f"{minutes}m {secs}s"


def format_timestamp(ms: float) -> str:
    """Converteer milliseconden naar MM:SS formaat."""
    if not ms:
        return "00:00"
    total_seconds = int(ms / 1000)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def transcript_to_markdown(transcript: dict) -> str:
    """Converteer een Fireflies transcript naar een markdown-bestand."""
    t = transcript
    date_str = ""
    if t.get("date"):
        # Fireflies date is Unix timestamp in milliseconds
        try:
            dt = datetime.fromtimestamp(int(t["date"]) / 1000, tz=timezone.utc)
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_str = str(t.get("date", ""))

    summary = t.get("summary") or {}
    sentences = t.get("sentences") or []
    participants = t.get("participants") or []

    lines = []

    # --- YAML-achtige frontmatter ---
    lines.append(f"# {t.get('title', 'Untitled Meeting')}")
    lines.append("")
    lines.append(f"- **Datum**: {date_str}")
    lines.append(f"- **Duur**: {format_duration(t.get('duration'))}")
    lines.append(f"- **Organisator**: {t.get('organizer_email', 'onbekend')}")
    if participants:
        lines.append(f"- **Deelnemers**: {', '.join(participants)}")
    lines.append(f"- **Fireflies ID**: {t.get('id', '')}")
    if t.get("transcript_url"):
        lines.append(f"- **Link**: {t['transcript_url']}")
    lines.append("")

    # --- SAMENVATTING ---
    if summary.get("overview"):
        lines.append("## Samenvatting")
        lines.append("")
        lines.append(summary["overview"])
        lines.append("")

    # --- KEY TOPICS / OUTLINE ---
    if summary.get("outline"):
        lines.append("## Onderwerpen")
        lines.append("")
        lines.append(summary["outline"])
        lines.append("")

    # --- ACTION ITEMS ---
    if summary.get("action_items"):
        lines.append("## Actiepunten")
        lines.append("")
        lines.append(summary["action_items"])
        lines.append("")

    # --- KEYWORDS ---
    if summary.get("keywords"):
        lines.append("## Keywords")
        lines.append("")
        if isinstance(summary["keywords"], list):
            lines.append(", ".join(summary["keywords"]))
        else:
            lines.append(str(summary["keywords"]))
        lines.append("")

    # --- BULLET SUMMARY ---
    if summary.get("shorthand_bullet"):
        lines.append("## Bullet Samenvatting")
        lines.append("")
        lines.append(summary["shorthand_bullet"])
        lines.append("")

    # --- VOLLEDIGE TRANSCRIPT ---
    if sentences:
        lines.append("---")
        lines.append("")
        lines.append("## Volledig Transcript")
        lines.append("")

        current_speaker = None
        for sentence in sentences:
            speaker = sentence.get("speaker_name", "Onbekend")
            text = sentence.get("text", "").strip()
            timestamp = format_timestamp(sentence.get("start_time"))

            if not text:
                continue

            if speaker != current_speaker:
                lines.append("")
                lines.append(f"**{speaker}** [{timestamp}]:")
                current_speaker = speaker

            lines.append(f"> {text}")

    lines.append("")
    return "\n".join(lines)


def save_transcript(transcript: dict, output_dir: Path) -> Path:
    """Sla een transcript op als markdown bestand."""
    output_dir.mkdir(parents=True, exist_ok=True)

    t = transcript
    date_str = "undated"
    if t.get("date"):
        try:
            dt = datetime.fromtimestamp(int(t["date"]) / 1000, tz=timezone.utc)
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            pass

    # Maak bestandsnaam: YYYY-MM-DD_meeting-title.md
    title = t.get("title", "untitled")
    safe_title = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
    safe_title = safe_title.strip().replace(" ", "-").lower()[:60]
    filename = f"{date_str}_{safe_title}.md"

    filepath = output_dir / filename
    content = transcript_to_markdown(t)

    filepath.write_text(content, encoding="utf-8")
    return filepath


# ============================================================
# CLI COMMANDS
# ============================================================

def cmd_list(args):
    """Toon beschikbare transcripts."""
    print("📋 Beschikbare transcripts ophalen...\n")

    data = fireflies_request(QUERY_LIST_TRANSCRIPTS, {
        "limit": args.limit or 20,
        "skip": 0,
    })

    transcripts = data.get("transcripts", [])
    if not transcripts:
        print("Geen transcripts gevonden.")
        return

    for t in transcripts:
        date_str = ""
        if t.get("date"):
            try:
                dt = datetime.fromtimestamp(int(t["date"]) / 1000, tz=timezone.utc)
                date_str = dt.strftime("%Y-%m-%d %H:%M")
            except (ValueError, TypeError):
                date_str = "?"

        duration = format_duration(t.get("duration"))
        print(f"  [{t['id']}]")
        print(f"    📝 {t.get('title', 'Untitled')}")
        print(f"    📅 {date_str} | ⏱  {duration}")
        print(f"    👤 {t.get('organizer_email', '?')}")
        print()


def cmd_fetch(args):
    """Haal transcripts op en sla op."""
    output_dir = Path(args.output) if args.output else OUTPUT_DIR

    if args.id:
        # Specifiek transcript ophalen
        print(f"📥 Transcript {args.id} ophalen...")
        data = fireflies_request(QUERY_TRANSCRIPT_DETAIL, {"id": args.id})
        transcript = data.get("transcript")
        if not transcript:
            print(f"❌ Transcript {args.id} niet gevonden.")
            return
        filepath = save_transcript(transcript, output_dir)
        print(f"✅ Opgeslagen: {filepath}")
        return

    # Lijst ophalen en filteren op datum
    print(f"📥 Transcripts ophalen (laatste {args.days} dagen)...\n")

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    cutoff_ms = int(cutoff.timestamp() * 1000)

    all_transcripts = []
    skip = 0
    limit = 50

    while True:
        data = fireflies_request(QUERY_LIST_TRANSCRIPTS, {
            "limit": limit,
            "skip": skip,
        })
        batch = data.get("transcripts", [])
        if not batch:
            break

        for t in batch:
            if t.get("date") and int(t["date"]) >= cutoff_ms:
                all_transcripts.append(t)
            elif t.get("date") and int(t["date"]) < cutoff_ms:
                # Transcripts zijn chronologisch, stop als we voorbij de cutoff zijn
                batch = []  # Force outer loop to break
                break

        if len(batch) < limit:
            break
        skip += limit

    if not all_transcripts:
        print(f"Geen nieuwe transcripts gevonden in de laatste {args.days} dagen.")
        return

    print(f"📋 {len(all_transcripts)} transcripts gevonden. Details ophalen...\n")

    saved = []
    for t in all_transcripts:
        print(f"  ⏳ {t.get('title', 'Untitled')}...")
        detail = fireflies_request(QUERY_TRANSCRIPT_DETAIL, {"id": t["id"]})
        transcript = detail.get("transcript")
        if transcript:
            filepath = save_transcript(transcript, output_dir)
            saved.append(filepath)
            print(f"  ✅ {filepath}")
        else:
            print(f"  ❌ Kon details niet ophalen voor {t['id']}")

    print(f"\n🎉 {len(saved)} transcripts opgeslagen in {output_dir}/")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Fireflies.ai Transcript Fetcher voor STX EU Knowledge Base"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commando's")

    # List command
    list_parser = subparsers.add_parser("list", help="Toon beschikbare transcripts")
    list_parser.add_argument("--limit", type=int, default=20, help="Max aantal (default: 20)")

    # Fetch command
    fetch_parser = subparsers.add_parser("fetch", help="Haal transcripts op en sla op")
    fetch_parser.add_argument("--days", type=int, default=7, help="Laatste N dagen (default: 7)")
    fetch_parser.add_argument("--id", type=str, help="Specifiek transcript ID")
    fetch_parser.add_argument("--all", action="store_true", help="Alle transcripts ophalen")
    fetch_parser.add_argument("--output", type=str, help="Output directory (default: kennis/content/transcripts)")

    args = parser.parse_args()

    # Default: fetch als geen command gegeven
    if not args.command:
        args.command = "fetch"
        args.days = 7
        args.id = None
        args.all = False
        args.output = None

    if args.command == "list":
        cmd_list(args)
    elif args.command == "fetch":
        if hasattr(args, "all") and args.all:
            args.days = 3650  # ~10 jaar
        cmd_fetch(args)


if __name__ == "__main__":
    main()
