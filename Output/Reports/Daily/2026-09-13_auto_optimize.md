Rapport staat in `Output/Reports/Daily/2026-09-13_auto_optimize.md`, gecommit en gepusht (734e40fa). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Er is geen levering om de kill-regels op te draaien. Geen ads gepauzeerd, geen `update_ad` calls.

**Beperking:** de eerste Pipeboard call kreeg direct de weeklimiet-melding (100 van 30 calls gebruikt, reset 21 september 00:00 UTC). Live Meta-cijfers over 10 t/m 13 september ontbreken. Campagnestatus komt uit het ads-rapport van vanochtend, ad-level cijfers uit het extract van 7 september.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM op 10, 11, 12 en 13 september, ook per campagne en per ad. Nul inzendingen. Distributeurspagina kreeg 0 tot 8 organische bezoekers per dag. Twaalfde dag zonder levering.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT), plus een nieuwe hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 35 in PostHog.
6. Eén gedeelde Meta-call per dag cachen voor de drie rapporten, anders valt Pipeboard na 21 september binnen 2 dagen opnieuw dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Eerstvolgende run met live Meta-data is op of na 21 september, tenzij Pipeboard eerder naar Pro gaat of je de MCP opnieuw autoriseert via /mcp. Geef aan welke nummers ik mag uitvoeren.
