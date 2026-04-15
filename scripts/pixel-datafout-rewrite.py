#!/usr/bin/env python3
"""
pixel-datafout-rewrite.py — overschrijft het morning report wanneer de
purchase sanity check faalt. Plakt een waarschuwingsblok bovenaan en
maskeert alle ROAS- en purchase-patronen in de rest van het rapport.

Aangeroepen door scripts/morning-report.sh nadat de hardcoded sanity check
een mismatch detecteert tussen Meta's purchase_value / purchase_count en de
werkelijke SYBB ticketprijs. Deze rewrite mag niet worden overgeslagen:
de sub-claudes die het rapport genereren hebben geen veto over deze stap.

Usage:
    pixel-datafout-rewrite.py <report_file> <purchase_value> <purchase_count> <per_purchase>
"""

import re
import sys
from pathlib import Path


def build_warning_block(pv: str, pc: str, per: str) -> str:
    return (
        "> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**\n"
        f"> Waarde per purchase: **EUR {per}** bij {pc} purchases "
        f"(totaal EUR {pv}).\n"
        "> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW "
        "/ EUR 423,50 incl BTW.\n"
        "> Geldige ranges per purchase (15% marge): "
        "EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), "
        "EUR 892-1465 (3 tickets), etc.\n"
        "> Purchase aantal en ROAS in onderstaand rapport zijn "
        "overschreven met `? (verifieer Wix)` en `n.v.t. (pixel datafout)`.\n"
        "> **Verifieer het echte aantal purchases handmatig in Wix orders.**\n"
        "\n"
    )


def mask_roas_and_purchases(text: str) -> str:
    # ROAS waarden: "60,95x", "299,8x", "ROAS 60.95x", "**ROAS 299,8x**"
    text = re.sub(
        r"\*{0,2}\s*ROAS\s*[:|]?\s*\*{0,2}\d+[.,]?\d*\s*x\*{0,2}",
        "ROAS n.v.t. (pixel datafout)",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\*{0,2}\d+[.,]?\d*\s*x\s*ROAS\*{0,2}",
        "ROAS n.v.t. (pixel datafout)",
        text,
        flags=re.IGNORECASE,
    )
    # Losse "X,Yx" of "X.Yx" in tabelcellen (geen woord-boundary ervoor nodig
    # want deze pattern is specifiek genoeg: minstens 1 digit, punt/komma,
    # digit(s), x).
    text = re.sub(
        r"(?<![A-Za-z])\d+[.,]\d+\s*x\b",
        "n.v.t. (pixel datafout)",
        text,
    )
    # "299,8x ROAS" / "60.95x ROAS" zonder de ROAS prefix
    text = re.sub(
        r"\b\d+[.,]\d+\s*x\b",
        "n.v.t.",
        text,
    )

    # Purchase waarden met expliciete EUR revenue: "2 (EUR 42.773,50)",
    # "**2 (EUR 42.773,50)**", "| 2 | EUR 42.773,50 |"
    text = re.sub(
        r"\*{0,2}\d+\s*\(\s*EUR\s*[\d.]+,\d{2}\s*\)\*{0,2}",
        "? (verifieer Wix)",
        text,
    )

    # "N purchases" / "N purchase" in prose
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
    if len(sys.argv) != 5:
        print(
            "usage: pixel-datafout-rewrite.py "
            "<report_file> <purchase_value> <purchase_count> <per_purchase>",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[1])
    pv, pc, per = sys.argv[2], sys.argv[3], sys.argv[4]

    if not path.exists():
        print(f"[pixel-datafout-rewrite] {path} bestaat niet", file=sys.stderr)
        return 1

    original = path.read_text(encoding="utf-8")
    masked = mask_roas_and_purchases(original)
    warning = build_warning_block(pv, pc, per)

    lines = masked.split("\n", 1)
    if lines and lines[0].startswith("# "):
        head = lines[0]
        rest = lines[1] if len(lines) > 1 else ""
        new_text = f"{head}\n\n{warning}{rest}"
    else:
        new_text = f"{warning}{masked}"

    path.write_text(new_text, encoding="utf-8")
    print(
        f"[pixel-datafout-rewrite] {path} overschreven "
        f"(pv=EUR {pv} pc={pc} per=EUR {per})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
