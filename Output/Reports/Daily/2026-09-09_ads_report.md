## Meta Ads Rapport — 9 september 2026

**Periode:** last 30 days (10 augustus t/m 8 september 2026)
**Account:** Sempertex Ad Account (`act_567892422940728`). Het in het command genoemde `act_607231713057715` bestaat niet in dit Pipeboard-account.
**Databronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, de MCP vroeg om authenticatie) en PostHog project STX EU (directe REST route, de MCP gaf HTTP 405). Geen Google MCPs aangeroepen. Google Sheet niet bijgewerkt (stap 6 overgeslagen op verzoek).

### Status: geen actieve campagnes

Alle zeven campagnes in het account staan op PAUSED. De twee Wholesaler campagnes (SWE en LIT) zijn op 4 september om 11:50 gepauzeerd. Meta registreert 0 spend en 0 impressies op 8 september, en PostHog ziet sinds 5 september maximaal 4 betaalde sessies per dag op de distributeurpagina (restverkeer uit gedeelde of opgeslagen ad-posts). Laatste distributeur-inzending: 4 september.

Ten opzichte van het rapport van 8 september is niets veranderd behalve het 30-daagse venster dat één dag opschoof. De cijfers hieronder zijn daardoor identiek aan gisteren.

Gepauzeerde campagnes (meest recent eerst):

| Campagne | Doel | Gepauzeerd op | Spend last 30d |
|---|---|---|---|
| Wholesaler Campagne (SWE) | Leads | 4 sep 2026 | €507,24 |
| Wholesaler Campagne (LIT) | Leads | 4 sep 2026 | €562,14 |
| 2026: SYBB - Kopie | Sales | 27 aug 2026 | €0,00 |
| 2026: SYBB | Sales | 19 apr 2026 | €0,00 |
| Last push Nozzle Up | Sales | 21 sep 2025 | €0,00 |
| Nozzle Up END OF AUGUST | Sales | 15 sep 2025 | €0,00 |
| Campagne Nozzle Up 2025 1 | Sales | 15 sep 2025 | €0,00 |

### Overzicht per campagne (last 30d)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending (PostHog) | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 | n.v.t. |
| **Totaal** | | **€1.069,38** | **130.155** | **2.854** | **2,2%** | **€0,37** | **€8,22** | | **19** | **23** | **€46,49** | |

ROAS is niet van toepassing: beide campagnes zijn lead-campagnes zonder aankoopwaarde. Meta telde 277 landing page views tegenover 1.407 betaalde PostHog-sessies op de distributeurpagina, dus de Meta pixel meet structureel te weinig. Funnel-conclusies zijn gebaseerd op PostHog. Naast de 23 geattribueerde inzendingen kwamen er 4 binnen zonder UTM.

### Overzicht per ad (last 30d)

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog sessies | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 3 | 248 | 5 | €29,38 |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 3 | 134 | 4 | €36,06 |
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 4 | 141 | 5 | €28,75 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 5 | 256 | 3 | €42,71 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 1 | 290 | 2 | €63,63 |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 1 | 97 | 2 | €63,50 |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 0 | 113 | 0 | n.v.t. |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 2 | 128 | 2 | €62,68 |

### Underperformers

- **Video 1 (SWE)** — CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15,00) en 0 inzendingen op 113 sessies → Aanbeveling: niet herstarten. Enige ad zonder resultaat.
- **Video 2 (SWE)** — CPC €0,69 (drempel €0,50), CPM €17,07 (drempel €15,00), €63,50 per inzending → Aanbeveling: niet herstarten.
- **Video 2 (LIT)** — CPC €0,58 (drempel €0,50), maar beste kosten per inzending (€28,75) → Aanbeveling: behouden. Lead-ads niet mechanisch afrekenen op CPC.
- **Statisch 1 (LIT)** — CTR 1,0% (op de drempel), maar €36,06 per inzending → Aanbeveling: behouden.
- **Wholesaler Campagne (LIT)** — frequency 3,97 (drempel 3,5) → Aanbeveling: bij herstart nieuwe creative toevoegen; inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer, wat op creative fatigue wijst.
- **Statisch 2 (LIT)** — goedkoopste clicks (€0,20) maar 290 sessies leveren maar 2 inzendingen op → Aanbeveling: budget verlagen, de ad trekt clickers maar geen distributeurs.

### Top performers

- **Beste CTR**: Statisch 2 (SWE) — 4,0%
- **Laagste CPC**: Statisch 2 (LIT) — €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes)
- **Beste kosten per inzending**: Video 2 (LIT) — €28,75, gevolgd door Video 1 (LIT) — €29,38

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days). Spend sinds 5 september: €0,00.
- **Beste performer**: Wholesaler Campagne (LIT) — €35,13 per inzending, 16 van de 23 geattribueerde inzendingen, laagste CPM (€6,18).
- **Slechtste performer**: Wholesaler Campagne (SWE) — €72,46 per inzending, twee keer zo duur als LIT; beide SWE-video's zitten boven de CPC- en CPM-drempels.
- **Aanbeveling (70-20-10)**: bij herstart 70% van het budget naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequency van 3,97 te doorbreken. Video 1 en Video 2 (SWE) niet herstarten. De vijf herstart-voorstellen uit het auto-optimize rapport van 3 september staan nog open.

### Google Sheet

Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker". Rapport alleen lokaal opgeslagen.

### PostHog verkeer laatste dagen (context)

| Datum | Betaalde sessies distributeurpagina | Inzendingen | Sessies site totaal |
|---|---|---|---|
| 4 sep | 63 | 1 | – |
| 5 sep | 2 | 0 | 7.595 |
| 6 sep | 4 | 0 | 5.990 |
| 7 sep | 3 | 0 | 1.103 |
| 8 sep | 1 | 0 | 747 |

De piek van 5 en 6 september in het sitetotaal is geen betaald verkeer (0 sessies met Meta-UTM).
