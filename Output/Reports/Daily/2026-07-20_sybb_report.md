# SYBB Daily Report: 20 juli 2026

## 1. Samenvatting
De SYBB funnel stond gisteren praktisch stil. De Meta campagne **"2026: SYBB" is PAUSED** en heeft de hele week (14 t/m 20 juli) nul euro besteed, dus er komt geen betaald verkeer binnen. De landingspagina (www.startyourballoonbusiness.com) kreeg gisteren slechts 6 pageviews, uitsluitend direct verkeer (waarvan 2 bots), met 100% bounce en nul CTA clicks. Kortom: zonder actieve ads ligt de hele acquisitie stil. Dit is de belangrijkste bevinding van vandaag.

## 2. Meta Ads Performance
Campagne **"2026: SYBB"** (id 120239435987290239) staat op **PAUSED**. Ingesteld dagbudget €100, maar geen enkele dag deze week actief. Alle metrics zijn nul.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen actieve ads) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t., campagne is gepauzeerd.
**Slechtste variant:** n.v.t., campagne is gepauzeerd.

## 3. Landing Page Health
Bron: PostHog, host www.startyourballoonbusiness.com. Gisteren 6 pageviews / 6 sessies / 6 unieke bezoekers. Elke sessie was 1 pageview (single-page), dus bounce rate 100%. Er werden alleen $pageview en $web_vitals events geregistreerd: geen scroll-events, geen CTA clicks, geen conversies.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | 100% | 100% | <55% | 🔴 |
| Avg Session Duration | ~0s (single-page) | ~0s | >90s | 🔴 |
| Scroll 25% | geen data | geen data | >80% | 🔴 |
| Scroll 50% | geen data | geen data | >60% | 🔴 |
| Scroll 75% | geen data | geen data | >40% | 🔴 |
| Scroll 100% | geen data | geen data | >20% | 🔴 |
| CTA Click Rate | 0% | 0% | >4% | 🔴 |

Let op: scroll-depth wordt momenteel niet gemeten op deze pagina (er komen geen scroll-events binnen in PostHog). Zolang de campagne uit staat en er geen echt verkeer is, is dit niet urgent, maar het moet werken voordat de ads weer live gaan.

### Verkeersbron gisteren
| Segment | Pageviews | Type |
|---------|-----------|------|
| Direct, Chrome, US | 4 | Regular (mens) |
| Direct, Edge, CN | 2 | Bot |

- 100% direct verkeer, 0% UTM-getagd, 0% vanuit Meta.
- 33% van het verkeer (2 van 6) is door PostHog als bot geclassificeerd.

## 4. Funnel Drop-off
Pageview (6, 100%) → Scroll 50% (geen data) → CTA Click (0, 0%) → /booking (0, 0%)

**Grootste lek:** De funnel begint niet eens. Er is geen instroom van betaald verkeer (campagne PAUSED) en het handjevol directe bezoekers converteert op geen enkele stap. Alle 6 bezoekers verlieten de pagina na 1 pageview.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne PAUSED:** "2026: SYBB" bestede €0 gisteren en de hele week. Geen paid traffic naar de funnel. Dit is de hoofdoorzaak van alle andere nullen.
- 🚩 **Bounce rate 100%:** alle 6 sessies waren single-page. Geen enkele bezoeker ging dieper de pagina in.
- 🚩 **0 CTA clicks:** nul interactie. (Aantal bezoekers is te laag om dit als losstaand ad-pagina probleem te lezen, het is een gevolg van de gepauzeerde campagne.)
- 🚩 **Bot-aandeel 33%:** 2 van de 6 pageviews zijn bots. Bij dit lage volume vertekent dat elke ratio.
- 🚩 **0% UTM-getagd verkeer:** er is op dit moment geen enkele meetbare koppeling tussen ad en pagina, logisch nu er geen ads draaien.

## 6. Top 3 Acties voor Vandaag
1. **Besluit over de campagne "2026: SYBB" (hoogste prioriteit).** Zolang deze op PAUSED staat, staat de volledige SYBB acquisitie stil en levert dit rapport elke dag nullen op. Actie: heractiveer de campagne in Meta Ads Manager (dagbudget €100 staat klaar) of leg expliciet vast dat SYBB bewust gepauzeerd blijft, zodat we niet elke ochtend een leeg rapport draaien. Escalatie: Rood (strategie, Robin beslist).
2. **Controleer UTM-tagging vóór heractivatie.** Nu is 0% van het verkeer getagd. Zorg dat de ad-URL's de conventie `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX` volgen, zodat we ad-variant vs. landingspaggedrag kunnen kruisen zodra verkeer binnenkomt. Escalatie: Geel (Robin goedkeuring).
3. **Verifieer de tracking op de landingspagina.** Er komen geen scroll- of CTA-events binnen in PostHog en 33% van het minieme verkeer is bot. Bevestig dat scroll-depth en CTA-click events correct vuren en overweeg bot-filtering, zodat het rapport echte engagement kan meten zodra de ads weer live zijn. Escalatie: Oranje (implementatie op de pagina).

---
*Databronnen: Meta Ads via Pipeboard MCP (campagne 2026: SYBB, account act_567892422940728) en PostHog MCP (project Default project, host www.startyourballoonbusiness.com). Periode: 20 juli 2026, met 7-daagse vergelijking 14 t/m 20 juli 2026. Geen andere bronnen geraadpleegd.*
