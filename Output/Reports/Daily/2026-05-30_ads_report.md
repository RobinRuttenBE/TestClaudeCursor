# Meta Ads Rapport — 30 May 2026

**Bron:** Pipeboard Meta Ads MCP (alleen). Geen Google MCPs gebruikt, niet naar Google Sheet geschreven.
**Periode opvraag:** last_30d (zie waarschuwing hieronder).

## Belangrijke bevindingen vooraf

1. **Geen actieve campagnes.** Alle 5 campagnes in het Sempertex Ad Account (`act_567892422940728`) staan op PAUSED. De `ACTIVE` filter gaf 0 resultaten.
2. **last_30d is overal leeg** (campagne- en ad-niveau): er heeft de afgelopen 30 dagen niets gedraaid. Dit is een echte lege uitkomst, geen fout. Daarom toont dit rapport de **lifetime performance** van de gepauzeerde campagnes (conform regel: bij geen actieve campagnes de meest recente gepauzeerde campagnes met laatste data tonen).
3. **`act_607231713057715` (Robin Rutten) is niet toegankelijk** met dit token. Toegestaan zijn alleen `act_1489853856181844` (AmbitionAvenue, €0,00 lifetime, geen campagnes) en `act_567892422940728` (Sempertex). Voor het Robin Rutten account kon dus geen data worden opgehaald.

## Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purchase) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Nozzle Up END OF AUGUST | PAUSED | €1.142,93 | 126.582 | 3.654 | 2,9% | €0,31 | €9,03 | 19 | 7,8x |
| Last push Nozzle Up | PAUSED | €627,18 | 58.241 | 2.103 | 3,6% | €0,30 | €10,77 | 8 | 5,9x |
| Campagne Nozzle Up 2025 1 | PAUSED | €611,31 | ~58.000 | 1.547 | n.b. | n.b. | n.b. | n.b. | n.b. |
| 2026: SYBB - Kopie | PAUSED | €0,00 | 0 | 0 | n.b. | n.b. | n.b. | 0 | n.b. |

\* De purchase-waarde van "2026: SYBB" (€44.247 op 6 aankopen) oogt opgeblazen of bevat testdata. Behandel de 17,8x ROAS met voorzichtigheid; de Nozzle Up ROAS-cijfers (5,9x en 7,8x) zijn realistischer.

n.b. = niet beschikbaar in API-respons (deels door paused status, deels onvolledige data voor "Campagne Nozzle Up 2025 1").

## Underperformers (drempelwaarden)

Getoetst op CPC > €0,50, CTR < 1%, Frequency > 3,5, CPM > €15.

- **Geen enkele campagne overschrijdt een drempel.** Alle CPC's liggen tussen €0,21 en €0,31 (ruim onder €0,50), alle CTR's boven 2,8% (ruim boven 1%), CPM's tussen €8,36 en €10,77 (onder €15), en geen frequency boven 3,5.
- **Wel let op:** de "2026: SYBB - Kopie" heeft nul spend/levering, en "Campagne Nozzle Up 2025 1" levert onvolledige conversiedata. Geen actiepunt qua kosten, wel qua opschoning.

## Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** 2026: SYBB — €0,21
- **Beste (betrouwbare) ROAS:** Nozzle Up END OF AUGUST — 7,8x
- **Meeste aankopen:** Nozzle Up END OF AUGUST — 19 purchases (€8.930,25 waarde)

## Samenvatting

- **Totaal spend (lifetime, alle campagnes):** €4.866,46 (komt overeen met account amount_spent €4.867,46).
- **Totaal spend last 30 days:** €0,00 (alles gepauzeerd).
- **Beste performer:** "2026: SYBB" op engagement (CTR 4,1%, CPC €0,21, 297k impressions, 12k clicks) — sterkste top-of-funnel cijfers van alle campagnes.
- **Beste verkoop-performer:** "Nozzle Up END OF AUGUST" — meeste aankopen (19) en gezonde 7,8x ROAS.
- **Slechtste performer:** "2026: SYBB - Kopie" — nul levering, draait niet.
- **Aanbeveling (Hormozi 70-20-10):** focus budget op de bewezen winnaar "2026: SYBB" zodra je heractiveert (laagste CPC, hoogste CTR = goedkoopste verkeer). Behandel de SYBB-hooks als je 70% bewezen basis. Schoon "2026: SYBB - Kopie" op of zet hem live met een duidelijke variant-hypothese (20% variaties). Verifieer eerst de SYBB purchase-tracking, want de €44k purchase-waarde lijkt vervuild en maakt ROAS-sturing onbetrouwbaar.

## Google Sheet

Overgeslagen (stap 6) conform instructie voor deze run. Rapport uitsluitend lokaal opgeslagen: `Output/Reports/Daily/2026-05-30_ads_report.md`.
