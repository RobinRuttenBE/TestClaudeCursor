# SYBB Daily Report — 1 July 2026

> Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP. Rapportdatum: gisteren (2026-07-01).

## 1. Samenvatting
De SYBB funnel stond gisteren volledig stil. De campagne `2026: SYBB` is **PAUSED** en had geen enkele delivery (nul spend, impressions en clicks) op 1 juli, net als de volledige week 25 juni t/m 1 juli. Er valt dus geen ad-performance te rapporteren. Daarnaast was de **PostHog MCP niet beschikbaar** in deze sessie, waardoor landing page data (bounce, scroll, CTA, funnel) niet opgehaald kon worden. Dit rapport bevat daarom geen cross-reference analyse.

## 2. Meta Ads Performance
Campagne `2026: SYBB` (ID `120239435987290239`) — status **PAUSED**, daily budget €100 (inactief).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Geen delivery over de hele periode 25 juni – 1 juli 2026. Alle dagsegmenten leeg.

### Ad Variant Performance
Geen actieve ads met delivery. Geen variant-data (h11–h15 / bX / ctaX) beschikbaar.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
⚠️ **PostHog MCP niet beschikbaar in deze sessie.** Landing page metrics voor startyourballoonbusiness.com konden niet opgehaald worden. Er is bewust geen alternatieve databron (GA4/Google) gebruikt.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

## 4. Funnel Drop-off
Niet te berekenen. Ad-zijde heeft nul verkeer (campagne paused) en PostHog-data ontbreekt. Geen funnel om drop-off op te meten.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — er is geen verkeer in de funnel.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — er wordt geen SYBB-verkeer gegenereerd. Al minstens 7 dagen geen delivery. Zolang dit zo blijft, groeit de workshop-funnel niet.
- 🚩 **PostHog MCP niet verbonden** — landing page monitoring ligt stil. Zelfs bij organisch of direct verkeer is er nu geen zicht op bounce/scroll/CTA-gedrag.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of `2026: SYBB` weer live moet.** Als SYBB-acquisitie deze maand een doel is: campagne activeren (budget €100/dag staat klaar) en creatives/UTM's checken vóór start. Zo niet, bevestig dat de pauze bewust is en zet dit rapport op standby. *(Impact: hoog — dit is de enige knop die de funnel weer op gang brengt.)*
2. **Herstel de PostHog MCP-verbinding** zodat landing page data morgen weer meekomt in het rapport. Zonder deze bron is cross-referencing (ad CTR vs bounce/scroll) onmogelijk. *(Impact: hoog voor rapportkwaliteit — snel op te lossen.)*
3. **Verifieer de creatives/UTM-opzet** (h11–h15 varianten, `utm_content=hXX_bX_ctaX`) terwijl de campagne uit staat, zodat een eventuele herstart direct schone tracking-data oplevert. *(Impact: middel — voorkomt datavervuiling bij relaunch.)*

---
*Notities: Meta data opgehaald via Pipeboard Meta Ads MCP (account `act_567892422940728`). Campagne-, dag- en ad-level insights gaven allemaal lege datasets terug voor 25 jun – 1 jul 2026. PostHog MCP was niet onder de verbonden servers in deze sessie; conform de run-instructie is er geen Google-bron als vervanging gebruikt.*
