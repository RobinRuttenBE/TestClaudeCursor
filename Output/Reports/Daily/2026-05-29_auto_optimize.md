# Auto-Optimize Rapport — 29 May 2026

> Databron: uitsluitend Meta Ads MCP (Pipeboard). Geen Google MCPs aangeroepen, niet naar de Google Sheet geschreven. Periode: laatste 3 dagen (`last_3d`).

## Samenvatting

**Geen actieve campagnes gevonden. Er zijn geen optimalisaties uitgevoerd en geen voorstellen gegenereerd.**

Op beide toegankelijke ad accounts staan op dit moment 0 actieve campagnes. Alle SYBB- en Nozzle Up-campagnes staan op PAUSED. Er zijn dus geen actieve ads om tegen de kill-regels of de 70-20-10 classificatie te toetsen.

## Accounts gecontroleerd

| Account | Status | Resultaat |
|---------|--------|-----------|
| `act_567892422940728` (Sempertex — primair) | Toegankelijk | 0 actieve campagnes (alle PAUSED) |
| `act_1489853856181844` | Toegankelijk | 0 actieve campagnes |
| `act_607231713057715` | **Niet toegankelijk** | Token heeft geen toegang — overgeslagen |

> **Let op:** Het commando noemt `act_607231713057715` als te controleren account, maar de huidige Pipeboard-token heeft daar geen toegang toe (toegestane accounts: `act_1489853856181844`, `act_567892422940728`). Als dit account wél moet worden meegenomen, is een re-auth of token met de juiste accounttoegang nodig.

## Campagnestatus primair account (`act_567892422940728`)

Alle gevonden campagnes staan op PAUSED:

| Campagne | Status | Objective | Dagbudget | Laatst gewijzigd |
|----------|--------|-----------|-----------|------------------|
| 2026: SYBB - Kopie | PAUSED | OUTCOME_SALES | — | 20 Apr 2026 |
| 2026: SYBB | PAUSED | OUTCOME_SALES | €100,00 | 19 Apr 2026 |
| Last push Nozzle Up | PAUSED | OUTCOME_SALES | — | 21 Sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | OUTCOME_SALES | €70,00 | 15 Sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | OUTCOME_SALES | €30,00 | 15 Sep 2025 |

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om te beoordelen.

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen — geen actieve ads om op fatigue, CPM of dalende Link CTR te toetsen.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatievoorstellen mogelijk zonder live data. Het enige aandachtspunt is operationeel:

1. **Campagne 2026: SYBB staat op PAUSED.** Als de SYBB-campagne actief hoort te zijn, moet die eerst worden geactiveerd voordat dit command zinvolle optimalisaties kan doen. Wil je dat ik de campagnestatus controleer of de campagne (na jouw goedkeuring) weer activeer?
2. **Tokentoegang `act_607231713057715`.** Indien dit account relevant is voor optimalisatie, regel een Pipeboard-token met toegang tot dat account.

---

**Er is niets te optimaliseren zolang alle campagnes op PAUSED staan. Laat weten of de SYBB-campagne geactiveerd moet worden, dan draai ik dit rapport opnieuw met live data.**
