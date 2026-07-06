# Morning Report — 2026-07-06

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 6 juli 2026

> **Let op: er zijn momenteel GEEN actieve campagnes.** Zowel het Sempertex Ad Account (`act_567892422940728`) als AmbitionAvenue (`act_1489853856181844`) hebben nul actieve campagnes. Hieronder de meest recente **gepauzeerde** campagnes met hun **lifetime** performance (`last_30d` is leeg omdat alles gepauzeerd is).

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

*Conv. = aankopen. ROAS bij 3-6 aankopen is ruisgevoelig — interpreteer voorzichtig.*

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15) → dure testvariant, nul aankopen. Niet heropstarten in deze vorm.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (grens 1%) → laagste engagement ondanks goedkoopste reach.
- **Last push Nozzle Up** — ROAS 0,8x (onder break-even) → zwakste return, slechts 3 aankopen.
- Geen campagne boven frequency 3,5 (hoogste 2,89).

### Top performers

- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — 17,8x (ruisgevoelig); meest betrouwbaar sterk: Campagne Nozzle Up 2025 1 — 8,3x

### Samenvatting

- **Totaal spend**: €4.867,46 (lifetime — geen data laatste 30 dagen)
- **Beste performer**: 2026: SYBB — hoogste CTR, laagste CPC binnen de grote campagnes, duidelijk de bewezen winnaar
- **Slechtste performer**: 2026: SYBB - Kopie — te duur op alle fronten, nul aankopen
- **Aanbeveling (70-20-10)**: 70% herstart "2026: SYBB" ongewijzigd zodra budget beschikbaar is; 20% hook-variaties binnen dezelfde audience; 10% goedkoop brede-reach experiment op basis van de Nozzle Up END OF AUGUST setup (CPM €1,64) mits de hook aangescherpt wordt. Laat "2026: SYBB - Kopie" en "Last push Nozzle Up" gepauzeerd.

### Google Sheet

Overgeslagen op verzoek (strikte MCP-regel). Rapport opgeslagen in `Output/Reports/Daily/2026-07-06_ads_report.md`.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` over de gecombineerde data.

---

Klaar. Het rapport staat opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-07-05_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevindingen

Ik heb het rapport eerlijk opgesteld want er viel deze run **geen performance te meten** — om twee redenen:

**1. Meta Ads werkt, maar de campagne staat stil**
De campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED** en leverde op 5 juli **nul** impressies/clicks/spend. Ik heb dit geverifieerd met een dag-voor-dag breakdown over **1 juni t/m 5 juli** (35 dagen, allemaal leeg) — dus dit is geen tijdelijke dip, de campagne draait al minstens sinds begin juni niet.

**2. PostHog MCP is niet beschikbaar**
De PostHog-server laadde in deze sessie geen enkele tool (`mcp__posthog__*` bestaat niet in het register). Landing page metrics voor startyourballoonbusiness.com konden dus niet opgehaald worden. Ik heb hier **niets** verzonnen — de landing page sectie staat op "geen data".

**Regel gerespecteerd:** alleen Meta Ads MCP gebruikt. Geen enkele Google-tool aangeroepen, niet naar de Tracker Sheet geschreven, alleen lokale markdown output.

## Wat je nu kunt doen
1. Beslis of `2026: SYBB` weer live moet (heractiveren in Meta, of bevestig dat de pauze bewust is zodat het niet elke ochtend als rode vlag terugkomt).
2. Herstel de PostHog connector zodat de landing page monitoring weer werkt.
3. Draai het rapport opnieuw zodra beide opgelost zijn — dan levert het pas echte funnel-inzichten.

Wil je dat ik de heractivatie van de campagne voorbereid?

---

Rapport klaar en gepusht. Hier de kern:

## Auto-Optimize 6 juli 2026 — geen actie vereist

**Er zijn geen actieve Meta Ads campagnes.** Dus geen data, geen kill-regels, geen budget-shifts.

- **act_567892422940728** (primair): alle campagnes PAUSED, waaronder `2026: SYBB` (dagbudget €100,00, laatst gewijzigd 19 april). Ook SYBB Kopie en alle Nozzle Up varianten staan uit.
- **act_1489853856181844**: geen actieve campagnes.
- **act_607231713057715** (het secundaire account in het command): **niet toegankelijk** met dit token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`.

**Gepauzeerd: 0 ads. Waarschuwingen: 0. 70-20-10: n.v.t.**

Twee dingen die jouw aandacht vragen:

1. **SYBB staat op PAUSED.** Zolang dat zo blijft levert dit dagelijkse rapport niks op. Wil je dat ik de campagne weer activeer?
2. **Secundair account-id klopt niet.** Het command wijst naar `act_607231713057715`, maar het token heeft daar geen toegang. Controleer het id of laat me het command bijwerken naar een toegankelijk account, anders missen we eventuele campagnes daar.

Conform de strikte regel: alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Sheet-tracker geschreven. Rapport opgeslagen in `Output/Reports/Daily/2026-07-06_auto_optimize.md` en gepusht naar main.

Wat wil je: SYBB activeren, of het secundaire account-id corrigeren?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
