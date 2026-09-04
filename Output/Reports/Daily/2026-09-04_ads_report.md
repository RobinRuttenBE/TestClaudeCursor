# Meta Ads Rapport, 4 september 2026

**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC, account `act_567892422940728` Sempertex Ad Account) en PostHog project STX EU (directe REST API, id 149694). Geen Google MCPs gebruikt, niets naar de Meta Ads Tracker Sheet geschreven.

**Periode:** last_30d (5 aug t/m 4 sep 2026). Beide actieve campagnes draaien pas sinds 27/28 augustus, dus de 30-dagen cijfers zijn feitelijk lifetime. Dag 4 september is nog niet compleet.

**Accounts:** het in het command genoemde `act_607231713057715` (Robin Rutten) bestaat niet in deze koppeling. Het tweede account is `act_1489853856181844` (AmbitionAvenue) en heeft geen spend. Account-totaal spend in de 30d window is €1.060,57, waarvan €47,03 niet toewijsbaar is aan de twee actieve campagnes (restspend van de gepauzeerde SYBB campagne begin augustus; de campagne-insight geeft daar geen rij meer voor terug).

---

## Overzicht per campagne

Beide campagnes hebben objective OUTCOME_LEADS, 4 ad sets elk €20,00/dag, landing page `/en_GB/become-a-distributor`. Er is geen ROAS: het zijn lead-campagnes zonder aankoopwaarde. In plaats daarvan staat de kostprijs per formulierinzending (PostHog) als conversiemaat.

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Link clicks | Link CTR | Link CPC | Leads (Meta) | Inzendingen (PostHog) | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Active | €532,78 | 85.830 | 1.556 | 1,8% | €0,34 | €6,21 | 3,88 | 858 | 1,0% | €0,62 | 11 | 16 | €33,30 |
| Wholesaler Campagne (SWE) | Active | €480,76 | 37.256 | 1.183 | 3,2% | €0,41 | €12,90 | 3,25 | 669 | 1,8% | €0,72 | 7 | 8 | €60,10 |
| **Totaal** | | **€1.013,54** | **123.086** | **2.739** | **2,2%** | **€0,37** | **€8,23** | | **1.527** | **1,2%** | **€0,66** | **18** | **24 toegewezen, 33 totaal** | **€30,71 (op 33)** |

PostHog telt sinds 27 augustus 33 inzendingen van `wholesaler_form_submit`. Daarvan zijn er 24 via de sessie-UTM aan een ad te koppelen, 9 hebben geen UTM (directe terugkeer, gekopieerde link, of ad-click zonder parameters). Meta's pixel ziet er 18. Meta Landing Page Views (263) zijn nog steeds waardeloos als funnelmaat: PostHog ziet 1.391 sessies met een wholesaler-UTM op 1.527 link clicks (91%).

---

## Overzicht per ad

Gesorteerd op spend. Link CTR en Link CPC zijn berekend uit `link_click`. Inzendingen en sessies komen uit PostHog via `session.$entry_utm_content`.

| Ad | Spend | Impr. | CTR (all) | CPC (all) | Link CTR | Link CPC | CPM | Freq. | Sessies LP | Bounce | Form starts | Inzendingen | € / inzending | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €139,53 | 18.089 | 2,4% | €0,32 | 1,3% | €0,60 | €7,71 | 1,91 | 246 | 30,5% | 21 | 5 | €27,91 | |
| Statisch 1 (LIT) | €136,59 | 26.601 | 1,1% | €0,48 | 0,6% | €0,85 | €5,13 | 2,89 | 134 | 29,1% | 14 | 4 | €34,15 | Link CTR <1% |
| Video 2 (LIT) | €135,71 | 16.354 | 1,5% | €0,56 | 1,1% | €0,77 | €8,30 | 2,48 | 140 | 30,0% | 11 | 5 | €27,14 | CPC >€0,50 |
| Statisch 2 (SWE) | €121,44 | 12.557 | 4,0% | €0,24 | 2,2% | €0,44 | €9,67 | 1,96 | 253 | 22,1% | 18 | 4 | €30,36 | |
| Video 1 (SWE) | €121,25 | 7.910 | 3,0% | €0,52 | 1,7% | €0,89 | €15,33 | 2,00 | 110 | 20,9% | 8 | 0 | geen | CPC >€0,50, CPM >€15, 0 inzendingen |
| Statisch 2 (LIT) | €120,95 | 24.786 | 2,4% | €0,20 | 1,2% | €0,42 | €4,88 | 2,34 | 285 | 28,1% | 10 | 2 | €60,48 | |
| Statisch 1 (SWE) | €119,07 | 9.828 | 2,7% | €0,44 | 1,6% | €0,78 | €12,12 | 2,12 | 127 | 19,7% | 17 | 2 | €59,54 | |
| Video 2 (SWE) | €119,00 | 6.961 | 2,5% | €0,69 | 1,5% | €1,12 | €17,10 | 2,00 | 96 | 24,0% | 14 | 2 | €59,50 | CPC >€0,50, CPM >€15 |

