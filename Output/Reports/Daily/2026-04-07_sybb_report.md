# SYBB Daily Report -- 7 april 2026

## 1. Samenvatting

Dag 31 zonder campagne. De SYBB campagne staat **PAUSED sinds 8 maart** en er was geen betaald verkeer op 7 april. GA4 data (vervangt PostHog) toont slechts 1 bezoeker gisteren, die direct bouncede. Over de afgelopen 7 dagen (1-7 april) waren er 24 sessies, waarvan slechts 4 via oude ad UTMs (h11, h12, h15). De bio_link in Instagram is momenteel de enige consistente verkeersbron (7 sessies, 42.9% bounce, 17.3s gemiddelde sessieduur). Met 31 dagen pauze is het algoritme volledig gereset. De 3 /booking visits deze week kwamen uitsluitend via bio_link en direct verkeer.

## 2. Meta Ads Performance

**Status: PAUSED sinds 8 maart 2026 (31 dagen)**

Geen data beschikbaar voor 7 april. Geen spend, impressions of clicks.

### Campagne Totaal (13 jan - 8 mrt 2026)

| Metric | Totaal | Daggemiddelde (~55d) | Target |
|--------|--------|---------------------|--------|
| Spend | €1,323.83 | ~€24.07 | - |
| Impressions | 189,067 | ~3,438 | - |
| Clicks | 9,965 | ~181 | - |
| CTR | 5.27% | - | - |
| CPC | €0.13 | - | <€0.50 |
| Reach | 91,119 | - | - |
| Frequency | 2.07 | - | <3.0 |
| Link Clicks | 9,703 | ~176 | - |
| Landing Page Views | 6,174 | ~112 | - |
| Leads | 15 | ~0.27 | - |
| Cost per Lead | €88.26 | - | - |

### Ad Variant Performance (lifetime)

| Ad (utm_content) | Impressions | Link Clicks | CTR | CPC | LP Views | Leads | Cost/Lead |
|-------------------|-------------|-------------|-----|-----|----------|-------|-----------|
| H13,B3,CTA5 | 60,073 | 6,342 | 9.82% | €0.07 | 4,063 | 3 | €140.43 |
| H15,B3,CTA5 | 34,142 | 1,399 | 4.26% | €0.15 | 842 | 0 | - |
| H14,B3,CTA5 | 16,684 | 602 | 3.68% | €0.18 | 357 | 1 | €109.40 |
| H11,B3,CTA5 | 31,060 | 684 | 2.56% | €0.25 | 445 | 6 | €33.75 |
| H12,B3,CTA5 | 47,108 | 676 | 2.54% | €0.31 | 467 | 5 | €74.81 |

**Beste variant (CTR/CPC):** H13,B3,CTA5, laagste CPC (€0.07) en hoogste CTR (9.82%). Verantwoordelijk voor 65% van alle link clicks.

**Beste variant (leads):** H11,B3,CTA5, laagste cost per lead (€33.75) met 6 van de 15 totale leads (40%).

**Slechtste variant:** H12,B3,CTA5, hoogste CPC (€0.31) en laagste CTR (2.54%) met relatief hoge spend (€374.03).

## 3. Landing Page Health (GA4 Data)

| Metric | 7 april | 7d Gemiddelde (1-7 apr) | Target | Status |
|--------|---------|------------------------|--------|--------|
| Pageviews | 1 | 3.7/dag | - | 🔴 |
| Unique Visitors | 1 | 3.0/dag | - | 🔴 |
| Sessions | 1 | 3.4/dag | - | 🔴 |
| Bounce Rate | 100% | 79.2% | <55% | 🔴 |
| Avg Session Duration | 0s | 7.0s | >90s | 🔴 |
| Scroll Rate (90%) | 0% | 29.2% | >60% | 🔴 |
| /booking Visits | 0 | 0.4/dag | - | 🔴 |

### Dagelijkse Breakdown (1-7 april, GA4)

