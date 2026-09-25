# Meta Ads Rapport, 25 september 2026

**Periode:** last 30d (26 augustus t/m 24 september 2026)
**Account:** Sempertex Ad Account (act_567892422940728). Het in het command genoemde act_607231713057715 bestaat niet in Pipeboard; het tweede account (act_1489853856181844, AmbitionAvenue) is leeg.
**Bronnen:** Pipeboard Meta Ads via directe JSON-RPC route (MCP meldde "requires authentication", 3 calls: campaign-level 30d, campagnelijst, ad-level 30d) en PostHog project STX EU 149694 via directe REST-route (8 sessions- en events-queries, alle onder 1 seconde). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

## Status

**Er draait niets.** Alle 7 campagnes staan op PAUSED. De twee Wholesaler Campagnes zijn sinds 4 september 11:50 gepauzeerd; dit is de 21e dag zonder levering. PostHog bevestigt dit live: nul sessies met utm_source facebook of meta sinds 11 september (de laatste twee nalopers waren op 9 september).

De 30d-cijfers zijn identiek aan die van 16, 21, 22 en 24 september, omdat het venster nog geen leverdag kwijt is. **Vanaf 27 september valt 27 augustus uit het venster** en gaan de LIT-cijfers dalen zonder dat de campagne iets deed. Lees dalende spend vanaf dat moment niet als verandering in performance.

| Campagne | Status | Laatste wijziging | Doel |
|---|---|---|---|
| Wholesaler Campagne (SWE) | Paused | 4 sep 2026 | Leads |
| Wholesaler Campagne (LIT) | Paused | 4 sep 2026 | Leads |
| 2026: SYBB - Kopie | Paused | 27 aug 2026 | Sales |
| 2026: SYBB | Paused | 19 apr 2026 | Sales |
| Last push Nozzle Up | Paused | 21 sep 2025 | Sales |
| Nozzle Up END OF AUGUST | Paused | 15 sep 2025 | Sales |
| Campagne Nozzle Up 2025 1 | Paused | 15 sep 2025 | Sales |

Alleen de twee Wholesaler Campagnes hebben spend in het venster. De SYBB-campagnes en Nozzle Up hebben 30 dagen lang nul spend, impressies en clicks.

## Overzicht per campagne (last 30d, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog sessies | PostHog inz. | € / inz. | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 815 | 16 | €35,13 | n.v.t. |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 597 | 7 | €72,46 | n.v.t. |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 1.412 | 23 (+9 organisch = 32) | €46,49 | |

ROAS is niet van toepassing: het zijn lead-campagnes (OUTCOME_LEADS) zonder aankoopwaarde. Meta pixel telt 19 leads, PostHog telt 23 betaalde inzendingen plus 9 organische. Het pixel-lead-event telt dus structureel te weinig (zie ook de aanbevelingen).

**Conversies (PostHog, echte bron):** 32 unieke sessies met een inzending op /become-a-distributor in 30 dagen (35 submit-events). Daarvan 16 via LIT, 7 via SWE, 9 zonder UTM (organisch of direct). De laatste inzendingen waren op 18 en 20 september, beide organisch. Sinds Malta (20 september) geen nieuwe inzending.

## Per ad (last 30d, gesorteerd op spend)

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PH sessies | Bounce | Gem. duur | Inz. | Conv. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 3 | 248 | 30,6% | 68s | 5 | 2,0% | €29,38 | OK |
| Statisch 1 (LIT) | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 3 | 134 | 29,1% | 102s | 4 | 3,0% | €36,06 | OK |
| Video 2 (LIT) | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 4 | 141 | 29,8% | 95s | 5 | 3,5% | €28,75 | CPC €0,58 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 5 | 256 | 22,3% | 114s | 3 | 1,2% | €42,71 | OK |
| Statisch 2 (LIT) | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 1 | 292 | 28,1% | 51s | 2 | 0,7% | €63,62 | OK |
| Video 2 (SWE) | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 1 | 97 | 23,7% | 73s | 2 | 2,1% | €63,50 | CPC €0,69, CPM €17,07 |
| Video 1 (SWE) | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 0 | 113 | 20,4% | 74s | 0 | 0,0% | geen | CPC €0,53, CPM €15,27 |
| Statisch 1 (SWE) | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 2 | 131 | 19,8% | 210s | 2 | 1,5% | €62,68 | OK |

PostHog-match via utm_campaign (wholesaler_lt / wholesaler_se) en utm_content (video_01, video_02, static_01, static_02) op de entry-UTM van de sessie. Conv. is inzendingen gedeeld door PostHog-sessies.

## Underperformers

