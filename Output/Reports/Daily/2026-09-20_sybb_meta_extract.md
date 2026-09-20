# SYBB Meta extract 2026-09-20 (30d, 21 aug t/m 20 sep)

Status: **geen data**. Eerste en enige Pipeboard-call (campaign-level 30d insights, account act_567892422940728, time_increment=1) kreeg `weekly_limit_exceeded` (30 van 30, reset 2026-09-21T00:00Z). Conform de regel van 19 september geen verdere Meta-calls gedaan. Pipeboard MCP zelf meldt "requires authentication", PostHog MCP gaf 405 bij verbinden.

Output JSON (fallback met nullen):

```
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```

Dit is geen echte nul-levering maar een ontbrekende meting. Laatste extract met echte cijfers: ads-rapport van 16 september 2026 (`2026-09-16_ads_report.md`). Op maandag 21 september eerst live testen, dan campaign-level 30d met time_increment=1 plus ad-level in één run.
