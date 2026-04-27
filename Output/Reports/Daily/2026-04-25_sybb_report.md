# SYBB Daily Report, 2026-04-25

## 1. Samenvatting

Vijfde volle pauzedag op rij. Op 2026-04-25 nul impressies, nul clicks, nul spend op beide SYBB campagnes (`2026: SYBB` en `2026: SYBB - Kopie`) op account `act_567892422940728`. De "2026: SYBB - Kopie" (120243293329420239) staat sinds 2026-04-20 17:09 op PAUSED, de originele "2026: SYBB" (120239435987290239) sinds 2026-04-19 14:29. Geen statuswijziging sinds het rapport van 2026-04-24. PostHog MCP is voor de zevende rapportdag op rij niet beschikbaar, dus landing page health blijft niet meetbaar.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)
- Geen Google MCPs gebruikt in deze run.

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt | Dagen op pauze (t/m 2026-04-25 23:59) |
|----------|----|----|-------------------|---------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 | 5 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 | 6 |

### Performance gisteren vs voorgaande dagen

Cijfers hieronder komen uit Meta Ads MCP `get_insights` met `time_breakdown=day` over periode 2026-04-18 t/m 2026-04-25, gecombineerd over beide campagnes. Op 2026-04-19 liepen origineel + Kopie tegelijk; die kolom is de optelling van beide.

| Metric | 2026-04-25 | 2026-04-24 | 2026-04-23 | 2026-04-22 | 2026-04-21 | 2026-04-20 | 2026-04-19 | 2026-04-18 | 7d gem. (run-dagen) |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------------------|
| Spend | €0,00 | €0,00 | €0,00 | €0,00 | €0,00 | €77,85 | €90,38 | €94,64 | €87,62 per run-dag |
| Impressions | 0 | 0 | 0 | 0 | 0 | 4.287 | 6.084 | 6.454 | 5.608 |
| Clicks (all) | 0 | 0 | 0 | 0 | 0 | 119 | 137 | 153 | 136 |
| Link clicks | 0 | 0 | 0 | 0 | 0 | 75 | 86 | 90 | 84 |
| CTR | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 2,78% | 2,21-2,28% | 2,37% | ~2,42% |
| CPC (all) | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | €0,65 | €0,66 | €0,62 | €0,64 |
| Frequency | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 1,34 | 1,21-1,35 | 1,34 | ~1,31 |
| Landing Page Views (Meta pixel) | 0 | 0 | 0 | 0 | 0 | 63 | 71 | 78 | 71 |
| Initiate Checkout | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 7 | 5,0 |

*7d gemiddelde berekend over de 3 daadwerkelijke run-dagen binnen het venster 2026-04-18 t/m 2026-04-24 (04-18, 04-19, 04-20). 04-17 valt nu buiten het 7d-venster, dus telt niet meer mee. Pauzedagen niet meegerekend in het gemiddelde.*

**Trend:** 120+ uur zonder enige Meta-spend op SYBB. De "2026: SYBB - Kopie" zit nu 5 volle dagen op pauze, de originele "2026: SYBB" 6 dagen. Het 7d run-dagen gemiddelde is gekrompen van 4 run-dagen (in het 04-24 rapport) naar 3 run-dagen, omdat 04-17 buiten het 7-daagse venster valt. Vanaf morgen (2026-04-26) valt 04-18 buiten het venster en blijven slechts 04-19 en 04-20 over als referentie. Vanaf 2026-04-28 is er geen run-dag meer in het 7d-venster en wordt dit aggregaat onbruikbaar.

### Ad variant performance

Niet van toepassing voor 2026-04-25. Geen ad-level data omdat geen enkele ad heeft gelopen. De laatste ad-level snapshot (uit het 04-21 rapport, gebaseerd op 04-19 en 04-20 data) blijft het laatste signaal: H12 (b3_cta5) leidt op CTR/CPC, H13 (b3_cta5) onderpresteert met CPC > €0,90, H11 (b3_cta5) zit in het midden. Sample is 2 run-dagen, dus directioneel, niet statistisch.

