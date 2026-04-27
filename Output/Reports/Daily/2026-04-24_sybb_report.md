# SYBB Daily Report, 2026-04-24

## 1. Samenvatting

Vierde volle pauzedag op rij. Op 2026-04-24 nul impressies, nul clicks, nul spend op beide SYBB campagnes (`2026: SYBB` en `2026: SYBB - Kopie`) op account `act_567892422940728`. De "2026: SYBB - Kopie" (120243293329420239) staat sinds 2026-04-20 17:09 op PAUSED, de originele "2026: SYBB" (120239435987290239) sinds 2026-04-19 14:29. Geen statuswijziging sinds het rapport van gisteren. PostHog MCP is voor de zesde rapportdag op rij niet beschikbaar, dus landing page health kan opnieuw niet gevalideerd worden.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)
- Geen Google MCPs gebruikt in deze run.

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt | Dagen op pauze |
|----------|----|----|-------------------|---------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 | 4 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 | 5 |

### Performance gisteren vs voorgaande dagen

Cijfers hieronder komen uit Meta Ads MCP `get_insights` met `time_breakdown=day` voor periode 2026-04-17 tot 2026-04-24, gecombineerd over beide campagnes. Op 2026-04-19 liepen origineel + Kopie tegelijk; die kolom toont de optelling.

| Metric | 2026-04-24 | 2026-04-23 | 2026-04-22 | 2026-04-21 | 2026-04-20 | 2026-04-19 | 2026-04-18 | 2026-04-17 | 7d gem. (run-dagen) |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------------------|
| Spend | €0,00 | €0,00 | €0,00 | €0,00 | €77,85 | €90,38 | €94,64 | €86,68 | €87,39 per run-dag |
| Impressions | 0 | 0 | 0 | 0 | 4.287 | 6.084 | 6.454 | 6.006 | 5.708 |
| Clicks (all) | 0 | 0 | 0 | 0 | 119 | 137 | 153 | 139 | 137 |
| Link clicks | 0 | 0 | 0 | 0 | 75 | 86 | 90 | 78 | 82 |
| CTR | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 2,78% | 2,25% | 2,37% | 2,31% | 2,38% |
| CPC (all) | n.v.t. | n.v.t. | n.v.t. | n.v.t. | €0,65 | €0,66 | €0,62 | €0,62 | €0,64 |
| Frequency | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 1,34 | 1,21-1,35 | 1,34 | 1,39 | ~1,33 |
| Landing Page Views (Meta pixel) | 0 | 0 | 0 | 0 | 63 | 71 | 78 | 63 | 69 |
| Initiate Checkout | 0 | 0 | 0 | 0 | 2 | 6 | 7 | 0 | 3,75 |

*7d gemiddelde berekend over de 4 daadwerkelijke run-dagen binnen de venster 2026-04-17 t/m 2026-04-23 (04-17, 04-18, 04-19, 04-20). Pauzedagen niet meegerekend in het gemiddelde, anders zou het gemiddelde kunstmatig verlaagd worden door 0-dagen.*

**Trend:** 96+ uur zonder enige Meta-spend op SYBB. De "2026: SYBB - Kopie" zit nu 4 volle dagen op pauze, de originele "2026: SYBB" 5 dagen. Het Meta-algoritme is inmiddels volledig uit de learning fase verdwenen voor deze campagnes; bij heractivering is een nieuwe learning fase onvermijdelijk (typisch 2 tot 4 dagen verhoogde CPC en wisselende CTR voor stabilisatie). Het pre-pauze momentum (04-18 piek: 153 clicks, 78 LPVs, 7 ICs) is onomkeerbaar verdwenen als baseline voor het volgende cohort.

### Ad variant performance

Niet van toepassing voor 2026-04-24. Geen ad-level data beschikbaar omdat geen enkele ad heeft gelopen. De laatste cumulatieve ad-level snapshot uit het rapport van 2026-04-21 (gebaseerd op 19 + 20 april data) blijft het actueelste beeld tot heractivering: H12 (b3_cta5) leidt op CTR/CPC, H13 (b3_cta5) onderpresteert met CPC boven €0,90, H11 zit in het midden. Sample is 2 run-dagen op ad-niveau, dus directioneel signaal, geen statistisch bewijs.

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

Zelfs bij werkende PostHog: zonder Meta-instroom is het signaal beperkt tot direct + organisch verkeer. Dat is bruikbaar als baseline (hoe presteert de LP zelfstandig?), maar levert geen inzicht in ad x LP mismatch op, en dat is precies de cross-reference waar dit rapport op leunt.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-24. Geen Meta instroom, geen PostHog data. De laatste meetbare funnel-slice uit de 4 run-dagen binnen de huidige 7d-venster (04-17 t/m 04-20):

Link clicks (329) > Meta pixel LPV (275, 83,6%) > Initiate Checkout (15, 4,6% van LC / 5,5% van LPV)

**Observatie:** Meta pixel LPV > IC conversie van ~5,5% over deze 4 dagen ligt iets onder de 6,1% uit het 5-daagse venster van het 04-23 rapport (dat 04-16 nog meenam). Niet alarmerend, wel een teken dat 04-17 (0 ICs op 78 LPVs) het gemiddelde drukt. Bij heractivering zou ik de eerste 3 dagen de IC rate per ad variant monitoren: onder 4% van LPV is offer/landing page mismatch, boven 7% is signaal om spend op te schalen.

## 5. Rode Vlaggen

