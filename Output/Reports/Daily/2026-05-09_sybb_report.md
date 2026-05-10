# SYBB Daily Report — 9 May 2026

## 1. Samenvatting

Campagne `2026: SYBB` staat al ~20 dagen op PAUSED (sinds 19/20 april). Gisteren weer geen Meta Ads activiteit (€0 spend, 0 impressies, 0 clicks). Landing page kreeg 2 pageviews uit organisch verkeer, identiek aan 8 mei. Dit is de tweede dag op rij dat het rapport feitelijk een stilstand-rapport is, en de pijplijn drijft volledig op bio link traffic. Beslissing relaunchen of definitief stoppen wordt deze week kritiek.

## 2. Meta Ads Performance

| Metric | Gisteren (9 mei) | 7d Gemiddelde (2-8 mei) | Trend |
|--------|------------------|-------------------------|-------|
| Spend | €0,00 | €0,00 | → (paused) |
| Impressions | 0 | 0 | → (paused) |
| Clicks | 0 | 0 | → (paused) |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

**Context (laatste actieve venster, 15-19 april 2026):**

| Metric | Waarde | Target | Status |
|--------|--------|--------|--------|
| Spend totaal | €357,70 | n/a | informatief |
| Impressions | 25.576 | n/a | informatief |
| Clicks | 579 | n/a | informatief |
| CTR | 2,26% | n/a | 🟢 boven 1% |
| CPC | €0,62 | <€0,50 | 🔴 24% boven target |
| Frequency | 1,37 | <3,0 | 🟢 |
| Landing page views | 273 | n/a | informatief |
| Initiate checkout | 18 | n/a | informatief |
| Purchases | 4 | n/a | informatief |

### Ad Variant Performance

Niet van toepassing voor 9 mei (campagne paused, 0 ads serveerden).

In de laatste 8 dagen (2-9 mei) is alleen `meta cpc / sybb / h13_b3_cta5` (2 pageviews) nog terug te vinden in PostHog UTM data, vermoedelijk uit gecachte links of late-arriving sessies, niet uit live ad delivery.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (9 mei) | 7d Gemiddelde (2-8 mei) | Target | Status |
|--------|------------------|-------------------------|--------|--------|
| Pageviews | 2 | 3,3/dag | n/a | informatief |
| Unique visitors | 2 | ~2,9/dag | n/a | informatief |
| Sessions | 2 | 2,6/dag | n/a | informatief |
| Bounce Rate | n/m | hoog | <55% | 🔴 maar volume te laag voor signaal |
| Avg Session Duration | n/m | n/m (sparse) | >90s | n/m |
| Scroll 25%+ | n/m | n/m | >80% | n/m |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| CTA Click Rate | n/m | n/m | >4% | n/m |

**Belangrijk:** met 2 pageviews op 9 mei en 23 pageviews over 2-8 mei is alle ratio-data statistisch betekenisloos. De landing page wordt feitelijk niet bezocht. Cijfers staan op rood, maar dat is een data-volume probleem, geen page-prestatie probleem.

### Pageviews per dag (2-9 mei)

| Datum | Pageviews | Sessions |
|-------|-----------|----------|
| 2 mei | 4 | 4 |
| 3 mei | 2 | 1 |
| 4 mei | 2 | 2 |
| 5 mei | 8 | 6 |
| 6 mei | 4 | 2 |
| 7 mei | 1 | 1 |
| 8 mei | 2 | 2 |
| **9 mei** | **2** | **2** |
| **Totaal 8d** | **25** | **20** |

### Trafficbron breakdown (2-9 mei)

| Bron | Pageviews | Aandeel |
|------|-----------|---------|
| instagram organic / bio_link | 9 | 36% |
| direct / no UTM | 8 | 32% |
| facebook organic / bio_link | 6 | 24% |
| meta cpc / sybb / h13_b3_cta5 | 2 | 8% |
| **Totaal** | **25** | 100% |

Vrijwel alle traffic komt uit Instagram en Facebook bio links plus direct verkeer, niet uit ads.

### Pagina breakdown (2-9 mei)

| Pad | Pageviews |
|-----|-----------|
| `/` (landing page) | 21 |
| `/checkout` | 3 |
| `/review` | 1 |

Klein lichtpuntje: er zijn 3 `/checkout` pageviews in deze periode, wat aangeeft dat een fractie van het organische bio-link verkeer wel doorklikt. Op de actieve campagne periode telde dit als de funnel-stap "initiate checkout".

## 4. Funnel Drop-off

Niet betrouwbaar berekenbaar op 9 mei. Ruwe volume per stap (2-9 mei totaal):

