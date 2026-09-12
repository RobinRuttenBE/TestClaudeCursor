Rapport staat in `Output/Reports/Daily/2026-09-12_auto_optimize.md`, gecommit en gepusht (62124ca0). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Er is geen levering om de kill-regels op te draaien. Geen ads gepauzeerd, geen `update_ad` calls.

**Beperking:** de allereerste Pipeboard call kreeg al de weeklimiet-melding (100 van 30 calls gebruikt, reset maandag 14 september). Live Meta-cijfers over 9 t/m 12 september ontbreken dus. De campagnestatus komt uit het ads-rapport van vanochtend, de ad-level cijfers uit het rapport van 7 september.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 8 september, ook op ad-niveau. De paar Facebook- en Instagram-verwijzingen zijn organisch zonder UTM. Distributeurspagina kreeg 1 tot 8 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Tiende dag op rij zonder levering.** De voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT), plus een nieuwe hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.
6. Nieuw: één gedeelde Meta-call per dag cachen voor de drie rapporten, anders valt Pipeboard na maandag opnieuw binnen 2 dagen droog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.