- **Vierde dag op rij zonder live SYBB campagne.** 2026-04-21, 04-22, 04-23 en 04-24 allemaal nul spend. "2026: SYBB - Kopie" niet heractiveerd sinds 2026-04-20 17:09. De stilstand is nu langer dan de gehele run-periode (5 dagen vs 5 run-dagen): 1:1 verhouding tussen actieve dagen en pauzedagen sinds launch. Als dit onbedoeld is, verliest het algoritme zijn learning window definitief. Als bewust, ontbreekt nog altijd een gedocumenteerde reden in het beslissingslog.
- **PostHog MCP structureel down.** 2026-04-19, 04-20, 04-21, 04-22, 04-23 en nu 04-24: zes rapportdagen op rij zonder landing page observability. Dit is geen incidentele storing, dit is een gebroken onderdeel van de dagelijkse pijplijn dat ingrijpen vereist.
- **Beslissings-stilstand rond H12 vs H13 nu 120+ uur oud.** De hypothese (H12 wint, H13 underperformt) staat onveranderd op basis van 2 run-dagen. Hoe langer dit blijft hangen, hoe minder relevant deze data is voor de volgende iteratie: audience saturation, seizoensfluctuatie en creative fatigue spelen mee bij heractivering.
- **Aggregaten 7d-venster gekrompen tot 4 run-dagen.** Vorig rapport (04-23) baseerde het 7d-gemiddelde op 5 run-dagen omdat 04-16 nog binnen het venster viel. In het 04-24 rapport valt 04-16 buiten het 7-daagse venster. Dat verlaagt het gewicht van vroeg-fase data en doet 04-17 (slechtste IC-dag) zwaarder meewegen. Conclusie: hoe langer de pauze duurt, hoe minder informatief het 7d-gemiddelde wordt als referentie.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag (definitief): heractiveren, killen, of rebuilden?**
   - **Wat:** Robin neemt vandaag de knoop door. De 4-daagse pauze is geen tussenstand meer maar een feitelijke campagne-stop. Bij heractivering: zet H13 op PAUSED op ad-niveau, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen om de re-learning fase te respecteren. Bij rebuild: documenteer wat de 5 run-dagen leerden voor iteratie 2 voor je nieuwe creatives uploadt. Bij kill: noteer expliciet "campagne stopgezet, geen iteratie 2 gepland" met reden.
   - **Waarom:** elke dag stilstand kost learning data en verplicht Meta tot een learning phase reset bij herstart. De H12 vs H13 hypothese staat nu 120+ uur op pauze gebaseerd op klein sample. Zonder beslissing wordt dit rapport elke dag dunner.
   - **Hoe:** Meta Ads Manager > campagne "2026: SYBB - Kopie" (120243293329420239) activeren OF beslissingslog vullen + volgende iteratie plannen. Als heractivering: eerst H13 op ad-niveau uitzetten voor activering campagne, dan 3 dagen onaangeraakt laten.
   - **Verwachte impact:** bij heractivering binnen 3 tot 4 dagen terug naar €50 tot €80 spend per dag met 2 tot 5 IC's per dag. Eerste 1 tot 2 dagen 10-20% hogere CPC verwacht door re-learning. Bij rebuild: 1 tot 2 weken voorbereidingstijd voor iteratie 2 launch.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Herstel PostHog MCP toegang (zes rapportdagen op rij offline).**
   - **Wat:** PostHog MCP server reactiveren of opnieuw configureren in de Claude Code setup zodat `posthog_*` tools weer in de deferred tool lijst verschijnen.
   - **Waarom:** zes dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Het centrale idee van de SKILL (Meta Ads x PostHog cross-referencing) werkt niet zonder PostHog. Zelfs bij gepauzeerde campagnes geeft LP baseline (direct + organic) inzicht of de pagina überhaupt traffic ziet en hoe die zich gedraagt. Bovendien: bij heractivering wil je PostHog dag-1 al werkend hebben, niet pas dag-3 als de eerste resultaten binnenkomen.
   - **Hoe:** check `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Verifieer API key uit PostHog project "Default project" (mogelijk verlopen token of project-renamed). Test na restart met een eenvoudige pageviews-query op startyourballoonbusiness.com over de laatste 24 uur.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run met cross-referencing Meta x LP weer mogelijk. Geen directe campagne-impact, wel hersteld diagnostisch vermogen.
   - **Escalatie:** Oranje, tooling ingreep.

3. **Documenteer de 5-run-dagen baseline als pre-iteratie-2 referentie.**
   - **Wat:** korte markdown in `Output/Reports/` met aggregaten over de 5 run-dagen (04-16 t/m 04-20): totale spend, clicks, LPVs, IC's, CTR, CPC, LPV>IC rate. Per hook variant (H11, H12, H13, en eventueel H14/H15) de directionele CTR/CPC/IC splitsing op basis van het 04-21 rapport.
   - **Waarom:** als heractivering uitblijft of als rebuild komt, verdampt het leerresultaat van 5 run-dagen zonder samenvatting. Zelfs bij heractivering is deze baseline nodig om iteratie 2 prestaties tegen af te zetten. Meta's aggregate over deze run: CTR stabiel rond 2,38%, CPC rond €0,64, IC rate ~5,5% van LPV. Dat is de nul-lijn waartegen elke nieuwe creative of audience-shift gemeten moet worden.
   - **Hoe:** markdown per hook (H11, H12, H13, H14, H15 als gelopen) met CTR, CPC, LPV, IC. Eindig met een expliciete hypothese voor iteratie 2: welke hook angle doorontwikkelen, welke creative elementen behouden, welk CTA format (cta5) blijft, welk audience-vlak verbreden of vernauwen.
   - **Verwachte impact:** geen directe KPI impact. Wel discipline: volgende launch start met een geschreven hypothese in plaats van vanaf nul of "uit het hoofd."
   - **Escalatie:** Groen, geen goedkeuring nodig.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-24_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers; alle Meta-getallen direct uit `get_insights` time_breakdown=day, 2026-04-17 t/m 2026-04-24.
