# SYBB Daily Report -- 9 april 2026

## 1. Samenvatting

**Dag 2 na heractivatie toont sterke verbetering.** CTR is meer dan verdubbeld (3.33% vs 1.48% op dag 1), CPC is gedaald naar €0.35 (vs €0.41). Drie nieuwe ad variants zijn actief naast H14: H12 (CPC €0.29, 2 add-to-carts!), H15 (CTR 6.37%, laagste CPC €0.23), en H13 (net gestart, nog geen data). Totale spend €56.18 voor 82 link clicks en 62 landing page views. Daarnaast zijn 4 nieuwe ad sets aangemaakt (Kopie 1-4) voor individuele variant testing, maar deze hadden nog geen significante spend op dag 1. Het algoritme optimaliseert duidelijk beter op dag 2. PostHog landing page data is niet beschikbaar vanwege authenticatie; GA4/PostHog metrics ontbreken in dit rapport.

## 2. Meta Ads Performance

### Campagne Status: ACTIEF (dag 2 na heractivatie)

| Metric | 9 april | 8 april | Verandering | Target |
|--------|---------|---------|-------------|--------|
| Spend | €56.18 | €62.28 | ↓ -10% | - |
| Impressions | 4.867 | 10.366 | ↓ -53% | - |
| Clicks | 162 | 153 | → +6% | - |
| CTR | 3.33% | 1.48% | ↑ +125% | - |
| CPC | €0.35 | €0.41 | ↑ verbeterd | <€0.50 |
| Link Clicks | 82 | 80 | → +2.5% | - |
| LP Views | 62 | 56 | ↑ +11% | - |
| Frequency | 1.62 | 1.18 | ↑ +37% | <3.0 |
| Video Views | 1.074 | 1.649 | ↓ -35% | - |
| Reach | 3.004 | 7.828 | ↓ -62% | - |
| Add to Cart | 2 | 0 | ↑ nieuw! | - |
| View Content | 4 | 0 | ↑ nieuw! | - |
| Post Reactions | 24 | - | - | - |
| Post Saves | 3 | - | - | - |

**Analyse:** Minder impressions maar meer clicks en LP views op minder spend. Meta's algoritme levert aan een beter geoptimaliseerd publiek. De daling in impressions (-53%) bij stijging in CTR (+125%) is een gezond teken: kwaliteit boven kwantiteit.

### Ad Variant Performance (9 april)

| Ad (utm_content) | Spend | Impressions | Clicks | CTR | CPC | Link Clicks | LP Views | Frequency | Pixel Events |
|-------------------|-------|-------------|--------|-----|-----|-------------|----------|-----------|--------------|
| **H14,B3,CTA5** | €39.48 | 3.651 | 102 | 2.79% | €0.39 | 58 | 41 | 1.34 | 3 view_content |
| **H12,B3,CTA5** | €14.37 | 1.058 | 50 | 4.73% | €0.29 | 20 | 18 | 1.94 | 2 add_to_cart, 1 view_content |
| **H15,B3,CTA5** | €2.32 | 157 | 10 | 6.37% | €0.23 | 4 | 3 | 1.34 | - |
| **H13,B3,CTA5** | €0.01 | 1 | 0 | 0% | - | 0 | 0 | 1.00 | - |

**Beste variant: H15,B3,CTA5** -- Hoogste CTR (6.37%) en laagste CPC (€0.23), maar met slechts 157 impressions is dit nog niet statistisch significant. Veelbelovend startpunt.

**Verrassende performer: H12,B3,CTA5** -- Op dag 1 al 2 add-to-cart events! Dit is de eerste keer dat add-to-cart events getriggerd worden sinds de heractivatie. CTR (4.73%) en CPC (€0.29) zijn beide sterk. H12 verdient meer budget.

**Werkpaard: H14,B3,CTA5** -- Krijgt 70% van het budget (€39.48/€56.18). CTR verbeterd van 1.48% (8 apr) naar 2.79% (9 apr). Nog steeds de laagste CTR van de actieve varianten, maar het meeste volume.

**Inactief: H13,B3,CTA5** -- Slechts 1 impressie. Effectief niet aan het draaien. In het originele ad set is H13 gepauzeerd; de versie in Kopie 3 is actief maar net aangemaakt (16:26).

### Nieuwe Ad Set Structuur (aangemaakt 9 april, 16:26)

Er zijn 4 nieuwe ad sets aangemaakt voor individuele variant testing:

| Ad Set | Actieve Ad | Status | Targeting |
|--------|-----------|--------|-----------|
| BATCH 2: Expertise & POC (origineel) | H14, H12*, H15* | Actief | NL, BE, LU, DE, 18-65 |
| Kopie 1 | H11,B3,CTA5 | Actief | NL, BE, LU, DE, 18-65 |
| Kopie 2 | H12,B3,CTA5 | Actief | NL, BE, LU, DE, 18-65 |
| Kopie 3 | H13,B3,CTA5 | Actief | NL, BE, LU, DE, 18-65 |
| Kopie 4 | H15,B3,CTA5 | Actief | NL, BE, LU, DE, 18-65 |

