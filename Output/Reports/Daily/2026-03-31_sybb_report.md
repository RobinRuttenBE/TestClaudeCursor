# SYBB Daily Report - 31 maart 2026

## 1. Samenvatting

**De SYBB campagne staat GEPAUZEERD sinds 8 maart.** Er is geen actieve Meta Ads spend. De landing page ontvangt alleen organisch/direct verkeer (5 pageviews, 2 unieke bezoekers gisteren). Het beperkte verkeer toont wel goede engagement (478s sessieduur), maar zonder betaald verkeer staat de funnel stil. Besluit nodig: campagne heractiveren of nieuwe campagne opzetten.

## 2. Meta Ads Performance

### Campagne Status: GEPAUZEERD (sinds 8 maart 2026)

Geen data beschikbaar voor gisteren of afgelopen 7 dagen. Hieronder de lifetime resultaten ter referentie.

### Lifetime Performance (13 jan - 8 mrt 2026)

| Metric | Lifetime | Dag Gem. (55 actieve dagen) | Target |
|--------|----------|----------------------------|--------|
| Spend | EUR 1.323,83 | EUR 24,07/dag | - |
| Impressions | 189.067 | 3.438/dag | - |
| Clicks | 9.965 | 181/dag | - |
| CTR | 5,27% | - | - |
| CPC | EUR 0,13 | - | <EUR 0,50 |
| Link Clicks | 9.703 | 176/dag | - |
| Landing Page Views | 6.174 | 112/dag | - |
| Leads | 15 | 0,27/dag | - |
| Cost per Lead | EUR 88,26 | - | - |
| Frequency | 2,07 | - | <3,0 |

**CPC (EUR 0,13) ruim onder target (EUR 0,50)**, uitstekende traffic-effici&euml;ntie.

### Ad Variant Performance (Lifetime)

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LP Views | Leads | Cost/Lead |
|-------------------|-------|-------------|-----|-----|----------|-------|-----------|
| H13,B3,CTA5 | EUR 421,28 | 6.342 | 9,82% | EUR 0,07 | 4.063 | 3 | EUR 140,43 |
| H15,B3,CTA5 | EUR 216,64 | 1.399 | 4,26% | EUR 0,15 | 842 | 0 | - |
| H12,B3,CTA5 | EUR 374,03 | 676 | 2,54% | EUR 0,31 | 467 | 5 | EUR 74,81 |
| H11, B3, CTA5 | EUR 202,48 | 684 | 2,56% | EUR 0,25 | 445 | 6 | EUR 33,75 |
| H14,B3,CTA5 | EUR 109,40 | 602 | 3,68% | EUR 0,18 | 357 | 1 | EUR 109,40 |
| SYBB w/ Semp (BLACK) | EUR 101,74 | 112 | 1,03% | EUR 0,61 | - | - | - |

**Beste variant (volume):** H13,B3,CTA5. Veruit de meeste clicks (6.342) en laagste CPC (EUR 0,07). Echter: slechts 3 leads ondanks 4.063 LP views (0,07% conversie). Hoge CTR door video engagement, niet koopintentie.

**Beste variant (conversie):** H11, B3, CTA5. Laagste cost per lead (EUR 33,75), 6 leads uit 445 LP views (1,35% conversie). Duidelijk de sterkste combinatie van kwaliteitsverkeer en conversie.

**Slechtste variant:** SYBB w/ Semp (BLACK). Hoogste CPC (EUR 0,61, boven target), laagste CTR (1,03%). Geen landing page views geregistreerd.

### Cross-referentie: Ad CTR vs LP Conversie

| Ad | CTR | LP Conversie | Diagnose |
|----|-----|--------------|----------|
| H13 | 9,82% | 0,07% | Hoge CTR + ultra-lage conversie = misleidende ad of verkeerd publiek |
| H12 | 2,54% | 1,07% | Gemiddelde CTR + redelijke conversie = goede match |
| H11 | 2,56% | 1,35% | Gemiddelde CTR + beste conversie = beste kwaliteitsverkeer |
| H15 | 4,26% | 0,00% | Hoge CTR + nul conversie = ad-pagina mismatch |
| H14 | 3,68% | 0,28% | Goede CTR + lage conversie = matige match |

## 3. Landing Page Health (PostHog)

### Gisteren (31 maart 2026) - Alleen organisch/direct verkeer

| Metric | 31 mrt | 30 mrt | 29 mrt | Target | Status |
|--------|--------|--------|--------|--------|--------|
| Pageviews | 5 | 20 | 7 | - | - |
| Unique Visitors | 2 | 2 | 4 | - | - |
| Avg Session Duration | 478s | 742s | 189s | >90s | Op target |
| CTA Clicks | 0 | 1 | 0 | >4% rate | Onvoldoende data |

