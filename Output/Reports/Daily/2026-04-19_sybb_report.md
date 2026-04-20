# SYBB Daily Report, 2026-04-19

## 1. Samenvatting
SYBB draaide gisteren op 2 campagnes: de originele "2026: SYBB" werd om 14:29 gepauzeerd, en "2026: SYBB - Kopie" startte om 14:25 (overlap van enkele minuten). Gecombineerd was het volume vergelijkbaar met het 7d gemiddelde (€89,58 spend, 136 clicks, 6 initiate checkouts). De grote zorg zit op de landing page: bounce rate steeg naar 85,7% (vs 80% 7d), avg session zakte naar 33s (vs 44s), en scroll depth viel terug naar 17,5% (vs 44%). Ads doen hun werk, de pagina vangt het verkeer niet op.

## 2. Meta Ads Performance

### Campagne setup
- "2026: SYBB" (oud, ID 120239435987290239): PAUSED sinds 14:29 op 19/04
- "2026: SYBB - Kopie" (nieuw, ID 120243293329420239): ACTIVE sinds 14:25 op 19/04

Cijfers hieronder zijn gecombineerd voor beide campagnes (gisteren), en het 7d gemiddelde komt uit alleen de oude campagne (Kopie bestond nog niet).

| Metric | Gisteren (combined) | 7d Avg/dag (oud) | Trend |
|--------|---------------------|------------------|-------|
| Spend | €89,58 | €84,89 | → |
| Impressions | 6.079 | 6.110 | → |
| Clicks | 136 | 134 | → |
| Link clicks | 85 | 74 | ↑ |
| Landing page views | 71 | 60 | ↑ |
| CTR | 2,24% | 2,20% | → |
| CPC | €0,66 | €0,63 | → |
| Frequency (per camp.) | 1,21 / 1,35 | 2,13 (cumul. 7d) | n.v.t. |
| Initiate checkouts | 6 | 3,3 | ↑↑ |
| Cost per IC | €14,93 | €25,84 | ↓ goed |

### Ad Variant Performance (gisteren, gecombineerd)

| Ad (utm_content) | Impr | Clicks | CTR | CPC | LPV | LP Sessions | LP Bounce |
|------------------|------|--------|-----|-----|-----|-------------|-----------|
| h11_b3_cta5 | 2.925 | 71 | 2,43% | €0,57 | 38 | 58 | 86,2% |
| h13_b3_cta5 | 2.353 | 46 | 1,95% | €0,81 | 28 | 46 | 89,1% |
| h12_b3_cta5 | 801 | 19 | 2,37% | €0,62 | 5 | 10 | 60,0% |
| h14_b3_cta5 | (geen actieve levering) | | | | | 1 | 100% |

**Beste variant:** h12_b3_cta5. Beste bounce rate (60%) en redelijke CPC (€0,62). Klein volume (801 impr) maar de bezoekers zijn het meest gekwalificeerd.
**Slechtste variant:** h13_b3_cta5. Hoogste CPC (€0,81, ver boven target €0,50) en hoogste bounce (89,1%). De hoge session duration (71s) suggereert dat de paar bezoekers die niet bouncen wel engaged zijn, maar de cost-efficiency is slecht.
**Hoogste volume:** h11_b3_cta5 levert het meeste verkeer maar bezoekers vertrekken binnen 7,4s gemiddeld.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 140 | 134/dag | n.v.t. | → |
| Unique visitors | 115 | 94/dag | n.v.t. | ↑ |
| Sessions | 119 | 98/dag | n.v.t. | ↑ |
| Bounce Rate | 85,71% | 79,97% | <55% | 🔴 |
| Avg Session Duration | 33,2s | 43,9s | >90s | 🔴 |
| Avg Scroll % | 17,5% | 44,2% | n.v.t. | 🔴 |
| Scroll 25% | 17,6% (3/17) | 47,4% | >80% | 🔴 |
| Scroll 50% | 17,6% (3/17) | 41,5% | >60% | 🔴 |
| Scroll 75% | 17,6% (3/17) | 36,6% | >40% | 🔴 |
| Scroll 100% | 5,9% (1/17) | 22,0% | >20% | 🔴 |
| CTA Click Rate ("Book Your Spot" / LP views) | 5,4% (7/130) | n.b. | >4% | 🟢 |

Let op: scroll-data komt uit pageleave events. Gisteren slechts 17 leave events op 140 pageviews (12% trigger rate), dus de scroll-cijfers zijn weinig betrouwbaar maar wijzen wel op een trend.

### Landing Page UTM Breakdown (sessies vs gedrag)

| utm_content | Sessions | Bounce | Avg Duration |
|-------------|----------|--------|--------------|
| h11_b3_cta5 | 58 | 86,2% | 7,4s |
| h13_b3_cta5 | 46 | 89,1% | 71,1s |
| h12_b3_cta5 | 10 | 60,0% | 25,0s |
| (geen utm) | 4 | 100% | 0s |
| h14_b3_cta5 | 1 | 100% | 0s |

