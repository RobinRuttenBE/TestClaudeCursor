# SYBB Daily Report — 5 July 2026

> **Databronnen deze run:** Meta Ads MCP (Pipeboard) + PostHog MCP.
> Geen Google-diensten (Gmail, Calendar, Drive, Sheets, Docs, Slides) gebruikt. Niet naar de Tracker Google Sheet geschreven.

## ⚠️ Datastatus — lees eerst

Dit rapport bevat **geen performance-cijfers**, om twee redenen:

1. **Meta Ads — campagne staat op PAUSED.** De campagne `2026: SYBB` (ID `120239435987290239`) leverde op 5 juli 2026 **niets** uit: nul impressies, nul clicks, nul spend. Een dag-voor-dag controle over de volledige periode **1 juni t/m 5 juli 2026** (35 dagen) geeft voor elke dag een lege dataset terug. De campagne is dus al minstens sinds begin juni niet actief geweest (status `PAUSED`, laatst gewijzigd 19 april 2026).
2. **PostHog — MCP niet beschikbaar.** De PostHog MCP-server heeft in deze sessie geen tools geladen. Landing page metrics voor `startyourballoonbusiness.com` (pageviews, bounce rate, scroll depth, CTA clicks, session recordings) konden **niet** worden opgehaald.

Zonder actieve advertenties én zonder PostHog-toegang is er geen funnel om te analyseren. De onderstaande secties documenteren wat wél verifieerbaar is en wat er nodig is om het rapport weer volwaardig te laten draaien.

---

## 1. Samenvatting

De SYBB-funnel stond op 5 juli 2026 **volledig stil aan de advertentiekant**: de Meta-campagne `2026: SYBB` is gepauzeerd en heeft de hele maand juni en de eerste week juli geen enkele impressie geleverd. Er is dus geen betaald verkeer naar de landing page gestuurd. De PostHog-databron was daarnaast niet bereikbaar in deze run, dus organische/overige landing page activiteit kon niet gemeten worden. **Belangrijkste trend: nul delivery — de campagne moet weer live voordat er iets te rapporteren valt.**

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` — ID `120239435987290239`
**Status:** 🔴 PAUSED
**Objective:** OUTCOME_SALES · **Dagbudget (ingesteld):** €100,00 · **Bid strategy:** LOWEST_COST_WITHOUT_CAP

| Metric | Gisteren (5 jul) | 7d Gemiddelde (28 jun–4 jul) | Trend |
|--------|------------------|------------------------------|-------|
| Spend | €0,00 | €0,00 | → geen delivery |
| Impressions | 0 | 0 | → geen delivery |
| Clicks | 0 | 0 | → geen delivery |
| CTR | n.v.t. | n.v.t. | → geen delivery |
| CPC | n.v.t. | n.v.t. | → geen delivery |
| Frequency | n.v.t. | n.v.t. | → geen delivery |

*Bron: Meta Ads MCP, dag-voor-dag breakdown 1 jun–5 jul 2026 (35 segmenten, alle leeg).*

### Ad Variant Performance

Geen ad-level data beschikbaar — de campagne leverde niets uit, dus er zijn geen impressies of clicks per `utm_content` variant (h11_b3_cta5, h12_b3_cta5, h13_b3_cta5, h14_b3_cta5, h15_b3_cta5) te tonen.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

🔴 **Niet beschikbaar** — PostHog MCP kon in deze sessie niet worden aangesproken (geen tools geladen). Bounce rate, session duration, scroll depth (25/50/75/100%) en CTA click rate voor `startyourballoonbusiness.com` konden niet worden opgehaald.

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

Niet te berekenen. Zonder Meta-verkeer (stap 1 instroom) en zonder PostHog (stap 2–4 gedrag) is er geen funnel om drop-off op te meten.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — de funnel wordt momenteel niet gevoed.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne `2026: SYBB` staat op PAUSED en levert nul impressies** (geverifieerd 1 jun–5 jul 2026). Zolang dit zo blijft komt er geen betaald verkeer binnen en genereert de SYBB-funnel geen leads.
- 🚩 **PostHog MCP niet beschikbaar in deze sessie.** De dagelijkse landing page monitoring kan niet draaien tot de verbinding hersteld is. Dit blindeert de helft van dit rapport (cross-referencing Meta ↔ PostHog is niet mogelijk).

## 6. Top 3 Acties voor Vandaag

1. **Beslis of de SYBB-campagne weer live moet.** De campagne is gepauzeerd sinds (uiterlijk) begin juni. Als SYBB actief gepromoot moet worden: heractiveer `2026: SYBB` in Meta Ads Manager (of laat mij dit voorbereiden) met een dagbudget van €100. Zo niet: bevestig dat de pauze bewust is, zodat dit dagrapport niet elke ochtend als "rode vlag" terugkomt. *(Impact: hoog — dit is de enige bron van betaald SYBB-verkeer. Snelheid: minuten.)*
2. **Herstel de PostHog MCP-verbinding.** Controleer de PostHog connector (auth/verbinding) zodat landing page metrics weer opgehaald kunnen worden. Zonder PostHog mist het rapport bounce rate, scroll depth en CTA-data volledig. *(Impact: hoog voor rapportagekwaliteit. Snelheid: afhankelijk van connector-setup.)*
3. **Draai het rapport opnieuw zodra 1 + 2 opgelost zijn.** Met een actieve campagne en werkende PostHog levert dit rapport pas echte inzichten (ad-variant performance, funnel drop-off, ad↔pagina mismatches). Overweeg een kleine test-batch (1 dag, €100) om de meetketen end-to-end te valideren voordat je opschaalt. *(Impact: middel. Snelheid: 1 dag data verzamelen.)*

---

*Gegenereerd op 6 juli 2026. Meta Ads data via Pipeboard MCP (account `act_567892422940728`, Sempertex Ad Account). PostHog data niet beschikbaar deze run.*
