#!/usr/bin/env python3
"""
verified-funnel.py -- Cross-reference Meta Ads, PostHog sessions en Wix orders.

Produceert een VERIFIED FUNNEL PER AD sectie in het morning report en
detecteert discrepanties tussen Meta pixel purchases en echte Wix orders.

Usage:
    verified-funnel.py <report_file> <meta_data_json> <posthog_sessions_json> \
                       <wix_orders_json> <period_from> <period_to>

Data bronnen:
  - meta_data_json:       logs/morning-report-YYYY-MM-DD.data.json (stap 4)
  - posthog_sessions_json: logs/morning-report-YYYY-MM-DD.posthog-sessions.json (stap 5)
  - wix_orders_json:      data/wix-orders.json (handmatig bijgewerkt door Robin)
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _fmt_eur(val: float) -> str:
    return f"{val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def normalize_ad_id(name: str) -> str:
    """Converteer Meta ad naam naar utm_content formaat.

    'H11, B3, CTA5' -> 'h11_b3_cta5'
    'H11,B3,CTA5'   -> 'h11_b3_cta5'
    """
    parts = re.split(r"[,\s]+", name.strip())
    parts = [p.strip().lower() for p in parts if p.strip()]
    return "_".join(parts)


def extract_ad_short(name: str) -> str:
    """Extract HXX identifier from ad name for display."""
    m = re.search(r"H\d+", name, re.IGNORECASE)
    return m.group(0).upper() if m else name[:10]


def parse_date(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d")


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_meta_data(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_posthog_sessions(path: Path) -> list:
    if not path.exists():
        return []
    try:
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            return []
        data = json.loads(raw)
        if isinstance(data, dict):
            return data.get("thank_you_sessions", [])
        if isinstance(data, list):
            return data
        return []
    except Exception:
        return []


def load_wix_orders(path: Path, period_from: str, period_to: str) -> tuple:
    """Returns (orders_list, last_updated_str, is_available)."""
    if not path.exists():
        return [], "", False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return [], "", False

    last_updated = data.get("last_updated", "")
    orders = data.get("orders", [])
    if not isinstance(orders, list):
        return [], last_updated, False

    # Filter orders within period
    try:
        dt_from = parse_date(period_from)
        dt_to = parse_date(period_to)
    except Exception:
        return orders, last_updated, True

    filtered = []
    for o in orders:
        try:
            od = parse_date(o.get("date", ""))
            if dt_from <= od <= dt_to:
                filtered.append(o)
        except Exception:
            filtered.append(o)

    return filtered, last_updated, True


# ---------------------------------------------------------------------------
# Cross-referencing
# ---------------------------------------------------------------------------

def match_sessions_to_ads(sessions: list, ad_ids: dict) -> dict:
    """Map utm_content -> list of sessions."""
    result = {}
    for sess in sessions:
        utm = (sess.get("utm_content") or "").strip().lower()
        if not utm:
            continue
        if utm not in result:
            result[utm] = []
        result[utm].append(sess)
    return result


def match_orders_to_sessions(orders: list, sessions: list) -> tuple:
    """Match Wix orders to PostHog sessions by date (+/- 1 day).

    Priority:
    1. manual_ad_attribution on the order (handmatig geverifieerd)
    2. PostHog /thank-you session match by date (+/- 1 day)

    Returns (matched_orders_by_utm, unmatched_orders).
    matched_orders_by_utm: {utm_content: [order, ...]}
    """
    matched_by_utm = {}
    unmatched = []

    for order in orders:
        # Priority 1: manual attribution (for orders without PostHog data)
        manual_utm = (order.get("manual_ad_attribution") or "").strip().lower()
        if manual_utm:
            if manual_utm not in matched_by_utm:
                matched_by_utm[manual_utm] = []
            matched_by_utm[manual_utm].append(order)
            continue

        # Priority 2: PostHog session match by date
        try:
            order_date = parse_date(order.get("date", ""))
        except Exception:
            unmatched.append(order)
            continue

        best_session = None
        for sess in sessions:
            try:
                sess_date = parse_date(sess.get("visit_date", ""))
            except Exception:
                continue
            if abs((order_date - sess_date).days) <= 1:
                best_session = sess
                break

        if best_session:
            utm = (best_session.get("utm_content") or "unknown").strip().lower()
            if utm not in matched_by_utm:
                matched_by_utm[utm] = []
            matched_by_utm[utm].append(order)
        else:
            unmatched.append(order)

    return matched_by_utm, unmatched


# ---------------------------------------------------------------------------
# Report building
# ---------------------------------------------------------------------------

def build_funnel_section(
    meta: dict,
    sessions: list,
    orders: list,
    wix_available: bool,
    wix_last_updated: str,
    period_from: str,
    period_to: str,
) -> str:
    lines = []
    lines.append("## VERIFIED FUNNEL PER AD (30 dagen)")
    lines.append("")

    ads = meta.get("ads", [])
    if not ads:
        lines.append("> Geen per-ad Meta data beschikbaar.")
        lines.append("")
        return "\n".join(lines)

    # Build ad lookup: normalized_id -> ad data
    ad_lookup = {}
    for ad in ads:
        name = ad.get("name", "")
        norm = normalize_ad_id(name)
        if norm in ad_lookup:
            # Merge duplicates (same HXX in different adsets)
            existing = ad_lookup[norm]
            existing["spend"] = existing.get("spend", 0) + (ad.get("spend", 0) or 0)
            existing["impressions"] = existing.get("impressions", 0) + (ad.get("impressions", 0) or 0)
            existing["link_clicks"] = existing.get("link_clicks", 0) + (ad.get("link_clicks", 0) or 0)
        else:
            ad_lookup[norm] = {
                "name": name,
                "spend": float(ad.get("spend", 0) or 0),
                "impressions": int(ad.get("impressions", 0) or 0),
                "link_clicks": int(ad.get("link_clicks", 0) or 0),
            }

    # Map sessions and orders to ads
    sessions_by_utm = match_sessions_to_ads(sessions, ad_lookup)
    orders_by_utm, unmatched_orders = match_orders_to_sessions(orders, sessions)

    # Build table
    lines.append("| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |")
    lines.append("|---|---|---|---|---|---|---|---|")

    total_spend = 0
    total_clicks = 0
    total_ty = 0
    total_wix = 0
    total_rev = 0.0

    for norm_id, ad in sorted(ad_lookup.items()):
        spend = ad["spend"]
        clicks = ad["link_clicks"]
        ty_count = len(sessions_by_utm.get(norm_id, []))
        wix_count = len(orders_by_utm.get(norm_id, []))
        wix_rev = sum(float(o.get("amount_eur", 0) or 0) for o in orders_by_utm.get(norm_id, []))

        total_spend += spend
        total_clicks += clicks
        total_ty += ty_count
        total_wix += wix_count
        total_rev += wix_rev

        roas = f"{wix_rev / spend:.2f}x" if spend > 0 and wix_rev > 0 else "-"
        cpa = f"EUR {_fmt_eur(spend / wix_count)}" if wix_count > 0 else "-"
        wix_str = f"{wix_count} (EUR {_fmt_eur(wix_rev)})" if wix_count > 0 else "0"

        if not wix_available:
            wix_str = "?"
            roas = "?"
            cpa = "?"

        short = extract_ad_short(ad["name"])
        display = ad["name"] if len(ad["name"]) < 25 else f"{short},..."

        lines.append(
            f"| {display} | EUR {_fmt_eur(spend)} | {clicks} | "
            f"{ty_count} | {wix_str} | "
            f"{f'EUR {_fmt_eur(wix_rev)}' if wix_available and wix_rev > 0 else '-'} | "
            f"{roas} | {cpa} |"
        )

    # Add unmatched orders
    if unmatched_orders:
        unmatched_rev = sum(float(o.get("amount_eur", 0) or 0) for o in unmatched_orders)
        total_wix += len(unmatched_orders)
        total_rev += unmatched_rev
        lines.append(
            f"| (geen ad match) | - | - | - | "
            f"{len(unmatched_orders)} (EUR {_fmt_eur(unmatched_rev)}) | "
            f"EUR {_fmt_eur(unmatched_rev)} | - | - |"
        )

    # Totals row
    total_roas = f"{total_rev / total_spend:.2f}x" if total_spend > 0 and total_rev > 0 else "-"
    total_cpa = f"EUR {_fmt_eur(total_spend / total_wix)}" if total_wix > 0 else "-"

    if not wix_available:
        total_roas = "?"
        total_cpa = "?"

    lines.append(
        f"| **Totaal** | **EUR {_fmt_eur(total_spend)}** | **{total_clicks}** | "
        f"**{total_ty}** | **{total_wix if wix_available else '?'}** | "
        f"**{f'EUR {_fmt_eur(total_rev)}' if wix_available else '?'}** | "
        f"**{total_roas}** | **{total_cpa}** |"
    )
    lines.append("")

    # Discrepancy analysis
    meta_pc = int(meta.get("purchase_count", 0) or 0)
    meta_pv = float(meta.get("purchase_value", 0) or 0)

    if wix_available:
        if orders:
            lines.append("> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**")
            count_diff = meta_pc - total_wix
            value_diff = meta_pv - total_rev

            lines.append(f"> - Meta pixel: {meta_pc} purchases (EUR {_fmt_eur(meta_pv)})")
            lines.append(f"> - Wix orders: {total_wix} orders (EUR {_fmt_eur(total_rev)})")

            if count_diff > 0:
                lines.append(f"> - Verschil: +{count_diff} pixel purchases, "
                             f"+EUR {_fmt_eur(value_diff)} pixel waarde")
                lines.append("> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.")
                lines.append("> - Mogelijke oorzaken: Conversions API duplicaten, "
                             "test purchases, cross-domain pixel fires")
            elif count_diff < 0:
                lines.append(f"> - Verschil: {count_diff} pixel purchases (pixel ondertelt)")
                lines.append("> - **Verdict: PIXEL ONDERTELT.** Er zijn meer echte orders dan "
                             "Meta rapporteert. Mogelijk directe/organische sales.")
            else:
                if abs(value_diff) / max(total_rev, 1) > 0.15:
                    lines.append(f"> - Verschil: count matcht, maar waarde wijkt af "
                                 f"met EUR {_fmt_eur(abs(value_diff))}")
                    lines.append("> - **Verdict: WAARDE MISMATCH.** Pixel telt correct "
                                 "maar rapporteert verkeerde bedragen.")
                else:
                    lines.append("> - **Verdict: MATCH OK.** Pixel en Wix komen overeen.")
        else:
            lines.append("> Wix orders: 0 orders in periode. Update `data/wix-orders.json` "
                         "met orders uit Wix admin.")

        # Staleness warning
        if wix_last_updated:
            try:
                updated_dt = datetime.fromisoformat(wix_last_updated)
                age_days = (datetime.now(updated_dt.tzinfo) - updated_dt).days
                if age_days > 2:
                    lines.append(f"> ")
                    lines.append(f"> Wix orders laatst bijgewerkt: {wix_last_updated[:10]} "
                                 f"({age_days} dagen geleden). Mogelijk niet actueel.")
            except Exception:
                pass
    else:
        lines.append("> Wix order data niet beschikbaar. Maak `data/wix-orders.json` aan "
                     "(zie `data/wix-orders.example.json` voor formaat) om discrepanties "
                     "te detecteren.")

    lines.append("")

    # Unmatched PostHog sessions
    all_matched_sessions = set()
    for utm, sess_list in sessions_by_utm.items():
        for s in sess_list:
            all_matched_sessions.add(s.get("session_id", ""))

    unmatched_sessions = [
        s for s in sessions
        if s.get("session_id", "") not in all_matched_sessions
        or not s.get("utm_content")
    ]

    if unmatched_sessions:
        lines.append("> **ONGEMATCHTE /thank-you SESSIES:**")
        for s in unmatched_sessions:
            utm = s.get("utm_content") or "(geen utm_content)"
            date = s.get("visit_date", "?")
            lines.append(f"> - Sessie op {date}, utm_content={utm}")
        lines.append("")

    return "\n".join(lines)


def build_verified_recommendations(
    meta: dict,
    sessions: list,
    orders: list,
    wix_available: bool,
) -> tuple:
    """Build a verified-ROAS-based budget recommendation section.

    Returns (section_text, ranking) where ranking is a list of dicts
    (sorted by verified ROAS desc) used by the override detector.

    HARD RULES (zie CLAUDE.md + MORNING_REPORT_COMMAND_v2):
      1. Ranking op Verified ROAS (Wix), hoogste eerst.
      2. 70% budget ALTIJD naar ad met hoogste verified ROAS.
      3. Ad met 0 Wix orders mag NOOIT "best performer" heten.
      4. Ad met hoogste verified ROAS mag NOOIT "pauzeren" advies krijgen.
      5. Als verified data beschikbaar is, Meta pixel purchase data wordt
         GENEGEERD voor budget advies.
    """
    lines = []
    ranking = []

    if not wix_available:
        lines.append("## BUDGET AANBEVELINGEN (VERIFIED)")
        lines.append("")
        lines.append("> Wix order data niet beschikbaar. Budget aanbevelingen "
                     "kunnen NIET verified worden. Geen aanbeveling uitgevoerd.")
        lines.append("")
        return "\n".join(lines), ranking

    ads = meta.get("ads", [])
    if not ads:
        return "", ranking

    # Merge duplicate normalized ad names (same HXX in multiple adsets)
    ad_lookup = {}
    for ad in ads:
        name = ad.get("name", "")
        norm = normalize_ad_id(name)
        if norm in ad_lookup:
            existing = ad_lookup[norm]
            existing["spend"] += float(ad.get("spend", 0) or 0)
            existing["link_clicks"] += int(ad.get("link_clicks", 0) or 0)
        else:
            ad_lookup[norm] = {
                "name": name,
                "spend": float(ad.get("spend", 0) or 0),
                "link_clicks": int(ad.get("link_clicks", 0) or 0),
            }

    # Recompute orders_by_utm from scratch so this function is self-contained.
    _, _ = match_orders_to_sessions(orders, sessions)  # for side-effect parity
    orders_by_utm, _ = match_orders_to_sessions(orders, sessions)

    # Build ranking
    for norm_id, ad in ad_lookup.items():
        spend = ad["spend"]
        wix_ord = orders_by_utm.get(norm_id, [])
        wix_count = len(wix_ord)
        wix_rev = sum(float(o.get("amount_eur", 0) or 0) for o in wix_ord)
        roas = (wix_rev / spend) if spend > 0 and wix_count > 0 else 0.0
        ranking.append({
            "norm_id": norm_id,
            "name": ad["name"],
            "short": extract_ad_short(ad["name"]),
            "spend": spend,
            "wix_orders": wix_count,
            "wix_revenue": wix_rev,
            "verified_roas": roas,
        })

    # Sort: ads WITH orders first (by ROAS desc), then ads without orders
    # (by spend desc so biggest wasters surface).
    ranking.sort(
        key=lambda r: (
            0 if r["wix_orders"] > 0 else 1,
            -r["verified_roas"],
            -r["spend"],
        )
    )

    has_any_orders = any(r["wix_orders"] > 0 for r in ranking)

    lines.append("## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)")
    lines.append("")
    lines.append("**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data "
                 "wordt genegeerd voor budget beslissingen. Waar deze sectie "
                 "conflicteert met adviezen elders in dit rapport, heeft DEZE "
                 "sectie voorrang.")
    lines.append("")

    if not has_any_orders:
        lines.append("> Geen van de ads heeft verified Wix orders in de periode. "
                     "GEEN budget herverdeling op basis van verified funnel mogelijk. "
                     "Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.")
        lines.append("")
        return "\n".join(lines), ranking

    # Build ranking table
    lines.append("**Ranking op Verified ROAS:**")
    lines.append("")
    lines.append("| Rank | Ad | Verified ROAS | Wix Orders | Revenue | Spend | Advies |")
    lines.append("|---|---|---|---|---|---|---|")

    rank_icons = ["🥇", "🥈", "🥉"]
    winners = [r for r in ranking if r["wix_orders"] > 0]

    for idx, r in enumerate(ranking):
        if r["wix_orders"] > 0:
            # Determine budget allocation
            winner_idx = next(
                (i for i, w in enumerate(winners) if w["norm_id"] == r["norm_id"]),
                -1,
            )
            if winner_idx == 0:
                advice = "**70% budget** — hoogste verified ROAS · NIET pauzeren"
                icon = rank_icons[0]
            elif winner_idx == 1:
                advice = "20% budget — tweede verified winner · houd actief"
                icon = rank_icons[1]
            elif winner_idx == 2:
                advice = "10% budget — test & monitor"
                icon = rank_icons[2]
            else:
                advice = "Behoud op klein budget, monitor verified ROAS"
                icon = str(winner_idx + 1)
            roas_str = f"{r['verified_roas']:.2f}x"
            rev_str = f"EUR {_fmt_eur(r['wix_revenue'])}"
            orders_str = str(r["wix_orders"])
        else:
            icon = "—"
            roas_str = "0 orders"
            rev_str = "—"
            orders_str = "0"
            if r["spend"] > 50:
                advice = ("NIET als best performer labelen · 0 Wix orders ondanks "
                          f"EUR {_fmt_eur(r['spend'])} spend · heroverweeg")
            else:
                advice = "NIET als best performer labelen · 0 Wix orders"

        display = r["name"] if len(r["name"]) < 25 else f"{r['short']},..."
        lines.append(
            f"| {icon} | {display} | {roas_str} | {orders_str} | "
            f"{rev_str} | EUR {_fmt_eur(r['spend'])} | {advice} |"
        )

    lines.append("")

    # Explicit rules block so future readers (humans + sub-claudes) can't miss it
    lines.append("**Verified funnel regels (hard):**")
    top_winner = winners[0]
    zero_order_ads = [r for r in ranking if r["wix_orders"] == 0]

    lines.append(f"- Top verified performer: **{top_winner['short']}** "
                 f"(verified ROAS {top_winner['verified_roas']:.2f}x, "
                 f"{top_winner['wix_orders']} Wix order(s), "
                 f"EUR {_fmt_eur(top_winner['wix_revenue'])} revenue).")
    lines.append(f"- {top_winner['short']} mag NIET gepauzeerd worden en "
                 f"krijgt 70% van het budget.")
    if zero_order_ads:
        zero_names = ", ".join(r["short"] for r in zero_order_ads)
        lines.append(f"- Ads zonder verified orders ({zero_names}) mogen NIET "
                     f"als 'beste performer' of 'winner' gelabeld worden, "
                     f"ongeacht Meta pixel CTR/IC/purchase cijfers.")
    lines.append("")

    return "\n".join(lines), ranking


# ---------------------------------------------------------------------------
# Override annotator: mark conflicting advice earlier in the report
# ---------------------------------------------------------------------------

def annotate_conflicting_advice(text: str, ranking: list) -> str:
    """Scan the report text for pause/shift advice that conflicts with the
    verified ROAS ranking and prepend an override warning block.

    Conflict detected when:
      - Text recommends pausing the top-verified-ROAS ad, OR
      - Text recommends shifting budget TO an ad with 0 Wix orders,
        OR labels a 0-order ad as "beste" / "winner" / "best performer".
    """
    if not ranking:
        return text

    winners = [r for r in ranking if r["wix_orders"] > 0]
    if not winners:
        return text

    top = winners[0]
    zero_order = [r for r in ranking if r["wix_orders"] == 0]

    conflicts = []

    top_short = top["short"]
    top_ci_patterns = [
        rf"pauzeer\s+{re.escape(top_short)}\b",
        rf"{re.escape(top_short)}[^\n.]{{0,40}}\bpauzeren\b",
        rf"{re.escape(top_short)}[^\n.]{{0,60}}\bkandidaat\s+om\s+te\s+pauzeren\b",
        rf"\bpauzeer\b[^\n.]{{0,40}}{re.escape(top_short)}\b",
    ]
    for pat in top_ci_patterns:
        if re.search(pat, text, re.IGNORECASE):
            conflicts.append(
                f"❌ **Pauzeer {top_short}** advies in dit rapport conflicteert met "
                f"verified ROAS {top['verified_roas']:.2f}x. {top_short} is de top "
                f"performer — NIET pauzeren."
            )
            break

    for z in zero_order:
        z_short = z["short"]
        winner_patterns = [
            rf"{re.escape(z_short)}[^\n.]{{0,80}}\b(beste|winner|best performer|wint)\b",
            rf"\b(beste|winner|best performer)\b[^\n.]{{0,40}}{re.escape(z_short)}\b",
            rf"\bschaal\s+{re.escape(z_short)}\b",
            rf"\bschuif\s+[^.\n]{{0,60}}\s+{re.escape(z_short)}\b",
            rf"\bbudget\s+[^.\n]{{0,40}}\s+{re.escape(z_short)}\b\s*\+",
            rf"{re.escape(z_short)}\s*\+\d+%",
        ]
        for pat in winner_patterns:
            if re.search(pat, text, re.IGNORECASE):
                conflicts.append(
                    f"❌ **{z_short}** wordt elders in dit rapport als winnaar/best "
                    f"performer gelabeld of krijgt extra budget, maar heeft "
                    f"**0 Wix orders** op EUR {_fmt_eur(z['spend'])} spend. Negeer dat advies."
                )
                break

    if not conflicts:
        return text

    header = "\n".join([
        "> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**",
        "> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties "
        "hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified "
        "Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie "
        "verderop in dit rapport.",
        ">",
        *[f"> {c}" for c in conflicts],
        ">",
        f"> **Top verified performer:** {top_short} · ROAS {top['verified_roas']:.2f}x · "
        f"{top['wix_orders']} order(s) · EUR {_fmt_eur(top['wix_revenue'])} revenue.",
        "",
        "",
    ])

    # Insert after the front-matter (first `---` separator). Fallback: prepend.
    first_sep = text.find("\n---\n")
    if first_sep >= 0:
        insert_pos = first_sep + len("\n---\n")
        return text[:insert_pos] + "\n" + header + text[insert_pos:]
    return header + text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if len(sys.argv) != 7:
        print(
            "usage: verified-funnel.py <report_file> <meta_data_json> "
            "<posthog_sessions_json> <wix_orders_json> <period_from> <period_to>",
            file=sys.stderr,
        )
        return 2

    report_path = Path(sys.argv[1])
    meta_path = Path(sys.argv[2])
    posthog_path = Path(sys.argv[3])
    wix_path = Path(sys.argv[4])
    period_from = sys.argv[5]
    period_to = sys.argv[6]

    if not report_path.exists():
        print(f"[verified-funnel] {report_path} bestaat niet", file=sys.stderr)
        return 1

    # Load data
    meta = load_meta_data(meta_path)
    sessions = load_posthog_sessions(posthog_path)
    orders, wix_last_updated, wix_available = load_wix_orders(wix_path, period_from, period_to)

    # Build sections
    section = build_funnel_section(
        meta, sessions, orders, wix_available, wix_last_updated,
        period_from, period_to,
    )
    recs_section, ranking = build_verified_recommendations(
        meta, sessions, orders, wix_available,
    )

    combined = section
    if recs_section:
        combined = combined.rstrip() + "\n\n" + recs_section

    # Insert into report: after the last `---` separator before the
    # "Voorstellen uit auto-optimize" line, or at the end if not found.
    text = report_path.read_text(encoding="utf-8")

    insert_marker = "Voorstellen uit auto-optimize"
    if insert_marker in text:
        idx = text.index(insert_marker)
        sep_idx = text.rfind("---", 0, idx)
        if sep_idx >= 0:
            text = text[:sep_idx] + "---\n\n" + combined + "\n" + text[sep_idx + 3:]
        else:
            text = text[:idx] + combined + "\n" + text[idx:]
    else:
        text = text.rstrip() + "\n\n---\n\n" + combined

    # Prepend an override warning block when the earlier report sections
    # advise actions that contradict the verified ROAS ranking.
    text = annotate_conflicting_advice(text, ranking)

    report_path.write_text(text, encoding="utf-8")

    # Summary to stderr for logging
    wix_count = len(orders) if wix_available else "n/a"
    print(
        f"[verified-funnel] ads={len(meta.get('ads', []))} "
        f"posthog_ty={len(sessions)} wix_orders={wix_count} "
        f"wix_available={wix_available} {report_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
