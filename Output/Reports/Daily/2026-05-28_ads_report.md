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
