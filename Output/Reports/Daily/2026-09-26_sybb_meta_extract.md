# SYBB Meta extract 2026-09-26 (zaterdag)

**Status:** Meta onbereikbaar, geen bevestigde nul-levering.

- Eén testcall (Pipeboard directe JSON-RPC, `get_insights` campaign-level, campagne 120239435987290239, 27 aug t/m 26 sep, time_increment=1) kreeg `weekly_limit_exceeded`.
- Verbruik: 30 van 30, trial_credits_remaining 0, reset_date 2026-09-28T00:00:00Z.
- MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` meldden "requires authentication" (non-interactieve sessie).
- Geen verdere Meta-calls gedaan; geen Google MCP's aangeroepen; niet naar de Google Sheet tracker geschreven.

**Teruggegeven JSON (nullen = onbereikbaar, niet gemeten):**

```
{"purchase_value": 0.0, "purchase_count": 0, "spend": 0.0, "impressions": 0, "link_clicks": 0, "active_days": 0, "ads": []}
```

**Laatste live bevestiging:** extract 24 september 2026 (campaign-level `{"data": []}`, echte nul-levering, campagne gepauzeerd).

**Volgende stap:** maandag 28 september eerst live testen (campaign-level 30d), daarna pas ad-level.
