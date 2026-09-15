## Meta Ads Rapport, 15 september 2026

**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, 4 calls) en PostHog project STX EU (directe REST route, 6 queries). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.
**Periode:** last 30d = 16 augustus t/m 14 september 2026. Meta-cijfers vers opgehaald op 15 september.

### Status account

**Er draait niets.** Alle 7 campagnes in het Sempertex Ad Account (act_567892422940728) staan op PAUSED. De twee Wholesaler Campagnes zijn gepauzeerd op 4 september om 11:50. Meta geeft voor de laatste 7 dagen (8 t/m 14 september) nul rijen.

PostHog bevestigt dit live:
- Betaald verkeer (utm_source facebook/meta) na 4 september: 2 sessies op 6 september, 1 op 7 september, 2 op 9 september. Daarna nul, ook op 10 t/m 14 september.
- Laatste wholesaler-inzending: 4 september. Nul inzendingen op 5 t/m 14 september.

Het tweede account uit het command (act_607231713057715) bestaat niet in Pipeboard. AmbitionAvenue (act_1489853856181844) is leeg.

| Campagne | Status | Laatst gewijzigd | Objective |
|---|---|---|---|
| Wholesaler Campagne (SWE) | Paused | 4 sep 2026 11:50 | Leads |
| Wholesaler Campagne (LIT) | Paused | 4 sep 2026 11:50 | Leads |
| 2026: SYBB - Kopie | Paused | 27 aug 2026 | Sales |
| 2026: SYBB | Paused | 19 apr 2026 | Sales |
| Last push Nozzle Up | Paused | 21 sep 2025 | Sales |
| Nozzle Up END OF AUGUST | Paused | 15 sep 2025 | Sales |
| Campagne Nozzle Up 2025 1 | Paused | 15 sep 2025 | Sales |

### Overzicht per campagne (last 30d)

Alleen de twee Wholesaler Campagnes hadden levering in de periode. Gesorteerd op spend.

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 | n.v.t. |
| **Totaal** | | **€1.069,38** | **130.155** | **2.854** | **2,2%** | **€0,37** | **€8,22** | | **19** | **24 (+11 zonder UTM)** | **€44,56** | |

- ROAS is niet van toepassing: beide campagnes zijn lead-campagnes zonder aankoopwaarde.
- Meta telt 19 leads, PostHog telt 35 inzendingen van het wholesaler-formulier in dezelfde periode (24 met UTM-match op een ad, 11 zonder UTM). Kosten per inzending zijn op PostHog gebaseerd. All-in over alle 35 inzendingen: €30,55 per inzending.
- Meta rapporteert 277 landing page views, PostHog telt 1.412 sessies vanuit de ads. De Meta pixel telt structureel te weinig, PostHog is de conversiebron.

### Overzicht per ad (last 30d)

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | PostHog sessies | Bounce | Gem. duur | Inzendingen | Conv. | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 248 | 30,6% | 69s | 5 | 2,0% | €29,38 |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 134 | 29,1% | 103s | 4 | 3,0% | €36,06 |
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 141 | 29,8% | 96s | 5 | 3,5% | €28,75 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 256 | 22,3% | 114s | 4 | 1,6% | €32,03 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 292 | 28,1% | 52s | 2 | 0,7% | €63,63 |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 97 | 23,7% | 74s | 2 | 2,1% | €63,50 |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 113 | 20,4% | 75s | 0 | 0,0% | geen |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 131 | 19,8% | 210s | 2 | 1,5% | €62,68 |

Conv. = inzendingen gedeeld door PostHog sessies met die utm_content.

### Underperformers

Drempels: CPC boven €0,50, CTR onder 1%, frequency boven 3,5, CPM boven €15.

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Twee vlaggen, €63,50 per inzending. Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50) en CPM €15,27 (drempel €15). Nul inzendingen op 113 sessies. Aanbeveling: definitief uitzetten.
- **Wholesaler Campagne (LIT)**: frequency 3,97 (drempel 3,5). Publiek is verzadigd. Aanbeveling: bij herstart verse creatives of een nieuw publiek, anders loopt de CPC direct op.
- **Video 2 (LIT)**: CPC €0,58 (drempel €0,50). Maar wel de beste kosten per inzending van alle ads (€28,75) en de hoogste conversie (3,5%). Aanbeveling: behouden, de dure click betaalt zich terug in het formulier.
- **Statisch 1 (LIT)**: CTR 1,0%, precies op de drempel. Conversie 3,0% en €36,06 per inzending zijn goed. Aanbeveling: behouden, hook aanscherpen voor meer clicks.
- **Statisch 2 (LIT)**: geen Meta-vlag (CPC €0,20 is de laagste), maar kortste sessies (52s), laagste conversie (0,7%) en €63,63 per inzending. De goedkope clicks zijn van lage kwaliteit. Aanbeveling: nieuwe hook of andere landingsbelofte testen.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03
- **Beste conversie**: Video 2 (LIT), 3,5% van de sessies vult het formulier in
- **Langste sessies**: Statisch 1 (SWE), gemiddeld 210 seconden

### Funnel /become-a-distributor (30d, PostHog)

| Stap | Aantal | Doorstroom |
|---|---|---|
| Pageviews wholesaler-pagina | 1.744 | |
| FAQ geopend | 178 | 10,2% van pageviews |
| Formulier gestart | 137 | 7,9% van pageviews |
| Formulier-fout | 21 | 15,3% van starts |
| Formulier ingezonden | 35 | 25,5% van starts, 2,0% van pageviews |
| Booking-pagina bekeken | 35 | 100% van inzendingen |

Belangrijkste lek: 102 van 137 starters maken het formulier niet af, en 21 daarvan zien een foutmelding. Dat is het eerste punt om aan te pakken vóór er weer budget op gaat.

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alles vóór 4 september)
- **Beste performer**: Wholesaler Campagne (LIT). Goedkoopste reach (CPM €6,18), laagste CPC (€0,35) en twee keer zoveel inzendingen als SWE voor 11% meer budget. €35,13 per inzending.
- **Slechtste performer**: Wholesaler Campagne (SWE). CPM twee keer zo hoog als LIT (€12,92), €63,41 per inzending, en beide video's leveren samen 2 inzendingen op €253,75.
- **Aanbeveling (70-20-10)** bij herstart: 70% van het budget naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de LIT-frequency, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Fix eerst de 21 formulier-fouten op /become-a-distributor. De herstart-voorstellen van 3 september wachten nog op goedkeuring.

### Wijzigingen t.o.v. 14 september

- Geen. Zelfde campagnestatus, zelfde 30d-cijfers (het venster schoof één dag op zonder levering aan beide kanten).
- SWE telt vandaag 8 inzendingen met UTM-match (gisteren 7); dat is een verschil in de UTM-koppeling per sessie, niet in het totaal van 35.

### Google Sheet

Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker". Rapport alleen lokaal opgeslagen.

### Operationeel

- Pipeboard werkte direct, geen weeklimiet-melding. Vier calls gebruikt (campagne 30d, ad 30d, campagne 7d, campagne-lijst zonder status_filter).
- De wholesaler-ads taggen met `utm_source=facebook`, niet `meta`. Een PostHog-filter op alleen `meta` vindt slechts 3 oude SYBB-sessies.
- Nog 3 sessies met `utm_campaign=sybb` (h11_b3_cta5) via utm_source=meta, ondanks dat de SYBB campagne sinds april gepauzeerd is: waarschijnlijk oude gedeelde links.
