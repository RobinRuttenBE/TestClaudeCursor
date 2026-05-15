# SYBB Daily Report — 14 May 2026

## 1. Samenvatting
Het rapport kon vandaag maar deels worden gevuld. De Meta Ads bron (Pipeboard) gaf een verbindingsfout ("Facebook connection required"), dus er is geen ad-data over campagne `2026: SYBB`. PostHog werkt wel, maar laat extreem lage traffic zien: slechts 1 pageview op 14 mei (1 unieke bezoeker). Bovendien capteert de site alleen `$pageview`, geen `$pageleave`, waardoor bounce rate, sessieduur en scroll depth niet meetbaar zijn. Conclusie: er is op dit moment te weinig signaal om performance te beoordelen. De urgente actie zit in het herstellen van datastromen, niet in optimalisatie.

## 2. Meta Ads Performance
**Status: data niet beschikbaar.** De Pipeboard Meta Ads MCP gaf de fout: *"Facebook connection required. Connect your account at https://pipeboard.co/connections to continue."* Er is geen account-, ad set- of ad-niveau data opgehaald.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | n.b. | n.b. | — |
| Impressions | n.b. | n.b. | — |
| Clicks | n.b. | n.b. | — |
| CTR | n.b. | n.b. | — |
| CPC | n.b. | n.b. | — |
| Frequency | n.b. | n.b. | — |

### Ad Variant Performance
Niet beschikbaar zonder Meta-verbinding. PostHog laat wel zien welke `utm_content` op de site landde (zie sectie 3) — de enige getagde ad-bezoeker op 14 mei kwam binnen via `h11_b3_cta5`.

**Beste variant:** n.b.
**Slechtste variant:** n.b.

## 3. Landing Page Health
**Site:** www.startyourballoonbusiness.com · Bron: PostHog (project "Default project", 149694)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 1 | 3,9 / dag | meten | 🔴 (zeer laag volume) |
| Unieke bezoekers | 1 | — | meten | 🔴 |
| Bounce Rate | niet meetbaar | niet meetbaar | <55% | ⚪ geen `$pageleave` |
| Avg Session Duration | niet meetbaar | niet meetbaar | >90s | ⚪ geen `$pageleave` |
| Scroll 25% | niet meetbaar | niet meetbaar | >80% | ⚪ niet geïnstrumenteerd |
| Scroll 50% | niet meetbaar | niet meetbaar | >60% | ⚪ niet geïnstrumenteerd |
| Scroll 75% | niet meetbaar | niet meetbaar | >40% | ⚪ niet geïnstrumenteerd |
| Scroll 100% | niet meetbaar | niet meetbaar | >20% | ⚪ niet geïnstrumenteerd |
| CTA Click Rate | niet meetbaar | niet meetbaar | >4% | ⚪ geen CTA-event |
| Rageclicks | 0 | 0 | 0 | 🟢 |
| Dead clicks | 0 | 0 | 0 | 🟢 |

**Pageviews per dag (host = www.startyourballoonbusiness.com):**

| Datum | Pageviews | Unieke bezoekers |
|-------|-----------|------------------|
| 07 May | 1 | 1 |
| 08 May | 2 | 2 |
| 09 May | 2 | 2 |
| 10 May | 3 | 3 |
| 11 May | 4 | 4 |
| 12 May | 14 | 8 |
| 13 May | 1 | 1 |
| **14 May (gisteren)** | **1** | **1** |

**UTM-segmentatie (pageviews per `utm_content`, 7–14 May):**

| utm_content | Pageviews (7-14 May) | Waarvan 14 May |
|-------------|----------------------|----------------|
| (geen utm) | 23 | 0 |
| bio_link | 5 | 0 |
| h11_b3_cta5 | 1 | 1 |

De 12 mei piek (14 pageviews, waarvan 13 op `/review`, vrijwel allemaal zonder utm) wijst op intern/review-verkeer, niet op betaald adverkeer. De enige getagde ad-bezoeker in de hele week kwam gisteren binnen via `h11_b3_cta5` en landde direct op `/booking`.

