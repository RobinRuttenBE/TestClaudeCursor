# Morning Report — 2026-05-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Klaar. Hieronder de samenvatting voor in de console:

## Meta Ads Rapport — 21 May 2026

**Status: geen actieve campagnes.** Alle SYBB en Nozzle Up campagnes staan PAUSED. Ambition Avenue (`act_1489853856181844`) heeft ook geen campagnes. Hieronder de lifetime data van de drie meest recente gepauzeerde campagnes.

### Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|------:|------------:|-------:|----:|----:|----:|------:|-----:|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) + CPM €16,34 (>€15). Slechts 1 dag actief. Niet herstarten in deze vorm.
- **Last push Nozzle Up** — ROAS 0,8x. Funnel/aanbod lekt, ads doen hun werk. Niet rebooten zonder LP fix.

### Top performers
- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** 2026: SYBB — €0,21
- **Beste ROAS:** 2026: SYBB — 17,8x

### Samenvatting
- **Totaal spend (lifetime, 3 campagnes):** €3.410,24
- **Belangrijkste lek:** ATC → purchase in SYBB funnel (53 → 6 = 11,3%, benchmark 25-40%). De ads werken, de checkout lekt.
- **Hormozi 70-20-10 aanbeveling:** Eerst checkout funnel fixen op startyourballoonbusiness.com, dan 2026: SYBB hoofdcampagne herstarten met bestaande winnende creatives. Geen nieuwe euro tot de funnel staat.

### Output
- **Lokaal:** `Output/Reports/Daily/2026-05-21_ads_report.md` (commit `1931406`, gepusht)
- **Google Sheet:** overgeslagen per run-instructie

> **Wil je funnel data toevoegen?** Geef dan PostHog of Wix Analytics metrics: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Met die data draai ik `/funnel-diagnose`.

---

Report `Output/Reports/Daily/2026-05-20_sybb_report.md` aangemaakt, gecommit en gepusht.

**Belangrijkste bevindingen:**
- Meta Ads campagne **"2026: SYBB" staat op PAUSED** — geen spend, impressies of clicks op 2026-05-20 én in de 7-daagse window
- Landing page kreeg 3 organische bezoeken (2× Instagram bio link, 1× Facebook bio link), allemaal op `/`, gem. duur ~19s
- **Scroll-depth en CTA-click events ontbreken in de event taxonomy** van dit PostHog project — die delen van de SKILL-structuur zijn als "niet gemeten" gemarkeerd met een aparte actie om ze aan te zetten

**Top 3 acties in het rapport:** beslissen over heractivatie campagne, scroll/CTA tracking aanzetten in Wix, session recordings van bio link verkeer reviewen.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-21_auto_optimize.md`.

**Samenvatting:** geen actieve Meta Ads campagnes op de toegankelijke accounts (`act_567892422940728` en `act_1489853856181844`), dus geen kill-acties of 70-20-10 optimalisatie mogelijk. `act_607231713057715` gaf een auth-error — token mist toegang. SYBB campagne staat sinds 2026-04-19 op PAUSED met €100/dag budget gereed; vraagt om een heractivatie- of refresh-besluit voordat dit command weer iets te doen heeft.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
