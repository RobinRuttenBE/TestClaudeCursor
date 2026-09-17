## Meta Ads Rapport, 17 september 2026

**Databronnen.** De Pipeboard MCP (`claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads`) vroeg om autorisatie, niet mogelijk in deze non-interactieve sessie. De directe JSON-RPC route kreeg op de eerste call `weekly_limit_exceeded` (30 van 30 wekelijkse executies, plan free, reset_date 21 september 2026 00:00 UTC). Meta is vandaag dus niet live bereikbaar. De PostHog MCP gaf HTTP 405, de directe REST-route op eu.posthog.com (project STX EU, 149694) werkte in 5 queries.

De Meta-cijfers hieronder komen uit het rapport van 16 september (live opgehaald om 09:03, venster 17 augustus t/m 15 september). Het venster van vandaag (18 augustus t/m 16 september) bevat dezelfde levering: PostHog toont nul betaalde sessies tussen 14 en 20 augustus en nul betaalde sessies sinds 10 september, dus er valt aan geen van beide kanten iets buiten het venster. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50 (status uit het live extract van 16 september). PostHog bevestigt dat live: nul sessies met een Meta-UTM sinds 10 september, nul formulierstarts, nul inzendingen sinds 4 september. Dat is de veertiende dag zonder levering. Meta-account act_607231713057715 uit het command bestaat niet; het tweede account (act_1489853856181844, AmbitionAvenue) is leeg.

### Overzicht per campagne (last 30d, 18 aug t/m 16 sep)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Conv. (Meta) | Conv. (PostHog) | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | ca. 1.606 | 1,8% | €0,35 | €6,18 | 3,97 | 11 leads | 16 inzendingen | n.v.t. |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | ca. 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 leads | 8 inzendingen | n.v.t. |
| 2026: SYBB | Paused (sinds 19 apr) | €0,00 | 0 | 0 | 0,0% | n.v.t. | n.v.t. | n.v.t. | 0 | 0 | n.v.t. |
| Overige 4 campagnes | Paused | €0,00 | 0 | 0 | 0,0% | n.v.t. | n.v.t. | n.v.t. | 0 | 0 | n.v.t. |
| **Totaal** | | **€1.069,38** | 130.155 | ca. 2.843 | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM = 35) | n.v.t. |

Clicks zijn afgeleid uit spend gedeeld door CPC (Meta gaf gisteren geen aparte clickkolom in het rapport). ROAS is niet van toepassing, het zijn lead-campagnes. Kosten per inzending op basis van PostHog: LIT €35,13, SWE €63,41, all-in €30,55. De Meta pixel telt structureel te weinig (19 leads tegenover 35 inzendingen).

### Underperformers (cijfers 16 september, ad-niveau)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Wholesaler (LIT)**: frequency 3,97 (drempel 3,5), inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer. Aanbeveling: verse creatives vóór herstart.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste kosten per inzending (€28,75). Aanbeveling: behouden.
- **Statisch 1 (LIT)**: link CTR 0,6% (drempel 1%), maar €36,06 per inzending en 3,0% conversie. Aanbeveling: behouden, geen kill op CTR.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies (52s), 0,7% conversie, €63,63 per inzending. Aanbeveling: nieuwe hook testen.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

### PostHog live bevestiging (17 september, 08:55)

| Meting | Waarde |
|---|---|
| Betaalde sessies (utm_source=facebook) 8 t/m 16 sep | 2 (beide 9 september, nalopers) |
| Betaalde sessies 10 t/m 16 sep | 0 |
| Wholesaler pageviews 16 sep | 9, allemaal organisch (direct, eigen site, Bing) |
| Formulierstarts sinds 10 sep | 0 |
| Inzendingen sinds 5 sep | 0 |
| SYBB sessies met utm_source=meta (30d) | 3, allemaal oude link h11_b3_cta5 op 23 en 28 augustus, geen levering |

**Funnel /become-a-distributor (30d, 18 aug t/m 16 sep):** 1.751 pageviews, 134 formulierstarts, 21 formulierfouten, 33 inzendingen. Van start naar inzending komt 24,6% door. De totalen dalen licht omdat 17 augustus uit het venster viel en er geen nieuwe inzendingen bijkomen.

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, ongewijzigd sinds 4 september)
- **Beste performer**: Video 2 (LIT), €28,75 per inzending en 3,5% sessie-conversie, ondanks CPC boven drempel
- **Slechtste performer**: Video 1 (SWE), €0,53 CPC, €15,27 CPM en nul inzendingen op 113 sessies
- **Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Fix eerst het formulierlek (75% van de starters haakt af) en de pixel-attributie vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten op goedkeuring.
- **Wijzigingen t.o.v. gisteren**: geen in Meta. PostHog: 9 organische pageviews op de distributeurspagina, geen starts, geen inzendingen.

### Operationeel

- Pipeboard-limiet is deze week vol (reset 21 september). Tot maandag draaien alle Meta-rapporten op het extract van 16 september. Op maandag eerst de directe call testen; de resetdatum in het antwoord bleek op 14 september niet betrouwbaar.
- Voorstel 6 (één gedeeld Meta-extract per dag cachen voor ads-report, SYBB en auto-optimize) blijft open. Zonder cache valt de route elke week vanaf woensdag dicht.

### Google Sheet
Niet geschreven, stap 6 overgeslagen op verzoek. Rapport uitsluitend lokaal opgeslagen.
