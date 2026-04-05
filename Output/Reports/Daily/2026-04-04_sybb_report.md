# SYBB Daily Report -- 4 april 2026

## 1. Samenvatting

Dag 28 zonder campagne. De SYBB campagne staat **PAUSED sinds 8 maart** en er was geen betaald verkeer op 4 april. PostHog data kon niet worden opgehaald (authenticatie vereist), maar op basis van het patroon van de afgelopen week (0 PV op 3 april, 22 PV op 2 april, 0 PV op 27-28 maart) is het zeer waarschijnlijk dat ook gisteren nul of minimaal organisch verkeer op de landing page was. De campagne had bewezen performance (CPC €0.14, ver onder target €0.50) en elke dag extra pauze is ~112 gemiste LP views en verdere erosie van Meta's optimalisatie-learnings.

## 2. Meta Ads Performance

**Status: PAUSED sinds 8 maart 2026 (28 dagen)**

Geen data beschikbaar voor 4 april. Geen spend, impressions of clicks.

### Campagne Totaal (13 jan - 8 mrt 2026)

| Metric | Totaal | Daggemiddelde (~55d) | Target |
|--------|--------|---------------------|--------|
| Spend | €1,425.57 | ~€25.92 | - |
| Impressions | 205,335 | ~3,733 | - |
| Clicks | 10,132 | ~184 | - |
| CTR | 4.93% | - | - |
| CPC | €0.14 | - | <€0.50 |
| Reach | 99,103 | - | - |
| Frequency | 2.07 | - | <3.0 |
| Link Clicks | 9,815 | ~178 | - |
| Landing Page Views | 6,174 | ~112 | - |
| Leads | 15 | ~0.27 | - |

### Ad Variant Performance (lifetime)

| Ad (utm_content) | Impressions | Link Clicks | CTR | CPC | LP Views | Leads | Cost/Lead |
|-------------------|-------------|-------------|-----|-----|----------|-------|-----------|
| H13,B3,CTA5 | 60,073 | 6,342 | 9.82% | €0.07 | 4,063 | 3 | €140.43 |
| H15,B3,CTA5 | 34,142 | 1,399 | 4.26% | €0.15 | 842 | 0 | - |
| H14,B3,CTA5 | 16,684 | 602 | 3.68% | €0.18 | 357 | 1 | €109.40 |
| H11,B3,CTA5 | 31,060 | 684 | 2.56% | €0.25 | 445 | 6 | €33.75 |
| H12,B3,CTA5 | 47,108 | 676 | 2.54% | €0.31 | 467 | 5 | €74.81 |
| SYBB w/ Semp (BLACK) | 16,268 | 112 | 1.03% | €0.61 | 0 | 0 | - |

**Beste variant (CTR/CPC):** H13,B3,CTA5 -- laagste CPC (€0.07) en hoogste CTR (9.82%). Verantwoordelijk voor 65% van alle link clicks.

**Beste variant (leads):** H11,B3,CTA5 -- laagste cost per lead (€33.75) met 6 van de 15 totale leads (40%).

**Slechtste variant:** SYBB w/ Semp (BLACK) -- €0.61 CPC (boven target), nul leads, nul LP views.

## 3. Landing Page Health

**PostHog authenticatie niet beschikbaar. Data gebaseerd op trend voorgaande dagen.**

| Metric | 4 april (geschat) | 7d Gemiddelde (28 mrt - 3 apr) | Target | Status |
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
| 29 mrt | 7 | 4 | Oude UTM links |
| 30 mrt | 20 | 2 | Organisch/direct |
| 31 mrt | 5 | 2 | Organisch |
| 1 apr | 2 | 1 | Minimaal |
| 2 apr | 22 | 15 | Piek: bio_link + direct |
| 3 apr | 0 | 0 | Nuldag |
| **4 apr** | **~0** | **~0** | **Geschat, PostHog niet beschikbaar** |

**Patroon:** Zonder betaalde campagne is er geen voorspelbaar verkeer. Incidentele pieken (2 apr) worden direct gevolgd door nuldagen. De organische baseline is effectief nul.

## 4. Funnel Drop-off

**4 april:** Geen data (PostHog niet beschikbaar, verwachting ~0 bezoekers)

**Geschatte 7d funnel (28 mrt - 3 apr, ~56 pageviews):**

```
Pageview (100%) --> CTA Click (~19.6%) --> /booking Visit (~12.5%)
   ~56 pvs             ~11 clicks            ~7 visits
```

