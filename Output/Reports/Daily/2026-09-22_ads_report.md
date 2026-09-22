Het rapport staat in `Output/Reports/Daily/2026-09-22_ads_report.md`, gecommit en gepusht (d0318806). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 2 sessions-queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 22 september 2026

**Meta was live bereikbaar.** Weekverbruik Pipeboard staat na deze run op 11 van 30 calls. Beide insights-calls hadden één retry nodig (eerste poging hing), daarna kwam alles binnen 20 seconden.

**PostHog events-queries hingen vandaag op beide routes.** Sessions-queries werkten wel. De funnelcijfers (formulierstarts, fouten, inzendingen) komen daarom uit het rapport van gisteren. Zonder levering veranderen die niet, behalve door organische inzendingen.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Negentiende dag zonder levering. PostHog bevestigt: nul betaalde sessies sinds 10 september.

**Overzicht per campagne (last 30d, 23 aug t/m 21 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 all-in | €30,55 all-in |

Cijfers identiek aan 21 en 16 september. ROAS niet van toepassing, het zijn lead-campagnes. De volledige per-ad tabel met 17 kolommen staat in het bestand.

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder. Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor:** organisch lopen er 1 tot 8 sessies per dag over de pagina (live, sinds 15 september), allemaal zonder betaald verkeer. Of daar op 21 september een nieuwe inzending bij zat kon ik niet bevestigen omdat de events-tabel niet antwoordde. Laatste bekende stand 30d: 141 formulierstarts, 22 fouten, 35 inzendingen.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
