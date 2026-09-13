## Meta Ads Rapport, 13 september 2026

**Er draait niets.** Alle 7 campagnes in het Sempertex Ad Account (act_567892422940728) staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt dat live: 48 betaalde sessies op 4 september, daarna in totaal 3 nalopers (1 op 6 september, 2 op 9 september) en nul op 10, 11 en 12 september. Elfde dag zonder levering.

**Bronnen en beperking**
- Pipeboard Meta Ads: MCP vroeg om authenticatie, de directe JSON-RPC route kreeg op de eerste call `weekly_limit_exceeded` (100 van 30 calls gebruikt, Free plan). Reset staat nu op **21 september 2026 00:00 UTC**, niet meer op 14 september. Geen live Meta-cijfers in deze run.
- Meta campagnestatus en spend komen uit het rapport van 12 september (live status) en het rapport van 7 september (laatste run met volledige 30d insights). Omdat er sinds 4 september geen levering is, zijn de 30d Meta-cijfers (14 aug t/m 12 sep) ongewijzigd.
- PostHog project STX EU (149694) via de directe REST-route, live vandaag. PostHog MCP gaf HTTP 405.
- Geen Google MCPs aangeroepen. Geen Google Sheet geschreven. Alleen dit lokale bestand.

### Overzicht per campagne (last 30d, 14 aug t/m 12 sep)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 1.606 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | n.v.t. |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | 0 | 0 | | | | | 0 | 0 | n.v.t. |
| 4 overige campagnes | Paused | €0,00 | 0 | 0 | | | | | 0 | 0 | n.v.t. |
| **Totaal** | | **€1.069,38** | 130.155 | 2.843 | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM) | n.v.t. |

ROAS is niet van toepassing, het zijn lead-campagnes zonder aankoopwaarde. Meta telt 19 leads, PostHog 35 inzendingen op de distributeurspagina in dezelfde periode (24 met ad-UTM, 11 zonder). Kosten per inzending zijn daarom op PostHog gebaseerd: **€35,13 (LIT)** en **€63,41 (SWE)**, all-in €30,55 per inzending over alle 35.

### Ad-level (PostHog live, 30d)

Meta ad-level insights waren vandaag niet bereikbaar. CPC en CPM per ad hieronder komen uit het rapport van 7 september en zijn ongewijzigd.

| Ad | Sessies | Gem. duur | Bounce | Inzendingen | Sessie naar inzending | € / inzending |
|---|---|---|---|---|---|---|
| Statisch 2 (LIT) | 250 | 56s | 32,8% | 2 | 0,8% | €63,63 (afgeleid) |
| Statisch 2 (SWE) | 230 | 123s | 24,8% | 4 | 1,7% | |
| Video 1 (LIT) | 216 | 75s | 35,2% | 5 | 2,3% | €29,38 |
| Video 2 (LIT) | 123 | 108s | 34,1% | 5 | 4,1% | €28,75 |
| Statisch 1 (SWE) | 116 | 235s | 22,4% | 2 | 1,7% | |
| Statisch 1 (LIT) | 106 | 111s | 36,8% | 4 | 3,8% | €36,06 |
| Video 1 (SWE) | 97 | 69s | 23,7% | 0 | 0,0% | geen inzending |
| Video 2 (SWE) | 84 | 83s | 27,4% | 2 | 2,4% | |

SWE per ad is alleen op campagneniveau te berekenen (€507,24 op 8 inzendingen). Totaal 1.222 betaalde sessies met minimaal 1 pageview. Verschil met de 1.412 van eerdere rapporten komt door het filter op sessies zonder pageview (tab-sluitingen en link-preview bots).

### Underperformers

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Duurste ad van het account, 2 inzendingen. Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15,00), 0 inzendingen op 97 sessies. Aanbeveling: definitief uit.
- **Wholesaler Campagne (LIT)**: frequency 3,97 (drempel 3,5). Publiek verzadigd voor de pauze. Aanbeveling: bij herstart minimaal één verse creative per ad set.
- **Statisch 2 (LIT)**: meeste sessies (250), kortste sessieduur (56s), 0,8% conversie, circa €63,63 per inzending. Aanbeveling: nieuwe hook testen, huidige versie is een klikmagneet zonder intentie.
- **Statisch 1 (LIT)**: link CTR 0,6% (drempel 1%), maar 3,8% conversie en €36,06 per inzending. Aanbeveling: behouden, lage CTR is hier geen kill-reden.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, daarna Video 1 (LIT) €29,38
- **Beste sessie naar inzending**: Video 2 (LIT) 4,1%, daarna Statisch 1 (LIT) 3,8%
- **Beste ROAS**: n.v.t. (lead-campagnes)

### Funnel /become-a-distributor (PostHog, 30d)

| Stap | Aantal | Ratio |
|---|---|---|
| Pageviews | 1.743 | |
| Formulier gestart | 137 | 7,9% van pageviews |
| Ingezonden | 35 | 25,5% van starts, 2,0% van pageviews |

Sinds de pauze: 1 tot 8 sessies per dag op de distributeurspagina, vrijwel allemaal organisch. Laatste formulierstart 9 september (2 starts, 0 inzendingen), laatste inzending 4 september. De 2 betaalde nalopers op 9 september kwamen via een oude ad-link en converteerden niet.

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alles uitgegeven tussen 27 aug en 4 sep)
- **Beste performer**: Video 2 (LIT), €28,75 per inzending, 4,1% sessie naar inzending, langste sessies van de LIT-set
- **Slechtste performer**: Video 1 (SWE), CPC en CPM boven drempel en nul inzendingen op 97 sessies
- **Aanbeveling (70-20-10)**: bij herstart 70% budget naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de frequency, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). De herstart-voorstellen van 3 september wachten nog op goedkeuring.
- **Operationeel**: Pipeboard blijft tot 21 september dicht. Tot die tijd draaien alle Meta-rapporten op de stand van 7 september. Voorstel 6 uit het auto-optimize rapport (één gedeelde Meta-call per dag cachen voor de drie rapporten) wordt hiermee urgent, anders valt de route na de reset binnen 2 dagen opnieuw dicht.

### Google Sheet
Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker". Rapport alleen lokaal opgeslagen in `Output/Reports/Daily/2026-09-13_ads_report.md`.
