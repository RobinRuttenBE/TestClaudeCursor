# SYBB Daily Report -- 2026-04-14

## 1. Samenvatting

Matige dag voor SYBB. CPC steeg naar **€0.62** (boven €0.50 target) en de bounce rate is met **82.7%** ver boven de 55% doelstelling. Positief: gemiddelde sessieduur van **3m35s** (ruim boven 90s target) en er waren **10 unieke bezoekers** op /booking. H12 presteert veruit het best qua CTR en CPC maar krijgt slechts 9% van het budget.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €95.93 | €100.25 | → |
| Impressions | 7,292 | 9,466 | ↓ |
| Clicks | 154 | 194 | ↓ |
| CTR | 2.11% | 2.05% | → |
| CPC | €0.62 | €0.52 | ↑ |
| Link Clicks | 83 | 102 | ↓ |
| Landing Page Views | 63 | 78 | ↓ |
| Frequency | 1.53 | 1.92 | → |
| Video Views | 1,568 | 1,866 | ↓ |
| Add to Cart | 2 | 3.7 | → |
| View Content (pixel) | 7 | 7 | → |

**Opmerking:** Impressies en clicks lagen gisteren ~23% onder het 7d gemiddelde. CTR bleef stabiel, maar CPC steeg met 19%. Budget is niet volledig besteed (€95.93 van €100 daily budget).

### Ad Variant Performance

| Ad (utm_content) | Spend | Impressions | Link Clicks | CTR | CPC | LP Views | Add to Cart |
|-------------------|-------|-------------|-------------|-----|-----|----------|-------------|
| H11, B3, CTA5 | €63.51 | 4,903 | 55 | 2.04% | €0.64 | 40 | 0 |
| H13, B3, CTA5 | €23.57 | 1,792 | 19 | 2.01% | €0.65 | 14 | 0 |
| H12, B3, CTA5 | €8.85 | 597 | 9 | 3.02% | €0.49 | 9 | 2 |

**Beste variant:** **H12, B3, CTA5** met de hoogste CTR (3.02%), laagste CPC (€0.49, enige onder target), en als enige 2 add-to-carts. Ondanks maar 9% van het budget genereert deze ad de beste downstream metrics.

**Slechtste variant:** **H13, B3, CTA5** met de laagste CTR (2.01%), hoogste CPC (€0.65), en geen add-to-carts. De kosten per link click (€1.24) zijn het hoogst van alle varianten.

### Ad Set Performance

| Ad Set | Spend | CPC | CTR | Frequency |
|--------|-------|-----|-----|-----------|
| BATCH 2: Kopie 1 (H11) | €63.51 | €0.64 | 2.04% | 1.34 |
| BATCH 2: Kopie 3 (H13) | €23.57 | €0.65 | 2.01% | 1.27 |
| BATCH 2: Kopie 2 (H12) | €8.85 | €0.49 | 3.02% | 1.64 |

## 3. Landing Page Health (PostHog)

| Metric | Gisteren | 7d Gem/dag | Target | Status |
|--------|----------|------------|--------|--------|
| Pageviews | 134 | 176 | meten | meten |
| Unique Visitors | 100 | ~125 | meten | meten |
| Sessions | 104 | n/a | meten | meten |
| Bounce Rate | 82.7% | n/a | <55% | :red_circle: |
| Avg Session Duration | 214.6s (3m35s) | n/a | >90s | :green_circle: |
| CTA Click Rate | 12.0% (12/100) | n/a | >4% | :green_circle: |
| /booking Visits | 10 unique | ~15/dag | meten | meten |

**Bounce rate berekening:** 86 van 104 sessies hadden slechts 1 pageview = 82.7%. Dit is de sessie-gebaseerde bounce rate berekend uit PostHog event data.

**Scroll Depth:** Niet beschikbaar. Er zijn geen `scroll_depth` events geconfigureerd in PostHog. Alleen $autocapture events (55) geregistreerd. **Aanbeveling:** scroll depth tracking instellen voor betere engagement data.

### CTA Click Details (autocapture)

| Element | Clicks |
|---------|--------|
| Explore Options | 5 |
| www...com/booking (link) | 5 |
| Go to workshop | 4 |
| What does my ticket include? | 3 |
| Book This Date! | 2 |
| Add to Cart | 1 |
| FAQ items (diverse) | 4 |

### UTM Segmentatie (PostHog)

| UTM Content | Pageviews | Unique Visitors | % van totaal |
|-------------|-----------|-----------------|--------------|
| h11_b3_cta5 | 76 | 61 | 61% |
| h13_b3_cta5 | 33 | 25 | 25% |
| h12_b3_cta5 | 11 | 7 | 7% |
| bio_link | 8 | 6 | 6% |
| (geen UTM) | 6 | ~1 | 1% |

### 7d Dagelijkse Pageviews Trend

