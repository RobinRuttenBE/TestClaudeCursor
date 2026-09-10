## Auto-Optimize Rapport, 10 september 2026

**Run:** 2026-09-10, analysevenster 7 t/m 9 september 2026 (3 dagen)
**Databronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, de MCP zelf vroeg om authenticatie) en PostHog project STX EU (directe REST route, de MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet in Pipeboard.

### Automatische acties uitgevoerd

Geen ads gepauzeerd. Er is geen enkele actieve ad om kill-regels op toe te passen.

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|----|-------------|
| geen | n.v.t. | n.v.t. | n.v.t. | 0 impressions, 0 link clicks, €0,00 spend |

**Totaal gepauzeerd: 0 ads.** Geen `update_ad` calls gedaan.

**Status alle campagnes (Meta, 10 september):**

| Campagne | Status | Laatst gewijzigd |
|---|---|---|
| Wholesaler Campagne (SWE) | PAUSED | 4 sep 2026 11:50 |
| Wholesaler Campagne (LIT) | PAUSED | 4 sep 2026 11:50 |
| 2026: SYBB - Kopie | PAUSED | 27 aug 2026 |
| 2026: SYBB | PAUSED | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | 15 sep 2025 |

Meta geeft over 7 t/m 9 september 0 rijen op ad-niveau en 0 rijen op campagneniveau. Dit is de zevende dag op rij zonder levering.

**PostHog bevestigt de stilstand (5 t/m 10 september):**

| Dag | Sessies /become-a-distributor met cpc | Organisch |
|---|---|---|
| 5 sep | 0 | 3 |
| 6 sep | 0 | 5 |
| 7 sep | 0 | 4 |
| 8 sep | 0 | 3 |
| 9 sep | 0 | 5 |
| 10 sep (tot nu) | 0 | 1 |

Sitewide 0 sessies met cpc als medium sinds 5 september. Laatste `wholesaler_form_submit`: 4 september 06:41 UTC. Totaal sinds 25 augustus: 33 inzendingen.

### Waarschuwingen

Geen. Frequency, CPM en Link CTR zijn niet meetbaar zonder levering. De lifetime-waarschuwing van het ads-rapport van vandaag blijft staan: Wholesaler (LIT) sloot af op frequency 3,97, dus bij herstart eerst een nieuwe creative toevoegen.

### 70-20-10 Classificatie

Niet van toepassing, 0 actieve ads. Huidig dagbudget €0,00.

Ter referentie de laatst bekende lifetime-classificatie (basis: 30d ads-rapport van 10 september, all-clicks metrics, niet link-gecorrigeerd):

**70% Core:** Video 2 (LIT) €28,75 per inzending, Video 1 (LIT) €29,38 per inzending, Statisch 1 (LIT)
**20% Emerging:** Statisch 2 (SWE) CTR 4,0%, Statisch 2 (LIT) CPC €0,20 maar lage conversie
**10% Experimental:** nieuwe creative per markt, nog te maken
**Niet herstarten:** Video 1 (SWE) 0 inzendingen op 113 sessies, Video 2 (SWE) €63,50 per inzending

**Budget mismatch:** Nee, er is geen budget in omloop.

### Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 3 september. Zolang niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen.

**1. Budget herverdeling / herstart**
- Wholesaler (LIT): herstart op €100,00 per dag. Verdeling €70,00 Core (Video 1, Video 2, Statisch 1), €20,00 Statisch 2 (LIT), €10,00 nieuwe creative.
- Wholesaler (SWE): herstart beperkt op €40,00 per dag, alleen Statisch 2 (SWE) plus één nieuwe creative. Beide SWE-video's uit laten.
- Reden: LIT leverde 16 inzendingen op €562,14 (€35,13 per inzending), SWE 8 op €507,24 (€63,41).
- Verwachte impact: bij gelijke conversie circa 20 tot 25 inzendingen per week uit LIT.

**2. Nieuwe variaties**
- Op Statisch 2 (SWE), best CTR 4,0%: variatie A met proof-hook (Sempertex heritage, EU-certificering), variatie B met Wholesaler-marge als hook.
- Op Video 2 (LIT), beste kosten per inzending: variatie A korte cut van 15 seconden met dezelfde eerste 3 seconden, variatie B met andere CTA ("Request your distributor pricing").

**3. Audience aanpassingen**
- LIT ad sets samenvoegen tot één ad set zodat Meta het budget zelf verdeelt.
- SWE audience verbreden om de CPM van €12,92 en de video-CPM boven €15 te drukken.

**4. Conversie-guard op kill-regels**
- Ads met minimaal 1 PostHog-inzending in de laatste 3 dagen niet automatisch pauzeren op Link CTR alleen. Voorkomt dat Statisch 1 (LIT) op dag 1 na herstart sneuvelt.

**5. Tracking fix vóór herstart**
- Meta telde 19 leads tegenover 33 in PostHog. Pixel-event op de bedankpagina controleren voordat er budget terug aangaat.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

### Log
- 2026-09-10 run: get_campaigns (7 campagnes, alle PAUSED), get_insights level=ad 2026-09-07 t/m 2026-09-09 (0 rijen), get_insights level=campaign last_3d (0 rijen). 0 automatische acties, 0 update_ad calls.
