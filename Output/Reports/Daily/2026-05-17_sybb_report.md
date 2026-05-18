# SYBB Daily Report — 17 May 2026

## 1. Samenvatting
De Meta Ads campagne **2026: SYBB** staat al sinds 19 april op PAUSED en leverde gisteren (en de hele afgelopen week) nul paid traffic op. De landing page draait dus volledig op organisch verkeer: 7 pageviews van 6 bezoekers, iets boven het 7-daags gemiddelde. Bounce rate was 100% en alle sessies waren single pageview, dus engagement is laag. Belangrijkste blokkade: scroll depth en CTA clicks worden niet getrackt in PostHog, waardoor de landing page diagnose grotendeels blind blijft.

## 2. Meta Ads Performance

Campagne **2026: SYBB** (ID `120239435987290239`) status: **PAUSED** (laatst gewijzigd 19 april 2026). Er is geen insights data voor 2026-05-17, en evenmin voor 10 t/m 16 mei. Geen spend, impressies, clicks of conversies in de hele rapportageweek.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads, dus geen variant data. De verwachte UTM structuur (`hXX_bX_ctaX`) komt niet voor in het verkeer. Alle landing page verkeer kwam van organische bio links (`utm_content=bio_link`) en direct verkeer, niet van betaalde ad varianten.

**Beste variant:** n.v.t. (campagne gepauzeerd)
**Slechtste variant:** n.v.t. (campagne gepauzeerd)

## 3. Landing Page Health
Bron: PostHog, host `www.startyourballoonbusiness.com`. 7-daags gemiddelde berekend over 10 t/m 16 mei.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 7 | 4,9 / dag | meten | 🟢 |
| Unieke bezoekers | 6 | 3,4 / dag | meten | 🟢 |
| Sessies | 5 | 2,6 / dag | meten | 🟢 |
| Bounce Rate | 100% | 86,2% | <55% | 🔴 |
| Avg Session Duration | 0s | ~45s | >90s | 🔴 |
| Scroll 25% | niet getrackt | niet getrackt | >80% | ⚪ |
| Scroll 50% | niet getrackt | niet getrackt | >60% | ⚪ |
| Scroll 75% | niet getrackt | niet getrackt | >40% | ⚪ |
| Scroll 100% | niet getrackt | niet getrackt | >20% | ⚪ |
| CTA Click Rate | niet getrackt | niet getrackt | >4% | ⚪ |

Caveat: avg session duration van 0s komt doordat alle 5 sessies precies 1 pageview hadden. PostHog meet zonder scroll of click events geen engagement binnen een single pageview sessie, dus 0s is deels een instrumentatie artefact, niet per se 0 seconden echte aandacht.

## 4. Funnel Drop-off
Alleen pageview niveau meetbaar. Scroll 50% en CTA click zijn niet geïnstrumenteerd, dus die stappen ontbreken.

Landing page pageview (7, 100%) → /booking pageview (1, 14%)

- 1 van de 7 pageviews kwam op `/booking` (bezoeker via Instagram bio link).
- 1 pageview op de productpagina `start-your-balloon-business-professional`.
- 5 pageviews bleven op de homepage `/` (3 direct, 1 Instagram, 1 Facebook).

**Grootste lek:** niet betrouwbaar te bepalen zonder scroll- en CTA-tracking. Op basis van het beschikbare signaal verlaat het overgrote deel het verkeer na de homepage zonder door te klikken naar booking.

## 5. Rode Vlaggen 🚩
- 🚩 **Meta SYBB campagne 8 dagen gepauzeerd.** Geen enkele paid impressie of click in de rapportageweek, terwijl het dagrapport hierop is ingericht. Strategische beslissing nodig: heractiveren of bewust stoppen.
- 🚩 **Bounce rate 100% gisteren** (target <55%). Alle 5 sessies single pageview, geen doorklik.
- 🚩 **Avg session duration 0s.** Deels artefact (zie caveat), maar er is geen enkel engagement signaal.
- 🚩 **Scroll depth en CTA click tracking ontbreekt volledig** op `startyourballoonbusiness.com`. Hierdoor zijn de landing page health KPI's en de funnel grotendeels onmeetbaar. Dit is een instrumentatiegat, niet een performance probleem op zich, maar het blokkeert wel alle diepere diagnose.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de Meta SYBB campagne.** Wat: bepaal of `2026: SYBB` weer aan moet of dat de focus verschuift. Waarom: 8 dagen lang nul paid traffic terwijl er dagelijks op gerapporteerd wordt. Hoe: in Meta Ads Manager de campagne heractiveren met een test budget, of het rapport tijdelijk pauzeren tot de campagne live gaat. Verwachte impact: zonder paid traffic levert dit rapport geen ad-optimalisatie waarde. Escalatie: Rood (strategie, Robin beslist).

2. **Implementeer scroll depth en CTA click tracking op de landing page.** Wat: PostHog autocapture activeren of custom events toevoegen voor scroll milestones (25/50/75/100%) en CTA clicks (Book Now). Waarom: 5 van de 7 health metrics en de volledige funnel zijn nu onmeetbaar. Hoe: via de Wix Editor / PostHog snippet op `startyourballoonbusiness.com`. Verwachte impact: vanaf dan echte landing page diagnose mogelijk in plaats van alleen pageview tellingen. Escalatie: Oranje (Wix Editor + Robin goedkeuring).

3. **Onderzoek het homepage naar booking pad.** Wat: bekijk waarom 6 van de 7 bezoekers niet op `/booking` komen. Waarom: bounce 100%, slechts 1 doorklik naar booking (via Instagram bio link). Hoe: session recordings van 17 mei bekijken in PostHog en de homepage hero plus eerste CTA controleren. Verwachte impact: lagere bounce en meer booking pageviews zodra de campagne weer paid traffic stuurt. Escalatie: Geel (Robin goedkeuring).

---
*Databronnen: Pipeboard Meta Ads MCP (campagne 2026: SYBB, account act_567892422940728) en PostHog MCP (project Default project, host www.startyourballoonbusiness.com). Periode: 2026-05-17, 7-daags gemiddelde over 2026-05-10 t/m 2026-05-16.*
