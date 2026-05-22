# Auto-Optimize Rapport — 2026-05-22

**Run modus:** scheduled / handmatig
**Data bron:** Meta Ads MCP (Pipeboard) — accounts gecheckt: `act_567892422940728`, `act_1489853856181844`
**Periode:** last_3d

---

## Status: GEEN ACTIEVE CAMPAGNES

Beide toegankelijke ad accounts hebben momenteel **0 actieve campagnes**. Er valt dus niets te optimaliseren, te pauzeren of te herclassificeren.

### Account overzicht

| Account | Actieve campagnes | Totaal campagnes | Status |
|---|---|---|---|
| `act_567892422940728` (Sempertex primair) | 0 | 5 | Alle 5 op PAUSED |
| `act_1489853856181844` (alternatief) | 0 | 0 | Leeg |

### Campagnes in `act_567892422940728` (allemaal PAUSED)

| Campagne | Objective | Status | Laatst geüpdatet |
|---|---|---|---|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | 2026-04-20 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | 2026-04-19 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | 2025-09-21 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | 2025-09-15 |

---

## ⚡ Automatische acties uitgevoerd

**Totaal gepauzeerd: 0 ads** — Geen actieve ads om te evalueren tegen de kill-regels (Link CTR < 0.8% of CPC (link) > €1.50).

## ⚠️ Waarschuwingen

Geen waarschuwingen — er zijn geen actieve ads die frequency, CPM of CTR-fatigue-checks kunnen triggeren.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen

Geen optimalisatievoorstellen mogelijk zonder live performance data. De hoofdcampagne **2026: SYBB** staat sinds 2026-04-19 op PAUSED. Robin: laat me weten wanneer je de campagne reactiveert of een nieuwe live wil zetten — dan kan de eerstvolgende run weer kill-regels toepassen en classificeren.

---

## Logregels

- 2026-05-22 — Auto-optimize gestart, both accounts gecheckt met `get_campaigns`.
- 2026-05-22 — `act_607231713057715` niet toegankelijk vanuit huidige token (allowed accounts: `act_1489853856181844`, `act_567892422940728`). Niet kritiek voor deze run.
- 2026-05-22 — Geen `get_insights` of `update_ad` calls uitgevoerd: pre-conditie (≥1 actieve campagne) niet behaald.
- 2026-05-22 — Geen Google MCPs aangeroepen conform run-instructie. Output uitsluitend lokaal opgeslagen.
