Rapport staat in `Output/Reports/Daily/2026-09-08_auto_optimize.md`, gecommit en gepusht (2245f9fa). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCPs zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes en alle 57 ads staan op PAUSED. Meta registreert 0 impressions en 0 spend over 5 t/m 8 september. De kill-regels hadden geen data om op te draaien, er zijn geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Sinds 6 september 0 sessies met cpc als medium. De distributeurspagina kreeg alleen een handvol organische bezoekers. Laatste inzending was op 4 september, daarna 0.

**Niets veranderd ten opzichte van gisteren.** De zes voorstellen uit de run van 7 september staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag, 70-20-10 verdeeld.
2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag, alleen Statisch 2 plus één nieuwe creative.
3. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
4. Conversie-guard op de kill-regels, zodat Statisch 1 (LIT) niet op dag 1 na herstart wordt gepauzeerd.
5. LIT ad sets samenvoegen, SWE audience verbreden.
6. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
