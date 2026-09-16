Rapport staat in `Output/Reports/Daily/2026-09-16_auto_optimize.md`, gecommit en gepusht (c9f23b93). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta gaf vanochtend nul rijen voor 9 t/m 15 september. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan. 0 van 0 actieve ads gepauzeerd.

**Meta was deze run niet vers bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call al op de weeklimiet (30 van 30, reset 21 september). Het ads-rapport van 09:03 had de Meta-data nog live, dus de campagnestatus komt daaruit. De SYBB-run daarna verbruikte de laatste calls.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 10 september, nul formulierstarts, nul inzendingen. Alleen 14 organische pageviews op de distributeurspagina in zeven dagen. Laatste betaalde inzending blijft 4 september, dertiende dag zonder levering.

**De zes voorstellen staan ongewijzigd en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Vandaag was de limiet op woensdag al vol, dus dit wordt urgent als er weer ads draaien.

Geef aan welke nummers ik mag uitvoeren.
