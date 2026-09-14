Rapport staat in `Output/Reports/Daily/2026-09-14_auto_optimize.md`, gecommit en gepusht (356b500b). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route) gebruikt, beide MCP-servers zelf weigerden opnieuw. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta bevestigt live dat alle 7 campagnes op PAUSED staan, de twee Wholesaler campagnes sinds 4 september 11:50. De ad-level insights over 11 t/m 13 september geven nul rijen. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Nul sessies met een Meta-UTM sinds 11 september. De distributeurspagina kreeg alleen 10 organische pageviews op 11 en 12 september en nul inzendingen. Laatste betaalde inzending blijft 4 september, elfde dag zonder levering.

**Pipeboard werkte vandaag weer.** De weeklimiet was maandag gewoon gereset, ondanks de resetdatum van 21 september in het antwoord van gisteren. Dat staat al in het geheugen. Deze run gebruikte bewust maar 2 calls om de limiet te sparen.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 35 in PostHog.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten, anders valt de gratis weeklimiet later deze week weer dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
