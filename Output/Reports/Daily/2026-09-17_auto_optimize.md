Rapport staat in `Output/Reports/Daily/2026-09-17_auto_optimize.md`, gecommit en gepusht (ec7aa520). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call al op de weeklimiet (30 van 30, reset 21 september). De campagnestatus komt uit het live extract van gisteren 09:03.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 10 september, nul formulierstarts, nul inzendingen. Gisteren 9 organische pageviews op de distributeurspagina. Laatste betaalde inzending blijft 4 september, veertiende dag zonder levering.

**De zes voorstellen staan ongewijzigd en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Dit is de derde run vandaag die op de limiet stuit.

Eén observatie: de opgeslagen dagrapporten bevatten geen per-ad tabellen met link-metrics, dus de 70-20-10 indeling draait nu op campagne-cijfers van 6 september plus kosten per inzending per ad. Bij de volgende live ad-level call sla ik die tabel expliciet op.

Geef aan welke nummers ik mag uitvoeren.
