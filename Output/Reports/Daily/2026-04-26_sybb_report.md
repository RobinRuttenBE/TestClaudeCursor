# SYBB Daily Report, 2026-04-26

## 1. Samenvatting

Zesde volle pauzedag op rij voor de SYBB ads. Op 2026-04-26 nul impressies, nul clicks, nul spend op zowel `2026: SYBB` (120239435987290239) als `2026: SYBB - Kopie` (120243293329420239) op account `act_567892422940728`. De Kopie staat sinds 2026-04-20 17:09 op PAUSED, het origineel sinds 2026-04-19 14:29. De pauzeperiode is nu langer dan de feitelijke runperiode (6 vs 5 run-dagen). PostHog MCP is voor de achtste rapportdag op rij niet beschikbaar, dus landing page health blijft niet meetbaar en de cross-reference die het hart van deze SKILL vormt blijft uit.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)
- Geen Google MCPs gebruikt in deze run, geen schrijfactie naar de Meta Ads Tracker Google Sheet

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt | Volle pauzedagen t/m 2026-04-26 23:59 |
|----------|----|----|-------------------|---------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 | 6 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 | 7 |

### Performance gisteren

| Metric | 2026-04-26 | 7d gem. (run-dagen 04-19, 04-20) | Trend |
|--------|-----------|----------------------------------|-------|
| Spend | €0,00 | €84,12 per run-dag | n.v.t. (nul vs 84) |
| Impressions | 0 | 5.186 per run-dag | n.v.t. |
| Clicks (all) | 0 | 128 per run-dag | n.v.t. |
| Link clicks | 0 | 80,5 per run-dag | n.v.t. |
| CTR | n.v.t. | ~2,47% | n.v.t. |
| CPC (all) | n.v.t. | ~€0,66 | n.v.t. |
| Frequency | n.v.t. | ~1,39 | n.v.t. |
| Landing Page Views (Meta pixel) | 0 | ~68 per run-dag | n.v.t. |
| Initiate Checkout | 0 | 4,0 per run-dag | n.v.t. |

### 7d window aggregaat (2026-04-19 t/m 2026-04-25, gecombineerd over beide SYBB campagnes)

Cijfers direct uit `get_insights` op campagne-niveau, periode 2026-04-19 t/m 2026-04-25. Run-dagen binnen dit venster: alleen 2026-04-19 (origineel + Kopie tegelijk gelopen) en 2026-04-20 (alleen Kopie). Vanaf 2026-04-21 staat alles op pauze.

| Campagne | Spend | Impressions | Clicks (all) | Link clicks | LPV (Meta pixel) | IC | CTR | CPC (all) |
|----------|-------|-------------|--------------|-------------|------------------|----|-----|-----------|
| 2026: SYBB (origineel), 04-19 | €43,81 | 2.756 | 61 | 36 | 34 | 2 | 2,21% | €0,72 |
| 2026: SYBB - Kopie, 04-19 + 04-20 | €124,42 | 7.615 | 195 | 125 | 100 | 6 | 2,56% | €0,64 |
| **Totaal 2 run-dagen** | **€168,23** | **10.371** | **256** | **161** | **134** | **8** | **2,47%** | **€0,66** |

**7d run-dagen gemiddelde** (over de 2 daadwerkelijke run-dagen 04-19 en 04-20): €84,12 spend per dag, 5.186 imp, 128 clicks, 80,5 link clicks, 68 LPV, 4,0 IC. Dit gemiddelde is gebaseerd op een sample van 2 dagen en is alleen directioneel.

**Trend:** 144+ uur zonder Meta-spend op SYBB. Het 7d run-dagen aggregaat is van 3 naar 2 run-dagen gekrompen sinds gisteren (04-18 viel uit het venster). Vanaf 2026-04-27 valt 04-19 ook buiten het 7d-venster, dan blijft alleen 04-20 over als referentie. Vanaf 2026-04-28 is het 7d-aggregaat volledig leeg en wordt deze tabel onbruikbaar als baseline. Frequentie zat bij beide campagnes onder 1,5, dus geen ad fatigue als oorzaak van de pauze.

### Ad variant performance

Niet van toepassing voor 2026-04-26. Geen ad-level data omdat geen enkele ad heeft gelopen (`get_insights` op level=ad gaf lege response). De laatste ad-level snapshot blijft het signaal uit het 04-21 rapport, gebaseerd op 04-19 en 04-20: H12 (b3_cta5) leidt op CTR/CPC, H13 (b3_cta5) onderpresteert met CPC > €0,90, H11 (b3_cta5) zit ertussenin. Sample is 2 run-dagen. Dit signaal is nu 6 dagen oud en directioneel, niet beslissend.

