# Meta Ads Rapport, 24 september 2026

**Periode:** last 30d (25 augustus t/m 23 september 2026)
**Bronnen:** Pipeboard Meta Ads (directe JSON-RPC route, 3 calls) en PostHog project STX EU (directe REST-route, 6 queries). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.
**Accounts:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet.

## Status

- **Er draait niets.** Alle 7 campagnes staan op PAUSED. De twee Wholesaler Campagnes zijn op 4 september gepauzeerd, vandaag is dag 20 zonder levering.
- **PostHog bevestigt:** de laatste betaalde sessies waren 2 nalopers op 9 september. Sindsdien nul betaalde sessies.
- **Cijfers ongewijzigd** ten opzichte van 16, 21 en 22 september. Het 30d-venster dekt nog de volledige leverperiode (27 augustus t/m 4 september). Vanaf de run van 27 september valt 27 augustus uit het venster en beginnen de LIT-cijfers te dalen zonder dat er iets gebeurt.
- **PostHog events-tabel antwoordde normaal** (alle queries onder 5 seconden), dus de funnelcijfers zijn vandaag live, niet overgenomen.

## Overzicht per campagne (30d)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. (PostHog) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal betaald** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 23 | €46,49 |
| Totaal all-in (incl. 12 organische) | | €1.069,38 | | | | | | | | 35 | €30,55 |

ROAS is niet van toepassing, dit zijn lead-campagnes. De overige 5 campagnes (2026: SYBB, 2026: SYBB - Kopie, drie Nozzle Up campagnes) hadden nul spend in het venster.

## Per ad (30d)

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Link clicks | Meta LPV | Meta leads | PostHog sessies | PostHog inz. | Sessie → inz. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 242 | 28 | 3 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 179 | 21 | 4 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 163 | 27 | 3 | 135 | 4 | 3,0% | €36,06 | CTR (rand) |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 297 | 45 | 1 | 292 | 2 | 0,7% | €63,63 | conversie |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 139 | 31 | 0 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM, 0 inz. |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 114 | 19 | 1 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 157 | 44 | 2 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 286 | 62 | 5 | 256 | 3 | 1,2% | €42,71 | |

PostHog sessies zijn betaalde sessies (utm_medium=paid) per utm_content in het venster. PostHog inzendingen zijn unieke sessies met een wholesaler_form_submit, gekoppeld via de sessie-UTM. Meta LPV telt structureel te laag (121 plus 156 tegenover 1.413 PostHog sessies), dus baseer funnelconclusies nooit op Meta LPV.

## Underperformers (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27 boven drempel, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Campagne LIT**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives voordat LIT opnieuw aan gaat.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste sessie-naar-inzending ratio (3,5%) en laagste kosten per inzending. Aanbeveling: behouden, niet mechanisch pauzeren op CPC.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie. Aanbeveling: nieuwe hook testen, huidige creative trekt het verkeerde publiek.
- **Statisch 1 (LIT)**: CTR 1,0% zit precies op de drempel. Aanbeveling: geen actie, de conversie (3,0%) compenseert.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06
- **Beste ROAS**: niet van toepassing (lead-campagnes)

## Funnel /become-a-distributor (PostHog, live)

| Metric | 30d (25 aug t/m 23 sep) |
|---|---|
| wholesaler_page_view | 1.710 |
| Formulierstarts | 141 |
| Formulierfouten | 22 |
| Inzendingen (events) | 35 |
| Inzendingen (unieke sessies) | 32 |
| Betaalde sessies | 1.413 |

Organisch verkeer op de pagina blijft laag: 3 tot 8 sessies per dag in de laatste 8 dagen, allemaal zonder betaald verkeer. Op 23 september waren het 3 sessies. Geen nieuwe inzendingen sinds Malta op 20 september; de laatste twee organische inzendingen blijven Letland (18 september) en Malta (20 september), beide nieuwe markten zonder budget.

Het formulierlek staat nog open: 22 fouten op 141 starts is 15,6%. Dat is de eerste fix voordat er opnieuw budget op gaat.

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alles uit de leverperiode 27 augustus t/m 4 september)
- **Beste performer**: Video 2 (LIT), laagste kosten per inzending (€28,75) en hoogste sessie-naar-inzending ratio (3,5%), ondanks CPC boven drempel
- **Slechtste performer**: Video 1 (SWE), €126,75 uitgegeven, dure reach, nul inzendingen op 113 sessies
- **Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de frequency van 3,97; 20% naar een Zweedse variant van Video 2 (LIT); 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta toevoegen als targeting-kandidaten. Eerst het formulierlek (15,6% fouten) dichten. De zes voorstellen van 3 en 16 september wachten nog op goedkeuring.

## Google Sheet

Overgeslagen op verzoek. Geen write naar de Meta Ads Tracker.
