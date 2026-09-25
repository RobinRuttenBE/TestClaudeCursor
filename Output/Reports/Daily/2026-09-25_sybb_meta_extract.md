# SYBB Meta extract, 25 September 2026

**Campagne:** 2026: SYBB (ID 120239435987290239), account act_567892422940728
**Venster:** 26 augustus t/m 25 september 2026 (30 dagen)
**Bron:** Pipeboard Meta Ads, directe JSON-RPC call (MCP meldde "requires authentication")

## Resultaat

Eén campaign-level `get_insights` call (time_range 26 aug t/m 25 sep, time_increment=1) kreeg direct `weekly_limit_exceeded`: 30 van 30 wekelijkse AI tool executions gebruikt op het gratis Pipeboard plan, reset_date 28 september 2026 00:00 UTC. Geen tweede call gedaan; tot maandag blijft de limiet dicht.

De nullen hieronder betekenen dus **"data onbereikbaar"**, niet bevestigde nul-levering. Laatste live bevestiging van echte nul-levering in dit venster: extract van 24 september (campaign-level `{"data": []}` voor 25 aug t/m 24 sep). De campagne staat volgens het ads-rapport van vanochtend (08:17) nog steeds op PAUSED; PostHog bevestigde in de auto-optimize run van 08:40 nul betaalde sessies van 18 t/m 25 september. Inhoudelijk is de verwachting daarom onveranderd: geen spend, impressies, link clicks of purchases.

Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

## JSON-extract

```json
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```
