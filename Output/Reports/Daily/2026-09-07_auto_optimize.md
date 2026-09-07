## Auto-Optimize Rapport, 7 september 2026

**Run:** 2026-09-07, handmatig via /ads-auto-optimize
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, de MCP vroeg om authenticatie), PostHog project STX EU via REST (de PostHog MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Account:** act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet in deze Pipeboard-koppeling (permission_denied, alleen act_567892422940728 en act_1489853856181844 zijn toegestaan).

### Status Meta Ads

- Actieve campagnes: **0**. Beide Wholesaler campagnes (LIT en SWE) staan sinds 4 september 11:50 op PAUSED.
- Alle 8 ads (4 LIT, 4 SWE) hebben status PAUSED en effective_status PAUSED.
- Spend per dag: 4 september €55,71 (tot de pauze), 5, 6 en 7 september €0,00. Meta levert dus niets meer.
- De `last_3d` preset (4 t/m 6 september) bevat uitsluitend de laatste ochtend van 4 september.

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd.** Er zijn geen actieve ads om kill-regels op toe te passen. Alles staat al op PAUSED sinds 4 september. Geen `update_ad` calls gedaan.

Ter informatie, de kill-regels toegepast op de `last_3d` data (alleen 4 september, dus onvolledige dag):

| Ad | Impressions | Link clicks | Link CTR | CPC (link) | Kill-regel | Actie |
|---|---|---|---|---|---|---|
| Statisch 1 (LIT) | 1.830 | 3 | 0,2% | €2,55 | Link CTR < 0,8% bij ≥ 1.000 imp: **ja** | Geen, staat al op PAUSED |
| Statisch 2 (LIT) | 1.356 | 10 | 0,7% | €0,63 | Link CTR < 0,8% bij ≥ 1.000 imp: **ja** | Geen, staat al op PAUSED |
| Video 1 (LIT) | 950 | 8 | 0,8% | €0,92 | Te weinig impressions | Overgeslagen |
| Video 2 (LIT) | 909 | 2 | 0,2% | €4,00 | Te weinig impressions | Overgeslagen |
| Statisch 2 (SWE) | 705 | 13 | 1,8% | €0,51 | Te weinig impressions | Overgeslagen |
| Video 2 (SWE) | 480 | 8 | 1,7% | €1,00 | Te weinig impressions | Overgeslagen |
| Statisch 1 (SWE) | 433 | 4 | 0,9% | €1,57 | Te weinig impressions | Overgeslagen |
| Video 1 (SWE) | 387 | 2 | 0,5% | €2,73 | Te weinig impressions | Overgeslagen |

Geen enkele ad haalde 500 link clicks, dus de CPC (link)-regel was nergens van toepassing. Let op: Statisch 1 (LIT) triggert mechanisch de Link CTR-regel, maar had over 30 dagen €36,06 per inzending en de hoogste sessie-naar-inzending ratio. Zie voorstel 4.

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Video 2 (SWE) | Dure reach | CPM €16,67 (3d), €17,07 (30d) | Niet herstarten zonder nieuwe audience |
| Statisch 1 (SWE) | Dure reach, net onder drempel | CPM €14,53 (3d) | Audience verbreden bij herstart |
| Video 1 (SWE) | Dure reach, net onder drempel | CPM €14,08 (3d), €15,27 (30d) | Definitief uit |
| Wholesaler (LIT) | Creative fatigue (30d) | Frequency 3,97 | Nieuwe creative voor herstart |

Frequency in de 3-daagse data ligt overal onder 1,6, maar dat komt door de korte periode. Het 30-daagse beeld uit het ads-rapport van vanochtend blijft leidend.

### 📈 PostHog bevestiging (live)

Betaalde sessies op /become-a-distributor (utm_medium=paid of utm_source=facebook):

| Dag | Sessies | Bounces | Gem. duur | Form starts | Inzendingen |
|---|---|---|---|---|---|
| 4 sep | 58 | 22 | 39s | 4 | 1 |
| 5 sep | 0 | 0 | 0s | 0 | 0 |
| 6 sep | 2 | 0 | 6s | 0 | 0 |
| 7 sep (tot nu) | 0 | 0 | 0s | 0 | 0 |

De twee sessies van 6 september kwamen allebei via instagram.com binnen op de Video 1 (SWE) UTM (04:53 UTC, 11 seconden, en 06:31 UTC, 0 seconden). Meta registreert 0 impressions en 0 spend op die dag, dus dit is een opgeslagen of gedeelde ad-post en geen levering. Geen actie nodig in Ads Manager. Het eerder gevraagde handmatige check-punt van 6 september is hiermee afgehandeld.

### 📊 70-20-10 Classificatie

Huidig budget: **€0,00 per dag** in alle categorieën, want er draait niets. De classificatie hieronder is de herstart-indeling op basis van de 30-daagse data (8 augustus t/m 6 september) uit het ads-rapport van vanochtend. De drempels zijn richtlijn, nog niet gekalibreerd op link metrics.

**70% Core (huidig 0% van totaal):**
- Video 2 (LIT), €28,75 per inzending, beste van de set
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), €36,06 per inzending ondanks lage Link CTR
- Statisch 2 (SWE), Link CTR 4,0% (30d), 1,8% (3d), CPC (link) €0,51 (3d)

