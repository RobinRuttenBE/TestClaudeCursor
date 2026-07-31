# SYBB Daily Report: 30 juli 2026

## 1. Samenvatting

De SYBB funnel stond op 30 juli volledig stil. De Meta campagne `2026: SYBB` staat op PAUSED en heeft sinds eind april 2026 nul delivery gehad: nul spend, nul impressies, nul clicks. De landing page `www.startyourballoonbusiness.com` kreeg gisteren 0 pageviews en 0 sessies. Dit is geen performance probleem maar een aan/uit probleem. Er valt niets te optimaliseren zolang de campagne uit staat.

Belangrijkste observatie deze week: het restje organisch verkeer droogt op. Drie opeenvolgende weken op de landing page laten 18, 14 en 2 pageviews zien. In het venster 24 t/m 30 juli waren er nog maar 2 pageviews verdeeld over 2 dagen, en beide sessies waren single page.

Tweede observatie, en die is belangrijker voor de herstart: de landing page tracking is onvolledig. Er worden geen scroll depth events en geen CTA click events gemeten. Vier van de zeven KPI rijen uit de skill kunnen daardoor niet berekend worden, ook niet als de campagne morgen weer aan gaat.

> Databronnen: Meta Ads via Pipeboard MCP (account `act_567892422940728`, Sempertex Ad Account) en PostHog MCP (project "Default project", id 149694, EU, host gefilterd op `www.startyourballoonbusiness.com`). Beide bronnen bevestigen onafhankelijk dat de funnel inactief was.

## 2. Meta Ads Performance

Campagne `2026: SYBB` (ID `120239435987290239`), status **PAUSED**, dagbudget €100,00 (niet actief), objective OUTCOME_SALES. Aangemaakt 13 januari 2026, laatste wijziging 19 april 2026.

