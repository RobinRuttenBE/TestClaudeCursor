# SYBB Daily Report — 2 July 2026

> Databronnen deze run: **Meta Ads MCP (Pipeboard)** + **PostHog MCP**.
> Status: Meta Ads data opgehaald (campagne staat op pauze, geen delivery). PostHog MCP was deze sessie **niet beschikbaar** (server niet verbonden/geautoriseerd), dus landing page data ontbreekt. Zie sectie 7.

## 1. Samenvatting
Er valt gisteren weinig te rapporteren: de campagne **`2026: SYBB`** stond op **PAUSED** en heeft op 2 juli 2026 **geen enkele impressie, click of spend** gedraaid. De hele week (26 jun – 2 jul) is leeg. Zonder ad-traffic komt er ook geen verkeer op de landing page, en de PostHog-koppeling was deze run bovendien niet beschikbaar. Kortom: de funnel staat stil. De enige actie die telt is beslissen of en wanneer de campagne weer aan gaat.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID `120239435987290239`, account `act_567892422940728`)
Status: **PAUSED** · Daily budget: €100,00 · Objective: OUTCOME_SALES · Laatst gewijzigd: 19 apr 2026

| Metric | Gisteren (2 jul) | 7d Gemiddelde | Trend |
|--------|------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Meta gaf voor 2 juli én voor het volledige venster 26 jun – 2 jul lege datasets terug (geen delivery). Dit is consistent met de PAUSED-status.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|------------------|--------|-----|-----|-----------|----------------|
| — | 0 | n.v.t. | n.v.t. | geen data | geen data |

Geen actieve ads, dus geen variant-data. Zodra de campagne weer draait, komen h11–h15_b3_cta5 hier terug.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

⚪ = geen data. PostHog MCP was deze sessie niet beschikbaar (zie sectie 7). Metrics konden niet worden opgehaald voor startyourballoonbusiness.com.

## 4. Funnel Drop-off
Niet te berekenen. Er is geen ad-traffic (Meta paused) en geen PostHog-data om de stappen te vullen.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — de funnel krijgt momenteel geen instroom.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — nul instroom in de SYBB-funnel. Geen spend, geen leads. Dit is de dominante bevinding.
- 🚩 **PostHog MCP niet beschikbaar** deze run — landing page monitoring ontbreekt volledig; blinde vlek zolang de koppeling niet werkt.

(De standaard drempel-alerts — CPC-stijging, bounce >70%, scroll <50%, frequency >3 — zijn niet van toepassing zonder delivery-data.)

## 6. Top 3 Acties voor Vandaag
1. **Beslis over de campagne-status.** De `2026: SYBB` campagne staat sinds april op pauze. Bepaal of ze weer aan moet (en vanaf welke datum/budget), of dat SYBB bewust on hold staat. Zonder deze beslissing blijft de funnel leeg en heeft dit rapport dagelijks niets te meten.
   - *Impact:* hoog · *Snelheid:* direct (Meta Ads Manager) · *Escalatie:* Rood (strategie/Robin)
2. **Herstel de PostHog MCP-koppeling.** De PostHog-server was deze sessie niet verbonden/geautoriseerd. Autoriseer PostHog opnieuw (via /mcp in een interactieve sessie of `claude mcp`) zodat landing page health weer meegenomen kan worden.
   - *Impact:* middel · *Snelheid:* snel · *Escalatie:* Geel (Robin)
3. **Plan de heractivatie-check.** Zet klaar dat op de dag dat de campagne weer live gaat, dit rapport de eerste 48u extra scherp let op CPC, bounce en frequency (koude herstart = vaak dure eerste clicks).
   - *Impact:* middel · *Snelheid:* snel · *Escalatie:* Groen

## 7. Databron-notities
- **Meta Ads MCP (Pipeboard):** ✅ verbonden. Campagne gevonden en bevraagd. Resultaat: geen delivery (PAUSED). Account `act_567892422940728`. Let op: er bestaat ook een duplicaat `2026: SYBB - Kopie` (ID `120243293329420239`, eveneens PAUSED) — niet gebruikt voor dit rapport.
- **PostHog MCP:** ❌ niet beschikbaar deze sessie. De server stond op "connecting" maar er zijn geen PostHog-tools beschikbaar gekomen; landing page data kon niet worden opgehaald. Zodra de koppeling hersteld is, kan sectie 3 en 4 gevuld worden.
- Conform de run-instructie zijn uitsluitend Meta Ads MCP en PostHog MCP geraadpleegd. Geen Google-diensten, geen schrijfactie naar de Meta Ads Tracker Google Sheet.