## 3. Landing Page Health

**Niet beschikbaar.** PostHog MCP is niet ingeladen in deze sessie. Geen pageviews, bounce rate, scroll depth, session duration, CTA click rate of session recordings voor `startyourballoonbusiness.com` op te halen.

| Metric | Target | Status |
|--------|--------|--------|
| Bounce Rate | <55% | geen data |
| Avg Session Duration | >90s | geen data |
| Scroll 25% | >80% | geen data |
| Scroll 50% | >60% | geen data |
| Scroll 75% | >40% | geen data |
| Scroll 100% | >20% | geen data |
| CTA Click Rate | >4% | geen data |

Bij werkende PostHog zou ook zonder Meta-instroom de baseline van direct + organisch verkeer zichtbaar zijn. Dat ontbreekt nu zeven rapportdagen op rij. De cross-reference tussen ad x landing page (de kern van deze SKILL) is daarmee structureel niet uitvoerbaar.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-25. Geen Meta instroom, geen PostHog data. De referentie blijft de aggregaat over de 5 run-dagen (04-16 t/m 04-20), die in het rapport van 04-23/04-24 al is samengevat:

Link clicks (329) > Meta pixel LPV (275, 83,6%) > Initiate Checkout (15, 4,6% van LC / 5,5% van LPV)

**Observatie:** geen verandering t.o.v. gisteren. De relevantie van deze cijfers neemt af naarmate de pauze langer duurt; bij heractivering moeten de eerste 3 dagen opnieuw gemeten worden om te bevestigen dat het LPV>IC pad nog rond 5-6% ligt of gedaald is.

## 5. Rode Vlaggen

