#!/usr/bin/env python3
"""
pixel-datafout-rewrite.py — hardcoded post-processing voor morning report.

Doet twee dingen, beide zonder dat een sub-claude er iets over te zeggen
heeft:

1. Link metric rewrite (ALTIJD behalve bij unverified):
   Vervangt kale `CTR` / `CPC` cellen in campagne-summary tabellen door
   de hardcoded link_ctr en link_cpc die bash berekend heeft (uit spend,
   impressions, link_clicks via de narrow JSON fetch). Plakt ook een
   "LINK METRICS" block bovenaan. Reden: sub-claudes negeren de
   "gebruik actions.link_click" regel uit het command herhaaldelijk en
   rapporteren Meta's standaard all-clicks CTR/CPC — die waarden
   beïnvloeden budget beslissingen op basis van verkeerde data.

2. Purchase sanity warning (alleen bij datafout of unverified):
   Plakt een PIXEL DATAFOUT of NIET GEVERIFIEERD block bovenaan en
   maskeert ROAS + purchase prose.

Modes:
  linkfix    — Alleen link metric rewrite. Default happy path.
  datafout   — Link metric rewrite + PIXEL DATAFOUT warning + ROAS/prose
               masking. Per-purchase waarde past niet bij ticketprijs.
  unverified — Alleen NIET GEVERIFIEERD warning + ROAS masking. Geen
               link metric rewrite want we hebben geen link data.

Usage:
    pixel-datafout-rewrite.py <mode> <report_file> \\
        <purchase_value> <purchase_count> <per_purchase> \\
        <spend> <impressions> <link_clicks> <link_ctr> <link_cpc>
"""

import re
import sys
from pathlib import Path


def _fmt_eur(value: str) -> str:
    """Format een numerieke string als EUR met Europese komma."""
    try:
        return f"{float(value):.2f}".replace(".", ",")
    except ValueError:
        return value


def _fmt_pct(value: str) -> str:
    try:
        return f"{float(value):.2f}".replace(".", ",")
    except ValueError:
        return value


def _fmt_int(value: str) -> str:
    try:
        return f"{int(float(value)):,}".replace(",", ".")
    except ValueError:
        return value


def build_datafout_warning(pv: str, pc: str, per: str) -> str:
    return (
        "> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**\n"
        f"> Waarde per purchase: **EUR {_fmt_eur(per)}** bij {pc} purchases "
        f"(totaal EUR {_fmt_eur(pv)}).\n"
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
        "> De hardcoded sanity check kon geen purchase data ophalen uit "
        "de Meta Ads MCP (NODATA of PARSE_ERROR). Dat betekent ook geen "
        "betrouwbare link metrics.\n"
        "> Dit rapport bevat mogelijk niet-gevalideerde cijfers. Behandel "
        "alle purchase getallen, ROAS en CTR/CPC als **onbetrouwbaar** "
        "tot je ze handmatig hebt geverifieerd.\n"
        "> ROAS is uit voorzorg overschreven met `n.v.t. (niet geverifieerd)`.\n"
        "> **Beter een false warning dan een foutieve metric die budget "
        "beslissingen beïnvloedt.**\n"
        "\n"
    )


def build_link_metrics_header(
    spend: str, impressions: str, link_clicks: str,
    link_ctr: str, link_cpc: str,
) -> str:
    return (
        "> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**\n"
        f"> - **Link CTR: {_fmt_pct(link_ctr)}%** "
        "(link_clicks ÷ impressions × 100)\n"
        f"> - **CPC (link): EUR {_fmt_eur(link_cpc)}** "
        "(spend ÷ link_clicks)\n"
        f"> - Bron: spend EUR {_fmt_eur(spend)} · "
        f"impressions {_fmt_int(impressions)} · "
        f"link_clicks {_fmt_int(link_clicks)}\n"
        "> Dit zijn de ENIGE betrouwbare CTR/CPC cijfers in dit rapport. "
        "Kale `CTR`/`CPC` in campagne-summary tabellen zijn overschreven "
        "met de link-based waarden. Per-ad tabellen bevatten mogelijk nog "
        "all-clicks cijfers — controleer dubbel.\n"
        "\n"
    )


