# SYBB Daily Report — 20 June 2026

> Gegenereerd op 21 June 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP.
> Rapportperiode: gisteren = **20 June 2026**.

## 1. Samenvatting
De SYBB funnel stond gisteren **stil**. De Meta-campagne `2026: SYBB` is **PAUSED** en had op 20 June 2026 geen enkele delivery (geen spend, impressions of clicks); dit geldt voor de volledige laatste 30 dagen. Daardoor was er ook geen betaald verkeer richting de landingspagina. **Belangrijkste actie:** beslis of de campagne weer aangezet wordt, want zonder delivery komen er geen leads binnen.

> ⚠️ **Datawaarschuwing:** de **PostHog MCP was tijdens deze run niet beschikbaar** (server exposeert geen tools, geen resources). De Landing Page Health en Funnel Drop-off secties konden daardoor **niet** gevuld worden. Conform de strikte regel voor deze run is er geen alternatieve (Google) databron gebruikt en zijn er geen cijfers geschat. Draai het rapport opnieuw zodra de PostHog MCP weer verbonden is.

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (id `120239435987290239`) — status **PAUSED**, daily budget €100,00, objective OUTCOME_SALES.

| Metric | Gisteren (20 Jun) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Toelichting:** Meta retourneert een lege dataset voor zowel gisteren als de volledige periode 22 May – 21 June 2026. De campagne heeft in die periode niet gelopen (geen impressies of spend op enige dag). Er is dus geen 7-daags gemiddelde om tegen af te zetten.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | geen delivery | — | — | PostHog n.b. | PostHog n.b. |

**Beste variant:** niet te bepalen — geen enkele ad leverde gisteren impressies/clicks.
**Slechtste variant:** niet te bepalen — zie hierboven.

## 3. Landing Page Health
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n.b. | n.b. | <55% | ⚪ |
| Avg Session Duration | n.b. | n.b. | >90s | ⚪ |
| Scroll 25% | n.b. | n.b. | >80% | ⚪ |
| Scroll 50% | n.b. | n.b. | >60% | ⚪ |
| Scroll 75% | n.b. | n.b. | >40% | ⚪ |
| Scroll 100% | n.b. | n.b. | >20% | ⚪ |
| CTA Click Rate | n.b. | n.b. | >4% | ⚪ |

⚪ = data niet beschikbaar. **PostHog MCP niet verbonden tijdens deze run** — `startyourballoonbusiness.com` analytics konden niet worden opgehaald. Geen schatting gemaakt (strikte regel: alleen PostHog MCP als bron voor LP-data).

## 4. Funnel Drop-off
Niet te berekenen. Stap 1 (pageview) vereist PostHog-data, en er was bovendien geen betaald verkeer vanuit Meta.

Pageview (n.b.) → Scroll 50% (n.b.) → CTA Click (n.b.) → /booking (n.b.)

**Grootste lek:** niet vast te stellen zonder PostHog-data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne PAUSED / nul delivery** — `2026: SYBB` levert al ≥30 dagen geen impressies. Zonder delivery: 0 verkeer, 0 leads, 0 omzet uit deze funnel.
- 🚩 **PostHog MCP onbereikbaar** — geen zicht op landingspagina-gedrag, bounce, scroll of CTA-clicks. Monitoring van de funnel is op dit moment blind aan de PostHog-kant.

## 6. Top 3 Acties voor Vandaag
1. **Beslis over de campagnestatus.** `2026: SYBB` staat op PAUSED met €100/dag budget klaar. Bepaal of dit bewust is (campagne afgelopen / in heropbouw) of dat hij weer live moet. **Impact: hoog — dit bepaalt of de funnel überhaupt verkeer krijgt. Snelheid: direct (Meta Ads Manager).**
2. **Herstel de PostHog MCP-verbinding.** Zonder PostHog mist het dagelijkse rapport de helft van zijn waarde (LP health + funnel). Controleer de MCP-config en draai dit rapport opnieuw zodra de bron weer verbonden is. **Impact: hoog — herstelt monitoring. Snelheid: snel (config/herstart).**
3. **Bij heractivering: controleer tracking vooraf.** Voordat de campagne weer aangaat, verifieer dat de UTM-conventie (`utm_content=hXX_bX_ctaX`) en de Meta Pixel correct vuren op `startyourballoonbusiness.com`, zodat de eerste live dag meteen bruikbare cross-reference data oplevert. **Impact: middel — voorkomt blinde herstart. Snelheid: medium.**

---
*Bronstatus: Meta Ads MCP = verbonden (lege dataset, campagne paused). PostHog MCP = niet beschikbaar tijdens run. Geen Google-bronnen gebruikt; niet weggeschreven naar de Tracker Google Sheet.*
