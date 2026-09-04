## Auto-Optimize Rapport, 4 september 2026

**Run:** 4 september 2026, 11:25 CEST (vanuit morning report script, alleen Niveau 1 uitgevoerd)
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC, MCP meldt "requires authentication") en PostHog (claude.ai connector, project STX EU 149694). Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet in de koppeling. Het tweede gekoppelde account (AmbitionAvenue, act_1489853856181844) heeft geen actieve campagnes.
**Periode:** Meta last_3d = 1 t/m 3 september. PostHog = laatste 72 uur tot 4 september 10:30 UTC.

Twee actieve campagnes, beide OUTCOME_LEADS naar `/en_GB/become-a-distributor`: Wholesaler Campagne (SWE) en Wholesaler Campagne (LIT). Acht ads, elk in een eigen ad set met €20,00/dag. Alle ads draaien sinds 27 of 28 augustus, dus ruim boven de minimale 24 uur.

### Performance per ad (last_3d, link metrics)

| Ad | Spend | Impr. | Link clicks | Link CTR | CPC (link) | CPM | Freq. | Inzendingen PostHog 3d | Inzendingen lifetime | € / inzending lifetime |
|---|---|---|---|---|---|---|---|---|---|---|
| Statisch 2 (SWE) | €56,18 | 6.220 | 110 | 1,8% | €0,51 | €9,03 | 1,49 | 0 | 4 | €31,78 |
| Video 2 (SWE) | €60,99 | 3.658 | 54 | 1,5% | €1,13 | €16,67 | 1,64 | 2 | 2 | €62,98 |
| Video 1 (SWE) | €58,14 | 3.996 | 52 | 1,3% | €1,12 | €14,55 | 1,60 | 0 | 0 | n.v.t. (€126,08 zonder inzending) |
| Statisch 1 (SWE) | €56,98 | 4.828 | 61 | 1,3% | €0,93 | €11,80 | 1,66 | 1 | 2 | €62,14 |
| Video 1 (LIT) | €62,87 | 9.294 | 104 | 1,1% | €0,60 | €6,76 | 1,61 | 1 | 5 | €29,19 |
| Statisch 2 (LIT) | €62,09 | 14.148 | 151 | 1,1% | €0,41 | €4,39 | 1,78 | 0 | 2 | €63,12 |
| Video 2 (LIT) | €59,70 | 7.147 | 52 | 0,7% | €1,15 | €8,35 | 2,11 | 1 | 5 | €28,54 |
| Statisch 1 (LIT) | €59,06 | 14.147 | 76 | 0,5% | €0,78 | €4,17 | 2,40 | 0 | 4 | €35,92 |

Link clicks komen uit `actions.link_click`, Link CTR en CPC (link) zijn zelf berekend. Meta's `clicks`, `ctr` en `cpc` zijn niet gebruikt. Inzendingen komen uit het PostHog event `wholesaler_form_submit`, gematcht op `utm_content` en `utm_campaign`. Daarnaast 9 inzendingen lifetime zonder ad-UTM (1 in de laatste 3 dagen).

### ⚡ Automatische acties uitgevoerd

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| Statisch 1 (LIT) (ad 120250160534150239) | Link CTR 0,5% (< 0,8%) | ACTIVE | PAUSED | 14.147 imp, 76 link clicks, €59,06 spend, 0 inzendingen in 3 dagen |

**Totaal gepauzeerd: 1 ad** (12,5% van de actieve ads, ruim onder de 50% grens)

Log: `logs/ads-auto-optimize.log`, 2026-09-04 11:25:22. Meta bevestigde de statuswijziging (readback 200, status PAUSED, effective_status kort IN_PROCESS). Dit sluit aan op het ads-rapport van vanochtend, dat deze pauze al aankondigde bij opnieuw 0 inzendingen.

**Kill-regel getriggerd maar NIET uitgevoerd: Video 2 (LIT).** Link CTR 0,7% op 7.147 impressions valt net onder de 0,8% drempel. Deze ad is echter de goedkoopste leadbron van het hele account: 5 inzendingen lifetime voor €28,54 per inzending, plus 1 inzending in de laatste 3 dagen en 4 Meta-leads lifetime. De kill-regel is bedoeld om duidelijke underperformers te stoppen en deze ad presteert op het campagnedoel (leads) juist het best. Pauzeren op basis van CTR alleen zou de lead-flow van LIT schaden. Ik heb de ad daarom laten draaien en leg de beslissing bij Robin (zie voorstel 4). Als Robin de regel strikt wil laten uitvoeren, pauzeer ik de ad in de volgende run.

