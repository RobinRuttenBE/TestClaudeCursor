# SYBB Daily Report, 2026-04-27

## 1. Samenvatting

Zevende volle pauzedag op rij voor de SYBB ads. Op 2026-04-27 nul impressies, nul clicks, nul spend op zowel `2026: SYBB` (120239435987290239) als `2026: SYBB - Kopie` (120243293329420239) op account `act_567892422940728`. De Kopie staat sinds 2026-04-20 17:09 op PAUSED, het origineel sinds 2026-04-19 14:29. De pauze (7 dagen) overstijgt de feitelijke runperiode (5 run-dagen) nu met 2 dagen. Het 7d-venster (04-21 t/m 04-27) bevat voor het eerst nul run-dagen, dus de baseline-tabel uit eerdere rapporten is vandaag onbruikbaar geworden, exact zoals voorspeld in het 04-26 rapport. PostHog MCP is voor de negende rapportdag op rij niet beschikbaar.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)
- Geen Google MCPs gebruikt in deze run, geen schrijfactie naar de Meta Ads Tracker Google Sheet

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt | Volle pauzedagen t/m 2026-04-27 23:59 |
|----------|----|--------|-------------------|---------------------------------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 | 7 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 | 8 |

Geen status- of update-wijziging sinds gisteren. Geen handmatige ingreep in Meta Ads Manager in de afgelopen 24 uur.

### Performance gisteren

| Metric | 2026-04-27 | 7d gem. (run-dagen in venster 04-21 t/m 04-27) | Trend |
|--------|------------|------------------------------------------------|-------|
| Spend | €0,00 | geen run-dagen in venster | n.v.t. |
| Impressions | 0 | geen run-dagen in venster | n.v.t. |
| Clicks (all) | 0 | geen run-dagen in venster | n.v.t. |
| Link clicks | 0 | geen run-dagen in venster | n.v.t. |
| CTR | n.v.t. | geen run-dagen in venster | n.v.t. |
| CPC (all) | n.v.t. | geen run-dagen in venster | n.v.t. |
| Frequency | n.v.t. | geen run-dagen in venster | n.v.t. |
| Landing Page Views (Meta pixel) | 0 | geen run-dagen in venster | n.v.t. |
| Initiate Checkout | 0 | geen run-dagen in venster | n.v.t. |

### 7d window aggregaat (2026-04-21 t/m 2026-04-27)

`get_insights` op campagne-niveau met `time_breakdown=day` over 04-21 t/m 04-27 retourneert lege metrics-segmenten voor elke dag op beide campagnes. Geen run-dag in dit venster. De aggregaat-tabel uit eerdere rapporten is daarmee leeg en wordt vanaf vandaag tot heractivering niet meer getoond.

**Laatste run-dag aggregaat (5 run-dagen 04-16 t/m 04-20, frozen baseline):** €322,xx spend in totaal, ~329 link clicks, ~275 LPV (Meta pixel), 15 IC, CTR ~2,5%, CPC ~€0,66, LPV>IC rate ~5,5%. Dit is nu de enige beschikbare baseline en is vandaag 7 dagen oud.

**Trend:** 168+ uur zonder Meta-spend op SYBB. Zoals gewaarschuwd in het 04-26 rapport: vanaf vandaag is het 7d-aggregaat structureel leeg en levert dit deel van het rapport tot heractivering geen nieuw signaal op. Re-learning verwachting bij heractivering blijft 2 tot 4 dagen met 10-20% verhoogde CPC in dag 1-2.

### Ad variant performance

Niet van toepassing voor 2026-04-27. Geen ad-level data, geen enkele ad heeft gelopen. De laatste ad-level snapshot blijft het signaal uit het 04-21 rapport, gebaseerd op 04-19 en 04-20: H12 (b3_cta5) leidt op CTR/CPC, H13 (b3_cta5) onderpresteert (CPC > €0,90), H11 (b3_cta5) zit ertussenin. Dit signaal is nu 7 dagen oud, gebaseerd op 2 run-dagen, en directioneel.

## 3. Landing Page Health

**Niet beschikbaar.** PostHog MCP is niet ingeladen in deze sessie. Geen pageviews, bounce rate, scroll depth, session duration, CTA click rate of session recordings voor `startyourballoonbusiness.com` op te halen. Negende rapportdag op rij zonder PostHog data (sinds 2026-04-19).

