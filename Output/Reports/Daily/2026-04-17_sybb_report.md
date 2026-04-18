# SYBB Daily Report — 2026-04-17

## 1. Samenvatting
Zwakke dag: lagere spend (€86,54) en 32% minder impressions dan het 7d-gemiddelde, met een CPC die opnieuw boven target kleeft (€0,62). De landing page blijft het grootste lek: bounce rate 84,6%, gemiddelde sessieduur 16,9s en gemiddelde scroll diepte 31%. Lichtpuntje: variant **H12** presteert sterk boven de rest (CTR 4,24%, CPC €0,32) maar krijgt amper budget (€8,84).

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (ID 120239435987290239) — status ACTIVE, daily budget €100.

| Metric | Gisteren (17-04) | 7d Gemiddelde (10-16 apr) | Trend |
|--------|------------------|---------------------------|-------|
| Spend | €86,54 | €102,21 | ↓ 15% |
| Impressions | 5.993 | 8.761 | ↓ 32% |
| Clicks (all) | 139 | 181 | ↓ 23% |
| Link clicks | 78 | 96 | ↓ 19% |
| Landing page views | 63 | 75 | ↓ 16% |
| CTR | 2,32% | 2,07% | ↑ 12% |
| CPC | €0,62 | €0,56 | ↑ 11% (slechter) |
| CPM | €14,44 | €11,67 | ↑ 24% (slechter) |
| Reach | 4.306 | 4.077/dag | → |
| Frequency (dag) | 1,39 | n.v.t. (cum. 2,15 over 7d) | → |

### Ad Variant Performance (gisteren)

| Ad (utm_content) | Spend | Impr | Clicks | CTR | CPC | Meta LPV | PH Sessions | PH Pageviews |
|------------------|-------|------|--------|-----|-----|----------|-------------|--------------|
| h11_b3_cta5 | €65,85 | 4.378 | 91 | 2,08% | €0,72 | 42 | 60 | 69 |
| h12_b3_cta5 | €8,84  | 661   | 28 | 4,24% | €0,32 | 12 | 14 | 16 |
| h13_b3_cta5 | €11,85 | 954   | 20 | 2,10% | €0,59 | 9  | 17 | 19 |
| (bio_link, organisch) | — | — | — | — | — | — | 1 | 1 |

**Beste variant:** **H12** — ruim 2x hogere CTR (4,24%) en minder dan de helft van de CPC (€0,32) van H11. Bovendien de laagste kost per landing page view (€0,74 vs €1,57 voor H11). Duidelijk ondergefund: slechts 10% van het dagbudget.
**Slechtste variant:** **H11** — hoogste CPC (€0,72, 44% boven target) en eet 76% van het budget op, maar levert slechts een middelmatige CTR (2,08%).

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target 30d | Status |
|--------|----------|---------------|-----------|--------|
| Pageviews | 106 | 166/dag | — | — |
| Unieke bezoekers | 89 | 111/dag | — | — |
| Sessions | 91 | 123/dag | — | — |
| Bounce Rate | 84,62% | 81,70% | <55% | 🔴 |
| Avg Session Duration | 16,9s | 44s | >90s | 🔴 |
| Scroll 25% | 31,8% (7/22) | 44,7% | >80% | 🔴 |
| Scroll 50% | 31,8% (7/22) | 39,1% | >60% | 🔴 |
| Scroll 75% | 27,3% (6/22) | 33,4% | >40% | 🔴 |
| Scroll 100% | 13,6% (3/22) | 25,6% | >20% | 🔴 |
| Avg scroll depth | 31,2% | 42,5% | >60% | 🔴 |
| CTA Click Rate ("Go to workshop") | 5,5% (5/91) | — | >4% | 🟢 |

Opm.: scroll depth is berekend op 22 `$pageleave` events; de overige sessies verlaten de pagina zonder een leave-event te sturen (typisch harde bounces).

### Pathname verdeling gisteren
| Path | Pageviews |
|------|-----------|
| `/` (landing) | 99 |
| `/product-page/start-your-balloon-business-professional` | 6 |
| `/booking` | 1 |

### Top autocapture clicks gisteren
| Element | Clicks |
|---------|--------|
| "Go to workshop" (CTA) | 5 |
| "Where does the workshop take place?" | 2 |
| Diverse FAQ clicks (parking, dates, money back, ticket, starttijd) | 5 |
| `www.startyourballoonbusiness.com/booking` link | 1 |
| Overige niet-getaggede clicks | 15 |

## 4. Funnel Drop-off

```
Meta impressions (5.993)
  → Link clicks (78, 1,3%)
    → Meta LPV (63, 81% van clicks)
      → PH sessies op landing (91 — incl. overlap/retargeting/repeat)
        → Scroll 50%+ (~7 van 22 leave-events, ~31%)
          → CTA click "Go to workshop" (5, ~5,5% sessies)
            → /booking pageview (1)
```