## 3. Landing Page Health

**Niet beschikbaar.** PostHog MCP is niet ingeladen in deze sessie. Geen pageviews, bounce rate, scroll depth, session duration, CTA click rate of session recordings voor `startyourballoonbusiness.com` op te halen. Dit is de achtste rapportdag op rij zonder PostHog data (sinds 2026-04-19).

| Metric | Target | Status |
|--------|--------|--------|
| Bounce Rate | <55% | geen data |
| Avg Session Duration | >90s | geen data |
| Scroll 25% | >80% | geen data |
| Scroll 50% | >60% | geen data |
| Scroll 75% | >40% | geen data |
| Scroll 100% | >20% | geen data |
| CTA Click Rate | >4% | geen data |

Bij werkende PostHog zou ook zonder Meta-instroom een baseline van direct + organisch + email verkeer zichtbaar zijn. Dat ontbreekt nu acht rapportdagen op rij. De cross-reference tussen ad x landing page (kern van deze SKILL) is daarmee structureel niet uitvoerbaar tot de tool weer beschikbaar is.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-26. Geen Meta instroom, geen PostHog data. De laatste meetbare aggregaat blijft de 5-run-dagen snapshot uit eerdere rapporten:

Link clicks (329) > Meta pixel LPV (275, 83,6% van LC) > Initiate Checkout (15, 4,6% van LC, 5,5% van LPV)

**Observatie:** geen verandering t.o.v. gisteren of eergisteren. Hoe langer de pauze duurt, hoe minder waard deze cijfers worden als baseline. Bij heractivering moeten de eerste 2 tot 3 dagen opnieuw gemeten worden om te bevestigen dat het LPV>IC pad nog rond 5-6% ligt of gedaald is door doelgroep- of seizoens-drift.

## 5. Rode Vlaggen

