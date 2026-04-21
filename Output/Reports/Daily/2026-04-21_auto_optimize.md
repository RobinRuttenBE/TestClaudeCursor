Rapport opgeslagen in `Output/Reports/Daily/2026-04-21_auto_optimize.md`.

**Samenvatting:**
- **0 ads gepauzeerd** — Pipeboard Meta Ads MCP niet geauthenticeerd, PostHog MCP niet geladen. Zonder `impressions` / `actions.link_click` kunnen kill-regels niet worden geëvalueerd.
- **Geen 70-20-10 classificatie** — vereist per-ad Link CTR / CPC (link) / ROAS.
- **Geen voorstellen** — advies zonder verse cijfers zou teruggrijpen op 24+ uur oude data uit het 2026-04-20 rapport; dat is niet verantwoord voor budget-shifts.
- **Geen writes naar Google Sheet tracker** (conform run-regel), geen Google MCPs aangeroepen.

**Fix:** verbind Pipeboard Meta Ads MCP opnieuw via `/mcp` → selecteer `claude.ai Pipeboard Meta Ads` → rond OAuth flow af. Herhaal daarna `/ads-auto-optimize`. Los ook de pixel datafout (€7.374,50 per purchase) op voordat ROAS-voorstellen bruikbaar zijn.
