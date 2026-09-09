## Auto-Optimize Rapport, 9 september 2026

**Run:** 2026-09-09, automatische run na /ads-report
**Databronnen:** Pipeboard Meta Ads via directe JSON-RPC route (MCP vroeg om authenticatie) en PostHog STX EU via directe REST route (MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er is niets om op te draaien: alle 7 campagnes staan op PAUSED en Meta registreert over last_3d (6 t/m 8 september) 0 rijen op ad-niveau, dus 0 impressions, 0 link clicks en €0,00 spend. Er zijn geen `update_ad` calls gedaan.

| Campagne | Status | Laatst gewijzigd |
|---|---|---|
| Wholesaler Campagne (SWE) | PAUSED | 4 september 2026 |
| Wholesaler Campagne (LIT) | PAUSED | 4 september 2026 |
| 2026: SYBB - Kopie | PAUSED | 27 augustus 2026 |
| 2026: SYBB | PAUSED | 19 april 2026 |
| Last push Nozzle Up | PAUSED | 21 september 2025 |
| Nozzle Up END OF AUGUST | PAUSED | 15 september 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | 15 september 2025 |

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

Geen actieve ads, dus geen frequency-, CPM- of Link CTR-signalen te melden. Dit rapport is de zesde opeenvolgende dag met 0 levering (sinds 4 september).

**PostHog bevestiging (6 t/m 9 september):**

| Dag | Sessies met utm_medium=cpc | Sessies op /become-a-distributor | Inzendingen |
|---|---|---|---|
| 6 september | 0 | 5 (organisch) | 0 |
| 7 september | 0 | 4 (organisch) | 0 |
| 8 september | 0 | 3 (organisch) | 0 |
| 9 september (tot nu) | 0 | 1 (organisch) | 0 |

Laatste wholesaler_form_submit: 4 september 2026. Sinds 1 september in totaal 6 inzendingen, allemaal vóór de pauze.

### 📊 70-20-10 Classificatie

Niet van toepassing, 0 actieve ads en €0,00 dagbudget in levering. De laatst bekende classificatie op basis van de 30-daagse data (zie /ads-report van 9 september) blijft staan als uitgangspunt voor een herstart:

**70% Core:** Video 1 (LIT), Video 2 (LIT), Statisch 1 (LIT). Beste kosten per inzending (€28,75 tot €29,38).
**20% Emerging:** Statisch 2 (SWE). Hoogste All Clicks CTR (4,0%), nog te weinig inzendingen voor een definitief oordeel.
**10% Experimental:** één nieuwe creative per markt om de frequency (LIT 3,97) te doorbreken.
**Niet herstarten:** Video 1 (SWE) en Video 2 (SWE). CPM boven €15 en 0 respectievelijk €63,50 per inzending.

**Budget mismatch:** Niet meetbaar, geen budget in levering.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 7 en 8 september. Niets is goedgekeurd of uitgevoerd.

**1. Budget herverdeling en herstart**
- Herstart Wholesaler Campagne (LIT) op €100,00 per dag: €70,00 naar de Core set (Video 1, Video 2, Statisch 1), €20,00 naar Statisch 2 (LIT) met verlaagd aandeel, €10,00 naar één nieuwe creative.
- Herstart Wholesaler Campagne (SWE) beperkt op €40,00 per dag: alleen Statisch 2 (SWE) plus één nieuwe creative. Beide SWE-video's uit laten.
- Reden: LIT levert inzendingen tegen €35,13, SWE tegen €72,46. De SWE-video's trekken de campagne omlaag.
- Verwachte impact: bij gelijke conversie circa 3 inzendingen per dag op LIT tegen €30,00 tot €35,00 per stuk.

**2. Nieuwe variaties**
- Twee variaties op Statisch 2 (SWE), sterkste hook op All Clicks CTR: andere CTA (aanvraagformulier direct benoemen) en een carrousel-format met productrange.
- Twee variaties op Video 2 (LIT), beste kosten per inzending: kortere cut (eerste 15 seconden) en versie met tekstoverlay op de eerste 3 seconden.
- Doel: nieuwe creatives tegen creative fatigue op LIT (frequency 3,97).

**3. Audience aanpassingen**
- LIT ad sets samenvoegen tot één set zodat het algoritme meer data per set krijgt.
- SWE audience verbreden (interesse-uitbreiding aan) om de hoge CPM (€12,92 campagne, €15,27 en €17,07 op de video's) te drukken.

**4. Conversie-guard op de kill-regels**
- Ads met minstens 1 PostHog-inzending in de laatste 7 dagen niet automatisch pauzeren op Link CTR alleen. Voorkomt dat Statisch 1 (LIT) op dag 1 na herstart wordt gepauzeerd.

**5. Tracking fix vóór herstart**
- Meta telde 19 leads tegenover 33 inzendingen in PostHog over dezelfde periode. Pixel of Conversions API nalopen op het formulier voordat er weer budget op gaat, anders optimaliseert Meta op te weinig signalen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.** Zolang er niets herstart is, blijft elke dagelijkse auto-optimize run op 0 acties uitkomen.
