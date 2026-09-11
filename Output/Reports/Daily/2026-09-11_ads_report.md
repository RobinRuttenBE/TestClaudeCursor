## Meta Ads Rapport, 11 september 2026

**Periode:** last 30 days (12 augustus t/m 10 september 2026)
**Account:** Sempertex Ad Account (act_567892422940728)
**Databronnen:** Meta Ads (Pipeboard, directe JSON-RPC) en PostHog (project STX EU, directe REST). Geen Google-bronnen gebruikt, geen Google Sheet geschreven.

### Status: geen actieve campagnes

Er draait op dit moment **niets**. Alle 7 campagnes in het account staan op PAUSED. De twee Wholesaler Campagnes (SWE en LIT) zijn op 4 september gepauzeerd; PostHog bevestigt dat betaald verkeer daarna is stilgevallen (58 sessies op 4 september, daarna 0 tot 2 per dag, wat past bij opgeslagen of gedeelde ad-posts). Dit rapport is dus een terugblik op de laatste leveringsperiode, geen live stand.

Het account act_607231713057715 (Robin Rutten) uit de command bestaat niet in Pipeboard. Het tweede beschikbare account (AmbitionAvenue, act_1489853856181844) heeft geen campagnes.

| Campagne | Status | Sinds | Laatste levering |
|----------|--------|-------|------------------|
| Wholesaler Campagne (SWE) | Paused | 28 aug 2026 | 4 sep 2026 |
| Wholesaler Campagne (LIT) | Paused | 27 aug 2026 | 4 sep 2026 |
| 2026: SYBB - Kopie | Paused | 19 apr 2026 | geen spend in periode |
| 2026: SYBB | Paused | 13 jan 2026 | geen spend in periode |
| Last push Nozzle Up | Paused | 15 sep 2025 | geen spend in periode |
| Nozzle Up END OF AUGUST | Paused | 26 aug 2025 | geen spend in periode |
| Campagne Nozzle Up 2025 1 | Paused | 23 jul 2025 | geen spend in periode |

### Overzicht per campagne (last 30d)

| Campagne | Status | Spend | Impressions | Reach | Freq. | Clicks | CTR | CPC | CPM | Link clicks | Meta leads | PostHog sessies | PostHog inzendingen | Kosten / inzending |
|----------|--------|-------|-------------|-------|-------|--------|-----|-----|-----|-------------|------------|-----------------|---------------------|--------------------|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 22.909 | 3,97 | 1.617 | 1,8% | €0,35 | €6,18 | 881 | 11 | 815 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 11.919 | 3,29 | 1.237 | 3,2% | €0,41 | €12,92 | 696 | 8 | 597 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | **130.155** | 34.828 | | 2.854 | 2,2% | €0,37 | €8,22 | 1.577 | 19 | 1.412 | 23 | €46,49 |

ROAS is niet van toepassing: beide campagnes hebben OUTCOME_LEADS als doel, er zijn geen aankoopwaarden.

**Meetverschil Meta vs PostHog:** Meta telt 277 landing page views en 19 leads, PostHog telt 1.412 sessies (90% van de 1.577 link clicks) en 23 inzendingen met een ad-UTM. Daarnaast 9 inzendingen zonder UTM (organisch of direct), samen 35 in 30 dagen. De Meta pixel telt structureel te weinig op /become-a-distributor; baseer kostenberekeningen op PostHog.

### Overzicht per ad (last 30d)

| Ad | Spend | Impr. | Freq. | CTR | CPC | CPM | Link clicks | Meta leads | PostHog sessies | Bounce | Gem. duur | Inzendingen | Sessie → inzending | Kosten / inzending |
|----|-------|-------|-------|-----|-----|-----|-------------|------------|-----------------|--------|-----------|-------------|--------------------|--------------------|
| Video 1 (LIT) | €146,91 | 19.041 | 1,90 | 2,4% | €0,32 | €7,72 | 242 | 3 | 248 | 30,6% | 69s | 5 | 2,0% | €29,38 |
| Video 2 (LIT) | €143,74 | 17.267 | 2,52 | 1,4% | €0,58 | €8,32 | 179 | 4 | 141 | 29,8% | 96s | 5 | 3,5% | €28,75 |
| Statisch 1 (LIT) | €144,24 | 28.434 | 2,91 | 1,0% | €0,49 | €5,07 | 163 | 3 | 134 | 29,1% | 103s | 4 | 3,0% | €36,06 |
| Statisch 2 (LIT) | €127,25 | 26.146 | 2,37 | 2,4% | €0,20 | €4,87 | 297 | 1 | 292 | 28,1% | 52s | 2 | 0,7% | €63,63 |
| Statisch 2 (SWE) | €128,13 | 13.265 | 1,97 | 4,0% | €0,24 | €9,66 | 286 | 5 | 256 | 22,3% | 114s | 3 | 1,2% | €42,71 |
| Video 2 (SWE) | €127,00 | 7.441 | 2,02 | 2,5% | €0,69 | €17,07 | 114 | 1 | 97 | 23,7% | 74s | 2 | 2,1% | €63,50 |
| Video 1 (SWE) | €126,75 | 8.299 | 2,05 | 2,9% | €0,53 | €15,27 | 139 | 0 | 113 | 20,4% | 75s | 0 | 0,0% | n.v.t. |
| Statisch 1 (SWE) | €125,36 | 10.262 | 2,15 | 2,7% | €0,45 | €12,22 | 157 | 2 | 131 | 19,8% | 210s | 2 | 1,5% | €62,68 |

