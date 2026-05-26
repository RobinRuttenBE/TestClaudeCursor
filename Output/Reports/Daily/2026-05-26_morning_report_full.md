# Morning Report — 2026-05-26

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 26 May 2026

Geen ACTIVE campagnes; rapport gebaseerd op lifetime data van de 3 grootste gepauzeerde campagnes.

### Overzicht per campagne (lifetime)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Purchases | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|-----------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 2,24 | 6 (€442) | 0,18x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 2,39 | 3 (€6) | 0,01x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,42 | 0 | n.v.t. |

### Underperformers

- **2026: SYBB - Kopie** CPM €16,34 + CPC €0,64. Duplicaten van BATCH 2 hebben Meta dwingen herleren — niet heractiveren in huidige vorm.
- **H11 Kopie 1** (€521 spend, CPC €0,67) en **H13 Kopie 3** (CPC €0,63): permanent pauzeren, focus op originelen.
- **SYBB w/ Semp (BLACK)** CTR 1,0% + CPC €0,61: statische creatief loslaten.

### Top performers

- **Beste echte hook:** H15, B3, CTA5 (BATCH 2) — CTR 4,3%, CPC €0,15.
- **Laagste CPC:** H13, B3, CTA5 (BATCH 2) — €0,07 (maar 9,8% CTR is een uitschieter, valideer in PostHog).
- **Geen enkele campagne haalt ROAS 1,0x** — purchase tracking is gebroken (€6 totaalwaarde op €800 Nozzle Up spend).

### Samenvatting

- **Totaal lifetime spend (3 campagnes):** €3.410,24
- **Spend last_30d:** €0,00
- **Hormozi 70-20-10 bij heropstart:** 70% op H15/BATCH 2 winnaar, 20% op H15-variaties, 10% nieuwe hook-test.
- **Kritisch:** Meta Pixel + Wix purchase events valideren vóór heropstart, anders blijft ROAS onbetrouwbaar.

### PostHog cross-reference (last 30d, startyourballoonbusiness.com)

110 pageviews / 90 sessies / 81 visitors. Verkeer komt uitsluitend via Instagram/Facebook bio links en direct, één Meta-UTM klik. Geen actieve paid funnel om te benchmarken.

### Output

Rapport opgeslagen in `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-26_ads_report.md`. Geen schrijfacties naar Google Sheet (overgeslagen volgens instructie).

**Wil je funnel data toevoegen?** Geef de landing page metrics uit Wix Analytics of GA4 (visitors, opt-in/booking clicks, add to cart, completed purchases), dan draai ik een volledige `/funnel-diagnose` analyse.

---

Report saved to `Output/Reports/Daily/2026-05-25_sybb_report.md`.

**Kernpunten van 25 mei:**
- Meta Ads campagne "2026: SYBB" staat al >30 dagen op PAUSED → €0 spend, 0 clicks, 0 impressies gisteren.
- Landing page kreeg 0 pageviews op 25 mei. Over de 7d window (18-24 mei) slechts 16 pageviews, 15 sessies, 93,3% bounce, 193s avg duration.
- Alle 7d-traffic kwam organisch binnen via Instagram/Facebook bio link (`mtrbio.com`).
- PostHog logt geen scroll-depth of CTA-click events op deze property → 5 van 7 KPI-rijen zijn `niet getrackt`.

**Top 3 acties:** (1) beslis campagne herstarten of archiveren, (2) fix scroll/CTA tracking op de Wix site, (3) verlaag bounce via een directe workshop-link op de bio link landing.

Geen Google MCP gebruikt — uitsluitend Pipeboard Meta Ads MCP en PostHog MCP. Output is alleen lokaal weggeschreven.

---

Klaar. Geen actieve campagnes gevonden — auto-optimize had niks te pauzeren of te classificeren.

**Bevindingen:**
- `act_567892422940728`: 0 actieve campagnes (5 gepauzeerd, incl. 2026: SYBB sinds 2026-04-19)
- `act_1489853856181844`: 0 campagnes
- `act_607231713057715`: token heeft geen toegang (genoemd in command, maar buiten allowlist)

**Acties uitgevoerd:** 0 ads gepauzeerd (geen actieve ads om te evalueren).

**Voorstellen:** SYBB campagne heractiveren of nieuwe campagne lanceren — de funnel ligt 37 dagen stil. Volledig rapport: `Output/Reports/Daily/2026-05-26_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
