# Auto-Optimize Rapport — 2026-04-22

## Status: GEBLOKKEERD — geen live data beschikbaar

### Wat er mis is
- **Pipeboard Meta Ads MCP niet geauthenticeerd.** Alleen `mcp__pipeboard-meta-ads__authenticate` en `mcp__pipeboard-meta-ads__complete_authentication` zijn beschikbaar. De data-tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_adsets`, `get_ads`, `update_ad`) komen pas na OAuth.
- **PostHog MCP tools niet geladen** in deze sessie. Cross-referencing met landing page data is niet mogelijk.
- **Strikte run-regel:** alleen Meta Ads MCP (Pipeboard) en PostHog MCP toegestaan. Geen Google MCPs, geen writes naar de Google Sheet tracker.

### Wat dit betekent voor vandaag
- **0 ads gepauzeerd.** Kill-regels (Link CTR < 0.8% na ≥1.000 impressions, CPC (link) > €1.50 na ≥500 link clicks) konden niet worden geëvalueerd — geen `impressions` of `actions.link_click` beschikbaar.
- **Geen 70-20-10 classificatie.** Vereist per-ad Link CTR, CPC (link) en ROAS over de laatste 3 dagen.
- **Geen voorstellen (Niveau 2).** Budget herverdeling, nieuwe variaties en audience aanpassingen zouden moeten leunen op 24+ uur oude cijfers uit het 2026-04-20 rapport — niet verantwoord voor budget-shifts.
- **Geen writes naar de Meta Ads Tracker Google Sheet** (conform run-regel).
- **Geen Google MCPs aangeroepen.**

### Dit is de tweede dag op rij met dezelfde blokkade
Het 2026-04-21 rapport meldde exact hetzelfde probleem. Zonder fix loopt de optimalisatie-loop stil: underperformers blijven draaien op budget, winners krijgen geen scale-up, en creative fatigue (freq > 3.5) blijft onzichtbaar.

### ⚡ Automatische acties uitgevoerd
Geen. (Zie status hierboven.)

### ⚠️ Waarschuwingen
Niet te bepalen zonder data.

### 📊 70-20-10 Classificatie
Niet te bepalen zonder data.

### 💡 Voorstellen (wacht op goedkeuring)
Niet te bepalen zonder data.

---

## Fix — actie vereist van Robin

**1. Pipeboard Meta Ads MCP opnieuw verbinden**
- Optie A: via `/mcp` → selecteer `claude.ai Pipeboard Meta Ads` → rond OAuth flow af.
- Optie B: ik heb de OAuth flow al gestart. Autorisatie-URL (uit deze sessie):
  ```
  https://pipeboard.co/oauth/authorize?response_type=code&client_id=6823b50ca3c6b944b526a0c535bd1649&code_challenge=fMvn4E1xnrYkk0ke4MIXfIs_q6Kx6lo71NIBjOq8PIk&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A61662%2Fcallback&state=aFfAN0WcI5bPQKtBX9WIlKftB7eGs91qPp9TI03WS5E&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
  ```
  Open de URL, autoriseer, plak de callback-URL terug in de chat en ik rond af.

**2. PostHog MCP activeren** als cross-referencing (ad → landing page) opnieuw standaard onderdeel van de optimalisatie moet zijn.

**3. Herhaal `/ads-auto-optimize`** zodra Pipeboard live is.

**4. Pixel datafout uit vorige rapport** (€7.374,50 per purchase) checken vóórdat ROAS-voorstellen bruikbaar zijn — anders komen Core-classificatie en budget-shifts uit op verkeerde aannames.

---

*Gegenereerd: 2026-04-22. Run-regel: alleen Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google MCPs aangeroepen, geen writes naar de Google Sheet tracker. Output opgeslagen in `Output/Reports/Daily/2026-04-22_auto_optimize.md`.*
