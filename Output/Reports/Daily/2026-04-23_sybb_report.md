# SYBB Daily Report, 2026-04-23

## 1. Samenvatting
Campagne "2026: SYBB" stond gisteren op PAUSED. Nul ad spend, nul impressies, nul ad clicks. De landingspagina kreeg slechts 4 pageviews van 3 sessies, allemaal via `utm_content=bio_link` (organisch / Instagram bio). Rapport dient vandaag vooral als baseline-controle en herstart-checklist, niet als performance-analyse.

## 2. Meta Ads Performance

**Campagne:** 2026: SYBB (ID 120239435987290239), status PAUSED op 2026-04-23.

| Metric | Gisteren (2026-04-23) | 7d totaal (2026-04-16 t/m 2026-04-22) | Trend |
|--------|-----------------------|----------------------------------------|-------|
| Spend | €0,00 | €283,02 | ↓ (campagne off) |
| Impressions | 0 | 19.726 | ↓ |
| Clicks (all) | 0 | 457 | ↓ |
| Link clicks | 0 | 268 | ↓ |
| CTR | n/a | 2,32% | ↓ |
| CPC | n/a | €0,62 | n/a |
| Frequency | n/a | 1,80 | n/a |
| Reach | 0 | 10.960 | ↓ |
| Landing page views (Meta) | 0 | 229 | ↓ |
| Add to cart | 0 | 16 (waarde €5.600) | ↓ |
| Initiate checkout | 0 | 14 (waarde €4.900) | ↓ |
| Complete registration | 0 | 1 (waarde €42.350) | ↓ |

### Ad Variant Performance (gisteren)
Geen actieve ads. Onderstaand de 7d UTM-splitsing vanuit PostHog (2026-04-16 t/m 2026-04-22) als referentie voor de eerstvolgende restart.

| utm_content | Sessies (7d) | Pageviews (7d) | PV/sessie |
|-------------|--------------|----------------|-----------|
| h11_b3_cta5 | 252 | 298 | 1,18 |
| h13_b3_cta5 | 124 | 133 | 1,07 |
| h12_b3_cta5 | 66 | 85 | 1,29 |
| bio_link | 7 | 10 | 1,43 |
| h14_b3_cta5 | 1 | 1 | 1,00 |
| test123 | 1 | 2 | 2,00 |

**Beste variant (7d):** h12_b3_cta5 haalt hoogste PV/sessie (1,29), wijst op meest betrokken bezoek. h11_b3_cta5 levert het grootste volume (252 sessies) maar lagere diepte.
**Slechtste variant (7d):** h13_b3_cta5 heeft forse share (124 sessies) maar laagste PV/sessie (1,07), suggereert oppervlakkig verkeer of ad/page-mismatch.
**Noot:** Een `test123` UTM (2 pageviews) is een QA-leak, die UTM-waarde hoort niet in een live ad te staan.

## 3. Landing Page Health

**Site:** www.startyourballoonbusiness.com (let op: host wordt met `www.` geregistreerd in PostHog, niet zonder).

| Metric | Gisteren (2026-04-23) | 7d totaal (2026-04-16 t/m 2026-04-22) | Target | Status |
|--------|-----------------------|----------------------------------------|--------|--------|
| Pageviews | 4 | 569 | n/a | n/a |
| Unique visitors | 3 | 451 | n/a | n/a |
| Sessies | 3 | 466 | n/a | n/a |
| Bounce proxy (PV=1 / sessie) | hoog, te weinig data | ~80% | <55% | 🔴 (proxy) |
| Avg session duration (PV≥2 subset) | n/a (geen multi-PV sessies) | ~145s op betrokken sessies | >90s | 🟢 (alleen voor multi-PV subset) |
| Scroll 25% | geen data | geen distributie beschikbaar | >80% | ⚠ |
| Scroll 50% | geen data | geen distributie beschikbaar | >60% | ⚠ |
| Scroll 75% | geen data | geen distributie beschikbaar | >40% | ⚠ |
| Scroll 100% | geen data | geen distributie beschikbaar | >20% | ⚠ |
| CTA Click Rate | 1 autocapture / 4 PV = 25% (n=1, statistisch ruis) | 262 autocaptures / 569 PV ≈ 46% (breed, incl. niet-CTA) | >4% | ⚠ niet specifiek genoeg |

**Belangrijke observaties datakwaliteit:**
- `$pageleave` wordt nauwelijks gevuurd (0 op 2026-04-23, 139 over 7d terwijl er 466 sessies waren). Dit ondermijnt zowel bounce rate als session duration.
- De PostHog event voor scroll depth (`$prev_pageview_max_scroll_percentage`) zit alleen op bezoeken met opvolgend pageview. Huidige distributie per drempel (25/50/75/100) is niet te berekenen uit de beschikbare data.
- Er is geen dedicated `cta_click` event. "CTA clicks" moeten nu worden afgeleid uit `$autocapture`, wat zowel echte CTA-klikken als andere klikken telt.

