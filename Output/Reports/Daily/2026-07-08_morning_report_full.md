# Morning Report — 2026-07-08

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-08_ads_report.md` (gecommit + gepusht). Alleen Meta Ads MCP gebruikt, geen Google MCPs.

## Meta Ads Rapport — 8 juli 2026

> **Geen actieve campagnes.** Het Sempertex Ad Account (`act_567892422940728`) heeft niets live staan en 0 data in de laatste 30 dagen. Hieronder de laatste **gepauzeerde** campagnes op **lifetime** basis. Het tweede account uit de commandoreferentie (`act_607231713057715`) bestaat niet meer; het beschikbare tweede account is **AmbitionAvenue** (€0 spend, geen campagnes).

### Overzicht per campagne (lifetime, gepauzeerd)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 0,18x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

**Totaal spend:** €2.609,46. De hoofdcampagne is feitelijk een **lead-/traffic-funnel** (15 leads, 6.992 landing page views), dus beoordeel op CPC/CTR, niet op ROAS.

### Underperformers
- **"2026: SYBB - Kopie"** — CPC €0,64 én CPM €16,34 (beide boven drempel), geen conversies. Kleine test die niet aansloeg → niet heractiveren.
- **Ad "H11,B3,CTA5" (set 2, €521,56)** — CPC €0,67, hoogste spend maar dure clicks → pauzeren.
- **Ad "H13,B3,CTA5" (set 2)** — CPC €0,63 tegenover €0,07 voor de winnende variant → budget verschuiven.
- **Ad "SYBB w/ Semp (BLACK)"** — CPC €0,61 + CTR 1,0% → uitfaseren.

Geen enkele ad boven de frequency-drempel (3,5), dus geen creative fatigue.

### Top performers
- **Beste CTR:** H13,B3,CTA5 — **9,8%**
- **Laagste CPC:** H13,B3,CTA5 — **€0,07**
- **Beste ROAS:** n.v.t. (geen betrouwbare purchase-tracking)

### Aanbeveling (70-20-10)
Er staat niets live. Bij heractivatie: **70%** budget op de bewezen winnaar **H13,B3,CTA5** (+ sterke H15 @ €0,15 CPC / 4,3% CTR), **20%** op varianten in dezelfde B3/CTA5-structuur, **10%** experimenten. Pauzeer de dure duplicaten definitief — ze leveren clicks 3-9x duurder dan de winnaars.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met die cijfers draai ik automatisch een `/funnel-diagnose` en voeg ik de volledige funnel-analyse (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking) toe aan het rapport.

---

Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-07_sybb_report.md` (gecommit en gepusht).

## Belangrijkste bevindingen

**Er is geen SYBB-activiteit om te rapporteren voor 7 juli 2026:**

1. **Meta Ads — campagne staat PAUSED.** De campagne `2026: SYBB` (account `act_567892422940728`) draaide **nul spend, impressies en clicks** op 7 juli, en ook de hele week 1–7 juli. Ze staat op pauze sinds ~19 april 2026. Meta gaf voor gisteren een lege dataset terug.

2. **PostHog MCP was niet beschikbaar.** De `posthog`-server stond op "connecting" maar heeft geen tools blootgesteld. Vijf gerichte ToolSearch-pogingen leverden niets op, dus landing page-data (bounce, scroll depth, CTA clicks) kon **niet** opgehaald worden.

Ik heb geen cijfers verzonnen — het rapport markeert beide bronnen eerlijk (Meta = 0 door pauze, PostHog = geen data) en volgt de SKILL-structuur.

## Twee dingen die je aandacht vragen

- 🚩 **Is de pauze van "2026: SYBB" bewust?** Zo niet, dan loopt er sinds april geen lead-flow via deze campagne. Dit is een strategische beslissing (Rood) — ik heb budget/status bewust niet aangepast.
- 🚩 **PostHog MCP herverbinden.** Zolang die niet verbindt, mist dit dagrapport de landing page- en cross-reference-analyse. Opnieuw verbinden kan via `/mcp` in een interactieve sessie of je connector-instellingen.

Conform je striktregel zijn alleen de Meta Ads MCP en (poging tot) PostHog MCP gebruikt — geen Google-services, niet naar de Google Sheet-tracker geschreven.

---

## Auto-Optimize Rapport, 8 juli 2026

**Er is niets om te optimaliseren: geen enkele actieve campagne.** Alle campagnes staan op PAUSED.

### ⚡ Automatische acties uitgevoerd
Geen ads gepauzeerd. Er zijn geen actieve ads, dus de kill-regels (Link CTR < 0,8% of CPC (link) > €1,50) waren niet van toepassing.

### 📊 Accountstatus

| Account | Bevinding |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED**, inclusief `2026: SYBB` (€100,00/dag) |
| `act_1489853856181844` | Leeg |
| `act_607231713057715` (secundair uit command) | **Niet toegankelijk** met deze token |

### ⚠️ Twee aandachtspunten voor jou

1. **De SYBB-campagne staat uit.** `2026: SYBB` is sinds 19 april 2026 gepauzeerd. Zolang die op PAUSED staat is er geen live data, en kan noch deze optimizer noch het dagelijkse SYBB-rapport iets meten. Zet hem op ACTIVE als hij weer moet lopen, dan pakt de volgende run wel op.
2. **Tweede account niet bereikbaar.** Het command noemt `act_607231713057715`, maar de token heeft daar geen toegang (toegestaan: `act_1489853856181844` en `act_567892422940728`). Controleer het account-ID of de token-permissies.

Rapport opgeslagen in `Output/Reports/Daily/2026-07-08_auto_optimize.md` en gecommit + gepusht naar GitHub. Alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Google Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
