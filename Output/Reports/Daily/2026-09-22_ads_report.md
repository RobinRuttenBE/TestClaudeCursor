# Meta Ads Rapport, 22 september 2026

**Bronnen:** Pipeboard Meta Ads (directe JSON-RPC route, 3 calls: campaign-level 30d, ad-level 30d, campagnelijst) en PostHog (directe REST-route, 2 sessions-queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

**Meta was live bereikbaar.** Weekverbruik Pipeboard na deze run: 11 van 30 calls (8 gisteren, 3 vandaag). Eerste campaign-level call hing 2 minuten zonder antwoord; de retry met `curl -m 45` kwam in 18 seconden terug. Ad-level: eerste poging http 000, retry direct geslaagd.

**PostHog:** alle `events`-queries (wholesaler-funnel per dag en 30d-totalen) hingen vandaag op beide routes (REST met `curl -m 35` liep 5 minuten door, connector `execute-sql` brak na 707s af). Alleen `sessions`-queries kwamen terug (onder 5 seconden). De funnelcijfers hieronder komen daarom uit het rapport van 21 september; sessies en betaald verkeer zijn live.

---

## Status

**Er draait nog steeds niets.** Alle 7 campagnes op account `act_567892422940728` staan op PAUSED. De twee Wholesaler Campagnes sinds 4 september 11:50. Negentiende dag zonder levering. Het account `act_607231713057715` uit de command bestaat niet (bekend sinds september).

PostHog bevestigt: nul betaalde sessies (`$entry_utm_source = 'facebook'`) sinds 10 september. Laatste nalopers: 2 sessies op 9 september.

| Campagne | Status | Doel | Laatst gewijzigd |
|---|---|---|---|
| Wholesaler Campagne (SWE) | Paused | Leads | 4 sep 2026 11:50 |
| Wholesaler Campagne (LIT) | Paused | Leads | 4 sep 2026 11:50 |
| 2026: SYBB - Kopie | Paused | Sales | 27 aug 2026 |
| 2026: SYBB | Paused | Sales | 19 apr 2026 |
| Last push Nozzle Up | Paused | Sales | 21 sep 2025 |
| Nozzle Up END OF AUGUST | Paused | Sales | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | Paused | Sales | 15 sep 2025 |

---

## Overzicht per campagne (last 30d, 23 aug t/m 21 sep)

Het venster schoof één dag op ten opzichte van gisteren (22 aug viel eruit, 21 sep kwam erbij). Beide dagen hadden geen levering, dus alle Meta-cijfers zijn identiek aan 21 september en 16 september.

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Reach | Link clicks | Meta LPV | Meta leads | PostHog inz. via ad | € / inz. (PostHog) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 22.909 | 881 | 121 | 11 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 11.919 | 696 | 156 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 34.828 | 1.577 | 277 | 19 | 23 | €46,49 via ad, €30,55 all-in (35 inz.) |

ROAS niet van toepassing: beide zijn lead-campagnes zonder aankoopwaarde. Meta telt 19 leads, PostHog 35 inzendingen in 30 dagen (23 via ad-UTM, de rest organisch of zonder UTM). Meta's pixel meet op deze pagina structureel te weinig (277 LPV tegenover 1.577 link clicks), dus kosten per inzending zijn op PostHog gebaseerd.

De PostHog-kolommen "inz. via ad" komen uit de sessie-join van 21 september; de events-queries kwamen vandaag niet terug. Zonder levering veranderen ze niet.

---

## Per ad (last 30d, live uit Meta, PostHog uit 21 september)

| Ad | Campagne | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Link clicks | Meta LPV | Meta leads | PostHog sessies | PostHog inz. | Conv. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | LIT | €146,91 | 19.041 | 453 | 2,4% | €0,32 | €7,72 | 1,90 | 242 | 28 | 3 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | LIT | €143,74 | 17.267 | 247 | 1,4% | €0,58 | €8,32 | 2,52 | 179 | 21 | 4 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | LIT | €144,24 | 28.434 | 294 | 1,0% | €0,49 | €5,07 | 2,91 | 163 | 27 | 3 | 134 | 4 | 3,0% | €36,06 | |
| Statisch 2 (LIT) | LIT | €127,25 | 26.146 | 623 | 2,4% | €0,20 | €4,87 | 2,37 | 297 | 45 | 1 | 292 | 2 | 0,7% | €63,63 | |
| Video 1 (SWE) | SWE | €126,75 | 8.299 | 238 | 2,9% | €0,53 | €15,27 | 2,05 | 139 | 31 | 0 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM |
| Video 2 (SWE) | SWE | €127,00 | 7.441 | 185 | 2,5% | €0,69 | €17,07 | 2,02 | 114 | 19 | 1 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | SWE | €125,36 | 10.262 | 281 | 2,7% | €0,45 | €12,22 | 2,15 | 157 | 44 | 2 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | SWE | €128,13 | 13.265 | 533 | 4,0% | €0,24 | €9,66 | 1,97 | 286 | 62 | 5 | 256 | 3 | 1,2% | €42,71 | |

Statisch 1 (LIT) zit met CTR 1,0% precies op de drempel (1,03%), niet eronder. Conv. = PostHog inzendingen gedeeld door PostHog sessies.

---

## Underperformers (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Aanbeveling: niet herstarten in deze vorm, hoogstens als Zweedse variant van de LIT-hook.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27 boven drempel, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Campagne LIT**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives voor herstart, anders stijgt CPC verder.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%, €28,75 per inzending). Aanbeveling: behouden, niet mechanisch pauzeren op CPC.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie. Aanbeveling: nieuwe hook testen die op kwaliteit selecteert, niet op clicks.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06.

---

## Funnel /become-a-distributor

**30d (cijfers 21 september, events-queries vandaag niet bereikbaar):** 1.699 pageviews, 141 formulierstarts, 22 fouten, 35 inzendingen. Van start naar inzending 24,8%.

**Live (sessions, sinds 15 september):** sessies met de distributor-pagina per dag, allemaal zonder betaald verkeer.

| Dag | Sessies op distributor-pagina | Betaald |
|---|---|---|
| 15 sep | 2 | 0 |
| 16 sep | 8 | 0 |
| 17 sep | 1 | 0 |
| 18 sep | 4 | 0 |
| 19 sep | 2 | 0 |
| 20 sep | 4 | 0 |
| 21 sep | 4 | 0 |
| 22 sep (tot 09:50) | 0 | 0 |

Organisch loopt er 1 tot 8 sessies per dag over de pagina. Of daar op 21 september een nieuwe inzending bij zat (na Letland 18 sep en Malta 20 sep) kon vandaag niet worden bevestigd; de events-tabel gaf geen antwoord.

---

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, 23 aug t/m 21 sep). Nul spend sinds 4 september.
- **Beste performer**: Video 2 (LIT). Laagste kosten per inzending (€28,75) en hoogste conversie (3,5%), ondanks CPC boven drempel.
- **Slechtste performer**: Video 1 (SWE). €126,75 uitgegeven, nul inzendingen, CPC en CPM beide boven drempel.
- **Aanbeveling (70-20-10)** bij herstart: 70% budget naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de frequency van 3,97. 20% naar een Zweedse variant van Video 2 (LIT). 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten (22 fouten op 141 starts in 30d) vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op goedkeuring.

## Google Sheet

Overgeslagen op verzoek. Rapport alleen lokaal opgeslagen.

## Technische notities voor volgende runs

- Pipeboard directe route: eerste call kan minutenlang hangen; `curl -m 45 --connect-timeout 10` en één retry is genoeg.
- PostHog `events`-queries hingen vandaag op beide routes (REST en connector). `sessions`-queries werkten direct. Bij herhaling: funnelcijfers uit het laatste rapport overnemen en alleen sessions live checken.
