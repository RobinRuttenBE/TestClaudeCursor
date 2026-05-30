# Meta Ads Rapport — 30 May 2026

**Bron:** Pipeboard Meta Ads MCP (alleen). Geen Google MCPs gebruikt, niet naar Google Sheet geschreven.
**Periode opvraag:** last_30d (zie waarschuwing hieronder). Alle cijfers in de tabel zijn lifetime (zie punt 2).

## Belangrijke bevindingen vooraf

1. **Geen actieve campagnes.** Alle 5 campagnes in het Sempertex Ad Account (`act_567892422940728`) staan op PAUSED. De `ACTIVE` filter gaf 0 resultaten.
2. **last_30d is overal leeg** (campagne- en ad-niveau): er heeft de afgelopen 30 dagen niets gedraaid. Echte lege uitkomst, geen fout. Daarom toont dit rapport de **lifetime performance** van de gepauzeerde campagnes (conform regel: bij geen actieve campagnes de meest recente gepauzeerde campagnes met laatste data tonen).
3. **`act_607231713057715` (Robin Rutten) is niet toegankelijk** met dit token. Toegestaan zijn alleen `act_1489853856181844` (AmbitionAvenue, €0,00 lifetime, geen campagnes) en `act_567892422940728` (Sempertex). Voor het Robin Rutten account kon dus geen data worden opgehaald.

## Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | PAUSED | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.b. |

\* De purchase-waarde van "2026: SYBB" (€44.247 op slechts 6 aankopen, gem. €7.374 per order) is vrijwel zeker opgeblazen of testdata. Behandel de 17,8x ROAS als onbetrouwbaar. De Nozzle Up ROAS-cijfers zijn realistischer.

**Totaal spend (5 campagnes, lifetime): €4.867,46** — komt exact overeen met het account amount_spent (€4.867,46).

## Underperformers (drempelwaarden)

Getoetst op CPC > €0,50, CTR < 1%, Frequency > 3,5, CPM > €15.

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) én CPM €16,34 (drempel €15) → te duur op zowel klik als reach, met 0 aankopen. Aanbeveling: niet heractiveren zoals hij is; herzie targeting/creative of archiveer.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel 1%, net op de grens) → relatief lage engagement, maar compenseert met extreem lage CPC (€0,17) en CPM (€1,64). Aanbeveling: prima reach-campagne, geen actie nodig.
- **Last push Nozzle Up** — geen drempeloverschrijding, maar ROAS 0,8x ligt onder break-even (€800,78 spend → €623 omzet). Aanbeveling: deze hook/aanbieding niet opnieuw inzetten zonder aanpassing.
- Geen enkele campagne heeft een frequency boven 3,5 (max 2,89).

## Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste (betrouwbare) ROAS:** Campagne Nozzle Up 2025 1 — 8,3x
- **Meeste aankopen:** gedeeld op 6 (2026: SYBB, Campagne Nozzle Up 2025 1, Nozzle Up END OF AUGUST)

## Samenvatting

- **Totaal spend last 30 days:** €0,00 (alles gepauzeerd).
- **Beste performer:** "Campagne Nozzle Up 2025 1" — beste betrouwbare ROAS (8,3x), 6 aankopen op €853 spend, gezonde CPC (€0,26) en CTR (2,5%).
- **Slechtste performer:** "Last push Nozzle Up" — ROAS 0,8x, onder break-even. "2026: SYBB - Kopie" is qua kosten het duurst (CPC €0,64, CPM €16,34) en leverde geen aankopen.
- **Aanbeveling (Hormozi 70-20-10):** zet bij heractivatie je 70% bewezen budget op de Nozzle Up winnaars (Campagne Nozzle Up 2025 1 als anker, 8,3x ROAS) en op "2026: SYBB" voor top-of-funnel verkeer (laagste-cost engagement, sterkste CTR 4,1%, CPC €0,21). Gebruik "2026: SYBB - Kopie" alleen als bewuste 20%-variatie met een nieuwe hypothese, niet als kopie. **Eerst de SYBB purchase-tracking fixen**, want de €44k purchase-waarde vervuilt elke ROAS-vergelijking en maakt budgetsturing op die campagne blind.

## Google Sheet

Overgeslagen (stap 6) conform instructie voor deze run. Rapport uitsluitend lokaal opgeslagen: `Output/Reports/Daily/2026-05-30_ads_report.md`.