**20% Emerging (huidig 0% van totaal):**
- Statisch 2 (LIT), CPC €0,20 (30d), CPC (link) €0,63 (3d), Link CTR 0,7% (3d), conversie nog niet bewezen
- Statisch 1 (SWE), Link CTR 0,9% (3d), CPM te hoog voor Core

**10% Experimental (huidig 0% van totaal):**
- Geen nieuwe ads. Bij herstart hoort hier één nieuwe creative per markt (voorstel 3).

**Niet herstarten:**
- Video 1 (SWE), 0 inzendingen op 113 sessies (30d)
- Video 2 (SWE), CPM €17,07 en CPC €0,69 (30d), ondanks 1 Meta-lead op 4 september

**Budget mismatch:** Nee, er is geen budget om te verdelen. Wel is het hele budget al 3 dagen op nul terwijl de LIT-set bewezen inzendingen onder €40 opleverde.

### 💡 Voorstellen (wacht op goedkeuring)

De vijf voorstellen van 3 september staan nog open. Meta is vandaag weer bereikbaar, dus voorstel 0 van 6 september (Meta-data herstellen) is niet meer urgent, maar de weeklimiet van het Pipeboard Free plan komt later deze week waarschijnlijk terug.

**1. Herstart Wholesaler (LIT) op €100,00 per dag, 70-20-10 verdeling**
- Video 2 (LIT): €30,00 per dag
- Video 1 (LIT): €30,00 per dag
- Statisch 1 (LIT): €20,00 per dag
- Statisch 2 (LIT): €10,00 per dag (Emerging)
- Nieuwe creative LIT: €10,00 per dag (Experimental)
- Reden: LIT leverde 16 inzendingen op €562,14 (30d). Frequency 3,97 vraagt om verse creative naast de winnaars.
- Verwachte impact: 2 tot 3 inzendingen per dag bij gelijke conversie, tegen €35,00 per inzending.

**2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag**
- Statisch 2 (SWE): €30,00 per dag (enige SWE-ad met Core-cijfers)
- Nieuwe creative SWE: €10,00 per dag
- Video 1 (SWE), Video 2 (SWE) en Statisch 1 (SWE) blijven PAUSED
- Reden: SWE kostte €72,46 per inzending (30d), tweemaal LIT. Alleen Statisch 2 verdient budget.
- Verwachte impact: CPM omlaag door de dure video-ads uit de mix te halen.

**3. Nieuwe variaties op de winnende hooks**
- Gebaseerd op Statisch 2 (SWE), Link CTR 4,0% (30d): variatie A als 6 seconden video van dezelfde visual met tekst-overlay, variatie B met CTA "Request your wholesale price list" in plaats van de huidige CTA.
- Gebaseerd op Video 2 (LIT), beste kosten per inzending: variatie A met een andere eerste 3 seconden (proof-hook: certificering en Europese voorraad), variatie B als statisch frame uit de video met dezelfde koptekst.
- Reden: 70-20-10 vraagt om 10% experiment, en frequency 3,97 op LIT betekent dat de huidige creatives verzadigd raken.

**4. Conversie-guard op de kill-regels**
- Pauzeer een lead-ad niet op Link CTR alleen als hij in dezelfde periode minimaal 1 PostHog-inzending had onder €40,00 per inzending.
- Reden: Statisch 1 (LIT) triggert de Link CTR-regel (0,6% over 30d, 0,2% op 4 september) maar is een van de drie goedkoopste converters. Zonder guard pauzeert auto-optimize hem op de eerste volle dag na herstart.

**5. Audience aanpassingen**
- LIT: de vier losse ad sets samenvoegen tot één ad set met alle actieve creatives, zodat Meta het budget zelf naar de winnaar stuurt en de frequency per persoon zakt.
- SWE: audience verbreden (leeftijd en interesses) om de CPM van €13 tot €17 richting de LIT-CPM van €6 te brengen.
- Reden: LIT frequency 3,97 bij 3.174 bereik per dag; SWE CPM structureel boven de €15-drempel.

**6. Tracking fix vóór herstart**
- Meta telde 19 leads, PostHog 33 inzendingen (30d). Meta pixel op /become-a-distributor controleren of Conversions API koppelen, anders optimaliseert Meta op de helft van de echte conversies.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

*Log automatische acties: 2026-09-07, 0 acties, 0 actieve ads, geen update_ad calls uitgevoerd.*
