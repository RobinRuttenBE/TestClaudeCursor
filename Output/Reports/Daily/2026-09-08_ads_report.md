# Meta Ads Rapport, 8 september 2026

**Periode:** last_30d (9 augustus t/m 7 september 2026)
**Account:** Sempertex Ad Account (act_567892422940728). Het in de command genoemde act_607231713057715 bestaat niet in dit Pipeboard-account; act_1489853856181844 (AmbitionAvenue) is leeg.
**Databronnen:** Meta Ads via Pipeboard (directe JSON-RPC, de MCP vroeg om authenticatie) en PostHog project STX EU (directe REST, de MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

## Status

**Geen actieve campagnes.** Alle zeven campagnes in het account staan op PAUSED. De twee Wholesaler campagnes (SWE en LIT) zijn op 4 september gepauzeerd. Meta registreert 0 spend en 0 impressies van 5 t/m 8 september. De laatste PostHog-inzending kwam op 4 september. De losse Video 1 (SWE) sessies op 6 en 7 september zijn geen ad-levering, maar een opgeslagen of gedeelde ad-post.

Ten opzichte van het rapport van 7 september is er niets veranderd behalve dat het venster één dag is opgeschoven. Alle 30-daagse cijfers zijn identiek.

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Reach | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 22.909 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 11.919 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 | n.v.t. |
| 2026: SYBB - Kopie | Paused sinds 27 aug | €0,00 | 0 | 0 | 0 | | | | | 0 | 0 | | |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | 0 | 0 | 0 | | | | | 0 | 0 | | |
| Nozzle Up (3 campagnes, 2025) | Paused sinds sep 2025 | €0,00 | 0 | 0 | 0 | | | | | 0 | 0 | | |

**Totaal:** €1.069,38 spend, 130.155 impressies, 2.854 clicks, 19 Meta leads, 23 PostHog inzendingen met UTM-attributie (plus 9 inzendingen zonder UTM, organisch of attributie verloren). ROAS is niet van toepassing, dit zijn lead-campagnes (OUTCOME_LEADS) zonder purchase-waarde.

Meta telde 277 landing page views tegenover 1.410 betaalde PostHog-sessies. De Meta pixel telt structureel te weinig op /become-a-distributor. Funnel-conclusies zijn daarom op PostHog gebaseerd.

## Overzicht per ad

| Ad | Spend | Impr. | Clicks | CTR | Link CTR | CPC | CPM | Freq. | Sessies (PH) | Bounce | Inzendingen (PH) | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | 1,0% | €0,58 | €8,32 | 2,52 | 141 | 29,8% | 5 | €28,75 | CPC > €0,50 |
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | 1,3% | €0,32 | €7,72 | 1,90 | 248 | 30,6% | 5 | €29,38 | |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | 0,6% | €0,49 | €5,07 | 2,91 | 134 | 29,1% | 4 | €36,06 | CTR op drempel |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | 2,2% | €0,24 | €9,66 | 1,97 | 256 | 22,3% | 3 | €42,71 | |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | 1,5% | €0,45 | €12,22 | 2,15 | 131 | 19,8% | 2 | €62,68 | |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | 1,5% | €0,69 | €17,07 | 2,02 | 97 | 23,7% | 2 | €63,50 | CPC > €0,50, CPM > €15 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | 1,1% | €0,20 | €4,87 | 2,37 | 290 | 27,9% | 2 | €63,63 | |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | 1,7% | €0,53 | €15,27 | 2,05 | 113 | 20,4% | 0 | geen | CPC > €0,50, CPM > €15, 0 conversies |

Gesorteerd op kosten per inzending. Sessies, bounce en inzendingen komen uit PostHog (koppeling via utm_content).

## Underperformers

- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15,00) en 0 inzendingen op 113 sessies. Aanbeveling: definitief uit, niet herstarten.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. €63,50 per inzending. Aanbeveling: niet herstarten, budget naar Statisch 2 (SWE).
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar de beste kosten per inzending van alle ads (€28,75). Aanbeveling: behouden, de CPC-vlag is hier geen kill-reden.
- **Wholesaler Campagne (LIT)**: frequency 3,97 (drempel 3,5). Inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer. Creative fatigue. Aanbeveling: bij herstart minimaal één nieuwe creative per markt toevoegen.
- **Statisch 1 (LIT)**: CTR 1,0% op de drempel, link CTR 0,6%. Toch €36,06 per inzending en de hoogste sessie-naar-inzending ratio (3,0%). Aanbeveling: behouden, niet pauzeren op CTR alleen.
- **Statisch 2 (LIT)**: laagste CPC van het account, maar 290 sessies leveren maar 2 inzendingen op (0,7%). Goedkope clicks van lage kwaliteit. Aanbeveling: budget verlagen ten gunste van Video 1 en 2 (LIT).

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Laagste CPM**: Statisch 2 (LIT), €4,87
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, gevolgd door Video 1 (LIT) €29,38
- **Beste ROAS**: niet van toepassing, lead-campagnes

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: 9 augustus t/m 7 september 2026). Sinds 5 september €0,00.
- **Beste performer**: Wholesaler Campagne (LIT). Helft van de spend, 16 van de 23 geattribueerde inzendingen, €35,13 per inzending. Binnen LIT zijn Video 1 en Video 2 de bewezen winnaars.
- **Slechtste performer**: Video 1 (SWE). Boven drempel op CPC en CPM en geen enkele inzending in 30 dagen.
- **Aanbeveling (70-20-10)**: bij herstart 70% van het budget naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE) als beste Zweedse ad, 10% naar één nieuwe creative per markt om de frequentie van 3,97 te doorbreken. Beide SWE-video's niet herstarten. De vijf herstart-voorstellen uit het auto-optimize rapport van 3 september staan nog open en worden door deze data bevestigd.

## Google Sheet

Overgeslagen op verzoek. Rapport alleen lokaal opgeslagen in `Output/Reports/Daily/2026-09-08_ads_report.md`.

## Funnel data

Gesprekken gepland, distributeurs geactiveerd en eerste orders per markt zitten niet in Meta of PostHog. Lever die aan voor een volledige funnel-diagnose.
