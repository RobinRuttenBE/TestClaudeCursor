# SYBB Daily Report -- 8 april 2026

## 1. Samenvatting

**De SYBB campagne is HERACTIVEERD op 8 april na 31 dagen pauze.** Alleen H14,B3,CTA5 draait in Ad Set "BATCH 2: Expertise & POC". Eerste dag resultaten: €62.28 spend, 10.366 impressions, 80 link clicks en 56 landing page views. CPC is €0.41 (onder target van €0.50, maar 3.2x hoger dan het historische gemiddelde van €0.13). Dit is verwacht tijdens de learning phase. GA4 bevestigt 80 pageviews en 75 sessies, een 20x stijging t.o.v. het 7d gemiddelde. Kritiek punt: 100% bounce rate met slechts 6.0s gemiddelde sessieduur. Toch 7 /booking visits (9.3% van sessies), wat suggereert dat sommige bezoekers wel converteren ondanks de bounce-classificatie.

## 2. Meta Ads Performance

### Campagne Status: ACTIEF (heractiveerd 8 april 2026)

| Metric | 8 april | Historisch Gem. (~55d) | Target | Trend |
|--------|---------|----------------------|--------|-------|
| Spend | €62.28 | €24.07/dag | - | ↑ |
| Impressions | 10.366 | 3.438/dag | - | ↑ |
| Clicks | 153 | 181/dag | - | → |
| CTR | 1.48% | 5.27% | - | ↓ |
| CPC | €0.41 | €0.13 | <€0.50 | ↓ |
| Link Clicks | 80 | 176/dag | - | ↓ |
| LP Views | 56 | 112/dag | - | ↓ |
| Frequency | 1.18 | 2.07 | <3.0 | ↑ |
| Video Views | 1.649 | - | - | - |
| Leads | 0 | 0.27/dag | - | ↓ |

*Opmerking: Vergelijking is met het historische gemiddelde (jan-mrt). Er is geen 7d gemiddelde beschikbaar omdat de campagne pas op 8 april heractiveerd is.*

### Actieve Ad Variants

Momenteel draait er slechts 1 ad variant:

| Ad (utm_content) | Impressions | Clicks | CTR | CPC | Link Clicks | LP Views | Cost/LP View |
|-------------------|-------------|--------|-----|-----|-------------|----------|-------------|
| H14,B3,CTA5 | 10.366 | 153 | 1.48% | €0.41 | 80 | 56 | €1.11 |

**Enige variant:** H14,B3,CTA5 is de enige actieve ad. Historisch was dit niet de beste performer:
- H11 had de laagste cost per lead (€33.75, 6 leads)
- H13 had de hoogste CTR (9.82%) en laagste CPC (€0.07)
- H14 had lifetime: CTR 3.68%, CPC €0.18, 1 lead van 357 LP views

**Huidige CTR (1.48%) ligt flink onder H14's historische CTR (3.68%)**, wat typisch is voor learning phase na een lange pauze.

### Ad Set Performance

| Ad Set | Spend | CPC | CTR | Frequency |
|--------|-------|-----|-----|-----------|
| BATCH 2: Expertise & POC | €62.28 | €0.41 | 1.48% | 1.18 |

## 3. Landing Page Health (GA4 Data)

| Metric | 8 april | 7d Gem. (1-7 apr) | Target | Status |
|--------|---------|-------------------|--------|--------|
| Pageviews | 80 | 4.0/dag | - | ↑ (20x) |
| Unique Visitors | 74 | 3.7/dag | - | ↑ (20x) |
| Sessions | 75 | 3.7/dag | - | ↑ (20x) |
| Bounce Rate | 100% | 80.8% | <55% | 🔴 |
| Avg Session Duration | 6.0s | 6.3s | >90s | 🔴 |
| Engaged Sessions | 0 | 0.7/dag | - | 🔴 |
| /booking Visits | 7 | 0.4/dag | - | ↑ (17.5x) |
| CTA Click Rate (booking/sessions) | 9.3% | 11.5% | >4% | 🟢 |

### Dagelijkse Breakdown (1-8 april, GA4)

| Datum | PVs | Users | Sessions | Bounce Rate | Avg Session | /booking |
|-------|-----|-------|----------|-------------|-------------|----------|
| 1 apr | 2 | 1 | 1 | 0% | 6.3s | - |
| 2 apr | 7 | 7 | 7 | 85.7% | 8.3s | - |
| 3 apr | 4 | 4 | 4 | 100% | 6.7s | - |
| 4 apr | 0 | 0 | 0 | - | - | - |
| 5 apr | 9 | 9 | 9 | 77.8% | 4.4s | - |
| 6 apr | 3 | 2 | 2 | 50% | 16.3s | - |
| 7 apr | 3 | 3 | 3 | 100% | 0s | - |
| **8 apr** | **80** | **74** | **75** | **100%** | **6.0s** | **7** |

