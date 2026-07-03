# Auto-Optimize Rapport — 3 juli 2026

**Run:** `/ads-auto-optimize` (dagelijkse automatische optimalisatie)
**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend
**Analyseperiode:** afgelopen 3 dagen (`last_3d`)
**Primair account:** `act_567892422940728` (Sempertex Ad Account)

---

## Samenvatting

**Geen actieve campagnes gevonden. Geen optimalisatie mogelijk of nodig.**

Alle campagnes in het account staan op PAUSED. Er zijn dus geen actieve ads om tegen de kill-regels of de 70-20-10 classificatie te toetsen. Er zijn geen automatische acties uitgevoerd en er zijn geen voorstellen te genereren.

Dit sluit aan bij de status van de afgelopen dagen (SYBB gepauzeerd, geen delivery).

---

## Account-scan

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (primair) | Toegankelijk | 5 campagnes, **allemaal PAUSED** |
| `act_1489853856181844` | Toegankelijk | 0 campagnes |
| `act_607231713057715` | **Geen toegang** | Token heeft geen rechten (zie noot) |

> **Noot toegang:** Het command noemt `act_607231713057715` als secundair account, maar de huidige API-token geeft daar geen toegang toe. Toegestane accounts voor deze token: `act_1489853856181844` en `act_567892422940728`. Als dit account meegenomen moet worden, moet de token-koppeling in Pipeboard uitgebreid worden.

---

## Campagnestatus — `act_567892422940728`

| Campagne | Objective | Dagbudget | Status |
|----------|-----------|-----------|--------|
| 2026: SYBB - Kopie | OUTCOME_SALES | — | PAUSED |
| 2026: SYBB | OUTCOME_SALES | €100,00 | PAUSED |
| Last push Nozzle Up | OUTCOME_SALES | — | PAUSED |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | €70,00 | PAUSED |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | €30,00 | PAUSED |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

## ⚠️ Waarschuwingen

Geen — geen actieve delivery om op te beoordelen.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder actieve delivery.

**Aanbeveling (organisatorisch, geen ad-actie):** Zodra een campagne (bv. `2026: SYBB`) weer live gaat, draai dit command opnieuw na minimaal 24 uur delivery zodat kill-regels en classificatie op échte link-metrics kunnen draaien.

---

*Gegenereerd op 2026-07-03. Alle metrics zouden op Link CTR / CPC (link) beoordeeld worden — niet op all-clicks. In deze run was er geen delivery om te meten.*
