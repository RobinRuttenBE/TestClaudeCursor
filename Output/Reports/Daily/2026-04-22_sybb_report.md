# SYBB Daily Report, 2026-04-22

## 1. Samenvatting

Tweede volle pauzedag op rij. Beide SYBB campagnes staan op PAUSED en er is gisteren (2026-04-22) nul impressies, nul clicks, nul spend geboekt op account `act_567892422940728`. De "2026: SYBB - Kopie" (120243293329420239) werd op 2026-04-20 17:09 gepauzeerd en is sindsdien niet meer heractiveerd. De oorspronkelijke "2026: SYBB" (120239435987290239) staat sinds 2026-04-19 14:29 op PAUSED. PostHog MCP is opnieuw niet beschikbaar in deze sessie, dus landing page health kan niet gevalideerd worden.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt |
|----------|----|----|-------------------|
| 2026: SYBB Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 |

### Performance gisteren vs voorgaande dagen

| Metric | 2026-04-22 | 2026-04-21 | 2026-04-20 | 2026-04-19 | 7d gemiddelde (laatste 5 run-dagen) |
|--------|-----------|-----------|-----------|-----------|-------------------|
| Spend | €0,00 | €0,00 | €77,85 | €46,57 | €71,54 per run-dag |
| Impressions | 0 | 0 | 4.287 | 3.328 | 5.119 |
| Clicks (all) | 0 | 0 | 119 | 76 | 116 |
| Link clicks | 0 | 0 | 75 | 50 | 65 |
| CTR | n.v.t. | n.v.t. | 2,78% | 2,28% | 2,26% |
| CPC (all) | n.v.t. | n.v.t. | €0,65 | €0,61 | €0,62 |
| Frequency | n.v.t. | n.v.t. | 1,34 | 1,35 | 1,37 |
| Landing Page Views (Meta pixel) | 0 | 0 | 63 | 34 | 55 |
| Initiate Checkout | 0 | 0 | 2 | 2 | 4 |

*7d gemiddelde berekend over 2026-04-15 t/m 2026-04-19 (origineel) en 2026-04-19 t/m 2026-04-20 (kopie). Alleen dagen met spend meegerekend.*

**Trend:** sinds 2026-04-20 17:09 staat alles stil. 48+ uur geen learning, geen nieuwe LPV data, geen nieuwe IC data. Het algoritme verliest momentum: de ad sets moeten bij heractivering opnieuw door de learning phase, wat typisch 2 tot 4 dagen hogere CPC betekent.

### Ad variant performance

Niet van toepassing vandaag. Geen ad-level data beschikbaar voor 2026-04-22 omdat geen enkele ad heeft gelopen. De laatste ad-level snapshot staat in het rapport van 2026-04-21 (cumulatief over 19 + 20 april): H12 (b3_cta5) was beste variant op CTR/CPC, H13 (b3_cta5) slechtst. Dat blijft het actueelste beeld tot heractivering.

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

Bedenk wel: zelfs als PostHog beschikbaar was, zou de landing page vandaag voornamelijk directe + organisch verkeer meten, niet Meta-attributed verkeer. Die baseline is nuttig (hoe presteert LP zonder betaald verkeer?), maar biedt geen inzicht in Meta > LP mismatch.

## 4. Funnel Drop-off

Niet te berekenen voor 2026-04-22: geen instroom vanuit Meta, geen PostHog. De laatste meetbare funnel-slice kwam uit 2 run-dagen (19 + 20 april):

Link clicks (125) > Meta LPV (100, 80%) > Initiate Checkout (6, 4,8% van clicks / 6% van LPV)

**Observatie:** dit gat blijft staan. Zodra campagnes heractiveren zou ik het eerste ingreep-signaal zoeken op de Meta LPV > IC conversie (nu 6% over klein sample). Als die na 3 dagen onder 4% zakt is er een landing page of offer mismatch.

## 5. Rode Vlaggen

- **Tweede dag op rij zonder live SYBB campagne.** 2026-04-21 en 2026-04-22 allebei nul spend. "2026: SYBB Kopie" is sinds 2026-04-20 17:09 niet heractiveerd. Als dit onbedoelde pauze is, loopt er learning phase verlies op (bij herstart typisch 2 tot 4 dagen verhoogde CPC). Als dit bewust was, ontbreekt een beslissingslog.
- **PostHog MCP structureel down in de dagelijkse flow.** 2026-04-19, 2026-04-20, 2026-04-21 en nu 2026-04-22 achter elkaar zonder PostHog data. Vier rapporten op rij zonder landing page observability is geen incident meer, dat is een kapotte pijplijn.
- **Data-stilstand creëert beslissings-stilstand.** De beste variant-hypothese (H12 wint op CTR/CPC, H13 verliezen) staat nu 72+ uur op pauze gebaseerd op slechts 2 run-dagen. Dat is te klein sample om definitieve conclusies te trekken, maar te groot om te negeren.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag: heractiveren, killen, of rebuilden?**
   - **Wat:** Robin check met team of de pauze op 2026-04-20 bewust was (budget hold, nieuwe creatives in productie, campagne-afronding voor nieuwe launch) of per ongeluk.
   - **Waarom:** elke dag stilstand kost leerdata. Meta learning phase reset komt eraan. De H12 vs H13 vraag staat 72+ uur op pauze met klein sample.
   - **Hoe:** bij heractivering van "2026: SYBB Kopie": zet H13 op PAUSED direct, houd H11 en H12 actief, laat 3 volle dagen draaien zonder ingrepen. Bij rebuild: documenteer wat de bestaande 2 dagen data ons leren voor de volgende iteratie (H12 hook, CTA5 format, B3 targeting).
   - **Verwachte impact:** terugkeer naar €50 tot €80 per dag spend met 2 tot 4 IC's per dag binnen 3 dagen na herstart.
   - **Escalatie:** Geel, Robin goedkeuring vereist.

2. **Herstel PostHog MCP toegang voor de daily flow.**
   - **Wat:** PostHog MCP server toevoegen of reactiveren in Claude Code config zodat `posthog_*` tools verschijnen in de deferred tool lijst.
   - **Waarom:** vier dagen op rij zonder landing page data ondermijnt de hele waarde van dit rapport. Cross-referencing Meta > LP is de belangrijkste beslissingsinput in de SKILL.md.
   - **Hoe:** verifieer `~/.claude/claude_desktop_config.json` of project-level `.claude/settings.local.json` voor PostHog MCP entry. Haal opnieuw API key uit PostHog project "Default project" als token verlopen is. Test na herstart met een `posthog_query_insight` call.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run, cross-referencing Meta CTR vs LP bounce weer mogelijk.
   - **Escalatie:** Oranje, tooling ingreep.

3. **Document wat we uit de 2 run-dagen hebben geleerd voor de volgende iteratie.**
   - **Wat:** korte markdown in `Output/Reports/` met de H11 vs H12 vs H13 snapshot, de 6% LPV > IC rate, en een hypothese voor wat de volgende iteratie moet testen.
   - **Waarom:** als heractivering niet komt, verdampt de leerdata. Als heractivering wel komt, is een baseline nuttig om tegen te vergelijken.
   - **Hoe:** samenvatten: H12 CTR 3,58% vs H11 2,51% vs H13 2,07%, H13 CPC €0,92 ruim boven target, LPV > IC rate 6% (klein sample), frequency onder 1,5 dus fatigue geen factor.
   - **Verwachte impact:** geen directe KPI impact, wel betere beslissingsdiscipline bij volgende launch.
   - **Escalatie:** Groen, geen goedkeuring nodig.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-22_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard), werkend. PostHog MCP, niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers.
