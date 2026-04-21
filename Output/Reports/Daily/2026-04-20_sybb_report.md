# SYBB Daily Report, 2026-04-20

## 1. Samenvatting
De hoofdcampagne "2026: SYBB" stond gisteren op pauze. "2026: SYBB Kopie" nam het stokje over met €77.85 spend, 119 clicks en een CTR van 2.78% (beter dan het 7d gemiddelde). Maar de landing page performance is zorgelijk: 89% bounce rate, slechts 2 CTA clicks, 0 purchases. Plus: scroll depth en session duration tracking leveren nul data, waardoor de LP health-metrics niet gemeten kunnen worden.

## 2. Meta Ads Performance

**Belangrijke context:** de oorspronkelijke campagne `2026: SYBB` (ID 120239435987290239) is sinds 19 april gepauzeerd. Een kopie `2026: SYBB Kopie` (ID 120243293329420239) draaide gisteren als vervanger met dezelfde ads (H11, H12, H13 / B3 / CTA5). Cijfers hieronder = Kopie voor "Gisteren", origineel voor 7d gemiddelde (14 apr t/m 19 apr actief, 20 apr 0).

| Metric | Gisteren (Kopie) | 7d Gemiddelde (origineel) | Trend |
|--------|------------------|---------------------------|-------|
| Spend | €77.85 | €64.81 /dag | ↑ +20% |
| Impressions | 4.287 | 4.696 /dag | → -9% |
| Clicks | 119 | 105 /dag | ↑ +13% |
| CTR | 2.78% | 2.23% | ↑ +25% |
| CPC | €0.65 | €0.62 | → +5% |
| Frequency | 1.34 | 1.41 | → -5% |
| Link clicks | 75 | 68 /dag | ↑ |
| Landing page views | 63 | 56 /dag | ↑ |
| Initiate Checkout | 2 (€700) | 3 /dag (€1.217) | ↓ |
| Purchases | 0 | 1.3 /dag (€245) | ↓ |

### Ad Variant Performance (Kopie, 2026-04-20)

| Ad (utm_content) | Clicks | CTR | CPC | Link Clicks | LPV (Meta) | PH Sessions | Checkouts |
|-------------------|--------|-----|-----|-------------|------------|-------------|-----------|
| h11_b3_cta5 | 55 | 2.79% | €0.51 | 33 | 22 | 22 | 1 |
| h12_b3_cta5 | 33 | 4.14% | €0.55 | 17 | 17 | 14 | 1 |
| h13_b3_cta5 | 31 | 2.04% | €1.02 | 25 | 24 | 31 | 0 |

**Beste variant:** H12 heeft de hoogste CTR (4.14%) en converteerde naar 1 initiate checkout tegen €0.55 CPC. H11 heeft de laagste CPC (€0.51) en ook 1 checkout.

**Slechtste variant:** H13. CPC van €1.02 is 2x boven target, CTR het laagst (2.04%), 0 checkouts. Ondanks 31 PH sessies geen conversie. Ad-pagina mismatch of verkeerde audience.

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 88 | 114 /dag | meten | 🟡 |
| Unique Visitors | 72 | 88 /dag | meten | 🟡 |
| Sessions | 75 | 96 /dag | meten | 🟡 |
| Bounce Rate | 89.3% (67/75) | 81.8% (551/674) | <55% | 🔴 |
| Avg Session Duration | geen data | geen data | >90s | 🔴 tracking |
| Scroll 25% | geen data | geen data | >80% | 🔴 tracking |
| Scroll 50% | geen data | geen data | >60% | 🔴 tracking |
| Scroll 75% | geen data | geen data | >40% | 🔴 tracking |
| Scroll 100% | geen data | geen data | >20% | 🔴 tracking |
| CTA Click Rate ("Book Your Spot") | 2.8% (2/71) | meten | >4% | 🟡 |

**Data quality probleem:** de PostHog properties `$session_duration` en `$prev_pageview_max_scroll_percentage` zijn leeg voor alle sessies op startyourballoonbusiness.com. Dit moet gerepareerd worden voordat LP optimalisatie-beslissingen zinnig zijn.

### UTM Content breakdown (PostHog, 2026-04-20)
| utm_content | Sessions | Pageviews |
|-------------|----------|-----------|
| h13_b3_cta5 | 31 | 31 |
| h11_b3_cta5 | 22 | 31 |
| h12_b3_cta5 | 14 | 14 |
| bio_link | 3 | 4 |