### UTM Content Breakdown (8 april, GA4)

| Bron (utm_content) | Sessions | Bounce Rate | Avg Session | Engaged | PVs |
|--------------------|----------|-------------|-------------|---------|-----|
| H14,B3,CTA5 | 62 | 100% | 1.3s | 0 | 64 |
| (leeg) | 8 | 100% | 46.6s | 0 | 7 |
| (not set) | 7 | 100% | 0s | 0 | 7 |
| H15,B3,CTA5 | 1 | 100% | 0s | 0 | 1 |
| h14_b3_cta5 | 1 | 100% | 0s | 0 | 1 |

**H14 ad verkeer:** 62 sessies met gemiddeld 1.3s sessieduur. Bezoekers komen binnen maar vertrekken vrijwel direct. De landing page hero/first fold overtuigt niet.

**UTM inconsistentie:** Zowel `H14,B3,CTA5` (uppercase, komma's) als `h14_b3_cta5` (lowercase, underscores) verschijnen. Standaardiseer naar lowercase met underscores.

### Vergelijking met vorige week (1-7 april, alleen organisch)

| Bron | Sessions | Bounce | Avg Session | Engaged |
|------|----------|--------|-------------|---------|
| (not set) / direct | 13 | 92.3% | 3.3s | 1 |
| bio_link | 8 | 50% | 15.2s | 4 |
| h11_b3_cta5 (oud) | 2 | 100% | 0s | 0 |
| Overig (oud UTMs) | 3 | 100% | 0s | 0 |

**bio_link was vorige week de beste bron** (50% bounce, 15.2s sessie). Het betaalde H14 verkeer (100% bounce, 1.3s) presteert significant slechter dan het organische bio_link verkeer.

## 4. Funnel Drop-off

### 8 april (75 sessies)

```
LP Pageview (100%)  -->  /booking Visit (9.3%)
   75 sessies               7 visits
     |                        |
     v                        v
   68 verloren (90.7%)      6 unieke users
```

**Conversie naar /booking: 9.3%** (7 van 75 sessies). Dit is boven de 4% CTA click rate target, wat positief is.

Echter: **0 leads gerapporteerd** in Meta Ads. Dit betekent dat bezoekers /booking bereiken maar niet het formulier invullen.

**Grootste lek:** /booking naar lead conversie. Mensen klikken door maar voltooien de boeking niet. Mogelijke oorzaken: prijs, formulier complexiteit, of onvoldoende urgentie op de booking pagina.

### Anomalie: 100% bounce maar 7 /booking visits

GA4 classificeert alle 75 sessies als "bounced" (0 engaged sessions), maar 7 sessies bereikten wel /booking. Dit is tegenstrijdig. Mogelijke verklaringen:
1. Sessies duurden <10 seconden totaal (GA4 engaged = >10s OF 2+ pageviews OF conversie)
2. /booking wordt in dezelfde pageview geladen (SPA/iframe)
3. GA4 tracking configuratie issue

**Aanbeveling:** Controleer de GA4 engaged session definitie en de Wix tracking implementatie.

## 5. Rode Vlaggen 🚩

1. **CPC €0.41 (3.2x historisch)** -- Verwacht tijdens learning phase, maar monitor de komende 5-7 dagen. Als CPC niet daalt naar <€0.25 binnen een week, is er een fundamenteel probleem.

2. **100% BOUNCE RATE** -- Alle 75 sessies als bounced geclassificeerd. Zelfs als dit deels een tracking issue is (7 /booking visits), is 1.3s gemiddelde sessieduur voor ad verkeer alarmerend. De landing page hero sectie engageert niet.

3. **SESSIEDUUR 6.0s (93% onder target)** -- Target is >90s. Zelfs het organische verkeer (leeg UTM) met 46.6s zit ver onder target. Ad verkeer (1.3s) is extreem laag.

4. **SLECHTS 1 AD VARIANT ACTIEF** -- Alleen H14 draait. Historisch was H14 niet de top performer (H11 was de lead kampioen, H13 de volume kampioen). Geen A/B testing mogelijk met 1 variant.

5. **0 LEADS ONDANKS 7 /BOOKING VISITS** -- Mensen bereiken de booking pagina maar converteren niet. De booking pagina zelf heeft een probleem (prijs zichtbaarheid, formulier, urgentie).

6. **UTM INCONSISTENTIE PERSISTS** -- Mix van `H14,B3,CTA5` en `h14_b3_cta5`. Dit was al gesignaleerd op 31 maart. Nog niet opgelost.

7. **SCROLL TRACKING NIET FUNCTIONEEL** -- Geen scroll depth data beschikbaar in GA4. Essentieel voor het diagnosticeren van welke LP sectie bezoekers verliest.

## 6. Top 3 Acties voor Vandaag

### 1. Activeer H11 als tweede ad variant
- **Wat:** Voeg H11,B3,CTA5 toe aan de actieve rotation naast H14.
- **Waarom:** H11 was historisch de beste lead converter (€33.75 per lead, 6 van 15 totale leads). Met alleen H14 is er geen A/B testing en mis je de sterkste lead-variant. H14 had historisch slechts 1 lead.
- **Hoe:** Meta Ads Manager > 2026: SYBB > BATCH 2 > H11,B3,CTA5 activeren. Budget evenredig verdelen.
- **Verwachte impact:** Betere lead conversie en benchmarkdata om te vergelijken. Historisch 4x betere cost per lead dan H14.
- **Escalatie:** Geel (Robin goedkeuring nodig)

### 2. Onderzoek LP bounce/engagement probleem
- **Wat:** Diagnosticeer waarom 100% van het ad verkeer bounced met 1.3s sessieduur, en waarom 7 /booking bezoekers niet converteren naar leads.
- **Waarom:** De LP verliest bezoekers in de eerste 2 seconden. Dit is het kritieke bottleneck. Zonder LP fix is elke ad spend weggegooid geld (€62.28 = 0 leads).
- **Hoe:** (1) Check LP laadsnelheid op mobiel (is de pagina traag?), (2) Vergelijk de H14 ad belofte met de LP hero sectie (mismatch?), (3) Check of het booking formulier correct werkt en of de prijs duidelijk is, (4) Fix scroll tracking in GA4 om te zien waar bezoekers afhaken.
- **Verwachte impact:** Identificatie van het exacte probleem. Oplossing kan bounce rate halveren en lead conversie verveelvoudigen.
- **Escalatie:** Oranje (Wix Editor + GA4 configuratie nodig)

### 3. Fix scroll tracking en UTM consistentie
- **Wat:** (1) Implementeer scroll depth tracking in GA4 (25/50/75/100%), (2) Update alle ad UTMs naar lowercase format (h14_b3_cta5).
- **Waarom:** Zonder scroll data is het onmogelijk te bepalen welke LP sectie faalt. UTM inconsistentie bemoeilijkt cross-referencing al sinds 31 maart.
- **Hoe:** (1) GA4 > Enhanced Measurement > controleer scroll tracking enabled, (2) Meta Ads Manager > alle ads > update URL parameters naar lowercase.
- **Verwachte impact:** Volledige funnel visibility vanaf morgen. Betrouwbare data matching tussen Meta Ads en GA4.
- **Escalatie:** Groen (zelf uit te voeren via GA4 + Meta Ads Manager)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| Ad CTR vs LP Bounce | CTR 1.48% (laag) + 100% bounce = traffic komt maar vertrekt direct. Ad belofte en LP content matchen mogelijk niet. |
| Ad CPC vs LP Conversie | CPC €0.41 + 0 leads = duur verkeer zonder resultaat. €62.28 spend voor 0 conversies. Learning phase kan dit verbeteren. |
| LP Views vs GA4 Sessions | Meta: 56 LP views. GA4: 62 H14 sessies. Redelijk consistente match (10% verschil normaal door attributieverschillen). |
| /booking Visits vs Leads | 7 /booking visits maar 0 leads = booking pagina converteert niet. Dit is een nieuw lek dat prioriteit verdient. |
| Bio_link vs Ad verkeer | Bio_link (vorige week): 50% bounce, 15.2s sessie. H14 ad verkeer (gisteren): 100% bounce, 1.3s sessie. Organisch verkeer is 12x meer engaged dan betaald verkeer. |
| Learning Phase indicatoren | Frequency 1.18 (laag, net gestart), CPC 3.2x historisch (verwacht), CTR 60% onder historisch (verwacht). Geef het algoritme 5-7 dagen. |

---

### KPI Dashboard vs Targets

| KPI | 8 april | Target 30d | Status |
|-----|---------|-----------|--------|
| LP Bounce Rate | 100% | <55% | 🔴 (82% boven target) |
| LP Conversie Rate | 0% (0 leads / 56 LP views) | >5% | 🔴 |
| Avg Scroll Depth | Geen data | >60% | 🔴 (tracking ontbreekt) |
| CTA Click Rate | 9.3% (/booking visits) | >4% | 🟢 |
| Meta CPC | €0.41 | <€0.50 | 🟡 (onder target, maar learning phase) |
| Time on Page | 6.0s | >90s (meten) | 🔴 |

---

*Rapport gegenereerd: 9 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard), Google Analytics 4 (property 528249861, SYBB)*
*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*Status: ACTIEF (heractiveerd 8 april 2026) | Actieve ad: H14,B3,CTA5 (Ad Set: BATCH 2)*
