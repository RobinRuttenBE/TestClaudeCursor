Het rapport staat in `Output/Reports/Daily/2026-09-22_auto_optimize.md`, gecommit en gepusht (7234f4fd). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route, 3 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. De ad-level call over 19 t/m 21 september gaf nul rijen, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan. Twintigste dag zonder levering.

**Meta was live bereikbaar.** Beide calls kwamen in de eerste poging binnen 3 seconden terug. Weekverbruik na deze run staat op 13 van 30. De per-ad tabel met Link CTR, CPC (link), Meta leads en PostHog inzendingen staat nu echt als markdown in het rapport. Het bestand van gisteren bevatte alleen de samenvatting, dus dit is de eerste bruikbare fallback-tabel voor als de limiet later deze week dichtgaat.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies van 12 tot en met 22 september. De events-tabel antwoordde vanmiddag weer normaal. Op 21 september geen nieuwe inzending, wat vanochtend nog niet te bevestigen was. De organische inzendingen uit Letland (18 september) en Malta (20 september) blijven de enige sinds de pauze.

**Wat de link-metrics laten zien.** Alleen Statisch 2 (SWE) haalt beide Core-drempels (Link CTR 2,2%, CPC link €0,45), maar kreeg maar 12,0% van het budget. Statisch 1 (LIT) zit met 0,6% Link CTR onder de kill-drempel en zou bij herstart mechanisch gepauzeerd worden, terwijl het met €36,06 per inzending de derde beste converteerder is. Beide SWE-video's vallen af op CPM boven €15,00 en op conversie.

**Zeven voorstellen wachten op je goedkeuring**, dezelfde als gisteren, nu onderbouwd met de live 30d-cijfers:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met concrete bedragen per ad en de twee SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), een Zweedse variant van Video 2 (LIT), nieuwe body voor Video 1 (SWE) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, Statisch 1 (LIT) verengen, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten.
7. Nieuwe 70-20-10 drempels op link-metrics, zodat de indeling overeenkomt met de conversie-ranking.

Geef aan welke nummers ik mag uitvoeren. Voorstel 2 wordt concreter als ik de huidige ad-copy mag ophalen; dat kost één extra Meta-call.