- **Vijfde dag op rij zonder live SYBB campagne.** 2026-04-21, 04-22, 04-23, 04-24 en nu 04-25 allemaal nul spend. "2026: SYBB - Kopie" niet heractiveerd sinds 2026-04-20 17:09. De stilstand is nu langer dan de gehele run-periode (5 pauzedagen vs 5 run-dagen). Vanaf vandaag heeft de pauze het run-venster in dagen geëvenaard; vanaf morgen gaat de pauze het run-venster overtreffen. Bij heractivering vrijwel zeker een nieuwe learning fase van 2 tot 4 dagen.
- **PostHog MCP zeven rapportdagen op rij offline.** 2026-04-19 t/m 2026-04-25. Geen tool-config wijziging zichtbaar in deferred tool lijst. Dit is geen incident meer maar een vaste state. Tool moet weer beschikbaar gemaakt worden voor de SKILL ueberhaupt nog werk levert.
- **7d run-dagen gemiddelde gekrompen van 4 naar 3.** 04-17 valt nu buiten het 7d-venster. Vanaf 2026-04-26 valt 04-18 ook buiten, dan zijn er nog 2 run-dagen over. Vanaf 2026-04-28 is het 7d-aggregaat leeg. Dit rapport wordt elke dag minder informatief zonder nieuwe data.
- **Beslissing rond H12 vs H13 nu 144+ uur oud.** Hypothese (H12 wint, H13 onder par) ongewijzigd op basis van 2 run-dagen. Bij hervatting met dezelfde line-up start je met klein-sample assumpties; bij vertraging van een week of meer is dit signaal te oud om op te leunen.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag definitief: heractiveren, killen, of rebuild + datum vastleggen.**
   - **Wat:** Robin neemt vandaag de knoop door en legt de keuze schriftelijk vast in een beslissingslog (markdown in `Output/Reports/`). Bij heractivering: zet H13 op PAUSED op ad-niveau, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen om de re-learning fase te respecteren. Bij rebuild: leg launchdatum iteratie 2 vast (concreet, niet "binnenkort") en koppel daar een lijst nieuwe creatives aan. Bij kill: noteer expliciet "campagne stopgezet, geen iteratie 2 gepland" met reden.
   - **Waarom:** vijfde pauzedag op rij. De pauzeperiode is nu gelijk aan de actieve runperiode. Elke extra dag drukt het 7d-venster verder leeg en maakt re-learning kostbaarder. Zonder schriftelijke beslissing groeit het aantal "dagen onbeslist" sneller dan het aantal dagen data.
   - **Hoe:** Meta Ads Manager > campagne "2026: SYBB - Kopie" (120243293329420239) activeren OF beslissingslog `Output/Reports/sybb_decision_log_2026-04-25.md` aanmaken met datum, gekozen pad en reden. Als heractivering: eerst H13 op ad-niveau uitzetten voor activering campagne.
   - **Verwachte impact:** bij heractivering binnen 3 tot 4 dagen terug naar €50 tot €80 spend per dag met 2 tot 5 IC's per dag. Eerste 1 tot 2 dagen 10-20% hogere CPC verwacht door re-learning. Bij rebuild: 1 tot 2 weken voorbereidingstijd voor iteratie 2 launch.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Herstel PostHog MCP toegang (zeven rapportdagen op rij offline).**
   - **Wat:** PostHog MCP server reactiveren of opnieuw configureren in de Claude Code setup zodat `posthog_*` tools weer in de deferred tool lijst verschijnen.
   - **Waarom:** zeven dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Het centrale idee van de SKILL (Meta Ads x PostHog cross-referencing) werkt niet zonder PostHog. Bij heractivering wil je PostHog dag-1 al werkend hebben, niet pas dag-3 als de eerste resultaten binnenkomen, anders mis je opnieuw de cross-reference op de eerste run.
   - **Hoe:** check `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Verifieer API key uit PostHog project "Default project" (mogelijk verlopen token of project-renamed). Test na restart met een eenvoudige pageviews-query op startyourballoonbusiness.com over de laatste 24 uur.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run. Geen directe campagne-impact, wel hersteld diagnostisch vermogen.
   - **Escalatie:** Oranje, tooling ingreep.

3. **Documenteer de 5-run-dagen baseline NU, voordat het 7d-venster leeg loopt.**
   - **Wat:** korte markdown in `Output/Reports/` (bv. `sybb_iter1_baseline.md`) met aggregaten over de 5 run-dagen (04-16 t/m 04-20): totale spend, clicks, LPVs, IC's, CTR, CPC, LPV>IC rate. Per hook variant (H11, H12, H13, H14, H15 als gelopen) de directionele CTR/CPC/IC splitsing op basis van het 04-21 rapport. Eindig met 1 expliciete hypothese voor iteratie 2.
   - **Waarom:** dit was punt 3 in het rapport van gisteren en is nog niet gebeurd. Het 7d-venster verliest morgen alweer een run-dag (04-18). Vanaf 04-28 is er geen referentiedata meer in het rolling venster. Als deze samenvatting niet vandaag wordt vastgelegd, moet bij iteratie 2 of heractivering het hele 5-run-dagen venster opnieuw uit oudere reports getrokken worden, met meer kans op fouten.
   - **Hoe:** markdown per hook (H11, H12, H13, H14, H15 indien gelopen) met CTR, CPC, LPV, IC. Eindig met expliciete hypothese voor iteratie 2: welke hook angle doorontwikkelen, welke creative elementen behouden, welk CTA format (cta5) blijft, welk audience-vlak verbreden of vernauwen.
   - **Verwachte impact:** geen directe KPI impact. Wel: volgende launch start met geschreven hypothese in plaats van vanaf nul of "uit het hoofd". Voorkomt dat 5 run-dagen aan data effectief weggegooid worden.
   - **Escalatie:** Groen, geen goedkeuring nodig.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-25_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers; alle Meta-getallen direct uit `get_insights` time_breakdown=day, range 2026-04-18 t/m 2026-04-25.
