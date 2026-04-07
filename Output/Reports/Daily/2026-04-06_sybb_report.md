# SYBB Daily Report -- 6 april 2026

## 1. Samenvatting

Dag 30 zonder campagne. De SYBB campagne staat **PAUSED sinds 8 maart** en er was geen betaald verkeer op 6 april. PostHog data kon niet worden opgehaald (authenticatie vereist). De campagne heeft nu een volle maand stilgestaan. Met een bewezen CPC van €0.14 (72% onder target) en een funnel die converteert (19.6% CTA click rate), zijn er naar schatting ~3,360 LP views en ~8.1 leads gemist in deze 30 dagen. Het algoritme is volledig gereset en bij heractivering moet de learning phase opnieuw doorlopen worden.

## 2. Meta Ads Performance

**Status: PAUSED sinds 8 maart 2026 (30 dagen)**

Geen data beschikbaar voor 6 april. Geen spend, impressions of clicks.

### Campagne Totaal (13 jan - 8 mrt 2026)

| Metric | Totaal | Daggemiddelde (~55d) | Target |
|--------|--------|---------------------|--------|
| Spend | €1,425.57 | ~€25.92 | - |
| Impressions | 205,335 | ~3,733 | - |
| Clicks | 10,132 | ~184 | - |
| CTR | 4.93% | - | - |
| CPC | €0.14 | - | <€0.50 |
| Reach | 100,122 | - | - |
| Frequency | 2.05 | - | <3.0 |
| Link Clicks | 9,815 | ~178 | - |
| Landing Page Views | 6,174 | ~112 | - |
| Leads | 15 | ~0.27 | - |

### Laatste Actieve Week: Dagelijkse Breakdown (3-8 mrt)

| Datum | Spend | Impressions | Clicks | CTR | CPC | Link Clicks | LP Views |
|-------|-------|-------------|--------|-----|-----|-------------|----------|
| 3 mrt | €125.17 | 14,959 | 616 | 4.12% | €0.20 | 395 | 291 |
| 4 mrt | €196.71 | 18,968 | 614 | 3.24% | €0.32 | 374 | 262 |
| 6 mrt | €181.76 | 23,474 | 4,377 | 18.65% | €0.04 | 4,853 | 2,973 |
| 7 mrt | €512.80 | 88,203 | 3,502 | 3.97% | €0.15 | 3,481 | 2,249 |
| 8 mrt | €307.39 | 43,463 | 856 | 1.97% | €0.36 | 600 | 399 |

**Opvallend:** De laatste dag (8 mrt) liet een forse daling zien in CTR (1.97% vs 5.27% gemiddeld) en stijging in CPC (€0.36 vs €0.13 gemiddeld). Dit was mogelijk al een signaal van ad fatigue of audience saturation.

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

## 3. Landing Page Health

**PostHog authenticatie niet beschikbaar. Data gebaseerd op trend voorgaande dagen.**

| Metric | 6 april (geschat) | 7d Gemiddelde (30 mrt - 5 apr) | Target | Status |
|--------|-------------------|-------------------------------|--------|--------|
| Pageviews | ~0 | ~7/dag | - | 🔴 |
| Unique Visitors | ~0 | ~3/dag | - | 🔴 |
| Bounce Rate | n.v.t. | ~85% (geschat) | <55% | 🔴 |
| Avg Session Duration | n.v.t. | ~170s | >90s | n.v.t. |
| CTA Click Rate | n.v.t. | ~19.6% | >4% | n.v.t. |
| /booking Visits | 0 | ~1/dag | - | 🔴 |

### 7-dagen Trend (op basis van voorgaande rapporten)

| Datum | Pageviews | Unique Visitors | Opmerking |
|-------|-----------|-----------------|-----------|
| 31 mrt | 5 | 2 | Organisch |
| 1 apr | 2 | 1 | Minimaal |
| 2 apr | 22 | 15 | Piek: bio_link + direct |
| 3 apr | 0 | 0 | Nuldag |
| 4 apr | ~0 | ~0 | Geschat (PostHog niet beschikbaar) |
| 5 apr | ~0 | ~0 | Geschat (PostHog niet beschikbaar) |
| **6 apr** | **~0** | **~0** | **Geschat (PostHog niet beschikbaar)** |

**Patroon:** Zonder betaalde campagne is er geen voorspelbaar verkeer. Organische baseline is effectief nul met incidentele pieken van bio links of direct verkeer.

## 4. Funnel Drop-off

**6 april:** Geen data (PostHog niet beschikbaar, verwachting ~0 bezoekers)

**Geschatte 7d funnel (30 mrt - 5 apr, ~29 pageviews geschat):**

```
Pageview (100%) --> CTA Click (~19.6%) --> /booking Visit (~12.5%)
   ~29 pvs             ~6 clicks            ~4 visits
```

**Grootste lek:** De funnel zelf functioneert goed (19.6% CTA rate, bijna 5x boven 4% target). Het probleem is de bovenkant: er komt simpelweg niemand binnen zonder betaald verkeer.

## 5. Rode Vlaggen

