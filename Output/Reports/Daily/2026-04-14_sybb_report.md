# SYBB Daily Report -- 2026-04-14

## 1. Samenvatting

Matige dag voor SYBB. Het verkeer lag 24% onder het 7-daags gemiddelde bij vrijwel dezelfde spend, wat resulteert in een CPC van €0.62 (boven target van €0.50). De bounce rate blijft hardnekkig hoog op 82.7%, met 40% van bezoekers die niet eens voorbij de hero scrollen. Positief: H12 blijft de best presterende variant met de laagste CPC (€0.49), hoogste CTR (3.02%) en laagste bounce (75%), maar krijgt slechts 9% van het budget. Er waren 10 unieke bezoekers op /booking, goed voor een conversieratio van 9.6%.

---

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €95.94 | €100.25 | → |
| Impressions | 7,294 | 9,466 | ↓ |
| Clicks | 154 | 194 | ↓ |
| CTR | 2.11% | 2.05% | → |
| CPC | €0.62 | €0.52 | ↑ |
| Link Clicks | 83 | 102 | ↓ |
| LP Views | 63 | 78 | ↓ |
| Frequency | 1.53 | 1.92 | ↓ |
| Video Views | 1,568 | 1,866 | ↓ |
| Add to Cart | 2 | 3.7 | → |

### Ad Set Performance

| Ad Set | Spend | Impressions | Clicks | CTR | CPC | LP Views | Frequency |
|--------|-------|-------------|--------|-----|-----|----------|-----------|
| Kopie 1 (H11) | €63.52 | 4,905 | 100 | 2.04% | €0.64 | 40 | 1.34 |
| Kopie 3 (H13) | €23.57 | 1,792 | 36 | 2.01% | €0.65 | 14 | 1.27 |
| Kopie 2 (H12) | €8.85 | 597 | 18 | 3.02% | €0.49 | 9 | 1.64 |

### Ad Variant Performance (Meta + PostHog Cross-Reference)

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LP Views (Meta) | PH Sessions | PH Bounce | PH Clicks |
|-------------------|-------|-------------|-----|-----|-----------------|-------------|-----------|-----------|
| h11_b3_cta5 | €63.52 | 55 | 2.04% | €0.64 | 40 | 62 | 83.9% | 28 |
| h13_b3_cta5 | €23.57 | 19 | 2.01% | €0.65 | 14 | 26 | 88.5% | 14 |
| h12_b3_cta5 | €8.85 | 9 | 3.02% | €0.49 | 9 | 8 | 75.0% | 6 |

**Beste variant:** H12,B3,CTA5. Hoogste CTR (3.02%), laagste CPC (€0.49, enige variant onder target), laagste bounce rate (75%). Ook de enige variant met add-to-cart conversies gisteren (2x). Krijgt echter slechts 9.2% van het dagbudget.

**Slechtste variant:** H13,B3,CTA5. Laagste CTR (2.01%), hoogste CPC (€0.65), en alarmerend hoge bounce rate van 88.5%. Bijna 9 van de 10 bezoekers verlaten de pagina direct.

### 7d Ad Variant Totalen (voor context)

| Ad | 7d Spend | 7d Link Clicks | 7d LP Views | 7d CPC |
|----|----------|----------------|-------------|--------|
| H11,B3,CTA5 | €266.81 | 213 | 165 | €0.66 |
| H13,B3,CTA5 | €142.67 | 138 | 117 | €0.61 |
| H12,B3,CTA5 | €117.18 | 141 | 116 | €0.40 |
| H14,B3,CTA5 | €122.96 | 158 | 108 | €0.41 |
| H15,B3,CTA5 | €52.15 | 61 | 39 | €0.47 |

---

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 134 | 176/d | - | ↓ |
| Unique Visitors | 100 | 119/d | - | ↓ |
| Sessions | 104 | 130/d | - | ↓ |
| Bounce Rate | 82.7% | 81.9% | <55% | 🔴 |
| Avg Session Duration | 196s | 199s | >90s | 🟢 |
| Median Session Duration | 7s | - | >90s | 🔴 |
| Scroll 25%+ | 55.3% | 50.5% | >80% | 🔴 |
| Scroll 50%+ | 50.0% | 45.5% | >60% | 🔴 |
| Scroll 75%+ | 44.7% | 38.9% | >40% | 🟢 |
| Scroll 100% | 31.6% | 25.1% | >20% | 🟢 |
| /booking Visits | 10 | - | - | - |
| LP > Booking Rate | 9.6% | - | >5% | 🟢 |

**Let op:** De gemiddelde sessieduur (196s) is misleidend. De mediaan is slechts 7 seconden, wat bevestigt dat de meerderheid direct bounced terwijl een kleine groep lang blijft. Dit is een bimodale verdeling.

### CTA Click Breakdown

| Element | Clicks |
|---------|--------|
| Explore Options | 5 |
| www.startyourballoonbusiness.com/booking | 5 |
| Go to workshop | 4 |
| What does my ticket include? (FAQ) | 3 |
| Book This Date! | 2 |
| Add to Cart | 1 |
| Overige FAQ items | 4 |

Totaal CTA clicks (excl. FAQ): 17 clicks van 104 sessions = 16.3%

---

## 4. Funnel Drop-off

```
Pageview (100%, 104 sessions)
    ↓ -44.7% drop
Scroll 50%+ (50.0%, ~52 sessions)
    ↓ -36.0% drop  
CTA Click (~14%, ~15 sessions)
    ↓ -4.4% drop
/booking (9.6%, 10 unique visitors)
```

