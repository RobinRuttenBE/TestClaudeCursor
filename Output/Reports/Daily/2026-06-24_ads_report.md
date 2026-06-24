## Meta Ads Rapport — 24 juni 2026

> **Belangrijk:** Er zijn op dit moment **geen actieve campagnes**. Alle campagnes in het Sempertex Ad Account staan op PAUSED en er is **0 spend in de laatste 30 dagen**. Onderstaand rapport toont daarom de **lifetime performance** van de meest recente gepauzeerde campagnes (laatste bekende data), gesorteerd op spend.
>
> Het tweede account uit de command (`act_607231713057715`) is **niet toegankelijk** met de huidige API-token. Het andere wel-toegankelijke account (AmbitionAvenue, `act_1489853856181844`) heeft **0 campagnes en 0 spend**.

### Overzicht per campagne (lifetime, want geen activiteit laatste 30d)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purch) | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

\* **ROAS-waarschuwing:** de purchase-waarden uit de Meta-pixel zijn inconsistent tussen campagnes (gemiddelde orderwaarde varieert van ~€73 tot ~€7.400 per order). Behandel ROAS als indicatief, niet als hard. Valideer tegen de werkelijke omzet in Wix/de webshop voordat je hierop budget baseert.

### Underperformers

**Op campagneniveau:**
- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) én CPM €16,34 (drempel €15) → Aanbeveling: dit is een mini-test (€124 spend, 0 purchases). Niet heractiveren in deze vorm; het origineel "2026: SYBB" presteert op elke metric beter.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel 1%, grensgeval) → Aanbeveling: zeer lage CPM (€1,64) compenseert; reach-campagne deed z'n werk. Bij heractivatie creatives verversen voor hogere CTR.

**Op ad-niveau (binnen 2026: SYBB):**
- **SYBB w/ Semp (BLACK)** — CPC €0,61 + laagste CTR (1,03%) van de set → Aanbeveling: zwakste creative, niet opnieuw inzetten.
- **H11, B3, CTA5** (variant, €521 spend) — CPC €0,67 + CPM €13,51 → Aanbeveling: dure variant; vervang door de goedkopere H11-versie (CPC €0,25).
- **H13, B3, CTA5** (variant, €207 spend) — CPC €0,63 → Aanbeveling: let op, een andere H13-variant is juist de topper (zie hieronder). Hook werkt; deze specifieke creative-versie niet.

Geen enkele ad overschrijdt de frequency-drempel (3,5); hoogste was 2,89 (Nozzle Up 2025 1).

### Top performers

- **Beste CTR**: `H13, B3, CTA5` (2026: SYBB) — **9,8%** (5.902 clicks op 60.074 impressies)
- **Laagste CPC**: `H13, B3, CTA5` (2026: SYBB) — **€0,07**
- **Beste ROAS**: 2026: SYBB — 17,8x (zie ROAS-waarschuwing hierboven)
- **Eervolle vermelding**: `H15, B3, CTA5` — CTR 4,3% bij CPC €0,15, sterke allround winner

### Samenvatting

- **Totaal spend**: €4.867,46 (lifetime, alle campagnes samen = 100% van het account; geen spend laatste 30 dagen)
- **Totaal purchases**: 21 | **Totaal leads**: 15 (allemaal uit 2026: SYBB)
- **Beste performer**: **2026: SYBB** — verreweg de hoogste CTR (4,1%), laagste blended CPC (€0,21) en de enige campagne die ook leads genereerde. Hook **H13** is de duidelijke winnaar (CTR 9,8%, CPC €0,07).
- **Slechtste performer**: **2026: SYBB - Kopie** — €124 spend, 0 purchases, duurste CPC (€0,64) en CPM (€16,34). Een test die niet aansloeg.
- **Aanbeveling (Hormozi 70-20-10):**
  1. **70% — Schaal de bewezen winnaar.** Heractiveer 2026: SYBB en zet budget achter hook **H13** en **H15** (laagste CPC, hoogste CTR). Dit zijn je golden BBs.
  2. **20% — Varieer rond de winnaar.** Maak nieuwe varianten van H13/H15 met B3+CTA5. Pauzeer de dure dubbele varianten van H11/H13 die €0,63–0,67 CPC draaien.
  3. **10% — Experiment.** Eén nieuwe hook tegen de SYBB-doelgroep; niet de "Kopie"-opzet herhalen.
  4. **Tracking eerst:** valideer de pixel purchase-waarden tegen werkelijke webshop-omzet voordat je op ROAS stuurt. Nu is CTR/CPC de betrouwbaarste signaal.

### Google Sheet
Overgeslagen — conform de instructie voor deze run is er **niet** naar de Meta Ads Tracker Google Sheet geschreven. Rapport opgeslagen in `Output/Reports/Daily/2026-06-24_ads_report.md`.