| Metric | Gisteren (30 jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Insights API gaf een lege dataset terug voor 30 juli en voor elk van de zeven dagen in het venster 24 t/m 30 juli. Ook op accountniveau is er over 1 t/m 30 juli nul delivery. Er draait op dit moment geen enkele campagne in het account.

**Laatste bekende delivery, april 2026, als referentiepunt bij heractivatie:**

| Metric | April 2026 | Lifetime (13 jan t/m 31 jul) |
|--------|-----------|------------------------------|
| Spend | €1.059,47 | €2.485,04 |
| Impressions | 91.839 | 297.174 |
| Clicks | 1.935 | 12.067 |
| CTR | 2,11% | 4,06% |
| CPC | €0,55 | €0,21 |
| Frequency | 2,19 | 2,24 |
| Landing page views | 818 | 6.992 |
| Add to cart | 44 | 53 |
| Initiate checkout | 33 | 36 |
| Purchases | 6 | 6 |

Het contrast tussen april en lifetime is het signaal dat telt. Over de hele looptijd zat de campagne op CTR 4,06% en CPC €0,21. In april was dat verslechterd naar CTR 2,11% en CPC €0,55, dus de CPC lag toen ruim boven de target van €0,50 en was meer dan verdubbeld ten opzichte van het campagnegemiddelde. Dat patroon, dalende CTR met stijgende CPC en oplopende frequency, is klassieke creative fatigue. Dezelfde creatives opnieuw aanzetten betekent waarschijnlijk starten op april niveau, niet op het gemiddelde.

### Ad Variant Performance

Er is geen delivery in het rapportvenster, dus alle waarden voor 30 juli zijn nul.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.v.t. | n.v.t. | n.v.t. | niet gemeten |
| h12_b3_cta5 | 0 | n.v.t. | n.v.t. | n.v.t. | niet gemeten |
| h13_b3_cta5 | 0 | n.v.t. | n.v.t. | n.v.t. | niet gemeten |
| h14_b3_cta5 | 0 | n.v.t. | n.v.t. | n.v.t. | niet gemeten |
| h15_b3_cta5 | 0 | n.v.t. | n.v.t. | n.v.t. | niet gemeten |

**Beste variant:** n.v.t., geen delivery.
**Slechtste variant:** n.v.t., geen delivery.

**Ad variant performance april 2026, ter voorbereiding op de herstart:**

| Ad | Ad set | Impressions | Clicks | CTR | CPC | Spend |
|----|--------|-------------|--------|-----|-----|-------|
| H12,B3,CTA5 | BATCH 2 | 1.058 | 50 | 4,73% | €0,29 | €14,37 |
| H15,B3,CTA5 | BATCH 2 | 157 | 10 | 6,37% | €0,23 | €2,32 |
| H12,B3,CTA5 | Kopie 2 | 13.955 | 356 | 2,55% | €0,40 | €141,43 |
| H15,B3,CTA5 | Kopie 4 | 4.737 | 107 | 2,26% | €0,47 | €49,83 |
| H11, B3, CTA5 | Kopie 1 | 38.614 | 784 | 2,03% | €0,67 | €521,56 |
| H13,B3,CTA5 | Kopie 3 | 16.766 | 331 | 1,97% | €0,63 | €206,99 |
| H14,B3,CTA5 | BATCH 2 | 16.551 | 297 | 1,79% | €0,41 | €122,96 |
| H13,B3,CTA5 | BATCH 2 | 1 | 0 | n.v.t. | n.v.t. | €0,01 |

Twee dingen springen eruit. H11 in Kopie 1 slokte 49% van het aprilbudget op (€521,56) tegen de op een na slechtste CPC van het hele veld (€0,67). H12 was in beide ad sets de sterkste presteerder op CPC. De twee bovenste rijen hebben te weinig volume om conclusies aan te verbinden.

De campagne bevat 25 ads, allemaal PAUSED, verdeeld over vier ad sets (BATCH 2: Expertise & POC plus drie kopieën). In april leverden slechts 8 daarvan delivery. De overige 17 hebben nooit gedraaid.

### Tweede campagne

`2026: SYBB - Kopie` (ID `120243293329420239`), status PAUSED, aangemaakt 19 april 2026. Deze heeft wél gedraaid, uitsluitend tussen 19 en 30 april 2026:

| Metric | 19 t/m 30 april |
|--------|-----------------|
| Spend | €124,42 |
| Impressions | 7.615 |
| Clicks | 195 |
| CTR | 2,56% |
| CPC | €0,64 |
| Frequency | 1,42 |
| Landing page views | 100 |
| Initiate checkout | 6 |
| Purchases | 0 |

CPC €0,64 en nul purchases uit 100 landing page views. Deze test heeft de hoofdcampagne niet verbeterd.

## 3. Landing Page Health

Host `www.startyourballoonbusiness.com`. Gisteren 0 pageviews en 0 sessies, dus er zijn geen sessie metrics te berekenen voor 30 juli. De kolom "7d" hieronder dekt 24 t/m 30 juli.

| Metric | Gisteren (30 jul) | 7d (24 t/m 30 jul) | Target | Status |
|--------|-------------------|--------------------|--------|--------|
| Pageviews | 0 | 2 | n.v.t. | 🔴 |
| Sessies | 0 | 2 | n.v.t. | 🔴 |
| Bounce Rate | n.v.t. | 100% (2/2) | <55% | 🔴 |
| Avg Session Duration | n.v.t. | 4,5s | >90s | 🔴 |
| Scroll 25% | niet gemeten | niet gemeten | >80% | ⚪ |
| Scroll 50% | niet gemeten | niet gemeten | >60% | ⚪ |
| Scroll 75% | niet gemeten | niet gemeten | >40% | ⚪ |
| Scroll 100% | niet gemeten | niet gemeten | >20% | ⚪ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚪ |

⚪ betekent: het event bestaat niet in PostHog, de KPI is dus niet berekenbaar. Zie sectie 5.

**Weekvergelijking, de trend is scherper dan de dagcijfers:**

| Venster | Pageviews | Sessies | Single page | Bounce | Avg duur |
|---------|-----------|---------|-------------|--------|----------|
| 10 t/m 16 juli | 18 | 18 | 17 | 94,4% | 30,3s |
| 17 t/m 23 juli | 14 | 14 | 14 | 100% | 9,0s |
| 24 t/m 30 juli | 2 | 2 | 2 | 100% | 4,5s |

**Dagpatroon laatste twee weken:**

| Dag | Pageviews | Sessies | Avg duur |
|-----|-----------|---------|----------|
| 17 jul | 1 | 1 | 10,0s |
| 18 jul | 3 | 3 | 20,0s |
| 19 jul | 2 | 2 | 13,0s |
| 20 jul | 6 | 6 | 3,5s |
| 21 jul | 1 | 1 | 9,0s |
| 22 jul | 0 | 0 | n.v.t. |
| 23 jul | 1 | 1 | 0,0s |
| 24 jul | 0 | 0 | n.v.t. |
| 25 jul | 0 | 0 | n.v.t. |
| 26 jul | 0 | 0 | n.v.t. |
| 27 jul | 1 | 1 | 0,0s |
| 28 jul | 0 | 0 | n.v.t. |
| 29 jul | 1 | 1 | 9,0s |
| **30 jul** | **0** | **0** | **n.v.t.** |

Maandtotaal juli (1 t/m 30 juli): 50 pageviews, 46 sessies, waarvan 44 single page. Bounce rate 95,7% over de hele maand, gemiddelde sessieduur ruim onder de 30 seconden op vrijwel elke dag.

**Verkeersbronnen juli (50 pageviews):**

| Bron | Pad | utm_source | utm_campaign | utm_content | Views |
|------|-----|-----------|--------------|-------------|-------|
| direct | `/` | geen | geen | geen | 40 |
| t-sml.mtrbio.com | `/` | instagram | sybb | bio_link | 3 |
| t-sml.mtrbio.com | `/` | facebook | sybb | bio_link | 2 |
| t-sml.mtrbio.com | `/checkout` | facebook | sybb | bio_link | 2 |
| interne link | `/checkout` | geen | geen | geen | 1 |
| direct | `/` | META | SYBB | H14,B3,CTA5 | 1 |
| direct | `/checkout` | META | SYBB | H14,B3,CTA5 | 1 |

80% van het verkeer is direct en ongetagd. De enige gestructureerde bron is de Metricool bio link vanuit Instagram en Facebook, goed voor 7 pageviews. Opvallend: er kwamen in juli nog 2 pageviews binnen met de UTM tag van ad H14,B3,CTA5, terwijl die campagne sinds april niet meer draait. Dat is restverkeer van een bewaarde of gedeelde advertentielink, geen delivery.

**Session recordings:** 0 sessies gisteren, dus geen nieuwe recordings. Over heel juli zijn er op deze host geen `$rageclick` en geen `$dead_click` events geregistreerd.

## 4. Funnel Drop-off

De funnel uit de skill is niet volledig meetbaar. Stap 2 en stap 3 bestaan niet in de data, en de laatste stap heet `/checkout`, niet `/booking`.

```
Pageview        →  Scroll 50%      →  CTA Click       →  /checkout
```

**Venster 24 t/m 30 juli:**

```
Pageview (2)    →  niet gemeten    →  niet gemeten    →  /checkout (0)
   100%                  ?                  ?                 0%
```

**Heel juli, voor een bruikbaarder beeld:**

```
Pageview `/` (46)  →  niet gemeten  →  niet gemeten  →  /checkout (4)
      100%                 ?                ?               8,7%
```

**Grootste lek:** bovenaan, niet onderaan. Met 2 bezoekers in zeven dagen is er geen funnel om te lekken. Het echte knelpunt is dat er geen instroom is. Zodra de instroom terugkomt is het tweede knelpunt dat het middenstuk van de funnel blind is: zonder scroll en CTA events kan niet vastgesteld worden of bezoekers afhaken op de hero, halverwege de pagina, of bij de CTA zelf.

## 5. Rode Vlaggen 🚩

1. **Campagne al ruim drie maanden zonder delivery.** Laatste spend eind april 2026, laatste campagnewijziging 19 april. Dagbudget van €100 staat klaar maar wordt niet gebruikt. Dit is de dominante rode vlag, alle andere zijn er een gevolg van.

2. **Scroll depth wordt niet gemeten.** Op host `www.startyourballoonbusiness.com` bestaan in juli enkel de events `$pageview` (50), `$web_vitals` (38), `$autocapture` (17) en `$pageleave` (3). Er is geen enkel scroll event. De KPI targets voor scroll 25/50/75/100% uit de skill kunnen structureel niet gerapporteerd worden.

3. **CTA clicks worden niet gemeten.** Er is geen CTA click event. De 17 `$autocapture` events in juli komen van slechts 2 personen, wat op intern verkeer wijst. CTA click rate is daarmee niet berekenbaar en de bijbehorende target van >4% is dood.

4. **`$pageleave` vuurt vrijwel niet.** 3 events van 2 personen in een maand met 46 sessies. Sessieduur en bounce rate zijn daardoor berekend uit event timestamps, niet uit een betrouwbaar exit signaal. Behandel die twee cijfers als indicatief.

5. **Bounce rate 100% in het 7d venster, 95,7% over heel juli.** Ruim boven de drempel van 70%. De steekproef is klein, maar het patroon is consistent over vier weken.

6. **UTM tagging wijkt af van de conventie.** In PostHog staat `utm_source=META`, `utm_campaign=SYBB`, `utm_content=H14,B3,CTA5`. De conventie schrijft lowercase voor met underscores: `utm_source=meta`, `utm_campaign=sybb`, `utm_content=h14_b3_cta5`. De komma's breken bovendien de match op `utm_content` in de Meta Ads Tracker. De ad namen in Meta zelf zijn ook inconsistent: "H11, B3, CTA5" met spaties naast "H12,B3,CTA5" zonder.

7. **Landing page pad wijkt af van de skill.** De skill verwacht `/booking` als conversiestap, de site gebruikt `/checkout`. Een van de twee moet bijgewerkt worden, anders blijft de funnelmeting scheef.

## 6. Top 3 Acties voor Vandaag

### 1. Beslis: SYBB heractiveren of formeel stopzetten

- **Wat:** neem vandaag een expliciet besluit over de SYBB campagne. Ofwel een herstartdatum met budget vastleggen, ofwel de campagne archiveren en het dagelijkse rapport pauzeren.
- **Waarom:** ruim drie maanden nul delivery, terwijl er dagelijks een rapport draait over een funnel die niet bestaat. Het rapport kost aandacht en levert nu geen beslisinformatie op.
- **Hoe:** Meta Ads Manager, campagne `120239435987290239`. Bij archiveren ook `2026: SYBB - Kopie` (`120243293329420239`) meenemen.
- **Verwachte impact:** einde aan de ruis. Bij herstart komt er weer stuurbare data.
- **Escalatie:** 🔴 Rood, strategie, dit is jouw besluit.

### 2. Repareer de landing page tracking vóór een eventuele herstart

- **Wat:** voeg scroll depth events (25/50/75/100%) en een CTA click event toe aan `www.startyourballoonbusiness.com`, en controleer waarom `$pageleave` niet vuurt.
- **Waarom:** vier van de zeven KPI rijen in dit rapport zijn nu niet invulbaar. Zet je de campagne aan zonder dit te fixen, dan betaal je voor verkeer dat je vervolgens niet kunt analyseren. In april is precies dat gebeurd: 818 landing page views zonder enig inzicht in waar mensen afhaakten.
- **Hoe:** PostHog snippet op de landing page uitbreiden. Dit moet vóór stap 1 af zijn als je voor herstart kiest, niet erna.
- **Verwachte impact:** de funnel uit sectie 4 wordt voor het eerst volledig meetbaar, en de secties "grootste lek" en "beste variant" worden echt bruikbaar.
- **Escalatie:** 🟠 Oranje, vereist aanpassing in de site editor.

### 3. Corrigeer de UTM tagging en ad naamgeving

- **Wat:** breng alle ad URLs in beide SYBB campagnes in lijn met de conventie: lowercase, underscores, dus `utm_source=meta&utm_medium=cpc&utm_campaign=sybb&utm_content=h14_b3_cta5&utm_term=batch_2`. Hernoem de ads naar hetzelfde patroon zodat namen en tags matchen.
- **Waarom:** de huidige tags (`META`, `SYBB`, `H14,B3,CTA5`) breken de match op `utm_content` in de Meta Ads Tracker, waardoor Meta data en PostHog data niet gekoppeld kunnen worden. Precies die koppeling is de reden dat dit rapport bestaat.
- **Hoe:** Meta Ads Manager, URL parameters per ad, of via `update_ad_url_tags` op campagneniveau. Nu doen is goedkoop omdat de campagne toch stilstaat.
- **Verwachte impact:** de kolommen "LP Bounce" en "LP Scroll 50%+" in de ad variant tabel worden na herstart daadwerkelijk vulbaar.
- **Escalatie:** 🟡 Geel, jouw goedkeuring volstaat.

---

*Gegenereerd op 31 juli 2026. Databronnen: Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google diensten geraadpleegd, geen schrijfacties naar externe systemen.*
