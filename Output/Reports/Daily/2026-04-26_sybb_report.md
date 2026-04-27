# SYBB Daily Report, 2026-04-26

## 1. Samenvatting

Campagne "2026: SYBB" stond gisteren op PAUSED, dus geen Meta Ads spend, impressies of clicks. De landing page kreeg 5 pageviews uit 4 organische sessies (geen UTM tagging), versus 241 pageviews in de voorgaande 7 dagen toen de campagne nog (deels) actief was. Sinds ~21 april is het verkeer gekelderd van 100+ pv/dag naar 3 a 5 pv/dag, wat bevestigt dat de paid funnel volledig stilligt.

## 2. Meta Ads Performance

Campagne ID: `120239435987290239`. Status: **PAUSED** (sinds 19-04, laatst geupdatet 19-04-2026).

| Metric        | Gisteren (26-04) | 7d Totaal (19-25) | 7d Daggemiddelde | Trend |
|---------------|------------------|-------------------|------------------|-------|
| Spend         | EUR 0,00         | EUR 43,81         | EUR 6,26         | downarrow (paused) |
| Impressions   | 0                | 2.756             | 394              | downarrow (paused) |
| Clicks (all)  | 0                | 61                | 9                | downarrow (paused) |
| Link clicks   | 0                | 36                | 5                | downarrow (paused) |
| CTR           | n/a              | 2,21%             | 2,21%            | n/a   |
| CPC (all)     | n/a              | EUR 0,72          | EUR 0,72         | rood (>0,50 target) |
| Frequency     | n/a              | 1,35              | 1,35             | groen (<3) |
| LP Views (Meta) | 0              | 34                | 5                | downarrow |
| Initiate checkouts | 0           | 2                 | 0,3              | downarrow |

**Beste variant gisteren:** n/a, geen ad delivery.
**Slechtste variant gisteren:** n/a, geen ad delivery.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric              | Gisteren (26-04) | 7d Daggemiddelde | Target | Status |
|---------------------|------------------|------------------|--------|--------|
| Pageviews           | 5                | 34,4             | n/a    | n/a    |
| Unique visitors     | 4                | 27,9             | n/a    | n/a    |
| Sessions            | 4                | 29,3             | n/a    | n/a    |
| Bounce Rate         | 75% (3/4 single page) | n.b.        | <55%   | rood (kleine n) |
| UTM tagged sessions | 0                | n.b.             | n/a    | rood (campagne paused) |
| CTA clicks          | 0                | n.b.             | >4%    | rood   |

**Pagina verdeling gisteren:**
- `/` homepage: 3 pageviews, 3 sessions
- `/review`: 1 pageview, 1 session
- `/thank-you-page`: 1 pageview, 1 session (mogelijk een legacy/test event, geen voorafgaande funnel stap zichtbaar)

NB. Scroll depth, session duration en CTA click events konden niet betrouwbaar worden gerapporteerd: te kleine sample (n=4 sessies) en het `$session_duration` veld is in deze property structuur niet geaggregeerd op te halen via HogQL sum().

## 4. Funnel Drop off

Niet bruikbaar te berekenen op n=4 sessies. Indicatief:

Pageview homepage (3) -> Scroll 50% (onbekend) -> CTA click (0) -> /booking (0)

**Grootste lek:** de funnel is feitelijk dood, want er komt geen ad traffic binnen.

## 5. Rode Vlaggen

- **Campagne staat op PAUSED.** Dit is de hoofdoorzaak: nul spend, nul impressies, nul ad clicks. Alle KPI vergelijkingen zijn vandaag betekenisloos zolang de campagne uit staat.
- **0 UTM tagged sessies.** Bevestigt dat er geen paid acquisitie heeft plaatsgevonden op 26-04.
- **/thank-you-page pageview zonder voorafgaande funnel stappen.** Mogelijk direct verkeer naar bookmark, een test, of een tracking gat in de booking flow. Verifieren wanneer ad traffic terugkomt.
- **CPC EUR 0,72 over de laatste 7d** ligt boven het target (<EUR 0,50). Dit moet het hoofdpunt zijn bij het herstarten van de campagne.

## 6. Top 3 Acties voor Vandaag

1. **Beslissen of "2026: SYBB" weer aangezet wordt, en zo ja onder welke voorwaarden.**
   - Wat: campagne reactiveren of formeel afschalen.
   - Waarom: de funnel ligt sinds ~21-04 stil. Zonder ad spend is er geen data om op te optimaliseren.
   - Hoe: Meta Ads Manager, campagne 120239435987290239 op ACTIVE zetten, of nieuwe duplicaat (120243293329420239 "2026: SYBB - Kopie", ook PAUSED) gebruiken.
   - Verwachte impact: traffic terug naar 100+ pv/dag, herstart van CTR, CPC en LP metrics.
   - Escalatie: Geel, vraagt Robin's beslissing.

2. **Onderzoek waarom CPC over de laatste actieve week op EUR 0,72 lag (44% boven target).**
   - Wat: per ad variant en adset CPC analyseren over 19-04 tot 25-04 voor de pause.
   - Waarom: bij herstart wil je niet hetzelfde CPC niveau accepteren. 44% boven target.
   - Hoe: in volgende rapport, Meta MCP `get_insights` op `level=ad` met `breakdown=ad_format_asset` voor de actieve periode.
   - Verwachte impact: identificeert welke variant de CPC opdrijft, basis voor 70-20-10 herallocatie.
   - Escalatie: Groen, kan ik vandaag als follow up draaien.

3. **Verifieer UTM tagging in de campagne URLs voor reactivering.**
   - Wat: controleer dat alle ad URLs `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X` (lowercase) bevatten.
   - Waarom: gisteren 0 UTM tagged sessies, terwijl er over de hele afgelopen week ook geen UTM segmentatie bruikbaar was in deze run, dus risico dat tagging brak is of niet doorpropageert.
   - Hoe: Meta Ads Manager per ad creative URL inspecteren tegen `tracking-standards.md` (Sempertex Europe convention).
   - Verwachte impact: per ad variant performance wordt traceerbaar in PostHog rapportages.
   - Escalatie: Geel (Robin goedkeuring per nieuwe URL).

---

**Datapunten verzameld via:**
- Meta Ads MCP (Pipeboard), account `act_567892422940728`, campagne `120239435987290239`.
- PostHog MCP, project "Default project" (149694), host `www.startyourballoonbusiness.com`.

**Rapport opgeslagen:** `Output/Reports/Daily/2026-04-26_sybb_report.md`.
