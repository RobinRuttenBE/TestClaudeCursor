# SYBB Daily Report -- 14 april 2026

## 1. Samenvatting

Matige dag voor SYBB. De CPC is met €0.62 flink boven target (€0.50) en de bounce rate op de landing page is gestegen naar 60%, boven de 55% target. Impressies en clicks zijn ~20% lager dan het 7-daags gemiddelde, wat wijst op dalende delivery. Lichtpuntje: H12 presteert uitstekend met de hoogste CTR (3.02%), laagste CPC (€0.49) en laagste bounce rate (40%), maar krijgt slechts 9% van het budget. Scroll depth is zorgwekkend: meer dan de helft van de bezoekers scrollt niet voorbij 25% van de pagina.

---

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €95.93 | €100.25 | → |
| Impressions | 7,290 | 9,466 | ↓ |
| Clicks (all) | 154 | 194 | ↓ |
| Link Clicks | 83 | 102 | ↓ |
| CTR | 2.11% | 2.05% | → |
| CPC | €0.62 | €0.52 | ↑ |
| Landing Page Views | 63 | 78 | ↓ |
| Frequency | 1.53 | 1.92 | → |
| Video Views | 1,567 | 1,865 | ↓ |
| Add to Cart | 2 | 3.7 | ↓ |
| View Content | 7 | 7.0 | → |

**Opvallend:** CPC stijgt (+19% vs 7d gem.), impressies dalen (-23%). Mogelijk begin van ad fatigue of algoritme-shift. Budget wordt niet volledig uitgeput (€95.93 van €100 daily budget).

### Ad Variant Performance

| Ad (utm_content) | Spend | Impressions | Link Clicks | CTR | CPC | LP Views | LP Bounce | Avg Sessie |
|-------------------|-------|-------------|-------------|-----|-----|----------|-----------|------------|
| h11_b3_cta5 | €63.51 | 4,902 | 55 | 2.04% | €0.64 | 40 | 61.5% | 83s |
| h13_b3_cta5 | €23.57 | 1,791 | 19 | 2.01% | €0.65 | 14 | 70.4% | 288s |
| h12_b3_cta5 | €8.85 | 597 | 9 | 3.02% | €0.49 | 9 | 40.0% | 63s |

**Beste variant:** H12 (h12_b3_cta5). Hoogste CTR (3.02%), enige variant onder CPC target (€0.49), en veruit de laagste bounce rate (40%). Dit is de best converterende ad, maar krijgt slechts 9.2% van het dagbudget.

**Slechtste variant:** H13 (h13_b3_cta5). Bounce rate van 70.4% is een rode vlag. Bezoekers klikken maar verlaten de pagina meteen. De hoge gemiddelde sessieduur (288s) wordt veroorzaakt door een paar lange sessies, terwijl 70% direct afhaakt. Sterke ad-pagina mismatch.

### Ad Set Performance

| Ad Set | Spend | CPC | CTR | Frequency |
|--------|-------|-----|-----|-----------|
| BATCH 2: Expertise & POC - Kopie 1 (H11) | €63.51 | €0.64 | 2.04% | 1.33 |
| BATCH 2: Expertise & POC - Kopie 3 (H13) | €23.57 | €0.65 | 2.01% | 1.27 |
| BATCH 2: Expertise & POC - Kopie 2 (H12) | €8.85 | €0.49 | 3.02% | 1.64 |

---

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | 60.0% | 56.2% | <55% | 🔴 |
| Avg Session Duration | 129s | 90s | >90s | 🟢 |
| Scroll ≥25% | 44.8% | 41.3% | >80% | 🔴 |
| Scroll ≥50% | 41.4% | 37.0% | >60% | 🔴 |
| Scroll ≥75% | 34.5% | 30.4% | >40% | 🟡 |
| Scroll ≥100% | 24.1% | 18.8% | >20% | 🟢 |
| CTA Click Rate | ~15% | ~21% | >4% | 🟢 |
| /booking Visits | 10 uniek | 14.7/dag | meten | → |

**Pageviews:** 134 (100 unieke bezoekers) vs. 7d gem. 176/dag (-24%)
**CTA Clicks gisteren:** Explore Options (5), booking link (5), Go to workshop (4), Book This Date! (2), Add to Cart (1)

**Let op:** "Book Now" button komt niet voor in de data van gisteren maar was de #1 CTA in de 7d data (76 clicks). Mogelijk is de buttontekst aangepast of is deze verplaatst.

---

## 4. Funnel Drop-off

```
Pageview (100 uniek) ──── 100%
       │
       │  ▼ 59% verliest
       │
Scroll 50%+ (~41)  ──── 41%
       │
       │  ▼ 63% verliest
       │
CTA Click (~15)    ──── 15%
       │
       │  ▼ 33% verliest
       │
/booking (10)      ──── 10%
```

**Grootste lek:** Scroll depth. 59% van de bezoekers scrollt niet voorbij de helft van de pagina. De hero sectie en eerste content blokken slagen er niet in om bezoekers vast te houden. Van de 100 unieke bezoekers haken er ~59 af voordat ze de kernboodschap bereiken.

**Secundair lek:** CTA Click naar /booking conversie (63% drop-off). Bezoekers die wel scrollen en CTA's zien, klikken er niet altijd op, of de CTA's staan te laag op de pagina.

---

## 5. Rode Vlaggen 🚩

### 1. CPC €0.62 -- 24% boven target
- **Probleem:** CPC is €0.12 boven de €0.50 target en 19% hoger dan het 7-daags gemiddelde (€0.52)
- **Oorzaak:** Mogelijk dalende relevance score, toenemende concurrentie, of te hoge frequentie op een kleiner audience segment
- **Urgentie:** Hoog