| Metric | Target | Status |
|--------|--------|--------|
| Bounce Rate | <55% | geen data |
| Avg Session Duration | >90s | geen data |
| Scroll 25% | >80% | geen data |
| Scroll 50% | >60% | geen data |
| Scroll 75% | >40% | geen data |
| Scroll 100% | >20% | geen data |
| CTA Click Rate | >4% | geen data |

Bij werkende PostHog zou ook zonder Meta-instroom een baseline van direct + organisch + email verkeer zichtbaar zijn. Dat ontbreekt nu negen rapportdagen op rij. De cross-reference tussen ad x landing page (kern van deze SKILL) is daarmee structureel niet uitvoerbaar tot de tool weer beschikbaar is.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-27. Geen Meta instroom, geen PostHog data. De laatste meetbare aggregaat blijft de 5-run-dagen snapshot uit eerdere rapporten:

Link clicks (~329) > Meta pixel LPV (~275, 83,6% van LC) > Initiate Checkout (15, 4,6% van LC, 5,5% van LPV)

**Observatie:** Hetzelfde getal als in het 04-26 rapport, en het 04-25 rapport. Deze frozen baseline is nu 7 dagen oud. Bij heractivering moeten de eerste 2 tot 3 dagen opnieuw gemeten worden om te bevestigen dat het LPV>IC pad nog rond 5-6% ligt of gedaald is door doelgroep- of seizoens-drift.

## 5. Rode Vlaggen

- **Zevende dag op rij zonder live SYBB campagne.** 2026-04-21, 04-22, 04-23, 04-24, 04-25, 04-26 en nu 04-27 allemaal nul spend over beide campagnes. De pauze (7 dagen) is nu 2 dagen langer dan de feitelijke runperiode van iteratie 1 (5 run-dagen, 04-16 t/m 04-20). Het iteratie-1 venster behoort vanaf nu tot het verleden voor elke 7d-vergelijking, dus elke nieuwe run is effectief een koude start.
- **7d-venster volledig leeg.** Voor het eerst sinds iteratie 1 is gestart bevat het rolling 7d-venster geen enkele run-dag. Tot heractivering is dit deel van het rapport een vaste "geen data" tabel zonder informatieve waarde, exact zoals voorspeld in het 04-26 rapport.
- **PostHog MCP negen rapportdagen op rij offline.** 2026-04-19 t/m 2026-04-27. Geen tooling-config wijziging zichtbaar in de deferred tool lijst. Dit is geen incident, het is de vaste state. De SKILL zoals beschreven (Meta Ads x PostHog cross-referencing) draait al meer dan een week op halve kracht. De fix uit actie 2 van het 04-26 rapport is niet uitgevoerd.
- **Beslissingslog drie dagen open.** Actie 1 stond in het 04-25, 04-26 en nu 04-27 rapport. Geen `sybb_decision_log_*.md` aangetroffen in `Output/Reports/`. Het aantal "dagen onbeslist" is nu groter dan het aantal dagen aan extra signaal en de actie wordt bij elke nieuwe rapportdag urgenter.
- **Iteratie-1 baseline-document drie dagen open.** Actie 3 stond in het 04-25 en 04-26 rapport. Geen `sybb_iter1_baseline.md` aangetroffen. Het 7d-venster is nu daadwerkelijk leeg. De ad-level snapshot uit het 04-21 rapport is de enige plek waar de hook-vergelijking nog terug te vinden is. Risico op verlies van het 5-run-dagen signaal stijgt elke dag.
- **Beslissing rond H12 vs H13 nu 192+ uur oud.** De directionele hypothese is gebaseerd op 2 run-dagen en is nu een week oud zonder validatie. Bij hervatting met dezelfde line-up start je met klein-sample assumpties op een week oude data. De urgentie van actie 3 (baseline document) loopt parallel met deze klok.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag definitief: heractiveren, killen, of rebuild + datum vastleggen, en leg het schriftelijk vast.**
   - **Wat:** maak vandaag het beslissingslog dat al drie dagen openstaat. Concreet: markdown in `Output/Reports/sybb_decision_log_2026-04-27.md` met datum, gekozen pad (heractiveren, rebuild, of kill) en reden. Bij heractivering: zet H13 op PAUSED op ad-niveau, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen om de re-learning fase te respecteren. Bij rebuild: leg launchdatum iteratie 2 vast (concrete datum, niet "binnenkort") en koppel daar een lijst nieuwe creatives aan. Bij kill: noteer expliciet "campagne stopgezet, geen iteratie 2 gepland" met reden en datum.
   - **Waarom:** zevende pauzedag op rij. Pauze (7) overstijgt nu runperiode (5) met 2 dagen. Het 7d-venster heeft 0 run-dagen aan baseline. De beslissingslog uit het 04-25 en 04-26 rapport is niet aangemaakt, dus dezelfde actie wordt vandaag voor de derde keer herhaald met elke dag extra urgentie en elke dag oudere ad-level data.
   - **Hoe:** Meta Ads Manager > campagne `2026: SYBB - Kopie` (120243293329420239) activeren OF beslissingslog markdown-bestand aanmaken. Bij heractivering: eerst H13 op ad-niveau uitzetten voor het indrukken van activeren op campagne-niveau, om de re-learning te starten met de twee best-presterende hooks.
   - **Verwachte impact:** bij heractivering binnen 3 tot 4 dagen terug naar €60 tot €85 spend per dag met 2 tot 5 IC's per dag, eerste 1 tot 2 dagen 10-20% hogere CPC verwacht door re-learning. Bij rebuild: 1 tot 2 weken voorbereidingstijd voor iteratie 2 launch. Bij kill: helderheid voor het hele kanaal en budget vrij voor andere campagnes.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Documenteer de 5-run-dagen baseline NU. Het 7d-venster is vanaf vandaag leeg.**
   - **Wat:** korte markdown in `Output/Reports/sybb_iter1_baseline.md` met aggregaten over de 5 run-dagen (04-16 t/m 04-20): totale spend, clicks, LPVs, IC's, CTR, CPC, LPV>IC rate. Per hook variant (H11, H12, H13, H14, H15 indien gelopen) de directionele CTR/CPC/IC splitsing op basis van het 04-21 rapport. Eindig met 1 expliciete hypothese voor iteratie 2.
   - **Waarom:** dit was punt 3 in het 04-25 en 04-26 rapport en is nog niet gebeurd. Vanaf vandaag is het 7d-venster volledig leeg. Het signaal verdwijnt niet uit de oude rapporten, maar het wordt steeds duurder om bij heractivering of iteratie 2 het overzicht uit gefragmenteerde rapportdata te reconstrueren. Een gefocust baseline-document is 30 minuten werk en bespaart bij iteratie 2 een uur+ aan herwerk.
   - **Hoe:** lees `Output/Reports/Daily/2026-04-21_sybb_report.md` voor de ad-level CTR/CPC/IC per hook, lees ook 04-19 t/m 04-22 rapporten voor de 5-run-dagen aggregaten. Schrijf het samen in 1 markdown. Eindig met expliciete hypothese voor iteratie 2: welke hook angle doorontwikkelen, welke creative elementen behouden, welk CTA format (cta5) blijft, welk audience-vlak verbreden of vernauwen.
   - **Verwachte impact:** geen directe KPI impact. Wel: volgende launch start met geschreven hypothese in plaats van vanaf nul of "uit het hoofd". Voorkomt dat 5 run-dagen aan data effectief weggegooid worden.
   - **Escalatie:** Groen, geen goedkeuring nodig.