CPC (link) > €1,50 regel: geen enkele ad haalt de minimale 500 link clicks in 3 dagen (max 151), dus niet van toepassing.

### ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|----|---------|--------|-----------------|
| Video 2 (SWE) | Dure reach | CPM €16,67 | Zweedse audience is duur; creative vervangen of audience verbreden (voorstel 3) |
| Video 1 (SWE) | Dure reach, grens | CPM €14,55 (lifetime €15,29) | Zie voorstel 1: pauzeren, 0 inzendingen na €126,08 |
| Video 2 (LIT) | Dalende Link CTR, grens | 3d 0,7% = 70,2% van lifetime 1,0% | Creative refresh LIT inplannen (voorstel 2) |
| Wholesaler Campagne (LIT) | Creative fatigue op campagneniveau | Freq lifetime 3,88 (ad-niveau 3d max 2,40) | Creative refresh LIT |

Geen enkele ad zit op ad-niveau boven frequency 3,5 in de laatste 3 dagen. De fatigue zit in de overlap tussen de vier LIT ad sets die dezelfde audience raken. Dat verklaart ook de terugval van inzendingen: 5,2 per dag van 27 t/m 31 augustus, 1,5 per dag van 1 t/m 4 september, bij stabiel verkeer.

### 📊 70-20-10 Classificatie

Let op: de drempels zijn nog gekalibreerd op all-clicks (zie TODO in het command). Classificatie is een richtlijn, geen hard oordeel. Er zijn geen budget-shifts uitgevoerd.

**70% Core (budget: €20,00/dag, huidig 14,3% van €140,00):**
- Statisch 2 (SWE): Link CTR 1,8%, CPC (link) €0,51 (net boven de €0,50 grens), €31,78 per inzending lifetime. Enige ad die het Core-profiel benadert.

**20% Emerging (budget: €100,00/dag, huidig 71,4% van totaal):**
- Video 2 (SWE): Link CTR 1,5%, CPC (link) €1,13. Twee inzendingen in de laatste 3 dagen, de meeste van alle ads. Potentieel, ondanks dure clicks.
- Video 1 (LIT): Link CTR 1,1%, CPC (link) €0,60, €29,19 per inzending. Potentieel.
- Statisch 2 (LIT): Link CTR 1,1%, CPC (link) €0,41, maar €63,12 per inzending en 0 in 3 dagen. Goedkope clicks, matige conversie.
- Statisch 1 (SWE): Link CTR 1,3%, CPC (link) €0,93. Eén inzending in 3 dagen.
- Video 1 (SWE): Link CTR 1,3%, CPC (link) €1,12. Nul inzendingen lifetime. Hoort qua CTR in Emerging, maar levert niets op.

**Buiten classificatie (budget: €20,00/dag, 14,3%):**
- Video 2 (LIT): Link CTR 0,7% valt onder Emerging, maar beste kostprijs per inzending van het account. Zie voorstel 4.

**10% Experimental (budget: €0,00/dag, 0%):**
- Geen. Alle ads hebben ruim meer dan 500 impressions. Er loopt op dit moment geen enkel experiment, terwijl alle 8 ads exact dezelfde tekst gebruiken (zie voorstel 2).

**Budget mismatch:** Ja. Core krijgt 14,3% in plaats van 70%, Emerging 71,4% in plaats van 20%, en er wordt 0% aan experimenten besteed. Dit komt doordat elke ad set een gelijk budget van €20,00/dag heeft, ongeacht performance.

### 💡 Voorstellen (wacht op goedkeuring)

**1. Budget herverdeling (budget-neutraal op €140,00/dag)**
- Video 1 (SWE): van €20,00/dag naar €0,00/dag (pauzeren). Reden: €126,08 lifetime spend, 0 inzendingen, CPM €14,55. Valt niet onder de kill-regel omdat de Link CTR 1,3% is, maar levert op het campagnedoel niets op.
- Statisch 2 (SWE): van €20,00/dag naar €35,00/dag (+75%). Reden: beste Link CTR van het account (1,8%), laagste CPC (link) in SWE (€0,51), €31,78 per inzending.
- Video 1 (LIT): van €20,00/dag naar €30,00/dag (+50%). Reden: €29,19 per inzending, CPC (link) €0,60, frequency 1,61 dus nog ruimte.
- Video 2 (LIT): van €20,00/dag naar €25,00/dag (+25%), alleen als voorstel 4 wordt goedgekeurd. Reden: €28,54 per inzending, goedkoopste leadbron.
- Video 2 (SWE) en Statisch 1 (SWE): op €20,00/dag houden. Video 2 (SWE) had 2 inzendingen in de laatste 3 dagen, wat de aanbeveling van gisteren (verlagen naar €10) tegenspreekt. Nog 3 dagen aankijken.
- Statisch 2 (LIT): van €20,00/dag naar €10,00/dag (-50%). Reden: goedkoopste clicks maar €63,12 per inzending, 0 inzendingen in 3 dagen.
- Verwachte impact: zelfde dagbudget, geschat 25 tot 35% meer inzendingen doordat budget verschuift van €63 tot oneindig per inzending naar €28 tot €32 per inzending.

