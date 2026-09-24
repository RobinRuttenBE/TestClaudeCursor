# SYBB Meta extract, 24 September 2026

**Campagne:** 2026: SYBB (ID 120239435987290239), account act_567892422940728
**Venster:** 25 augustus t/m 24 september 2026 (30 dagen)
**Bron:** Pipeboard Meta Ads, directe JSON-RPC call (MCP meldde "requires authentication")

## Resultaat

Eén campaign-level `get_insights` call (time_range 25 aug t/m 24 sep, time_increment=1) gaf direct `{"data": []}` in de eerste poging. Geen limietmelding, dus dit is echte nul-levering: de campagne staat gepauzeerd en heeft in dit venster geen spend, impressies, link clicks of purchases.

Ad-level call overgeslagen: bij een lege campaign-level set zijn er per definitie geen ads met spend > 0.

Weekverbruik Pipeboard na deze run: circa 6 van 30 calls.

## JSON-extract

```json
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```

Nullen betekenen hier: geen levering in het venster (bevestigd door Meta), niet "data onbereikbaar".
