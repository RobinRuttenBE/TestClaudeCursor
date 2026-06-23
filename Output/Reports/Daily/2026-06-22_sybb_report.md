# SYBB Daily Report — 22 June 2026

> **Datastatus:** Dit rapport kon niet volledig worden samengesteld. De Meta Ads campagne stond gisteren stil (geen delivery) en de PostHog MCP was in deze sessie niet beschikbaar. Details per sectie hieronder.

## 1. Samenvatting
Er valt voor 22 juni 2026 geen prestatie te rapporteren: de campagne **"2026: SYBB"** is **PAUSED** en had gisteren nul impressies, nul clicks en nul spend. De campagne draait feitelijk niet meer sinds eind april 2026 (laatste spend in april). Daarnaast kon de **landing page health niet worden opgehaald** omdat de PostHog MCP niet verbonden is in deze sessie. Kortom: niets om te optimaliseren op adniveau zolang de campagne uit staat; eerste actie is een beslissing over heractivatie.

## 2. Meta Ads Performance
**Bron:** Meta Ads MCP (Pipeboard) · Account `Sempertex Ad Account` (act_567892422940728) · Campagne `2026: SYBB` (ID 120239435987290239)
**Campagnestatus:** 🔴 PAUSED (laatst gewijzigd 19 apr 2026)

| Metric | Gisteren (22 jun) | 7d (15–21 jun) | Trend |
|--------|-------------------|----------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De campagne leverde geen data op voor gisteren én voor het volledige 7-daagse venster. Er is dus geen 7d-gemiddelde om tegen af te zetten en geen trend te bepalen.

### Ad Variant Performance
Geen data beschikbaar — campagne staat uit. Er zijn geen actieve ads (utm_content h11_b3_cta5 t/m h15_b3_cta5) die gisteren impressies of clicks genereerden.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

### Context — laatste bekende prestaties (ter referentie, niet gisteren)
De laatste maanden waarin de campagne wél draaide (via maandbreakdown over de looptijd):

| Maand | Impressions | Clicks | Spend | CTR | CPC |
|-------|-------------|--------|-------|-----|-----|
| Jan 2026 | 16.268 | 167 | €101,74 | 1,03% | €0,61 |
| Mrt 2026 | 189.067 | 9.965 | €1.323,83 | 5,27% | €0,13 |
| Apr 2026 | 91.839 | 1.935 | €1.059,47 | 2,11% | €0,55 |
| **Lifetime** | **297.174** | **12.067** | **€2.485,04** | **4,06%** | **€0,21** |

> Mei en juni 2026 ontbreken volledig: geen delivery in die maanden. Maart was veruit de sterkste maand (CTR 5,27%, CPC €0,13).

## 3. Landing Page Health
**Bron:** PostHog MCP — ⚠️ **NIET BESCHIKBAAR in deze sessie.**

De PostHog MCP is niet verbonden, dus pageviews, bounce rate, sessieduur, scroll depth, CTA click rate en session recordings voor `startyourballoonbusiness.com` konden niet worden opgehaald. Conform de strikte regel voor deze run is er bewust **geen** alternatieve Google/GA4-bron gebruikt.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

**Actie nodig:** verbind de PostHog MCP voordat het volgende dagrapport draait (zie sectie 6).

## 4. Funnel Drop-off
Niet te berekenen. Stap 1 (ad clicks via Meta) is nul én de PostHog-stappen (scroll 50%, CTA click, /booking pageview) ontbreken. De volledige funnel mist dus aan beide kanten data.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** niet vast te stellen zonder actieve campagne en PostHog-data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat uit (PAUSED).** "2026: SYBB" levert sinds eind april 2026 niets meer. Twee maanden zonder delivery betekent geen leadflow naar de SYBB-workshop via dit kanaal.
- 🚩 **PostHog MCP niet verbonden.** Landing page health kan niet gemonitord worden; het dagrapport mist standaard de helft van zijn databronnen zolang dit zo blijft.
- ℹ️ Geen ad-fatigue, CPC- of bounce-anomalieën te melden — er is simpelweg geen actuele data.

## 6. Top 3 Acties voor Vandaag
1. **Beslis over heractivatie van "2026: SYBB"** (impact: hoog · snelheid: hoog). De campagne staat al ~2 maanden stil. Bepaal: heractiveren we (met welk budget en welke winnende creatives), of is SYBB-acquisitie bewust gepauzeerd? Maart 2026 presteerde sterk (CTR 5,27%, CPC €0,13) — die winnende variant is het logische startpunt bij herstart. *Escalatie: Rood (strategie/Robin).*
2. **Verbind de PostHog MCP** (impact: hoog · snelheid: middel). Zonder PostHog mist het dagrapport bounce rate, scroll depth, CTA clicks en session recordings. Controleer de MCP-config zodat `startyourballoonbusiness.com` weer uitleesbaar is vóór het volgende rapport. *Escalatie: Geel (Robin goedkeuring/setup).*
3. **Bevestig de juiste databron-koppeling voor toekomstige runs** (impact: middel · snelheid: hoog). Leg vast dat het dagrapport alleen betekenisvol is als (a) de campagne actief is én (b) PostHog verbonden is. Zolang de campagne PAUSED blijft, kan het dagelijkse rapport worden opgeschort om ruis te voorkomen. *Escalatie: Groen.*

---
*Gegenereerd op 23 juni 2026 voor rapportagedatum 22 juni 2026. Databronnen: Meta Ads MCP (Pipeboard) — campagne inactief; PostHog MCP — niet verbonden. Geen Google/GA4-bronnen gebruikt conform run-instructie.*
