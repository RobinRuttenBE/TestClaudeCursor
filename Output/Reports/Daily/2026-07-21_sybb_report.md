# SYBB Daily Report, 21 juli 2026

> Databronnen: Meta Ads MCP (Pipeboard) en PostHog MCP. Rapportperiode: gisteren (2026-07-21). 7d gemiddelde over 2026-07-14 t/m 2026-07-20.

## 1. Samenvatting

De SYBB funnel stond gisteren praktisch stil. De Meta campagne **"2026: SYBB" is PAUSED** en had nul spend, nul impressies en nul clicks (niet alleen gisteren, maar de hele maand juli). De landingspagina kreeg daardoor alleen organische restverkeer: **1 pageview, 1 bezoeker, 1 sessie** op 21 juli, die direct bounce'te. Belangrijkste bevinding is geen performanceprobleem maar een activatieprobleem: er draaien geen ads, en de landingspagina mist tracking voor scroll depth, CTA clicks en de booking-stap, waardoor de funnel niet gemeten kan worden.

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (id 120239435987290239), account "Sempertex Ad Account" (act_567892422940728).
Status: **PAUSED**. Objective: OUTCOME_SALES. Daily budget ingesteld op €100,00 maar niet actief.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Controle over 2026-07-01 t/m 2026-07-21 bevestigt: **nul activiteit de hele maand**. Ook de kopie "2026: SYBB - Kopie" (id 120243293329420239) staat op PAUSED.

### Ad Variant Performance

Niet beschikbaar. Zonder actieve ads is er geen data per `utm_content` (h11_b3_cta5, h12_b3_cta5, etc.). Zodra de campagne weer live gaat, wordt deze tabel automatisch gevuld.

## 3. Landing Page Health

Host: `www.startyourballoonbusiness.com` (PostHog project "Default project", Sempertex Europe).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 1 | 2,4 / dag | meten | 🔴 |
| Unieke bezoekers | 1 | 2,4 / dag | meten | 🔴 |
| Sessies | 1 | 2,4 / dag | meten | 🔴 |
| Bounce Rate | 100% (n=1) | ~100% | <55% | 🔴 |
| Avg Session Duration | 0s | ~0s | >90s | 🔴 |
| Scroll 25% / 50% / 75% / 100% | niet getrackt | niet getrackt | >80/60/40/20% | ⚪ |
| CTA Click Rate | niet getrackt | niet getrackt | >4% | ⚪ |

Let op: alle percentages zijn gebaseerd op n=1 sessie en zijn statistisch betekenisloos. De rode status weerspiegelt het gebrek aan verkeer, niet een kwaliteitsprobleem met de pagina zelf.

**Tracking gap:** op deze host vuren alleen de events `$pageview` en `$web_vitals`. Er zijn **geen scroll-depth events, geen CTA-click events en geen booking events** ingericht. Scroll depth, CTA click rate en de funnel kunnen daarom niet berekend worden. Dit is de eerste blokkade om deze pagina serieus te kunnen optimaliseren.

## 4. Funnel Drop-off

Niet te berekenen. De funnel (Pageview → Scroll 50% → CTA Click → /booking) vereist scroll- en CTA-events die niet in PostHog binnenkomen voor deze host. Enige meetbare stap gisteren:

Pageview (1) → Scroll 50% (onbekend) → CTA Click (onbekend) → /booking (onbekend)

**Grootste lek:** onmeetbaar zolang de tracking ontbreekt. Op basis van het enige signaal dat er wel is (0s sessieduur, directe bounce) verlaat de bezoeker de pagina vrijwel meteen, maar één sessie is te weinig om een conclusie op te bouwen.

## 5. Rode Vlaggen 🚩

- **Campagne PAUSED, nul spend de hele maand juli.** De SYBB acquisitiemotor staat uit. Dit is de dominante rode vlag: zonder ads geen funnel.
- **Landingspagina tracking onvolledig.** Geen scroll-depth, CTA-click of booking events op `www.startyourballoonbusiness.com`. Ook als ads weer aangaan, blijft de pagina een black box.
- **Verwaarloosbaar organisch verkeer.** 17 pageviews over 7 dagen (~2,4/dag). Onvoldoende om iets te leren of te optimaliseren.

## 6. Top 3 Acties voor Vandaag

1. **Beslis en activeer de SYBB campagne (of bevestig bewust uit).** Wat: campagne `2026: SYBB` in Meta Ads Manager op ACTIVE zetten, of expliciet vastleggen dat SYBB voorlopig on hold is. Waarom: nul spend de hele maand, de hele funnel hangt hierop. Hoe: Meta Ads Manager, campagne 120239435987290239 activeren en budget/creatives checken. Escalatie: **Rood (strategie, Robin beslist).**
2. **Zet basis-tracking live op de landingspagina.** Wat: scroll-depth events (25/50/75/100%) en een CTA-click event toevoegen aan `www.startyourballoonbusiness.com`. Waarom: zonder deze events blijven secties 3 en 4 leeg en kan geen enkele optimalisatie onderbouwd worden. Hoe: PostHog autocapture of custom events via de site-editor (Wix/Odoo), matchen op UTM `utm_content`. Escalatie: **Oranje (site-editor nodig).**
3. **Controleer de UTM-link tussen ads en pagina vóór heractivatie.** Wat: verifieer dat de advertentie-URLs de conventie `utm_source=meta&utm_medium=cpc&utm_campaign=sybb&utm_content=hXX_bX_ctaX` dragen en dat PostHog deze op de LP ontvangt. Waarom: nu de campagne toch uitstaat is dit hét moment om de meetketen kloppend te maken, zodat de eerste dag ná heractivatie meteen bruikbare data oplevert. Hoe: Meta ad-URL tags plus een PostHog testbezoek. Escalatie: **Geel (Robin goedkeuring).**

---

### Databron-notities
- Meta: token beperkt tot act_1489853856181844 (AmbitionAvenue) en act_567892422940728 (Sempertex Ad Account). SYBB campagne staat in de Sempertex-account.
- PostHog: host `www.startyourballoonbusiness.com`, 61 pageviews / 56 bezoekers over de laatste 30 dagen. Verreweg het grootste verkeer in dit project gaat naar `www.sempertexeurope.com` (23.100 pageviews/30d), niet naar de SYBB LP.
- Geen Google-bronnen (Gmail, Calendar, Drive, Sheets, Docs, Slides) gebruikt. Uitsluitend Meta Ads MCP en PostHog MCP, output alleen lokaal opgeslagen.
