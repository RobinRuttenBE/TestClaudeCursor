Rapport staat in `Output/Reports/Daily/2026-09-15_auto_optimize.md`, gecommit en gepusht (c1df7ff4). Alleen Pipeboard (directe JSON-RPC route, 3 calls, geen weeklimiet) en PostHog (directe REST-route) gebruikt. Beide MCP-servers zelf weigerden opnieuw. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta geeft over 12 t/m 14 september nul rijen op campagne- en ad-niveau. Alle 7 campagnes staan op PAUSED, de twee Wholesaler campagnes sinds 4 september 11:50. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 12 september, nul wholesaler-inzendingen sinds 8 september. Laatste betaalde inzending blijft 4 september, twaalfde dag zonder levering.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten, anders valt de gratis Pipeboard weeklimiet later deze week weer dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
