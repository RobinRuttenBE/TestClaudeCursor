Het rapport staat in `Output/Reports/Daily/2026-09-24_auto_optimize.md`, gecommit en gepusht (0435a0b3). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route, 6 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** De ad-level call over 21 t/m 23 september gaf nul rijen. Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn geen `update_ad` calls gedaan. Eenentwintigste dag zonder levering.

**Beide bronnen waren live.** De Pipeboard MCP-tools melden "requires authentication", maar de directe route met dezelfde token werkte in de eerste poging. PostHog bevestigt nul betaalde sessies van 14 t/m 24 september en geen nieuwe inzendingen sinds Malta op 20 september. Weekverbruik Meta staat op circa 5 van 30.

**De per-ad link-tabel staat nu echt in het bestand.** De rapporten van 21, 22 en 24 september (ads-report) bevatten alleen de chatsamenvatting, ondanks de tekst dat de tabel erin stond. Iets in de rapportflow overschrijft het bestand. Dit bestand is gecontroleerd met grep.

**Wat de 30d link-metrics laten zien** (25 augustus t/m 23 september, ongewijzigd sinds 16 september):

- Alleen Statisch 2 (SWE) haalt beide Core-drempels: Link CTR 2,2%, CPC (link) €0,45, maar kreeg 12,0% van het budget.
- Statisch 1 (LIT) zit met Link CTR 0,6% onder de kill-drempel en zou bij herstart mechanisch gepauzeerd worden, terwijl het met €36,06 per inzending de derde beste converteerder is.
- Beide SWE-video's vallen af: CPM boven €15,00, CPC (link) €0,91 en €1,11, samen 2 inzendingen op €253,75.
- De link-metric ranking en de conversie-ranking spreken elkaar tegen. Op kosten per inzending winnen Video 2 (LIT), Video 1 (LIT) en Statisch 1 (LIT). Daarom geen mechanische budget-shift.

**Zeven voorstellen wachten op je goedkeuring**, dezelfde als op 22 september:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met bedragen per ad en beide SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout (15,6%) en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten.
7. Nieuwe 70-20-10 drempels op link-metrics.

Geef aan welke nummers ik mag uitvoeren.
