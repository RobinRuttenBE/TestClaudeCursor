# Wix orders fetch: 13 sep 2026

**Status:** MISLUKT, geen API call uitgevoerd.

**Reden:** De Wix MCP server (claude.ai Wix) vereist autorisatie en was niet verbonden in deze non-interactieve sessie. De tool CallWixSiteAPI was daardoor niet beschikbaar.

**Bedoelde call:**
- siteId: 476f7384-3ec8-4157-8440-73bef7409891 (Start Your Balloon Business)
- url: https://www.wixapis.com/ecom/v1/orders/search
- method: POST
- body: {"search": {"filter": {"paymentStatus": "PAID"}, "sort": [{"fieldName": "createdDate", "order": "DESC"}], "cursorPaging": {"limit": 50}}}

**Vereiste actie:** Wix connector autoriseren via de claude.ai connector-instellingen, daarna de run herhalen.

**Overige MCP status deze run:** Pipeboard Meta Ads vereist eveneens autorisatie. PostHog MCP (posthog) faalde met een 405. Geen Google MCPs aangeroepen.
