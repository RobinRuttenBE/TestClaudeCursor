# Auto-Optimize Rapport — 21 June 2026

**Run:** 2026-06-21 (handmatig via `/ads-auto-optimize`)
**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs, geen schrijfacties naar de tracker.
**Analyseperiode:** afgelopen 3 dagen (`last_3d`)

---

## ⚠️ Geen actieve campagnes gevonden — geen optimalisatie uitgevoerd

De auto-optimalisatie kon niet draaien omdat er **geen enkele actieve Meta Ads campagne** is op de toegankelijke accounts. Er valt dus niets te pauzeren, te classificeren of te herverdelen.

### Account-status

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (Sempertex, primair) | ✅ Toegankelijk | 5 campagnes gevonden, **allemaal PAUSED** |
| `act_607231713057715` (uit command) | ❌ Geen toegang | Token heeft geen toegang tot dit account |
| `act_1489853856181844` (wel toegestaan door token) | ✅ Toegankelijk | **0 campagnes** |

> De API-token geeft alleen toegang tot `act_1489853856181844` en `act_567892422940728`. Het in het command genoemde `act_607231713057715` is met deze token niet benaderbaar.

### Campagnes op het Sempertex-account (act_567892422940728)

Alle campagnes staan op PAUSED. Geen enkele levert op dit moment uit:

| Campagne | Objective | Status | Daily budget | Laatst gewijzigd |
|----------|-----------|--------|--------------|------------------|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | — | 20 Apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100.00 | 19 Apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | — | 21 Sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70.00 | 15 Sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30.00 | 15 Sep 2025 |

---

## ⚡ Automatische acties uitgevoerd

Geen. Er zijn geen actieve ads om tegen de kill-regels (Link CTR < 0.8% / CPC (link) > €1.50) te toetsen.

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen actieve ads om op creative fatigue (Frequency > 3.5), dure reach (CPM > €15) of dalende Link CTR te controleren.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen performance-gebaseerde voorstellen mogelijk zonder live data. Wel twee aandachtspunten van operationele aard:

1. **Hoofdcampagne staat uit.** "2026: SYBB" (het primaire SYBB-vehikel, €100/dag budget) is sinds 19 April 2026 gepauzeerd. Als SYBB-acquisitie nog een doel is, moet deze campagne eerst weer aangezet worden voordat auto-optimize zinvol kan draaien. Wil je dat ik deze (of de "- Kopie"-variant) heractiveer?
2. **Account-toegang corrigeren.** Het command verwijst naar `act_607231713057715`, maar de huidige token geeft daar geen toegang toe. Controleer of dit het juiste account-ID is of dat de token-permissies bijgewerkt moeten worden.

---

**Conclusie:** Niets te optimaliseren — alle campagnes liggen stil. Laat weten of ik de SYBB-campagne moet heractiveren; daarna kan deze run wél betekenisvolle data analyseren.
