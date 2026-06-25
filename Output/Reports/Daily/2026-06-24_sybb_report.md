# SYBB Daily Report — 24 June 2026

## 1. Samenvatting
Er is op 24 juni 2026 geen betaalde activiteit geweest: de campagne `2026: SYBB` (en de kopie `2026: SYBB - Kopie`) staat op PAUSED, en op accountniveau is er geen spend, geen impressies en geen clicks geregistreerd. Er valt dus geen Meta Ads performance te rapporteren. De PostHog landing page data kon deze run niet worden opgehaald omdat de PostHog MCP niet beschikbaar was, dus landing page health, scroll depth en funnel drop-off ontbreken. Belangrijkste signaal: zonder live campagne komt er geen verkeer uit Meta naar startyourballoonbusiness.com.

## 2. Meta Ads Performance

| Metric | Gisteren (24 Jun) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0 | €0 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Campagnestatus:** `2026: SYBB` (ID 120239435987290239) = **PAUSED**, daily budget €100. Geen leveringsdata voor 24 juni en geen data over de laatste 7 dagen (18–24 juni). De campagne draait dus al langer niet.

### Ad Variant Performance
Geen data beschikbaar. De campagne leverde gisteren geen ads uit, dus er is geen performance per `utm_content` variant (h11_b3_cta5 t/m h15_b3_cta5) te tonen.

## 3. Landing Page Health
**Niet beschikbaar deze run.** De PostHog MCP kon niet worden aangeroepen (server niet verbonden), waardoor pageviews, bounce rate, sessie duur, scroll depth en CTA click rate voor startyourballoonbusiness.com niet konden worden opgehaald. Geen data betekent dat hier bewust geen cijfers worden ingevuld in plaats van geschatte of verzonnen waarden.

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
Niet te berekenen. Zonder Meta Ads verkeer (0 clicks) en zonder PostHog data is er geen funnel om door te rekenen.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — geen instroom bovenaan de funnel.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED.** Geen enkele dag spend in de laatste 7 dagen. Zolang dit zo blijft, genereert SYBB geen leads via Meta.
- 🚩 **PostHog data niet beschikbaar.** De PostHog MCP-verbinding ontbrak deze run. Hierdoor kan de landing page health niet gemonitord worden en ontbreekt de cross-reference tussen ad en pagina. Verbinding herstellen vóór de volgende rapportage.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of de SYBB campagne weer live moet.** Als er deze periode leads nodig zijn, heractiveer `2026: SYBB` (of de kopie) in Meta Ads Manager en controleer budget (€100/dag), ad sets en creatives vóór heractivatie. *Impact: hoog — zonder live campagne geen instroom. Escalatie: Geel (Robin goedkeuring).*
2. **Herstel de PostHog MCP-verbinding.** Controleer of de PostHog MCP server verbonden is zodat landing page metrics weer opgehaald kunnen worden; zonder deze bron is de helft van het rapport blind. *Impact: hoog voor monitoring. Escalatie: Geel.*
3. **Plan een korte heractivatie-check.** Mocht de campagne bewust gepauzeerd zijn, leg vast waarom en wanneer hij weer aangaat, zodat het dagelijkse rapport niet elke ochtend leeg blijft. *Impact: middel — voorkomt ruis. Escalatie: Groen.*

---
*Databronnen: Meta Ads MCP (Pipeboard) — account `act_567892422940728` (Sempertex Ad Account). PostHog MCP — niet beschikbaar deze run. Periode: 24 juni 2026. Geen Google-bronnen gebruikt; geen cijfers geschat of verzonnen.*
