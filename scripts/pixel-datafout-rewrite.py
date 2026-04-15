#!/usr/bin/env python3
"""
pixel-datafout-rewrite.py — overschrijft het morning report wanneer de
purchase sanity check iets anders dan PASS oplevert. Plakt een
waarschuwingsblok bovenaan en maskeert ROAS-patronen in het rapport.

Twee modes (mutually exclusive):
  datafout   — Hard mismatch: per-purchase waarde past niet bij de SYBB
               ticketprijs. Het aantal purchases in Meta klopt dus niet.
  unverified — Fail-closed: we konden geen purchase data ophalen of
               parsen uit de Meta Ads MCP. Liever een false warning dan
               een foutieve ROAS die budget beslissingen beïnvloedt.

Aangeroepen door scripts/morning-report.sh nadat de hardcoded sanity check
het verdict bepaalt. Deze rewrite mag niet worden overgeslagen: de
sub-claudes die het rapport genereren hebben geen veto over deze stap.

Usage:
    pixel-datafout-rewrite.py <mode> <report_file> <purchase_value> <purchase_count> <per_purchase>

    mode = "datafout" | "unverified"
"""

import re
import sys
from pathlib import Path


def build_datafout_warning(pv: str, pc: str, per: str) -> str:
    return (
        "> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**\n"
        f"> Waarde per purchase: **EUR {per}** bij {pc} purchases "
        f"(totaal EUR {pv}).\n"
        "> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW "
        "/ EUR 423,50 incl BTW.\n"
        "> Geldige ranges per purchase (15% marge): "
        "EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), "
        "EUR 892-1465 (3 tickets), etc.\n"
        "> ROAS is overschreven met `n.v.t. (pixel datafout)`. "
        "Purchase aantal in prose als `? purchases (verifieer Wix)`.\n"
        "> **Verifieer het echte aantal purchases handmatig in Wix orders.**\n"
        "\n"
    )


def build_unverified_warning() -> str:
    return (
        "> ⚠️ **PURCHASE DATA KON NIET GEVERIFIEERD WORDEN**\n"
        "> De hardcoded sanity check kon geen purchase_value / purchase_count "
        "ophalen uit de Meta Ads MCP (NODATA of PARSE_ERROR).\n"
        "> Dit rapport bevat mogelijk niet-gevalideerde purchase cijfers. "
        "Behandel alle purchase getallen en ROAS als **onbetrouwbaar** "
        "tot je ze handmatig in Wix hebt geverifieerd.\n"
        "> ROAS is uit voorzorg overschreven met `n.v.t. (niet geverifieerd)`. "
        "Purchase aantallen zijn niet geraakt — de tabellen tonen wat Meta "
        "rapporteerde, maar die cijfers zijn niet gecheckt tegen de "
        "ticketprijs (EUR 350 ex BTW / EUR 423,50 incl BTW).\n"
        "> **Beter een false warning dan een foutieve ROAS die budget "
        "beslissingen beïnvloedt.**\n"
        "\n"
    )


def mask_roas_and_purchases(text: str, mode: str) -> str:
    """Maskeer ROAS en (optioneel) purchase prose in de rapport tekst.

    mode = "datafout"   → ROAS label "n.v.t. (pixel datafout)",
                          purchase prose "? purchases (verifieer Wix)"
    mode = "unverified" → ROAS label "n.v.t. (niet geverifieerd)",
                          purchase prose blijft ongemoeid (we weten niet
                          of de getallen fout zijn, we weten alleen dat ze
                          niet geverifieerd konden worden — de warning
                          bovenaan maakt dat duidelijk)
    """
    if mode == "datafout":
        roas_label = "ROAS n.v.t. (pixel datafout)"
        bare_label = "n.v.t. (pixel datafout)"
    else:  # unverified
        roas_label = "ROAS n.v.t. (niet geverifieerd)"
        bare_label = "n.v.t. (niet geverifieerd)"

    # ROAS waarden: "60,95x", "299,8x", "ROAS 60.95x", "**ROAS 299,8x**"
    text = re.sub(
        r"\*{0,2}\s*ROAS\s*[:|]?\s*\*{0,2}\d+[.,]?\d*\s*x\*{0,2}",
        roas_label,
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\*{0,2}\d+[.,]?\d*\s*x\s*ROAS\*{0,2}",
        roas_label,
        text,
        flags=re.IGNORECASE,
    )
    # Losse "X,Yx" of "X.Yx" in tabelcellen (geen woord-boundary ervoor nodig
    # want deze pattern is specifiek genoeg: minstens 1 digit, punt/komma,
    # digit(s), x).
    text = re.sub(
        r"(?<![A-Za-z])\d+[.,]\d+\s*x\b",
        bare_label,
        text,
    )

    # Purchase prose alleen bij datafout — bij unverified laten we de
    # getallen staan omdat we niet weten of ze fout zijn, we weten alleen
    # dat we ze niet konden checken. De warning block zegt dat expliciet.
    if mode == "datafout":
        text = re.sub(
            r"\*{0,2}\d+\s*\(\s*EUR\s*[\d.]+,\d{2}\s*\)\*{0,2}",
            "? (verifieer Wix)",
            text,
        )
        text = re.sub(
            r"\b\d+\s+purchases?\b",
            "? purchases (verifieer Wix)",
            text,
            flags=re.IGNORECASE,
        )

    # Tabelrijen van het type "| Purchases | 2 | EUR ... |" kunnen niet
    # veilig met regex worden aangepast zonder ook header-rijen te breken
    # (bijv. "| Purchases | Revenue |" waarbij Revenue de volgende kolom-
    # header is). De waarschuwing bovenaan + de ROAS / prose masking
    # maken voldoende duidelijk dat de tabelcijfers niet betrouwbaar zijn.

    return text


def main() -> int:
    if len(sys.argv) != 6:
        print(
            "usage: pixel-datafout-rewrite.py <mode> "
            "<report_file> <purchase_value> <purchase_count> <per_purchase>\n"
            "  mode = datafout | unverified",
            file=sys.stderr,
        )
        return 2

    mode = sys.argv[1]
    if mode not in ("datafout", "unverified"):
        print(
            f"[pixel-rewrite] onbekende mode: {mode!r} "
            "(verwacht 'datafout' of 'unverified')",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[2])
    pv, pc, per = sys.argv[3], sys.argv[4], sys.argv[5]

    if not path.exists():
        print(f"[pixel-rewrite] {path} bestaat niet", file=sys.stderr)
        return 1

    original = path.read_text(encoding="utf-8")
    masked = mask_roas_and_purchases(original, mode)

    if mode == "datafout":
        warning = build_datafout_warning(pv, pc, per)
    else:
        warning = build_unverified_warning()

    lines = masked.split("\n", 1)
    if lines and lines[0].startswith("# "):
        head = lines[0]
        rest = lines[1] if len(lines) > 1 else ""
        new_text = f"{head}\n\n{warning}{rest}"
    else:
        new_text = f"{warning}{masked}"

    path.write_text(new_text, encoding="utf-8")
    print(
        f"[pixel-rewrite] mode={mode} {path} overschreven "
        f"(pv=EUR {pv} pc={pc} per=EUR {per})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
