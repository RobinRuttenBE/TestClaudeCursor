Hier is het rapport. Belangrijkste bevinding vooraf: **er draait niets actief** — alle campagnes staan op pauze en er was €0 spend de laatste 30 dagen. Ik toon daarom de laatst bekende lifetime-data.

## Meta Ads Rapport — 24 juni 2026

> Geen actieve campagnes. Account `act_607231713057715` uit de command is niet toegankelijk met deze token; AmbitionAvenue heeft 0 campagnes. Alle 5 spending-campagnes hieronder zitten in het Sempertex Ad Account en zijn samen goed voor 100% van de €4.867,46 lifetime spend.

### Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Purch. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|--------|-------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

\* **ROAS-waarschuwing:** de pixel-purchasewaarden zijn inconsistent (gem. orderwaarde varieert van ~€73 tot ~€7.400). Behandel ROAS als indicatief en valideer tegen de echte webshop-omzet voordat je er budget op baseert. CTR/CPC zijn nu je betrouwbaarste signaal.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34 boven drempel, 0 purchases → niet heractiveren; het origineel verslaat het op elke metric.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (grensgeval), maar spotgoedkope CPM €1,64 → creatives verversen bij heractivatie.
- **Ad-niveau (binnen SYBB):** `SYBB w/ Semp (BLACK)` (CPC €0,61, laagste CTR 1,0%) en de dure dubbele varianten van `H11` (€0,67) en `H13` (€0,63). Geen enkele ad boven frequency 3,5.

### Top performers
- **Beste CTR**: `H13, B3, CTA5` — **9,8%**
- **Laagste CPC**: `H13, B3, CTA5` — **€0,07**
- **Eervolle vermelding**: `H15, B3, CTA5` — CTR 4,3% bij CPC €0,15

### Aanbeveling (Hormozi 70-20-10)
1. **70%** — heractiveer 2026: SYBB en schaal hook **H13** + **H15** (je golden BBs).
2. **20%** — varianten rond H13/H15; pauzeer de dure H11/H13-dubbels.
3. **10%** — één nieuwe hook, niet de "Kopie"-opzet herhalen.
4. Valideer eerst de pixel-omzet tegen de webshop voordat je op ROAS stuurt.

### Google Sheet
Overgeslagen conform de instructie voor deze run. Opgeslagen in `Output/Reports/Daily/2026-06-24_ads_report.md` (gecommit en gepusht).

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er automatisch een `/funnel-diagnose` overheen.
