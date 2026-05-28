# Morning Report — 2026-05-28

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-05-28

**Geen actieve campagnes.** Lifetime data van 5 gepauzeerde campagnes op `act_567892422940728` (totaal spend €4.867,46).

### Overzicht (gesorteerd op spend)

| # | Campagne | Status | Spend | CTR | CPC | CPM | Purch. | ROAS |
|---|----------|--------|-------|-----|-----|-----|--------|------|
| 1 | 2026: SYBB | PAUSED | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,81x* |
| 2 | Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,30x |
| 3 | Last push Nozzle Up | PAUSED | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| 4 | Nozzle Up END OF AUGUST | PAUSED | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,37x |
| 5 | 2026: SYBB - Kopie | PAUSED | €124,42 | 2,6% | €0,64 | €16,34 | 0 | — |

\* SYBB ROAS lijkt opwaarts vertekend (€7.374/order avg, hoger dan ticketprijs). Mogelijk attributie-issue.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34 (beide boven drempel). Beperkte run-tijd (2 dagen), niet representatief.
- **Nozzle Up END OF AUGUST** — CTR 0,99% marginaal onder 1% drempel ondanks zeer lage CPM.

### Top performers
- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste zuivere ROAS:** Campagne Nozzle Up 2025 1 — 8,30x

### Belangrijkste funnel-inzicht
SYBB-funnel knelpunt zit op **LPV → ATC** (6.992 LPV → 53 ATC = 0,76%). De ad zelf werkt (4,1% CTR), de landing page converteert niet door. Onderzoek met PostHog scroll depth + session recordings.

### Aanbeveling
1. Heractiveer SYBB met bewezen winnende hooks (70-20-10 regel)
2. Diagnose LPV → ATC drop op de SYBB landing page
3. Laat "2026: SYBB - Kopie" varen, focus op creative variaties van de hoofdcampagne

### Output
- Rapport opgeslagen: `Output/Reports/Daily/2026-05-28_ads_report.md`
- Google Sheet write **overgeslagen** per strikte regel voor deze run

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch `/funnel-diagnose` met de Meta data + LP data erbij.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-27_sybb_report.md`.

**Belangrijkste bevindingen:**
- Meta campagne `2026: SYBB` (id 120239435987290239) staat **PAUSED** sinds 19 april 2026 op account act_567892422940728. Geen spend, geen clicks, geen impressions over 20-27 mei.
- PostHog ziet 1 pageview op 27 mei (YouTube referral, `utm_content=bio_link`) en 9 pageviews over de hele week, allemaal op `/`. Geen rageclicks, dead clicks of exceptions.
- Bounce rate, scroll depth en CTA click rate zijn niet meetbaar: de landing page heeft alleen PostHog autocapture events, geen custom `cta_clicked`, `scroll_*` of `booking_started` events.

**Top 3 acties:** (1) besluit nemen over reactivering van de SYBB campagne, (2) PostHog tracking uitbreiden met scroll/CTA events op de Wix LP, (3) bio_link traffic instrumenteren met UTM standaard.

Geen Google MCPs of tracker sheet aangeroepen, output uitsluitend lokaal in `Output/Reports/Daily/`.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-28_auto_optimize.md`.

**Samenvatting:**
- `act_567892422940728` (Sempertex) — 5 campagnes gevonden, **allemaal PAUSED**. SYBB hoofdcampagne staat al ~40 dagen uit (sinds 2026-04-19).
- `act_1489853856181844` (Ambition Avenue) — 0 actieve campagnes.
- `act_607231713057715` — token mist toegang tot dit account.

**Acties uitgevoerd:** 0 (geen actieve ads om kill-regels op toe te passen).

**Beslispunt voor jou:** wil je de SYBB campagne weer activeren of archiveren? Zolang niets live staat heeft `/ads-auto-optimize` geen werk om te doen.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
