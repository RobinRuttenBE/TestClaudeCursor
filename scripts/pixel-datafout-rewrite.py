#!/usr/bin/env python3
"""
pixel-datafout-rewrite.py — hardcoded post-processing voor morning report.

Vier soorten hardcoded fixes, in deze volgorde:

1. Purchase sanity warning (alleen bij datafout of unverified):
   Plakt PIXEL DATAFOUT of NIET GEVERIFIEERD block bovenaan en maskeert
   ROAS + purchase prose.

2. Campagne link metric rewrite (altijd behalve bij unverified):
   Vervangt kale `| CTR | X |` en `| CPC | Y |` rijen in campagne-summary
   tabellen door de hardcoded link_ctr / link_cpc. Plakt ook LINK METRICS
   block bovenaan met bron cijfers.

3. Daily spend rewrite (altijd behalve bij unverified):
   Vervangt `€X/dag`, `Gem. dagspend: €X` patterns door de correcte
   `€X/dag over Y actieve dagen` waarde. Voorkomt dat sub-claudes
   `total_spend / 30` rapporteren voor campagnes die slechts een deel
   van de periode actief waren.

4. Per-ad link metric rewrite (altijd behalve bij unverified):
   Voor elke ad in de per-ad data: zoek tabelrijen die de ad identifier
   (H11, H12, ...) bevatten en vervang percentage waarden (CTR) en EUR
   waarden < 10 (CPC, niet spend) met de hardcoded per-ad link metrics.
   Plakt ook een Per-ad link metrics tabel in het LINK METRICS block.

Modes:
  linkfix    — Happy path. Alle link-rewrites, geen sanity warning.
  datafout   — Link-rewrites + PIXEL DATAFOUT warning + ROAS/prose mask.
  unverified — Alleen NIET GEVERIFIEERD warning + ROAS mask. Geen link
               rewrites want we hebben geen link data.

Usage:
    pixel-datafout-rewrite.py <mode> <report_file> \\
        <purchase_value> <purchase_count> <per_purchase> \\
        <spend> <impressions> <link_clicks> <link_ctr> <link_cpc> \\
        <active_days> <avg_daily_spend> <data_json_path>
"""

import json
import re
import sys
from pathlib import Path


# --------------------------------------------------------------------------
# Formatters
# --------------------------------------------------------------------------

def _fmt_eur(value: str) -> str:
    try:
        return f"{float(value):.2f}".replace(".", ",")
    except ValueError:
        return str(value)


def _fmt_pct(value: str) -> str:
    try:
        return f"{float(value):.2f}".replace(".", ",")
    except ValueError:
        return str(value)


def _fmt_int(value: str) -> str:
    try:
        return f"{int(float(value)):,}".replace(",", ".")
    except ValueError:
        return str(value)


def _fmt_cpc_compact(value: float) -> str:
    return f"{value:.2f}".replace(".", ",")


# --------------------------------------------------------------------------
# Warning blocks
# --------------------------------------------------------------------------

def build_datafout_warning(pv: str, pc: str, per: str) -> str:
    return (
        "> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**\n"
        f"> Waarde per purchase: **EUR {_fmt_eur(per)}** bij {pc} purchases "
        f"(totaal EUR {_fmt_eur(pv)}).\n"
        "> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW "
        "/ EUR 423,50 incl BTW.\n"
        "> Geldige ranges per purchase (10% marge, max 5 tickets): "
        "EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), "
        "EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).\n"
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
    active_days: str, avg_daily_spend: str,
    ads: list,
) -> str:
    lines = [
        "> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**",
        f"> - **Link CTR: {_fmt_pct(link_ctr)}%** "
        "(link_clicks ÷ impressions × 100)",
        f"> - **CPC (link): EUR {_fmt_eur(link_cpc)}** "
        "(spend ÷ link_clicks)",
    ]

    try:
        adays = int(float(active_days))
    except ValueError:
        adays = 0
    if adays > 0:
        lines.append(
            f"> - **Gem. dagspend: EUR {_fmt_eur(avg_daily_spend)}** "
            f"over {adays} actieve dagen (niet totaal/30)"
        )

    lines.append(
        f"> - Bron: spend EUR {_fmt_eur(spend)} · "
        f"impressions {_fmt_int(impressions)} · "
        f"link_clicks {_fmt_int(link_clicks)}"
    )

    if ads:
        lines.append("> ")
        lines.append("> **Per-ad link metrics (hardcoded):**")
        lines.append("> ")
        lines.append("> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |")
        lines.append("> |---|---|---|---|---|---|")
        for ad in ads:
            ad_name = ad.get("name", "?")
            ad_spend = ad.get("spend", 0) or 0
            ad_imp = ad.get("impressions", 0) or 0
            ad_lc = ad.get("link_clicks", 0) or 0
            ad_ctr = (ad_lc / ad_imp * 100) if ad_imp > 0 else 0.0
            ad_cpc = (ad_spend / ad_lc) if ad_lc > 0 else 0.0
            lines.append(
                f"> | {ad_name} | EUR {_fmt_eur(str(ad_spend))} | "
                f"{_fmt_int(str(ad_imp))} | {_fmt_int(str(ad_lc))} | "
                f"{_fmt_pct(str(ad_ctr))}% | EUR {_fmt_eur(str(ad_cpc))} |"
            )

    lines.append(
        "> "
        "\n"
        "> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit "
        "rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn "
        "waar mogelijk hardcoded overschreven."
    )
    lines.append("")

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Masking helpers
# --------------------------------------------------------------------------