3. **Herstel PostHog MCP toegang (negen rapportdagen op rij offline).**
   - **Wat:** PostHog MCP server reactiveren of opnieuw configureren in de Claude Code setup zodat `posthog_*` tools weer in de deferred tool lijst verschijnen.
   - **Waarom:** negen dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Bij heractivering wil je PostHog dag-1 al werkend hebben, niet pas dag-3 als de eerste resultaten binnenkomen, anders mis je opnieuw de cross-reference op de eerste run en herhaalt de iteratie 1 blinde-vlek-fout zich. Dit is een eenmalige fix met permanent rendement. Stond als actie 2 in het 04-26 rapport en is niet uitgevoerd.
   - **Hoe:** check `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Verifieer API key uit PostHog project "Default project" (mogelijk verlopen token of project-renamed). Test na restart met een eenvoudige pageviews-query op startyourballoonbusiness.com over de laatste 24 uur.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run. Geen directe campagne-impact, wel hersteld diagnostisch vermogen voor alle daaropvolgende rapporten en cruciaal voor dag-1 van iteratie 2.
   - **Escalatie:** Oranje, tooling ingreep.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-27_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen schrijfactie naar Meta Ads Tracker Google Sheet. Alle Meta-getallen direct uit `get_insights`, range 2026-04-20 t/m 2026-04-27 (zowel daily breakdown als status check via `get_campaigns`).
