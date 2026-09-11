## Auto-Optimize Rapport, 11 september 2026

**Run:** 2026-09-11 11:12 (lokale tijd)
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, MCP weigerde authenticatie) en PostHog project STX EU (directe REST route, MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in de command genoemde act_607231713057715 bestaat niet in Pipeboard.
**Periode:** 8 t/m 11 september 2026 (last_3d plus vandaag)

### Status van het account

| Campagne | Status | Laatste wijziging |
|---|---|---|
| Wholesaler Campagne (SWE) | PAUSED | 4 sep 2026, 11:50 |
| Wholesaler Campagne (LIT) | PAUSED | 4 sep 2026, 11:50 |
| 2026: SYBB - Kopie | PAUSED | 27 aug 2026 |
| 2026: SYBB | PAUSED | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | 15 sep 2025 |

`get_campaigns` met `status_filter: ACTIVE` geeft een lege lijst. `get_insights` op ad-niveau over 8 t/m 11 september geeft 0 rijen: 0 impressions, 0 link clicks, €0,00 spend. Dit is de achtste dag op rij zonder levering.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn geen actieve ads, dus geen enkele ad heeft de minimale data (1.000 impressions of 500 link clicks) voor een kill-regel. Geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| Geen levering | 8 dagen zonder impressions sinds 4 sep | Beslissen over herstart Wholesaler (LIT) en (SWE), zie voorstellen |
| Frequency LIT bij herstart | 3,97 over laatste 30 dagen (boven 3,5) | Verse creatives vóór herstart, anders start fatigue direct opnieuw |
| CPM SWE video's bij herstart | Video 1 €15,27 en Video 2 €17,07 (boven €15) | Niet herstarten in huidige vorm |

De frequency- en CPM-waarden komen uit het ads-report van vandaag (last 30d) en gelden als startpunt voor een herstart, niet als live signaal.

### 📊 PostHog bevestiging (live)

| Dag | Betaalde sessies (meta/cpc) | Sessies /become-a-distributor | Inzendingen wholesaler_form_submit |
|---|---|---|---|
| 8 sep | 0 | 3 | 0 |
| 9 sep | 2 | 5 | 0 |
| 10 sep | 0 | 1 | 0 |
| 11 sep (tot run) | 0 | 2 | 0 |

De 2 betaalde sessies op 9 september zijn nalopers op oude ad-URL's, geen nieuwe levering. Laatste inzending blijft 4 september. Sitewide verkeer schommelt sterk (554 tot 7.595 sessies per dag) maar dat is organisch en direct verkeer, niet uit Meta.

### 📊 70-20-10 Classificatie

Niet van toepassing: 0 actieve ads, €0,00 dagbudget in levering.

**Referentie voor herstart** (op basis van de 30-daagse cijfers uit het ads-report van 11 september, all-clicks metrics, dus richtlijn en geen hard oordeel):

**70% Core:**
- Video 2 (LIT), goedkoopste inzending €28,75, conversie 3,5%
- Video 1 (LIT) en Statisch 1 (LIT), stabiele inzendingen
- Statisch 2 (SWE), hoogste All Clicks CTR 4,0%

**20% Emerging:**
- Zweedse variant op Video 2 (LIT), SWE heeft nog geen werkende video

**10% Experimental:**
- Nieuwe hook voor Statisch 2 (LIT), klikt goedkoop (€0,20 CPC all) maar converteert 0,7%

**Budget mismatch:** Nee, er is geen budget in levering.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 9 en 10 september. Zolang niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen.

**1. Herstart Wholesaler (LIT) en (SWE)**
- Wholesaler (LIT): van €0,00 naar €100,00 per dag, verdeeld €70,00 Core (Video 1, Video 2, Statisch 1), €20,00 Emerging, €10,00 Experimental
- Wholesaler (SWE): van €0,00 naar €40,00 per dag, alleen Statisch 2 (SWE) en een nieuwe video, zonder Video 1 (SWE) en Video 2 (SWE)
- Reden: LIT leverde 16 inzendingen op €562,14 (€35,13 per inzending), SWE 7 op €507,24 (€72,46 per inzending)
- Verwachte impact: 25 tot 30 inzendingen per maand op €4.200,00 spend bij gelijke conversie

**2. Nieuwe variaties**
- Op Statisch 2 (SWE), All Clicks CTR 4,0%: variatie A met een callout-hook ("Zweedse ballonwinkels: dit is wat jullie missen in jullie assortiment"), statisch beeld. Variatie B met een proof-hook (aantal Europese distributeurs of jaren ervaring), carrousel.
- Op Video 2 (LIT), beste conversie: variatie A als Zweedse vertaling voor SWE. Variatie B met een andere eerste 3 seconden (probleem-hook in plaats van product-hook), zelfde body.
- Alle Engelstalige copy in UK spelling.

**3. Audience aanpassingen**
- LIT: ad sets samenvoegen tot één ad set, frequency 3,97 op een klein publiek wijst op te veel overlap
- SWE: audience verbreden (interesses uitbreiden of lookalike op de 7 inzenders), CPM €12,92 wijst op te smal publiek

**4. Conversie-guard op kill-regels**
- Ads met minimaal 1 PostHog-inzending in de laatste 7 dagen niet automatisch pauzeren op Link CTR alleen. Voorkomt dat Statisch 1 (LIT) op dag 1 na herstart sneuvelt.

**5. Tracking fix vóór herstart**
- Meta telde 19 leads tegenover 33 in PostHog over de laatste campagneperiode. De pixel ondertelt structureel. Eerst het lead-event op /become-a-distributor controleren, anders stuurt Meta op 40% te weinig conversiedata.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

### Log

| Timestamp | Actie | Reden |
|---|---|---|
| 2026-09-11 11:12 | get_campaigns (ACTIVE) op act_567892422940728 | 0 actieve campagnes |
| 2026-09-11 11:12 | get_campaigns (alle) | 7 campagnes, alle PAUSED |
| 2026-09-11 11:12 | get_insights level=ad, 8 t/m 11 sep | 0 rijen |
| 2026-09-11 11:12 | PostHog HogQL: sessies, distributor-pagina, form submits | 0 tot 2 betaalde sessies per dag, 0 inzendingen sinds 4 sep |
| 2026-09-11 11:12 | Geen update_ad calls | Geen actieve ads |
