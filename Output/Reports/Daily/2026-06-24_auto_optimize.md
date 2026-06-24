## Auto-Optimize Rapport — 24 juni 2026

**Run:** 2026-06-24 (handmatig)
**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs gebruikt. Geen schrijfacties naar Google Sheet.
**Periode:** afgelopen 3 dagen (`last_3d`)
**Primaire bron:** Sempertex Ad Account `act_567892422940728`

---

### 🔍 Status: geen actieve campagnes — niets te optimaliseren

De optimalisatie-engine heeft geen enkele actieve ad gevonden. Alle kill-regels, waarschuwingen en 70-20-10 classificatie zijn daarmee niet van toepassing. Er zijn **geen automatische acties uitgevoerd** en er zijn **geen wijzigingen** aangebracht in welke campagne dan ook.

#### Gecontroleerde accounts

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (Sempertex, primair) | ✅ Toegankelijk | 0 actief — alle 5 campagnes PAUSED |
| `act_607231713057715` (in command genoemd) | ❌ Geen toegang met dit API-token | n.v.t. |
| `act_1489853856181844` (toegestaan door token) | ✅ Toegankelijk | 0 actief |

> Het API-token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`. Account `act_607231713057715` uit het command kon niet worden uitgelezen ("This API token does not have access to account act_607231713057715"). Als dit account wel relevant is, moet het token-toegang krijgen of moet het juiste account-ID in het command worden gezet.

#### Campagnes op het primaire account (`act_567892422940728`)

Alle campagnes staan op PAUSED:

| Campagne | Status | Dagbudget (indien gezet) | Laatst gewijzigd |
|----------|--------|--------------------------|------------------|
| 2026: SYBB - Kopie | PAUSED | — | 20 apr 2026 |
| 2026: SYBB | PAUSED | €100,00/dag | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | — | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00/dag | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00/dag | 15 sep 2025 |

---

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

### ⚠️ Waarschuwingen

Geen waarschuwingen — geen actieve ads om op creative fatigue, dure reach of dalende Link CTR te beoordelen.

### 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

### 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen performance-gebaseerde voorstellen, omdat er geen lopende campagnes met data zijn. Wel twee operationele aandachtspunten:

**1. Beslis over de SYBB-campagne**
De hoofdcampagne "2026: SYBB" (€100,00/dag) staat sinds 19 april 2026 op pauze. Zolang deze niet draait, levert dit auto-optimize command geen waarde. Actie aan Robin: bepaal of/wanneer SYBB weer aangezet wordt, zodat de dagelijkse optimalisatie weer data heeft om op te sturen.

**2. Corrigeer de account-configuratie van het command**
Het command verwijst naar `act_607231713057715`, maar dit token heeft daar geen toegang toe. Toegestaan zijn `act_567892422940728` en `act_1489853856181844`. Actie aan Robin: ofwel het token uitbreiden, ofwel het tweede account-ID in het command vervangen door `act_1489853856181844` als dat de bedoelde tweede bron is.

---

**Conclusie:** geen optimalisaties nodig of mogelijk vandaag. Zodra een campagne weer actief is, draait dit command weer met volledige kill-regels en classificatie. Wil je dat ik een van de twee voorstellen verder oppak? Geef het nummer aan.
