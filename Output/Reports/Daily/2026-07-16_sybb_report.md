# SYBB Daily Report — 16 July 2026

> Gegenereerd op 17 July 2026. Databronnen: Meta Ads MCP (Pipeboard) en PostHog MCP.

## 1. Samenvatting
Er is voor 16 July 2026 geen te rapporteren activiteit. De Meta campagne **"2026: SYBB"** staat op **PAUSED** en heeft gisteren, de afgelopen 7 dagen en de afgelopen 30 dagen geen enkele delivery gehad (0 spend, 0 impressions, 0 clicks). Daarnaast kon de **PostHog MCP niet worden aangeroepen** in deze sessie (de connector is niet verbonden), waardoor er geen landing page data beschikbaar is. Zonder actieve ads en zonder PostHog bron is er geen funnel om te analyseren. De belangrijkste actie is een keuze: heractiveer de campagne, of bevestig dat SYBB bewust op pauze staat.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID 120239435987290239), account Sempertex Ad Account (act_567892422940728).
Status: **PAUSED**. Daily budget ingesteld op €100,00, maar niet actief.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Geen delivery in het window 10 July tot en met 16 July 2026 (per-dag breakdown: 7 dagen, allemaal leeg). Ook geen delivery in de 30 dagen tot 16 July 2026.

### Ad Variant Performance
Geen actieve ads met delivery op 16 July 2026, dus geen variant data (h11_b3_cta5, h12_b3_cta5, etc.) beschikbaar.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
**Niet beschikbaar.** De PostHog MCP kon in deze sessie niet worden aangeroepen (connector niet verbonden). Er is dus geen data voor startyourballoonbusiness.com over bounce rate, session duration, scroll depth of CTA click rate.

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
Niet te berekenen. Er is geen ad traffic (Meta paused) en geen PostHog data om de stappen Pageview → Scroll 50% → CTA Click → /booking mee te vullen.

**Grootste lek:** n.v.t.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** met €0 delivery over minimaal 30 dagen. Als SYBB actief zou moeten adverteren, is dit de meest urgente issue.
- 🚩 **PostHog MCP niet verbonden.** Zolang de connector niet geautoriseerd is, kan het dagelijkse rapport de landing page kant niet meten en dus geen cross-referencing doen (Meta CTR vs LP bounce, etc.).

## 6. Top 3 Acties voor Vandaag
1. **Beslis over de campagnestatus.** Bevestig of "2026: SYBB" bewust gepauzeerd is of per ongeluk. Zo ja bewust: prima, geen actie op ads. Zo niet: heractiveer in Meta Ads Manager en controleer budget (€100/dag staat ingesteld) en ad set delivery. *Impact: hoog, snelheid: minuten.*
2. **Herstel de PostHog connectie.** Autoriseer de PostHog MCP zodat landing page metrics weer opgehaald kunnen worden. Zonder deze bron blijft de helft van het dagrapport blind. *Impact: hoog, snelheid: minuten via connector settings.*
3. **Plan een verificatie-run.** Zodra campagne actief is en PostHog verbonden, draai dit rapport opnieuw voor een dag met echte delivery om de volledige funnel (ads + landing page) te valideren. *Impact: middel, snelheid: 1 dag data nodig.*

---

### Databron notitie
- Meta Ads MCP (Pipeboard): succesvol bevraagd. Account act_567892422940728, campagne 120239435987290239. Resultaat: 0 rijen (campagne paused).
- PostHog MCP: **niet beschikbaar** in deze sessie. Geen data opgehaald.
- Conform de run-regels zijn uitsluitend Meta Ads MCP en (poging tot) PostHog MCP gebruikt. Geen Google MCPs aangeroepen. Niet naar de Google Sheet tracker geschreven. Output alleen lokaal opgeslagen.