**Grootste lek:** tussen **landing** en **50% scroll**. Van elke 10 mensen die de pagina openen scrollen er ruwweg 3 voorbij de helft. Dit is de root cause van de lage CTA en boekingen — het aanbod bereikt de meeste bezoekers niet visueel.

**Tweede lek:** **scroll → CTA → /booking**. Zelfs van de 5 "Go to workshop" clicks komt er slechts 1 aan op `/booking`. Check of de CTA daadwerkelijk naar `/booking` routeert (mogelijk naar extern ticketsysteem of modal dat geen pageview triggert).

## 5. Rode Vlaggen

- **Bounce rate 84,6%** — 30 punten boven 55%-target (🚨 kritiek, verder opgelopen vs 7d avg van 81,7%).
- **Avg session duration 16,9s** — 62% onder het 7d-gemiddelde (44s), 81% onder target (90s). Zware daling op één dag.
- **CPC €0,62** — 24% boven target van €0,50 en 11% hoger dan 7d avg.
- **CPM €14,44** — 24% hoger dan 7d avg; auction druk neemt toe of creatives vermoeien.
- **H11 budget-dominantie** — 76% van de spend naar de slechtst presterende actieve variant (hoogste CPC, laagste CTR).
- **H12 onderbenut** — top CTR/CPC maar slechts 10% van de spend; learning wordt niet geëxploiteerd.
- **Funnel gap CTA → /booking** — 5 "Go to workshop" clicks, maar slechts 1 `/booking` pageview. Mogelijk tracking- of routingprobleem.
- **Scroll data sparse** — slechts 22 van 91 sessies sturen `$pageleave`; 69 sessies (76%) verlaten waarschijnlijk zonder enige interactie of event (consistent met ~85% bounce).

## 6. Top 3 Acties voor Vandaag

1. **Budget herverdelen richting H12.** Stijg H12 van ~€8 naar €35-40/dag en verlaag H11 naar €35-40/dag. H12 heeft 2x de CTR en 56% lagere CPC — dat is bewezen, niet experimenteel. Dit kan alleen als de campagne-budgetstructuur dit toelaat (ABO). Bij CBO: pauzeer of duplicer H11 en H13 met lager budget om Meta te sturen.
   - **Waarom:** H12 CTR 4,24% vs 2,08% H11; kost per LPV €0,74 vs €1,57.
   - **Verwachte impact:** 20-30% lagere blended CPC binnen 3-5 dagen als H12 het volume aankan.
   - **Escalatie:** 🟡 Geel (Robin goedkeuring).

2. **Fix de landing page hero-sectie — diagnose + hypothese.** Scroll 25% is slechts 31,8%; d.w.z. 68% van de bezoekers scrollt niet eens voorbij de fold. Open 2-3 session recordings van gisteren (m.n. H11 traffic) en identificeer of het (a) laadtijd, (b) above-the-fold copy mismatch, of (c) mobiele rendering betreft. Zet 1 duidelijke hero-test op voor volgende week: hook-match met H12 ad copy.
   - **Waarom:** Grootste lek in funnel; alle optimalisaties downstream (CTA, offer) zijn verspild als niemand het ziet.
   - **Verwachte impact:** bij 10pp verbetering in scroll 50%+ verdubbelt de effectieve lead flow.
   - **Escalatie:** 🟠 Oranje (Wix Editor + copy review).

3. **Valideer CTA → /booking tracking.** Klik zelf vanuit de ad op de CTA "Go to workshop" en controleer of `/booking` pageview in PostHog verschijnt. 5 CTA clicks vs 1 `/booking` pv gisteren suggereert ofwel een redirect naar een extern ticketplatform (zonder PH pixel) ofwel een JS-routing die de `$pageview` niet triggert.
   - **Waarom:** Zonder betrouwbare booking tracking is de downstream conversie rate niet meetbaar en kunnen we H12-winst niet valideren.
   - **Verwachte impact:** directe meetbaarheid van conversies; mogelijk "verborgen" boekingen die nu niet geteld worden.
   - **Escalatie:** 🟢 Groen (kan Robin zelf doen in 5 min).

---

## Bronnen
- **Meta Ads:** Pipeboard MCP, campaign ID `120239435987290239`, account `act_567892422940728`, tijdsvenster `2026-04-17` (dag) + `2026-04-10 t/m 2026-04-16` (7d baseline).
- **PostHog:** project `Default project` (id 149694), host `www.startyourballoonbusiness.com`, HogQL queries op `events` tabel.
- Rapport gegenereerd op 2026-04-18.
