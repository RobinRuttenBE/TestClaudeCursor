# SYBB Daily Report — 23 June 2026

> **Datastatus:** ⚠️ Geen bruikbare data voor gisteren.
> - **Meta Ads:** campagne `2026: SYBB` staat op **PAUSED**. Geen spend, impressions of clicks op 23 juni (en feitelijk de hele laatste 30 dagen geen activiteit).
> - **PostHog:** de PostHog MCP was **niet verbonden** in deze sessie. Landing page health, scroll depth, bounce rate en funnel drop-off konden niet worden opgehaald. (Conform de strikte regel voor deze run is GEEN Google MCP als vervanging gebruikt.)
>
> Onderstaand rapport bevat daarom geen dag-op-dag performance. Ter referentie staat onderaan de **lifetime** campagnedata (13 jan – 24 jun 2026).

---

## 1. Samenvatting
Er valt voor 23 juni niets te rapporteren: de SYBB-campagne is uitgezet en heeft gisteren €0 besteed. Zolang de campagne op PAUSED staat, levert dit dagrapport per definitie lege cijfers op. De landing page kant kon bovendien niet gemeten worden omdat de PostHog-bron deze run niet beschikbaar was. Belangrijkste actie: beslissen of de campagne weer aan moet, of dit dagrapport pauzeren tot dat zo is.

## 2. Meta Ads Performance — 23 juni 2026

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Status campagne:** `2026: SYBB` (ID `120239435987290239`) — **PAUSED**, daily budget €100,00, objective OUTCOME_SALES. Laatst gewijzigd 19 april 2026. Geen leverings­activiteit geregistreerd in de periode 25 mei – 23 juni 2026.

### Ad Variant Performance
Niet beschikbaar — campagne leverde gisteren niet uit, dus er is geen breakdown per `utm_content` variant.

## 3. Landing Page Health
**Niet beschikbaar — PostHog MCP niet verbonden in deze sessie.**

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

Zonder PostHog data is er bovendien geen organisch verkeer of betaald verkeer te beoordelen voor startyourballoonbusiness.com.

## 4. Funnel Drop-off
Niet beschikbaar. Funnel-analyse vereist zowel Meta Ads clicks (0 gisteren) als PostHog pageview/CTA events (geen bron). Geen berekening mogelijk.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat uit.** `2026: SYBB` is PAUSED en heeft de afgelopen ~30 dagen geen enkele dag uitgeleverd. Er komt dus geen nieuw SYBB-verkeer binnen via deze campagne.
- 🚩 **PostHog meetbron ontbreekt.** De landing page kant van dit rapport kan niet worden gevuld. Als dit structureel is, is het dagrapport blind voor on-page gedrag.

## 6. Top 3 Acties voor Vandaag
1. **Beslis over de campagnestatus.** Wil je SYBB weer live? Zet `2026: SYBB` op ACTIVE (of dupliceer naar een verse campagne met nieuwe creatives) en bevestig het dagbudget van €100. Zo niet, pauzeer dit dagrapport tot er weer een actieve campagne draait. *Impact: hoog · Snelheid: direct.*
2. **Herstel de PostHog-koppeling.** Controleer of de PostHog MCP weer verbonden is voordat het volgende dagrapport draait, anders blijft de Landing Page Health-sectie leeg. *Impact: hoog voor rapportkwaliteit · Snelheid: snel.*
3. **Controleer de pixel-waardes.** In de lifetime data lijkt de purchase conversion value onrealistisch hoog t.o.v. 6 purchases (mogelijk verkeerde valuta/centen-configuratie). Verifieer de pixel value-mapping vóór een nieuwe live periode, zodat ROAS-rapportage klopt. *Impact: middel · Snelheid: middel.*

---

## Referentie — Lifetime campagnedata `2026: SYBB` (13 jan – 24 jun 2026)
*Alleen ter context; dit is GEEN gisteren-data.*

| Metric | Lifetime |
|--------|----------|
| Spend | €2.485,04 |
| Impressions | 297.174 |
| Reach | 132.674 |
| Clicks (all) | 12.067 |
| Unique clicks | 8.763 |
| Link clicks | 10.851 |
| CTR | 4,06% |
| CPC | €0,21 |
| CPM | €8,36 |
| Frequency | 2,24 |
| Landing page views | 6.992 |
| Add to cart | 53 |
| Initiate checkout | 36 |
| Leads | 15 |
| Purchases | 6 |

**Observaties (lifetime, ter info):**
- CTR (4,06%) en CPC (€0,21) zijn historisch sterk — ruim binnen target (<€0,50). De top-of-funnel hooks deden het goed.
- De bottleneck zat verderop: van 6.992 landing page views naar 53 add-to-cart, 15 leads en 6 purchases. Dat is het punt om bij een herstart op te focussen (landing page → checkout/booking), zodra PostHog-data dit weer kan onderbouwen.
- ⚠️ Purchase conversion value lijkt verkeerd geconfigureerd (zie actie 3); niet gebruiken voor ROAS zonder verificatie.

---

*Gegenereerd op 24 juni 2026. Bronnen: Meta Ads MCP (Pipeboard). PostHog MCP niet beschikbaar deze run.*
