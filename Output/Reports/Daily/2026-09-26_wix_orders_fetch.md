# Wix orders fetch: 26 sep 2026

**Status:** MISLUKT, geen API call uitgevoerd.

**Reden:** De Wix MCP server (claude.ai Wix) vereist autorisatie en was niet verbonden in deze non-interactieve sessie. De tool CallWixSiteAPI was daardoor niet beschikbaar (ToolSearch vond geen Wix tools). Er staat geen lokale Wix API key in het project (geen .env, geen WIX-variabele in de omgeving, geen credentials in scripts) waarmee de call via directe HTTP kon worden uitgevoerd.

**Bedoelde call:**
- siteId: 476f7384-3ec8-4157-8440-73bef7409891 (Start Your Balloon Business)
- url: https://www.wixapis.com/ecom/v1/orders/search
- method: POST
- body: {"search": {"filter": {"paymentStatus": "PAID"}, "sort": [{"fieldName": "createdDate", "order": "DESC"}], "cursorPaging": {"limit": 50}}}

**Gevolg:** Er is bewust geen JSON verzonnen. Downstream stappen vallen terug op data/wix-orders.json (handmatige fallback).

**Vereiste actie:** Wix connector autoriseren via de claude.ai connector-instellingen, daarna de run herhalen. Dit is de zesde geregistreerde run (13, 17, 20, 21, 22 en 26 sep) waarin dit faalde. Structurele oplossing: een Wix API key in een lokale .env en scripts/fetch-wix-orders.py de call rechtstreeks laten doen, zodat de flow niet meer afhankelijk is van MCP-autorisatie.

**Overige MCP status deze run:** Pipeboard Meta Ads (beide varianten) vereist eveneens autorisatie. PostHog MCP (posthog) faalde met een 405. GA4 verbinding gesloten. Geen Google MCPs aangeroepen. Niet naar de Google Sheet tracker geschreven.
