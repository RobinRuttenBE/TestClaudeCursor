# Morning Report — 2026-05-14

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

De Meta Ads MCP (Pipeboard) heeft een verlopen Facebook connectie en kan op dit moment geen data ophalen. Ik kan zonder die data geen rapport genereren.

**Wat je moet doen:**

Open deze URL in je browser om de Pipeboard Meta Ads connectie te herstellen:

```
https://pipeboard.co/oauth/authorize?response_type=code&client_id=3600e7cd3a17d279dde0e741c5c191f9&code_challenge=_EblJapPNOgVttoTvT3hIddIoifN4s-Qojm7tP-g5zU&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A56927%2Fcallback&state=xAMquyQBOKt4YdIQ7L_-WTtscF_s7l2YsSgihK_h2jA&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
```

Na het voltooien van de autorisatie kun je `/ads-report` opnieuw draaien. Als de browser een connection error toont op de redirect pagina, plak dan de volledige URL uit de adresbalk hier zodat ik `complete_authentication` kan aanroepen.

**Status rapport:** niet gegenereerd. Geen lokaal bestand geschreven naar `Output/Reports/Daily/2026-05-14_ads_report.md` omdat er geen brondata beschikbaar is.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-13_sybb_report.md` en gepusht naar GitHub.

**Kernpunten 13 mei:**
- **Meta Ads:** Pipeboard MCP geblokkeerd voor de 3e dag op rij ("Facebook connection required"). Een nieuwe OAuth URL is in actie 1 van het rapport opgenomen voor reconnect. Campagne `2026: SYBB` presumed nog steeds PAUSED (24 dagen).
- **PostHog:** 1 pageview, 1 sessie, 1 unieke bezoeker. Dezelfde Instagram bio link sessie (US mobiel, 0s, bounce) als gisteren. De `/review` spike van 12 mei (13 pv) is verdampt naar 0, wat sterk wijst op een eenmalige link share of test.
- **Funnel:** nul `/booking` voor de 10e dag op rij, nul `/checkout` sinds 6 mei.
- **Top 3 acties:** (1) Pipeboard MCP reconnect, (2) binaire relaunch-of-stop beslissing forceren, (3) onderzoek of de dagelijkse Instagram bio link sessie een bot/crawler is.

---

Run afgebroken: Pipeboard Meta Ads MCP gaf op beide accounts `Facebook connection required` — geen data, geen kill-regels geëvalueerd, geen ads gepauzeerd. Rapport opgeslagen in `Output/Reports/Daily/2026-05-14_auto_optimize.md` en gepusht. Herverbind Facebook op https://pipeboard.co/connections en draai `/ads-auto-optimize` opnieuw.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
