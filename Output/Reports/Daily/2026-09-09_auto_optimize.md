Rapport staat in `Output/Reports/Daily/2026-09-09_auto_optimize.md`, gecommit en gepusht (0f2db115). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCPs zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED. Meta geeft over 6 t/m 8 september 0 rijen op ad-niveau, dus 0 impressions, 0 link clicks en €0,00 spend. Er zijn geen ads gepauzeerd en geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** 0 sessies met cpc als medium sinds 6 september. De distributeurspagina kreeg 1 tot 5 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Niets veranderd ten opzichte van gisteren.** Dit is de zesde dag op rij zonder levering. De vijf voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, en Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