*H12 en H15 zijn gepauzeerd in het originele ad set maar hebben gisteren nog spend gehad voordat ze gepauzeerd werden (rond 16:30).*

**LET OP:** H11 is nu ook actief via Kopie 1. Dit was de aanbeveling van gisteren (#1 actie). De historisch beste lead converter draait nu weer.

### Ad Set Performance (9 april)

| Ad Set | Spend | CPC | CTR | Frequency |
|--------|-------|-----|-----|-----------|
| BATCH 2: Expertise & POC | €56.18 | €0.35 | 3.33% | 1.62 |
| Kopie 1-4 | €0.00 | - | - | - |

*De Kopie ad sets zijn laat op de dag aangemaakt en hadden nog geen significante spend.*

## 3. Landing Page Health

**PostHog data niet beschikbaar** -- PostHog MCP vereist authenticatie die niet voltooid is. Landing page metrics (bounce rate, scroll depth, sessieduur, CTA clicks) ontbreken in dit rapport.

| Metric | 9 april | 8 april | Target | Status |
|--------|---------|---------|--------|--------|
| Bounce Rate | n/a | 100% | <55% | -- |
| Avg Session Duration | n/a | 6.0s | >90s | -- |
| Scroll 25% | n/a | n/a | >80% | -- |
| Scroll 50% | n/a | n/a | >60% | -- |
| Scroll 75% | n/a | n/a | >40% | -- |
| Scroll 100% | n/a | n/a | >20% | -- |
| CTA Click Rate | n/a | 9.3% | >4% | -- |

### UTM Segmentation

Niet beschikbaar zonder PostHog/GA4 data.

## 4. Funnel Drop-off

### Meta Ads Funnel (beschikbare data)

```
Impressions (100%)  -->  Clicks (3.33%)  -->  Link Clicks (1.68%)  -->  LP Views (1.27%)  -->  Add to Cart (0.04%)
   4.867                    162                   82                      62                      2
```

**Drop-off analyse:**
- Impressions naar Clicks: 96.7% verlies (normaal voor video ads)
- Clicks naar Link Clicks: 49.4% van clicks zijn link clicks (rest is engagement: likes, saves, video views)
- Link Clicks naar LP Views: 75.6% van link clicks resulteert in LP view (24.4% verlies door slow loading of direct terugkeren)
- LP Views naar Add to Cart: 3.2% van LP views naar add-to-cart (beide via H12)

**Vergelijking met 8 april:**
- LP View rate (LP views / link clicks): 75.6% (9 apr) vs 70.0% (8 apr) -- verbeterd
- Add to cart: 2 (9 apr) vs 0 (8 apr) -- eerste conversies!

**Grootste lek:** LP Views naar conversie. 62 LP views resulteren in slechts 2 add-to-carts (3.2%). Maar dit is al beter dan dag 1 (0%). De landing page blijft het kritieke knelpunt.

## 5. Rode Vlaggen 🚩

1. **GEEN POSTHOG DATA BESCHIKBAAR** -- Authenticatie niet voltooid. Zonder landing page analytics (bounce rate, scroll depth, sessieduur) vliegen we blind op LP performance. Fix dit als eerste prioriteit.

2. **H14 DOMINEERT BUDGET (70%)** -- H14 krijgt €39.48 van €56.18, terwijl het de laagste CTR (2.79%) en hoogste CPC (€0.39) heeft van alle actieve varianten. Meta's algoritme verdeelt op basis van historische data, maar H12 en H15 laten betere metrics zien.

3. **FREQUENCY STIJGING H12 (1.94)** -- H12 heeft al 1.94 frequency op dag 1. Dit is hoog voor een nieuwe ad variant. Klein bereik (544 unieke mensen) kan leiden tot snelle ad fatigue als het publiek niet uitgebreid wordt.

4. **H13 DRAAIT NIET** -- Slechts 1 impressie. De ad is gepauzeerd in het originele ad set. De versie in Kopie 3 is net actief maar krijgt geen levering.

5. **KOPIE AD SETS NOG GEEN DATA** -- De 4 nieuwe ad sets zijn laat op de dag aangemaakt. Er is nog geen performance data beschikbaar. Monitor morgen of ze levering krijgen.

6. **COST PER LP VIEW BLIJFT HOOG** -- €0.91 per LP view (€56.18 / 62 views). Bij een conversiepercentage van 3.2% (add-to-cart) kost elke add-to-cart €28.09. Zonder data over daadwerkelijke bookings is ROI onduidelijk.

## 6. Top 3 Acties voor Vandaag

### 1. Voltooi PostHog authenticatie
- **Wat:** Completeer de PostHog OAuth flow zodat landing page data beschikbaar is.
- **Waarom:** Twee dagen op rij geen LP metrics. Bounce rate, scroll depth en sessieduur zijn essentieel om te begrijpen waarom 62 LP views slechts 2 add-to-carts opleveren. Het verschil met dag 1 (0 conversies) is bemoedigend, maar we weten niet wat er op de pagina gebeurt.
- **Hoe:** Open de PostHog autorisatie URL in de browser en voltooi de OAuth flow.
- **Verwachte impact:** Volledige funnel visibility voor het morning report van morgen.
- **Escalatie:** Groen (zelf uit te voeren)

### 2. Monitor de nieuwe ad set structuur (Kopie 1-4)
- **Wat:** Check of alle 4 Kopie ad sets levering krijgen. Specifiek: krijgen H11 (Kopie 1), H12 (Kopie 2), H13 (Kopie 3), en H15 (Kopie 4) impressions?
- **Waarom:** De ad sets zijn gistermiddag aangemaakt maar hadden nog geen spend. Als ze na 24u nog steeds geen levering hebben, kan er een budget- of biedingsprobleem zijn. De hele A/B test strategie hangt af van gelijke verdeling.
- **Hoe:** Meta Ads Manager > 2026: SYBB > controleer delivery status per ad set. Zorg dat het campagnebudget (€100/dag) hoog genoeg is voor 5 ad sets.
- **Verwachte impact:** Gelijke verdeling betekent ~€20/ad set/dag, genoeg voor 40-50 LP views per variant per dag.
- **Escalatie:** Geel (Robin goedkeuring als budget aanpassing nodig is)

### 3. Overweeg budget herverdeling richting H12
- **Wat:** Geef H12 meer budget ten koste van H14, of wacht tot de Kopie ad sets data genereren.
- **Waarom:** H12 heeft op dag 1 al 2 add-to-cart events, CTR 4.73% en CPC €0.29. H14 heeft na 2 dagen 0 add-to-carts, CTR 2.79% en CPC €0.39. Historisch was H12 ook een sterke performer. De signalen zijn consistent.
- **Hoe:** Optie A: Wacht 2-3 dagen op data van de Kopie ad sets voor een eerlijke vergelijking. Optie B: Pauzeer H14 in het originele ad set en laat alleen de Kopie sets draaien voor een schone A/B test.
- **Verwachte impact:** Betere budget allocatie kan CPC verlagen naar <€0.30 en add-to-cart rate verhogen.
- **Escalatie:** Geel (Robin goedkeuring, strategische keuze)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| Ad CTR vs LP Performance | CTR verdubbeld naar 3.33%, maar zonder PostHog data weten we niet of LP engagement ook verbeterd is. |
| H12 vs H14 | H12 (CTR 4.73%, CPC €0.29, 2 add-to-carts) outperformt H14 (CTR 2.79%, CPC €0.39, 0 conversies) op alle metrics. |
| H15 early signal | CTR 6.37% en CPC €0.23 zijn uitstekend, maar 157 impressions is te weinig om conclusies te trekken. |
| Frequency risk | H12 frequency 1.94 op dag 1 is hoog. Bij klein publiek (544 reach) kan dit snel stijgen naar >3.0. |
| Budget verdeling | Meta geeft H14 70% van het budget ondanks slechtere metrics. De Kopie ad set structuur kan dit probleem oplossen door elke variant een eigen ad set te geven. |
| Eerste conversies | 2 add-to-carts en 4 view_content events zijn de eerste pixel events sinds heractivatie. Het begin van een conversie trail. |

---

### KPI Dashboard vs Targets

| KPI | 9 april | 8 april | Target 30d | Status |
|-----|---------|---------|-----------|--------|
| LP Bounce Rate | n/a (PostHog) | 100% | <55% | -- |
| LP Conversie Rate | 3.2% (add-to-cart) | 0% | >5% | 🟡 |
| Avg Scroll Depth | n/a (PostHog) | n/a | >60% | -- |
| CTA Click Rate | n/a (PostHog) | 9.3% | >4% | -- |
| Meta CPC | €0.35 | €0.41 | <€0.50 | 🟢 |
| Cost per LP View | €0.91 | €1.11 | - | ↑ verbeterd |
| Time on Page | n/a (PostHog) | 6.0s | >90s | -- |

---

*Rapport gegenereerd: 10 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard)*
*PostHog data: NIET BESCHIKBAAR (authenticatie vereist)*
*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*Status: ACTIEF (dag 2 na heractivatie) | Actieve ads: H14, H12, H15 (origineel ad set) + H11, H12, H13, H15 (Kopie 1-4)*
*Nieuwe structuur: 5 ad sets, 4 Kopie ad sets aangemaakt op 9 april voor individuele variant A/B testing*
