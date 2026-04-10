# SYBB Daily Report -- 9 april 2026

## 1. Samenvatting

**Dag 2 van de heractivering, campagne gepauzeerd om 16:24.** Drie nieuwe ad variants (H12, H13, H15) gelanceerd naast H14. De campagne werd efficienter: CTR steeg van 1.48% naar 3.33% en CPC daalde van €0.41 naar €0.35 terwijl de spend lager lag (€56.18 vs €62.28). H12 springt eruit met de hoogste CTR (4.73%) en laagste CPC (€0.29). Twee add-to-cart events geregistreerd voor het eerst. GA4 toont 103 sessies met een gemiddelde sessieduur van 45.4s (7.5x beter dan gisteren), maar bounce rate blijft 100%. Er waren 8 /booking visits (7.8% van sessies). De UTM inconsistentie (komma's vs underscores) is nog steeds niet opgelost en splitst de data.

## 2. Meta Ads Performance

### Campagne Status: GEPAUZEERD (gepauzeerd 9 april 16:24, na heractivering op 8 april)

| Metric | 9 april | 8 april | 7d Gem. | Trend vs 8 apr |
|--------|---------|---------|---------|----------------|
| Spend | €56.18 | €62.28 | €16.97 | ↓ (-10%) |
| Impressions | 4.867 | 10.366 | 2.185 | ↓ (-53%) |
| Clicks | 162 | 153 | 45 | → (+6%) |
| CTR | 3.33% | 1.48% | 2.06% | ↑ (+125%) |
| CPC | €0.35 | €0.41 | €0.38 | ↑ (-15%) |
| Link Clicks | 82 | 80 | 23 | → (+3%) |
| LP Views | 62 | 56 | 17 | ↑ (+11%) |
| Frequency | 1.62 | 1.18 | 1.37 | → |
| Video Views | 1.074 | 1.649 | 390 | ↓ (-35%) |
| Add to Cart | 2 | 0 | 0.3 | ↑ (nieuw!) |
| Leads | 0 | 0 | 0 | → |

*7d gemiddelde = cumulatief 3-9 april / 7 dagen. Campagne was alleen actief op 8-9 april.*

### Ad Variant Performance (9 april)

| Ad (utm_content) | Impressions | Clicks | CTR | CPC | Link Clicks | LP Views | Spend | Add to Cart |
|-------------------|-------------|--------|-----|-----|-------------|----------|-------|-------------|
| **H14,B3,CTA5** | 3.651 | 102 | 2.79% | €0.39 | 58 | 41 | €39.48 | 0 |
| **H12,B3,CTA5** | 1.058 | 50 | 4.73% | €0.29 | 20 | 18 | €14.37 | 2 |
| **H15,B3,CTA5** | 157 | 10 | 6.37% | €0.23 | 4 | 3 | €2.32 | 0 |
| H13,B3,CTA5 | 1 | 0 | 0% | - | 0 | 0 | €0.01 | 0 |

**Beste variant:** H12,B3,CTA5. Hoogste CTR na H15 (4.73%), laagste CPC na H15 (€0.29), en de enige variant met add-to-cart conversies (2x). Met meer volume dan H15 is dit de meest betrouwbare performer.

**Veelbelovend:** H15,B3,CTA5 toont de hoogste CTR (6.37%) en laagste CPC (€0.23), maar met slechts 157 impressies is het nog te vroeg voor conclusies.

**Worst performer:** H13,B3,CTA5 kreeg vrijwel geen distributie (1 impressie). Het algoritme heeft deze variant direct verworpen.

**Budget allocatie:** H14 krijgt 70% van het budget (€39.48 van €56.18). Meta's algoritme favoriseert H14 qua volume, maar H12 levert betere efficiency.

### Ad Set Performance (9 april)

| Ad Set | Spend | CPC | CTR | Frequency | Link Clicks |
|--------|-------|-----|-----|-----------|-------------|
| BATCH 2: Expertise & POC | €56.18 | €0.35 | 3.33% | 1.62 | 82 |

## 3. Landing Page Health (GA4 Data)

| Metric | 9 april | 8 april | 7d Gem. | Target | Status |
|--------|---------|---------|---------|--------|--------|
| Pageviews | 120 | 80 | 34.6/dag | - | ↑ (+50%) |
| Unique Visitors | 100 | 74 | 29.1/dag | - | ↑ (+35%) |
| Sessions | 103 | 75 | 29.7/dag | - | ↑ (+37%) |
| Bounce Rate | 100% | 100% | 95.2% | <55% | 🔴 |
| Avg Session Duration | 45.4s | 6.0s | 35.8s | >90s | 🔴 |
| Scroll Events | 10 (9.7%) | 0 | 1.9/dag | >60% | 🔴 |
| Click Events | 4 (3.9%) | 0 | 0.6/dag | >4% | 🟡 |
| /booking Visits | 8 (7.8%) | 7 (9.3%) | 1.1/dag | >4% | 🟢 |
| Product Page Visits | 5 | - | - | - | nieuw |

**Positief:** Sessieduur sprong van 6.0s naar 45.4s. Bezoekers blijven significant langer. Scroll events (10) en click events (4) worden nu geregistreerd.

**Negatief:** Bounce rate blijft 100% ondanks 45.4s sessieduur en 10 scroll events. Dit bevestigt een GA4 configuratie-issue: GA4 telt engaged sessions alleen bij >10s + user_engagement event. De Wix site vurt mogelijk geen user_engagement events correct.

### UTM Content Breakdown (9 april, GA4)

| Bron (utm_content) | Sessions | Bounce | Avg Duration | PVs |
|--------------------|----------|--------|--------------|-----|
| H14,B3,CTA5 | 39 | 100% | 48.3s | 47 |
| (leeg/direct) | 22 | 100% | 108.6s | 18 |
| H12,B3,CTA5 | 16 | 100% | 22.6s | 17 |
| h14_b3_cta5 | 7 | 100% | 0s | 7 |
| h15_b3_cta5 | 7 | 100% | 0s | 7 |
| h11_b3_cta5 | 6 | 100% | 0s | 6 |
| h12_b3_cta5 | 6 | 100% | 0s | 6 |
| h13_b3_cta5 | 6 | 100% | 3.3s | 6 |
| (not set) | 3 | 100% | 7.9s | 4 |
| H15,B3,CTA5 | 2 | 100% | 0s | 2 |

**UTM Inconsistentie (nog steeds!):** Twee formaten actief:
- `H14,B3,CTA5` (komma's, mixed case) = 39+16+2 = 57 sessies
- `h14_b3_cta5` (underscores, lowercase) = 7+7+6+6+6 = 32 sessies

De underscore-varianten tonen 0s sessieduur, wat suggereert dat deze vanuit een andere tracking flow komen (mogelijk oude links of redirect issues). Dit splitst de data en maakt analyse onbetrouwbaar.

**Gecombineerde UTM data per variant:**
| Variant | Totaal Sessions | Meta LP Views | Match |
|---------|----------------|---------------|-------|
| H14 | 46 (39+7) | 41 | ~112% |
| H12 | 22 (16+6) | 18 | ~122% |
| H15 | 9 (7+2) | 3 | ~300% |
| H13 | 6 | 0 | n.v.t. |
| H11 | 6 | n.v.t. (niet actief) | oud verkeer |

H15 toont 9 GA4 sessies vs 3 Meta LP views. Dit grote verschil duidt op vertraagde attributie of gecachte UTMs van eerdere bezoeken.

### Cross-Reference: Ad Performance vs LP Engagement

| Variant | Meta CTR | Meta CPC | GA4 Avg Duration | GA4 Sessions |
|---------|----------|----------|------------------|-------------|
| H14 | 2.79% | €0.39 | 48.3s | 46 |
| H12 | 4.73% | €0.29 | 22.6s | 22 |
| H15 | 6.37% | €0.23 | 0s* | 9 |
| H13 | 0% | - | 3.3s | 6 |

*H15 GA4 duration 0s is waarschijnlijk een tracking artifact (te weinig data + UTM inconsistentie)

**Insight:** H14 heeft de langste on-page tijd (48.3s) ondanks lagere CTR. H12 trekt meer clicks maar bezoekers blijven korter (22.6s). Dit suggereert dat H14's hook beter aansluit bij de LP content, terwijl H12 bredere interesse wekt maar minder gerichte bezoekers trekt.

## 4. Funnel Drop-off

### 9 april (103 sessies)

```
LP Pageview (/)     -->   Scroll Event    -->   /booking Visit    -->   Product Page     -->   Add to Cart
  98 sessies (100%)        10 users (10.2%)       8 sessies (8.2%)       5 sessies (5.1%)       2 events (2.0%)
       |                        |                       |                       |                      |
       v                        v                       v                       v                      v
  88 verloren (89.8%)     2 naar booking (20%)     3 naar product (37.5%)    onbekend               0 leads
```

**Grootste lek:** LP naar Scroll (89.8% drop-off). Slechts 10% van bezoekers scrollt voorbij de GA4 scroll threshold. De hero section of first fold overtuigt niet genoeg om door te scrollen.

**Positief:** Van de bezoekers die /booking bereiken, gaat 62.5% verder naar een product pagina. En er zijn 2 add-to-cart events (eerste keer!).

**Nog steeds: 0 leads.** De volledige funnel van ad klik tot daadwerkelijke boeking converteert niet. De bottleneck zit nu verdeeld over twee punten:
1. LP hero/first fold (90% verlies)
2. Product pagina naar boeking (add to cart maar geen checkout)

### Vergelijking met 8 april

| Funnel Stap | 8 april | 9 april | Trend |
|-------------|---------|---------|-------|
| LP Sessions | 75 | 98 | ↑ (+31%) |
| /booking | 7 (9.3%) | 8 (8.2%) | → (percentage stabiel) |
| Product Page | - | 5 (5.1%) | nieuw |
| Add to Cart | 0 | 2 (2.0%) | ↑ (nieuw!) |
| Leads | 0 | 0 | → |

## 5. Rode Vlaggen 🚩

1. **100% BOUNCE RATE (dag 2)** -- Bounce rate blijft 100% ondanks 45.4s sessieduur. Dit is bijna zeker een GA4 configuratie-issue. De `user_engagement` event vurt niet correct op de Wix site. Zonder fix is deze metric waardeloos.

2. **CAMPAGNE WEER GEPAUZEERD** -- Na slechts 2 dagen actief (8-9 april) is de campagne weer gepauzeerd. Dit onderbreekt de learning phase van het Meta algoritme. Elke pauze reset deels het optimalisatieproces. De campagne had minimaal 7 dagen ononderbroken moeten draaien.

3. **UTM INCONSISTENTIE (dag 10 onopgelost)** -- Mix van `H14,B3,CTA5` en `h14_b3_cta5` gesignaleerd sinds 31 maart. Splitst 36% van de sessies (32 van 89 UTM-getagde sessies) naar het verkeerde format. Maakt cross-referencing onbetrouwbaar.

4. **0 LEADS NA 2 DAGEN EN €118.46 SPEND** -- Twee dagen actief, €118.46 totale spend, 0 leads. De cost per lead is effectief oneindig. De 2 add-to-cart events zijn een eerste signaal maar nog geen conversie.

5. **H13 KRIJGT GEEN DISTRIBUTIE** -- H13,B3,CTA5 kreeg slechts 1 impressie. Het algoritme verwerpt deze variant volledig. Evalueer of de creative/hook dusdanig verschilt dat het een eerlijke kans verdient, of verwijder om budget te concentreren.

6. **SCROLL RATE 10%** -- Slechts 10 van 98 LP bezoekers scrollde voorbij de threshold. De hero/above-the-fold content houdt 90% van bezoekers niet vast.

## 6. Top 3 Acties voor Vandaag

### 1. Heractiveer de campagne en laat hem minimaal 7 dagen draaien
- **Wat:** Zet de campagne weer aan en pauzeer niet opnieuw tot minimaal 16 april.
- **Waarom:** Twee keer pauzeren in 2 dagen saboteert de learning phase. Meta's algoritme heeft 7+ ononderbroken dagen nodig om te optimaliseren. De dag-2 data toont al verbetering: CTR +125%, CPC -15%, sessieduur +656%. Dit zijn positieve signalen die tijd nodig hebben.
- **Hoe:** Meta Ads Manager > 2026: SYBB > Campaign activeren.
- **Verwachte impact:** Stabielere delivery, lagere CPC door learning phase completion, betrouwbaardere data.
- **Escalatie:** Geel (Robin goedkeuring nodig)

### 2. Fix UTM tags naar consistent lowercase format
- **Wat:** Update alle ad URL parameters naar `utm_content=h14_b3_cta5` format (lowercase, underscores).
- **Waarom:** Al 10 dagen onopgelost. Splitst 36% van sessies naar verkeerd format. Maakt cross-referencing tussen Meta Ads en GA4 onbetrouwbaar. Zonder fix is het onmogelijk om variant performance accuraat te meten.
- **Hoe:** Meta Ads Manager > 2026: SYBB > elke ad > URL Parameters > wijzig naar lowercase underscores.
- **Verwachte impact:** Schone data vanaf morgen. Accurate variant-level analyse mogelijk.
- **Escalatie:** Groen (zelf uit te voeren, geen impact op delivery)

### 3. Onderzoek en fix GA4 engagement tracking op Wix
- **Wat:** Diagnosticeer waarom GA4 0 engaged sessions rapporteert terwijl sessieduur 45.4s is en er scroll/click events zijn.
- **Waarom:** 100% bounce rate maakt de belangrijkste LP health metric waardeloos. Zonder betrouwbare engagement data is het onmogelijk om LP optimalisatie te prioriteren.
- **Hoe:** (1) Check GA4 > Admin > Data Streams > Enhanced Measurement (scroll, outbound clicks, site search moeten aan staan), (2) Controleer of de Wix GA4 integratie `user_engagement` events correct stuurt, (3) Overweeg een custom event voor "engaged visit" (>10s op pagina).
- **Verwachte impact:** Betrouwbare bounce rate en engagement metrics. Basis voor LP optimalisatie.
- **Escalatie:** Oranje (Wix Editor + GA4 configuratie nodig)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| Ad CTR vs LP Bounce | CTR steeg naar 3.33% (van 1.48%), bounce blijft 100%. Meer en betere clicks, maar LP engagement tracking is stuk. De 45.4s sessieduur suggereert dat bounce rate niet klopt. |
| Ad CPC vs LP Conversie | CPC daalde naar €0.35 (van €0.41). 2 add-to-cart events (eerste keer), maar nog 0 leads. Positieve trend in efficiency. |
| H12 CTR vs LP Duration | H12 heeft hoogste CTR (4.73%) maar kortste LP sessieduur (22.6s). Trekt clicks maar houdt bezoekers minder vast dan H14 (48.3s). Mogelijke ad-page mismatch bij H12. |
| Frequency vs Performance | Frequency 1.62 (van 1.18). Nog ver onder de 3.0 fatigue drempel. Audience is niet verzadigd. |
| Meta LP Views vs GA4 Sessions | Meta: 62 LP views. GA4: 89 getagde sessies + 22 direct = 111 sessies. GA4 telt meer sessies, deels door UTM duplicatie en direct verkeer. |
| Learning Phase voortgang | Dag 2 toont verbetering op alle key metrics: CTR +125%, CPC -15%, LP views +11%. Het algoritme optimaliseert, maar pauze onderbreekt dit proces. |

---

### KPI Dashboard vs Targets

| KPI | 9 april | 8 april | Target 30d | Status |
|-----|---------|---------|-----------|--------|
| LP Bounce Rate | 100% | 100% | <55% | 🔴 (tracking issue) |
| LP Conversie Rate | 0% (0 leads / 62 LP views) | 0% | >5% | 🔴 |
| Scroll Rate | 10.2% | 0% (geen data) | >60% | 🔴 |
| CTA Click Rate | 7.8% (/booking visits) | 9.3% | >4% | 🟢 |
| Meta CPC | €0.35 | €0.41 | <€0.50 | 🟢 |
| Meta CTR | 3.33% | 1.48% | - | ↑ |
| Time on Page | 45.4s | 6.0s | >90s | 🟡 (sterk verbeterd) |
| Add to Cart | 2 | 0 | - | ↑ (nieuw!) |

---

*Rapport gegenereerd: 10 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard), Google Analytics 4 (property 528249861, SYBB)*
*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*Status: GEPAUZEERD (gepauzeerd 9 april 16:24) | Actieve ads: H12, H13, H14, H15 (Ad Set: BATCH 2)*
*Opmerking: PostHog MCP niet beschikbaar, GA4 gebruikt als landing page analytics bron*
