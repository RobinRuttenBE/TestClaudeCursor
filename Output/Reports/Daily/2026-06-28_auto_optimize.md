# Auto-Optimize Rapport — 28 juni 2026

**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven.
**Analyseperiode:** laatste 3 dagen (`last_3d`)
**Primair account:** `act_567892422940728` (Sempertex)

---

## ⛔ Geen optimalisatie uitgevoerd — geen actieve campagnes

Er draaien op dit moment **geen actieve Meta Ads campagnes**. Alle kill-regels, waarschuwingen en 70-20-10 classificatie zijn daardoor niet van toepassing.

### Wat is gecontroleerd

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (primair) | ✅ Toegankelijk | 0 actieve campagnes. 5 campagnes totaal, **allemaal PAUSED** |
| `act_1489853856181844` | ✅ Toegankelijk | 0 actieve campagnes |
| `act_607231713057715` (genoemd in command) | ❌ Geen toegang | API-token heeft geen toegang tot dit account |

> **Let op — accounttoegang:** Het command verwijst naar `act_607231713057715`, maar het huidige Pipeboard-token geeft daar geen toegang toe. De toegestane accounts zijn `act_567892422940728` en `act_1489853856181844`. Als dit account daadwerkelijk gemonitord moet worden, moet de Pipeboard-connectie opnieuw geautoriseerd worden (zie https://pipeboard.co/connections).

### Campagnes op het primaire account (allemaal PAUSED)

| Campagne | Objective | Status | Laatst gewijzigd |
|----------|-----------|--------|------------------|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | 20 apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | 19 apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | 21 sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | 15 sep 2025 |

De hoofdcampagne **2026: SYBB** staat sinds 19 april 2026 op pauze. Een insights-check over de laatste 3 dagen bevestigt **geen spend, geen impressions, geen delivery**.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om tegen de drempelwaarden te toetsen.

## ⚠️ Waarschuwingen

Geen — niet van toepassing zonder actieve delivery.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatievoorstellen mogelijk zonder live data. Wel twee aandachtspunten voor Robin:

**1. Geen enkele campagne is live.** De SYBB-funnel draait al sinds half april niet meer. Als er actief budget moet lopen, moet campagne **2026: SYBB** (of een nieuwe variant) eerst geactiveerd worden. Pas daarna levert dit command zinvolle optimalisatie op.

**2. Accounttoegang herstellen.** `act_607231713057715` is niet bereikbaar met het huidige token. Controleer of dit het juiste account-ID is of herautoriseer de Pipeboard-connectie, anders blijft dit account buiten elke geautomatiseerde optimalisatie.

---

**Conclusie:** Niets te optimaliseren vandaag. Activeer eerst minimaal één campagne (vermoedelijk 2026: SYBB) en draai dit command daarna opnieuw voor een volwaardige analyse.
