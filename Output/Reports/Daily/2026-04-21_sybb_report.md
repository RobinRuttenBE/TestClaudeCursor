# SYBB Daily Report, 2026-04-21

## 1. Samenvatting

Er is gisteren geen SYBB advertentieactiviteit geweest. De enige live campagne "2026: SYBB - Kopie" (ID 120243293329420239) is op 2026-04-20 om 17:09 gepauzeerd en heeft op 2026-04-21 nul impressies, nul clicks en nul spend geboekt. De oorspronkelijke "2026: SYBB" (ID 120239435987290239) staat sinds 2026-04-19 op PAUSED. PostHog MCP is in deze sessie niet beschikbaar, dus landing page health is niet te valideren.

**Data status:**
- Meta Ads MCP (Pipeboard): werkend, account `act_567892422940728` (Sempertex Ad Account)
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in de deferred tool lijst)

## 2. Meta Ads Performance

### Campagne status

| Campagne | ID | Status | Laatst bijgewerkt |
|----------|----|----|-------------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | 2026-04-20 17:09 |
| 2026: SYBB (origineel) | 120239435987290239 | PAUSED | 2026-04-19 14:29 |

### Performance gisteren vs laatste run-dagen

| Metric | 2026-04-21 | 2026-04-20 | 2026-04-19 | 7d totaal (live ran alleen 19+20) |
|--------|-----------|-----------|-----------|-------------------|
| Spend | €0,00 | €77,85 | €46,57 | €124,42 |
| Impressions | 0 | 4.287 | 3.328 | 7.615 |
| Clicks (all) | 0 | 119 | 76 | 195 |
| Link clicks | 0 | 75 | 50 | 125 |
| CTR | n.v.t. | 2,78% | 2,28% | 2,56% |
| CPC (all) | n.v.t. | €0,65 | €0,61 | €0,64 |
| Frequency | n.v.t. | 1,34 | 1,21 | 1,42 (7d) |
| Landing Page Views (Meta pixel) | 0 | 63 | 37 | 100 |
| Initiate Checkout | 0 | 2 | 4 | 6 |
| IC action value | €0 | €700 | €1.400 | €2.100 |

**Trend vs dag 1:** Dag 2 (20 april) toonde stijgende CTR (2,28% → 2,78%) en stijgende LPV conversie (74% → 84% van link clicks), maar IC daalde van 4 naar 2, en CPC steeg licht. Frequency op dag 2 nog ruim onder 3, dus fatigue was geen factor. Dag 3 (21 april) is niet gedraaid.

### Ad variant performance (cumulatief over 2 live dagen: 19+20 april)

| Ad | Impressions | Clicks | Link clicks | CTR | CPC (all) | Spend | LPV | IC | IC waarde |
|----|-------------|--------|-------------|-----|-----------|-------|-----|----|-----------|
| **H11, B3, CTA5** | 3.782 | 95 | 58 | 2,51% | €0,54 | €51,34 | 42 | 3 | €1.050 |
| **H12, B3, CTA5** | 1.367 | 49 | 25 | 3,58% | €0,53 | €25,87 | 22 | 2 | €700 |
| **H13, B3, CTA5** | 2.466 | 51 | 42 | 2,07% | €0,92 | €47,21 | 36 | 1 | €350 |

**Beste variant:** H12 heeft de hoogste CTR (3,58%) en laagste CPC (€0,53), en zette op dag 2 zelfs een uitschieter neer (CTR 4,14%, 17 LPV uit 17 link clicks = 100% Meta-LPV rate). H12 is de duidelijke winnaar qua engagement-efficiëntie.

**Slechtste variant:** H13 heeft de laagste CTR (2,07%) en hoogste CPC (€0,92). Op dag 2 steeg H13 CPC zelfs naar €1,02. Dit is een pauzeer-kandidaat zodra de campagne heractiveert, mits er geen creative-fix plaatsvindt.

**Volume vs efficiency trade-off:** H11 krijgt het meeste budget en levert 3 van de 6 IC's op, maar op CTR/CPC-basis wint H12. Overweeg budget van H13 naar H12 te verschuiven bij herstart.

## 3. Landing Page Health

**Niet beschikbaar.** PostHog MCP is niet ingeladen in deze sessie. Geen pageviews, bounce rate, scroll depth, session duration, CTA click rate of session recordings voor `startyourballoonbusiness.com` op te halen.

