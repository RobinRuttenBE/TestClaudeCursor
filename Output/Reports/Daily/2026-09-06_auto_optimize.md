Rapport staat in `Output/Reports/Daily/2026-09-06_auto_optimize.md`, gecommit en gepusht (bde52e95). Alleen Pipeboard (geprobeerd) en PostHog (claude.ai connector) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta Ads was voor de tweede dag op rij op geen enkele route bereikbaar. De Pipeboard MCP vraagt authenticatie, de directe JSON-RPC route zit nog op de weeklimiet van het Free plan, en er staat geen ander Meta-token in de config. Zonder impressions en link clicks kunnen de kill-regels niet draaien. Volgens de laatst bekende stand staan alle 8 Wholesaler-ads sowieso op PAUSED sinds 4 september.

**PostHog bevestigt de stilstand.** Betaalde sessies per dag gingen van 186 op 3 september naar 50 op 4 september, 4 op 5 september en 1 vandaag. De vier sessies van 5 september waren organisch Facebook-verkeer via een Britse retailer, geen ads. Sinds de pauze zijn er 0 form starts en 0 inzendingen.

**Eén ding om zelf te checken.** Vanochtend om 04:53 UTC kwam een echte Zweedse bezoeker via Instagram binnen op de Video 1 (SWE) UTM, 11 seconden op de pagina. Eén bezoeker in 48 uur tegenover 10 sessies per dag toen de ad live was, wijst op een opgeslagen of gedeelde ad-post en niet op actieve levering. Omdat ik dit niet in Meta kan verifiëren: open Ads Manager en bevestig dat Video 1 (SWE) op PAUSED staat.

**Voorstellen die op goedkeuring wachten** staan ongewijzigd in het rapport, met één nieuwe randvoorwaarde:

0. Meta-data herstellen: Pipeboard Pro, connector opnieuw autoriseren via `/mcp`, of een System User token als fallback. Zonder dit kan auto-optimize morgen weer niets doen.
1. Tracking fixen voor de herstart (Meta 19 leads, PostHog 33).
2. Budget herverdeling bij herstart op €140 per dag, Core op Statisch 2 (SWE) en de twee LIT-video's.
3. Drie hook-varianten per land plus CTA-test.
4. Beslissing over Video 2 (LIT): conversie-guard of strikt pauzeren.
5. LIT ad sets samenvoegen, SWE audience verbreden.

Geef aan welke nummers ik mag uitvoeren.