def mask_roas_and_purchases(text: str, mode: str) -> str:
    """Maskeer ROAS en (optioneel) purchase prose in de rapport tekst.

    mode = "datafout"   → ROAS label "n.v.t. (pixel datafout)",
                          purchase prose "? purchases (verifieer Wix)"
    mode = "unverified" → ROAS label "n.v.t. (niet geverifieerd)",
                          purchase prose blijft ongemoeid
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
    # Losse "X,Yx" of "X.Yx" in tabelcellen
    text = re.sub(
        r"(?<![A-Za-z])\d+[.,]\d+\s*x\b",
        bare_label,
        text,
    )

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

    return text


def rewrite_link_metrics(text: str, link_ctr: str, link_cpc: str) -> str:
    """Overschrijf kale CTR/CPC cellen in campagne-summary tabellen.

    Targeteert ALLEEN single-metric tabelrijen van de vorm:
        | CTR | 2,0% |
        | CPC | EUR 0,52 |

    Laat multi-column header rijen zoals "| Ad | CPC | CTR | Purch |"
    ongemoeid, want daar zijn CTR/CPC kolom-labels en we hebben geen
    per-ad link data. Die per-ad cellen staan via de LINK METRICS block
    bovenaan gemarkeerd als "mogelijk all-clicks".

    Ook prose patronen zoals "CPC EUR 0,62 ligt boven target" worden
    NIET aangeraakt — te fragile zonder context over welke campagne ze
    refereren. De campagne-summary tabel rewrite dekt het belangrijkste
    geval.
    """
    ctr_replacement = (
        f"| Link CTR | {_fmt_pct(link_ctr)}% |"
    )
    cpc_replacement = (
        f"| CPC (link) | EUR {_fmt_eur(link_cpc)} |"
    )

    # Single-metric row waar de eerste cel EXACT "CTR" is (evt met bold/spaces)
    text = re.sub(
        r"(?m)^\|\s*\*{0,2}CTR\*{0,2}\s*\|\s*[^|]*\s*\|\s*$",
        ctr_replacement,
        text,
    )
    text = re.sub(
        r"(?m)^\|\s*\*{0,2}CPC\*{0,2}\s*\|\s*[^|]*\s*\|\s*$",
        cpc_replacement,
        text,
    )

    return text


def main() -> int:
    if len(sys.argv) != 11:
        print(
            "usage: pixel-datafout-rewrite.py <mode> <report_file> "
            "<purchase_value> <purchase_count> <per_purchase> "
            "<spend> <impressions> <link_clicks> <link_ctr> <link_cpc>\n"
            "  mode = linkfix | datafout | unverified",
            file=sys.stderr,
        )
        return 2

    mode = sys.argv[1]
    if mode not in ("linkfix", "datafout", "unverified"):
        print(
            f"[pixel-rewrite] onbekende mode: {mode!r}",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[2])
    pv, pc, per = sys.argv[3], sys.argv[4], sys.argv[5]
    spend, impressions, link_clicks = sys.argv[6], sys.argv[7], sys.argv[8]
    link_ctr, link_cpc = sys.argv[9], sys.argv[10]

    if not path.exists():
        print(f"[pixel-rewrite] {path} bestaat niet", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")

    # Mask ROAS/purchases alleen bij datafout/unverified
    if mode in ("datafout", "unverified"):
        text = mask_roas_and_purchases(text, mode)

    # Link metric rewrite: altijd behalve bij unverified (dan hebben we
    # geen betrouwbare link data). Check ook of link_clicks > 0 en
    # impressions > 0 — anders zouden we 0% / €0 in het rapport zetten.
    do_link_rewrite = False
    if mode != "unverified":
        try:
            lc = float(link_clicks)
            imp = float(impressions)
            if lc > 0 and imp > 0:
                do_link_rewrite = True
        except ValueError:
            pass

    if do_link_rewrite:
        text = rewrite_link_metrics(text, link_ctr, link_cpc)

    # Bouw de warning blocks voor bovenaan
    blocks = []
    if mode == "datafout":
        blocks.append(build_datafout_warning(pv, pc, per))
    elif mode == "unverified":
        blocks.append(build_unverified_warning())

    if do_link_rewrite:
        blocks.append(build_link_metrics_header(
            spend, impressions, link_clicks, link_ctr, link_cpc,
        ))

    header_block = "".join(blocks)
    if header_block:
        lines = text.split("\n", 1)
        if lines and lines[0].startswith("# "):
            head = lines[0]
            rest = lines[1] if len(lines) > 1 else ""
            text = f"{head}\n\n{header_block}{rest}"
        else:
            text = header_block + text

    path.write_text(text, encoding="utf-8")
    print(
        f"[pixel-rewrite] mode={mode} link_rewrite={do_link_rewrite} "
        f"link_ctr={link_ctr}% link_cpc=EUR{link_cpc} "
        f"{path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
