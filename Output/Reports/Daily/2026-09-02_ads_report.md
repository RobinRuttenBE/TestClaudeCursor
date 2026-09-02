## Meta Ads Rapport, 2 september 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode:** last 30 days (3 aug t/m 1 sep 2026). Beide actieve campagnes draaien pas sinds 27/28 augustus, dus de 30d-cijfers zijn feitelijk 5 tot 6 dagen data.
**Databron:** Meta Ads via Pipeboard (directe JSON-RPC call, de MCP zelf meldde "requires authentication"). Geen Google MCPs gebruikt, geen Google Sheet geschreven.
**Opmerking:** het in het command genoemde account act_607231713057715 (Robin Rutten) bestaat niet in Pipeboard. Het tweede beschikbare account (AmbitionAvenue, act_1489853856181844) heeft geen campagnes.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Leads | CPL | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|-------|-----|------|
| Wholesaler Campagne (LIT) | Active | €390,33 | 57.230 | 1.149 | 2,0% | €0,34 | €6,82 | 3,58 | 11 | €35,48 | n.v.t. |
| Wholesaler Campagne (SWE) | Active | €343,29 | 25.060 | 845 | 3,4% | €0,41 | €13,70 | 3,03 | 5 | €68,66 | n.v.t. |
| **Totaal** | | **€733,62** | **82.290** | **1.994** | **2,4%** | **€0,37** | **€8,92** | | **16** | **€45,85** | |

ROAS is niet van toepassing: beide campagnes zijn lead-campagnes (OUTCOME_LEADS, optimalisatie op offsite conversions) zonder aankoopwaarde. "Leads" = Meta pixel lead events.

Setup per campagne: 4 ad sets met elk 1 ad, elk €20,00 per dag. Totaal dagbudget €160,00 (8 ad sets).

### Ad-level performance

**Wholesaler Campagne (LIT), targeting Litouwen**

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | LPV | Leads | CPL |
|----|-------|-------|--------|-----|-----|-----|-------|-----|-------|-----|
| Video 1 (LIT) | €103,87 | 12.510 | 316 | 2,5% | €0,33 | €8,30 | 1,77 | 19 | 3 | €34,62 |
| Statisch 1 (LIT) | €101,29 | 17.215 | 209 | 1,2% | €0,48 | €5,88 | 2,61 | 18 | 3 | €33,76 |
| Video 2 (LIT) | €99,87 | 11.906 | 193 | 1,6% | €0,52 | €8,39 | 2,29 | 16 | 4 | €24,97 |
| Statisch 2 (LIT) | €85,30 | 15.599 | 431 | 2,8% | €0,20 | €5,47 | 2,16 | 30 | 1 | €85,30 |

**Wholesaler Campagne (SWE), targeting Zweden**

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | LPV | Leads | CPL |
|----|-------|-------|--------|-----|-----|-----|-------|-----|-------|-----|
| Video 1 (SWE) | €88,37 | 5.566 | 186 | 3,3% | €0,48 | €15,88 | 1,90 | 23 | 0 | geen lead |
| Statisch 2 (SWE) | €87,63 | 8.204 | 348 | 4,2% | €0,25 | €10,68 | 1,87 | 46 | 4 | €21,91 |
| Statisch 1 (SWE) | €85,53 | 6.722 | 198 | 2,9% | €0,43 | €12,72 | 1,98 | 33 | 1 | €85,53 |
| Video 2 (SWE) | €81,76 | 4.568 | 113 | 2,5% | €0,72 | €17,90 | 1,87 | 9 | 0 | geen lead |

LPV = landing page views.

### Gisteren (1 september)

| Campagne | Spend | Impr. | Clicks | CTR | CPC | Leads |
|----------|-------|-------|--------|-----|-----|-------|
| LIT | €101,29 | 16.137 | 283 | 1,8% | €0,36 | 1 |
| SWE | €94,81 | 6.505 | 174 | 2,7% | €0,54 | 0 |

Beide campagnes geven meer uit dan het ingestelde dagbudget van €80,00 (Meta mag tot 25% meer uitgeven op dagbasis). SWE zit gisteren boven de CPC-drempel en leverde geen leads.

### Underperformers