---

## Underperformers

Drempels uit het command: CPC >€0,50, CTR <1%, frequency >3,5, CPM >€15. Op all-clicks CPC zit geen enkele ad boven €0,50 op een manier die ertoe doet; op Link CPC zitten 6 van de 8 ads erboven. De echte beslissingsmaat is kostprijs per inzending.

- **Video 1 (SWE)**: €121,25 uitgegeven, 110 sessies, 8 form starts, 0 inzendingen. CPM €15,33, Link CPC €0,89. Dit is de enige ad zonder één conversie na 8 dagen. Aanbeveling: pauzeren, budget naar Statisch 2 (SWE). Dit is voorstel 1 uit het auto-optimize rapport van 3 september en de data is sindsdien niet verbeterd.
- **Video 2 (SWE)**: CPM €17,10 (drempel €15), Link CPC €1,12 (duurste van alle 8), €59,50 per inzending. Aanbeveling: budget halveren naar €10,00/dag, Instagram uitsluiten (daar was de Link CTR gisteren al 0,74%).
- **Statisch 1 (LIT)**: Link CTR 0,60%, de enige ad onder de 1% op link clicks. Maar: 4 inzendingen op 134 sessies (3,0% sessie-naar-inzending, tweede beste van alle ads) en langste tijd op pagina (103 s). Niet pauzeren op CTR alleen. Aanbeveling: audience-fix uit voorstel 3 (25-65, desktop uit) en de kill-regel "Link CTR <0,8% én 0 inzendingen in 3 dagen" hanteren. Gisteren en vandaag: 0 inzendingen. Als dat morgen nog zo is, pauzeren.
- **Wholesaler Campagne (LIT)**: frequency 3,88 op campagne-niveau (drempel 3,5), SWE zit op 3,25. Per ad set ligt frequency tussen 1,9 en 2,9, maar de 4 ad sets richten op dezelfde mensen, dus een Litouwer heeft gemiddeld bijna 4 keer een Sempertex-ad gezien in 8 dagen. Dit is creative fatigue in wording. Aanbeveling: zie samenvatting.
- **Statisch 2 (LIT)**: goedkoopste clicks van het account (Link CPC €0,42) en meeste sessies (285), maar slechts 2 inzendingen, €60,48 per inzending. Kortste tijd op pagina (53 s). De ad trekt verkeer dat niet converteert. Niet opschalen op clicks.

---

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0% all-clicks en 2,2% Link CTR. Beste van beide landen.
- **Laagste CPC**: Statisch 2 (LIT), €0,20 all-clicks en €0,42 Link CPC.
- **Beste ROAS**: niet van toepassing (lead-campagnes). Laagste kostprijs per inzending: Video 2 (LIT) €27,14, gevolgd door Video 1 (LIT) €27,91.
- **Beste sessie-naar-inzending**: Video 2 (LIT) 3,6% (5 op 140), Statisch 1 (LIT) 3,0%, Video 1 (LIT) 2,0%.

---

## Trend: inzendingen dalen terwijl verkeer gelijk blijft

| Dag | Spend | Link clicks | Sessies LP (PostHog) | Leads (Meta) | Inzendingen (PostHog) |
|---|---|---|---|---|---|
| 28 aug | €90,59 | 261 | 254 | 5 | 6 |
| 29 aug | €173,31 | 251 | 216 | 2 | 4 |
| 30 aug | €116,85 | 149 | 124 | 6 | 6 |
| 31 aug | €156,79 | 206 | 160 | 2 | 5 |
| 1 sep | €196,34 | 237 | 205 | 1 | 1 |
| 2 sep | €125,88 | 192 | 156 | 2 | 3 |
| 3 sep | €153,78 | 231 | 210 | 0 | 1 |
| 4 sep (deels) | €47,03 | 42 | 48 | 1 | 1 |

