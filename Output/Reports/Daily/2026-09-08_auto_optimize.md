## Auto-Optimize Rapport, 8 september 2026

**Run:** 8 september 2026, ochtend. Venster: last_3d (5 t/m 7 september, plus de eerste uren van 8 september).
**Databronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, de MCP vroeg om authenticatie) en PostHog project STX EU 149694 (directe REST route, de MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet in de Pipeboard-koppeling.

### Status van het account

Alle 7 campagnes staan op PAUSED. Meta levert niets en registreert 0 impressions en 0 spend in de laatste 3 dagen (`get_insights` op ad-niveau geeft een lege dataset).

| Campagne | Status | Ads | Laatste wijziging |
|---|---|---|---|
| Wholesaler Campagne (LIT) | PAUSED | 4 (Video 1, Video 2, Statisch 1, Statisch 2) | 4 sep 11:25 tot 11:52 |
| Wholesaler Campagne (SWE) | PAUSED | 4 (Video 1, Video 2, Statisch 1, Statisch 2) | 4 sep 11:51 tot 11:52 |
| 2026: SYBB | PAUSED | 27 hook-ads (H11 t/m H15) | 19 april |
| 2026: SYBB - Kopie | PAUSED | 17 hook-ads | 28 augustus |
| Nozzle Up (3 campagnes) | PAUSED | 1 ad | 21 september 2025 |

**PostHog bevestigt de stilstand.** Sinds 6 september zijn er 0 sessies met utm_medium=cpc. De distributeurspagina kreeg 4 organische sessies op 6 september en 3 op 7 september. De laatste wholesaler_form_submit was op 4 september (1 inzending). Van 5 t/m 8 september: 0 inzendingen.

### Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn 0 actieve ads, dus de kill-regels (Link CTR < 0,8% bij 1.000+ impressions, CPC (link) > €1,50 bij 500+ link clicks) hadden geen data om op te draaien. Er zijn geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads**

### Waarschuwingen

Geen. Zonder levering zijn frequency, CPM en Link CTR-trend niet meetbaar.

Wel een herinnering uit de run van 7 september die bij herstart direct relevant wordt: Statisch 1 (LIT) triggerde op de laatste ochtend van 4 september mechanisch de Link CTR-regel (0,2% bij 1.830 impressions), terwijl het over 30 dagen een van de drie goedkoopste converters is. Zonder conversie-guard pauzeert auto-optimize deze ad op de eerste volle dag na herstart.

### 70-20-10 Classificatie

Niet van toepassing. Er is 0 actief budget, dus er is geen verdeling om te toetsen.

Ter referentie, de laatste 30-daagse stand (9 augustus t/m 7 september, uit het ads-rapport van vandaag):

**Core (bewezen):**
- Video 2 (LIT), €28,75 per inzending, beste converter
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), top 3 goedkoopste converters

**Emerging (potentieel):**
- Statisch 2 (SWE), beste All Clicks CTR van het account (4,0%)

**Niet herstarten:**
- Video 1 (SWE), 0 inzendingen op 113 sessies, CPM €15,27
- Video 2 (SWE), €63,50 per inzending, CPM €17,07
- Statisch 2 (LIT), goedkoopste clicks (€0,20 all) maar 2 inzendingen op 290 sessies

**Budget mismatch:** Nee (geen actief budget).

### Voorstellen (wacht op goedkeuring)

Ongewijzigd sinds 7 september. Er is geen nieuwe data die de voorstellen verandert.

**1. Herstart Wholesaler (LIT) op €100,00 per dag**
- Verdeling 70-20-10: Video 2 en Video 1 samen €50,00, Statisch 1 €20,00, Statisch 2 €20,00, één nieuwe creative €10,00
- Reden: 16 inzendingen in 30 dagen op €562,14 spend, €35,13 per inzending
- Verwachte impact: 25 tot 30 inzendingen per maand bij gelijke conversie, mits de creative fatigue (frequency 3,97) wordt doorbroken met de nieuwe creative

**2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag**
- Alleen Statisch 2 (SWE) plus één nieuwe creative, beide video's blijven uit
- Reden: SWE kostte €72,46 per inzending, de video's leverden bijna niets

**3. Nieuwe variaties**
- Op Statisch 2 (SWE), hoogste All Clicks CTR (4,0%): variatie A met een "Hidden Insight" hook (marge-cijfer voor wholesalers), variatie B met een "Proof" hook (aantal Europese distributeurs)
- Op Video 2 (LIT), beste converter: variatie A als 15s cut met de CTA in de eerste 3 seconden, variatie B met een carousel van dezelfde productshots

**4. Conversie-guard op de kill-regels**
- Pauzeer een ad niet automatisch als PostHog minimaal 1 wholesaler_form_submit toont bij minder dan €40,00 spend in het venster
- Reden: voorkomt dat Statisch 1 (LIT) op dag 1 na herstart wordt gepauzeerd

**5. Audience aanpassingen**
- LIT: de ad sets samenvoegen zodat Meta het budget zelf verdeelt
- SWE: audience verbreden, CPM lag boven €12,00 en frequency op 3,29

**6. Tracking fix vóór herstart**
- Meta telde 19 leads tegenover 33 inzendingen in PostHog. Pixel-event op de bedankpagina controleren voordat er opnieuw budget loopt

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

### Log

| Tijdstip | Actie | Resultaat |
|---|---|---|
| 8 sep, ochtend | get_campaigns act_567892422940728 | 7 campagnes, alle PAUSED |
| 8 sep, ochtend | get_insights last_3d, ad-niveau | lege dataset, 0 spend |
| 8 sep, ochtend | get_ads act_567892422940728 | 57 ads, alle PAUSED |
| 8 sep, ochtend | PostHog sessions en wholesaler_form_submit 6 t/m 8 sep | 0 cpc-sessies, 0 inzendingen |
| 8 sep, ochtend | update_ad | niet aangeroepen |
