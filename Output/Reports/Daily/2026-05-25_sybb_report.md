# SYBB Daily Report — 25 May 2026

## 1. Samenvatting
Campagne "2026: SYBB" staat al meer dan 30 dagen op PAUSED, dus geen Meta Ads spend, impressies of clicks op 25 mei. De landing page kreeg ook nul pageviews gisteren; alle traffic in de afgelopen week (16 pageviews) kwam organisch binnen via Instagram/Facebook bio links met een bounce rate van 93,3%. Zonder actieve ads en zonder organische pull is de funnel effectief stil.

## 2. Meta Ads Performance

| Metric | Gisteren (25-05) | 7d Gemiddelde (18-24/05) | Trend |
|--------|------------------|--------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Campagne status:** PAUSED sinds vóór 25 april 2026 (laatste update campagne: 19 april). Geen actieve ad sets, geen actieve ads.

**Lifetime context (13 jan – 26 mei):** €2.485 spend, 297K impressions, 12.067 clicks, CTR 4,06%, CPC €0,21, 6 purchases, 15 leads, 6.992 landing page views, frequency 2,24.

### Ad Variant Performance
Geen data: campagne PAUSED, geen impressies of clicks per variant op 25 mei.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

| Metric | Gisteren (25-05) | 7d Gemiddelde (18-24/05) | Target | Status |
|--------|------------------|--------------------------|--------|--------|
| Pageviews | 0 | 16 totaal / ~2,3 per dag | groei | 🔴 |
| Sessies | 0 | 15 totaal | groei | 🔴 |
| Unique Visitors | 0 | 15 | groei | 🔴 |
| Bounce Rate | n.v.t. | 93,3% | <55% | 🔴 |
| Avg Session Duration | n.v.t. | 193s | >90s | 🟢 (kleine n) |
| Scroll 25% | niet getrackt | niet getrackt | >80% | ⚪ |
| Scroll 50% | niet getrackt | niet getrackt | >60% | ⚪ |
| Scroll 75% | niet getrackt | niet getrackt | >40% | ⚪ |
| Scroll 100% | niet getrackt | niet getrackt | >20% | ⚪ |
| CTA Click Rate | niet getrackt | niet getrackt | >4% | ⚪ |

**Bronnen 7d:** 100% organisch via `t-sml.mtrbio.com` bio link (utm_source=facebook/instagram, utm_medium=organic, utm_campaign=sybb, utm_content=bio_link) plus enkele directe en Google Android-app visits.

**Tracking gap:** PostHog vangt op deze property momenteel geen scroll-depth events of CTA-click custom events. Alleen `$pageview` events worden geregistreerd op `www.startyourballoonbusiness.com`. Zonder die signalen kunnen scroll- en CTA-targets niet gemeten worden.

## 4. Funnel Drop-off

Gisteren: geen funnel data (0 pageviews).

7d funnel (18-24 mei, n=15 sessies):
- Pageview LP: 15 (100%)
- Scroll 50%: niet meetbaar
- CTA click: niet meetbaar
- Pageview /checkout: 1 (6,7%) — één enkele bezoeker via Instagram bio_link kwam tot de checkout pagina

**Grootste lek:** Niet vast te stellen door ontbrekende scroll- en CTA-events. De 93,3% bounce rate suggereert dat verreweg de meeste bezoekers de homepage verlaten zonder een tweede pageview, maar zonder scroll-tracking is het onduidelijk of ze de hero zien of direct weg klikken.

## 5. Rode Vlaggen 🚩

