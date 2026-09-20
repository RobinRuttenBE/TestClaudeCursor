Het rapport staat in `Output/Reports/Daily/2026-09-20_auto_optimize.md`, gecommit en gepusht (c16889ff). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call op de weeklimiet (30 van 30). De reset is vannacht, 21 september 00:00 UTC. Campagnestatus en per-ad cijfers komen uit het extract van 16 september.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies sinds 9 september. De enige beweging is organisch: na Letland op 18 september kwam vanochtend een inzending uit Malta binnen, vermoedelijk direct met aangemaakt klantaccount.

**Waarschuwingen** zijn ongewijzigd en gelden bij herstart: frequency 3,97 op LIT, CPM boven €15,00 op beide SWE-video's, en 0,7% conversie op Statisch 2 (LIT).

**De zes voorstellen staan open**, met één nieuwe aanvulling op nummer 3: Malta als testland in de Experimental-laag, naast Letland.

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Variaties op Statisch 2 (SWE), Video 2 (LIT) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop, plus Letland en Malta toevoegen.
4. Conversie-guard op de kill-regels zodat de beste converteerders niet op dag 1 na herstart sneuvelen.
5. Funnel fix vóór herstart: 24,8% van de formulierstarters komt door.
6. Eén gedeeld Meta-extract per dag cachen. Auto-optimize stuitte deze week vijf keer op de limiet.

Morgen draait auto-optimize weer live en slaat de per-ad Link CTR en CPC (link) tabel op als markdown. Geef aan welke nummers ik mag uitvoeren.
