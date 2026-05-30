# Auto-Optimize Rapport — 30 mei 2026

**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend
**Periode:** afgelopen 3 dagen (`last_3d`)
**Primair account:** `act_567892422940728` (Sempertex)
**Status run:** Geen optimalisaties uitgevoerd — geen actieve campagnes

---

## Samenvatting

**Er draaien op dit moment geen actieve Meta Ads campagnes.** Alle campagnes op het Sempertex account staan op PAUSED. Daardoor zijn er geen actieve ads om tegen de kill-regels te toetsen, geen 70-20-10 classificatie te maken, en geen budget te herverdelen. De run stopt na de data-check.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

Geen waarschuwingen — geen actieve ads om te beoordelen op creative fatigue, dure reach of dalende Link CTR.

---

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

**Budget mismatch:** Nee (geen actief budget in omloop).

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder live performance. Eén operationeel signaal:

**1. Campagne staat uit**
- De hoofdcampagne `2026: SYBB` (`120239435987290239`, dagbudget €100,00) staat op PAUSED sinds de laatste update op 19 april 2026.
- Dit is consistent met het SYBB dagrapport van 29 mei 2026 ("campaign paused, no LP traffic").
- **Actie vereist van Robin:** als SYBB weer moet draaien, reactiveer de campagne. Daarna kan dit command weer zinvol optimaliseren.

---

## Account- & campagne-overzicht (controle)

### `act_567892422940728` (Sempertex — primair)
Actieve campagnes: **0**. Alle campagnes staan op PAUSED:

| Campagne | ID | Objective | Status | Dagbudget |
|----------|-----|-----------|--------|-----------|
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | PAUSED | €100,00 |
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | PAUSED | — |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | PAUSED | — |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | PAUSED | €70,00 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | PAUSED | €30,00 |

### `act_607231713057715` (secundair — uit command)
**Niet toegankelijk** met de huidige API-token. Foutmelding: token heeft alleen toegang tot `act_1489853856181844` en `act_567892422940728`. Deze mismatch (command verwijst naar een account dat de token niet kan zien) is het melden waard — mogelijk verouderd account-ID in het command.

### `act_1489853856181844` (extra toegankelijk account)
Actieve campagnes: **0**.

---

## Conclusie

Geen actie ondernomen. Het auto-optimize systeem werkt zoals bedoeld: bij afwezigheid van actieve ads worden er geen kill-regels getriggerd en geen budget-wijzigingen voorgesteld. Zodra `2026: SYBB` (of een andere campagne) weer ACTIVE is en minimaal 24 uur draait, levert dit command bruikbare optimalisaties.

**Volgende stap:** Robin beslist of/wanneer SYBB heractiveert. Draai dit command opnieuw zodra de campagne ≥24 uur live is.