def mask_roas_and_purchases(text: str, mode: str) -> str:
    if mode == "datafout":
        roas_label = "ROAS n.v.t. (pixel datafout)"
        bare_label = "n.v.t. (pixel datafout)"
    else:  # unverified
        roas_label = "ROAS n.v.t. (niet geverifieerd)"
        bare_label = "n.v.t. (niet geverifieerd)"

    text = re.sub(
        r"\*{0,2}\s*ROAS\s*[:|]?\s*\*{0,2}\d+[.,]?\d*\s*x\*{0,2}",
        roas_label, text, flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\*{0,2}\d+[.,]?\d*\s*x\s*ROAS\*{0,2}",
        roas_label, text, flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(?<![A-Za-z])\d+[.,]\d+\s*x\b",
        bare_label, text,
    )

    if mode == "datafout":
        text = re.sub(
            r"\*{0,2}\d+\s*\(\s*EUR\s*[\d.]+,\d{2}\s*\)\*{0,2}",
            "? (verifieer Wix)", text,
        )
        text = re.sub(
            r"\b\d+\s+purchases?\b",
            "? purchases (verifieer Wix)", text, flags=re.IGNORECASE,
        )

    return text


def rewrite_campaign_link_metrics(text: str, link_ctr: str, link_cpc: str) -> str:
    """Overschrijf single-metric tabelrijen `| CTR | X |` / `| CPC | Y |`."""
    ctr_replacement = f"| Link CTR | {_fmt_pct(link_ctr)}% |"
    cpc_replacement = f"| CPC (link) | EUR {_fmt_eur(link_cpc)} |"
    text = re.sub(
        r"(?m)^\|\s*\*{0,2}CTR\*{0,2}\s*\|\s*[^|]*\s*\|\s*$",
        ctr_replacement, text,
    )
    text = re.sub(
        r"(?m)^\|\s*\*{0,2}CPC\*{0,2}\s*\|\s*[^|]*\s*\|\s*$",
        cpc_replacement, text,
    )
    return text


def rewrite_daily_spend(text: str, avg_daily_spend: str, active_days: str) -> str:
    """Vervang `€X/dag`, `Gem. dagspend: €X` en varianten door de correcte
    waarde berekend over active_days.

    Doet niets als active_days == 0 (dan hebben we geen valide deler)."""
    try:
        adays = int(float(active_days))
        avg_float = float(avg_daily_spend)
    except ValueError:
        return text
    if adays <= 0 or avg_float <= 0:
        return text

    avg_str = _fmt_eur(avg_daily_spend)

    # Patroon 1: "EUR X/dag" of "€X/dag"
    text = re.sub(
        r"(?:EUR|€)\s*\d+[.,]\d+\s*/\s*dag",
        f"EUR {avg_str}/dag ({adays} actieve dagen)",
        text,
    )
    # Patroon 2: "Gem. dagspend EUR X,XX" / "gemiddelde (dag)spend EUR X,XX"
    text = re.sub(
        r"(Gem(?:iddelde)?\.?\s*(?:dag)?spend)[:\s]*(?:EUR|€)\s*\d+[.,]\d+",
        lambda m: f"{m.group(1)}: EUR {avg_str} ({adays} actieve dagen)",
        text, flags=re.IGNORECASE,
    )
    # Patroon 3: "daggemiddelde EUR X,XX"
    text = re.sub(
        r"daggemiddelde[:\s]*(?:EUR|€)\s*\d+[.,]\d+",
        f"daggemiddelde: EUR {avg_str} ({adays} actieve dagen)",
        text, flags=re.IGNORECASE,
    )

    return text


