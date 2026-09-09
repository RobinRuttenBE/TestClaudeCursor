# SYBB 30-dagen metrics (Meta Ads, Pipeboard direct JSON-RPC)

Datum run: 9 September 2026
Campagne: 2026: SYBB (ID 120239435987290239, status PAUSED)
Periode: 2026-08-10 t/m 2026-09-08
Account: act_567892422940728

## Resultaat
Geen levering in de afgelopen 30 dagen. Campaign-level, daily breakdown (30 segmenten) en ad-level insights gaven allemaal lege data. Sanity check met time_range "maximum" gaf wel data (lifetime spend EUR 2485.04, 297.174 impressies, 10.851 link clicks, 6 purchases), dus de API werkt en de lege 30d-set is echt.

## JSON
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}

## Bronnen
Alleen Meta Ads (Pipeboard, directe JSON-RPC). Geen Google MCPs gebruikt, geen Google Sheet geschreven. PostHog MCP was niet verbonden (405).