| Metric | Target | Status |
|--------|--------|--------|
| Bounce Rate | <55% | ⚫ geen data |
| Avg Session Duration | >90s | ⚫ geen data |
| Scroll 25% | >80% | ⚫ geen data |
| Scroll 50% | >60% | ⚫ geen data |
| Scroll 75% | >40% | ⚫ geen data |
| Scroll 100% | >20% | ⚫ geen data |
| CTA Click Rate | >4% | ⚫ geen data |

## 4. Funnel Drop-off

Niet te berekenen zonder PostHog. Enige funnel-indicatie uit Meta pixel over 2 live dagen:

Link clicks (125, 100%) → Meta LPV (100, 80%) → Initiate Checkout (6, 4,8% van clicks / 6% van LPV)

**Gat tussen link clicks en Meta LPV:** 20% van mensen die klikt registreert niet als landing page view. Normaal verlies, maar zonder PostHog pageview data niet te kruisvalideren. Dit is hetzelfde observatiepunt als in het rapport van 2026-04-19.

## 5. Rode Vlaggen

- 🚩 **Geen live SYBB campagne op 2026-04-21.** "2026: SYBB - Kopie" werd op 2026-04-20 17:09 gepauzeerd, na twee dagen vliegen. Ofwel was dit een bewuste pauze door Robin (budget bewaking, nieuwe iteratie voorbereiden), ofwel een ongewenste pauze. Als doel was doorlopend testen, is er nu 24+ uur data-verlies.
- 🚩 **PostHog MCP observability pijplijn faalt meerdere dagen op rij.** 2026-04-19, 2026-04-20, 2026-04-21 rapporten alle zonder PostHog data. Dit is een structureel tooling incident, geen data incident.
- 🚩 **H13 CPC hardloopt weg (€0,92 gemiddeld, €1,02 op dag 2).** Ruim boven €0,50 target. Bij herstart pauze of creative-fix nodig.
- 🚩 **IC daalde van 4 naar 2 tussen dag 1 en dag 2** terwijl spend steeg van €47 naar €78. CPA per IC verdubbelde van €11,64 naar €38,93. Klein sample, maar richting is slecht.

## 6. Top 3 Acties voor Vandaag

1. **Bevestig status van "2026: SYBB - Kopie" pauze en beslis: heractiveren of laten staan.**
   - **Wat:** check bij Robin of de pauze op 2026-04-20 17:09 bewust was.
   - **Waarom:** zonder live campagne geen leerdata, en 2 dagen is te kort voor statistisch significante conclusies over H11/H12/H13.
   - **Hoe:** als heractiveren, overweeg direct H13 op PAUSED te zetten (hoogste CPC, laagste CTR) en budget te verschuiven naar H12 (beste CTR/CPC combinatie).
   - **Verwachte impact:** 20-30% lagere CPA per IC door H13 weg te nemen.
   - **Escalatie:** Geel (Robin goedkeuring vereist op campagne-aanpassingen).

2. **Herstel PostHog MCP toegang voor de morning-report flow.**
   - **Wat:** voeg PostHog MCP toe aan `.claude/settings.local.json` of verifieer dat de server in de Claude Code MCP config zit.
   - **Waarom:** drie opeenvolgende dagen geen landing page data. Zonder PostHog verliest het SYBB rapport bounce, scroll, CTA click rate en session recordings. Dat is 50% van de report-waarde.
   - **Hoe:** open PostHog project "Default project", haal API key op, registreer MCP server. Test met een `posthog_query_insight` of equivalent tool call na herstart.
   - **Verwachte impact:** volledig rapport vanaf eerstvolgende run.
   - **Escalatie:** Oranje (tooling ingreep, geen ad-data ingreep).

3. **Na heractivering: laat minstens 3 volle dagen draaien voor je variant-beslissingen neemt.**
   - **Wat:** bevries H11/H12/H13 setup na herstart, geen pauzes of budget-shifts tot 2026-04-24 avond.
   - **Waarom:** huidige sample (2 dagen, 125 link clicks, 6 IC) is te klein voor significantie. Dag-variance domineert het signaal.
   - **Hoe:** monitor dagelijks via dit rapport, documenteer observaties, grijp alleen in als rode vlag (frequency >3, CPC >€1 aanhoudend, bounce >70%) activeert.
   - **Verwachte impact:** betrouwbare winnaar-bepaling na ~7 dagen data.
   - **Escalatie:** Groen (discipline, geen ingreep vereist).

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-21_sybb_report.md`
**Data bronnen gebruikt:** Meta Ads MCP (Pipeboard) — werkend. PostHog MCP — niet beschikbaar.
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers.