| Dag | Pageviews | Unique Visitors |
|-----|-----------|-----------------|
| Ma 8 apr | 136 | 111 |
| Di 9 apr | 127 | 87 |
| Wo 10 apr | 224 | 170 |
| Do 11 apr | 242 | 176 |
| Vr 12 apr | 189 | 124 |
| Za 13 apr | 178 | 105 |
| Zo 14 apr | 134 | 100 |

Trend: **dalend weekend**. Piek was donderdag 11 april (242 pv). Zondag was de zwakste dag van de week.

## 4. Funnel Drop-off

```
Pageview (100 uniek)  ---- 100%
        |
        |  -84% drop
        v
CTA Click (16 uniek)  ---- 16%
        |
        |  -37.5% drop
        v
/booking (10 uniek)   ---- 10%
```

**Grootste lek:** Van Pageview naar CTA Click verliezen we **84%** van de bezoekers. Dit correleert met de hoge bounce rate van 82.7%. De meeste bezoekers verlaten de pagina voordat ze een CTA bereiken.

**Positief:** Van de 16 mensen die een CTA klikten, gingen 10 (62.5%) door naar /booking. De CTA-naar-booking conversie is sterk.

## 5. Cross-Reference Analyse

### Ad CTR vs LP Bounce Rate
- **H11:** Gemiddelde CTR (2.04%) + Hoge bounce = ad belofte matcht, maar LP engagement faalt
- **H13:** Laagste CTR (2.01%) + Hoge bounce = slechtste combinatie
- **H12:** Hoogste CTR (3.02%) + 2 add-to-carts = beste ad-to-page match

### Budget vs Performance Mismatch
Meta's Advantage+ geeft 66% van budget aan H11, terwijl H12 de beste downstream metrics heeft:
- H11: €63.51 spend voor 0 add-to-carts (geen downstream conversie)
- H12: €8.85 spend voor 2 add-to-carts (€4.43 per ATC)

Dit is een **klassieke optimalisatie-mismatch**: Meta optimaliseert op clicks/impressions, niet op werkelijke conversies.

### Frequency vs Bounce
Frequency is nog laag (1.53 gisteren, 1.92 7d). Ad fatigue is **nog geen probleem**, de hoge bounce rate wordt niet veroorzaakt door herhaalde blootstelling maar door landing page issues.

## 6. Rode Vlaggen

1. **CPC €0.62 > €0.50 target** -- 19% boven 7d gemiddelde (€0.52). Stijgende trend.
2. **Bounce rate 82.7% > 70% drempel** -- Kritiek. De landing page verliest 83% van bezoekers op de eerste interactie.
3. **Impressies -23% vs 7d gem** -- Ongebruikelijke daling op een zondag. Budget niet volledig besteed.
4. **Geen scroll depth tracking** -- Zonder scroll data missen we cruciale engagement informatie.
5. **H12 budget allocatie (9%)** -- Best presterende ad krijgt het minste budget van Meta's algoritme.

## 7. Top 3 Acties voor Vandaag

### 1. Dupliceer H12 als nieuwe ad set met hoger budget
- **Wat:** Maak een nieuwe ad set specifiek voor H12,B3,CTA5 met een minimum spend van €30/dag
- **Waarom:** H12 heeft de beste CTR (3.02%), laagste CPC (€0.49), en enige add-to-carts. Meta geeft het maar 9% budget.
- **Hoe:** Meta Ads Manager > Dupliceer ad set "Kopie 2" > Stel manueel budget in op €30/dag
- **Verwachte impact:** Bij gelijke performance: ~30 extra link clicks voor ~€15, potentieel 6-7 add-to-carts
- **Escalatie:** Geel (Robin goedkeuring nodig)

### 2. Onderzoek landing page bounce probleem
- **Wat:** Analyseer de first fold/hero sectie van startyourballoonbusiness.com via session recordings
- **Waarom:** 82.7% bounce rate betekent dat de hero sectie mensen niet vasthoudt. Met 214s gemiddelde sessieduur voor degenen die blijven, is de content sterk, maar de eerste indruk faalt.
- **Hoe:** PostHog > Session Recordings bekijken. Zoek patronen: laden mensen lang? Scrollen ze en vertrekken ze? Of sluiten ze direct het tabblad?
- **Verwachte impact:** Identificatie van het exacte probleem voor targeted fixes
- **Escalatie:** Groen (onderzoek, geen wijziging)

### 3. Stel scroll depth tracking in op PostHog
- **Wat:** Configureer custom scroll depth events (25%, 50%, 75%, 100%) in PostHog
- **Waarom:** Zonder scroll data weten we niet of bezoekers de CTA's zien. Dit blokkeert alle toekomstige LP optimalisatie.
- **Hoe:** Voeg een scroll depth tracking script toe aan de Wix site of configureer via PostHog's toolbar
- **Verwachte impact:** Compleet beeld van engagement, basis voor alle LP A/B tests
- **Escalatie:** Oranje (Wix Editor nodig)

---

*Rapport gegenereerd op 2026-04-15 | Data bronnen: Meta Ads MCP (Pipeboard) + PostHog MCP*
*Campagne: 2026: SYBB | Account: Sempertex Ad Account (act_567892422940728)*
