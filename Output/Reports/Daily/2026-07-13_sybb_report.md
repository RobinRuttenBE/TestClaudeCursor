# SYBB Daily Report — 13 July 2026

> **Databronnen:** Meta Ads MCP (Pipeboard) + PostHog MCP.
> Voor deze run zijn uitsluitend deze twee bronnen benaderd. Geen Google (Gmail/Calendar/Drive/Sheets/Docs/Slides) aangeroepen, niet naar de Google Sheet tracker geschreven.

## 1. Samenvatting
Er valt over gisteren geen performance te rapporteren: de campagne **`2026: SYBB` staat op PAUSED** en heeft op 13 juli (en de volledige afgelopen 30 dagen) **nul delivery** gehad, geen spend, impressions of clicks. Daarnaast kon de **PostHog data niet worden opgehaald** omdat er in deze sessie geen PostHog MCP verbonden is. Er is dus geen live landing page of funnel data beschikbaar. Belangrijkste actie: bepalen of SYBB weer aangezet moet worden, en de PostHog connector herstellen zodat het rapport weer volledig draait.

## 2. Meta Ads Performance
**Campagne:** `2026: SYBB` (id `120239435987290239`)
**Account:** Sempertex Ad Account (`act_567892422940728`, EUR)
**Status:** 🔴 PAUSED — laatst gewijzigd 19 April 2026, geen budgetlevering sinds april

| Metric | Gisteren (13 jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Insights API gaf een lege dataset terug voor 13 juli, voor het 7-daags venster (7–13 juli, dag-voor-dag allemaal leeg) én voor de laatste 30 dagen (14 juni – 13 juli). Dit is consistent met de PAUSED status: er is geen actieve levering.

### Ad Variant Performance
Geen ad-level data beschikbaar (campagne inactief). Zodra de campagne weer draait, wordt hier gebroken op `utm_content` (h11_b3_cta5, h12_b3_cta5, h13_b3_cta5, h14_b3_cta5, h15_b3_cta5).

**Beste variant:** n.v.t. — geen data
**Slechtste variant:** n.v.t. — geen data

> Let op: er bestaat ook een gepauzeerde duplicaat-campagne `2026: SYBB - Kopie` (id `120243293329420239`). Ook deze levert niets. Controleer welke van de twee de bedoelde live-campagne moet worden voordat je heractiveert, om dubbele levering / verwarring te voorkomen.

## 3. Landing Page Health
**Site:** startyourballoonbusiness.com

🔴 **PostHog data niet beschikbaar.** Er is in deze sessie geen PostHog MCP verbonden, dus pageviews, bounce rate, session duration, scroll depth en CTA click rate konden niet worden opgehaald.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

## 4. Funnel Drop-off
Niet te berekenen zonder PostHog data.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** onbekend — PostHog bron ontbreekt. Met de campagne op pauze is er sowieso geen betaald verkeer dat de funnel voedt.

## 5. Rode Vlaggen 🚩
- 🔴 **Campagne `2026: SYBB` staat op PAUSED** en levert al ~30+ dagen niets. Als SYBB actief hoort te zijn, is dit budgetverlies aan momentum en de belangrijkste bevinding van vandaag.
- 🔴 **PostHog MCP niet verbonden** in deze sessie. Zolang dit niet is hersteld draait het dagelijkse rapport half-blind (geen landing page/funnel monitoring).
- 🟡 **Dubbele campagne** aanwezig (`2026: SYBB` + `2026: SYBB - Kopie`), beide gepauzeerd. Risico op verwarring/dubbele activatie.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of `2026: SYBB` weer aan moet.** Als de workshop-funnel actief hoort te lopen: heractiveer de juiste campagne (niet de duplicaat) in Meta Ads Manager en bevestig het dagbudget (staat ingesteld op €100/dag). *Waarom:* nul delivery in de laatste 30 dagen. *Escalatie:* Oranje (Robin-beslissing + Ads Manager).
2. **Herstel de PostHog MCP connectie.** Zonder PostHog is er geen landing page/funnel monitoring en blijft dit rapport incompleet. Verbind PostHog opnieuw via `/mcp` in een interactieve sessie. *Waarom:* bron ontbrak volledig vandaag. *Escalatie:* Geel.
3. **Ruim de duplicaat op.** Archiveer of hernoem `2026: SYBB - Kopie` zodat er één bron van waarheid is voordat er weer live gegaan wordt. *Waarom:* voorkomt dubbele activatie/rapportage-ruis. *Escalatie:* Geel.

---
*Gegenereerd 14 July 2026. Meta Ads via Pipeboard MCP (live, lege dataset door PAUSED campagne). PostHog: bron niet verbonden — landing page en funnel secties niet ingevuld. Geen data verzonnen.*
