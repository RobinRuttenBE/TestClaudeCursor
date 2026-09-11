Rapport staat in `Output/Reports/Daily/2026-09-11_auto_optimize.md`, gecommit en gepusht (8a87b96a). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Meta geeft over 8 t/m 11 september 0 rijen op ad-niveau, dus 0 impressions, 0 link clicks en €0,00 spend. Geen ads gepauzeerd, geen `update_ad` calls.

**PostHog bevestigt de stilstand.** 0 tot 2 betaalde sessies per dag, en die 2 op 9 september zijn nalopers op oude ad-URL's. De distributeurspagina kreeg 1 tot 5 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Achtste dag op rij zonder levering.** Niets veranderd ten opzichte van gisteren. De vijf voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
