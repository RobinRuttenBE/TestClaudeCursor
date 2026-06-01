## Meta Ads Rapport — 1 juni 2026

**Live data niet beschikbaar.** De Pipeboard Meta Ads MCP en PostHog MCP zijn deze sessie niet online gekomen — ToolSearch vindt geen `get_campaigns`, `get_insights`, of `get_ad_accounts` tools. Geen Python/CLI fallback in `scripts/`. Ik heb dus geen verse cijfers kunnen pullen.

### Laatste bekende state (uit 2026-05-31_ads_report.md)

| Campagne | Status | Spend (lifetime) | CTR | CPC | CPM | ROAS |
|----------|--------|------------------|-----|-----|-----|------|
| 2026: SYBB | PAUSED | €2.485,04 | 4,1% | €0,21 | €8,36 | 17,8x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 2,6% | €0,64 | €16,34 | 0,0x |

Spend last_30d op 31 mei: **€0,00** — alles gepauzeerd. Tenzij sinds gisteren iets aan staat, verandert dit niet.

### Aanbeveling (onveranderd)
Reactiveer `2026: SYBB` (bewezen 70%, ROAS 17,8x). Niet schalen vóór LPV → view content drop (98%) is gediagnosticeerd — eerst pixel check, dan LP CRO.

### Acties om dit op te lossen
1. Check MCP config voor `pipeboard-meta-ads` en `posthog`, herstart de sessie zodat ze connecten.
2. Overweeg een `scripts/fetch-meta-ads.py` als CLI fallback (zoals `fetch-wix-orders.py`).

Rapport opgeslagen in `Output/Reports/Daily/2026-06-01_ads_report.md`. Geen Google Sheet write (per instructie). Geen funnel-diagnose mogelijk zonder PostHog data.
