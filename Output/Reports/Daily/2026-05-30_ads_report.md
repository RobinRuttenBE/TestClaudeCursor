Rapport klaar en opgeslagen in `Output/Reports/Daily/2026-05-30_ads_report.md` (lokaal, geen Google Sheet write zoals gevraagd).

## Meta Ads Rapport — 30 May 2026

**Twee zaken vooraf:**
1. **Geen actieve campagnes.** Alle 5 campagnes in het Sempertex account staan op PAUSED, en `last_30d` is daardoor overal leeg. Ik toon hieronder de **lifetime** cijfers van de gepauzeerde campagnes.
2. **`act_607231713057715` (Robin Rutten) is niet toegankelijk** met dit token. Alleen AmbitionAvenue (€0, geen campagnes) en het Sempertex account waren bereikbaar.

### Overzicht per campagne (lifetime, op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | PAUSED | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.b. |

\* SYBB purchase-waarde €44.247 op 6 aankopen (gem. €7.374/order) is vrijwel zeker testdata/vervuild. Behandel die 17,8x als onbetrouwbaar. **Totaal spend: €4.867,46** (klopt exact met het account amount_spent).

### Underperformers
- **2026: SYBB - Kopie** → CPC €0,64 (>€0,50) én CPM €16,34 (>€15), 0 aankopen. Niet zo heractiveren; herzien of archiveren.
- **Nozzle Up END OF AUGUST** → CTR 1,0% (net op de 1%-grens), maar compenseert met CPC €0,17 en CPM €1,64. Geen actie nodig.
- **Last push Nozzle Up** → geen drempeloverschrijding, maar ROAS 0,8x (onder break-even). Niet herhalen zonder aanpassing.
- Geen frequency-issue (max 2,89).

### Top performers
- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1 — 8,3x

### Aanbeveling (70-20-10)
Bij heractivatie: 70% bewezen budget op de Nozzle Up winnaar (Campagne 2025 1, 8,3x) en op "2026: SYBB" voor goedkoop top-of-funnel verkeer. "SYBB - Kopie" alleen als bewuste variatie (20%), niet als kopie. **Fix eerst de SYBB purchase-tracking** — die €44k waarde maakt ROAS-sturing op die campagne blind.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er automatisch een `/funnel-diagnose` op (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking).
