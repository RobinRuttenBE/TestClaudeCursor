# Auto-Optimize Rapport — 15 juli 2026

> Run-modus: STRIKT. Uitsluitend Meta Ads MCP (Pipeboard) gebruikt. Geen Google MCPs (Gmail, Calendar, Drive, Sheets, Docs, Slides). Niet naar de Meta Ads Tracker Google Sheet geschreven. Output uitsluitend lokaal opgeslagen.

## Samenvatting

**Geen actieve campagnes gevonden. Geen automatische acties uitgevoerd, geen voorstellen mogelijk.**

Alle campagnes op beide toegankelijke ad accounts staan op PAUSED. Er zijn dus geen actieve ads om tegen de kill-regels of de 70-20-10-classificatie te toetsen. De optimalisatie-run heeft niets uit te voeren.

Dit sluit aan op het SYBB-rapport van 14 juli 2026 ("campaign paused").

---

## Data-check (afgelopen 3 dagen, `last_3d`)

### Accounts
Het command noemt `act_567892422940728` (primair) en `act_607231713057715` (secundair). Het actieve API-token geeft echter **geen toegang tot `act_607231713057715`**. Toegestane accounts volgens het token:

| Account | Rol in command | Toegang | Actieve campagnes |
|---------|----------------|---------|-------------------|
| `act_567892422940728` | Primair (Sempertex) | ✅ Ja | 0 |
| `act_1489853856181844` | (token-alternatief voor secundair) | ✅ Ja | 0 |
| `act_607231713057715` | Secundair (uit command) | ❌ Geen toegang | n.v.t. |

> **Aandachtspunt voor Robin:** het secundaire account in het command (`act_607231713057715`) is niet bereikbaar met dit token. In plaats daarvan geeft het token toegang tot `act_1489853856181844`. Controleer of het command het juiste account-ID moet vermelden, of dat het token-toegang uitgebreid moet worden.

### Campagne-status op `act_567892422940728`
`status_filter: "ACTIVE"` → 0 resultaten. Volledige lijst (alle statussen):

| Campagne | ID | Objective | Status | Dagbudget |
|----------|-----|-----------|--------|-----------|
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | **PAUSED** | €100,00 |
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | **PAUSED** | — |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | **PAUSED** | — |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | **PAUSED** | €70,00 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | **PAUSED** | €30,00 |

### Campagne-status op `act_1489853856181844`
`status_filter: "ACTIVE"` → 0 resultaten.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen — geen actieve ads om op frequency, CPM of Link CTR-trend te toetsen.

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren of budget over te herverdelen.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder actieve campagnes. Één operationele opmerking:

**1. Account-toegang controleren (geen ads-actie)**
- Het secundaire account uit het command (`act_607231713057715`) is niet toegankelijk; het token wijst naar `act_1489853856181844`.
- Reden: `get_campaigns` gaf `(#) This API token does not have access to account act_607231713057715`.
- Verwachte impact: correcte account-referentie voorkomt dat een tweede account onbedoeld buiten de optimalisatie valt.

**2. Campagne heractiveren (buiten scope van deze run)**
- Zodra "2026: SYBB" weer live gaat, levert deze auto-optimize run pas zinvolle kill-regels en 70-20-10-analyse op. De volgende run pikt dat automatisch op.

---

## Definitie-conventie (voor volgende runs)
- Kill-regels draaien uitsluitend op **Link CTR** (`actions.link_click / impressions × 100`) en **CPC (link)** (`spend / actions.link_click`), nooit op Meta's kale `ctr`/`cpc`.
- Drempels: pauzeer bij Link CTR < 0,8% (≥ 1.000 impressions) of CPC (link) > €1,50 (≥ 500 link clicks).

---

*Rapport gegenereerd 15 juli 2026. Bron: Meta Ads MCP (Pipeboard), `date_preset: last_3d`. Geen automatische wijzigingen doorgevoerd.*
