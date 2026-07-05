# Auto-Optimize Rapport — 5 juli 2026

**Run:** 2026-07-05 (handmatig via `/ads-auto-optimize`)
**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs aangeroepen, geen schrijfacties naar de Tracker Google Sheet.
**Periode:** laatste 3 dagen (`last_3d`)
**Metrics-conventie:** kill-regels op Link CTR en CPC (link), nooit all-clicks.

---

## ⛔ Geen actieve campagnes gevonden

De analyse kon niet worden uitgevoerd omdat er **geen enkele actieve Meta Ads campagne draait** in de toegankelijke accounts. Er is dus niets om te meten, te pauzeren of te optimaliseren.

### Account-status

| Account | Toegang | Actieve campagnes | Opmerking |
|---------|---------|-------------------|-----------|
| `act_567892422940728` (Sempertex — primair) | ✅ Ja | **0** | Alle 5 campagnes staan op PAUSED |
| `act_1489853856181844` | ✅ Ja | **0** | Geen actieve campagnes |
| `act_607231713057715` | ❌ Nee | n.v.t. | Token heeft geen toegang tot dit account |

> Het commando noemt `act_607231713057715` als secundair account, maar de huidige API-token geeft daar geen toegang toe. Toegestane accounts volgens de token: `act_567892422940728` en `act_1489853856181844`.

### Campagnes in het primaire account (`act_567892422940728`)

Alle campagnes staan gepauzeerd — geen enkele levert momenteel impressies:

| Campagne | Objective | Status | Dagbudget | Laatst gewijzigd |
|----------|-----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | — | 2026-04-20 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100,00 | 2026-04-19 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | — | 2025-09-21 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30,00 | 2025-09-15 |

De hoofdcampagne **2026: SYBB** is sinds 19 april 2026 gepauzeerd.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd** — er zijn geen actieve ads om tegen de kill-regels te toetsen. ✅

- Lage Link CTR (< 0.8% na ≥1.000 impressions): niet van toepassing
- Hoge CPC (link) (> €1.50 na ≥500 link clicks): niet van toepassing

## ⚠️ Waarschuwingen

Geen — geen actieve creatives om op creative fatigue (freq > 3.5), dure reach (CPM > €15) of dalende Link CTR te controleren.

## 📊 70-20-10 Classificatie

Niet uitvoerbaar. Er zijn geen actieve ads om te classificeren in Core / Emerging / Experimental. Budgetverdeling en -mismatch zijn n.v.t.

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen performance-gedreven voorstellen mogelijk zonder actieve data. Wel twee praktische aandachtspunten:

**1. Campagne activeren**
Als SYBB weer moet draaien: heractiveer campagne **2026: SYBB** (`120239435987290239`, dagbudget €100,00). Pas na minimaal 24 uur levering zijn de kill-regels en 70-20-10 classificatie betrouwbaar toepasbaar. Dit vereist expliciete goedkeuring — geen actie ondernomen.

**2. Token-toegang controleren**
Het account `act_607231713057715` uit het commando is niet bereikbaar met de huidige token. Controleer of dit account nog relevant is, of werk het commando bij naar de toegestane accounts (`act_567892422940728`, `act_1489853856181844`).

---

**Conclusie:** geen actieve campagnes → geen automatische acties, geen voorstellen. Zodra een campagne minimaal 24 uur draait, kan dit rapport zinvolle optimalisaties genereren. Wil je dat ik **2026: SYBB** heractiveer? Geef dat expliciet aan.
