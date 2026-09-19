Het rapport staat in `Output/Reports/Daily/2026-09-19_auto_optimize.md`, gecommit en gepusht (5d5999f6). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call op de weeklimiet (30 van 30, reset maandag 21 september). De campagnestatus komt uit het live extract van 16 september. Ik heb verder geen Meta-calls gedaan.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies sinds 9 september, nul sessies op de distributeurspagina vandaag. De enige beweging is de organische inzending van 18 september uit Letland, die vanochtend ook al in het ads-rapport stond.

**Waarschuwingen** komen uit het extract van 16 september en gelden bij herstart in de huidige vorm: frequency 3,97 op de LIT-campagne, CPM boven €15,00 op beide SWE-video's, en 0,7% conversie op Statisch 2 (LIT).

**De zes voorstellen staan ongewijzigd open**, met één aanvulling op nummer 3: Letland toevoegen aan de LIT-targeting bij herstart, op basis van die eerste Letse inzending ooit.

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Variaties op Statisch 2 (SWE), Video 2 (LIT) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop, plus Letland toevoegen.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: 24,6% van de formulierstarters komt door.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Dit is de vierde dag deze week dat auto-optimize op de limiet stuit.

Geef aan welke nummers ik mag uitvoeren.
