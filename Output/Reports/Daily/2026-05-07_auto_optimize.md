# Auto-Optimize Rapport — 2026-05-07

**Run mode:** strikt (alleen Meta Ads MCP + PostHog MCP, geen Google MCPs, geen Sheet writes)
**Periode geanalyseerd:** afgelopen 3 dagen (2026-05-04 t/m 2026-05-06)
**Accounts gecheckt:** `act_567892422940728` (primair), `act_1489853856181844` (secundair)

---

## Samenvatting

**Geen actieve Meta Ads campagnes gevonden. Geen optimalisaties uitgevoerd of voorgesteld.**

Beide accounts waarvoor de API token toegang heeft, zijn 100% paused. Er zijn dus geen ads om tegen kill-regels of de 70-20-10 classificatie te toetsen, en er is geen spend, impressions of click data over de laatste 3 dagen.

---

## ⚡ Automatische acties uitgevoerd

Geen. Er zijn geen actieve ads om te pauzeren. ✅

---

## ⚠️ Waarschuwingen

Geen creative-fatigue, dure-reach of dalende-CTR signalen gedetecteerd, simpelweg omdat er geen ads draaien.

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn 0 actieve ads in beide accounts.

- **70% Core:** —
- **20% Emerging:** —
- **10% Experimental:** —

**Budget mismatch:** N.v.t.

---

## Account status

### `act_567892422940728` — Sempertex Europe (primair)

| Campagne | Status | Daily budget | Laatst geüpdatet |
|----------|--------|--------------|------------------|
| 2026: SYBB - Kopie | PAUSED | — | 2026-04-20 |
| 2026: SYBB | PAUSED | €100,00 | 2026-04-19 |
| Last push Nozzle Up | PAUSED | — | 2025-09-21 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 2025-09-15 |

- Actieve campagnes: 0
- Spend last_3d: €0,00
- Impressions last_3d: 0

### `act_1489853856181844` — secundair

- Actieve campagnes: 0
- Spend last_3d: €0,00
- Impressions last_3d: 0

### `act_607231713057715`

- API token heeft geen toegang tot dit account. Niet geanalyseerd.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder live ads. Wel een paar observaties van het type "wat nu":

**1. SYBB campagne herstarten of definitief opbergen**
- De campagne `2026: SYBB` (id `120239435987290239`) staat sinds 2026-04-19 op pause met een daily budget van €100,00.
- Reden om te beslissen: óf herstarten met de geüpdatete kill-drempels (Link CTR < 0,8%, CPC link > €1,50) en het link-metrics regime, óf archiveren zodat de account-overzichten leeger en duidelijker worden.
- Verwachte impact: zonder beslissing blijft `/ads-auto-optimize` dagelijks een lege run produceren.

**2. Account-toegang `act_607231713057715` valideren**
- API token mist permissies; dit account is dus een blinde vlek.
- Actie: óf toegang regelen via de Pipeboard MCP, óf het account uit het command verwijderen zodat de auto-optimize niet meer onnodig naar een ontoegankelijke bron grijpt.

**3. Geen variatie- of audience-voorstellen**
- Zonder Link CTR / CPC data van de laatste 3 dagen kan ik geen winnende hooks of saturated audiences identificeren. Eerst spend nodig.

---

## Methodologie

- Tools gebruikt: `get_campaigns` (status_filter ACTIVE en zonder filter), `get_insights` op account-niveau met `time_range: last_3d`.
- Niet gebruikt: Google Gmail/Calendar/Drive/Sheets/Docs/Slides MCPs (per run-instructie geblokkeerd).
- Output: alleen dit lokale markdown bestand. Geen schrijfacties naar de Meta Ads Tracker Google Sheet.
- Kill-regels (Link CTR < 0,8% bij ≥ 1.000 impressions, CPC link > €1,50 bij ≥ 500 link clicks): niet getriggerd, want geen impressions/clicks.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