### 2. H13 Bounce Rate 70.4% -- Ad-pagina mismatch
- **Probleem:** 7 van de 10 bezoekers via H13 verlaten de pagina direct
- **Oorzaak:** De hook van H13 creëert een verwachting die de landing page niet meteen waarmaakt
- **Urgentie:** Hoog

### 3. Scroll Depth ≥25% slechts 44.8% -- Hero sectie faalt
- **Probleem:** Meer dan de helft van alle bezoekers scrollt niet voorbij het eerste kwart van de pagina
- **Oorzaak:** Hero sectie is niet overtuigend genoeg, of er is een disconnect tussen ad belofte en pagina-opening
- **Urgentie:** Hoog

### 4. Bounce Rate 60% -- Boven 55% target
- **Probleem:** 66 van 110 sessies waren bounces, 6.8% stijging vs. 7d gemiddelde
- **Oorzaak:** Samenhangende factor met lage scroll depth en H13 mismatch
- **Urgentie:** Medium

### 5. Impressies -23% vs 7d gemiddelde
- **Probleem:** Delivery daalt, budget wordt niet volledig uitgeput
- **Oorzaak:** Meta algoritme schaalt terug, mogelijk door lagere engagement of kwaliteitsscore
- **Urgentie:** Medium

---

## 6. Cross-Reference Analyse

| Cross-Reference | H11 | H12 | H13 |
|-----------------|-----|-----|-----|
| Ad CTR | 2.04% | 3.02% | 2.01% |
| LP Bounce Rate | 61.5% | 40.0% | 70.4% |
| CTR vs Bounce Match | ⚠️ Mismatch | ✅ Match | ❌ Mismatch |
| CPC vs Target | ❌ €0.64 | ✅ €0.49 | ❌ €0.65 |
| Budget Allocatie | 66.2% | 9.2% | 24.6% |

**Patroon:** H12 is verreweg de best presterende variant op ALLE metrics: hoogste CTR, laagste CPC, laagste bounce rate. Toch krijgt het de minste impressies. Meta's algoritme optimaliseert hier suboptimaal, waarschijnlijk door het kleine sample size.

**H13 analyse:** Hoge CTR-to-bounce ratio (2.01% CTR maar 70.4% bounce) = klassieke ad-pagina mismatch. De hook trekt mensen aan die niet matchen met het aanbod, of de landing page beantwoordt de verwachting niet.

**H11 analyse:** Grootste budgettrekker (66%) maar CPC (€0.64) en bounce rate (61.5%) zijn beide boven target. Redelijke CTR maar de on-page engagement is onvoldoende.

---

## 7. Top 3 Acties voor Vandaag

### 1. Herverdeel budget naar H12 (Escalatie: Geel -- Robin goedkeuring)
- **Wat:** Verhoog de dagelijkse budgetcap van H12's ad set, of dupliceer H12 in een nieuwe ad set met hoger budget
- **Waarom:** H12 scoort het best op alle metrics (CTR 3.02%, CPC €0.49, bounce 40%) maar krijgt slechts 9.2% van het budget
- **Hoe:** Meta Ads Manager > Campaign > Ad Set "Kopie 2" > Budget verhogen naar minimaal €30/dag
- **Verwachte impact:** Daling overall CPC richting target, lagere bounce rate, meer /booking visits
- **Escalatie:** Geel (Robin goedkeuring vereist voor budgetwijziging)

### 2. Overweeg H13 te pauzeren (Escalatie: Geel -- Robin goedkeuring)
- **Wat:** Pauzeer H13 of verlaag het budget significant
- **Waarom:** 70.4% bounce rate bij €23.57 spend = betalen voor traffic die direct afhaakt. Dit budget kan beter naar H12
- **Hoe:** Meta Ads Manager > Ad Set "Kopie 3" > Status op Paused zetten
- **Verwachte impact:** Besparing van ~€24/dag die naar betere variant kan, daling overall bounce rate
- **Escalatie:** Geel (Robin goedkeuring vereist)

### 3. Optimaliseer hero sectie landing page (Escalatie: Oranje -- Wix Editor)
- **Wat:** Versterkt de above-the-fold content op startyourballoonbusiness.com. De hero moet direct de belofte uit de ads waarmaken
- **Waarom:** 55% van bezoekers scrollt niet voorbij 25% van de pagina. De hero sectie overtuigt niet
- **Hoe:** Wix Editor > Hero sectie aanpassen: sterkere headline die matcht met ad hooks, social proof (testimonial/badge) boven de fold, duidelijkere CTA hoger op de pagina
- **Verwachte impact:** Daling bounce rate, stijging scroll depth en CTA clicks
- **Escalatie:** Oranje (vereist handmatige edit in Wix)

---

## Appendix: Ruwe Data

### Meta Ads Campagne Totalen (7 dagen: 8-14 apr)
- Totaal spend: €701.76
- Totaal impressies: 66,259
- Totaal link clicks: 711
- Landing page views: 545
- Add to cart: 26
- Initiate checkout: 15
- Purchases: 2
- View content: 49

### PostHog Sessie Data (7 dagen)
- Totaal sessies: 1,015
- Bounce sessies: 570 (56.2%)
- Gem. sessie duur: 90.0s
- /booking pageviews: 146 (103 uniek)

### UTM Breakdown PostHog (gisteren)
| utm_content | Pageviews | Unieke Bezoekers |
|-------------|-----------|------------------|
| h11_b3_cta5 | 76 | 61 |
| h13_b3_cta5 | 33 | 25 |
| h12_b3_cta5 | 11 | 7 |
| bio_link | 8 | 6 |

---

*Rapport gegenereerd op 15 april 2026 via Meta Ads MCP (Pipeboard) + PostHog MCP*
*Data periode: 14 april 2026 (met 7-daags gemiddelde 8-14 april)*
