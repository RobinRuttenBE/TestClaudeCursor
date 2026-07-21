# Auto-Optimize Rapport — 21 July 2026

**Run:** 2026-07-21 (handmatig via /ads-auto-optimize)
**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs, geen schrijfacties naar de Tracker Google Sheet.
**Periode:** last_3d
**Metrics:** Link CTR en CPC (link) waar van toepassing (kill-regels draaien uitsluitend op link-varianten).

---

## Samenvatting

**Geen actieve Meta Ads campagnes gevonden. Geen automatische acties uitgevoerd, geen optimalisaties mogelijk.**

Alle campagnes op het primaire Sempertex Ad Account staan op PAUSED, inclusief de SYBB-campagne. Er zijn dus geen ads die tegen de kill-regels of de 70-20-10 classificatie kunnen worden getoetst. Er is niets gepauzeerd (er stond niets aan) en er zijn geen budget- of variatievoorstellen, omdat er geen live performance-data is over de afgelopen 3 dagen.

---

## Accounts gecontroleerd

| Account | Toegang | Actieve campagnes | Opmerking |
|---------|---------|-------------------|-----------|
| `act_567892422940728` (primair) | ✅ Ja | 0 | Alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ Ja | 0 | Geen campagnes aanwezig |
| `act_607231713057715` | ❌ Nee | n.v.t. | Token heeft geen toegang tot dit account |

> **Let op — accounttoegang.** Het command noemt `act_607231713057715` als extra te controleren account, maar de Meta API-token via Pipeboard heeft daar geen toegang toe. Toegestane accounts voor deze token: `act_1489853856181844` en `act_567892422940728`. Als dit account wél gemonitord moet worden, moet de juiste Facebook-login/connection aan Pipeboard gekoppeld worden (via https://pipeboard.co/connections).

---

## Campagne-status primair account (`act_567892422940728`)

| Campagne | Status | Daily budget | Laatst gewijzigd |
|----------|--------|-------------|------------------|
| 2026: SYBB | PAUSED | €100,00 | 2026-04-19 |
| 2026: SYBB - Kopie | PAUSED | — | 2026-04-20 |
| Last push Nozzle Up | PAUSED | — | 2025-09-21 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 2025-09-15 |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

## ⚠️ Waarschuwingen

Geen — zonder actieve ads is er geen creative fatigue, CPM- of Link CTR-signaal te meten.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven optimalisatievoorstellen mogelijk zonder live campagnes.

**Actiepunt voor Robin (geen automatische actie):**
1. De SYBB-campagne (`120239435987290239`, daily budget €100,00) staat op PAUSED. Als SYBB weer moet lopen, zet de campagne (en de gewenste ad sets/ads) op ACTIVE. Zodra er ≥24 uur live data is, levert een volgende /ads-auto-optimize run wél kill-regel-checks en 70-20-10 classificatie op.
2. Bevestig of `act_607231713057715` gemonitord moet worden; zo ja, koppel de juiste connection in Pipeboard.

---

**Geen goedkeuring nodig deze run — er waren geen acties of voorstellen. Laat weten wanneer SYBB weer live staat, dan draai ik de volledige analyse.**
