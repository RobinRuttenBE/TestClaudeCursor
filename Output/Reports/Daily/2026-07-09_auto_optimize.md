# Auto-Optimize Rapport — 9 juli 2026

**Run:** `/ads-auto-optimize` (handmatig)
**Periode geanalyseerd:** laatste 3 dagen (6–9 juli 2026)
**Databronnen:** Meta Ads MCP (Pipeboard). PostHog niet geraadpleegd (zie toelichting).
**Primair account:** `act_567892422940728` (Sempertex)
**Secundair account:** `act_607231713057715` — **geen toegang** met deze token (allowed: `act_1489853856181844`, `act_567892422940728`)

---

## ⛔ Belangrijkste bevinding: geen actieve campagnes

Er zijn **0 actieve (ACTIVE) campagnes** op het primaire account. Alle 5 aanwezige campagnes staan op **PAUSED**. Er is dus geen live delivery, geen impressie- of clickdata over de afgelopen 3 dagen, en er is **niets om te optimaliseren of te pauzeren**.

| Campagne | Status | Daily budget | Objective | Laatst gewijzigd |
|----------|--------|-------------|-----------|------------------|
| 2026: SYBB - Kopie | PAUSED | — | OUTCOME_SALES | 20 apr 2026 |
| 2026: SYBB | PAUSED | €100,00 | OUTCOME_SALES | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | — | OUTCOME_SALES | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | OUTCOME_SALES | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | OUTCOME_SALES | 15 sep 2025 |

> De hoofdcampagne **2026: SYBB** (€100,00/dag budget) staat sinds 19 april 2026 op pauze.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om tegen de kill-regels te toetsen. ✅

**Totaal gepauzeerd: 0 ads**

Kill-regels (Link CTR < 0.8% na ≥1.000 impressions; CPC (link) > €1,50 na ≥500 link clicks) zijn **niet van toepassing**: geen enkele ad heeft in de meetperiode gedraaid.

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---------|--------|------------------|
| Geen actieve campagnes | 5/5 PAUSED | Beslis of de SYBB-campagne heractiveerd moet worden — er wordt momenteel geen budget besteed en geen data verzameld |
| Secundair account onbereikbaar | `act_607231713057715` geen token-toegang | Indien dit account relevant is: connectie/permissies herstellen via Pipeboard (zie toelichting) |

Creative fatigue, dure reach (CPM) en dalende Link CTR konden niet beoordeeld worden — geen delivery.

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Zonder actieve ads en zonder performance-data (impressions, link clicks, spend) kan geen enkele ad worden geclassificeerd als Core / Emerging / Experimental.

**Budget mismatch:** Nee — er wordt geen budget besteed.

---

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven budget-, variatie- of audience-voorstellen mogelijk zonder live performance. De enige zinvolle vervolgstappen zijn operationeel:

**1. Beslissing over heractivatie SYBB**
- De campagne **2026: SYBB** (€100,00/dag) staat sinds 19 april 2026 op pauze.
- Actie nodig van Robin: is dit bewust (campagne afgelopen/on hold) of moet de campagne weer aan?
- Zolang alles op PAUSED staat heeft dagelijkse auto-optimalisatie geen functie.

**2. Toegang secundair account controleren**
- `act_607231713057715` geeft een token-fout. De actieve Pipeboard-connectie heeft alleen toegang tot `act_1489853856181844` en `act_567892422940728`.
- Actie nodig van Robin: bevestig of `act_607231713057715` nog gebruikt wordt. Zo ja, herstel de connectie/permissies via Pipeboard. Zo nee, verwijder het account uit dit command zodat de foutmelding verdwijnt.
- Opvallend: er is wél een account `act_1489853856181844` toegankelijk dat niet in dit command staat — mogelijk relevant om toe te voegen.

---

## Toelichting op databronnen

- **PostHog** is niet geraadpleegd: cross-referencing van ad-data met landingspagina-gedrag heeft geen waarde zonder actieve ad-traffic in de periode.
- Conform de strikte regel voor deze run zijn **uitsluitend** de Meta Ads MCP (Pipeboard) gebruikt. Geen Google-services (Gmail, Calendar, Drive, Sheets, Docs, Slides) aangeroepen. Niet naar de Meta Ads Tracker Google Sheet geschreven. Output uitsluitend lokaal opgeslagen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
