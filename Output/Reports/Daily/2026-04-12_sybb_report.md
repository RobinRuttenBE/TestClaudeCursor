# SYBB Daily Report -- 12 April 2026

## 1. Samenvatting

Gemengde dag. Meta Ads CPC steeg fors naar **\EUR0.68** (target <\EUR0.50), ruim boven het 7d gemiddelde van \EUR0.47. GA4 toont 100% bounce rate en 0% engagement rate op alle sessies, wat wijst op een **tracking probleem** (want er zijn WEL 21 /booking bezoeken en 2 booking completes). Positief: de /booking conversie (22.8%) lag ver boven het 7d gemiddelde (10.9%), en H12 presteert sterk met de laagste CPC (\EUR0.41) en hoogste CTR (2.94%).

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | \EUR139.73 | \EUR66.43 | ↑ |
| Impressions | 10,775 | 7,008 | ↑ |
| Clicks | 207 | 142 | ↑ |
| CTR | 1.92% | 2.03% | → |
| CPC | \EUR0.68 | \EUR0.47 | ↑ |
| Link Clicks | 99 | 74 | ↑ |
| LP Views (Meta) | 90 | 57 | ↑ |
| Frequency | 1.51 | 1.79 | → |

> **Let op:** 7d gemiddelde is vertekend omdat ad sets Kopie 1-4 pas op 9 april startten. De eerste 2 dagen (6-7 april) hadden minimale spend. Het originele "BATCH 2: Expertise & POC" ad set (met H14) werd gepauzeerd op 11 april.

### Ad Variant Performance (gisteren)

| Ad (utm_content) | Link Clicks | CTR | CPC | LP Views (Meta) | GA4 Sessions | GA4 Avg Duration |
|-------------------|-------------|------|------|-----------------|--------------|------------------|
| H11,B3,CTA5 | 51 | 1.64% | \EUR0.81 | 44 | 44 | 0.9s |
| H12,B3,CTA5 | 18 | 2.94% | \EUR0.41 | 14 | 16 | 7.6s |
| H13,B3,CTA5 | 24 | 1.99% | \EUR0.62 | 24 | 17 | 0s |
| H15,B3,CTA5 | 6 | 1.77% | \EUR0.77 | 8 | 5 | 0s |

**Budget verdeling gisteren:**
- H11: \EUR78.82 (56%) -- disproportioneel hoog
- H13: \EUR27.84 (20%)
- H12: \EUR19.24 (14%)
- H15: \EUR13.83 (10%)

**Beste variant:** H12,B3,CTA5 -- laagste CPC (\EUR0.41), hoogste CTR (2.94%), en langste GA4 session duration (7.6s). Efficiëntste ad van de groep.

**Slechtste variant:** H11,B3,CTA5 -- hoogste CPC (\EUR0.81), krijgt 56% van het budget maar heeft <1s GA4 session duration. 2 initiate checkouts is het enige positieve signaal.

### Pixel Conversies (gisteren)

| Event | Aantal |
|-------|--------|
| View Content | 10 |
| Add to Cart | 4 |
| Initiate Checkout | 2 |
| Purchase | 0 |

### 7d Pixel Conversies (ter referentie)

| Event | 7d Totaal | Daggemiddelde |
|-------|-----------|---------------|
| View Content | 31 | 4.4 |
| Add to Cart | 16 | 2.3 |
| Initiate Checkout | 10 | 1.4 |
| Purchase | 2 | 0.3 |
| Complete Registration | 1 | 0.1 |

## 3. Landing Page Health (GA4)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Sessions | 102 | 93.4/d | -- | -- |
| Unique Users | 98 | 88.0/d | -- | -- |
| Bounce Rate | 100% | 85.8% | <55% | :red_circle: |
| Avg Session Duration | 27s | ~35s | >90s | :red_circle: |
| Scroll 90% (GA4 scroll event) | 3.1% (3/98) | 4.1% (28/654) | >20% | :red_circle: |
| /booking Visit Rate | 20.6% (21/102) | 10.6% (69/654) | >4% | :green_circle: |
| Engagement Rate (GA4) | 0% | 14.2% | -- | :red_circle: |
| sybb_booking_complete | 2 | 0.43/d | -- | :green_circle: |

> **TRACKING ISSUE:** GA4 rapporteert 0% engagement rate en 100% bounce rate op 12 april, terwijl er WEL 21 sessies naar /booking navigeerden en 2 booking completes plaatsvonden. De GA4 engagement tracking is kapot of incorrect geconfigureerd. Session duration data per UTM segment is onbetrouwbaar.

### UTM Segment Detail (GA4, gisteren)

| UTM Content | Sessions | Avg Duration | Pageviews |
|-------------|----------|--------------|-----------|
| h11_b3_cta5 | 44 | 0.9s | 45 |
| (geen UTM) | 25 | 102.5s | 36 |
| h13_b3_cta5 | 17 | 0s | 17 |
| h12_b3_cta5 | 16 | 7.6s | 19 |
| (not set) | 11 | 4.4s | 12 |
| h15_b3_cta5 | 5 | 0s | 5 |

**Opvallend:** Organisch/direct traffic (geen UTM) heeft 102.5s session duration terwijl Meta traffic 0-8s heeft. Dit kan wijzen op een tracking issue specifiek voor Meta traffic, of op een fundamenteel verschil in engagement.

