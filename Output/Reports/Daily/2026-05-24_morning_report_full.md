# Morning Report — 2026-05-24

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Hier is het rapport.

## Meta Ads Rapport, 2026-05-24

**Status:** Geen actieve campagnes. Rapport toont 5 gepauzeerde campagnes uit het Sempertex Ad Account.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.383,30 | 280.906 | 11.900 | 4,2% | €0,20 | €8,48 | 6 | 18,6x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0x |

*\* ROAS opgeblazen door pixel value misconfiguratie.*

### Underperformers

- **2026: SYBB - Kopie**: CPC €0,64 én CPM €16,34, beide boven drempel
- **Nozzle Up END OF AUGUST**: CTR 1,0%, op de ondergrens
- **Last push Nozzle Up**: ROAS 0,8x, verlies op deze laatste push

### Top performers

- **Beste CTR:** 2026: SYBB, 4,2%
- **Laagste CPC:** Nozzle Up END OF AUGUST, €0,17
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1, 8,3x (€7.081 omzet op €853 spend)

### Samenvatting

- **Totaal spend:** €4.765,72
- **Beste performer:** Campagne Nozzle Up 2025 1, 8,3x ROAS, AOV €1.180. Sterkste template voor relaunch.
- **Slechtste performer:** Last push Nozzle Up, 0,8x ROAS. Funnel knelde aan checkout.
- **Belangrijke vlag:** 2026: SYBB rapporteert €7.374 per purchase (€44.247 totaal voor 6 purchases). Pixel value tracking is misgeconfigureerd, ROAS-data onbetrouwbaar tot dit gefixed is.

### Aanbeveling (Hormozi 70-20-10)

- **70%:** Relaunch op het Campagne Nozzle Up 2025 1 template, hoogste betrouwbare ROAS.
- **20%:** Combineer SYBB-hooks (4,2% CTR) met de Nozzle Up funnel-flow die converteert.
- **10%:** Fix pixel value tracking voor SYBB voordat nieuwe campagnes live gaan.

### Output

- Rapport: `Output/Reports/Daily/2026-05-24_ads_report.md`
- Gecommit en gepusht naar GitHub (commit `7ea4321`)
- Google Sheet write: overgeslagen per command argument

---

**Wil je funnel data toevoegen?** Geef dan landing page metrics uit PostHog of GA4 (landing page visitors, opt-in/booking clicks, add to cart, completed purchases). Ik kan ook direct PostHog data ophalen voor startyourballoonbusiness.com, zeg het maar.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-23_sybb_report.md`.

**Belangrijkste bevindingen:**
- **Meta Ads:** `2026: SYBB` staat sinds 19 april op PAUSED — 0 spend/impressies/clicks gisteren, geen insights data.
- **Landing page:** 0 pageviews op 23 mei (eerste nul-dag in 14 dagen; 7d-gemiddelde 3,3 pv/dag).
- **Funnel 7d:** 20 homepage sessies → 1 booking → 1 checkout (95% drop-off op homepage).
- **Verkeersbronnen:** instagram bio (9 pv) + direct (9 pv) + facebook bio (5 pv); geen Meta Ads attributie.
- **Meetgap:** scroll depth, CTA clicks en sessieduur worden niet getrackt — 4 van de 7 KPI rijen leeg.

**Top 3 acties:** (1) go/no-go op campagne hervatten, (2) scroll + CTA tracking implementeren in Wix/PostHog, (3) session recordings reviewen voor homepage drop-off oorzaak.

Geen Google MCPs aangeroepen, geen sheet updates uitgevoerd — conform strikte run-regel.

---

Rapport opgeslagen, gecommit en gepusht.

**Auto-Optimize 2026-05-24 — no-op run.** Er staan geen actieve campagnes in act_567892422940728 (5 campagnes, allemaal PAUSED) of act_1489853856181844 (leeg). act_607231713057715 uit het commando is niet toegankelijk voor de API token. Geen kill-regels getriggerd, geen 70-20-10 mogelijk.

Het rapport (`Output/Reports/Daily/2026-05-24_auto_optimize.md`) bevat in plaats daarvan 4 strategische voorstellen voor de relaunch, gebaseerd op de bevindingen uit het ads-report van vanochtend: pixel value fix voor SYBB, Nozzle Up 2025 1 als hoogste-ROAS template, SYBB-hooks combineren met de Nozzle Up funnel, en Last push Nozzle Up niet hergebruiken. Geen Google MCPs of Sheet-writes aangeroepen.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