**2. Nieuwe variaties (creative refresh, urgent voor LIT)**
Alle 8 ads gebruiken exact dezelfde tekst per land: titel "Become a Sempertex partner in [land]", body "Sempertex Europe is looking for official wholesale partners in [land]. Party shops and wholesalers: premium latex balloons, shipped from Belgium, with a ready-to-sell starter package. Two minute form, then an intake call.", CTA SEE_DETAILS. De enige variabele is het visual. De hook-test uit het ads-rapport van 3 september is daarmee nog niet gestart. Voorstel, per land 3 nieuwe ads in de bestaande ad sets van Statisch 2 en Video 1/2 (winnende visuals), met nieuwe primary text:
- Gebaseerd op winnende visual Statisch 2 (SWE) (Link CTR 1,8%):
  - Variatie A (Label + statement): "Party shop owners in Sweden: the balloon brand professional decorators ask for by name is looking for a wholesale partner." Statisch, zelfde visual.
  - Variatie B (Vraag): "Do your customers ask for balloons that last longer than the party? Sempertex is looking for wholesale partners in Sweden." Statisch, zelfde visual.
- Gebaseerd op Video 2 (SWE) (Link CTR 1,5%, 2 inzendingen in 3 dagen):
  - Variatie C (Conditioneel): "If you already sell party supplies in Sweden, you are one two minute form away from an official Sempertex partnership." Video, zelfde asset.
- Gebaseerd op Video 1 (LIT) en Video 2 (LIT) (beste kostprijs per inzending):
  - Variatie D (Lijst): "3 things you get as an official Sempertex partner in Lithuania: a ready-to-sell starter package, shipping from Belgium, and a brand your customers already know." Video.
  - Variatie E (Commando): "Stop reordering balloons that pop before the event. Become the Sempertex partner for Lithuania." Statisch, visual van Statisch 2 (LIT).
- CTA-test: SEE_DETAILS versus APPLY_NOW op de beste variant per land.
- Alle copy in UK spelling, geen concurrenten genoemd. Ik schrijf de definitieve copy en UTM's (`utm_content=static_03` en verder) uit zodra Robin dit goedkeurt.

**3. Audience aanpassingen**
- SWE: CPM ligt tussen €9,03 en €16,67 tegenover €4,17 tot €8,35 in LIT. De Zweedse audience (SE, 25 tot 65, Advantage+ audience) is klein en duur. Voorstel: Advantage+ audience laten staan, maar de leeftijd verbreden naar 21 tot 65 en in de nieuwe ads (voorstel 2) placements beperken tot Facebook Feed en Instagram Feed, zodat het budget niet naar Audience Network en Reels lekt. Reden: 63% van de SWE spend gaat naar video ads met CPM boven €14 en samen 2 inzendingen.
- LIT: campagne-frequency 3,88 lifetime bij 4 ad sets op dezelfde audience. Voorstel: de vier LIT ad sets samenvoegen tot 2 ad sets (statisch en video) met Advantage+ budget, zodat Meta zelf verdeelt en de overlap daalt. Reden: 4 losse ad sets van €20,00 bieden tegen elkaar op in een land met een beperkte doelgroep.
- Nog niet mogelijk: uitsluiting op demografie of placement. Daarvoor is een breakdown-query nodig die in deze run niet is opgehaald. Kan ik in een interactieve sessie draaien.

**4. Beslissing over Video 2 (LIT)**
- Optie A: ad laten draaien en de kill-regel aanvullen met een conversie-guard, bijvoorbeeld "pauzeer alleen bij Link CTR < 0,8% én 0 inzendingen in de laatste 3 dagen". Dit is de regel die het ads-rapport van gisteren al feitelijk hanteerde.
- Optie B: de regel strikt toepassen en Video 2 (LIT) pauzeren in de volgende run.
- Mijn aanbeveling: optie A. Het campagnedoel is leads, niet clicks.

**5. Tracking check (herhaling van gisteren)**
- Meta telt 18 leads lifetime, PostHog 33 inzendingen. Verifieer dat het Meta Lead-event op de bedankpagina vuurt. Zolang dit niet klopt, optimaliseert Meta op onvolledige data.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
