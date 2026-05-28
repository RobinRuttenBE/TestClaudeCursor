# SYBB Daily Report, 27 May 2026

## 1. Samenvatting

De SYBB funnel staat operationeel stil. Meta campagne "2026: SYBB" is PAUSED (laatste update 19 april 2026), dus geen ad spend, geen paid clicks, geen UTM gerelateerde landingen. PostHog registreert organisch 1 pageview op 27 mei vanuit een YouTube referral, in lijn met het magere 7d gemiddelde van 1,3 pageviews per dag. Topactie: knoop doorhakken over reactivering of formeel afblazen tot er nieuw budget en hooks klaarliggen.

## 2. Meta Ads Performance

**Campaign status:** `2026: SYBB` (id 120239435987290239) staat op **PAUSED** sinds 19 april 2026, daily budget 100,00 euro is bevroren. De duplicate `2026: SYBB - Kopie` (id 120243293329420239) staat eveneens op PAUSED. Geen impressions, clicks of spend vanuit Pipeboard Meta Ads MCP over 2026-05-20 t/m 2026-05-27.

| Metric | 27 May | 7d Gemiddelde (20-26 May) | Trend |
|--------|--------|---------------------------|-------|
| Spend | 0,00 euro | 0,00 euro | flat |
| Impressions | 0 | 0 | flat |
| Clicks | 0 | 0 | flat |
| CTR | n.v.t. | n.v.t. | flat |
| CPC | n.v.t. | n.v.t. | flat |
| Frequency | n.v.t. | n.v.t. | flat |

### Ad Variant Performance

Niet rapporteerbaar. Geen actieve ads, dus geen variantdata per `utm_content` (h11_b3_cta5 t/m h15_b3_cta5).

**Beste variant:** n.v.t. zolang campagne paused is.
**Slechtste variant:** n.v.t. zolang campagne paused is.

## 3. Landing Page Health

Bron: PostHog `$pageview` events met `$host` icontains `startyourballoonbusiness.com`, project "Default project" (id 149694). Bounce rate, scroll depth en CTA click rate zijn niet aanwezig als events in PostHog (alleen standaard PostHog events $pageview, $rageclick, $dead_click, $exception). Volume is daarnaast te laag (n=1 op 27 mei, n=9 over 7 dagen) voor betrouwbare ratios.

| Metric | 27 May | 7d Gemiddelde | Target | Status |
|--------|--------|---------------|--------|--------|
| Pageviews | 1 | 1,3 / dag | n.v.t. | rood (zonder paid traffic) |
| Unique Visitors | 1 | 1,3 / dag | n.v.t. | rood |
| Unique Sessions | 1 | 1,3 / dag | n.v.t. | rood |
| Avg Session Duration | 61 s | ~22 s (sterk vertekend door dagen met 0 sessies) | >90 s | geel |
| Bounce Rate | n.v.t. (geen $pageleave events) | n.v.t. | <55% | geen data |
| Scroll 25 / 50 / 75 / 100% | n.v.t. (geen scroll events) | n.v.t. | >80 / 60 / 40 / 20% | geen data |
| CTA Click Rate | n.v.t. (geen CTA click events) | n.v.t. | >4% | geen data |
| Rageclicks | 0 | 0 | 0 | groen |
| Dead clicks | 0 | 0 | 0 | groen |
| Exceptions | 0 | 0 | 0 | groen |

**Bronnen 27 May:** youtube (1).
**Bronnen 20-26 May:** instagram (3), facebook (2), youtube (0), geen utm_source (4).
**Pathnames:** 100% landt op `/` (homepage). Geen views op `/booking`, `/checkout` of vervolgpaginas.
**UTM content 27 May:** `bio_link` (1). Geen `h*_b*_cta*` patroon, bevestigt dat het geen ad traffic is.

## 4. Funnel Drop-off

Pageview homepage (1) -> Scroll 50% (geen data) -> CTA Click (geen data) -> `/booking` view (0).

**Grootste lek:** structureel. Zonder gemeten scroll, CTA click of booking pageview kan PostHog de funnel niet meten. De feitelijke trechter is een single-page bezoek dat doodloopt op de homepage zonder een vervolgactie te triggeren in PostHog.

## 5. Rode Vlaggen

- **Campagne PAUSED zonder restart datum.** Daily budget 100 euro staat sinds 19 april stil, terwijl PostHog 0 paid clicks ziet. Dit blokkeert elke vorm van funnel optimalisatie.
- **Geen funnel telemetrie op LP.** Scroll depth, CTA clicks en `/booking` pageviews worden niet gecaptured door PostHog (alleen autocapture events). Zelfs als ads weer aanstaan ontbreekt het meetraam.
- **Volume te laag voor signaal.** 9 pageviews in 7 dagen, met 3 dagen op 0. Iedere ratio op deze basis is ruis.
- **Single utm_content waarde organisch.** Alleen `bio_link` traffic, geen ad-attributie zichtbaar.

## 6. Top 3 Acties voor Vandaag

1. **Besluit nemen over `2026: SYBB` reactivering.** Wat: kies vandaag voor reactiveren (met welke hooks en welk budget) of formeel afblazen. Waarom: campagne staat 38 dagen op pauze met 100 euro per dag bevroren budget, geen leads, geen learnings. Hoe: open Meta Ads Manager via account act_567892422940728, ofwel status -> ACTIVE met geverifieerde creatives, ofwel duplicate (`2026: SYBB - Kopie`) eerst opfrissen. Impact: zonder dit besluit blijft elk rapport leeg. Escalatie: rood, strategiebeslissing Robin.
2. **PostHog landing page tracking uitbreiden.** Wat: voeg scroll-depth en CTA click captures toe op startyourballoonbusiness.com. Waarom: zelfs bij heractivering van ads kan dit rapport geen bounce, scroll of CTA rate berekenen. Hoe: PostHog snippet uitbreiden met `posthog.capture('cta_clicked', {...})` op de Book Now button en scroll milestones via `posthog-js` autocapture extension (Wix custom code). Impact: maakt de KPI tabel echt invulbaar. Escalatie: oranje, Wix Editor + PostHog config.
3. **Brief de bio_link traffic op.** Wat: stuur de YouTube en Instagram bio_link bezoekers naar een instrumented variant met `utm_source=bio&utm_campaign=organic&utm_content=bio_link_v1`. Waarom: enige consistente traffic bron op dit moment; momenteel landt 4 van 9 sessies zonder utm_source dus is attributie onmogelijk. Hoe: update bio links in Linktree / Instagram / YouTube met UTM standaard uit `tracking-standards`. Impact: geeft minimaal een baseline voor organische conversie zolang ads uit staan. Escalatie: groen, direct uitvoerbaar.

---

**Bronnen:**
- Meta Ads MCP (Pipeboard), accounts act_567892422940728 + act_1489853856181844, 27 May 2026 en 20-26 May 2026
- PostHog MCP project "Default project" (id 149694), org Sempertex Europe, `$pageview` getrendd op `$host` icontains `startyourballoonbusiness.com`, 20-27 May 2026

**Notities:**
- Schema check via `read-data-schema` toont alleen standaard PostHog events op deze property. Custom events `cta_clicked`, `scroll_50`, `booking_started` zijn niet aanwezig, dus targets uit SKILL.md zijn momenteel onmeetbaar.
- Bounce rate en scroll depth zijn bewust niet gefabriceerd, in plaats daarvan staat "geen data".
- Niets geschreven naar Google Sheet of Google Drive op verzoek van de run-instructie.