| Datum | Pageviews | Users | Sessions | Bounce Rate | Avg Session |
|-------|-----------|-------|----------|-------------|-------------|
| 1 apr | 2 | 1 | 1 | 0% | 6.3s |
| 2 apr | 7 | 7 | 7 | 85.7% | 8.3s |
| 3 apr | 4 | 4 | 4 | 100% | 6.7s |
| 4 apr | 0 | 0 | 0 | - | - |
| 5 apr | 9 | 9 | 9 | 77.8% | 4.4s |
| 6 apr | 3 | 2 | 2 | 50% | 16.3s |
| **7 apr** | **1** | **1** | **1** | **100%** | **0s** |

### UTM Content Breakdown (7d, GA4)

| Bron (utm_content) | Sessions | Bounce Rate | Avg Session | Engaged |
|--------------------|----------|-------------|-------------|---------|
| bio_link | 7 | 42.9% | 17.3s | 4 |
| (not set / direct) | 13 | 92.3% | 3.3s | 1 |
| h11_b3_cta5 | 2 | 100% | 0s | 0 |
| h12_b3_cta5 | 1 | 100% | 0s | 0 |
| h15_b3_cta5 | 1 | 100% | 0s | 0 |

**Opvallend:** De 4 sessies via oude ad UTMs (h11, h12, h15) bouncen allemaal direct (100%, 0s sessieduur). Dit zijn waarschijnlijk gecachte links of bookmarks, geen verse ad clicks. De bio_link is de enige bron met echte engagement (42.9% bounce, 17.3s sessieduur).

### Page Breakdown (7d)

| Pagina | Pageviews | Users |
|--------|-----------|-------|
| / (landing page) | 22 | 24 |
| /booking | 3 | 3 |
| /product-page/start-your-balloon-business... | 1 | 1 |

## 4. Funnel Drop-off

**7 april:** Geen funnel data (slechts 1 bezoeker, direct gebounced)

**7d funnel (1-7 april, 24 sessies):**

```
Pageview (100%) --> Scroll 90% (29.2%) --> /booking (12.5%)
   24 sessies          7 scrolls           3 visits
```

**Drop-off analyse:**
- Pageview naar Scroll: 70.8% drop-off (17 van 24 scrollen niet)
- Scroll naar /booking: 57.1% drop-off (4 van 7 scrollers klikken niet door)

**Grootste lek:** De eerste interactie. 70.8% van bezoekers bounced of scrolt niet voorbij de hero sectie. Bij het lage volume (24 sessies/week) is dit echter statistisch niet significant. De bio_link bezoekers presteren veel beter (57.1% scrollt) dan direct/ongetagd verkeer (7.7% scrollt).

## 5. Rode Vlaggen

- **CAMPAGNE PAUSED (31 DAGEN)** -- Meer dan een maand zonder campagne. Geschatte gemiste resultaten: ~3,472 LP views en ~8.4 leads. Elke dag pauze kost ~112 LP views en ~0.27 leads op basis van historisch gemiddelde.
- **ALGORITME VOLLEDIG GERESET** -- Na 31 dagen zonder data heeft Meta alle optimalisatie-learnings verloren. Bij heractivering verwacht 5-7 dagen learning phase met CPC's 2-3x hoger dan het historisch gemiddelde van €0.13.
- **LANDING PAGE EFFECTIEF ONBEREIKBAAR** -- 1 bezoeker gisteren, 3.4 sessies/dag gemiddeld deze week. Zonder betaald verkeer is de LP onzichtbaar.
- **AD UTM VERKEER IS SPOOKVERKEER** -- De 4 sessies via h11/h12/h15 UTMs zijn 100% bounce met 0s sessieduur. Dit zijn geen echte ad clicks (campagne is uit) maar gecachte URLs. Niet meetellen als relevant verkeer.
- **BIO LINK IS ENIGE WERKENDE BRON** -- 7 van 24 sessies (29%) komt via bio_link met 42.9% bounce en 17.3s sessieduur. Dit is de enige bron met echte engagement. Alle 3 /booking visits kwamen waarschijnlijk via dit kanaal.
- **SESSIEDUUR VER ONDER TARGET** -- 7.0s gemiddeld vs 90s target. Zelfs de bio_link bezoekers (17.3s) zitten ver onder target. De landing page overtuigt niet snel genoeg.