```
Pageview /         21
Pageview /checkout  3   (≈14% van LP-bezoekers)
Pageview /review    1
```

`/booking` pageviews in dit venster: 0 (niet aanwezig in data, vermoedelijk worden conversies via `/checkout` en `/review` afgehandeld).

**Grootste lek:** geen ad delivery dus geen instroom om een lek over te detecteren. Het enige meetbare signaal is dat van 21 LP-views slechts 3 doorklikten naar `/checkout` (~14%); die ratio is met 21 sessies te dun om er beleid op te baseren.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat al ~20 dagen op PAUSED** (sinds 19/20 april). Geen ad spend, geen attribuable conversies. Iedere dag pauze = ~€33-50 minder pijplijn op basis van het april venster.
- 🚩 **Geen herstel in organisch volume**: pageviews zitten op 1-8/dag (peak 5 mei), geen opbouw zichtbaar. Bio link traffic compenseert het ad-gat niet.
- 🚩 **CPC tijdens laatste actieve venster (€0,62) lag 24% boven target (€0,50)**: zonder creative refresh blijft dit punt onverbeterd bij relaunch.
- 🚩 **Zero `/booking` events**: workshop-funnel is volledig stil; checkout-views (3 in 8 dagen) zijn de enige conversiesignalen.
- 🚩 **Tweede achtereenvolgende dag met identiek volume (2 pv, 2 sessies)**: lijkt op vloer-niveau organisch baseline; verdere daling betekent dat zelfs bio links uitdrogen.

## 6. Top 3 Acties voor Vandaag

1. **Beslissing forceren: SYBB campagne deze week relaunchen of definitief pauzeren in jaarplan.**
   - **Waarom:** 20 dagen paused zonder herstart blokkeert alle workshop-pijplijn data en KPI tracking. Dit is nu de tweede SYBB rapport-dag op rij met identieke "geen activiteit" output. Zonder beslissing blijven rapporten leeg.
   - **Hoe:** Robin agendeert blokje deze week (uiterlijk 12 mei). Bij relaunch: nieuwe creatives gereed (anders blijft CPC €0,62), nieuw budget set, plan voor minimaal 14 dagen continu draaien. Bij stop: SYBB uit dagelijkse morning report flow halen tot nieuw besluit.
   - **Verwachte impact:** zonder ads blijft funnel rapport leeg. Met relaunch + creative refresh: terug naar ~100 pageviews/dag basislijn binnen week 1.
   - **Escalatie:** 🟠 Robin (strategie + budget).

2. **Voor relaunch: bouw 2-3 nieuwe ad varianten op basis van de winnende hooks uit het 9 april - 8 mei venster (batch_4).**
   - **Waarom:** CPC was €0,56-0,62 en frequency raakte 2,32 op 30d in laatste actieve periode. Bij hervatten met dezelfde creatives loopt frequency snel naar 3+ (ad fatigue). Creative refresh nu inplannen voorkomt dat.
   - **Hoe:** check welke `utm_content` (h11/h12/h13/h14/h15_b3_cta5) het laagste CPC en hoogste landing_page_view ratio had in maart-april en bouw daar varianten op. Lever batch_4 aan met nieuwe hooks gebaseerd op SYBB 8 pillars (Bronnen/Sempertex Europe/sybb-8-pillars.md).
   - **Verwachte impact:** CPC terug richting <€0,50, frequency onder 2,0 in eerste 14 dagen.
   - **Escalatie:** 🟡 Robin goedkeuring voor briefing en oplevering.

3. **Quick win: zet 1-2 SYBB-gerichte Reels of carousels live deze week om bio link traffic te boosten zolang ads paused zijn.**
   - **Waarom:** Instagram bio_link levert 36% van het schamele organische volume, Facebook bio_link nog 24%. Samen 60% van de pijplijn. Eén of twee gerichte posts per week kunnen pageviews verdubbelen zonder ad spend, en houden de checkout-funnel actief tot relaunch.
   - **Hoe:** plan deze week 2 SYBB-gerichte Reels/posts met expliciete CTA naar bio link, gebruik bestaande hooks die nog niet als ad zijn ingezet. Stem af op funnel-stap "awareness" → "consideration" voor starters.
   - **Verwachte impact:** organische pageviews van ~3/dag naar ~10-15/dag, kleine maar continue funnel-instroom tot relaunch, behoud van pixel-warmte.
   - **Escalatie:** 🟢 auto, content team kan dit zelfstandig oppakken.

---

**Data sources:** Meta Ads MCP (Pipeboard), account `act_567892422940728`, campaign `120239435987290239`. PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets / Drive / Gmail / Calendar / Docs / Slides aangeroepen voor dit rapport.**
