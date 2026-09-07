# Meta Ads Rapport, 7 september 2026

**Periode:** last_30d (8 augustus t/m 6 september 2026)
**Account:** Sempertex Ad Account (act_567892422940728)
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, weeklimiet gereset), PostHog project STX EU via REST API (MCP verbrak de verbinding)
**Google Sheet:** overgeslagen op verzoek, niets geschreven

## Status

**Geen actieve campagnes.** Beide Wholesaler campagnes staan sinds 4 september 11:50 op PAUSED. Meta registreert 0 spend en 0 impressies van 5 t/m 7 september, dus de pauze is volledig doorgevoerd. Het account `act_607231713057715` uit het command bestaat niet, alleen AmbitionAvenue (leeg) en het Sempertex account zijn beschikbaar.

De twee betaalde sessies van 6 september (Video 1 SWE, utm_content=video_01) uit het rapport van gisteren zijn dus geen ad-levering. Meta heeft die dag niets uitgeleverd. Het past bij een gedeelde of opgeslagen ad-post. Geen actie nodig.

## Overzicht per campagne (alle gepauzeerd)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 0 | n.v.t. | n.v.t. |

CTR en CPC zijn op alle clicks. Link-metrics staan in de ad-tabel. ROAS is niet van toepassing: beide campagnes zijn lead-campagnes zonder aankoopwaarde. PostHog inzendingen zijn `wholesaler_form_submit` sessies gekoppeld op entry UTM. 7 van de 30 inzendingen hadden geen UTM en zijn niet aan een campagne toe te wijzen; het totaal aantal form submit events is 33.

## Overzicht per ad

| Ad | Spend | Impr. | Freq. | CTR (all) | CPC (all) | CPM | Link clicks | Link CTR | Link CPC | LPV (Meta) | Sessies (PostHog) | Inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 1,90 | 2,4% | €0,32 | €7,72 | 242 | 1,3% | €0,61 | 28 | 248 | 5 | €29,38 |
| Statisch 1 (LIT) | €144,24 | 28.434 | 2,91 | 1,0% | €0,49 | €5,07 | 163 | 0,6% | €0,88 | 27 | 134 | 4 | €36,06 |
| Video 2 (LIT) | €143,74 | 17.267 | 2,52 | 1,4% | €0,58 | €8,32 | 179 | 1,0% | €0,80 | 21 | 141 | 5 | €28,75 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 1,97 | 4,0% | €0,24 | €9,66 | 286 | 2,2% | €0,45 | 62 | 255 | 3 | €42,71 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 2,37 | 2,4% | €0,20 | €4,87 | 297 | 1,1% | €0,43 | 45 | 290 | 2 | €63,63 |
| Video 2 (SWE) | €127,00 | 7.441 | 2,02 | 2,5% | €0,69 | €17,07 | 114 | 1,5% | €1,11 | 19 | 97 | 2 | €63,50 |
| Video 1 (SWE) | €126,75 | 8.299 | 2,05 | 2,9% | €0,53 | €15,27 | 139 | 1,7% | €0,91 | 31 | 113 | 0 | geen |
| Statisch 1 (SWE) | €125,36 | 10.262 | 2,15 | 2,7% | €0,45 | €12,22 | 157 | 1,5% | €0,80 | 44 | 131 | 2 | €62,68 |

Meta LPV telt structureel te laag: 277 landing page views tegenover 1.409 PostHog sessies. Baseer funnel-conclusies op PostHog.

## Underperformers (drempels uit het command)

- **Video 2 (SWE)** — CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15) → Niet herstarten in huidige vorm. Duurste reach en duurste clicks van de set.
- **Video 1 (SWE)** — CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15), 0 inzendingen op 113 sessies → Definitief uit. Terecht gepauzeerd op 4 september.
- **Video 2 (LIT)** — CPC €0,58 (drempel €0,50) → Ondanks dure clicks de laagste kosten per inzending (€28,75). Houden bij herstart, maar met de LIT-campagne als geheel de frequentie in de gaten houden.
- **Wholesaler Campagne (LIT)** — Frequency 3,97 (drempel 3,5) → Creative fatigue op campagneniveau. Bij herstart audience verbreden of creatives roteren; niet dezelfde 4 ads op dezelfde doelgroep zetten.
- **Statisch 1 (LIT)** — Link CTR 0,6% (all-clicks CTR net 1,0%) → Zwakke hook, maar €36,06 per inzending is de op twee na beste. Lage CTR is hier geen reden om te killen.

## Top performers

- **Beste CTR:** Statisch 2 (SWE) — 4,0% (link CTR 2,2%)
- **Laagste CPC:** Statisch 2 (LIT) — €0,20 (link CPC €0,43)
- **Beste ROAS:** n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) — €28,75, direct gevolgd door Video 1 (LIT) — €29,38
- **Laagste CPM:** Statisch 2 (LIT) — €4,87

## Samenvatting

- **Totaal spend:** €1.069,38 (periode: last 30 days, alle spend viel tussen 27 augustus en 4 september)
- **Totaal PostHog:** 1.409 betaalde sessies, 33 form submits, gemiddeld €32,41 per inzending over beide campagnes
- **Beste performer:** Wholesaler Campagne (LIT) — €35,13 per inzending tegenover €72,46 voor SWE. Binnen LIT winnen de twee video's op conversie (5 inzendingen elk), Statisch 2 wint op clicks maar converteert het slechtst.
- **Slechtste performer:** Video 1 (SWE) — hoogste CPM, 0 inzendingen, verkeer zonder resultaat.
- **Aanbeveling (70-20-10):** bij een herstart gaat 70% van het budget naar de bewezen LIT-set (Video 1, Video 2, Statisch 1). 20% naar Statisch 2 (SWE), de enige SWE-ad met acceptabele kosten per inzending en de hoogste CTR. 10% naar één nieuwe creative-variant per markt om de frequentie van 3,97 op LIT te doorbreken. Video 1 (SWE) en Video 2 (SWE) niet herstarten.

## Dagelijks verloop (PostHog, betaalde sessies en inzendingen)

| Dag | Sessies | Form starts | Inzendingen |
|---|---|---|---|
| 27 aug | 21 | 27 | 6 |
| 28 aug | 254 | 46 | 6 |
| 29 aug | 216 | 12 | 4 |
| 30 aug | 126 | 10 | 6 |
| 31 aug | 161 | 10 | 5 |
| 1 sep | 205 | 13 | 1 |
| 2 sep | 156 | 5 | 3 |
| 3 sep | 210 | 5 | 1 |
| 4 sep | 58 | 4 | 1 |
| 5 sep | 0 | 0 | 0 |
| 6 sep | 2 | 0 | 0 |

Conversie zakte vanaf 1 september duidelijk in (16 inzendingen op 26 t/m 31 augustus, 6 op 1 t/m 4 september bij vergelijkbaar verkeer). Dat is consistent met de frequency van bijna 4 op LIT: dezelfde mensen zagen de ads te vaak.

## Google Sheet

Overgeslagen op verzoek. Niets geschreven naar "Meta Ads Tracker".

## Openstaand

De vijf herstart-voorstellen uit het auto-optimize rapport van 3 september wachten nog op goedkeuring. Dit rapport verandert niets aan die voorstellen; het bevestigt ze met 30-daagse data.
