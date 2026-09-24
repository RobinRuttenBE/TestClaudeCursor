# Morning Report — 2026-09-24

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-24_ads_report.md`, gecommit en gepusht (ea30dcd9). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 6 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 24 september 2026

**Beide bronnen waren live bereikbaar.** De Pipeboard MCP meldt "requires authentication", maar de directe route werkte in één keer. De PostHog events-tabel antwoordde vandaag normaal, dus de funnelcijfers zijn live en niet overgenomen uit een eerder rapport. Het rapport van gisteren was leeg door een API-fout.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Twintigste dag zonder levering. PostHog bevestigt: laatste betaalde sessies waren 2 nalopers op 9 september.

**Overzicht per campagne (last 30d, 25 aug t/m 23 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 all-in | €30,55 all-in |

Cijfers identiek aan 16, 21 en 22 september. ROAS niet van toepassing, het zijn lead-campagnes. De per-ad tabel met 16 kolommen staat in het bestand.

**Let op vanaf 27 september:** dan valt 27 augustus uit het 30d-venster en beginnen de LIT-cijfers te dalen zonder dat de campagne iets deed.

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%). Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (live):** 30d staat op 141 formulierstarts, 22 fouten (15,6%), 35 inzendingen. Organisch lopen er 3 tot 8 sessies per dag over de pagina, geen nieuwe inzendingen sinds Malta op 20 september.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

SYBB rapport niet beschikbaar.

---

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

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
