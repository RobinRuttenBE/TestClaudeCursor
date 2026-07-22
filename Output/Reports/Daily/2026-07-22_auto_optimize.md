# Auto-Optimize Rapport — 22 juli 2026

**Databron:** Meta Ads MCP (Pipeboard) — accounts `act_567892422940728` (primair) en `act_1489853856181844`
**Periode:** laatste 3 dagen (last_3d)
**Run type:** automatisch (Niveau 1 kill-regels + Niveau 2 voorstellen)

---

## Samenvatting

**Geen actieve campagnes gevonden. Geen optimalisatie-acties uitgevoerd.**

Op beide toegankelijke ad accounts staan momenteel geen actieve campagnes of ads. Er is geen spend geregistreerd in de afgelopen 3 dagen. De kill-regels (Niveau 1) en de 70-20-10 classificatie zijn daardoor niet van toepassing — er is niets om te pauzeren, te classificeren of te herverdelen.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

Geen creative fatigue, dure reach of dalende Link CTR te melden — er draaien geen ads.

**Wel een operationele waarschuwing (data-toegang):**

| Signaal | Detail | Actie aanbevolen |
|---|---|---|
| Account niet toegankelijk | `act_607231713057715` (in command genoemd als secundair account) geeft: "This API token does not have access". Toegestane accounts: `act_1489853856181844`, `act_567892422940728`. | Controleer of dit account nog gecheckt moet worden; zo ja, API-token permissies uitbreiden in Pipeboard. |

---

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

**Budget mismatch:** Nee (geen lopend budget).

---

## Status per account

### `act_567892422940728` (primair — Sempertex)
Alle campagnes staan op **PAUSED**. Geen spend in last_3d.

| Campagne | Objective | Status | Dagbudget | Laatst gewijzigd |
|---|---|---|---|---|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | — | 20 apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | — | 21 sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30,00 | 15 sep 2025 |

### `act_1489853856181844` (secundair — toegankelijk)
Geen campagnes gevonden (leeg).

### `act_607231713057715` (in command genoemd)
Niet toegankelijk met huidige API-token — overgeslagen.

---

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven optimalisatie-voorstellen mogelijk zonder actieve campagnes. Wel twee acties om de flow werkend te krijgen:

**1. SYBB-campagne activeren**
De hoofdcampagne `2026: SYBB` (act_567892422940728) staat sinds 19 april 2026 op PAUSED met een dagbudget van €100,00. Zolang deze niet loopt, levert `/ads-auto-optimize` geen bruikbare output. Actie: bevestig of SYBB weer live moet en zo ja, activeer de campagne (of de gewenste ad sets) handmatig.

**2. Account-toegang controleren**
Los de toegang tot `act_607231713057715` op, of verwijder dit account uit de command-configuratie als het niet meer relevant is. Nu wordt het bij elke run overgeslagen met een foutmelding.

---

**Er zijn geen Niveau 2 voorstellen om goed te keuren — er draait geen verkeer. Zodra SYBB (of een andere campagne) actief is, levert de volgende run een volledige analyse op.**
