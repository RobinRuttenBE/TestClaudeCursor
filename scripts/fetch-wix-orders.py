#!/usr/bin/env python3
"""
fetch-wix-orders.py -- Haal Wix eCommerce orders op via de Wix MCP (Claude sub-process).

Omdat de Wix MCP alleen beschikbaar is als MCP tool binnen Claude Code, en
morning-report.sh al Claude sub-processen spawnt voor elke stap, draait dit
script NIET direct tegen de Wix API. In plaats daarvan genereert het de
Claude prompt die morning-report.sh aan run_claude() doorgeeft.

Alternatief: als de Wix MCP niet beschikbaar is of faalt, valt het script
terug op data/wix-orders.json (handmatige fallback).

Usage (standalone test):
    fetch-wix-orders.py <output_json> <period_from> <period_to>

Dit script wordt NIET direct aangeroepen door morning-report.sh.
Morning-report.sh roept in plaats daarvan een Claude sub-process aan die
de Wix MCP tools gebruikt, en dit script parseert de output.

Het script wordt WEL gebruikt om de Claude-output te parsen naar het
gestandaardiseerde wix-orders formaat dat verified-funnel.py verwacht.
"""

import json
import sys
from pathlib import Path


def parse_wix_orders_response(raw_json: str) -> list:
    """Parse Wix eCommerce Search Orders API response into simplified format."""
    try:
        data = json.loads(raw_json)
    except Exception:
        return []

    # Handle both direct response and wrapped response
    orders_raw = data.get("orders", [])
    if not isinstance(orders_raw, list):
        return []

    orders = []
    for o in orders_raw:
        order_id = o.get("number", o.get("id", ""))
        created = o.get("createdDate", "")
        date_part = created[:10] if created else ""
        time_part = created[11:19] if len(created) > 19 else ""

        # Get total price (what customer actually paid)
        price_summary = o.get("priceSummary", {})
        total = price_summary.get("totalPrice", {}).get("amount", "0")
        subtotal = price_summary.get("subtotal", {}).get("amount", "0")
        tax = price_summary.get("tax", {}).get("amount", "0")

        # Product name from first line item
        line_items = o.get("lineItems", [])
        product = ""
        tickets = 0
        for li in line_items:
            name_obj = li.get("productName", {})
            product = name_obj.get("original", name_obj.get("translated", ""))
            tickets += int(li.get("quantity", 1))

        # Customer info
        billing = o.get("billingInfo", {})
        contact = billing.get("contactDetails", {})
        address = billing.get("address", {})
        country = address.get("countryFullname", address.get("country", ""))

        # Payment status
        payment_status = o.get("paymentStatus", "")

        orders.append({
            "order_id": f"WIX-{order_id}",
            "date": date_part,
            "time": time_part,
            "amount_eur": float(total),
            "amount_ex_btw": float(subtotal),
            "tax": float(tax),
            "tickets": tickets,
            "product": product,
            "customer_country": country,
            "payment_status": payment_status,
        })

    return orders


def build_wix_orders_json(orders: list, period_from: str, period_to: str) -> dict:
    """Build the standardized wix-orders JSON format."""
    from datetime import datetime
    return {
        "last_updated": datetime.now().isoformat(),
        "period": {
            "from": period_from,
            "to": period_to,
        },
        "source": "wix_mcp_api",
        "orders": orders,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "usage: fetch-wix-orders.py <output_json> [<period_from> <period_to>]\n"
            "  Reads Wix API response from stdin, writes standardized JSON to output_json.",
            file=sys.stderr,
        )
        return 2

    output_path = Path(sys.argv[1])
    period_from = sys.argv[2] if len(sys.argv) > 2 else ""
    period_to = sys.argv[3] if len(sys.argv) > 3 else ""

    raw = sys.stdin.read()
    orders = parse_wix_orders_response(raw)

    result = build_wix_orders_json(orders, period_from, period_to)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        f"[fetch-wix-orders] {len(orders)} orders parsed, written to {output_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
