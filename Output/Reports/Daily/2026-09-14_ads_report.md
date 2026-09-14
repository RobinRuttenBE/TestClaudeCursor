# Meta Ads Rapport, 14 september 2026

**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, live vandaag) en PostHog project STX EU (directe REST-route, live vandaag). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Periode:** last 30 days (15 augustus t/m 13 september 2026). Account: Sempertex Ad Account (act_567892422940728). Het in het command genoemde act_607231713057715 bestaat niet.

## Status

**Er draait niets.** Alle 7 campagnes in het account staan op PAUSED. De twee Wholesaler Campagnes (LIT en SWE) zijn op 4 september om 11:50 gepauzeerd. Meta geeft voor last_7d nul rijen, dus geen levering sinds 4 september. PostHog bevestigt dat: na 4 september nog 5 nalopers in totaal (6, 7 en 9 september), nul betaald verkeer op 10 t/m 13 september. Laatste inzending: 4 september 06:41 UTC.

Pipeboard werkte vandaag weer normaal (weeklimiet reset op maandag, ondanks de resetdatum 21 september in het antwoord van gisteren). De Meta-cijfers hieronder zijn daardoor vandaag vers opgehaald, niet uit het extract van 7 september.

| Campagne | Status | Sinds | Objective |
|---|---|---|---|
| Wholesaler Campagne (SWE) | PAUSED | 4 sep 2026 | Leads |
| Wholesaler Campagne (LIT) | PAUSED | 4 sep 2026 | Leads |
| 2026: SYBB - Kopie | PAUSED | 27 aug 2026 | Sales |
| 2026: SYBB | PAUSED | 19 apr 2026 | Sales |
| Last push Nozzle Up | PAUSED | 21 sep 2025 | Sales |
| Nozzle Up END OF AUGUST | PAUSED | 15 sep 2025 | Sales |
| Campagne Nozzle Up 2025 1 | PAUSED | 15 sep 2025 | Sales |

## Overzicht per campagne (last 30d, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 | n.v.t. |
| **Totaal** | | **€1.069,38** | **130.155** | **2.854** | **2,2%** | **€0,37** | **€8,22** | | **19** | **23 (+12 zonder UTM-match)** | **€30,55 all-in** | |

ROAS is niet van toepassing, het zijn lead-campagnes zonder aankoopwaarde. Meta telt 19 leads, PostHog 35 inzendingen op /become-a-distributor in dezelfde 30 dagen. Kosten per inzending zijn op PostHog gebaseerd (Meta pixel telt structureel te weinig op deze pagina). 23 inzendingen zijn aan een ad te koppelen via utm_content, 12 niet (9 zonder UTM plus 3 zonder sessiematch).

## Ad-level (last 30d)

| Ad | Spend | Impr. | CTR | CPC | CPM | Freq. | Link clicks | Meta LPV | PostHog sessies | Gem. duur | Inzendingen | Sessie → inzending | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 2,4% | €0,32 | €7,72 | 1,90 | 242 | 28 | 216 | 69s | 5 | 2,3% | €29,38 |
| Statisch 1 (LIT) | €144,24 | 28.434 | 1,0% | €0,49 | €5,07 | 2,91 | 163 | 27 | 106 | 103s | 4 | 3,8% | €36,06 |
| Video 2 (LIT) | €143,74 | 17.267 | 1,4% | €0,58 | €8,32 | 2,52 | 179 | 21 | 123 | 96s | 5 | 4,1% | €28,75 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 4,0% | €0,24 | €9,66 | 1,97 | 286 | 62 | 230 | 114s | 3 | 1,3% | €42,71 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 2,4% | €0,20 | €4,87 | 2,37 | 297 | 45 | 250 | 52s | 2 | 0,8% | €63,63 |
| Video 2 (SWE) | €127,00 | 7.441 | 2,5% | €0,69 | €17,07 | 2,02 | 114 | 19 | 84 | 74s | 2 | 2,4% | €63,50 |
| Video 1 (SWE) | €126,75 | 8.299 | 2,9% | €0,53 | €15,27 | 2,05 | 139 | 31 | 97 | 75s | 0 | 0,0% | geen |
| Statisch 1 (SWE) | €125,36 | 10.262 | 2,7% | €0,45 | €12,22 | 2,15 | 157 | 44 | 116 | 210s | 2 | 1,7% | €62,68 |

PostHog sessies zijn sessies met minimaal 1 pageview. Meta LPV (landing page view) blijft ver onder PostHog: 277 LPV tegenover 1.222 echte sessies.

## Underperformers

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Duurste ad van de set, €63,50 per inzending. Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27, beide boven drempel, en 0 inzendingen op 97 sessies. Aanbeveling: definitief uit.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar hoogste sessie-naar-inzending ratio (4,1%) en laagste kosten per inzending (€28,75). Aanbeveling: behouden, de CPC-vlag weegt hier niet op tegen de conversie.
- **Statisch 1 (LIT)**: CTR 1,0% op de drempel, maar 3,8% conversie en lange sessies (103s). Aanbeveling: behouden, niet mechanisch pauzeren op CTR.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies (52s) en 0,8% conversie, €63,63 per inzending. De hook trekt clickers, geen wholesalers. Aanbeveling: nieuwe hook testen.
- **Campagne LIT als geheel**: frequency 3,97 (drempel 3,5). Publiek verzadigd bij de pauze. Aanbeveling: verse creatives of breder publiek bij herstart.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, daarna Video 1 (LIT) €29,38
- **Beste conversie**: Video 2 (LIT), 4,1% sessie naar inzending

## Funnel /become-a-distributor (PostHog, 30d)

| Stap | Aantal |
|---|---|
| Pageviews | 1.743 |
| Formulierstarts | 137 |
| Inzendingen | 35 |
| Start → inzending | 25,5% |

Betaald verkeer per dag: 156 tot 210 sessies per dag op 31 augustus t/m 3 september, 58 op 4 september (pauzedag), daarna 2, 1 en 2 nalopers op 6, 7 en 9 september. Nul op 10 t/m 13 september.

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alles vóór 4 september)
- **Beste performer**: Video 2 (LIT) en Video 1 (LIT), samen 10 van de 23 gekoppelde inzendingen voor €290,65, circa €29 per inzending
- **Slechtste performer**: Video 1 (SWE), €126,75 uitgegeven, 0 inzendingen, CPC en CPM boven drempel
- **Aanbeveling (70-20-10)**: bij herstart 70% van het budget naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de frequency van 3,97; 20% naar een Zweedse variant van Video 2 (LIT), de beste converteerder; 10% naar een nieuwe hook voor Statisch 2 (LIT). Video 1 en Video 2 (SWE) niet meenemen. De herstart-voorstellen van 3 september wachten nog op goedkeuring van Robin.

## Operationeel

- Pipeboard weeklimiet is vandaag gereset. Vier calls gebruikt in deze run (campaign 30d, ad 30d, campaign 7d, campaign-lijst). Een `get_campaigns` met `status_filter` hing 60 seconden; zonder filter kwam de lijst in seconden terug.
- Het voorstel om één gedeelde Meta-call per dag te cachen voor de drie rapporten (ads, SYBB, auto-optimize) blijft staan, anders valt de route later deze week opnieuw dicht.

## Google Sheet

Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker".
