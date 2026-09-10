## Meta Ads Rapport, 10 september 2026

**Databronnen.** De Pipeboard MCP vroeg om authenticatie en de PostHog MCP gaf HTTP 405. Beide werkten via de directe route met de geconfigureerde tokens. Periode: last 30d (11 augustus t/m 9 september 2026). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

**Status: geen actieve campagnes.** Alle zeven campagnes in het Sempertex Ad Account (act_567892422940728) staan op PAUSED. De Wholesaler campagnes (SWE en LIT) zijn sinds 4 september 11:50 uit. Meta registreert €0,00 spend van 5 t/m 9 september. Er is niets gewijzigd in het account sinds 4 september. De SYBB campagnes (2026: SYBB en de kopie) en de drie Nozzle Up campagnes hebben in deze periode geen spend. Het account act_607231713057715 bestaat niet in Pipeboard.

**Vergelijking met gisteren.** Het venster schoof één dag op (10 augustus viel eraf, 9 september kwam erbij). Beide dagen hadden €0,00 spend, dus alle Meta-cijfers zijn identiek aan het rapport van 9 september.

### Overzicht per campagne (last 30d, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused (4 sep) | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused (4 sep) | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 | n.v.t. |
| **Totaal** | | **€1.069,38** | **130.155** | **2.854** | **2,2%** | **€0,37** | **€8,22** | | **19** | **24** | **€44,56** | |

ROAS is niet van toepassing: beide campagnes hebben doel OUTCOME_LEADS, er is geen omzetwaarde in Meta.

**Meting.** Meta telde 277 landing page views tegenover 1.410 betaalde PostHog-sessies op /become-a-distributor. Meta's pixel telt op deze pagina structureel te weinig, dus funnel-conclusies en kosten per inzending zijn op PostHog gebaseerd. PostHog zag in het venster 35 inzendingen: 24 met ad-UTM, 9 zonder UTM tijdens de campagneperiode (browser zonder parameters of terugkerende bezoeker) en 2 op 17 augustus, vóór de campagnestart, dus organisch.

### Overzicht per ad (last 30d)

| Ad | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog sessies | Inzendingen | Sessie → inzending | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 2,4% | €0,32 | €7,72 | 1,90 | 3 | 248 | 5 | 2,0% | €29,38 | |
| Statisch 1 (LIT) | €144,24 | 1,0% | €0,49 | €5,07 | 2,91 | 3 | 134 | 4 | 3,0% | €36,06 | CTR net boven 1% |
| Video 2 (LIT) | €143,74 | 1,4% | €0,58 | €8,32 | 2,52 | 4 | 141 | 5 | 3,5% | €28,75 | CPC > €0,50 |
| Statisch 2 (SWE) | €128,13 | 4,0% | €0,24 | €9,66 | 1,97 | 5 | 256 | 4 | 1,6% | €32,03 | |
| Statisch 2 (LIT) | €127,25 | 2,4% | €0,20 | €4,87 | 2,37 | 1 | 292 | 2 | 0,7% | €63,63 | Lage conversie |
| Video 2 (SWE) | €127,00 | 2,5% | €0,69 | €17,07 | 2,02 | 1 | 97 | 2 | 2,1% | €63,50 | CPC > €0,50, CPM > €15 |
| Video 1 (SWE) | €126,75 | 2,9% | €0,53 | €15,27 | 2,05 | 0 | 113 | 0 | 0,0% | n.v.t. | CPC > €0,50, CPM > €15, 0 inzendingen |
| Statisch 1 (SWE) | €125,36 | 2,7% | €0,45 | €12,22 | 2,15 | 2 | 128 | 2 | 1,6% | €62,68 | |

Inzendingen per ad zijn vandaag gekoppeld via de UTM-parameters op het inzendevent zelf. Gisteren liep de koppeling via de sessie-entry, vandaar 8 in plaats van 7 voor SWE. Het beeld is hetzelfde.

### Underperformers

- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15,00) en 0 inzendingen op 113 sessies. Aanbeveling: niet herstarten.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, €63,50 per inzending. Aanbeveling: niet herstarten.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste kosten per inzending (€28,75) en beste sessie-naar-inzending ratio (3,5%). Aanbeveling: behouden, de dure click betaalt zich terug.
- **Wholesaler Campagne (LIT)**: frequency 3,97 (drempel 3,5). Creative fatigue was zichtbaar in de laatste campagneweek. Aanbeveling: bij herstart minimaal één nieuwe creative toevoegen.
- **Statisch 2 (LIT)**: goedkoopste clicks van het account (€0,20), maar 292 sessies leveren maar 2 inzendingen op (0,7%). Trekt clicks aan die niet converteren. Aanbeveling: budget verlagen of landingsboodschap aanscherpen.

Geen enkele ad zit onder 1% CTR. Statisch 1 (LIT) zit met 1,0% op de grens, maar converteert goed (3,0%), dus geen actie.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, daarna Video 1 (LIT) €29,38 en Statisch 2 (SWE) €32,03
- **Beste ROAS**: niet van toepassing (lead-campagnes)

### Restverkeer na de pauze (PostHog, 5 t/m 9 september)

| Datum | Sessies distributeurpagina | Waarvan met ad-UTM |
|---|---|---|
| 5 sep | 3 | 0 |
| 6 sep | 5 | 2 |
| 7 sep | 4 | 1 |
| 8 sep | 3 | 0 |
| 9 sep | 5 | 2 |

De 5 sessies met ad-UTM sinds de pauze passen bij opgeslagen of gedeelde ad-posts, niet bij levering: twee op 6 september via instagram.com op Video 1 (SWE), één direct op Statisch 2 (SWE) en op 9 september twee direct op Statisch 2 (LIT) binnen twee seconden na elkaar (0 en 6 seconden duur, dus één persoon of een link-preview). Meta bevestigt €0,00 spend. Laatste inzending: 4 september. Geen actie nodig.

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alle spend viel tussen 27 augustus en 4 september)
- **Beste performer**: Video 2 (LIT). Laagste kosten per inzending (€28,75) en hoogste sessie-naar-inzending ratio (3,5%), ondanks een CPC boven de drempel.
- **Slechtste performer**: Video 1 (SWE). Boven de drempel op CPC én CPM, €126,75 uitgegeven zonder één inzending.
- **Aanbeveling (70-20-10)**: bij herstart 70% van het budget naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequency van 3,97 te doorbreken. Beide SWE-video's niet herstarten. Budget van Statisch 2 (LIT) verlagen. De vijf herstart-voorstellen uit het auto-optimize rapport van 3 september wachten nog op goedkeuring; zolang er niets draait is er geen dagelijkse actie.

### Google Sheet

Overgeslagen op verzoek. Rapport uitsluitend lokaal opgeslagen in `Output/Reports/Daily/2026-09-10_ads_report.md`.

---

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs geactiveerd en eerste orders per inzending zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose (tabel, #1 bottleneck, 3 actiepunten, SYBB vergelijking).
