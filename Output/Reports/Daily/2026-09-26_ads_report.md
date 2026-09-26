Het rapport staat in `Output/Reports/Daily/2026-09-26_ads_report.md`, gecommit en gepusht (dd2c2f51). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 5 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 26 september 2026

**Pipeboard zit dicht tot maandag.** De eerste call kreeg `weekly_limit_exceeded` (30 van 30 wekelijkse executions op het gratis plan, reset 28 september 00:00 UTC). Geen tweede call gedaan. De Meta-cijfers komen uit het laatste live extract van 24 september. Dat is veilig: alle campagnes staan sinds 4 september op PAUSED en PostHog bevestigt live nul betaalde sessies sinds 9 september. Morgen valt 27 augustus uit het 30d-venster, dan dalen de LIT-cijfers zonder dat er iets veranderde.

**Er draait nog steeds niets.** Alle 7 campagnes PAUSED. Laatste betaalde sessies: 2 op 9 september.

**Overzicht per campagne (last 30d, 27 aug t/m 25 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 23 (+12 organisch) | €46,49 |

ROAS niet van toepassing, lead-campagnes. De volledige per-ad tabel (8 ads, 11 kolommen) staat in het bestand en is met grep gecontroleerd.

**Underperformers** (bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%). Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (live):** 30d staat op 142 formulierstarts, 22 fouten (15,5%), 35 inzendingen in 32 sessies. Laatste 7 dagen: 21 pageviews, 4 starts, 1 inzending. Geen nieuwe inzending sinds Malta op 20 september. Organisch 2 tot 6 sessies per dag op de pagina, geen enkele betaald.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Eerst het formulierlek en het pixel-lead-event fixen (Meta telt 19 van de 32 inzendingen). Voorstel 6 van 22 september (één gedeeld Meta-extract per dag voor de drie rapporten) is nu urgent: de 30 calls zijn op vrijdag al op. De zeven voorstellen wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
