## Meta Ads Rapport — 29 May 2026

> **Let op:** er draaien op dit moment **geen actieve campagnes** op beide toegankelijke ad accounts (Sempertex Ad Account en AmbitionAvenue). Het account `act_607231713057715` (Robin Rutten) uit de command is niet toegankelijk via deze connectie. Onderstaand rapport toont de **laatste bekende performance (lifetime)** van de meest recente gepauzeerde campagnes op het Sempertex account, conform de regel "geen actieve campagnes → toon recentste gepauzeerde campagnes".

### Accounts gecontroleerd
| Account | ID | Actieve campagnes | Lifetime spend |
|---------|-----|-------------------|----------------|
| Sempertex Ad Account | act_567892422940728 | 0 | €4.867,46 |
| AmbitionAvenue | act_1489853856181844 | 0 | €0,00 |

### Overzicht per campagne (gepauzeerd — lifetime data, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purchase) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

\* Zie waarschuwing onder ROAS hieronder.

Periode: lifetime (2026: SYBB vanaf 13 Jan 2026; Kopie vanaf 19 Apr 2026). Andere gepauzeerde campagnes (Nozzle Up reeks, 2025) niet meegenomen — buiten scope, ouder dan huidige focus.

### Ad-level performance — 2026: SYBB (lifetime)

| Ad | Spend | Impr. | Clicks | CTR | CPC | Freq. |
|----|-------|-------|--------|-----|-----|-------|
| H13,B3,CTA5 | €421,29 | 60.074 | 5.902 | 9,8% | €0,07 | 1,6 |
| H11,B3,CTA5 | €521,56 | 38.614 | 784 | 2,0% | €0,67 | 1,9 |
| H12,B3,CTA5 | €388,40 | 48.166 | 1.248 | 2,6% | €0,31 | 1,8 |
| H14,B3,CTA5 | €232,36 | 33.235 | 911 | 2,7% | €0,26 | 1,5 |
| H15,B3,CTA5 | €218,96 | 34.299 | 1.465 | 4,3% | €0,15 | 1,5 |
| H13,B3,CTA5 (2) | €206,99 | 16.766 | 331 | 2,0% | €0,63 | 1,6 |
| H11,B3,CTA5 (2) | €202,48 | 31.060 | 796 | 2,6% | €0,25 | 1,6 |
| H12,B3,CTA5 (2) | €141,43 | 13.955 | 356 | 2,6% | €0,40 | 1,9 |
| SYBB w/ Semp (BLACK) | €101,74 | 16.268 | 167 | 1,0% | €0,61 | 1,8 |
| H15,B3,CTA5 (2) | €49,83 | 4.737 | 107 | 2,3% | €0,47 | 1,5 |

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel: €0,50) en CPM €16,34 (drempel: €15) → te duur op kleine schaal (€124 spend, 0 purchases). Aanbeveling: niet heractiveren in deze vorm; de hoofdcampagne presteert op elke metric beter.
- **Ad "H11,B3,CTA5" (€521,56)** — CPC €0,67, hoogste spend van alle ads met slechts 784 clicks → grootste budgetlek. Aanbeveling: pauzeren/niet heruploaden.
- **Ad "SYBB w/ Semp (BLACK)"** — CPC €0,61 + CTR 1,0% (grens) → zwakste hook/engagement. Aanbeveling: hook vervangen.
- **Ad "H13,B3,CTA5 (2)"** — CPC €0,63 → duur, terwijl de andere H13-variant juist de absolute topper is. Aanbeveling: budget weg van deze variant.

Geen creative fatigue: alle frequencies < 2,0 (drempel 3,5).

### Top performers

- **Beste CTR**: H13,B3,CTA5 — 9,8% (uitschieter, 5.902 clicks)
- **Laagste CPC**: H13,B3,CTA5 — €0,07
- **Beste campagne-CTR**: 2026: SYBB — 4,1%

### ROAS-waarschuwing

De gerapporteerde purchase-waarde voor 2026: SYBB is €44.247 op 6 purchases (€7.374 per order → ROAS 17,8x). Een gemiddelde orderwaarde van €7.374 is onrealistisch voor de SYBB-funnel; dit wijst vrijwel zeker op een **verkeerd geconfigureerde pixel-waarde** (value misconfiguratie). Behandel de ROAS niet als betrouwbaar tot de pixel value-events gecontroleerd zijn. De volume-metrics (clicks, CTR, CPC, add_to_cart 53, initiate_checkout 36, leads 15) zijn wel betrouwbaar.

### Samenvatting

- **Totaal spend (twee 2026 SYBB-campagnes)**: €2.609,46 — geen spend in de laatste 30 dagen (alles gepauzeerd)
- **Beste performer**: 2026: SYBB — CTR 4,1%, CPC €0,21, ruim onder alle drempelwaarden; geleverd op schaal (297k impressies)
- **Slechtste performer**: 2026: SYBB - Kopie — duurder op elke metric (CPC €0,64, CPM €16,34) en 0 purchases
- **Aanbeveling (Hormozi 70-20-10)**: bij heractivatie, bouw de nieuwe campagne om de bewezen winnaar **H13,B3,CTA5** (9,8% CTR, €0,07 CPC) als 70%-fundament. Gebruik H15,B3,CTA5 (4,3% CTR, €0,15) als de 20%-variatie. Schrap de dure low-CTR ads (H11-variant €521, BLACK). Fix éérst de pixel value-tracking zodat ROAS-beslissingen op echte data rusten.

### Google Sheet
Overgeslagen conform run-instructie (stap 6). Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-05-29_ads_report.md`.
