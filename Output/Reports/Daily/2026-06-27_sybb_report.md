# SYBB Daily Report — 27 June 2026

## 1. Samenvatting
Er is **geen data te rapporteren** voor 27 June 2026. De Meta campagne **"2026: SYBB"** staat op **PAUSED** en heeft de hele week (20–27 June) nul delivery gehad: geen spend, impressions of clicks. Daarnaast was de **PostHog MCP niet beschikbaar** in deze sessie, dus landing page data van startyourballoonbusiness.com kon niet worden opgehaald. De belangrijkste actie is een keuze: de campagne weer activeren of bewust gepauzeerd laten.

## 2. Meta Ads Performance
**Campagne:** `2026: SYBB` (id `120239435987290239`) — status **PAUSED**, daily budget €100,00, objective OUTCOME_SALES. Laatst gewijzigd 19 April 2026.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Geen enkele dag tussen 20 June en 27 June 2026 vertoonde delivery. De campagne is gepauzeerd, dus er valt niets te optimaliseren op ad-niveau.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| n.v.t. | — | — | — | — | — |

Geen variant-data: campagne leverde niets uit.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
**PostHog data niet beschikbaar.** De PostHog MCP was niet verbonden met deze sessie (beschikbare MCP servers: ga4, google, imessage, instagram, lottiefiles, pipeboard-meta-ads). Conform de strikte regel voor deze run is geen Google MCP als vervanging gebruikt. Landing page metrics konden daarom niet worden opgehaald.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n.b. | n.b. | <55% | ⚪ |
| Avg Session Duration | n.b. | n.b. | >90s | ⚪ |
| Scroll 25% | n.b. | n.b. | >80% | ⚪ |
| Scroll 50% | n.b. | n.b. | >60% | ⚪ |
| Scroll 75% | n.b. | n.b. | >40% | ⚪ |
| Scroll 100% | n.b. | n.b. | >20% | ⚪ |
| CTA Click Rate | n.b. | n.b. | >4% | ⚪ |

⚪ = data niet beschikbaar (n.b. = niet beschikbaar)

## 4. Funnel Drop-off
Niet te berekenen. Met nul betaald verkeer (campagne paused) en zonder PostHog data is er geen funnel om te analyseren.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** en heeft 8 dagen op rij (20–27 June) nul delivery. Als de bedoeling was dat SYBB live stond, draait er momenteel geen acquisitie.
- 🚩 **PostHog MCP niet verbonden.** De landing page monitoring werkt niet zolang de PostHog MCP niet beschikbaar is. Dit blokkeert de cross-reference analyse die de kern is van dit rapport.

## 6. Top 3 Acties voor Vandaag
1. **Beslis over campagne-status (PAUSED).** Wat: bepaal of `2026: SYBB` weer geactiveerd moet worden of bewust gepauzeerd blijft. Waarom: nul delivery sinds minimaal 20 June betekent nul nieuwe SYBB leads via Meta. Hoe: Meta Ads Manager → campagne activeren (of bevestigen dat pauze gewenst is). Escalatie: Geel (Robin goedkeuring — budget/strategie beslissing).
2. **Herstel de PostHog MCP verbinding.** Wat: zorg dat de PostHog MCP weer beschikbaar is in de Claude sessie. Waarom: zonder PostHog is er geen landing page health en geen funnel/cross-reference analyse mogelijk. Hoe: PostHog MCP server config controleren en opnieuw verbinden. Escalatie: Geel.
3. **Re-run dit rapport zodra campagne live is én PostHog werkt.** Wat: genereer het dagrapport opnieuw met beide databronnen actief. Waarom: alleen met live delivery + landing page data levert dit rapport bruikbare optimalisatie-inzichten. Hoe: `/morning-report` of de daily-sybb-report skill opnieuw draaien. Escalatie: Groen (auto).

---
*Databronnen: Meta Ads MCP (Pipeboard) — campagne bevestigd, status PAUSED, geen delivery. PostHog MCP — niet beschikbaar in deze sessie. Geen Google MCPs gebruikt conform de strikte regel voor deze run.*
