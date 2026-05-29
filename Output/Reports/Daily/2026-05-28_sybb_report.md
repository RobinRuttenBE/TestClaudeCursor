# SYBB Daily Report — 28 May 2026

## 1. Samenvatting
De **SYBB campagne staat op PAUSED** en heeft de hele maand mei geen euro uitgegeven, geen impressies en geen klikken gedraaid. Er is dus geen Meta Ads performance om te rapporteren. De landingspagina (startyourballoonbusiness.com) krijgt daardoor alleen een organische druppel verkeer: **3 pageviews van 2 unieke bezoekers** gisteren, tegenover gemiddeld ~1 pageview per dag in de voorgaande 7 dagen. Belangrijkste actie: beslissen of de campagne weer aangezet wordt, want zonder ad spend staat de hele funnel stil.

## 2. Meta Ads Performance

> ⚠️ **Geen data.** Campagne `2026: SYBB` (ID `120239435987290239`, account "Sempertex Ad Account") staat op **PAUSED** (laatst gewijzigd 19 apr 2026). Insights voor 28 mei 2026 én voor de volledige maand mei (1–28 mei) geven nul resultaten terug. Er is geen spend, geen bereik en geen klikken.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads, dus geen variant-data (h11_b3_cta5 t/m h15_b3_cta5 niet meetbaar).

**Beste variant:** n.v.t. — campagne staat uit
**Slechtste variant:** n.v.t. — campagne staat uit

## 3. Landing Page Health

> ⚠️ **Zeer laag volume + ontbrekende instrumentatie.** Met 3 pageviews is geen enkele ratio statistisch betekenisvol. Daarnaast zijn in dit PostHog project **geen scroll-depth, CTA-click of pageleave events** geconfigureerd, dus bounce rate, scroll depth en CTA click rate kunnen niet gemeten worden. Alleen pageviews en unieke bezoekers zijn beschikbaar.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 3 | ~1,0/dag | meten | 🟡 |
| Unique visitors | 2 | ~1,0/dag | meten | 🟡 |
| Bounce Rate | geen data | geen data | <55% | ⚪ niet gemeten |
| Avg Session Duration | geen data | geen data | >90s | ⚪ niet gemeten |
| Scroll 25/50/75/100% | geen data | geen data | >80/60/40/20% | ⚪ niet gemeten |
| CTA Click Rate | geen data | geen data | >4% | ⚪ niet gemeten |

**Verkeersbron (17–28 mei):** `t-sml.mtrbio.com` (link-in-bio) en `$direct`. **Geen** verkeer met `utm_medium=cpc` of Meta-bron — bevestigt dat al het verkeer organisch is.

**Pageviews per dag (host = www.startyourballoonbusiness.com):**
```
21 mei: 1   22 mei: 2   23 mei: 0   24 mei: 0
25 mei: 0   26 mei: 3   27 mei: 1   28 mei: 3
```

## 4. Funnel Drop-off
Niet te berekenen. De funnel vereist Meta Ads instroom (stap 0) plus scroll- en CTA-events op de landingspagina. Beide ontbreken:
- Stap 0 (ad click) → **0**, campagne paused
- Stap 1 (pageview) → 3 (organisch)
- Stap 2 (scroll 50%) → niet geïnstrumenteerd
- Stap 3 (CTA click) → niet geïnstrumenteerd
- Stap 4 (/booking) → niet geïnstrumenteerd

**Grootste lek:** de instroom zelf. Zonder actieve campagne komt er niemand de funnel in.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — al sinds ~19 april geen spend. Dit is de hoofdoorzaak van alle nullen.
- 🚩 **Funnel-instrumentatie ontbreekt** — geen scroll-depth, CTA-click of pageleave events in PostHog. Zodra de campagne weer aanstaat, kun je on-page gedrag (bounce, scroll, CTA) niet meten en dus niet optimaliseren.
- 🚩 **Organisch verkeer is verwaarloosbaar** (~1 pageview/dag). De landingspagina draait nu vrijwel op nul.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of de SYBB campagne weer aan moet** (impact: hoog / snelheid: direct). De campagne `2026: SYBB` staat op PAUSED met een dagbudget van €100 al ingesteld. Zonder reactivering blijft de funnel leeg. → Robin-beslissing: doel, budget en periode bevestigen voordat we 'm aanzetten (escalatie: 🟠 strategie).
2. **Zet on-page tracking live vóór reactivering** (impact: hoog / snelheid: middel). Configureer in PostHog scroll-depth (25/50/75/100%), een CTA-click event en `$pageleave` zodat bounce rate en scroll depth meetbaar worden. Zonder deze events is dit dagrapport blind voor landing-page gedrag (escalatie: 🟡 Robin goedkeuring + technische setup).
3. **Controleer UTM-tagging op de actieve ads** (impact: middel / snelheid: snel). Voordat de campagne aangaat: verifieer dat alle ads de conventie `utm_source=meta`, `utm_medium=cpc`, `utm_content=hXX_bX_ctaX` dragen, zodat variant-attributie meteen werkt vanaf dag 1 (escalatie: 🟢 auto, in Meta Ads Manager).

---
*Databronnen: Meta Ads MCP (Pipeboard) — campagne `2026: SYBB`. PostHog MCP — project "Default project", host www.startyourballoonbusiness.com. Periode: 28 mei 2026 (gisteren) vs. 21–27 mei 2026 (baseline). Gegenereerd 29 mei 2026.*