- 🔴 **Campagne PAUSED, geen budget actief.** Geen spend in last_30d. Zonder herstart komt er geen betaalde traffic binnen.
- 🔴 **Nul ad traffic naar de LP gisteren.** Direct gevolg van de gepauzeerde campagne.
- 🔴 **Bounce rate 93,3% over 7 dagen.** Boven de >70% red flag drempel uit de skill. Wel op een zeer kleine sample (15 sessies), dus statistisch zwak signaal.
- 🟡 **Tracking gap: geen scroll-depth en geen CTA-click events.** Het skill verwacht beide; PostHog ziet ze niet op deze property. Hierdoor zijn 5 van de 7 KPI-rijen onmeetbaar.
- 🟡 **/checkout zonder /booking events.** Het skill verwacht een `/booking` stap; de gevonden conversie pagina is `/checkout` (Wix shop). UTM-conventie en funnel definitie wijken af van wat in CLAUDE.md / SKILL staat.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: SYBB campagne herstarten of definitief afsluiten.**
   - **Waarom:** Campagne staat al >30 dagen op PAUSED, levert nul nieuwe data op en blokkeert daarmee zowel het dagelijkse rapport als verdere ad-optimalisatie.
   - **Hoe:** Open Meta Ads Manager → campagne "2026: SYBB" (ID 120239435987290239). Optie A: nieuwe daily budget (huidig €100/dag) en zet ACTIVE op de winnende ad sets uit lifetime data. Optie B: archiveer en bouw een nieuwe campagne met verse creatives.
   - **Verwachte impact:** Activering met €100/dag → bij lifetime CPC €0,21 ca. 475 clicks/dag en op CTR 4% ca. 12K impressies/dag. Daarmee komt het rapport weer betekenisvol vooruit.
   - **Escalatie:** Oranje (Robin goedkeuring, budget + status).

2. **Fix scroll-depth en CTA-click tracking op startyourballoonbusiness.com.**
   - **Waarom:** 5 van 7 KPI-rijen in dit rapport zijn `niet getrackt`. Zonder deze events kan het skill geen kwalitatieve LP-diagnose maken, ook niet zodra ads weer live gaan.
   - **Hoe:** Wix Editor → site code → custom PostHog snippet voor (a) `$pageview` met `scrollDepth` listener (PostHog autocapture scroll mile-markers) en (b) `posthog.capture('cta_click', {...})` op de "Book Now" knop. Test in incognito en check `read-data-schema` op `cta_click` event.
   - **Verwachte impact:** Volledige 🟢/🟡/🔴 status op alle KPI's vanaf morgen, plus bruikbare cross-reference data tussen ad CTR en LP scroll.
   - **Escalatie:** Oranje (Wix Editor toegang nodig).

3. **Forceer minimaal één funnel stap voorbij de homepage via de bio link strategie.**
   - **Waarom:** De enige werkende traffic bron (bio_link, n=14 in 7d) levert 93% bounce. Slechts 1 bezoeker bereikte /checkout. Het workshop aanbod komt blijkbaar niet hard genoeg over op de homepage.
   - **Hoe:** Op de bio link landing in mtrbio of in een hero overlay op de homepage: voeg een directe "See the workshop programme →" link toe die naar `/checkout` of een dedicated workshop sectie scrollt. Houd UTM intact (`utm_content=bio_link`) en log een aparte `cta_click` event zodat we de improvement morgen kunnen meten.
   - **Verwachte impact:** Bij gelijke traffic verwachten we tweede pageview rate van 7% (huidig) naar 20%+ en bounce rate omlaag richting 75%.
   - **Escalatie:** Geel (Robin keuze: bio-link copy of LP hero).

---

### Cross-reference notes
- Ad CTR vs LP Bounce: n.v.t. gisteren (geen ads).
- Ad Variant vs LP Behavior: n.v.t. gisteren.
- Bio_link organisch verkeer toont hoge bounce + goede avg duration (193s). De kleine n maakt het signaal zwak, maar de combinatie (lang op pagina, geen tweede view) wijst op lezers die de homepage scannen maar geen volgende stap zien.
- UTM in bio link gebruikt `utm_medium=organic` (niet `cpc`) en `utm_content=bio_link` — afwijkend van de cpc-conventie uit CLAUDE.md, hier wel correct omdat dit organisch is.

### Data scope
- **Meta Ads bron:** Pipeboard Meta Ads MCP, account `act_567892422940728` (Sempertex Ad Account), campagne ID `120239435987290239`.
- **PostHog bron:** project Default project (149694), host `www.startyourballoonbusiness.com`.
- **Periode gisteren:** 2026-05-25 00:00–23:59 UTC.
- **Periode 7d gemiddelde:** 2026-05-18 t/m 2026-05-24 UTC.
