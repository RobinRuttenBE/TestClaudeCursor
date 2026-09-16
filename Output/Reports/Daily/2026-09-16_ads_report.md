# Meta Ads Rapport, 16 september 2026

**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, 4 calls, geen weeklimiet) en PostHog project STX EU (directe REST-route). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

**Periode:** last 30d = 17 augustus t/m 15 september 2026. Account `act_567892422940728` (Sempertex Ad Account). Het in de command genoemde `act_607231713057715` bestaat niet in dit Pipeboard-profiel.

## Status in één zin

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED. De twee Wholesaler Campagnes (LIT en SWE) zijn gepauzeerd op 4 september om 11:50 en zijn de enige met levering in de afgelopen 30 dagen. Meta geeft voor last 7d (9 t/m 15 september) nul rijen. PostHog bevestigt dat: na 4 september nog 5 nalopers (6, 7 en 9 september), daarna nul betaald verkeer op 10 t/m 15 september. Laatste wholesaler-inzending blijft 4 september. Op 15 september kwamen 2 organische bezoekers op /become-a-distributor, nul via ads.

## Overzicht per campagne (last 30d)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 | n.v.t. |
| **Totaal** | | **€1.069,38** | **130.155** | **2.854** | **2,2%** | **€0,37** | **€8,22** | | **19** | **24 (+11 zonder UTM = 35)** | **€30,55 all-in** | |

ROAS is niet van toepassing: beide campagnes hebben objective OUTCOME_LEADS, er zijn geen purchase-acties. Kosten per inzending zijn op PostHog `wholesaler_form_submit` gebaseerd, omdat de Meta pixel op deze pagina structureel te weinig telt (19 Meta leads tegenover 35 echte inzendingen).

Overige 5 campagnes (2026: SYBB, 2026: SYBB - Kopie, Last push Nozzle Up, Nozzle Up END OF AUGUST, Campagne Nozzle Up 2025 1) staan op PAUSED zonder spend in de periode.

## Ad-level (last 30d), gesorteerd op spend

| Ad | Spend | Imp. | Clicks | CTR | CPC | CPM | Freq. | Link clicks | LPV (Meta) | Sessies (PostHog) | Inzendingen | Sessie → inz. | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 242 | 28 | 248 | 5 | 2,0% | €29,38 | |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 163 | 27 | 134 | 4 | 3,0% | €36,06 | CTR 1,0% (drempel 1%) |
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 179 | 21 | 141 | 5 | 3,5% | €28,75 | CPC €0,58 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 286 | 62 | 256 | 4 | 1,6% | €32,03 | |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 297 | 45 | 292 | 2 | 0,7% | €63,63 | Laagste conversie |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 114 | 19 | 97 | 2 | 2,1% | €63,50 | CPC €0,69 + CPM €17,07 |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 139 | 31 | 113 | 0 | 0,0% | n.v.t. | CPC €0,53 + CPM €15,27 + 0 inz. |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 157 | 44 | 131 | 2 | 1,5% | €62,68 | |

Daarnaast 11 inzendingen zonder UTM-koppeling (direct, organisch of sessiekoppeling verloren).

## Underperformers

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Twee inzendingen op 97 sessies, €63,50 per inzending. Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Wholesaler Campagne (LIT)**, campagneniveau: frequency 3,97 (drempel 3,5). Publiek verzadigd. Aanbeveling: verse creatives of breder publiek bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) en hoogste sessievolume (292), maar kortste sessies (52s gemiddeld) en 0,7% conversie, €63,63 per inzending. Aanbeveling: hook trekt clickers, geen leads. Nieuwe hook of andere doelgroep testen.
- **Video 2 (LIT)** (CPC €0,58) en **Statisch 1 (LIT)** (CTR 1,0%) raken een drempel, maar zijn de twee beste converteerders (3,5% en 3,0%) en zitten onder €37 per inzending. Aanbeveling: behouden, niet mechanisch pauzeren op CPC of CTR alleen.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03
- **Beste sessie-naar-inzending**: Video 2 (LIT) 3,5%, Statisch 1 (LIT) 3,0%
- **Beste ROAS**: n.v.t. (lead-campagnes)

## Funnel /become-a-distributor (PostHog, 30d)

| Stap | Events | Sessies |
|---|---|---|
| wholesaler_page_view | 1.746 | 1.418 |
| wholesaler_form_start | 137 | 129 |
| wholesaler_form_error | 21 | 11 |
| wholesaler_form_submit | 35 | 32 |
| wholesaler_booking_view | 35 | 32 |
| wholesaler_faq_open | 178 | 39 |

Pageview → formulierstart: 9,1% van de sessies. Formulierstart → inzending: 24,8%. Het grootste lek zit tussen start en inzending: 97 van 129 startende sessies haken af, 11 daarvan met een formulierfout. Dat eerst fixen vóór er weer budget op gaat.

## Betaald verkeer per dag sinds de pauze (PostHog)

| Dag | Betaalde sessies | Echte bezoekers (pageview > 0) |
|---|---|---|
| 4 sep | 58 | 48 |
| 5 sep | 0 | 0 |
| 6 sep | 2 | 1 |
| 7 sep | 1 | 0 |
| 8 sep | 0 | 0 |
| 9 sep | 2 | 2 |
| 10 t/m 15 sep | 0 | 0 |

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, 17 augustus t/m 15 september 2026). Alles vóór 4 september uitgegeven.
- **Beste performer**: Video 2 (LIT). Hoogste sessie-naar-inzending (3,5%) en laagste kosten per inzending (€28,75), ondanks een CPC boven drempel. Leads, niet clicks, bepalen de winnaar.
- **Slechtste performer**: Video 1 (SWE). €126,75 uitgegeven, nul inzendingen, CPC en CPM beide boven drempel.
- **Aanbeveling (70-20-10) bij herstart**: 70% van het budget naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de LIT-verzadiging. 20% naar een Zweedse variant van Video 2 (LIT), de beste converteerder. 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Herstart pas nadat het formulier-lek (start → inzending 24,8%, 21 fouten) is aangepakt.
- **Openstaand**: de herstart-voorstellen van 3 september wachten nog op goedkeuring van Robin.

## Wijzigingen t.o.v. gisteren (15 september)

Geen. Zelfde status, zelfde 30d-cijfers per campagne en per ad, zelfde 35 inzendingen. Pageviews op de distributeurspagina stegen van 1.744 naar 1.746 door 2 organische bezoekers op 15 september. Meta last 7d blijft leeg.

## Google Sheet

Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker". Dit rapport is alleen lokaal opgeslagen.
