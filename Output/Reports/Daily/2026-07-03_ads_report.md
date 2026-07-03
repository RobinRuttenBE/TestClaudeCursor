# Meta Ads Rapport: 3 juli 2026

**Account:** Sempertex Ad Account (`act_567892422940728`)
**Periode:** lifetime per campagne (zie kolom periode). Er draaien op dit moment GEEN actieve campagnes, dus `last_30d` levert geen data. Getoond wordt de laatste bekende performance van de meest recente gepauzeerde campagnes.
**Databron:** Meta Ads MCP (Pipeboard). Geen Google Sheet write (overgeslagen per instructie).

> **Let op status:** alle campagnes staan op PAUSED. Het tweede toegankelijke account (AmbitionAvenue, `act_1489853856181844`) heeft geen campagnes en €0 spend. Het in het command genoemde account `act_607231713057715` is niet toegankelijk met dit token (toegestaan: `act_1489853856181844`, `act_567892422940728`).

---

## Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purchases) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------------------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x* |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

\* **Datakwaliteit caveat:** de purchase-waarden uit de pixel zijn opvallend hoog (bijv. SYBB: 6 purchases ter waarde van €44.247, gemiddeld €7.374 per order). Dit wijst mogelijk op een verkeerd geconfigureerde pixel value of dubbeltelling. Behandel ROAS als indicatief, niet als hard cijfer, tot de pixel value config gecontroleerd is.

---

## Underperformers (drempelwaarden)

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) → Aanbeveling: kleine test met weinig data (195 clicks). CPC hoog omdat het volume mist om te optimaliseren. Niet los uitrollen; vouw de winnende creatives terug in de hoofd-SYBB campagne.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel €15) → Aanbeveling: dure reach door smalle/koude targeting op laag budget. Bij heropstart breder publiek of hoger budget zodat het leeralgoritme uit de leerfase komt.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel 1%) → Aanbeveling: net op de grens. De extreem lage CPM (€1,64) en CPC (€0,17) compenseren dit ruim; dit is een awareness/reach setup, geen zwakke engagement. Behouden als top-of-funnel, niet afschieten op CTR alleen.
- **Frequency:** geen enkele campagne boven 3,5 (hoogste is Campagne Nozzle Up 2025 1 met 2,9). Geen creative fatigue risico.

---

## Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** 2026: SYBB — 17,8x (indicatief, zie caveat). Zonder SYBB is Campagne Nozzle Up 2025 1 de beste met 8,3x.

---

## Samenvatting

- **Totaal spend:** €4.867,46 (lifetime, alle campagnes samen; komt exact overeen met account amount_spent)
- **Beste performer: 2026: SYBB.** Hoogste volume (297k impressions, 12k clicks), veruit de beste CTR (4,1%), lage CPC (€0,21) en de sterkste ROAS. Dit is de bewezen winnaar en het logische fundament voor de volgende run.
- **Slechtste performer: Last push Nozzle Up.** ROAS 0,8x (onder break-even): €800,78 spend leverde €623 aan getrackte purchase-waarde. Het was expliciet een "last push" restbudget, dus dat verklaart de zwakke efficiëntie.
- **Aanbeveling (Hormozi 70-20-10):** focus budget op de bewezen winnaar. Herstart **2026: SYBB** als kern (70% budget op de best presterende hooks/creatives daaruit), gebruik 20% voor variaties op die winnende SYBB-angles, en reserveer 10% voor nieuwe experimenten. Rol de "Kopie" niet los uit; die mist volume om te optimaliseren. Controleer eerst de pixel purchase value config voordat ROAS als beslismetric wordt gebruikt.

---

## Google Sheet

Overgeslagen per instructie voor deze run. Rapport lokaal opgeslagen: `Output/Reports/Daily/2026-07-03_ads_report.md`.
