# Auto-Optimize Rapport — 2026-05-26

## Samenvatting

**Geen actieve campagnes in Meta Ads.** Auto-optimize kan niet draaien omdat er geen ads zijn om te evalueren tegen de kill-regels of te classificeren volgens 70-20-10.

## Account scan

| Account | Toegang | Actieve campagnes | Totaal campagnes (alle statussen) |
|---------|---------|-------------------|-----------------------------------|
| `act_567892422940728` (Sempertex primair) | Ja | 0 | 5 (allemaal PAUSED) |
| `act_1489853856181844` | Ja | 0 | 0 |
| `act_607231713057715` | Geen toegang | n.v.t. | n.v.t. |

> Account `act_607231713057715` staat vermeld in het command maar de API-token heeft hier geen toegang toe. Allowed accounts volgens Pipeboard: `act_1489853856181844`, `act_567892422940728`.

## Gepauzeerde campagnes op `act_567892422940728`

| Campagne ID | Naam | Objective | Laatste update | Daily budget |
|-------------|------|-----------|----------------|--------------|
| 120243293329420239 | 2026: SYBB - Kopie | OUTCOME_SALES | 2026-04-20 | n.v.t. |
| 120239435987290239 | 2026: SYBB | OUTCOME_SALES | 2026-04-19 | €100.00 |
| 120233295855990239 | Last push Nozzle Up | OUTCOME_SALES | 2025-09-21 | n.v.t. |
| 120232324822740239 | Nozzle Up END OF AUGUST | OUTCOME_SALES | 2025-09-15 | €70.00 |
| 120230372047970239 | Campagne Nozzle Up 2025 1 | OUTCOME_SALES | 2025-09-15 | €30.00 |

De laatste actieve campagne (2026: SYBB) is op 2026-04-19 gepauzeerd. Er is sindsdien (37 dagen geleden) geen ad-activiteit op het account.

## ⚡ Automatische acties uitgevoerd

**0 ads gepauzeerd** — er waren geen actieve ads om tegen de kill-regels te evalueren.

| Regel | Drempel | Triggers |
|-------|---------|----------|
| Lage Link CTR | < 0.8% bij ≥ 1.000 impressions | n.v.t. (geen actieve ads) |
| Hoge CPC (link) | > €1.50 bij ≥ 500 link clicks | n.v.t. (geen actieve ads) |

## ⚠️ Waarschuwingen

Geen creative-fatigue of CPM-waarschuwingen te genereren — er draaien geen ads.

## 📊 70-20-10 Classificatie

Niet uitvoerbaar zonder actieve ads.

## 💡 Voorstellen (wacht op goedkeuring)

**1. Heractiveer SYBB campagne of lanceer nieuwe campagne**
- De 2026: SYBB campagne staat sinds 2026-04-19 (37 dagen) op pauze
- Reden: zonder actieve ads bouw je geen pipeline-data op voor de SYBB-funnel, en de landing page op startyourballoonbusiness.com krijgt geen verkeer
- Verwachte impact: hervat data-collectie voor funnel-optimalisatie en lead-generatie

**2. Audit van de gepauzeerde campagnes vóór heropstart**
- Bekijk de lifetime performance van de 2026: SYBB campagne ads om te bepalen welke creatives bewezen winners waren
- Reden: bij heropstart wil je beginnen met de top performers (70% Core) in plaats van vanaf nul
- Verwachte impact: snellere ramp-up, lagere CPL in de eerste week

**3. Volgende run inplannen na campagne-launch**
- Auto-optimize draait pas zinvol als er minimaal 24 uur actieve ad-data is
- Reden: kill-regels en 70-20-10 classificatie hebben drempels die data nodig hebben (1.000 impressions, 500 link clicks)
- Verwachte impact: zinvolle automatische optimalisatie zodra de campagne live is

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

## Notities

- Output uitsluitend opgeslagen in lokale markdown file (geen Google Sheets, geen Gmail, geen Drive)
- Volgende auto-optimize run pas zinvol nadat een campagne minimaal 24 uur actief is