## 4. Funnel Drop-off (gisteren)

```
Landing page (/)        130  (100%)
   ↓
CTA click "Book Spot"     7    (5,4%)   ← drop -94,6%
   ↓
Pageview /booking         2    (1,5%)   ← drop -71%
   ↓
Pageview /checkout        7    (5,4%)*
   ↓
Initiate Checkout (Meta)  6    (4,6%)
```

*Checkout-pageviews komen ook via /product-page/start-your-balloon-business-professional binnen, niet alleen via /booking.

**Grootste lek:** stap 1 → 2. Van 130 landing page views komen er maar 7 tot een CTA click, en slechts 2 daarvan landen op /booking. De CTR op de CTA zelf is OK (5,4%), maar de absolute conversie is laag omdat 86% bouncet voordat ze überhaupt scrollen.

## 5. Rode Vlaggen 🚩

1. **Bounce rate 85,71% (target <55%, 7d avg 80%).** Yesterday was 5,7 ppt slechter dan het al hoge weekgemiddelde. Hero-sectie + first-fold faalt voor het grootste deel van het verkeer.
2. **Avg session duration 33,2s (target >90s).** Daling van 24% vs 7d. Mensen krijgen niet genoeg om vast te bijten.
3. **h11_b3_cta5: 86,2% bounce + 7,4s session.** Hoogste volume-ad maar levert "instant exits". Sterke ad/page mismatch: de hook trekt aandacht maar de pagina vervult de belofte niet.
4. **h13_b3_cta5: CPC €0,81 (target <€0,50, +62% boven).** Duurste klikker met slechtste bounce.
5. **Scroll depth gecollapseerd:** avg 17,5% gisteren vs 44,2% over 7d. Steekproef is klein (17 pageleaves) maar 14 van de 17 raken niet eens 25% scroll.
6. **Frequency oude campagne 2,13 cumulatief over 7d.** Nog niet kritiek, maar de campagne is logischerwijs gepauzeerd vanwege fatigue. Goede beslissing, monitor frequency van de Kopie.

## 6. Top 3 Acties voor Vandaag

1. **Onderzoek de h11_b3_cta5 ad-naar-page mismatch.** Wat: bekijk 5 session recordings van h11 sessies in PostHog en de h11 ad creative in Meta. Waarom: 58 sessies, 86% bounce, 7s session. Mensen klikken massaal maar verlaten direct. Hoe: PostHog → Recordings → filter op utm_content=h11_b3_cta5, vergelijk de hook in de ad met wat ze als eerste op de pagina zien. Verwachte impact: als de mismatch boven water komt, kunnen we de hero-sectie aanpassen of de ad-copy bijschaven, doel bounce naar <70%. Escalatie: Geel (Robin goedkeuring nadat de oorzaak duidelijk is).
2. **Pauzeer of vervang h13_b3_cta5 in de Kopie-campagne.** Wat: zet h13 op pause, laat h11 en h12 doorlopen, en lanceer 1 nieuwe variant (bv. h15) als test. Waarom: h13 kost €0,81/click (62% boven target) en heeft 89% bounce. We betalen premium voor het slechtste verkeer. Verwachte impact: campagne-CPC zakt richting €0,57 (gewogen avg van h11+h12), bespaart ~€8 per dag. Escalatie: Geel.
3. **Fix scroll-tracking en/of voeg scroll-trigger toe aan de pagina.** Wat: controleer in Wix of de PostHog autocapture pageleave/scroll-tracking volledig actief is op alle viewports (vooral mobile). Waarom: maar 17 van 140 pageviews (12%) leveren scroll-data, dus we kunnen de hero-performance niet betrouwbaar meten en kunnen niet onderbouwd optimaliseren. Hoe: PostHog Toolbar live op de pagina + check of pageleave event beforeunload wordt afgevuurd. Verwachte impact: bredere dataset (target >50% trigger rate), waardoor de scroll-KPIs uit het rapport bruikbaar worden voor optimalisatie. Escalatie: Geel (Robin goedkeuring) → mogelijk Oranje (Wix Editor).

---

### Cross-reference samenvatting
- **Ad CTR (2,24%) vs LP Bounce (85,7%):** ads doen het goed, pagina vangt het verkeer niet op. Ad-page mismatch is het hoofdprobleem.
- **CPC daalt licht maar bounce stijgt:** goedkoper verkeer, slechtere kwaliteit. Prijs is geen probleem, fit is dat wel.
- **h12 wint op kwaliteit, h11 op volume, h13 verliest op alles.** Volgende batch: schaal h11 + h12, dood h13, test 2 nieuwe hooks die het patroon van h12 (lagere bounce) imiteren.
- **Initiate checkouts up (+71% vs 7d avg).** Ondanks slechte LP-engagement halen meer mensen dan gemiddeld de checkout. Mogelijk effect van de campagnewissel of een batch betere bezoekers laat in de avond. Houd morgen in de gaten of dit een trend is.
