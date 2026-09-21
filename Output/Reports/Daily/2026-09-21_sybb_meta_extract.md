# SYBB Meta extract 2026-09-21 (30d, 22 aug t/m 21 sep)

Status: **echte nul-levering, live gemeten**. De Pipeboard-weeklimiet was gereset. Twee directe JSON-RPC calls op campagne `2026: SYBB` (ID 120239435987290239):

1. `get_insights`, level campaign, `date_preset: last_30d`, `time_increment: 1` → `{"data": []}`
2. `get_insights`, level ad, `date_preset: last_30d` → `{"data": []}`

Geen enkele dag met spend in het 30d-venster, dus 0 actieve dagen en geen ads met spend. Dit is geen ontbrekende meting zoals op 19 en 20 september, maar een bevestigde stilstand: de SYBB-campagne staat gepauzeerd (zie `2026-09-21_ads_report.md`, alle 7 campagnes PAUSED). De enige spend van de afgelopen 30 dagen zat in de twee Wholesaler-campagnes, niet in SYBB.

Pipeboard MCP zelf meldde "requires authentication", PostHog MCP gaf 405 bij verbinden; geen Google MCPs aangeroepen, niets naar de Sheet geschreven. Verbruik Pipeboard vandaag na deze run: 8 van 30 calls.

Output JSON:

```
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```
