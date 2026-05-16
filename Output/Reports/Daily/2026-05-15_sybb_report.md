# SYBB Daily Report — 15 May 2026

## 1. Samenvatting
De Meta campagne **"2026: SYBB" staat op PAUSED en heeft gisteren (en de hele afgelopen 7 dagen) niets uitgeleverd**: nul spend, nul impressies, nul clicks. Alle landingspagina traffic is dus volledig organisch en zeer laag in volume (3 sessies, 4 pageviews gisteren). De on-page kwaliteit van die paar bezoekers was goed (0% bounce, lange sessieduur), maar het volume is te klein om conclusies op te trekken. De prioriteit ligt niet bij optimalisatie maar bij de vraag of de campagne bewust uit staat.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (id 120239435987290239)
**Status:** 🔴 PAUSED — daily budget €100,00 (niet actief)
**Account:** Sempertex Ad Account (act_567892422940728)

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Ads MCP gaf voor zowel 15 May als de volledige periode 9 t/m 15 May een lege dataset terug. De campagne levert niet uit.

### Ad Variant Performance
Geen ad delivery, dus geen variant data beschikbaar. De verwachte UTM varianten (h11_b3_cta5 t/m h15_b3_cta5) zijn deze periode niet vertoond.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health

Bron: PostHog, host `www.startyourballoonbusiness.com`. Let op: extreem laag volume (3 sessies gisteren), cijfers zijn statistische ruis.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Sessies | 3 | 3,3 / dag | meten | → |
| Pageviews | 4 | 3,9 / dag | meten | → |
| Unieke bezoekers | 3 | 3,0 / dag | meten | → |
| Bounce Rate | 0,0% | ~43% (sessie-gewogen) | <55% | 🟢 |
| Avg Session Duration | 245s | ~66s | >90s | 🟢 |
| Scroll 25% / 50% / 75% / 100% | geen data | geen data | >80/60/40/20% | ⚪ niet getrackt |
| CTA Click Rate | geen data | geen data | >4% | ⚪ niet getrackt |

**Datagaten:** PostHog vangt op dit project alleen `$pageview` (plus systeemevents zoals `$rageclick` / `$dead_click`). Er zijn **geen scroll-depth events en geen CTA-click events** ingericht, en autocapture lijkt uit. Scroll depth en CTA click rate kunnen daardoor niet gerapporteerd worden tot deze tracking is toegevoegd.

### Verkeer per dag (sessies)
| Dag | Sessies | Pageviews | Bounce | Avg duur |
|-----|---------|-----------|--------|----------|
| 08 May | 2 | 2 | 100% | 7s |
| 09 May | 2 | 2 | 0% | 19s |
| 10 May | 3 | 3 | 67% | 4s |
| 11 May | 4 | 4 | 25% | 123s |
| 12 May | 10 | 14 | 30% | 95s |
| 13 May | 1 | 1 | 100% | 5s |
| 14 May | 1 | 1 | 100% | 5s |
| **15 May** | **3** | **4** | **0%** | **245s** |

### UTM segmentatie (15 May)
| utm_content | Sessies | Bounce | Avg duur |
|-------------|---------|--------|----------|
| bio_link | 2 | 0% | 41s |
| (none) / direct | 1 | 0% | 654s |

Alle traffic komt via `bio_link` (Instagram/social bio) en direct. Geen enkele sessie met betaalde Meta UTM tagging, wat bevestigt dat de campagne niet draait.

## 4. Funnel Drop-off
Pageview (100%) → Scroll 50% (geen data) → CTA Click (geen data) → /booking (geen data)

Funnel kan niet opgebouwd worden: scroll- en CTA-events ontbreken in PostHog, en er was geen meetbaar /booking verkeer. **Grootste lek:** niet vast te stellen zonder tracking, en bovendien irrelevant zolang er geen ad-verkeer is.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat uit.** "2026: SYBB" is PAUSED met €0 delivery over minimaal 7 dagen. Dit is de enige relevante anomalie. Als dit niet bewust is, ligt hier de volledige prioriteit.
- 🚩 **Tracking gaten op de landingspagina.** Geen scroll-depth en geen CTA-click tracking. Zodra de campagne weer aan gaat is het rapport blind voor de helft van de funnel.
- ℹ️ Geen CPC-, bounce- of frequency-vlaggen mogelijk: er is geen delivery om tegen te toetsen.

## 6. Top 3 Acties voor Vandaag

1. **Bevestig de campagnestatus van "2026: SYBB" (hoogste prioriteit).**
   - *Wat:* Controleer in Meta Ads Manager of de pauze bewust is. Zo niet, heractiveer de campagne.
   - *Waarom:* Nul delivery over 7+ dagen betekent nul nieuwe SYBB-leads uit ads.
   - *Hoe:* Handmatig in Meta Ads Manager (escalatie: Geel, Robin goedkeuring voor heractivatie).
   - *Verwachte impact:* Herstel van de volledige acquisitiestroom.

2. **Richt scroll-depth en CTA-click tracking in op startyourballoonbusiness.com.**
   - *Wat:* Voeg PostHog scroll-tracking en een custom event op de "Book Now" CTA toe (of zet autocapture aan).
   - *Waarom:* Zonder deze events is funnel- en variantanalyse onmogelijk zodra ads weer draaien.
   - *Hoe:* Wix Editor / PostHog snippet configuratie (escalatie: Oranje, Wix Editor).
   - *Verwachte impact:* Volledig funnelrapport bij hervatten campagne.

3. **Geen optimalisatie-acties op ad- of pagina-niveau deze run.**
   - *Wat:* Houd huidige creatives en pagina ongewijzigd.
   - *Waarom:* 3 organische sessies zijn statistische ruis. Optimaliseren op deze data zou misleidend zijn.
   - *Hoe:* Niets wijzigen tot er ad-volume is (escalatie: Groen).
   - *Verwachte impact:* Voorkomt verkeerde beslissingen op te kleine steekproef.

---
*Databronnen: Meta Ads MCP (Pipeboard), PostHog MCP. Periode: 15 May 2026, baseline 08 t/m 14 May 2026. Geen Google MCPs of Sheets gebruikt conform run-instructie.*
