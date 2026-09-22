# SYBB Meta extract, 22 september 2026

**Campagne:** 2026: SYBB (ID 120239435987290239)
**Venster:** 23 augustus t/m 22 september 2026 (30 dagen)
**Bron:** Pipeboard Meta Ads via directe JSON-RPC call (MCP meldde "requires authentication")

## Resultaat

Campaign-level `get_insights` met dagelijkse uitsplitsing gaf `{"data": []}`: echte nul-levering, geen `weekly_limit_exceeded`. De campagne staat gepauzeerd (status uit het ads-rapport van dezelfde ochtend). Ad-level call is overgeslagen om de weeklimiet te sparen; zonder campaign-level spend zijn er geen ads met spend > 0.

| Metric | Waarde |
|---|---|
| purchase_value | 0.0 |
| purchase_count | 0 |
| spend | 0.0 |
| impressions | 0 |
| link_clicks | 0 |
| active_days | 0 |
| ads met spend > 0 | 0 |

## JSON output

```
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```

**Let op:** dit zijn echte nullen (geen levering), niet een fallback wegens onbereikbare data. Pipeboard-verbruik na deze run: 14 van 30 calls deze week.
