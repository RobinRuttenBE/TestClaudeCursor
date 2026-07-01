# SYBB Daily Report — 30 June 2026

> **Databronnen:** Meta Ads MCP (Pipeboard) ✅ · PostHog MCP ⚠️ niet beschikbaar deze run
> **Campagne:** `2026: SYBB` (ID 120239435987290239) — account `Sempertex Ad Account` (act_567892422940728)

## 1. Samenvatting
Er is op 30 juni **geen SYBB-activiteit** om te rapporteren. De campagne `2026: SYBB` staat op **PAUSED** en had over de hele periode 24–30 juni **nul delivery**: geen spend, geen impressions, geen clicks. Er is dus ook geen verkeer naar de landing page vanuit Meta. Daarnaast was de **PostHog MCP niet verbonden** in deze sessie, waardoor landing-page-analytics (bounce, scroll, CTA) niet opgehaald konden worden. Belangrijkste actie: beslis of SYBB weer live moet, en herstel de PostHog-connectie voordat het volgende rapport bruikbaar is.

## 2. Meta Ads Performance

| Metric | Gisteren (30 jun) | 7d Gemiddelde (24–30 jun) | Trend |
|--------|-------------------|---------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Campagnestatus:** `PAUSED` (laatst gewijzigd 19 apr 2026). Daily budget staat ingesteld op €100,00 maar levert niets omdat de campagne gepauzeerd is. Elke dag in het venster 24–30 juni gaf een lege dataset terug van de Meta API.

### Ad Variant Performance
Geen delivery op ad-niveau — er zijn geen impressions of clicks per `utm_content` variant om te rapporteren.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| _(geen data)_ | 0 | — | — | — | — |

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
⚠️ **Niet beschikbaar.** De PostHog MCP was niet verbonden tijdens deze run, dus er zijn geen metrics voor startyourballoonbusiness.com opgehaald (pageviews, bounce rate, scroll depth, session duration, CTA click rate). Zodra de connectie hersteld is kan deze sectie gevuld worden.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

## 4. Funnel Drop-off
Geen funnel te berekenen. Stap 1 (Meta traffic) is nul door de gepauzeerde campagne, en de PostHog-stappen (scroll 50%, CTA click, /booking) zijn niet beschikbaar.

`Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)`

**Grootste lek:** n.v.t. — er stroomt niets de funnel in.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — SYBB levert al minstens sinds 24 juni (en waarschijnlijk sinds de laatste wijziging op 19 apr) geen verkeer. Als SYBB actief hoort te zijn, is dit de meest kritieke bevinding.
- 🚩 **PostHog MCP niet verbonden** — dagelijkse landing-page-monitoring ligt stil. Zolang de connectie ontbreekt kan het rapport zijn belangrijkste cross-reference (ad ↔ landing page gedrag) niet uitvoeren.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of `2026: SYBB` weer live moet.** Wat: check in Meta Ads Manager of de pauze bewust is. Waarom: nul delivery sinds min. 24 juni. Hoe: campagne activeren (status → ACTIVE) als SYBB moet lopen, of bevestigen dat de pauze intentioneel is en dit rapport pauzeren tot heractivatie. Escalatie: 🟡 Robin-goedkeuring (budget €100/dag gaat weer lopen bij activatie).
2. **Herstel de PostHog MCP-connectie.** Wat: PostHog MCP opnieuw verbinden in de Claude-sessie/omgeving. Waarom: landing-page-health en funnel-analyse zijn de kern van dit rapport en ontbreken nu volledig. Hoe: MCP-server config controleren en reconnecten; daarna een test-query op startyourballoonbusiness.com draaien. Escalatie: 🟢 auto/technisch.
3. **Draai dit rapport opnieuw zodra 1 en 2 klaar zijn.** Wat: hergenereer het SYBB-rapport met beide bronnen live. Waarom: pas dan is de dagelijkse trend- en cross-reference-analyse betekenisvol. Hoe: `/daily-sybb-report` of dezelfde prompt met een dag actieve delivery + werkende PostHog. Escalatie: 🟢 auto.

---
_Gegenereerd 1 juli 2026 · alleen Meta Ads MCP (Pipeboard) geraadpleegd · PostHog MCP niet beschikbaar · geen Google-bronnen gebruikt._