- **CAMPAGNE PAUSED (30 DAGEN)** -- Mijlpaal bereikt: een volle maand zonder campagne. Elke dag pauze kost ~112 LP views en ~0.27 leads. Na 30 dagen: geschatte ~3,360 gemiste LP views en ~8.1 gemiste leads.
- **ALGORITME VOLLEDIG GERESET** -- Na 30 dagen zonder data heeft Meta alle optimalisatie-learnings verloren. Bij heractivering moet het algoritme volledig opnieuw door de learning phase (verwacht 5-7 dagen met hogere CPC's, mogelijk €0.30-€0.50 i.p.v. de eerdere €0.14).
- **LAATSTE DAG WAS ZWAK** -- De laatste actieve dag (8 mrt) toonde al verslechtering: CTR daalde naar 1.97% en CPC steeg naar €0.36. Bij heractivering is het verstandig om met een lager budget te starten en H13 + H11 als enige actieve ads te houden.
- **PostHog AUTHENTICATIE VERLOPEN** -- PostHog MCP vereist re-authenticatie. Zonder LP data is het onmogelijk om per-variant on-page gedrag te analyseren bij heractivering.
- **GEEN ORGANISCHE BASELINE** -- ~7 PV/dag gemiddeld met veel nuldagen. Er is geen SEO, geen email traffic, geen social push naar de LP.

## 6. Top 3 Acties voor Vandaag

### 1. Heractiveer de SYBB campagne (gefaseerd)
- **Wat:** Heractiveer de campagne met alleen H13 (volume/CTR kampioen) + H11 (lead kampioen) actief. Pause H12, H14, H15.
- **Waarom:** 30 dagen pauze. €0.14 CPC die niet wordt benut. Geschatte 3,360 gemiste LP views. Hoe langer de pauze, hoe duurder de re-learning phase.
- **Hoe:** Meta Ads Manager > 2026: SYBB > Campaign activeren. Ad set "BATCH 2" activeren. Alleen H11 + H13 actief houden. Start met €15-20/dag budget (lager dan eerdere €25 om learning phase rustig te doorlopen).
- **Verwachte impact:** Binnen 5-7 dagen terug op ~80-120 LP views/dag na learning phase. Hogere CPC eerste week (verwacht €0.25-€0.40).
- **Escalatie:** Rood (strategie, Robin beslissing)

### 2. Fix PostHog authenticatie
- **Wat:** Herautenticeer PostHog MCP zodat LP analytics weer beschikbaar zijn voor de heractivering.
- **Waarom:** Zonder PostHog data is het onmogelijk om bounce rate, scroll depth en CTA clicks per variant te meten. Dit is essentieel bij heractivering om ad-LP mismatch te detecteren en de learning phase te monitoren.
- **Hoe:** Open de PostHog OAuth URL in de browser en autoriseer de connectie.
- **Verwachte impact:** Volledige LP analytics weer beschikbaar in het dagelijks rapport.
- **Escalatie:** Groen (Robin handmatig, 2 minuten)

### 3. Bereid nieuwe creatives voor (BATCH 3)
- **Wat:** Ontwikkel 2-3 nieuwe hook varianten om naast H11 en H13 te testen na de learning phase.
- **Waarom:** Na 30 dagen dezelfde audience met dezelfde creatives is ad fatigue onvermijdelijk. Frequency was al op 2.05 voor de pauze. Verse creatives zijn nodig om de audience te verfrissen.
- **Hoe:** Gebruik `/social-content` of `/video-scripting` om nieuwe hooks te genereren gebaseerd op het Hormozi hook framework (70% bewezen, 20% variaties, 10% experiment). Focus op de 8 SYBB pillars.
- **Verwachte impact:** Lagere CPC en hogere CTR door fresh creative rotation. Voorkomt snelle ad fatigue bij heractivering.
- **Escalatie:** Geel (content creatie, Robin + Claude)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| 30d pauze = volledige algoritme reset | Meta's delivery optimization is volledig vervallen. Verwacht een volledige learning phase van 5-7 dagen met CPC's 2-3x hoger dan het historisch gemiddelde. |
| H13 vs H11 paradox | H13 heeft de beste CPC (€0.07) maar slechts 3 leads. H11 heeft hogere CPC (€0.25) maar 6 leads. Bij heractivering: beide actief houden voor volume + conversie strategie. |
| Laatste dag degradatie | 8 mrt toonde CTR 1.97% en CPC €0.36 (bijna 3x het gemiddelde). Dit wijst op audience fatigue. Fresh creatives en/of audience expansion overwegen bij herstart. |
| LP funnel is niet het probleem | CTA click rate (~19.6%) is bijna 5x boven target (4%). De funnel converteert prima, maar er is geen verkeer. |
| 30-dagen mijlpaal | Na een maand pauze is dit een strategisch beslismoment: heractiveren met bestaande creatives + lager budget, of eerst nieuwe BATCH 3 creatives voorbereiden en dan heractiveren met verse content. |

---

*Rapport gegenereerd: 7 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard). PostHog niet beschikbaar (authenticatie vereist).*
*Campagne status: PAUSED sinds 8 maart 2026 (30 dagen)*