## 4. Funnel Drop-off

```
LP Pageview (100%, 92 sessions)
    ↓ [77.2% drop-off]
/booking (22.8%, 21 sessions)
    ↓ [61.9% drop-off]
Product Page (8.7%, 8 sessions)
    ↓ [87.5% drop-off]
/checkout (1.1%, 1 session)
    ↓ [0% drop-off]
/thank-you-page (1.1%, 1 session)
```

**sybb_booking_complete events:** 2 (van 1 user)

**Grootste lek:** Product Page naar Checkout -- 87.5% drop-off. Slechts 1 van 8 product page bezoekers gaat door naar checkout.

**Positief:** LP naar /booking conversie (22.8%) is ruim boven het 7d gemiddelde (10.9%). De CTA op de landing page werkt goed.

## 5. Rode Vlaggen

1. **CPC \EUR0.68 -- 36% boven target (\EUR0.50)** en 45% hoger dan 7d gemiddelde. H11 is de grootste oorzaak (\EUR0.81 CPC, 56% van budget).

2. **GA4 Engagement Tracking kapot** -- 100% bounce rate en 0% engagement rate terwijl er aantoonbaar navigatie naar /booking plaatsvindt. Alle GA4 engagement metrics zijn onbetrouwbaar totdat dit is opgelost.

3. **H11 budget-prestatie mismatch** -- Krijgt 56% van dagbudget (\EUR78.82) maar heeft slechtste CPC (\EUR0.81) en near-zero session duration (0.9s). Meta's algoritme optimaliseert op volume, niet op kwaliteit.

4. **Scroll depth extreem laag** -- Slechts 3 van 98 users (3.1%) bereiken 90% scroll. Dit betekent dat vrijwel niemand de hele landing page ziet. De hero sectie of eerste fold houdt mensen niet vast.

5. **Meta traffic vs organisch traffic** -- Dramatisch verschil in session duration (0-8s vs 102s). Cross-reference: dit bevestigt dat Meta traffic snel afhaakt, of dat GA4 session tracking niet correct werkt voor Meta referrals.

## 6. Cross-Referencing Analyse

| Pattern | Signaal | Interpretatie |
|---------|---------|---------------|
| H11: Mid CTR (1.64%) + 0.9s session | Ad-page partial mismatch | Hook trekt juiste klik, maar LP levert niet wat de ad belooft |
| H12: Hoge CTR (2.94%) + laag CPC + 7.6s session | Beste match | Ad en LP sluiten het best aan; efficiëntste variant |
| H13: Mid CTR + 0s session + 2 ATC's | Inconsistent | Conversies ondanks lage engagement, mogelijk tracking artefact |
| High /booking rate (22.8%) + 100% bounce | Tracking issue | Navigatie naar /booking BEWIJST engagement, maar GA4 registreert het niet |
| Rising frequency (1.79 7d) + steady CTR | Nog geen fatigue | Frequency is acceptabel maar moet gemonitord worden |

## 7. Top 3 Acties voor Vandaag

### 1. FIX GA4 Engagement Tracking (Escalatie: Rood)
**Wat:** Onderzoek en repareer waarom GA4 0% engagement rate en 100% bounce rate rapporteert terwijl er navigatie plaatsvindt.
**Waarom:** 100% bounce rate op een dag met 21 /booking bezoeken en 2 booking completes is onmogelijk. Zonder werkende analytics vlieg je blind.
**Hoe:** Check in Wix of de GA4 tag correct vuurt op alle pages (niet alleen landing). Verifieer dat de GA4 measurement ID klopt en dat enhanced measurement aan staat. Test met GA4 DebugView.
**Verwachte impact:** Betrouwbare data voor alle toekomstige optimalisaties.

### 2. Budget Herverdelen: H11 Beperken, H12 Opschalen (Escalatie: Geel)
**Wat:** Verlaag H11 budget aandeel van 56% naar ~25%. Verhoog H12 aandeel.
**Waarom:** H11 CPC (\EUR0.81) is 2x die van H12 (\EUR0.41). H12 heeft hoogste CTR (2.94%) en langste session duration. Door H11 zoveel budget te geven betaal je te veel per bezoeker.
**Hoe:** In Meta Ads Manager: pas de CBO structuur aan of splits naar aparte budgets per ad set. Overweeg H11 ad set budget cap in te stellen.
**Verwachte impact:** CPC daling richting \EUR0.50 target, meer efficiënte clicks.

### 3. Landing Page Hero Sectie Evalueren (Escalatie: Oranje)
**Wat:** Analyseer waarom slechts 3.1% van bezoekers voorbij 90% scrollt.
**Waarom:** 96.9% van bezoekers ziet de onderste secties van de LP niet. De hero/first fold moet sterker, of de scroll motivatie ontbreekt.
**Hoe:** Check de LP in mobiele view (waar Meta traffic vandaan komt). Evalueer of de hero sectie een duidelijke "waarom doorlezen" geeft. Overweeg een anchor link of scroll indicator toe te voegen.
**Verwachte impact:** Hogere scroll depth leidt tot meer exposure aan social proof en CTA's lager op de pagina.

---

*Rapport gegenereerd op 13 april 2026 | Data bronnen: Meta Ads MCP (Pipeboard), GA4 (property 528249861) | Campagne: 2026: SYBB (act_567892422940728)*
