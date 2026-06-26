# SYBB Daily Report — 25 June 2026

> **Databronnen:** Meta Ads MCP (Pipeboard) ✅ opgehaald · PostHog MCP ⚠️ niet beschikbaar deze run (server verbonden maar registreerde geen tools). Landing page sectie kon niet gevuld worden, zie sectie 3.

## 1. Samenvatting
Er valt voor 25 juni niets te rapporteren op adniveau: de campagne **"2026: SYBB"** staat op **PAUSED** en heeft gisteren (en de volledige laatste 30 dagen) **geen enkele delivery** gehad. Nul spend, nul impressies, nul clicks. De PostHog landing page data kon deze run niet opgehaald worden omdat de PostHog MCP geen tools beschikbaar stelde. Conclusie: de funnel ligt momenteel stil. Belangrijkste actie is een beslissing over heractivatie, niet optimalisatie.

## 2. Meta Ads Performance

**Campagne:** 2026: SYBB (`120239435987290239`)
**Status:** 🔴 PAUSED · Objective: OUTCOME_SALES · Daily budget ingesteld: €100,00 · Laatst gewijzigd: 19 April 2026

| Metric | Gisteren (25 Jun) | 7d Gemiddelde (18–24 Jun) | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> Geen data omdat de campagne gepauzeerd is. Zowel de dag-query (25 Jun) als de 7-daagse dag-breakdown (18–24 Jun) als een controle over de laatste 30 dagen (26 Mei – 25 Jun) gaven allemaal lege resultaten terug.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| _geen actieve ads_ | — | — | — | — | — |

**Beste variant:** n.v.t. — geen delivery
**Slechtste variant:** n.v.t. — geen delivery

## 3. Landing Page Health
⚠️ **Niet beschikbaar deze run.** De PostHog MCP stelde geen tools beschikbaar (server stond op "connecting" maar registreerde geen functies). Er is dus geen pageview-, bounce-, scroll- of CTA-data voor startyourballoonbusiness.com opgehaald.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

> Let op: ook als PostHog wél data had geleverd, zou ad-attributie (bounce/scroll per utm_content) leeg zijn, omdat er geen Meta-verkeer naar de pagina ging.

## 4. Funnel Drop-off
Niet te berekenen. Stap 1 (ad delivery) is nul, dus er is geen funnel om door te rekenen.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** De campagne staat uit. Dat is op dit moment het enige "lek" dat telt.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne PAUSED met nul delivery over 30+ dagen.** De SYBB-funnel genereert momenteel geen verkeer en geen leads via Meta.
- 🚩 **PostHog MCP onbeschikbaar.** Geen landing page monitoring mogelijk deze run. Dit verbergt mogelijke problemen op de pagina zelf.
- ⚠️ Er bestaat een tweede campagne **"2026: SYBB - Kopie"** (`120243293329420239`), ook PAUSED (aangemaakt 19 April 2026). Controleer of dit een bedoelde duplicaat/test is of opruimwerk.

## 6. Top 3 Acties voor Vandaag
1. **Beslis over heractivatie van "2026: SYBB".** De campagne ligt al sinds half april stil. Bepaal of SYBB weer live moet (en met welke creatives/budget) of bewust gepauzeerd blijft. Zonder delivery is er geen pipeline en geen data om op te sturen. *(Impact: hoog · Snelheid: direct in Meta Ads Manager)*
2. **Herstel de PostHog MCP-verbinding** voordat het volgende rapport draait, zodat de landing page helft weer meeloopt. Zonder PostHog mist het rapport de helft van zijn waarde (de cross-reference tussen ad-gedrag en pagina-gedrag). *(Impact: hoog voor rapportkwaliteit · Snelheid: setup-taak)*
3. **Ruim de duplicaat "2026: SYBB - Kopie" op of label hem helder** zodat toekomstige rapporten en deploys niet de verkeerde campagne raken. *(Impact: middel · Snelheid: snel)*

---
*Gegenereerd op 26 June 2026. Meta Ads via Pipeboard MCP (account act_567892422940728, Sempertex Ad Account). PostHog data ontbreekt — MCP niet beschikbaar. Geen Google-bronnen gebruikt; output uitsluitend lokaal opgeslagen.*