**Sessieduur boven target:** Bezoekers die de pagina vinden besteden gemiddeld 478 seconden (bijna 8 minuten). Dit is sterk boven de 90s target. De pagina engageert goed, het probleem is volume en conversie, niet engagement.

### UTM Segmentatie (29-31 maart)

| Bron | Pageviews 29 mrt | Pageviews 30-31 mrt |
|------|------------------|---------------------|
| H11,B3,CTA5 / h11_b3_cta5 | 4 | 0 |
| H12,B3,CTA5 | 1 | 0 |
| h13_b3_cta5 | 1 | 0 |
| Geen UTM (organisch/direct) | 1 | 25 |

Alle verkeer op 30-31 maart is organisch of direct. De 6 UTM-getagde bezoeken op 29 maart zijn waarschijnlijk late attributie of opgeslagen links.

**Let op UTM inconsistentie:** Mix van formaten (`H11,B3,CTA5` vs `h11_b3_cta5`). Standaardiseer naar lowercase met underscores bij heractivering.

## 4. Funnel Drop-off (Lifetime referentie)

```
Impressions (189.067, 100%)
    |
    v  5,1% click-through
Link Clicks (9.703)
    |
    v  63,6% landing rate
Landing Page Views (6.174)
    |
    v  0,24% conversie
Leads (15)
```

**Grootste lek:** Landing Page naar Leads (99,76% drop-off). Van 6.174 LP views converteren slechts 15 naar een lead. Dit is het kritieke optimalisatiepunt. Target LP conversie is >5%, huidige conversie is 0,24%.

## 5. Rode Vlaggen

1. **CAMPAGNE GEPAUZEERD (23 dagen)** - Geen actieve spend sinds 8 maart. De volledige lead generatie funnel staat stil.

2. **LP conversie kritiek laag (0,24%)** - Target is >5%. Dit is 20x onder target. Zelfs met uitstekende CPC (EUR 0,13) maakt dit de funnel onrendabel. EUR 88,26 per lead is te hoog.

3. **H13 anomalie** - 9,82% CTR maar 0,07% LP conversie. De ad trekt 65% van alle LP views maar levert slechts 20% van de leads. Video engagement (20.866 views) drijft de CTR, niet koopintentie.

4. **H15 nul leads** - EUR 216,64 spend, 842 LP views, 0 leads. Complete ad-page mismatch.

5. **UTM inconsistentie** - Mix van `H11,B3,CTA5` en `h11_b3_cta5`. Bemoeilijkt cross-referencing tussen Meta Ads en PostHog.

## 6. Top 3 Acties voor Vandaag

### 1. Besluit nemen over campagne heractivering
**Wat:** Bepaal of de SYBB campagne herstart wordt en met welk budget.
**Waarom:** 23 dagen zonder actieve ads. Funnel staat stil, geen nieuwe leads.
**Hoe:** Review de workshop pipeline/planning. Als er nog plaatsen beschikbaar zijn: heractiveer met focus op H11 (beste conversie, EUR 33,75 per lead) en H12 (EUR 74,81 per lead). Pauzeer H13, H15 en SYBB BLACK.
**Verwachte impact:** Met herverdeeld budget naar H11/H12 kan cost per lead dalen van EUR 88 naar ~EUR 50.
**Escalatie:** Rood (strategiebesluit Robin)

### 2. Landing page conversie optimalisatie
**Wat:** De LP converteert op 0,24%. Target is 5%. De pagina moet fundamenteel verbeterd worden.
**Waarom:** Dit is het grootste lek: 6.174 LP views leveren slechts 15 leads. De sessieduur (478s) toont dat mensen lezen maar niet actie ondernemen.
**Hoe:** (1) CTA prominenter boven de fold, (2) social proof (testimonials eerdere deelnemers), (3) urgentie (beperkt aantal plaatsen), (4) formulier versimpelen. Via Wix Editor.
**Verwachte impact:** Van 0,24% naar 2-3% conversie zou bij heractivering 10-15x meer leads opleveren uit hetzelfde budget.
**Escalatie:** Oranje (Wix Editor nodig)

### 3. UTM tracking standaardiseren
**Wat:** Fix de UTM inconsistentie voor heractivering.
**Waarom:** Huidige mix (`H11,B3,CTA5` vs `h11_b3_cta5`) maakt cross-referencing onbetrouwbaar.
**Hoe:** Bij heractivering alle ads updaten naar lowercase format: `utm_content=h11_b3_cta5`. Update de UTM & Tracking Reference in Drive.
**Verwachte impact:** Betere data-matching tussen Meta Ads en PostHog, betrouwbaardere analyse.
**Escalatie:** Groen (zelf uit te voeren)

---

*Rapport gegenereerd op 1 april 2026 08:00 | Databronnen: Meta Ads MCP (Pipeboard), PostHog MCP*
*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*PostHog Project: Default project (149694) | Site: startyourballoonbusiness.com*