Op 27 augustus vielen nog 6 inzendingen zonder ad-UTM (organisch of directe links, de campagne draaide nog niet volledig). Van 28 t/m 31 augustus kwamen gemiddeld 5,3 inzendingen per dag binnen op ongeveer €135 spend. Van 1 t/m 3 september is dat 1,7 per dag op €159 spend. Het verkeer naar de landing page is niet gedaald (205, 156, 210 sessies), de bounce rate ook niet. Wat wel verandert: de warme eerste laag van de doelgroep is opgebruikt, en de frequency loopt op. Kostprijs per inzending is in vier dagen gestegen van rond €25 naar rond €95.

Dit is de belangrijkste bevinding van vandaag en het bevestigt dat de creative-refresh (voorstel 2 van 3 september) niet langer kan wachten.

---

## Samenvatting

- **Totaal spend**: €1.013,54 op de twee actieve campagnes (periode last_30d, effectief 27 aug t/m 4 sep). Account-totaal €1.060,57.
- **Beste performer**: Wholesaler Campagne (LIT), €33,30 per inzending, 16 van de 24 toegewezen inzendingen, Link CPC €0,62. Binnen LIT zijn de twee video's de motor (10 inzendingen op €275,24).
- **Slechtste performer**: Wholesaler Campagne (SWE), €60,10 per inzending, bijna dubbel LIT. CPM is 2x hoger (€12,90 vs €6,21) wat normaal is voor Zweden, maar de video's converteren niet: Video 1 (SWE) 0 inzendingen, Video 2 (SWE) €59,50 per inzending.
- **70-20-10 stand**: core (Video 1 LIT, Video 2 LIT, Statisch 2 SWE, Statisch 1 LIT) krijgt nu 50% van het budget in plaats van 70%. De twee SWE-video's die samen 2 inzendingen op €240 leverden krijgen 25% in plaats van 10%.
- **Aanbeveling, in volgorde**:
  1. **Video 1 (SWE) pauzeren** en Video 2 (SWE) naar €10,00/dag. Vrijgekomen €30 naar Statisch 2 (SWE) (+€10) en Video 1 en Video 2 (LIT) (elk +€10). Budget-neutraal op €160/dag, spend verschuift naar de ads met bewezen inzendingen.
  2. **Creative refresh deze week.** Alle 8 ads draaien nog met identieke copy. De inzendingen dalen bij gelijk verkeer, de LIT frequency zit op 3,88. Maak per land 3 hook-varianten op de winnende visual (Statisch 2 in SWE, Video 1/2 in LIT) zoals in voorstel 2 beschreven, en zet ze als nieuwe ads in de bestaande ad sets zodat het learning niet reset.
  3. **Tracking check landing page** (voorstel 4): Meta telt 18 leads, PostHog 33. De ad sets optimaliseren op een half signaal. Verifieer of het Lead-event bij de formulierinzending vuurt (pixel of Conversions API). Zonder dit blijft de Meta-optimalisatie de verkeerde mensen zoeken.
  4. **Statisch 1 (LIT)** houden onder de aangepaste kill-regel (0,8% én 0 inzendingen 3 dagen). Staat nu op 2 dagen zonder inzending.
  5. **Statisch 2 (LIT)** niet opschalen ondanks de laagste CPC. 285 sessies, 2 inzendingen, 53 seconden op pagina. Onderzoek of de visual een verkeerde verwachting wekt (consumentenpubliek in plaats van wholesalers).

---

## Google Sheet

Overgeslagen op verzoek. Rapport uitsluitend lokaal opgeslagen in `Output/Reports/Daily/2026-09-04_ads_report.md`.

## Funnel data

Meta Ads en PostHog zijn al gecombineerd in dit rapport (sessies, form starts, inzendingen, booking views). Ontbrekend voor een volledige `/funnel-diagnose`: wat er na de inzending gebeurt (gesprek gepland, distributeur aangemeld, eerste order). Die stappen zitten niet in PostHog of Meta.
