# Morning Report — 2026-05-20

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 2026-05-20

**Periode:** last_30d (2026-04-20 t/m 2026-05-19)
**Account:** Sempertex Ad Account (act_567892422940728)
**Status:** GEEN actieve campagnes. Alles staat op PAUSED.

### Overzicht per campagne (gesorteerd op spend, last_30d)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | IC | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|----|----|
| 2026: SYBB, Kopie | PAUSED | €77,85 | 4.287 | 119 | 2,8% | €0,65 | €18,16 | 2 | 9,00x |

*ROAS op basis van initiate_checkout waarde (€700), geen voltooide purchases.

### Context: 90 dagen

| Campagne | Status | Spend | Clicks | CTR | CPC | CPM | Purchases | ROAS |
|----------|--------|-------|--------|-----|-----|-----|-----------|------|
| 2026: SYBB | PAUSED | €2.383,30 | 11.900 | 4,2% | €0,20 | €8,48 | 6 | **18,57x** |
| 2026: SYBB, Kopie | PAUSED | €124,42 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |
| Last push Nozzle Up | PAUSED | €800,78 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |

### Ad-level (last_30d)

| Ad | Spend | CTR | CPC | CPM | IC |
|----|-------|-----|-----|-----|----|
| H13,B3,CTA5 | €31,56 | 2,0% | €1,02 | €20,80 | 0 |
| H11,B3,CTA5 | €28,14 | 2,8% | €0,51 | €14,27 | 1 |
| H12,B3,CTA5 | €18,15 | 4,1% | €0,55 | €22,74 | 1 |

### Underperformers
- **Ad H13,B3,CTA5**: CPC €1,02 (2x boven drempel), CPM €20,80, 0 IC. **KILL.**
- **2026: SYBB, Kopie (campagne)**: CPC €0,65 en CPM €18,16, 30 tot 50% slechter dan moeder-campagne.

### Top performers
- **Beste CTR last_30d:** H12,B3,CTA5, 4,1%
- **Laagste CPC last_30d:** H11,B3,CTA5, €0,51
- **Historische topper:** 2026: SYBB, ROAS **18,57x** op €2.383,30 spend (gepauzeerd 2026-04-19)

### Belangrijkste aanbeveling

Op dit moment draait er €0 aan ads. De campagne "2026: SYBB" werd op 2026-04-19 gepauzeerd terwijl de KPI's uitstekend waren (CPC €0,20, ROAS 18,57x, 6 purchases). Hormozi 70-20-10: **herstart de bewezen winnaar eerst**, kill H13 in de Kopie variant, behoud H11 en H12 voor verdere variant-tests.

### Output

- Rapport opgeslagen in `Output/Reports/Daily/2026-05-20_ads_report.md`
- Google Sheet write (stap 6) overgeslagen per instructie

---

**Wil je funnel data toevoegen?** Geef landing page metrics: visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik een `/funnel-diagnose` met #1 bottleneck en 3 actiepunten.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-19_sybb_report.md`.

**Kerncijfers 19 mei 2026:**
- **Meta Ads:** campagne `2026: SYBB` staat sinds 19 april op PAUSED — €0 spend, geen impressions, geen clicks. Geen 7d-baseline om tegen af te zetten.
- **Landing page:** 6 sessies (6 unieke bezoekers), waarvan 1 via Instagram bio_link en 5 direct. Alle 6 sessies bleven op "/" — 0 /booking visits, 100% single-pageview bounce.
- **Tracking gap:** scroll depth komt niet door (`$prev_pageview_max_scroll_percentage` is None op alle pageviews), dus de scroll 25/50/75/100 KPI's konden niet ingevuld worden.

**Top 3 acties:** (1) campagne aanzetten of vervangen door `2026: SYBB - Kopie`, (2) homepage CTA → /booking fixen in Wix, (3) scroll tracking in PostHog activeren.

---

Rapport opgeslagen, gecommit en gepusht.

## Samenvatting

**Geen automatische acties uitgevoerd** — er zijn 0 ACTIVE campagnes in `act_567892422940728`. Alle 5 campagnes (inclusief de SYBB campagne `120239435987290239`) staan op PAUSED, sinds 2026-04-19 voor SYBB.

**Twee aandachtspunten voor je:**
1. SYBB staat al een maand uit — bewust (na drempelwijziging 2026-04-13) of drift?
2. Het command refereert `act_607231713057715`, maar Pipeboard token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`. Token uitbreiden of command-definitie corrigeren.

Rapport: `Output/Reports/Daily/2026-05-20_auto_optimize.md`. Geen Google MCPs aangeroepen, niets naar Google Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
