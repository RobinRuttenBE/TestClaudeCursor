# Meta Ads Rapport, 26 september 2026

**Bronnen:** Pipeboard Meta Ads (directe JSON-RPC route, 1 call) en PostHog project STX EU 149694 (directe REST-route, 5 sessions/events queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven. Stap 6 (Google Sheet) overgeslagen op verzoek.

## Databeschikbaarheid

- **Pipeboard: weeklimiet vol.** De eerste call (`get_campaigns`, account act_567892422940728) kreeg `weekly_limit_exceeded`: 30 van 30 wekelijkse tool executions op het gratis plan, reset maandag 28 september 2026 00:00 UTC. Geen tweede call gedaan. De Meta-cijfers hieronder komen uit het laatste live extract (24 september, venster 25 augustus t/m 24 september) dat op 16, 21, 22 en 24 september identiek was.
- **Waarom dat veilig is:** alle campagnes staan sinds 4 september op PAUSED en PostHog bevestigt live nul betaalde sessies sinds 9 september. Zonder levering veranderen spend, impressies en clicks niet. Het huidige 30d-venster (27 augustus t/m 25 september) bevat nog de eerste leveringsdag (27 augustus), dus de totalen kloppen nog. Vanaf morgen (27 september) valt 27 augustus eruit en dalen de LIT-cijfers zonder dat er iets veranderde.
- **PostHog: live.** Zowel de sessions- als de events-tabel antwoordde binnen 2 seconden.
- **Account act_607231713057715 (Robin Rutten):** bestaat niet in Pipeboard (bevestigd in eerdere runs). Tweede account act_1489853856181844 (AmbitionAvenue) is leeg.

## Status

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Laatste betaalde sessies in PostHog: 2 op 9 september. Nul betaalde sessies van 10 t/m 25 september (17 dagen). SYBB-campagne `2026: SYBB` (120239435987290239) is gepauzeerd sinds 19 april 2026.

## Overzicht per campagne (last 30d, 27 augustus t/m 25 september)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 | n.v.t. |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 23 via ad (+12 zonder UTM = 35) | €46,49 via ad, €30,55 all-in | n.v.t. |

ROAS niet van toepassing: het zijn lead-campagnes zonder aankoopwaarde. Meta telt 19 leads, PostHog telt 32 sessies met een inzending (35 submit-events). Het Meta pixel-lead-event telt structureel te weinig.

De overige 5 campagnes (waaronder 2026: SYBB) hadden in het venster geen spend en staan niet in de tabel.

## Per ad (last 30d, laatste live extract)

| Ad | Campagne | Spend | CTR | CPC | CPM | PostHog sessies | Inz. | Conv. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | LIT | €146,91 | 2,4% | €0,32 | €7,72 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | LIT | €143,74 | 1,4% | €0,58 | €8,32 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | LIT | €144,24 | 1,0% | €0,49 | €5,07 | 134 | 4 | 3,0% | €36,06 | |
| Statisch 2 (LIT) | LIT | €127,25 | 2,4% | €0,20 | €4,87 | 292 | 2 | 0,7% | €63,63 | |
| Video 1 (SWE) | SWE | €126,75 | 2,9% | €0,53 | €15,27 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM |
| Video 2 (SWE) | SWE | €127,00 | 2,5% | €0,69 | €17,07 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | SWE | €125,36 | 2,7% | €0,45 | €12,22 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | SWE | €128,13 | 4,0% | €0,24 | €9,66 | 256 | 3 | 1,2% | €42,71 | |

Drempels: CPC boven €0,50, CTR onder 1%, frequency boven 3,5, CPM boven €15.

## Underperformers (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Aanbeveling: niet herstarten in deze vorm, budget naar €0,00.
- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15), nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Campagne Wholesaler (LIT)**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives vóór herstart.
- **Video 2 (LIT)**: CPC €0,58 (drempel €0,50), maar beste converteerder (3,5%) en laagste kosten per inzending. Aanbeveling: behouden, niet mechanisch pauzeren.
- **Statisch 1 (LIT)**: CTR 1,0% zit precies op de drempel. Aanbeveling: nieuwe hook testen, conversie (3,0%) is goed.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie en kortste sessieduur. Aanbeveling: nieuwe hook testen, huidige hook trekt klikkers die niet invullen.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

## Funnel /become-a-distributor (PostHog, live)

| Periode | Pageviews | Formulierstarts | Fouten | Inzendingen (events) | Inzendingen (sessies) |
|---|---|---|---|---|---|
| 30d (27 aug t/m 25 sep) | 1.682 | 142 | 22 (15,5%) | 35 | 32 |
| 7d (19 t/m 25 sep) | 21 | 4 | 1 | 1 | 1 |

Inzendingen per dag: 27 t/m 31 augustus 4 tot 6 per dag (campagne live), 1 t/m 4 september 1 tot 3 per dag, daarna alleen 18 en 20 september (elk 1, organisch). Geen nieuwe inzending sinds Malta op 20 september. Organisch verkeer op de pagina: 2 tot 6 sessies per dag (17 t/m 25 september), geen enkele betaald.

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, 27 augustus t/m 25 september; alles vóór 5 september)
- **Beste performer**: Video 2 (LIT), €28,75 per inzending bij 3,5% conversie. Video 1 (LIT) direct erachter met €29,38 en de meeste sessies van de LIT-video's.
- **Slechtste performer**: Video 1 (SWE), €126,75 uitgegeven, 113 sessies, nul inzendingen, en boven beide kostendrempels.
- **Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Eerst het formulierlek (15,5% fouten) en het pixel-lead-event fixen (Meta telt 19 van de 32 inzendingen) vóór er weer budget op gaat.
- **Pipeboard-limiet**: tot maandag 28 september is er geen live Meta-data. Voorstel 6 van 22 september (één gedeeld Meta-extract per dag voor de drie rapporten) is nu urgent: 30 calls per week zijn op vrijdag al op.

De zeven voorstellen van 22 september wachten nog op goedkeuring.

## Google Sheet

Overgeslagen op verzoek. Niets geschreven naar "Meta Ads Tracker".

---
*Databronnen: Pipeboard Meta Ads directe JSON-RPC (1 call, weekly_limit_exceeded, cijfers uit live extract 24 september), PostHog REST eu.posthog.com project 149694 (5 queries, live). Gegenereerd 26 september 2026, circa 09:00 CEST.*
