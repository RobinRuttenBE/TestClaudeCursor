# SYBB Daily Report, 15 april 2026

## 1. Samenvatting

Sterke conversie-dag: 4 purchases (€1.473,50) uit slechts €74,65 spend, ROAS 19,7x. Maar het totale volume lag fors onder het 7d gemiddelde (spend -27%, impressions -34%). CPC steeg naar €0,61 (boven de €0,50 target). H11 blijft de enige ad die converteert, terwijl H12 goedkoop verkeer genereert dat niet engageert op de landing page. De /booking pagina toonde slechts 1 tracked pageview, al zijn er wel 3 "Place Order & Pay" clicks geregistreerd, wat wijst op tracking inconsistentie op de Wix booking pagina.

---

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €74,65 | €101,97 | ↓ -27% |
| Impressions | 5.847 | 8.811 | ↓ -34% |
| Link Clicks | 57 | 98 | ↓ -42% |
| CTR | 2,09% | 2,15% | → |
| CPC | €0,61 | €0,54 | ↑ +13% |
| Frequency | 1,34 | 2,10 | ↓ |
| Landing Page Views | 44 | 76 | ↓ -42% |
| Purchases | 4 | 0,86 | ↑↑ |
| Purchase Value | €1.473,50 | €6.321 | ↓ |
| ROAS | 19,7x | 62,0x | ↓ |

> 7d ROAS wordt sterk opgeblazen door 2 hoge-waarde purchases (€42.773) eerder in de week via H13. Dagelijkse ROAS fluctueert sterk bij lage volumes.

### Ad Variant Performance

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LPV | Purchases | LP Scroll 50%+ |
|-------------------|-------|-------------|-----|-----|-----|-----------|----------------|
| h11_b3_cta5 | €62,18 | 46 | 1,95% | €0,68 | 32 | 4 | 57,7% (15/26) |
| h13_b3_cta5 | €6,64 | 4 | 1,14% | €0,95 | 5 | 0 | 50,0% (1/2) |
| h12_b3_cta5 | €5,83 | 7 | 4,55% | €0,25 | 7 | 0 | 25,0% (1/4) |

**7d referentie per variant:**

| Ad (utm_content) | 7d Spend | 7d LPV | 7d Purchases | 7d CPC |
|-------------------|----------|--------|--------------|--------|
| h11_b3_cta5 | €328,99 | 197 | 4 | €0,66 |
| h13_b3_cta5 | €149,30 | 122 | 2 | €0,62 |
| h12_b3_cta5 | €123,01 | 123 | 0 | €0,39 |
| h14_b3_cta5 | €60,30 | 52 | 0 | €0,42 |
| h15_b3_cta5 | €52,15 | 39 | 0 | €0,47 |

**Beste variant:** H11 (enige converterend, 4 purchases gisteren, beste scroll engagement op LP met 57,7% voorbij 50%)
**Slechtste variant:** H12 (hoge CTR van 4,55% maar slechts 25% scroll 50%+ op LP en 0 conversies in 7 dagen, €123 verspild)

---

## 3. Landing Page Health

*Bron: PostHog (startyourballoonbusiness.com). NB: PostHog staat op UTC timezone, TrendsQuery toonde 0 voor 15 april. Data opgehaald via HogQL met expliciete timestamps.*

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 97 | 170 | meten | &#x1F7E1; laag volume |
| Unique Visitors | 70 | 119 | meten | &#x1F7E1; laag volume |
| Scroll 25%+ | 65,6% (21/32) | 63,9% (230/360) | >80% | &#x1F534; |
| Scroll 50%+ | 53,1% (17/32) | 54,7% (197/360) | >60% | &#x1F7E1; |
| Scroll 75%+ | 43,8% (14/32) | 45,0% (162/360) | >40% | &#x1F7E2; |
| Scroll 100% | 28,1% (9/32) | 30,3% (109/360) | >20% | &#x1F7E2; |
| CTA Click Rate | 15,7% (11/70) | 10,9% (13/119) | >4% | &#x1F7E2; |
| /booking Views | 1 | 19,7 | meten | &#x1F534; |

### CTA Click Breakdown (15 april)
| Element | Clicks |
|---------|--------|
| Go to workshop | 9 |
| Continue (booking flow) | 6 |
| Place Order & Pay | 3 |
| Buy Now | 2 |
| FAQ interacties | 6 |

### Rage Clicks
0 rage clicks gisteren. Geen UX frustratie signalen.

---

## 4. Funnel Drop-off

```
Pageview LP (97, 100%) 
  --> Scroll 50%+ (~53%) 
    --> CTA Click (11, ~15,7% van visitors)
      --> /booking pageview (1, ~1,4%) 
        --> Place Order & Pay (3 clicks)
          --> Purchase (4 via Meta attributie)
```

**Grootste lek:** CTA Click naar /booking pageview. 11 CTA clicks maar slechts 1 tracked /booking pageview. Dit is waarschijnlijk een **tracking probleem**, want er zijn 6 "Continue" clicks en 3 "Place Order & Pay" clicks op de booking pagina geregistreerd. Wix SPA navigatie triggert mogelijk geen nieuwe $pageview bij routing naar /booking.

