# SYBB Daily Report, 2026-04-23

## 1. Samenvatting

Derde volle pauzedag op rij. Op 2026-04-23 nul impressies, nul clicks, nul spend op beide SYBB campagnes (`2026: SYBB` en `2026: SYBB - Kopie`) op account `act_567892422940728`. De "2026: SYBB - Kopie" (120243293329420239) staat sinds 2026-04-20 17:09 op PAUSED, de originele "2026: SYBB" (120239435987290239) sinds 2026-04-19 14:29. PostHog MCP is voor de vijfde rapportdag op rij niet beschikbaar, dus landing page health kan opnieuw niet gevalideerd worden.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt |
|----------|----|----|-------------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 |

### Performance gisteren vs voorgaande dagen

| Metric | 2026-04-23 | 2026-04-22 | 2026-04-21 | 2026-04-20 | 2026-04-19 | 2026-04-18 | 2026-04-17 | 2026-04-16 | 7d gem. (run-dagen) |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-------------------|
| Spend | €0,00 | €0,00 | €0,00 | €77,85 | €90,38 | €94,64 | €86,68 | €57,89 | €81,49 per run-dag |
| Impressions | 0 | 0 | 0 | 4.287 | 6.084 | 6.454 | 6.006 | 4.510 | 5.468 |
| Clicks (all) | 0 | 0 | 0 | 119 | 137 | 153 | 139 | 104 | 130 |
| Link clicks | 0 | 0 | 0 | 75 | 86 | 90 | 78 | 64 | 79 |
| CTR | n.v.t. | n.v.t. | n.v.t. | 2,78% | 2,25% | 2,37% | 2,31% | 2,31% | 2,38% |
| CPC (all) | n.v.t. | n.v.t. | n.v.t. | €0,65 | €0,66 | €0,62 | €0,62 | €0,56 | €0,62 |
| Frequency | n.v.t. | n.v.t. | n.v.t. | 1,34 | 1,28-1,35 | 1,34 | 1,39 | 1,45 | ~1,37 |
| Landing Page Views (Meta pixel) | 0 | 0 | 0 | 63 | 71 | 78 | 63 | 54 | 66 |
| Initiate Checkout | 0 | 0 | 0 | 2 | 6 | 7 | 0 | 5 | 4,0 |

*7d gemiddelde berekend over de 5 daadwerkelijke run-dagen (2026-04-16 t/m 2026-04-20), aggregeert beide campagnes op 04-19 (origineel + kopie samen). Pauzedagen niet meegerekend.*

**Trend:** 72+ uur zonder enige Meta-spend op SYBB. De "2026: SYBB - Kopie" zit nu 3 dagen op pauze. Voor Meta learning phase betekent dit: bij heractivering opnieuw door de learning fase, typisch 2 tot 4 dagen verhoogde CPC voor het algoritme stabiliseert. Het cumulatief effect bij 3 dagen stilstand: het momentum van de 04-18 piek (153 clicks, 78 LPVs, 7 ICs, laagste CPC-trend) is nu volledig verdampt.

### Ad variant performance

Niet van toepassing voor 2026-04-23. Geen ad-level data beschikbaar omdat geen enkele ad heeft gelopen. De laatste cumulatieve ad-level snapshot (rapport 2026-04-21, 19 + 20 april data) blijft het actueelste beeld tot heractivering: H12 (b3_cta5) leidt op CTR/CPC, H13 (b3_cta5) onderpresteert met CPC boven €0,90 (ruim boven target). H11 zit in het midden. Dit is gebaseerd op 2 run-dagen en blijft te klein sample voor harde conclusies.

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

Zelfs als PostHog zou werken: zonder Meta-verkeer is het signaal beperkt tot direct + organisch. Dat is nuttig als baseline (hoe presteert de LP zelfstandig?), maar levert geen inzicht in ad > LP mismatch op en dat is precies de cross-reference waar dit rapport op leunt.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-23. Geen Meta instroom, geen PostHog data. De laatste meetbare funnel-slice uit de 5 run-dagen (04-16 t/m 04-20):

Link clicks (393) > Meta LPV (329, 83,7%) > Initiate Checkout (20, 5,1% van LC / 6,1% van LPV)

**Observatie:** Meta pixel LPV > IC conversie van ~6% is de beste meetbare indicator van LP performance die we nu hebben. Dat is binnen verwachting voor een workshop-sale funnel met €35 orderwaarde. Bij heractivering zou ik de eerste 3 dagen de IC rate monitoren: als die onder 4% van LPV zakt, is er een offer of landing page mismatch; boven 7% is signaal om spend op te schalen.

## 5. Rode Vlaggen