### Underperformers

- **Video 2 (SWE)**, CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15) → Aanbeveling: niet herstarten in huidige vorm. Duurste klik van alle acht ads, en de Zweedse videoveilingen zijn structureel duurder dan de statische varianten.
- **Video 1 (SWE)**, CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15) en 0 inzendingen op 113 sessies → Aanbeveling: uitschakelen. Enige ad zonder één inzending in 30 dagen, ondanks 139 link clicks.
- **Video 2 (LIT)**, CPC €0,58 (drempel €0,50) → Aanbeveling: behouden ondanks de CPC. Het is de goedkoopste inzending van alle ads (€28,75) met de hoogste sessie-naar-inzending ratio (3,5%). Link CTR alleen zegt hier weinig.
- **Wholesaler Campagne (LIT)**, frequency 3,97 op campagneniveau (drempel 3,5) → Aanbeveling: bij herstart nieuwe creatives of een bredere doelgroep. Het Litouwse publiek is klein (22.909 bereik) en was na twee weken verzadigd.
- **Statisch 2 (LIT)**, laagste CPC (€0,20) maar slechts 0,7% sessie-naar-inzending en de kortste sessies (52s) → Aanbeveling: trekt goedkoop veel kliks, maar het verkeerde publiek. Hook of doelgroep herzien voor herstart.

Geen enkele ad zit onder de 1% CTR (Statisch 1 LIT zit met 1,0% op de grens).

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes zonder aankoopwaarde)
- **Goedkoopste inzending**: Video 2 (LIT), €28,75 per inzending
- **Hoogste conversie**: Video 2 (LIT), 3,5% sessie-naar-inzending

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, volledig besteed tussen 27 augustus en 4 september)
- **Beste performer**: Wholesaler Campagne (LIT). Ruim twee keer zo goedkoop per inzending als SWE (€35,13 tegenover €72,46) bij lagere CPC en CPM. Binnen LIT zijn de twee video's de winnaars, allebei rond €29 per inzending.
- **Slechtste performer**: Video 1 (SWE). Nul inzendingen bij €126,75 spend en een CPM boven de drempel. Ook Video 2 (SWE) en Statisch 1 (SWE) zitten boven €60 per inzending.
- **Aanbeveling (70-20-10)**: bij een herstart 70% van het budget naar de bewezen LIT-winnaars (Video 1, Video 2, Statisch 1) en Statisch 2 (SWE), met verse creatives om de frequency van 3,97 te doorbreken. 20% naar een variatie op Video 2 (LIT) voor het Zweedse publiek, omdat SWE geen werkende video heeft. 10% experiment: een nieuwe hook voor Statisch 2 (LIT), dat wel klikt maar niet converteert. Video 1 (SWE) niet meer inzetten.
- **Openstaand besluit**: de campagnes staan sinds 4 september stil. Er is in dit rapport geen actie mogelijk zolang niet vaststaat of en wanneer ze hervat worden.

### Funnel (PostHog, 30d, alle verkeer op /become-a-distributor)

| Stap | Aantal | Conversie vanaf vorige stap |
|------|--------|-----------------------------|
| wholesaler_page_view | 1.739 | |
| wholesaler_form_start | 138 | 7,9% |
| wholesaler_form_submit | 35 | 25,4% |
| wholesaler_booking_view | 35 | 100% |

Van pageview naar inzending: 2,0%. Het grootste lek zit tussen pageview en form start (92% haakt af voor het formulier). Wie het formulier start, maakt het in een kwart van de gevallen af.

### Google Sheet

Overgeslagen op verzoek. Rapport alleen lokaal opgeslagen.
