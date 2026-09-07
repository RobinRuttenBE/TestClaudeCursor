Rapport staat in `Output/Reports/Daily/2026-09-07_auto_optimize.md`, gecommit en gepusht (43f6b966). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Er zijn 0 actieve campagnes. Alle 8 Wholesaler-ads (4 LIT, 4 SWE) staan sinds 4 september 11:50 op PAUSED. Meta registreert €0,00 spend op 5, 6 en 7 september. De kill-regels hadden dus niets om op te draaien en er zijn geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Betaalde sessies op de distributeurspagina gingen van 58 op 4 september naar 0 op 5 september, 2 op 6 september en 0 vandaag. Die twee sessies van gisteren kwamen via Instagram op de Video 1 (SWE) UTM binnen zonder Meta-impressions, dus het is een gedeelde of opgeslagen post en geen levering. Het handmatige check-punt van gisteren is daarmee afgehandeld. Sinds de pauze 0 form starts en 0 inzendingen.

**Eén observatie voor de herstart.** Op de laatste ochtend van 4 september triggerde Statisch 1 (LIT) mechanisch de Link CTR-regel (0,2% bij 1.830 impressions), terwijl het over 30 dagen een van de drie goedkoopste converters is. Zonder conversie-guard pauzeert auto-optimize deze ad op de eerste volle dag na herstart.

**Twee bijzonderheden in de setup**
- Het in het command genoemde tweede account act_607231713057715 bestaat niet in de Pipeboard-koppeling. Het staat al zo in het geheugen, maar het command verwijst er nog naar.
- De PostHog-token stond op een ander pad in de config dan verwacht. Ik heb dat pad in het geheugen genoteerd zodat de volgende run niet stokt.

**Voorstellen die op goedkeuring wachten** (uitgewerkt in het rapport):

1. Herstart Wholesaler (LIT) op €100,00 per dag, 70-20-10 verdeeld over Video 2, Video 1, Statisch 1, Statisch 2 en één nieuwe creative.
2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag, alleen Statisch 2 plus één nieuwe creative.
3. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
4. Conversie-guard op de kill-regels: niet pauzeren bij minimaal 1 PostHog-inzending onder €40,00.
5. LIT ad sets samenvoegen, SWE audience verbreden.
6. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Geef aan welke nummers ik mag uitvoeren.