def rewrite_per_ad_metrics(text: str, ads: list) -> str:
    """Vervang per-ad CPC/CTR in tabelrijen.

    Heuristiek per ad:
    1. Vind ad identifier (H11, H12, H13, ...) uit de name.
    2. Voor elke regel die met `|` begint en die identifier bevat:
       - Vervang ALLE `X,XX%` waarden door de hardcoded link_ctr.
       - Vervang `EUR X,XX` of `€X,XX` waarden KLEINER dan EUR 10 door de
         hardcoded link_cpc. Waarden >= EUR 10 zijn waarschijnlijk spend
         en blijven staan.

    Deze heuristiek werkt voor de tabellen die sub-claudes typisch
    genereren, waar spend €50+ is en CPC €0.30-€3 is. Het raakt geen
    percentages buiten ad rijen en het raakt geen spend kolommen aan."""
    if not ads:
        return text

    # Map van ad identifier -> (link_ctr_str, link_cpc_str, link_cpc_float)
    ad_lookup: dict = {}
    for ad in ads:
        name = str(ad.get("name", ""))
        m = re.search(r"H\d+", name)
        if not m:
            continue
        short = m.group(0)
        ad_spend = float(ad.get("spend", 0) or 0)
        ad_imp = int(float(ad.get("impressions", 0) or 0))
        ad_lc = int(float(ad.get("link_clicks", 0) or 0))
        if ad_imp <= 0 or ad_lc <= 0:
            continue
        ad_ctr = ad_lc / ad_imp * 100
        ad_cpc = ad_spend / ad_lc
        ad_lookup[short] = {
            "ctr_str": _fmt_pct(str(ad_ctr)) + "%",
            "cpc_str": _fmt_eur(str(ad_cpc)),
            "cpc_float": ad_cpc,
        }

    if not ad_lookup:
        return text

    new_lines = []
    for line in text.split("\n"):
        stripped = line.lstrip()
        if not stripped.startswith("|"):
            new_lines.append(line)
            continue
        # Skip de Per-ad link metrics tabel die wijzelf in de header hebben
        # geplakt (staat binnen een blockquote: `> | ... |`).
        if stripped.startswith("> |"):
            new_lines.append(line)
            continue

        # Zoek welke ad in deze regel voorkomt
        matched_short = None
        for short in ad_lookup:
            if re.search(rf"\b{re.escape(short)}\b", line):
                matched_short = short
                break
        if not matched_short:
            new_lines.append(line)
            continue

        lk = ad_lookup[matched_short]

        # Vervang percent waarden (CTR)
        line = re.sub(
            r"\b\d+[.,]\d+\s*%",
            lk["ctr_str"],
            line,
        )

        # Vervang kleine EUR waarden (< 10) met de CPC
        def _eur_sub(m: re.Match) -> str:
            num = m.group(2).replace(",", ".")
            try:
                val = float(num)
            except ValueError:
                return m.group(0)
            if val >= 10:
                return m.group(0)  # spend, laat staan
            currency = m.group(1)
            return f"{currency} {lk['cpc_str']}"

        line = re.sub(
            r"(EUR|€)\s*(\d+[.,]\d+)",
            _eur_sub,
            line,
        )

        new_lines.append(line)

    return "\n".join(new_lines)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    if len(sys.argv) != 14:
        print(
            "usage: pixel-datafout-rewrite.py <mode> <report_file> "
            "<pv> <pc> <per> <spend> <imp> <lc> <link_ctr> <link_cpc> "
            "<active_days> <avg_daily_spend> <data_json_path>\n"
            "  mode = linkfix | datafout | unverified",
            file=sys.stderr,
        )
        return 2

    mode = sys.argv[1]
    if mode not in ("linkfix", "datafout", "unverified"):
        print(f"[pixel-rewrite] onbekende mode: {mode!r}", file=sys.stderr)
        return 2

    path = Path(sys.argv[2])
    pv, pc, per = sys.argv[3], sys.argv[4], sys.argv[5]
    spend, impressions, link_clicks = sys.argv[6], sys.argv[7], sys.argv[8]
    link_ctr, link_cpc = sys.argv[9], sys.argv[10]
    active_days, avg_daily_spend = sys.argv[11], sys.argv[12]
    data_json_path = Path(sys.argv[13])

    if not path.exists():
        print(f"[pixel-rewrite] {path} bestaat niet", file=sys.stderr)
        return 1

    # Laad per-ad data (mag leeg zijn)
    ads: list = []
    if data_json_path.exists():
        try:
            payload = json.loads(data_json_path.read_text(encoding="utf-8") or "{}")
            ads_raw = payload.get("ads", []) or []
            if isinstance(ads_raw, list):
                ads = ads_raw
        except Exception as exc:
            print(f"[pixel-rewrite] kan ads niet parsen: {exc}", file=sys.stderr)
            ads = []

    text = path.read_text(encoding="utf-8")

    # 1. Sanity masking (alleen datafout/unverified)
    if mode in ("datafout", "unverified"):
        text = mask_roas_and_purchases(text, mode)

    # 2. Campagne link metric rewrite (altijd behalve unverified)
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
        text = rewrite_campaign_link_metrics(text, link_ctr, link_cpc)
        # 3. Daily spend rewrite
        text = rewrite_daily_spend(text, avg_daily_spend, active_days)
        # 4. Per-ad metrics rewrite
        text = rewrite_per_ad_metrics(text, ads)

    # Bouw header blocks
    blocks = []
    if mode == "datafout":
        blocks.append(build_datafout_warning(pv, pc, per))
    elif mode == "unverified":
        blocks.append(build_unverified_warning())

    if do_link_rewrite:
        blocks.append(build_link_metrics_header(
            spend, impressions, link_clicks, link_ctr, link_cpc,
            active_days, avg_daily_spend, ads,
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
        f"avg_daily=EUR{avg_daily_spend}/{active_days}d "
        f"ads={len(ads)} {path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
