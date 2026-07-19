# SYBB Daily Report — 18 juli 2026

> Databronnen voor deze run: **Meta Ads MCP (Pipeboard)** en **PostHog MCP**, zoals afgesproken. Geen Google-bronnen gebruikt.

## 1. Samenvatting
Er is gisteren **geen SYBB-activiteit** om te rapporteren. De campagne **"2026: SYBB"** staat op **PAUSED** (laatst gewijzigd 19 april 2026) en had op 18 juli 2026 nul spend, nul impressies en nul clicks. Er is de afgelopen 7 én 30 dagen geen enkele spend geregistreerd op het account. Daarnaast kon de **PostHog MCP niet worden bereikt** in deze sessie, dus de landing page health-cijfers ontbreken. Netto: dit rapport is een status- en dataverificatierapport, geen performancerapport.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID `120239435987290239`)
**Status:** 🔴 PAUSED · Objective: OUTCOME_SALES · Dagbudget: €100,00 · Laatst gewijzigd: 19 apr 2026

| Metric | Gisteren (18 jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

*Bron: `get_insights` op campagne-ID voor `yesterday` gaf een lege dataset terug; `bulk_get_insights` op account-niveau gaf `no_data` voor last_7d en last_30d. Bevestigd: de campagne draait niet.*

### Ad Variant Performance
Geen ad-variant data beschikbaar — de campagne is gepauzeerd en heeft geen leveringen. De verwachte varianten (`h11_b3_cta5` t/m `h15_b3_cta5`) kunnen pas gerapporteerd worden zodra de campagne weer live is.

**Beste variant:** n.v.t. (geen data)
**Slechtste variant:** n.v.t. (geen data)

> Let op: er bestaat ook een gepauzeerde kopie **"2026: SYBB - Kopie"** (ID `120243293329420239`, aangemaakt 19 apr 2026). Controleer welke van de twee de bedoelde live-campagne is voordat je heractiveert, om dubbele levering te voorkomen.

## 3. Landing Page Health
🔴 **Niet beschikbaar — PostHog MCP niet bereikbaar in deze sessie.**

De PostHog MCP-tools zijn tijdens deze run niet geladen (server bleef in "connecting" staan en leverde geen tools). Er kon dus geen data opgehaald worden voor startyourballoonbusiness.com.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

*Actie: PostHog MCP opnieuw verbinden/autoriseren in een interactieve sessie, daarna dit rapport aanvullen.*

## 4. Funnel Drop-off
Niet te berekenen. Geen ad-verkeer (campagne gepauzeerd) én geen PostHog-data. Zodra beide bronnen weer leveren:
Pageview (100%) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** onbekend — geen data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED** — SYBB genereert momenteel geen enkel verkeer. Als dit onbedoeld is, is dit de #1 prioriteit.
- 🚩 **Nul spend gedurende ≥30 dagen** — de SYBB-funnel is al langere tijd inactief, niet enkel gisteren.
- 🚩 **PostHog MCP onbereikbaar** — het cross-reference gedeelte (ad ↔ landing page), de kern van dit rapport, kan niet worden uitgevoerd tot de connectie hersteld is.
- 🚩 **Dubbele SYBB-campagne aanwezig** ("2026: SYBB" + "2026: SYBB - Kopie", beide paused) — risico op dubbele levering bij onzorgvuldige heractivatie.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of SYBB weer live moet.** Als de campagne actief hoort te zijn: heractiveer bewust één van beide campagnes (niet allebei) in Meta Ads Manager en verwijder/archiveer de overbodige kopie. *Impact: hoog · Snelheid: direct.*
2. **Herstel de PostHog MCP-connectie** in een interactieve sessie (autoriseer de PostHog-connector), en genereer dit rapport daarna opnieuw zodat landing page health en de funnel wél gevuld zijn. *Impact: hoog · Snelheid: minuten.*
3. **Zodra beide bronnen live zijn: draai een verse dagrapportage** met ad-variant performance (`utm_content`) gekruist met LP-gedrag, zodat de eerste live dag meteen op mismatches (CTR vs bounce, CPC vs conversie) gemonitord wordt. *Impact: middel · Snelheid: na stap 1+2.*

---

*Gegenereerd op 19 juli 2026. Databronnen: Meta Ads MCP (Pipeboard) — gelukt; PostHog MCP — niet bereikbaar. Geen Google-bronnen geraadpleegd, niet naar de Google Sheet-tracker geschreven.*