- **Zesde dag op rij zonder live SYBB campagne.** 2026-04-21, 04-22, 04-23, 04-24, 04-25 en nu 04-26 allemaal nul spend over beide campagnes. De pauze (6 dagen) is nu langer dan de feitelijke runperiode van iteratie 1 (5 run-dagen, 04-16 t/m 04-20). Heractivering betekent vrijwel zeker een nieuwe learning fase van 2 tot 4 dagen met 10-20% verhoogde CPC in dag 1-2. Elke extra pauzedag verlengt deze re-learning verwachting niet, maar verkleint wel de waarde van het oude signaal H12 vs H13.
- **PostHog MCP acht rapportdagen op rij offline.** 2026-04-19 t/m 2026-04-26. Geen tooling-config wijziging zichtbaar in de deferred tool lijst. Dit is geen incident meer, het is de vaste state geworden. De SKILL zoals beschreven (Meta Ads x PostHog cross-referencing) draait al langer dan een week op halve kracht.
- **7d run-dagen gemiddelde gekrompen van 3 naar 2.** Sinds gisteren is 04-18 uit het venster gevallen, dus het aggregaat is van 3 run-dagen naar 2 run-dagen geslonken. Vanaf 2026-04-27 valt ook 04-19 weg, vanaf 2026-04-28 is er geen run-dag meer in het 7d-venster. Daarmee verliest dit rapport elke werkdag verder aan baseline tot de campagne weer aan staat.
- **Beslissing rond H12 vs H13 nu 168+ uur oud.** De directionele hypothese (H12 wint, H13 onder par, H11 midden) is gebaseerd op 2 run-dagen en is nu een week oud zonder validatie. Bij hervatting met dezelfde line-up start je met klein-sample assumpties. Bij 2+ weken vertraging is dit signaal te oud om beslissingen op te baseren en moet iteratie 2 vrijwel from scratch beginnen.
- **Beslissingslog van actie 1 in het 04-25 rapport is niet aangemaakt** (geen `sybb_decision_log_*.md` in `Output/Reports/` aangetroffen tijdens deze run). Het aantal "dagen onbeslist" loopt inmiddels op naar 6, sneller dan het aantal dagen aan extra data.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag definitief: heractiveren, killen, of rebuild + datum vastleggen, en leg het schriftelijk vast.**
   - **Wat:** maak vandaag het beslissingslog dat al twee dagen openstaat. Concreet: markdown in `Output/Reports/sybb_decision_log_2026-04-26.md` met datum, gekozen pad (heractiveren, rebuild, of kill) en reden. Bij heractivering: zet H13 op PAUSED op ad-niveau, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen om de re-learning fase te respecteren. Bij rebuild: leg launchdatum iteratie 2 vast (concrete datum, niet "binnenkort") en koppel daar een lijst nieuwe creatives aan. Bij kill: noteer expliciet "campagne stopgezet, geen iteratie 2 gepland" met reden en datum.
   - **Waarom:** zesde pauzedag op rij. Pauze (6) overstijgt nu runperiode (5). Het 7d-venster heeft nog 2 run-dagen aan baseline en verliest morgen weer een dag. De beslissingslog uit het 04-25 rapport is niet aangemaakt, dus dezelfde actie wordt vandaag herhaald met een dag extra urgentie.
   - **Hoe:** Meta Ads Manager > campagne `2026: SYBB - Kopie` (120243293329420239) activeren OF beslissingslog markdown-bestand aanmaken. Bij heractivering: eerst H13 op ad-niveau uitzetten voor het indrukken van activeren op campagne-niveau, om de re-learning te starten met de twee best-presterende hooks.
   - **Verwachte impact:** bij heractivering binnen 3 tot 4 dagen terug naar €60 tot €85 spend per dag met 2 tot 5 IC's per dag. Eerste 1 tot 2 dagen 10-20% hogere CPC verwacht door re-learning. Bij rebuild: 1 tot 2 weken voorbereidingstijd voor iteratie 2 launch. Bij kill: helderheid voor het hele kanaal en budget vrij voor andere campagnes.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Herstel PostHog MCP toegang (acht rapportdagen op rij offline).**
   - **Wat:** PostHog MCP server reactiveren of opnieuw configureren in de Claude Code setup zodat `posthog_*` tools weer in de deferred tool lijst verschijnen.
   - **Waarom:** acht dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Bij heractivering wil je PostHog dag-1 al werkend hebben, niet pas dag-3 als de eerste resultaten binnenkomen, anders mis je opnieuw de cross-reference op de eerste run en herhaalt de iteratie 1 blinde-vlek-fout zich. Dit is een eenmalige fix met permanent rendement.
   - **Hoe:** check `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Verifieer API key uit PostHog project "Default project" (mogelijk verlopen token of project-renamed). Test na restart met een eenvoudige pageviews-query op startyourballoonbusiness.com over de laatste 24 uur.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run. Geen directe campagne-impact, wel hersteld diagnostisch vermogen voor alle daaropvolgende rapporten.
   - **Escalatie:** Oranje, tooling ingreep.

3. **Documenteer de 5-run-dagen baseline NU, voordat het 7d-venster volledig leeg loopt.**
   - **Wat:** korte markdown in `Output/Reports/` (bv. `sybb_iter1_baseline.md`) met aggregaten over de 5 run-dagen (04-16 t/m 04-20): totale spend, clicks, LPVs, IC's, CTR, CPC, LPV>IC rate. Per hook variant (H11, H12, H13, H14, H15 indien gelopen) de directionele CTR/CPC/IC splitsing op basis van het 04-21 rapport. Eindig met 1 expliciete hypothese voor iteratie 2 (welke hook angle behouden, welk CTA-format, welke audience-richting).
   - **Waarom:** dit was punt 3 in het rapport van 04-25 en is nog niet gebeurd. Vanaf morgen valt 04-19 uit het 7d-venster, vanaf overmorgen is het 7d-aggregaat leeg. Als deze samenvatting niet vandaag wordt vastgelegd, moet bij iteratie 2 of heractivering het hele 5-run-dagen venster opnieuw uit oudere reports getrokken worden, met meer kans op fouten en verlies van de hook-snapshot.
   - **Hoe:** markdown per hook (H11, H12, H13, H14, H15 indien gelopen) met CTR, CPC, LPV, IC. Eindig met expliciete hypothese voor iteratie 2: welke hook angle doorontwikkelen, welke creative elementen behouden, welk CTA format (cta5) blijft, welk audience-vlak verbreden of vernauwen.
   - **Verwachte impact:** geen directe KPI impact. Wel: volgende launch start met geschreven hypothese in plaats van vanaf nul of "uit het hoofd". Voorkomt dat 5 run-dagen aan data effectief weggegooid worden.
   - **Escalatie:** Groen, geen goedkeuring nodig.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-26_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen schrijfactie naar Meta Ads Tracker Google Sheet. Alle Meta-getallen direct uit `get_insights`, range 2026-04-19 t/m 2026-04-26.