**Pathname-verdeling (7-14 May):** `/` (12), `/review` (15), `/booking` (1), met losse hits op `/checkout`, `/thank-you-page`, `/review`.

## 4. Funnel Drop-off
Funnel landing pageview → `/booking` pageview (window 1 dag), 7–14 May:

Landing pageview (22 personen / 100%) → `/booking` (0 / 0%)

**Grootste lek:** 100% drop-off vóór `/booking`. Let op: dit cijfer is statistisch betekenisloos bij dit volume. De enkele `/booking` view op 14 mei telde niet als stap 2 omdat er geen voorafgaande landingspageview binnen het venster aan gekoppeld was (directe entry op `/booking` via de getagde ad-link). Conclusie blijft: te weinig data voor funnelanalyse.

## 5. Rode Vlaggen 🚩
- 🚩 **Meta Ads databron down** — Pipeboard Facebook-verbinding verbroken. Zolang dit niet hersteld is, is er geen ad performance, geen spend-bewaking en geen variant-analyse. Dit is de hoogste prioriteit.
- 🚩 **Geen `$pageleave` / scroll / CTA tracking op de site** — bounce rate, sessieduur, scroll depth en CTA click rate zijn structureel niet meetbaar. Zonder dit kan het dagrapport zijn kernfunctie (ad ↔ pagina cross-referencing) niet uitvoeren.
- 🚩 **Extreem laag traffic volume** — 1 pageview op 14 mei, ~3,9/dag over de week. Bij dit volume zijn alle ratio's ruis. Dit wijst op vrijwel nul actieve ad-spend of een tracking-/UTM-breuk tussen Meta en de landingspagina.

## 6. Top 3 Acties voor Vandaag
1. **Herstel de Pipeboard Meta Ads verbinding** (impact: hoog, snelheid: snel). Wat: opnieuw verbinden via https://pipeboard.co/connections. Waarom: zonder Meta-data is er geen zicht op spend, CTR, CPC of variant-performance van `2026: SYBB`. Verwachte impact: rapport kan weer ad ↔ pagina cross-referencen. Escalatie: Geel (Robin actie vereist — login).
2. **Instrumenteer `$pageleave` + scroll-tracking op startyourballoonbusiness.com** (impact: hoog, snelheid: middel). Wat: PostHog autocapture met pageleave en scroll-depth aanzetten, plus een expliciet CTA-click event op de "Book Now" knop. Waarom: bounce rate, sessieduur, scroll depth en CTA click rate zijn nu blind. Verwachte impact: de Landing Page Health en Funnel secties worden bruikbaar. Escalatie: Oranje (Wix/site editor).
3. **Verifieer of campagne `2026: SYBB` daadwerkelijk live is en correct getagd** (impact: hoog, snelheid: snel). Wat: check in Meta Ads Manager of er budget loopt en of de bestemmings-URL's de juiste `utm_content` dragen (h11_b3_cta5, h12_b3_cta5, …). Waarom: slechts 1 getagde ad-bezoeker in 7 dagen wijst op nul/zeer lage spend of een gebroken UTM-link. Verwachte impact: traffic en meetbaarheid herstellen. Escalatie: Geel (Robin goedkeuring).

---

### Databronnen & beperkingen
- **Meta Ads (Pipeboard MCP):** geen data — verbindingsfout.
- **PostHog MCP:** project "Default project" (149694), host `www.startyourballoonbusiness.com`. Alleen `$pageview` (+ `$rageclick`, `$dead_click`) gecaptured; `$pageleave`/scroll/CTA-events ontbreken.
- Conform run-instructie zijn uitsluitend Meta Ads MCP en PostHog MCP gebruikt. Geen Google MCP's aangeroepen, niet naar de Meta Ads Tracker Google Sheet geschreven.
