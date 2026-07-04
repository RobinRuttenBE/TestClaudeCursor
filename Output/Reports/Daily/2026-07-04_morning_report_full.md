# Morning Report — 2026-07-04

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 4 juli 2026

**Er draaien geen actieve campagnes.** Alles op het Sempertex-account staat op PAUSED en de spend over de laatste 30 dagen is €0,00. Ik heb daarom de meest recente gepauzeerde campagnes gerapporteerd met hun **lifetime** data. Het tweede account (`act_607231713057715`) is niet toegankelijk met het huidige API-token.

### Overzicht per campagne (lifetime)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 0,18x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | — |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 (beide boven drempel) → dure test op klein volume, niet in deze vorm heropstarten.
- **Ad H11,B3,CTA5** — CPC €0,67, hoogste spend (€521,56), maar 2,0% CTR → pauzeren.
- **Ad H13,B3,CTA5 (2e set)** — CPC €0,63 → zwakke duplicaat van de winnaar, stopzetten.
- **Ad "SYBB w/ Semp (BLACK)"** — CTR 1,0% + CPC €0,61 → laagste engagement, retireren.
- Geen enkele ad boven de frequency-drempel (3,5) → geen creative fatigue.

### Top performers
- **Beste CTR:** H13,B3,CTA5 — **9,8%** (op 60k impressies, dus solide)
- **Laagste CPC:** H13,B3,CTA5 — **€0,07**
- **Beste campagne:** 2026: SYBB — ruim binnen alle KPI-targets

### Samenvatting
- **Totaal spend:** €2.609,46 lifetime · **laatste 30 dagen €0,00**
- **Beste performer:** hook **H13** — de bewezen winnaar (70%-bucket).
- **Slechtste:** ad H11 + de "- Kopie" campagne.
- **Kernbevinding:** de ads presteerden gezond op traffic (CTR/CPC/CPM binnen target), maar de funnel converteerde slecht: **6 aankopen op 297k impressies**. Het knelpunt zit ná de klik (landing page → checkout), niet in de ads.

**Aanbeveling (70-20-10):** herstart met H13 als kern-hook, zet de zwakke duplicaten uit, en fix eerst de landing page-conversie voordat je opschaalt — bij 12.067 clicks en 6 aankopen zit de winst in de funnel, niet in meer ad-spend.

⚠️ **Databetrouwbaarheid:** de pixel purchase-value is onbetrouwbaar geconfigureerd (tegenstrijdige bedragen per event), dus ROAS 0,18x is indicatief. Valideer de pixel-tracking voor je op ROAS stuurt.

Rapport opgeslagen: `Output/Reports/Daily/2026-07-04_ads_report.md` (Google Sheet-write overgeslagen zoals gevraagd).

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` en voeg de volledige funnel-analyse toe aan dit rapport.

---

Rapport gegenereerd en opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-07-03_sybb_report.md`

**Belangrijkste bevindingen — twee dingen die je moet weten:**

1. **De campagne `2026: SYBB` staat op PAUSED.** Via de Meta Ads MCP zag ik: €0 spend, 0 impressies, 0 clicks — zowel gisteren (3 juli) als de hele afgelopen 7 dagen. De laatste keer dat de campagne écht draaide was **april 2026** (€1.059 spend, CPC €0,55, 6 purchases). Er valt dus niets aan live performance te optimaliseren; de echte vraag is of je SYBB weer aanzet.

2. **De PostHog MCP was deze sessie niet verbonden.** Ik heb er meerdere keren op gezocht, maar de server heeft geen tools beschikbaar gemaakt. Daardoor is er geen landing page data (bounce rate, scroll depth, CTA clicks). Ik heb dit als open gemarkeerd in plaats van cijfers te verzinnen.

Ik heb me strikt aan de regels gehouden: alleen Meta Ads MCP geraadpleegd, **geen** Google-tools, en het rapport is puur lokaal weggeschreven (niets naar de Google Sheet tracker).

**Top acties in het rapport:** (1) beslissen of SYBB heractiveert — strategiebeslissing voor jou; (2) PostHog connector herstellen via `/mcp` in een interactieve sessie; (3) landing page tracking verifiëren vóór een eventuele herstart.

Wil je dat ik uitzoek wanneer/waarom de campagne in april is gepauzeerd, of help met het klaarzetten voor een herstart?

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-04_auto_optimize.md` en gecommit/gepusht.

## Samenvatting

**Er zijn geen actieve campagnes om te optimaliseren.** De auto-optimize kon dus geen kill-regels of voorstellen toepassen.

**Wat ik vond (alleen Meta Ads MCP / Pipeboard gebruikt, geen Google MCPs):**

| Account | Resultaat |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allen PAUSED** — 0 actief |
| `act_1489853856181844` (toegestaan) | 0 actieve campagnes |
| `act_607231713057715` (in command) | **Geen token-toegang** |

De kerncampagne **`2026: SYBB` staat op PAUSED** (net als de Kopie en alle Nozzle Up-campagnes). Zolang die niet ACTIVE is, is er geen live performance data voor `/ads-auto-optimize`, `/ads-report` of het SYBB daily report.

**Twee dingen om te beslissen:**
1. Wil je `2026: SYBB` (opnieuw) activeren? Dan kan ik de optimalisatie morgen tegen echte data draaien.
2. Account `act_607231713057715` is niet bereikbaar met de huidige Pipeboard-token (alleen de twee bovenstaande accounts zijn toegestaan). Als die account meetelt, moet de toegang in Pipeboard worden uitgebreid.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