- **Derde dag op rij zonder live SYBB campagne.** 2026-04-21, 2026-04-22 en 2026-04-23 allemaal nul spend. "2026: SYBB - Kopie" is sinds 2026-04-20 17:09 niet heractiveerd. Als dit onbedoeld is, verliest het algoritme z'n learning window. Als bewust, ontbreekt een gedocumenteerde reden.
- **PostHog MCP structureel down.** 2026-04-19, 04-20, 04-21, 04-22 en nu 04-23: vijf rapportdagen op rij zonder landing page observability. Dit is geen incidentele storing meer, dit is een gebroken onderdeel van de dagelijkse pijplijn dat ingrijpen vereist.
- **Beslissings-stilstand rond H12 vs H13 nu 96+ uur oud.** De hypothese (H12 wint, H13 underperformt) staat gebaseerd op 2 run-dagen. Hoe langer we wachten, hoe minder recent de data relevant is voor de volgende iteratie. Audience saturation, seizoensfluctuatie en creative fatigue spelen mee.
- **Verloren momentum:** 04-18 was de sterkste dag van de 5 run-dagen (153 clicks, 78 LPVs, 7 ICs, CTR 2,37%). Die piek werd gevolgd door pauzering 24 uur later. Dat is precies het moment waarop Meta algoritme voldoende data had om te optimaliseren — nu resetten we dat bij heractivering.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag: heractiveren, killen, of rebuilden?**
   - **Wat:** Robin bepaalt of de 3-daagse pauze bewust is (budget hold, nieuwe creatives in productie, tussenevaluatie) of per ongeluk nog steeds loopt. Bij heractivering: zet H13 op PAUSED, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen. Bij rebuild: document wat de 5 run-dagen leerden voor iteratie 2.
   - **Waarom:** elke dag stilstand kost learning data en verplicht Meta tot een learning phase reset bij herstart. De H12 vs H13 hypothese staat nu 96+ uur op pauze gebaseerd op klein sample.
   - **Hoe:** Meta Ads Manager > campagne "2026: SYBB - Kopie" (120243293329420239) > activeren OF pauze documenteren in beslissingslog + volgende iteratie plannen. Als heractivering: eerst H13 op ad-niveau uitzetten voor activering campagne.
   - **Verwachte impact:** bij heractivering binnen 3 tot 4 dagen terug naar €50 tot €80 spend per dag met 2 tot 5 IC's per dag. Eerste 1 tot 2 dagen vaak 10-20% hogere CPC vanwege re-learning.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Herstel PostHog MCP toegang.**
   - **Wat:** PostHog MCP server reactiveren of opnieuw configureren in de Claude Code setup zodat `posthog_*` tools weer in de deferred tool lijst verschijnen.
   - **Waarom:** vijf dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Het centrale idee van de SKILL (Meta Ads x PostHog cross-referencing) werkt niet zonder PostHog. Zelfs bij gepauzeerde campagnes geeft LP baseline (direct + organic) inzicht.
   - **Hoe:** check `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Verifieer API key uit PostHog project "Default project" (mogelijk verlopen token). Test na restart met een `posthog_query_insight` call op startyourballoonbusiness.com pageviews laatste 24u.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run met cross-referencing Meta > LP weer mogelijk.
   - **Escalatie:** Oranje, tooling ingreep.

3. **Snapshot documenteren van de 5 run-dagen voor iteratie 2 planning.**
   - **Wat:** korte markdown in `Output/Reports/` met aggregaten: 5 dagen spend €407,44, 652 clicks, 329 LPVs, 20 ICs, CTR 2,38%, CPC €0,625, LPV > IC rate 6,1%. Per hook variant de CTR/CPC splitsing (op basis van de 04-21 rapport snapshot).
   - **Waarom:** als heractivering uitblijft, verdampt het leerresultaat van 5 run-dagen. Zelfs als heractivering komt, is deze baseline nodig om iteratie 2 prestaties tegen af te zetten. Meta's aggregate laat zien: CTR stabiel rond 2,3%, CPC rond €0,62 — dat is de nul-lijn waar nieuwe creatives tegen moeten presteren.
   - **Hoe:** markdown per hook (H11, H12, H13 en latere H14/H15 als die gelopen hebben) met CTR, CPC, LPV, IC. Conclusie-hypothese voor iteratie 2: welke hook angle doorontwikkelen, welke creative elementen behouden, welk CTA format (cta5) blijft.
   - **Verwachte impact:** geen directe KPI impact. Wel discipline: volgende launch start met een expliciete hypothese in plaats van vanaf nul.
   - **Escalatie:** Groen, geen goedkeuring nodig.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-23_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers.
