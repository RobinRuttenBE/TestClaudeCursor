Het rapport staat in `Output/Reports/Daily/2026-09-21_ads_report.md`, gecommit en gepusht (5c5047b5). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 4 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 21 september 2026

**Meta was vandaag weer live bereikbaar.** De Pipeboard-weeklimiet is vannacht gereset. Alle Meta-cijfers zijn vers opgehaald en identiek aan het extract van 16 september. De per-ad tabel staat nu als markdown in het rapportbestand, zodat latere runs erop kunnen terugvallen als de limiet weer dichtgaat.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Achttiende dag zonder levering. PostHog bevestigt: laatste betaalde sessies op 9 september, nul sinds.

**Overzicht per campagne (last 30d, 22 aug t/m 20 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 (23 via ad, 9 zonder UTM) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. SWE staat op 7 inzendingen via ad in plaats van 8: de sessie-join telt unieke sessies, eerdere rapporten telden submit-events. Het all-in totaal van 35 is ongewijzigd.

**Per ad** (volledige tabel met 15 kolommen in het bestand)

| Ad | Spend | CTR | CPC | CPM | Sessies | Inz. | Conv. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 2,4% | €0,32 | €7,72 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | €143,74 | 1,4% | €0,58 | €8,32 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | €144,24 | 1,0% | €0,49 | €5,07 | 134 | 4 | 3,0% | €36,06 | |
| Statisch 2 (LIT) | €127,25 | 2,4% | €0,20 | €4,87 | 292 | 2 | 0,7% | €63,63 | |
| Video 1 (SWE) | €126,75 | 2,9% | €0,53 | €15,27 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM |
| Video 2 (SWE) | €127,00 | 2,5% | €0,69 | €17,07 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | €125,36 | 2,7% | €0,45 | €12,22 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | €128,13 | 4,0% | €0,24 | €9,66 | 256 | 3 | 1,2% | €42,71 | |

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC boven drempel, maar beste converteerder. Behouden, niet mechanisch pauzeren.
- **Statisch 2 (LIT)**: goedkoopste clicks, maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (30d, live):** 1.699 pageviews, 141 formulierstarts, 22 fouten, 35 inzendingen. Van start naar inzending komt 24,8% door. Sinds de pauze twee organische inzendingen (Letland 18 september, Malta 20 september) en op 20 september nog een formulierfout. Het formulier hapert dus ook zonder betaald verkeer.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
