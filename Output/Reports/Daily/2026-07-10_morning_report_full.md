# Morning Report — 2026-07-10

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-10_ads_report.md`.

## Meta Ads Rapport — 10 juli 2026

⚠️ **Geen actieve campagnes.** Het Sempertex Ad Account had **€0,00 spend** in de laatste 30 dagen. Alles staat op pauze. Hieronder de meest recente gepauzeerde campagnes met lifetime data (fallback-regel).

### Overzicht per campagne (lifetime, gepauzeerd)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 (15 leads) | 0,18x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Underperformers
- **Campagne "2026: SYBB - Kopie"** — CPC €0,64 + CPM €16,34, 0 aankopen → niet heropstarten
- **Ad "H11 Kopie 1"** — CPC €0,67, hoogste spend (€521), 0 rendement → pauzeren
- **Ad "H13 Kopie 3"** — CPC €0,63, terwijl origineel 9x beter presteert → uitzetten
- **Ad "SYBB w/ Semp (BLACK)"** — CPC €0,61 + CTR 1,0% → vervangen door video-hooks

### Top performers
- **Beste CTR & laagste CPC**: ad **H13,B3,CTA5** (origineel) — **9,8% CTR / €0,07 CPC**
- **Beste ROAS**: 2026: SYBB — 0,18x (enige met aankopen)

### Kern-inzicht
De ads zijn sterk (CTR 4,1%, CPC €0,21), maar 297k impressies leverden slechts **6 aankopen** op. De bottleneck zit **ná de klik** (landingspagina/funnel), niet in de creatives. Bij heropstart: schaal H13 (70%), behoud H15/H14 (20%), faseer alle "Kopie"-adsets uit (10%).

**Google Sheet-write:** overgeslagen conform de run-instructie (geen Google MCP gebruikt).

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit PostHog, Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` om die 6-aankopen-bottleneck scherp te krijgen. Ik kan de PostHog-data ook zelf ophalen als je wilt.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-09_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevindingen

Twee dingen maakten dit een leeg-verkeer-rapport, en het is belangrijk dat je ze weet:

1. **De campagne `2026: SYBB` staat op PAUSED.** Meta gaf **nul** impressies, clicks en spend terug voor 9 juli (en voor de hele week 2–8 juli). Er liep dus geen SYBB-acquisitie. De campagne heeft wél sterke *lifetime* cijfers (CTR 4,06%, CPC €0,21, 6 aankopen t.w.v. €44.247), dus het probleem is niet de creatives, maar dat de campagne uit staat.

2. **De PostHog MCP was niet beschikbaar** tijdens deze run. De connector was nog aan het verbinden en leverde geen tools op, ook niet na herhaald zoeken. Ik heb, conform je strikte regel, **geen enkele Google- of alternatieve bron** aangeroepen om dit op te vullen — landing page health, bounce rate, scroll depth en de funnel staan daarom als "geen data" in het rapport.

## Wat ik wél heb gebruikt
Alleen de Meta Ads MCP (Pipeboard), account `act_567892422940728`, campagne `120239435987290239`. Geen Gmail, Calendar, Drive, Sheets, Docs of Slides. Niet naar de Google Sheet tracker geschreven. Alleen lokaal opgeslagen.

## Top acties (staan uitgewerkt in het rapport)
1. **Beslis of `2026: SYBB` weer aan moet** (daily budget €100 staat klaar) of bewust gepauzeerd blijft — Robin-beslissing.
2. **PostHog-connector herstellen** via `/mcp` in een interactieve sessie, anders blijft het dagrapport half.
3. **Dubbele campagne opruimen** — er staat ook een gepauzeerde `2026: SYBB - Kopie` in het account.

Wil je dat ik het rapport opnieuw draai zodra de PostHog-connector verbonden is, of wil je eerst de campagne-beslissing maken?

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-10_auto_optimize.md` en gepusht.

## Kort resultaat

**Geen acties uitgevoerd — er zijn geen actieve campagnes.**

- **Primair account `act_567892422940728`:** alle 5 campagnes staan op `PAUSED`, inclusief `2026: SYBB` (€100/dag). Geen actieve ads, dus de kill-regels (Link CTR < 0.8%, CPC (link) > €1.50) en de 70-20-10 classificatie zijn niet van toepassing. Dit klopt met het daily report van gisteren (SYBB gepauzeerd).
- **Secundair account `act_607231713057715`:** **niet toegankelijk** met dit token. De MCP meldt dat het token wél `act_1489853856181844` mag zien (dat niet in het command staat).

## Twee beslissingen voor jou
1. **SYBB weer aanzetten?** Zodra die live is, kan dit command dagelijks daadwerkelijk optimaliseren.
2. **Account-scope:** het command wijst naar een account zonder toegang, terwijl het token een ander account (`act_1489853856181844`) wél dekt. Wil je dat meenemen of de command-config bijwerken?

Alleen de Meta Ads MCP is gebruikt — geen Google MCP's, niet naar de Tracker Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
