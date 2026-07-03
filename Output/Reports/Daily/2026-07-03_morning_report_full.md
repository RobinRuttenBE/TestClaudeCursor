# Morning Report — 2026-07-03

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport: 3 juli 2026

⚠️ **Er draaien op dit moment GEEN actieve campagnes.** Alle campagnes staan op PAUSED. Hieronder de laatste bekende performance van de meest recente gepauzeerde campagnes (lifetime data, want `last_30d` is leeg). Het account `act_607231713057715` uit het command is niet toegankelijk met dit token; AmbitionAvenue heeft €0 spend.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x* |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

\* **Datakwaliteit caveat:** de pixel purchase-waarden zijn onrealistisch hoog (SYBB: 6 purchases = €44.247, ofwel €7.374 per order). Waarschijnlijk een fout in de pixel value config. Behandel ROAS als indicatief.

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15) → te weinig volume (195 clicks) om te optimaliseren. Niet los uitrollen; winnende creatives terugvouwen in hoofd-SYBB.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (net op grens) → maar met CPM €1,64 en CPC €0,17 is dit een efficiënte reach/awareness setup, geen zwakke engagement. Behouden als top-of-funnel.
- **Frequency:** geen enkele campagne boven 3,5. Geen creative fatigue risico.

### Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** 2026: SYBB — 17,8x (indicatief). Zonder SYBB: Campagne Nozzle Up 2025 1 met 8,3x.

### Samenvatting

- **Totaal spend:** €4.867,46 (lifetime, alle campagnes samen)
- **Beste performer:** 2026: SYBB — hoogste volume, beste CTR (4,1%), lage CPC, sterkste ROAS. De bewezen winnaar.
- **Slechtste performer:** Last push Nozzle Up — ROAS 0,8x (onder break-even), maar het was bewust restbudget.
- **Aanbeveling (70-20-10):** herstart **2026: SYBB** als kern (70% op de best presterende hooks), 20% op variaties van die winnende angles, 10% op nieuwe experimenten. Controleer eerst de pixel purchase value config voordat je op ROAS stuurt.

📄 Opgeslagen in `Output/Reports/Daily/2026-07-03_ads_report.md` (gecommit en gepusht). Google Sheet write overgeslagen per instructie.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4. Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` erbovenop.

Zal ik daarnaast de PostHog landing page data van startyourballoonbusiness.com ophalen om de funnel-kant af te maken?

---

Klaar. Rapport staat op `Output/Reports/Daily/2026-07-02_sybb_report.md` en is gecommit + gepusht.

## Samenvatting van deze run

Twee harde bevindingen bepaalden het rapport:

**1. Meta Ads — campagne staat op pauze.** De campagne `2026: SYBB` (ID `120239435987290239`, account `act_567892422940728`) heeft status **PAUSED** en gaf voor 2 juli én de hele week 26 jun–2 jul lege data terug. Nul spend, impressies, clicks. De funnel krijgt dus geen instroom. (Er bestaat ook een duplicaat `2026: SYBB - Kopie`, eveneens paused — niet gebruikt.)

**2. PostHog MCP was niet beschikbaar.** De server stond op "connecting" maar er zijn ondanks meerdere zoekacties geen PostHog-tools beschikbaar gekomen. Landing page data (bounce, scroll, CTA, sessies) kon ik niet ophalen. Secties 3 en 4 zijn daarom leeg gemarkeerd (⚪).

Ik heb me strikt aan je regel gehouden: alleen Meta Ads MCP en PostHog MCP geraadpleegd, geen Google-diensten, en niets naar de Google Sheet tracker geschreven.

**De 3 acties die er nu toe doen:**
1. Beslis of `2026: SYBB` weer aan moet (sinds april op pauze) — zonder dit blijft de funnel leeg.
2. Herstel de PostHog MCP-koppeling (via `/mcp` in een interactieve sessie of `claude mcp`) zodat landing page monitoring terugkomt.
3. Plan een scherpe 48u-check voor het moment dat de campagne weer live gaat.

Wil je dat ik help met het opnieuw activeren van de campagne, of eerst de PostHog-koppeling nakijken?

---

Klaar. Rapport opgeslagen, gecommit en gepusht.

## Resultaat auto-optimize — 3 juli 2026

**Geen actieve campagnes → geen optimalisatie mogelijk of nodig.** Alle campagnes staan op PAUSED, dus er zijn geen ads om tegen de kill-regels of de 70-20-10 classificatie te toetsen. Geen automatische acties uitgevoerd, geen voorstellen.

**Account-scan (alleen Meta Ads MCP gebruikt, geen Google MCPs):**

| Account | Bevinding |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED** (2× SYBB, 3× Nozzle Up) |
| `act_1489853856181844` | 0 campagnes |
| `act_607231713057715` | **Geen toegang** met deze token |

⚠️ **Twee aandachtspunten:**
1. Het account `act_607231713057715` uit het command is niet bereikbaar met de huidige Pipeboard-token (toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`). Als dit account meegenomen moet worden, moet de tokenkoppeling in Pipeboard uitgebreid worden.
2. Zodra `2026: SYBB` weer live gaat, draai dit command opnieuw na minimaal 24 uur delivery — dan pas kunnen de kill-regels en classificatie op échte link-metrics draaien.

Rapport staat in `Output/Reports/Daily/2026-07-03_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
