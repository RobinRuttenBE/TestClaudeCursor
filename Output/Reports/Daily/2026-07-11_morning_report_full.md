# Morning Report — 2026-07-11

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 11 juli 2026

> **Let op:** Er zijn momenteel **geen actieve campagnes**. Het Sempertex Ad Account (`act_567892422940728`) heeft geen ACTIVE campagnes; het tweede account uit het commando (`act_607231713057715`) is niet toegankelijk met dit token; het extra toegankelijke account (`act_1489853856181844`) is ook leeg. Hieronder daarom de **5 meest recente gepauzeerde campagnes** met **lifetime** performance.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | — |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) én CPM €16,34 (drempel €15) → testkopie met 0 aankopen. Niet heractiveren; test winnende creatives liever binnen de hoofdcampagne.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (op de grens) → pure reach-campagne (CPM €1,64), sterk voor awareness maar zwak voor conversie-engagement.
- Frequency-drempel (>3,5) door niemand overschreden (hoogste 2,9).

### Top performers
- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — 17,8x

### Samenvatting
- **Totaal spend**: €4.867,46 (lifetime, 5 campagnes)
- **Beste performer**: **2026: SYBB** — hoogste CTR, laagste CPC op schaal, €44.247 omzet op €2.485 spend (ROAS 17,8x). Bewezen winnaar.
- **Slechtste performer**: **Last push Nozzle Up** — ROAS 0,8x, verlieslatend; koopintentie was uitgeput tegen einde van de Nozzle Up-cyclus.
- **Aanbeveling (70-20-10)**: focus 70% budget op heractiveren/opschalen van **2026: SYBB** (daily budget stond op €100), 20% op variaties van de werkende SYBB-hooks, 10% op experimenten. Kopie- en Last push-varianten links laten liggen.

### Google Sheet
Overgeslagen op verzoek (geen Google MCP). Rapport opgeslagen: `Output/Reports/Daily/2026-07-11_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking) en voeg die toe aan het rapport.

---

Rapport gegenereerd en opgeslagen: `Output/Reports/Daily/2026-07-10_sybb_report.md`.

## Samenvatting van de run

**Meta Ads (Pipeboard MCP) — opgehaald ✅**
- Campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED**.
- **10 juli: nul spend, nul impressies, nul clicks.** Ook de hele week 3–9 juli geen delivery, en accountniveau geen spend in de laatste 14 dagen. Geen dag-op-dag of variant-analyse mogelijk.
- Lifetime-context als referentie: €2.485 spend, 297K impressies, CTR 4,06%, CPC €0,21, 15 leads, 6 purchases (€44.247). De creatives presteren historisch sterk — het probleem is puur dat de campagne uit staat.

**PostHog — NIET opgehaald ⚠️**
- De PostHog MCP-connector verbond niet tijdens deze run; er kwamen geen `mcp__posthog__*` tools beschikbaar. Landing page health, bounce rate en scroll depth konden dus niet worden opgehaald. Dit is de **tweede dag op rij** dat dit misgaat.

**Belangrijkste bevinding:** de SYBB-campagne draait niet — twee dagen op rij nul acquisitie. Actie #1 is een bewuste keuze: heractiveren of gepauzeerd laten (jouw goedkeuring nodig, budget €100/dag staat klaar).

Ik heb me strikt aan de regel gehouden: **alleen Meta Ads MCP** geraadpleegd, geen Google MCPs, en niet naar de Google Sheet tracker geschreven. Output uitsluitend lokaal opgeslagen.

Wil je dat ik de campagne heractiveer (via de Meta Ads MCP), of laten we hem bewust op pauze staan?

---

## Auto-Optimize Rapport — 11 July 2026

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-11_auto_optimize.md` (gecommit en gepusht).

**Belangrijkste bevinding: er zijn geen actieve Meta Ads campagnes, dus er is niets te optimaliseren.**

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (primair) | ✅ Toegang | 0 actieve campagnes — alle 5 op PAUSED |
| `act_1489853856181844` | ✅ Toegang | 0 actieve campagnes |
| `act_607231713057715` | ❌ Geen toegang | Token heeft geen rechten op dit account |

Concreet:
- **⚡ Automatische acties:** 0 ads gepauzeerd (geen actieve ads om tegen de kill-regels te toetsen).
- **⚠️ Waarschuwingen:** geen.
- **📊 70-20-10 / 💡 Voorstellen:** niet van toepassing zonder actieve ads.

Twee dingen om te weten:
1. De hoofdcampagne **"2026: SYBB" staat sinds 19 Apr 2026 op PAUSED** (net als de kopie). Als die weer moet lopen, moet je 'm handmatig activeren — daarna kan dit command pas echte optimalisaties doen.
2. Het command noemt `act_607231713057715`, maar de huidige Pipeboard-token heeft **geen toegang** tot dat account. Als je daar wél campagnes verwacht, moet de Pipeboard-connectie/permissies gecheckt worden — anders blijft dat account onzichtbaar voor dit rapport.

Ik heb me strikt aan de regel gehouden: alleen de Meta Ads MCP gebruikt, geen Google MCPs, en niets naar de Google Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
