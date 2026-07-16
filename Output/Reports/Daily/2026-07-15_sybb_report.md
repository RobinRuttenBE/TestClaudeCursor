# SYBB Daily Report — 15 July 2026

> Gegenereerd op 16 July 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP.
> **Let op:** dit rapport bevat geen performance-cijfers omdat er gisteren geen campagne-activiteit was en de PostHog-bron niet beschikbaar was. Zie sectie 7.

## 1. Samenvatting
Er is op 15 July 2026 **geen SYBB-activiteit** om te rapporteren. De campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED** en heeft gisteren, over de afgelopen 7 dagen én de afgelopen 30 dagen **nul spend, impressies en clicks** geregistreerd. Er valt dus geen ad-performance te analyseren. Daarnaast kon de landing page health niet worden opgehaald: de **PostHog MCP is in deze sessie niet verbonden**, dus er is geen bounce rate, scroll depth of funnel data beschikbaar.

## 2. Meta Ads Performance
Bron: Meta Ads MCP (Pipeboard) — account `Sempertex Ad Account` (`act_567892422940728`).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Campagnestatus:** `2026: SYBB` = **PAUSED** (daily budget €100,00 ingesteld, laatst gewijzigd 19 April 2026). Er is een gedupliceerde campagne `2026: SYBB - Kopie` (ook PAUSED). Geen van beide heeft in de afgelopen 30 dagen gedraaid.

### Ad Variant Performance
Geen data. Omdat de campagne pauzeert, zijn er geen impressies of clicks per ad-variant (h11_b3_cta5, h12_b3_cta5, etc.) om te vergelijken.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health
**Niet beschikbaar.** De PostHog MCP was in deze run niet verbonden, dus pageviews, bounce rate, session duration, scroll depth en CTA click rate voor startyourballoonbusiness.com konden niet worden opgehaald.

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
Niet te berekenen zonder PostHog data (en zonder ad traffic als instroom).
Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** onbekend — geen funnel data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — `2026: SYBB` draait niet en genereert geen traffic naar de landing page. Dit is de belangrijkste bevinding.
- 🚩 **PostHog MCP niet verbonden** — de landing page monitoring werkt niet in deze sessie. Zolang dit zo blijft, mist het dagelijkse rapport de helft van zijn databron en de cross-referencing.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of de SYBB-campagne weer live moet.** Als SYBB actief gepromoot moet worden, activeer `2026: SYBB` in Meta Ads Manager (of vraag mij dit te doen). Zolang de campagne PAUSED staat, komt er geen data en heeft het dagelijkse rapport geen input. *(Impact: hoog — Snelheid: direct)*
2. **Herstel de PostHog-verbinding.** Autoriseer/verbind de PostHog MCP zodat landing page health (bounce, scroll, CTA, funnel) weer opgehaald kan worden. Zonder deze bron kan het rapport geen ad-vs-pagina cross-referencing doen. *(Impact: hoog — Snelheid: medium)*
3. **Bevestig of dit rapport nog dagelijks nodig is bij een gepauzeerde campagne.** Overweeg de automatische trigger tijdelijk te pauzeren tot SYBB weer draait, om lege rapporten te voorkomen. *(Impact: laag — Snelheid: direct)*

---

### Databron-status (deze run)
- ✅ **Meta Ads MCP (Pipeboard):** verbonden. Account `act_567892422940728` opgehaald. Campagne `2026: SYBB` gevonden, status PAUSED, geen insights (leeg voor yesterday / last_7d / last_30d).
- ❌ **PostHog MCP:** niet verbonden in deze sessie — geen landing page data beschikbaar.
- ℹ️ Conform de run-instructie zijn uitsluitend Meta Ads MCP en PostHog MCP geraadpleegd. Geen Google MCPs aangeroepen en niet naar de Google Sheet tracker geschreven.
