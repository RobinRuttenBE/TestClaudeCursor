# SYBB Daily Report — 3 July 2026

## 1. Samenvatting
**Geen activiteit om te rapporteren.** De campagne `2026: SYBB` staat op **PAUSED** en heeft gisteren (3 juli 2026) én de volledige afgelopen 7 dagen **€0 uitgegeven, 0 impressies en 0 clicks** gedraaid. De laatste meetbare activiteit dateert van **april 2026**. Daarnaast kon de **PostHog MCP deze run niet worden bereikt** (server niet verbonden), waardoor er geen landing page data beschikbaar is. Er valt vandaag dus niets te optimaliseren aan de live performance; de enige relevante actie is een besluit over het al dan niet heractiveren van de campagne.

---

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID `120239435987290239`) — status **PAUSED**, dagbudget €100,00
**Account:** Sempertex Ad Account (`act_567892422940728`)

| Metric | Gisteren (3 jul) | 7d Gemiddelde | Trend |
|--------|------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De campagne leverde over de periode 27 juni – 3 juli 2026 zeven lege dag-segmenten op (geen enkele metric > 0). De campagne is dus de hele week inactief geweest.

### Ad Variant Performance
Geen data. Er draaiden gisteren geen actieve ads onder deze campagne, dus er zijn geen `utm_content` varianten (h11_b3_cta5 t/m h15_b3_cta5) om te vergelijken.

**Beste variant:** n.v.t. — geen actieve ads
**Slechtste variant:** n.v.t. — geen actieve ads

### Context: laatste bekende activiteit (april 2026)
Ter referentie, de laatste periode waarin de campagne wél draaide (5–30 april 2026, lifetime laatste segment):

| Metric | Waarde |
|--------|--------|
| Spend | €1.059,47 |
| Impressions | 91.839 |
| Clicks | 1.935 |
| CTR | 2,11% |
| CPC | €0,55 |
| Frequency | 2,19 |
| Landing page views | 818 |
| Purchases | 6 (waarde €442,47) |
| Add to cart | 44 |
| Initiate checkout | 33 |

Let op: in die laatste actieve periode lag de **CPC op €0,55 — boven het target van <€0,50**. Als de campagne wordt heractiveerd, is dit het eerste aandachtspunt.

---

## 3. Landing Page Health
**Niet beschikbaar.** De PostHog MCP was deze run niet verbonden — er kon geen data worden opgehaald voor startyourballoonbusiness.com (pageviews, bounce rate, scroll depth, session duration, CTA click rate, session recordings). Zonder actieve ad-traffic naar de landing page zouden deze cijfers hoe dan ook nauwelijks betekenis hebben.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

---

## 4. Funnel Drop-off
Niet te berekenen. Zonder Meta Ads traffic (0 clicks) en zonder PostHog data is er geen funnel om te analyseren.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t.

---

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — de SYBB funnel genereert momenteel geen leads of workshop-verkopen. Dit is de belangrijkste vlag: er wordt geen budget verbrand, maar er komt ook geen omzet binnen.
- 🚩 **PostHog MCP niet verbonden** — landing page monitoring ontbreekt volledig deze run. Cross-referencing tussen ads en pagina-gedrag is niet mogelijk zolang de connector niet actief is.
- ⚠️ **CPC €0,55 in laatste actieve periode (april)** — boven target <€0,50. Relevant zodra de campagne herstart.

---

## 6. Top 3 Acties voor Vandaag
1. **Besluit nemen over heractivatie van `2026: SYBB`** (impact hoog, snelheid hoog). De campagne ligt sinds april stil. Bepaal met Robin of SYBB weer live moet. Zo ja: herstart met verse creatives en een CPC-doel van <€0,50 (de april-CPC van €0,55 zat erboven). Escalatie: **Rood (strategie)** — dit is een budget-/campagnebeslissing, geen auto-actie.
2. **PostHog MCP-verbinding herstellen** (impact middel, snelheid hoog). Zonder deze connector is het dagelijkse rapport half blind. Controleer de PostHog connector in een interactieve sessie (`/mcp`) zodat landing page data morgen weer meekomt. Escalatie: **Geel (Robin goedkeuring/actie).**
3. **Landing page klaarzetten vóór herstart** (impact middel, snelheid middel). Als SYBB heractiveert, wil je dat startyourballoonbusiness.com meteen goed getrackt en geoptimaliseerd is. Verifieer UTM-tagging (`utm_content=hXX_bX_ctaX`) en Meta Pixel events vóór de eerste euro traffic. Escalatie: **Oranje (Wix Editor / tracking-check).**

---

*Databronnen: Meta Ads MCP (Pipeboard) — campagne `2026: SYBB`. PostHog MCP was deze run niet beschikbaar. Geen Google-bronnen gebruikt. Rapport lokaal opgeslagen; niet naar Google Sheet geschreven.*