### Path breakdown
| Path | Pageviews | Sessions |
|------|-----------|----------|
| / | 78 | 71 |
| /checkout | 8 | 5 |
| /booking | 2 | 2 |

### Klik-events (autocapture)
- 23x generieke click op /
- 2x "Book Your Spot" op /
- 1x productprijs "€423.50" op /checkout
- 1x directe URL-klik
- 1x "Spain" country-selector op /checkout
- 2x FAQ clicks ("From what time", "Where does it take place")

## 4. Funnel Drop-off (2026-04-20)

```
Landing /             71 sessions   (100%)
    ↓ -97% drop-off
Book Your Spot klik    2 clicks      (2.8%)
    ↓
/checkout              5 sessions    (7.0% van landing)
    ↓ -60% drop-off
/booking               2 sessions    (2.8% van landing)
```

Opmerking: /checkout toont meer sessies (5) dan geregistreerde Book Your Spot klikken (2). Mogelijk bereikt een deel /checkout via een andere route (directe link, retargeting). De echte bottleneck zit tussen landing en CTA klik.

**Grootste lek:** van 71 landing sessies klikt slechts 2.8% op "Book Your Spot". De hoofdpagina faalt in CTA conversie. Mogelijke oorzaken: hero/eerste sectie trekt geen aandacht, CTA-knop te laag/niet zichtbaar, ad promises matchen niet met pagina-belofte.

## 5. Rode Vlaggen

- **Bounce rate 89.3%** >> drempel 70%. Grote ad/pagina mismatch of verkeerde audience targeting.
- **CPC €0.65** > target €0.50, alle drie ads boven target.
- **H13 CPC €1.02** is een outlier, 2x target, 0 checkouts bij 31 PH sessies.
- **Scroll depth + session duration tracking broken** op startyourballoonbusiness.com. Alle sessies geven null. Nul signaal over pagina-engagement.
- **Hoofdcampagne sinds 19 apr gepauzeerd**, Kopie draait als schaduwcampagne zonder leverbare historie. Learning fase reset.
- **0 purchases** bij €77.85 spend, 2 initiate checkouts zonder follow-through.

## 6. Top 3 Acties voor Vandaag

1. **Fix PostHog tracking config voor scroll depth en session duration**
   - Waarom: zonder deze data kunnen we geen zinnige LP optimalisatie doen. 0% van sessies rapporteert scroll of duur.
   - Hoe: check de PostHog Web snippet config op de Wix site. Verify dat `capture_pageleave` aanstaat en dat session recording properties doorkomen. Mogelijk Wix-plugin issue.
   - Verwachte impact: onmiddellijk signaal over waar bezoekers afhaken op de landing page, unlocks de rest van de optimalisatie.
   - Escalatie level: **Geel** (Robin goedkeuring, mogelijk Wix Editor actie).

2. **Pauzeer H13, herverdeel budget naar H11 + H12**
   - Waarom: H13 CPC €1.02 (2x target), CTR 2.04% (laagste), 0 checkouts bij 31 PH sessies. H12 heeft CTR 4.14% en 1 checkout. H11 heeft CPC €0.51 en 1 checkout.
   - Hoe: in Meta Ads Manager pauseer ad "H13,B3,CTA5" in "BATCH 2: Expertise & POC Kopie 3". Verhoog adset budgets voor Kopie 1 (H11) en Kopie 2 (H12) met gelijke delen.
   - Verwachte impact: gemiddelde CPC zakt van €0.65 naar richting €0.53, meer checkouts per euro.
   - Escalatie level: **Groen** (auto-uitvoerbaar na Robin fiat).

3. **Onderzoek de 89% bounce rate met session recordings**
   - Waarom: landing page verliest 89% meteen. H13 heeft disproportioneel veel sessies (31) maar 0 checkouts, duidt op ad-pagina mismatch.
   - Hoe: open PostHog en bekijk 5 session recordings van sessies met `utm_content = h13_b3_cta5` van 2026-04-20. Let op: waar scrollen ze? Wat klikken ze? Hoe lang blijven ze? Noteer patronen.
   - Verwachte impact: concrete hypothese voor hero-aanpassing of ad-creative aanpassing, basis voor A/B test.
   - Escalatie level: **Geel** (Robin kijkt mee, strategische input nodig).

---

**Data bronnen:** Meta Ads MCP (Pipeboard), PostHog MCP project "Default project" (id 149694). Host filter: `startyourballoonbusiness.com`. Tijdzone: UTC.
**Rapport gegenereerd:** 2026-04-21
