# Auto-Optimize Rapport — 29 June 2026

**Run:** automatische Meta Ads optimalisatie (laatste 3 dagen)
**Databronnen:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs aangeroepen, niet naar Google Sheet geschreven.
**Primair account:** `act_567892422940728` (Sempertex Ad Account)
**Secundair account:** `act_607231713057715`

---

## ⚠️ Belangrijkste bevinding: geen actieve campagnes

**Er zijn op dit moment geen actieve Meta Ads campagnes om te optimaliseren.** De kill-regels, 70-20-10 classificatie en budgetvoorstellen zijn daardoor niet van toepassing. Er zijn geen ads gepauzeerd en geen automatische acties uitgevoerd.

### Accountstatus

| Account | Status | Toelichting |
|---------|--------|-------------|
| `act_567892422940728` (primair) | ✅ Toegankelijk | 0 actieve campagnes. Alle 5 campagnes staan op PAUSED. |
| `act_607231713057715` (secundair) | ❌ Geen toegang | API-token heeft geen toegang tot dit account. Toegestane accounts voor dit token: `act_1489853856181844`, `act_567892422940728`. |

### Campagnes in primair account (allemaal PAUSED)

| Campagne | Status | Dagbudget | Objective | Laatst gewijzigd |
|----------|--------|-----------|-----------|------------------|
| 2026: SYBB - Kopie | PAUSED | — | OUTCOME_SALES | 20 Apr 2026 |
| 2026: SYBB | PAUSED | €100.00 | OUTCOME_SALES | 19 Apr 2026 |
| Last push Nozzle Up | PAUSED | — | OUTCOME_SALES | 21 Sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70.00 | OUTCOME_SALES | 15 Sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30.00 | OUTCOME_SALES | 15 Sep 2025 |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om tegen de kill-regels te toetsen.

- Kill-regel Lage Link CTR (< 0.8% na ≥ 1.000 impressions): niet van toepassing
- Kill-regel Hoge CPC (link) (> €1.50 na ≥ 500 link clicks): niet van toepassing

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen waarschuwingen — geen actieve ads om creative fatigue (frequency > 3.5), dure reach (CPM > €15) of dalende Link CTR te meten.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven optimalisatievoorstellen mogelijk zonder actieve campagnes. De volgende punten zijn operationeel, geen ad-optimalisaties:

1. **Heractiveer een campagne als er getest moet worden.** De `2026: SYBB` campagne (dagbudget €100.00) is de meest recente live SYBB-campagne. Zodra die weer actief is, kan dit command dagelijks meelopen en de kill-regels op echte Link CTR / CPC (link) toepassen.
2. **Tokentoegang secundair account.** Het huidige Pipeboard-token heeft géén toegang tot `act_607231713057715`. Als dit account meegenomen moet worden in de dagelijkse optimalisatie, moet de Meta-connectie opnieuw geautoriseerd worden via https://pipeboard.co/connections. Token heeft wél toegang tot `act_1489853856181844` (niet in dit command meegenomen) — bevestig of dat account relevant is.

---

**Conclusie:** geen actie nodig. Het systeem heeft niets om te optimaliseren totdat er minimaal één campagne actief is (en ten minste 24 uur loopt voordat de kill-regels gelden). Zodra `2026: SYBB` of een nieuwe campagne live gaat, draait deze run automatisch de volledige analyse.
