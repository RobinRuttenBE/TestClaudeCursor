# SYBB Daily Report — 8 May 2026

## 1. Samenvatting

Campagne `2026: SYBB` staat sinds ~19 april op PAUSED. Gisteren dus geen Meta Ads activiteit (€0 spend, 0 impressies, 0 clicks). De landing page kreeg 2 pageviews uit residueel organisch verkeer. Er valt op deze datum geen funnel performance te beoordelen, dit is feitelijk een "stilstand-rapport". De enige beslissing die telt: relaunchen of definitief afbouwen.

## 2. Meta Ads Performance

| Metric | Gisteren (8 mei) | 7d Gemiddelde (1-7 mei) | Trend |
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

**30d aggregaat (9 april - 8 mei, ter referentie):** €996,81 spend, 1.782 clicks, CTR 2,19%, CPC €0,56, frequency 2,32, 6 purchases (€442,47 attributed value op pixel basis).

### Ad Variant Performance

Niet van toepassing voor 8 mei (campagne paused, 0 ads serveerden).

In de laatste 7 dagen werd alleen `meta cpc / sybb / h13_b3_cta5` (2 pageviews) nog gezien in PostHog UTM data, vermoedelijk uit gecachte links of late-arriving sessies, niet uit live ad delivery.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (8 mei) | 7d Gemiddelde | Target | Status |
|--------|------------------|---------------|--------|--------|
| Pageviews | 2 | 3,1/dag | n/a | informatief |
| Unique visitors | 2 | 2,7/dag | n/a | informatief |
| Sessions | 2 | 2,9/dag | n/a | informatief |
| Bounce Rate | n/m | ~95%+ (24 pv ≈ 22 sessies) | <55% | 🔴 maar volume te laag voor signaal |
| Avg Session Duration | n/m | n/m (sparse data) | >90s | 🔴 / n/m |
| Scroll 25%+ | n/m | n/m | >80% | n/m |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| CTA Click Rate | n/m | n/m (8 autocaptures op 24 pv) | >4% | n/m |

**Belangrijk:** met 2 pageviews op 8 mei en 22 pageviews over 7 dagen is alle ratio-data statistisch betekenisloos. De landing page wordt feitelijk niet bezocht. Cijfers staan op rood, maar dat is een data-volume probleem, geen page-prestatie probleem.

### Trafficbron breakdown (1-8 mei)

| Bron | Pageviews | Aandeel |
|------|-----------|---------|
| instagram organic / bio_link | 10 | 42% |
| facebook organic / bio_link | 6 | 25% |
| direct / no UTM | 6 | 25% |
| meta cpc / sybb / h13_b3_cta5 | 2 | 8% |
| **Totaal** | **24** | 100% |

Vrijwel alle trafiek komt nu uit de Instagram en Facebook bio links, niet uit ads.

## 4. Funnel Drop-off

Niet berekenbaar op 8 mei. Volume per stap (1-8 mei totaal):

```
Pageview         24
$pageleave       10
$autocapture      8   (proxy voor click events op de pagina)
$web_vitals      25
```

`/booking` pageviews in dit venster: 0 (geen vermelding in pageview data).

**Grootste lek:** geen ad delivery, dus geen instroom om een lek over te detecteren.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat al ~19 dagen op PAUSED** (sinds 19/20 april). Geen ad spend, geen attribuable conversies.
- 🚩 **Geen organische pijplijn ter compensatie**: organische pageviews vielen van ~110/dag (active period) naar ~3/dag direct na de pauze. Bio link traffic dekt dit gat niet.
- 🚩 **CPC tijdens laatste actieve venster (€0,62) lag 24% boven target (€0,50)**: bij relaunch zonder optimalisatie blijft dit punt onverbeterd.
- 🚩 **Geen `/booking` events in de laatste 7 dagen**: workshop-funnel is volledig stil.

## 6. Top 3 Acties voor Vandaag

1. **Beslissing: SYBB campagne relaunchen of definitief uit budget halen.**
   - **Waarom:** 19 dagen paused zonder herstart blokkeert alle workshop-pijplijn data en KPI tracking. Het rapport heeft alleen waarde als er traffic is om te meten.
   - **Hoe:** Robin beslist deze week. Als relaunch: nieuwe creatives klaar (anders blijft CPC €0,62), nieuw budget set, plan voor minimaal 14 dagen continu draaien.
   - **Verwachte impact:** zonder ads blijft het funnel rapport leeg. Met relaunch + creative refresh: terug naar ~100 pageviews/dag basislijn.
   - **Escalatie:** 🟠 Robin (strategie + budget).

2. **Voor relaunch: bouw 2-3 nieuwe ad varianten op basis van de winnende hooks uit het 9 april - 8 mei venster.**
   - **Waarom:** CPC was €0,56-0,62 en frequency raakte 2,32 op 30d. Bij hervatten met dezelfde creatives loopt frequency snel naar 3+ (ad fatigue). Creative refresh nu inplannen voorkomt dat probleem.
   - **Hoe:** check welke `utm_content` (h11/h12/h13/h14/h15_b3_cta5) het laagste CPC en hoogste landing_page_view ratio had in maart-april en bouw daar varianten op. Lever batch_3 of batch_4 aan.
   - **Verwachte impact:** CPC terug richting <€0,50, frequency onder 2,0 in eerste 14 dagen.
   - **Escalatie:** 🟡 Robin goedkeuring voor briefing en oplevering.

3. **Snel-fix: zet bio link Instagram en Facebook posts aan om de organische pageview-flow gaande te houden tijdens pauze.**
   - **Waarom:** instagram bio_link levert nu 42% van het schamele organische volume. Eén of twee gerichte posts per week kunnen dit verdubbelen zonder ad spend.
   - **Hoe:** plan deze week 2 SYBB-gerichte Reels/posts met bio link CTA, gebruik bestaande hooks die nog niet als ad zijn ingezet.
   - **Verwachte impact:** organische pageviews van ~3/dag naar ~10-15/dag, kleine maar continue funnel-instroom tot relaunch.
   - **Escalatie:** 🟢 auto, content team kan dit zelfstandig oppakken.

---

**Data sources:** Meta Ads MCP (Pipeboard), account `act_567892422940728`, campaign `120239435987290239`. PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets / Drive / Gmail / Calendar / Docs / Slides aangeroepen voor dit rapport.**