## 4. Funnel Drop-off

Funnel niet betrouwbaar te berekenen voor gisteren (n=3 sessies).

Indicatief voor 7d (2026-04-16 t/m 2026-04-22) op basis van Meta + PostHog:
```
Meta link clicks (268)  →  Meta LP views (229)      →  PostHog sessies (466*)  →  Initiate checkout (14)   →  Complete registration (1)
     100%                      85,4%                        zie noot                    5,2% van Meta LPV          0,4%
```
*PostHog telt 466 sessies terwijl Meta 229 LP views meldt. Dit verschil komt van organisch/direct + `bio_link` + niet-Meta bronnen. Cross-check vereist.

**Grootste lek (7d):** Tussen Initiate Checkout (14) en Complete Registration (1). Dat is 92,9% drop-off in de laatste stap, ruim boven normaal voor een B2C/B2B workshop funnel. Prioriteit 1 bij restart.

## 5. Rode Vlaggen

- **Campagne volledig uit.** Status PAUSED, geen ad spend op 2026-04-23. Als dit onbedoeld is, prioriteit 0.
- **Volume collapse vanaf 2026-04-21.** PostHog sessies vielen van 75 (20e) naar 0 (21e) naar 3 (22e) naar 3 (23e). Consistent met pause-moment rond 20/21 april.
- **Scroll depth telemetrie ontbreekt.** Voor de 4 pageviews van gisteren is geen enkele scroll-metric beschikbaar. Ook over 7d zijn alleen 126 records gevonden, terwijl er 569 pageviews waren. PostHog scroll tracking is niet consistent geïmplementeerd op de Wix pagina.
- **`$pageleave` ondergerapporteerd.** Dit maakt bounce rate en session duration onbetrouwbaar. Moet vóór restart opgelost.
- **QA-leak UTM `test123`** heeft 2 pageviews ontvangen op 2026-04-18. Test/staging traffic lekt naar production UTM-namespace.
- **Complete registration drop-off 92,9%** (7d). Laatste funnel-stap bloedt.

## 6. Top 3 Acties voor Vandaag

1. **Bevestig campagne-status en bepaal restart-datum.**
   - Wat: controleer of PAUSED op 2026-04-23 intentioneel was (bv. wachtend op nieuwe creatives of budget-review). Zo nee, campagne vandaag activeren.
   - Waarom: geen spend, geen data, geen progress. Elke dag paused is verloren leertijd op de campagne.
   - Hoe: Meta Ads Manager, campagne "2026: SYBB" (ID 120239435987290239). Handmatige check door Robin.
   - Verwachte impact: herstel van de ~90+ dagelijkse sessies en de eerste funnelstappen.
   - Escalatie: Geel (Robin goedkeuring).

2. **Scroll-depth en `$pageleave` tracking fixen in PostHog/Wix.**
   - Wat: verifieer dat PostHog autocapture config `capture_pageleave: true` en `capture_performance: true` aan heeft staan, en dat scroll-events op de Wix SYBB-pagina vuren.
   - Waarom: zonder deze events zijn bounce rate, session duration en scroll-depth niet rapporteerbaar. Rapportstructuur vereist deze metrics en ze ontbreken al meerdere dagen.
   - Hoe: PostHog dashboard project 149694 → snippet config check, plus Wix custom code block inspecteren. Daarna 1 testsessie draaien op productie-URL.
   - Verwachte impact: volledige scroll-funnel en echte bounce rate zichtbaar vanaf volgende rapport.
   - Escalatie: Oranje (Wix Editor + PostHog settings).

3. **Verwijder QA-UTM `test123` uit productie en documenteer UTM-namespace.**
   - Wat: audit alle live ads en kill switches op testtrafiek richting productie-UTMs. Voeg vaste prefix (bv. `qa_`) toe voor test-UTMs in CLAUDE.md / tracking-standards skill.
   - Waarom: 2 productie-pageviews met `test123` op 2026-04-18 vervuilen rapportage en kunnen Meta-attributie scheeftrekken.
   - Hoe: Pipeboard / Meta Ads Manager creative-review + update van `tracking-standards` skill.
   - Verwachte impact: schone UTM-data, geen ruis in variant-vergelijking bij restart.
   - Escalatie: Groen (auto na review).

---

**Data bronnen:** Meta Ads via Pipeboard MCP (account act_567892422940728, campagne 120239435987290239). PostHog MCP project 149694 "Default project", host `www.startyourballoonbusiness.com`. Geen Google-services gebruikt voor deze run.
