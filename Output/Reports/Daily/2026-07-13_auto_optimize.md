# Auto-Optimize Rapport — 13 juli 2026

_Bron: Meta Ads MCP (Pipeboard). Alleen Meta Ads en PostHog toegestaan voor deze run. Er is niet naar Google Sheets of andere Google-diensten geschreven._

## Samenvatting

**Er zijn geen actieve Meta Ads campagnes om te optimaliseren.** Alle campagnes op het Sempertex Ad Account staan op PAUSED. Er zijn dus geen ads waarop kill-regels, waarschuwingsregels of 70-20-10 classificatie van toepassing kunnen zijn. Er zijn geen automatische acties uitgevoerd en er zijn geen voorstellen te doen.

## Accountstatus

| Account | Toegang | Actieve campagnes | Opmerking |
|---------|---------|-------------------|-----------|
| `act_567892422940728` (Sempertex, primair) | ✅ Ja | 0 | Alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ Ja | 0 | Geen actieve campagnes |
| `act_607231713057715` | ❌ Nee | n.v.t. | API-token heeft geen toegang tot dit account |

> Opmerking: het command noemt `act_607231713057715` als tweede te controleren account, maar het huidige API-token geeft daar geen toegang toe (toegestane accounts: `act_1489853856181844`, `act_567892422940728`). Dit account is daarom overgeslagen. Als dit account wel gecontroleerd moet worden, moet de Pipeboard-koppeling opnieuw geautoriseerd worden met een login die dit account bezit.

## Campagnes op het primaire account (`act_567892422940728`)

Alle campagnes staan op **PAUSED**:

| Campagne | ID | Objective | Status | Dagbudget | Laatst gewijzigd |
|----------|-----|-----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | PAUSED | — | 20 apr 2026 |
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | PAUSED | — | 21 sep 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | PAUSED | €30,00 | 15 sep 2025 |

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

## ⚠️ Waarschuwingen

Geen — er zijn geen actieve ads om op te beoordelen (creative fatigue, CPM, dalende Link CTR).

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven optimalisatie-voorstellen mogelijk zonder actieve campagnes. Wel één operationeel aandachtspunt:

**1. SYBB-campagne staat sinds ~19 april 2026 op pauze**
- De campagne `2026: SYBB` (dagbudget €100,00) en de kopie `2026: SYBB - Kopie` zijn beide inactief.
- Zolang deze op PAUSED staan is er geen ad-verkeer, geen landingspagina-data, en niets om dagelijks te optimaliseren.
- **Actie voor Robin:** bevestig of dit bewust is (campagne afgerond / seizoenspauze) of dat de campagne weer live moet. Pas als er een actieve campagne draait, levert dit auto-optimize command dagelijks bruikbare acties op.

---

**Wil je dat ik iets doe zodra de SYBB-campagne weer actief is, of moet ik nu een van de gepauzeerde campagnes activeren? Dat laatste is een niveau-2 actie en voer ik alleen uit na jouw expliciete goedkeuring.**