**Grootste lek:** De eerste stap. 45% van alle bezoekers scrollt niet eens voorbij 25% van de pagina. De hero sectie/above-the-fold content verliest bijna de helft van het verkeer direct. Dit is het primaire probleem.

---

## 5. Rode Vlaggen 🚩

1. **CPC €0.62 > €0.50 target** -- 19% boven 7d gemiddelde (€0.52). Bij gelijke spend krijg je minder verkeer. Impressions daalden 23% terwijl spend slechts 4% daalde.

2. **Bounce rate 82.7% > 70% drempel** -- Consistent hoog. 7d gemiddelde is 81.9%, dus dit is structureel. 86 van 104 sessies zijn single-page bounces.

3. **H13 bounce rate 88.5%** -- Bijna 9 op 10 bezoekers via H13 verlaten de pagina direct. Dit is de slechtste ad-pagina match van alle varianten.

4. **40% zero-scroll rate** -- 15 van 38 gemeten pageleave events tonen 0% scroll. Deze bezoekers zien de pagina en vertrekken zonder enige interactie.

5. **Mediaan sessieduur 7 seconden** -- De "gemiddelde" van 196s wordt opgetrokken door enkele geengageerde bezoekers. De typische bezoeker is in 7 seconden weer weg.

---

## 6. Cross-Reference Analyse

### Ad CTR vs LP Bounce (ad-pagina mismatch detectie)

| Pattern | Variant | Bevinding |
|---------|---------|-----------|
| Hoge CTR + Lage Bounce | H12 (3.02% CTR, 75% bounce) | Beste match. De ad belofte sluit het best aan bij de LP content. |
| Lage CTR + Hoge Bounce | H13 (2.01% CTR, 88.5% bounce) | Slechtste performer op beide assen. Ad trekt verkeerd publiek of LP voldoet niet aan de verwachting. |
| Hoge Spend + Hoge Bounce | H11 (€63.52 spend, 83.9% bounce) | Grootste geldlek: 66% van dagbudget gaat naar een variant met 84% bounce. |

### Frequency vs Bounce

Frequency is laag gisteren (1.53 vs 1.92 7d), wat betekent dat het publiek relatief vers is. Toch bounced 83% direct. Conclusie: het probleem zit niet in ad fatigue maar in de landing page zelf.

### Cost per Engaged Visitor

Van de 104 sessies bleven ~18 bezoekers langer dan de mediaan en scrollden voorbij 50%. Effectieve cost per geengageerde bezoeker: €95.94 / 18 = **€5.33 per geengageerde bezoeker**. Voor de 10 /booking bezoekers: **€9.59 per /booking bezoek**.

---

## 7. Top 3 Acties voor Vandaag

### 1. Verschuif budget van H13 naar H12
- **Wat:** Pauzeer ad set Kopie 3 (H13) of verlaag budget significant. Verhoog budget voor Kopie 2 (H12).
- **Waarom:** H13 heeft de slechtste CTR (2.01%), hoogste CPC (€0.65), en 88.5% bounce. H12 presteert beter op alle metrics: 3.02% CTR, €0.49 CPC, 75% bounce, en is de enige variant met add-to-cart conversies gisteren.
- **Hoe:** Meta Ads Manager > Campagne 2026: SYBB > Budget aanpassen per ad set. Verdubbel Kopie 2 budget, halveer Kopie 3.
- **Verwachte impact:** Lagere gemiddelde CPC, minder verspild budget, hogere LP engagement.
- **Escalatie:** 🟡 Geel (Robin goedkeuring nodig voor budgetverschuiving)

### 2. Optimaliseer hero sectie (above the fold)
- **Wat:** Analyseer en herwerk de hero sectie van startyourballoonbusiness.com. De eerste viewport moet sterker.
- **Waarom:** 40% van bezoekers scrollt niet eens voorbij de eerste sectie. Mediaan sessieduur is 7 seconden. De hero faalt in het vasthouden van aandacht.
- **Hoe:** Check de hero headline, visueel, en eerste CTA positie in Wix Editor. Overweeg: sterkere headline die aansluit bij ad hooks, social proof boven de fold, meer visuele urgentie.
- **Verwachte impact:** Als zero-scroll rate daalt van 40% naar 20%, stijgt de effectieve funnel throughput met 33%.
- **Escalatie:** 🟠 Oranje (Wix Editor wijziging nodig)

### 3. A/B test LP variant voor H11 verkeer
- **Wat:** Maak een LP variant specifiek voor H11 verkeer (grootste budget, 84% bounce).
- **Waarom:** H11 krijgt 66% van het budget maar heeft 84% bounce. De ad hook matcht niet goed met de huidige LP. Door een LP variant te maken die beter aansluit bij de H11 belofte, kan de bounce significant dalen.
- **Hoe:** Dupliceer de LP in Wix, pas de hero aan op de H11 hook, en stuur H11 verkeer naar de variant via een aparte UTM landing URL.
- **Verwachte impact:** Als bounce daalt van 84% naar 70%, stijgt het aantal geengageerde bezoekers van H11 met ~85%.
- **Escalatie:** 🔴 Rood (strategische LP aanpassing + Wix + Meta Ads URL update)

---

*Rapport gegenereerd op 2026-04-15 op basis van Meta Ads MCP (Pipeboard) en PostHog MCP data.*
*Datumbereik: 2026-04-14 (dagdata) vs 2026-04-08 t/m 2026-04-14 (7d referentie).*