**Tweede lek:** Hero section retentie. 34% van bezoekers (11/32 met scroll data) verlaat de pagina bij <10% scroll, zonder de eerste sectie te zien. Dit zijn vooral mobiele bounces.

---

## 5. Rode Vlaggen

**&#x1F6A9; CPC boven target: €0,61 vs €0,50 target (+22%)**
H11 CPC is €0,68, H13 zelfs €0,95. Alleen H12 zit onder target (€0,25) maar die converteert niet.

**&#x1F6A9; H12 ad-page mismatch: Hoge CTR (4,55%), lage LP engagement (25% scroll 50%+), 0 conversies**
Klassiek signaal: de ad trekt kliks aan maar de verkeerde doelgroep of misleidende hook. €123 spend in 7 dagen zonder enige conversie.

**&#x1F6A9; /booking tracking breakdown**
Slechts 1 /booking pageview terwijl er aantoonbaar booking-pagina interactie is (6 "Continue" + 3 "Place Order & Pay" clicks). PostHog $pageview events worden niet correct gefired bij Wix interne routing.

**&#x1F6A9; Volume daling: -27% spend, -34% impressions vs 7d gemiddelde**
Meta levert minder impressions uit. Kan duiden op audience saturation in de huidige targeting, of budget pacing na eerdere hoge-spend dagen.

**&#x1F6A9; Scroll 25%+ op 65,6% (target >80%)**
35% van bezoekers scrollt niet voorbij de hero. De bovenste sectie van de LP houdt onvoldoende aandacht vast.

---

## 6. Cross-Referencing: Meta Ads x PostHog

| Patroon | Signaal | Actie |
|---------|---------|-------|
| H11: CTR 1,95% + LP Scroll 57,7% 50%+ | Goede match: ad belofte sluit aan bij pagina content | Doorschalen |
| H12: CTR 4,55% + LP Scroll 25% 50%+ | **Mismatch**: hook trekt verkeerde publiek, pagina voldoet niet aan verwachting | Pauzeren of hook aanpassen |
| H13: CTR 1,14% + LP Scroll 50% 50%+ (n=2) | Te weinig volume om conclusies te trekken | Meer budget geven voor data |
| Frequency 1,34 gisteren vs 2,10 7d avg | Verse doelgroep bereikt | Positief, doorgaan |
| 4 purchases uit 1 variant (H11) | Alle conversies geconcentreerd in 1 ad | Risico: als H11 vermoeit, vallen conversies weg |

---

## 7. Top 3 Acties voor Vandaag

### 1. Pauzeer H12 ad variant (Kopie 2 adset)
- **Wat:** Pauzeer adset "BATCH 2: Expertise & POC - Kopie 2" (H12, B3, CTA5)
- **Waarom:** €123 spend in 7 dagen, 0 conversies, slechtste LP scroll engagement (25%). Hoge CTR (4,55%) is misleidend: het trekt kliks maar geen kopers.
- **Hoe:** Meta Ads Manager > Campagne 2026: SYBB > Adset Kopie 2 > Pauzeer
- **Verwachte impact:** €15-17/dag besparing, budget wordt herverdeeld naar beter converterende varianten
- **Escalatie:** Geel (Robin goedkeuring)

### 2. Fix /booking pageview tracking in Wix
- **Wat:** Voeg een expliciet PostHog `$pageview` event toe bij navigatie naar /booking op de Wix site
- **Waarom:** Funnel data is onbetrouwbaar door ontbrekende /booking pageviews. Gisteren slechts 1 tracked pageview terwijl er 3 "Place Order & Pay" clicks waren. Zonder accurate funnel data kun je de LP niet optimaliseren.
- **Hoe:** Wix Editor > /booking pagina > voeg custom code toe met `posthog.capture('$pageview')` bij page load, of configureer Wix Velo routing om pageview events te triggeren
- **Verwachte impact:** Complete funnel visibility, betere optimalisatie beslissingen
- **Escalatie:** Oranje (Wix Editor nodig)

### 3. Test hero section variant om scroll 25%+ te verhogen
- **Wat:** De huidige hero sectie verliest 35% van bezoekers. Test een variant met een sterkere opening: direct het probleem benoemen ("You know you can make beautiful balloon decorations, but turning that into a real business feels overwhelming") gevolgd door een kort social proof element.
- **Waarom:** Scroll 25%+ is 65,6% vs 80% target. Als meer mensen voorbij de hero komen, stijgt de hele funnel.
- **Hoe:** Wix Editor > Hero sectie > A/B test met aangepaste headline en subheadline
- **Verwachte impact:** +15-20% scroll 25%+, cascade effect op alle funnel stappen
- **Escalatie:** Oranje (Wix Editor nodig)

---

*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*PostHog Project: Default project (ID: 149694) | Timezone: UTC*
*Rapport gegenereerd: 16 april 2026*