Alle flags gelden voor een eventuele herstart in de huidige vorm; er loopt nu niets.

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Duurste clicks van de hele set en maar 2 inzendingen op 97 sessies. Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50) en CPM €15,27 (drempel €15,00). Nul inzendingen op 113 sessies, terwijl Meta ook nul leads telt. Aanbeveling: definitief uit.
- **Video 2 (LIT)**: CPC €0,58 (drempel €0,50). Maar wel de beste converteerder van LIT (3,5%, €28,75 per inzending). Aanbeveling: behouden, dure clicks worden goedgemaakt door de conversie.
- **Campagne LIT als geheel**: frequency 3,97 (drempel 3,5). Het Litouwse publiek is verzadigd; dezelfde persoon zag de ads bijna vier keer. Aanbeveling: verse creatives of ruimer publiek vóór herstart.
- **Statisch 1 (LIT)**: CTR 1,0%, precies op de drempel. Goedkoop bereik (CPM €5,07) maar zwakke hook. Conversie is wel goed (3,0%). Aanbeveling: hook testen, visual behouden.
- **Statisch 2 (LIT)**: geen flag op link-metrics (CPC €0,20, CTR 2,4%), maar de slechtste conversie: 2 inzendingen op 292 sessies (0,7%), de kortste sessieduur van de set (51s) en een bounce van 28,1%. De goedkope clicks landen niet bij de juiste mensen. Aanbeveling: nieuwe hook, of budget verschuiven naar de video's.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Laagste CPM**: Statisch 2 (LIT), €4,87
- **Beste ROAS**: n.v.t. (lead-campagnes)
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06
- **Beste conversie op sessies**: Video 2 (LIT) 3,5%, dan Statisch 1 (LIT) 3,0%, dan Video 1 (LIT) 2,0%
- **Langste sessieduur**: Statisch 1 (SWE), 210s gemiddeld (maar slechts 2 inzendingen)

## Funnel /become-a-distributor (30d, live uit PostHog)

| Stap | Aantal | Sessies |
|---|---|---|
| wholesaler_page_view | 1.713 | 1.442 |
| wholesaler_form_start | 141 | 134 |
| wholesaler_form_error | 22 | 12 |
| wholesaler_form_submit | 35 | 32 |

Formulierstart naar inzending: 23,9% (32 inzendingssessies op 134 startsessies). Foutpercentage op starts: 15,6%. Organisch lopen er 2 tot 6 sessies per dag over de pagina (18 t/m 24 september: 4, 2, 4, 4, 6, 3, 4). Onveranderd ten opzichte van gisteren.

Noot: 12 sessies kregen een formulierfout; 22 foutmeldingen in totaal, dus meerdere pogingen per sessie. Dat lek staat nog open.

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, 26 aug t/m 24 sep). Nul spend sinds 4 september.
- **Beste performer**: Video 2 (LIT). Beste conversie (3,5%) en laagste kosten per inzending (€28,75), ondanks een CPC boven de drempel. Conversie weegt zwaarder dan clickprijs.
- **Slechtste performer**: Video 1 (SWE). Nul inzendingen op €126,75 en 113 sessies, met CPC en CPM boven de drempel.
- **Aanbeveling (70-20-10)** bij herstart:
  - 70% naar de bewezen set: Video 1 (LIT), Video 2 (LIT), Statisch 1 (LIT), Statisch 2 (SWE). Wel met verse creatives, want LIT zit op frequency 3,97.
  - 20% naar een Zweedse variant van Video 2 (LIT), de beste converteerder, voor het SWE-publiek.
  - 10% naar een nieuwe hook voor Statisch 2 (LIT), dat wel clicks maar geen inzendingen oplevert.
  - Beide SWE-video's niet meenemen.
  - Vóór herstart: formulierfout (15,6%) dichten en het pixel-lead-event repareren, zodat Meta op echte inzendingen kan optimaliseren in plaats van op 19 van de 32.
  - De zes voorstellen van 3 en 16 september wachten nog op goedkeuring.

## Google Sheet

Overgeslagen op verzoek. Niets geschreven naar de Meta Ads Tracker.

## Databronnen en verbruik

- Pipeboard: 3 calls deze run (campaign-level 30d, get_campaigns, ad-level 30d). Geen limietmelding.
- PostHog: 8 queries (sessions: betaald per dag, distributor-pagina per dag, per-ad sessies; events: funnelstappen, inzendingen per dag, inzendingen per ad via join). Events-tabel antwoordde normaal.
- Meta 30d-cijfers zijn nog altijd het extract van de leverperiode 27 aug t/m 4 sep; het venster verschuift, de data niet.