**Grootste lek:** De funnel zelf functioneert goed (19.6% CTA rate, ver boven 4% target). Het probleem is de bovenkant: er komt simpelweg niemand binnen zonder betaald verkeer.

## 5. Rode Vlaggen

- **CAMPAGNE PAUSED (28 DAGEN)** -- De #1 prioriteit. Elke dag pauze kost ~112 LP views en ~0.27 leads. Na 28 dagen: geschatte ~3,136 gemiste LP views en ~7.5 gemiste leads.
- **ALGORITME DEGRADATIE** -- Na 28 dagen zonder data verliest Meta vrijwel alle optimalisatie-learnings. Bij heractivering moet het algoritme opnieuw door de learning phase (3-7 dagen hogere CPC's).
- **GEEN ORGANISCHE BASELINE** -- 7d gemiddelde ~7 PV/dag met de helft van de dagen op 0. De landing page genereert geen structureel organisch verkeer.
- **PostHog AUTHENTICATIE VERLOPEN** -- PostHog MCP vereist re-authenticatie. Zonder LP data is het onmogelijk om per-variant on-page gedrag te analyseren bij heractivering.
- **GEMIST MOMENTUM** -- De campagne had een CPC van €0.14 (72% onder target). Dit is uitzonderlijk goede performance die nu niet wordt benut.

## 6. Top 3 Acties voor Vandaag

### 1. Heractiveer de SYBB campagne
- **Wat:** Heractiveer de campagne met alleen H13 (volume) + H11 (leads) actief. Pause H12, H14, H15, BLACK.
- **Waarom:** 28 dagen pauze. €0.14 CPC die niet wordt benut. Elke dag kost ~112 LP views. Hoe langer de pauze, hoe duurder de re-learning phase.
- **Hoe:** Meta Ads Manager > 2026: SYBB > Campaign activeren. Ad set "BATCH 2" activeren. In ad set: alleen H11 + H13 actief houden. Budget: €25/dag.
- **Verwachte impact:** Binnen 3-5 dagen terug op ~80-120 LP views/dag na learning phase.
- **Escalatie:** Rood (strategie, Robin beslissing)

### 2. Fix PostHog authenticatie
- **Wat:** Herautenticeer PostHog MCP zodat LP analytics weer beschikbaar zijn.
- **Waarom:** Zonder PostHog data is het onmogelijk om bounce rate, scroll depth en CTA clicks per variant te meten. Dit is essentieel bij heractivering om ad-LP mismatch te detecteren.
- **Hoe:** Open de PostHog OAuth URL in de browser en autoriseer de connectie.
- **Verwachte impact:** Volledige LP analytics weer beschikbaar in het dagelijks rapport.
- **Escalatie:** Groen (Robin handmatig, 2 minuten)

### 3. Standaardiseer UTM tagging voor heractivering
- **Wat:** Voordat de campagne opnieuw actief gaat: check en fix alle UTM parameters naar lowercase + underscores.
- **Waarom:** Eerdere PostHog data toonde dubbele entries door inconsistente UTM formatting. Schone data is essentieel voor per-variant LP analyse.
- **Hoe:** Check alle ad URLs in Meta Ads Manager. Format: `utm_content=h11_b3_cta5` (niet "H11, B3, CTA5"). Run `/tracking-check` na aanpassing.
- **Verwachte impact:** Betrouwbare per-variant conversie data vanaf dag 1 heractivering.
- **Escalatie:** Geel (Robin handmatig)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| 28d pauze = algoritme reset | Meta's delivery optimization vereist continue data. Na 28 dagen is de "learning" effectief verdwenen. Verwacht 3-7 dagen hogere CPC's bij herstart. |
| H13 vs H11 paradox | H13 heeft de beste CPC (€0.07) en meeste clicks, maar H11 genereert de meeste leads. Bij heractivering: H11 als lead-driver, H13 als volume/awareness. |
| LP funnel is niet het probleem | CTA click rate (~19.6%) is bijna 5x boven target (4%). De funnel converteert, maar er is geen verkeer om te converteren. |
| PostHog gap | Zonder LP analytics is cross-referencing (Ad CTR vs LP Bounce, variant vs scroll depth) onmogelijk. Fix authenticatie voor heractivering. |
| Organisch kanaal ontbreekt | Na bijna een maand: gemiddeld ~7 PV/dag organisch, waarvan 50% nuldagen. Er is geen SEO, geen email traffic, geen social push naar de LP. |

---

*Rapport gegenereerd: 5 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard). PostHog niet beschikbaar (authenticatie vereist).*
*Campagne status: PAUSED sinds 8 maart 2026 (28 dagen)*