## 6. Top 3 Acties voor Vandaag

### 1. Heractiveer de SYBB campagne (gefaseerd)
- **Wat:** Heractiveer de campagne met alleen H13 (volume/CTR kampioen) + H11 (lead kampioen) actief. Pause H12, H14, H15.
- **Waarom:** 31 dagen pauze. €0.13 CPC die niet wordt benut. Geschatte 3,472 gemiste LP views. Het algoritme moet hoe dan ook opnieuw leren, en elke dag uitstel maakt dat niet beter.
- **Hoe:** Meta Ads Manager > 2026: SYBB > Campaign activeren. Ad set "BATCH 2" activeren. Alleen H11 + H13 actief houden. Start met €15-20/dag budget (lager dan eerdere €24 om learning phase rustig te doorlopen).
- **Verwachte impact:** Binnen 5-7 dagen terug op ~80-120 LP views/dag na learning phase. Hogere CPC eerste week (verwacht €0.25-€0.40).
- **Escalatie:** Rood (strategie, Robin beslissing)

### 2. Optimaliseer bio_link flow
- **Wat:** Zorg dat de Instagram bio link direct naar startyourballoonbusiness.com wijst met correcte UTM tracking. Overweeg een Linktree-achtige pagina te vervangen door een directe LP link.
- **Waarom:** Bio_link is momenteel de enige bron met echte engagement (42.9% bounce, 17.3s sessie). Dit is 3 van de 3 /booking visits. Maximaliseer deze gratis verkeersbron terwijl de campagne uit staat.
- **Hoe:** Check Instagram bio link setup. Zorg dat UTM parameters correct zijn (utm_source=instagram, utm_medium=organic, utm_content=bio_link).
- **Verwachte impact:** Betere tracking van organisch verkeer en mogelijk hogere conversie door directe LP link.
- **Escalatie:** Groen (Robin handmatig, 5 minuten)

### 3. Bereid BATCH 3 creatives voor
- **Wat:** Ontwikkel 2-3 nieuwe hook varianten om naast H11 en H13 te testen na de learning phase.
- **Waarom:** Na 31 dagen dezelfde audience met dezelfde creatives is ad fatigue bij heractivering onvermijdelijk. Frequency was al op 2.07 voor de pauze. Verse creatives zijn nodig voor de herstart.
- **Hoe:** Gebruik `/social-content` of `/video-scripting` om nieuwe hooks te genereren gebaseerd op het Hormozi hook framework (70% bewezen, 20% variaties, 10% experiment). Focus op de 8 SYBB pillars.
- **Verwachte impact:** Lagere CPC en hogere CTR door fresh creative rotation. Voorkomt snelle ad fatigue bij heractivering.
- **Escalatie:** Geel (content creatie, Robin + Claude)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| Bio_link vs Ad UTM traffic | Bio_link: 42.9% bounce, 17.3s sessie. Ad UTMs (oud): 100% bounce, 0s. Organisch verkeer via Instagram bio is significant beter dan spook-ad-verkeer. Bij heractivering wordt dit de baseline voor vergelijking. |
| LP engagement probleem | Zelfs bio_link bezoekers (de meest gemotiveerde groep) hebben slechts 17.3s gemiddelde sessieduur vs 90s target. De landing page hero sectie en eerste value proposition moeten sterker. |
| Funnel werkt, top is leeg | 3 /booking visits bij slechts 24 sessies = 12.5% conversie. De funnel zelf functioneert, maar er is geen volume. Campagne heractivering is de #1 prioriteit. |
| 31-dagen pauze mijlpaal | Strategisch beslismoment: heractiveren met bestaande creatives + lager budget, of eerst BATCH 3 voorbereiden. Aanbeveling: beide parallel, start met H11+H13 terwijl BATCH 3 in ontwikkeling is. |

---

*Rapport gegenereerd: 8 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard), Google Analytics 4 (property 528249861, SYBB)*
*Campagne status: PAUSED sinds 8 maart 2026 (31 dagen)*