- **Video 2 (SWE)**, CPC €0,72 (drempel €0,50), CPM €17,90 (drempel €15,00), 0 leads na €81,76. Aanbeveling: pauzeren. Duurste ad van het account zonder resultaat.
- **Video 1 (SWE)**, CPM €15,88 (drempel €15,00), 0 leads na €88,37. CTR is prima (3,3%) maar de klik converteert niet. Aanbeveling: nog 2 dagen geven; blijft het op 0 leads, pauzeren.
- **Video 2 (LIT)**, CPC €0,52 (drempel €0,50). Maar: laagste CPL van heel LIT (€24,97, 4 leads). Aanbeveling: laten draaien, de CPC-overschrijding is marginaal en de leadprijs compenseert.
- **Wholesaler Campagne (LIT)**, frequency 3,58 (drempel 3,5) na 6 dagen. Creative fatigue risico: de Litouwse doelgroep is klein (reach 15.995). Aanbeveling: binnen een week nieuwe creatives of doelgroep verbreden.
- **Statisch 1 (LIT)**, CTR 1,2%, vlak boven de drempel van 1%, frequency 2,61 (hoogste ad-level). Aanbeveling: monitoren, bij CTR onder 1% vervangen.
- **Statisch 2 (LIT) en Statisch 1 (SWE)**, CPL €85,30 en €85,53. Hoge CTR maar de klikkers converteren niet. Geen actie nu, wel aandachtspunt bij de volgende optimalisatieronde.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,2%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Laagste CPL**: Statisch 2 (SWE), €21,91 (4 leads uit €87,63)
- **Beste ROAS**: n.v.t. (lead-campagnes)

Opvallend: de "Statisch 2" creative wint in beide landen op CTR en CPC. In Zweden is het ook de leadmotor (4 van de 5 leads). In Litouwen levert het veel goedkoop verkeer, maar slechts 1 lead. Verschil zit waarschijnlijk in de landingspagina of de aansluiting van de hook op wat de pagina belooft.

### Funnel-signaal: klik naar landingspagina

| Campagne | Link clicks | Landing page views | LPV-rate |
|----------|-------------|--------------------|----------|
| SWE | 489 | 111 | 22,7% |
| LIT | 614 | 83 | 13,5% |

Meer dan driekwart van de link clicks bereikt de landingspagina niet als geregistreerde view. Dat wijst op een trage pagina, pixel die te laat laadt, of veel onbedoelde tikken op mobiel. Dit is de grootste lekkage in de funnel en groter dan elk ad-level verschil. Aanbeveling: laadsnelheid van de wholesaler-landingspagina checken op mobiel en de Meta pixel-plaatsing verifiëren (via `/tracking-check`).

### Samenvatting

- **Totaal spend**: €733,62 (periode last 30 days, feitelijk 27 aug t/m 1 sep). 16 leads, gemiddelde CPL €45,85.
- **Beste performer**: Wholesaler Campagne (LIT). 11 leads voor €35,48 per lead, CPC €0,34 en CPM €6,82. Goedkope markt, maar frequency loopt al op.
- **Slechtste performer**: Wholesaler Campagne (SWE). CPL €68,66, bijna het dubbele van LIT. Twee van de vier ads (beide video's) hebben nog geen enkele lead opgeleverd voor samen €170,13. De Zweedse markt is per impressie twee keer zo duur (CPM €13,70 vs €6,82).
- **Aanbeveling (70-20-10)**:
  1. **70% budget naar bewezen winnaars**: Statisch 2 in beide landen plus Video 2 (LIT). Verhoog het dagbudget van Statisch 2 (SWE) van €20 naar €35 en Statisch 2 (LIT) naar €30.
  2. **Pauzeer Video 2 (SWE)** vandaag. Geef Video 1 (SWE) tot 4 september; geen lead, dan ook pauzeren. Vrijgekomen budget naar Statisch 2 (SWE).
  3. **20% variaties**: maak 2 nieuwe statische varianten op basis van de Statisch 2 hook voor Litouwen. Nodig vóór de frequency de 4 passeert (verwacht binnen 3 tot 4 dagen bij huidig tempo).
  4. **Fix de funnel-lek**: LPV-rate van 13 tot 23% is het echte probleem. Eén technische fix op de landingspagina heeft meer effect dan elke ad-optimalisatie.

### Gepauzeerde campagnes (context)

| Campagne | Laatste update | Spend 30d |
|----------|----------------|-----------|
| 2026: SYBB - Kopie | 27 aug 2026 | €0,00 |
| 2026: SYBB | 19 apr 2026 | €0,00 |
| Last push Nozzle Up | 21 sep 2025 | €0,00 |
| Nozzle Up END OF AUGUST | 15 sep 2025 | €0,00 |
| Campagne Nozzle Up 2025 1 | 15 sep 2025 | €0,00 |

SYBB heeft in de afgelopen 30 dagen geen spend gehad. Alle actieve uitgaven gaan naar de twee wholesaler-campagnes.

### Google Sheet

Niet geschreven, op verzoek overgeslagen voor deze run. Rapport alleen lokaal opgeslagen.
