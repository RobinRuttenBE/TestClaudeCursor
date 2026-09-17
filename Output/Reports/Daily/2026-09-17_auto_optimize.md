## Auto-Optimize Rapport, 17 september 2026

Run: 17 september 2026, ochtend (UTC). Bronnen: Pipeboard Meta Ads (directe JSON-RPC route, 1 call) en PostHog project STX EU 149694 (directe REST-route, 2 HogQL queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Google Sheet geschreven. Primair account: act_567892422940728 (Sempertex Ad Account). Het tweede account act_607231713057715 uit het command bestaat niet in de Pipeboard-koppeling (act_1489853856181844 AmbitionAvenue is leeg).

### Databeschikbaarheid

**Meta was niet live bereikbaar.** De MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` vragen autorisatie (niet mogelijk in deze non-interactieve sessie). De directe route kreeg op de allereerste call (`get_insights`, level ad, last_3d) meteen `weekly_limit_exceeded`: 30 van 30 wekelijkse executies gebruikt, plan free, trial credits 0, reset_date 21 september 2026 00:00 UTC. Geen verdere Meta-calls gedaan, geen `update_ad` mogelijk.

**Campagnestatus** komt daarom uit het laatste live Meta-extract van 16 september 09:03: alle 7 campagnes PAUSED, de twee Wholesaler Campagnes (LIT en SWE) sinds 4 september 11:50, `2026: SYBB` sinds 19 april. Meta gaf toen nul rijen voor 9 t/m 15 september.

**PostHog bevestigt live dat er ook 14 t/m 16 september niets geleverd is:**

| Dag | Betaalde sessies (Meta UTM) | Distributeurspagina views | Formulierstarts | Inzendingen |
|---|---|---|---|---|
| 10 sep | 0 | 1 | 0 | 0 |
| 11 sep | 0 | 6 | 0 | 0 |
| 12 sep | 0 | 2 | 0 | 0 |
| 13 sep | 0 | 0 | 0 | 0 |
| 14 sep | 0 | 1 | 0 | 0 |
| 15 sep | 0 | 2 | 0 | 0 |
| 16 sep | 0 | 9 | 0 | 0 |

Laatste sessies met een Meta-UTM: 1 op 7 september (0 pageviews, nalooper) en 2 op 9 september (oude ad-URL's). Sinds 10 september nul. Laatste betaalde inzending blijft 4 september. Dit is de veertiende dag zonder levering.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn 0 actieve ads, dus de kill-regels (Link CTR < 0,8% bij ≥ 1.000 impressions, CPC (link) > €1,50 bij ≥ 500 link clicks) hadden niets om op te draaien. Over de laatste 3 dagen (14 t/m 16 september): €0,00 spend, 0 impressions, 0 link clicks.

| Ad | Reden | Was | Nu | Performance |
|---|---|---|---|---|
| geen | n.v.t. | n.v.t. | n.v.t. | 0 imp, 0 link clicks, €0,00 |

**Totaal gepauzeerd: 0 ads** (0 van 0 actieve ads, 50%-grens niet van toepassing)

Log: 2026-09-17 ochtend UTC, geen `update_ad` calls, reden: geen levering en Meta op weeklimiet.

### ⚠️ Waarschuwingen

Geen actieve levering, dus geen verse frequency- of CPM-signalen. Onderstaande punten zijn de bekende 30d-waarden (extract 16 september, venster 17 augustus t/m 15 september) die bij een herstart direct weer relevant zijn:

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT) | Creative fatigue | Frequency 3,97 | Verse creatives vóór herstart |
| Video 2 (SWE) | Dure reach | CPM €17,07, CPC (all) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, geen conversie | CPM €15,27, 0 inzendingen op 113 sessies | Definitief uit |
| Wholesaler (SWE) | Dure reach | CPM €12,92 | Audience verbreden bij herstart |
| Pipeboard | Weeklimiet vol | 30 van 30, reset 21 sep | Eén gedeeld extract per dag (voorstel 6) |
| Funnel /become-a-distributor | Formulierlek | 24,6% van starters komt door (134 starts, 33 inzendingen, 21 fouten) | Fix vóór herstart (voorstel 5) |

### 📊 70-20-10 Classificatie

Er zijn geen actieve ads, dus huidig budget per categorie is €0,00/dag (0% van €0,00). De classificatie hieronder is de herstart-indeling op basis van 30d-data (link-metrics op campagneniveau uit het extract van 6 september: LIT Link CTR 1,0% en CPC (link) €0,64, SWE Link CTR 1,8% en CPC (link) €0,73; conversie per ad uit PostHog). Volgens de TODO in het command gelden de link-drempels als richtlijn, niet als hard oordeel, en er worden geen budget-shifts uitgevoerd.

**70% Core (voorgesteld €98,00/dag van €140,00):**
- Video 2 (LIT), beste kosten per inzending €28,75, conversie 3,5% van sessie naar inzending
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), 3,0% conversie, maar Link CTR mechanisch onder 0,8% (0,5% op 4 september); alleen herstarten met conversie-guard (voorstel 4)
- Statisch 2 (SWE), beste CTR van alle ads (All Clicks CTR 4,0%), €32,03 per inzending

**20% Emerging (voorgesteld €28,00/dag):**
- Zweedse variant van Video 2 (LIT), nog niet gemaakt (voorstel 2)

**10% Experimental (voorgesteld €14,00/dag):**
- Statisch 2 (LIT) met nieuwe Vraag-hook: goedkoopste clicks (CPC (all) €0,20) maar 0,7% conversie en €63,63 per inzending; nieuwe hook testen

**Niet herstarten:** Video 1 (SWE) en Video 2 (SWE).

**Budget mismatch:** Nee. Er loopt geen budget, dus er is niets te herverdelen. Zodra de herstart is goedgekeurd, geldt bovenstaande verdeling als startpunt.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 16 september. Geen enkel voorstel is uitgevoerd.

**1. Budget herverdeling / herstart**
- Wholesaler (LIT): van €0,00/dag naar €100,00/dag, verdeeld 70-20-10 over Video 2 (LIT), Video 1 (LIT), Statisch 1 (LIT), Statisch 2 (LIT) met nieuwe hook, plus één nieuwe creative
- Wholesaler (SWE): van €0,00/dag naar €40,00/dag, alleen Statisch 2 (SWE) plus één nieuwe creative, beide SWE-video's uit
- Reden: LIT levert inzendingen voor €35,13, SWE voor €63,41; de LIT-set is bewezen, de SWE-video's niet
- Verwachte impact: circa 4 inzendingen per dag bij €30,00 tot €35,00 per inzending, mits het formulierlek (voorstel 5) eerst dicht is

**2. Nieuwe variaties**
- Op Statisch 2 (SWE) (All Clicks CTR 4,0%): variatie A met Vraag-hook, variatie B met Sociaal-bewijs-hook (aantal Europese distributeurs), zelfde statische format
- Op Video 2 (LIT) (€28,75 per inzending): variatie A als Zweedse vertaling voor SWE (Emerging), variatie B met andere eerste 3 seconden (Belofte-hook) voor LIT
- Op Statisch 2 (LIT): één nieuwe Vraag-hook (Experimental)

**3. Audience aanpassingen**
- LIT ad sets samenvoegen (frequency 3,97 duidt op overlap en verzadiging)
- Audience Network in alle ad sets uitsluiten
- SWE audience verbreden (CPM €12,92 tegenover €6,18 in LIT)
- Statisch 1 (LIT) naar 25-65 en desktop uitsluiten (lage Link CTR zat in Facebook desktop)

**4. Conversie-guard op de kill-regels**
- Ad niet pauzeren bij minimaal 1 PostHog-inzending onder €40,00 in de laatste 3 dagen, ook als Link CTR onder 0,8% zit
- Reden: Statisch 1 (LIT) triggert anders op dag 1 na herstart terwijl het een top-3 converter is

**5. Tracking en funnel fix vóór herstart**
- Meta pixel telt 19 leads tegenover 35 inzendingen in PostHog
- 102 van 137 formulierstarters haken af, 21 formulierfouten in 30 dagen

**6. Eén gedeeld Meta-extract per dag**
- Ads-report haalt 's ochtends één extract op en cachet dat lokaal; SYBB en auto-optimize lezen dat bestand
- Reden: de gratis Pipeboard-limiet van 30 calls per week was deze week op woensdag al vol, vandaag faalde de eerste call opnieuw. Zonder dit kan auto-optimize na herstart geen kill-regels draaien op de dagen dat het ertoe doet.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Eerstvolgende run met live Meta-data: op of na maandag 21 september, tenzij Pipeboard eerder naar Pro gaat of je de MCP opnieuw autoriseert via /mcp in een interactieve sessie.
