# Morning Report — 2026-04-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-21

**Status: niet gegenereerd — Pipeboard Meta Ads MCP is niet geladen in deze sessie.**

Beschikbare MCPs in deze run zijn Google, Instagram/Facebook Graph, GA4 en Lottiefiles. De strikte run-regels verbieden Google MCPs, en de Facebook Graph MCP dekt Pages/IG, geen Ads insights. Daardoor konden stap 1 t/m 5 niet worden uitgevoerd. Stap 6 was per instructie al overgeslagen.

Status-rapport opgeslagen in `Output/Reports/Daily/2026-04-21_ads_report.md` met daarin:
- Welke MCP-calls faalden en waarom
- Laatst bekende staat uit het 2026-04-20 rapport (H12 winnaar, H13 pauzeer-kandidaat, account `act_607231713057715` niet toegankelijk)
- Aanbevolen fix: Pipeboard Meta Ads MCP server opnieuw verbinden, dan `/ads-report` herhalen

Geen verzonnen cijfers, geen funnel-vraag — er is geen verse data om aan te koppelen.

---

Status-rapport opgeslagen in `Output/Reports/Daily/2026-04-20_sybb_report.md`. 

Kortaf: geen verse data, want (1) Pipeboard Meta Ads MCP vereist OAuth-auth die niet-interactief niet te voltooien is, en (2) PostHog MCP staat niet in de deferred tool lijst van deze sessie. Het rapport bevat de laatst bekende staat uit 2026-04-19 (H12 winnaar, H13 pauzeer-kandidaat) en drie concrete herstel-acties. Geen Google MCPs gebruikt, geen verzonnen cijfers.

Wil je de Pipeboard-auth nu interactief afronden zodat ik 2026-04-20 alsnog met echte data kan backfillen?

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-21_auto_optimize.md`.

**Samenvatting:**
- **0 ads gepauzeerd** — Pipeboard Meta Ads MCP niet geauthenticeerd, PostHog MCP niet geladen. Zonder `impressions` / `actions.link_click` kunnen kill-regels niet worden geëvalueerd.
- **Geen 70-20-10 classificatie** — vereist per-ad Link CTR / CPC (link) / ROAS.
- **Geen voorstellen** — advies zonder verse cijfers zou teruggrijpen op 24+ uur oude data uit het 2026-04-20 rapport; dat is niet verantwoord voor budget-shifts.
- **Geen writes naar Google Sheet tracker** (conform run-regel), geen Google MCPs aangeroepen.

**Fix:** verbind Pipeboard Meta Ads MCP opnieuw via `/mcp` → selecteer `claude.ai Pipeboard Meta Ads` → rond OAuth flow af. Herhaal daarna `/ads-auto-optimize`. Los ook de pixel datafout (€7.374,50 per purchase) op voordat ROAS-voorstellen bruikbaar zijn.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
