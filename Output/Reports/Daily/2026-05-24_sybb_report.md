# SYBB Daily Report, 24 May 2026

## 1. Samenvatting
Geen activiteit op 24 mei. De Meta Ads campagne "2026: SYBB" staat op PAUSED (laatste update 19 april 2026) en de landingspagina kreeg nul bezoekers. Effectief een blanco dag, want zonder ads is er geen aansturing en zonder traffic geen funnel data.

## 2. Meta Ads Performance
Campagne ID: 120239435987290239
Status: PAUSED
Laatste update: 19 april 2026
Daily budget (configuratie): 100 EUR

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | 0,00 EUR | 0,00 EUR | n.v.t. |
| Impressions | 0 | 0 | n.v.t. |
| Clicks | 0 | 0 | n.v.t. |
| CTR | n.v.t. | n.v.t. | n.v.t. |
| CPC | n.v.t. | n.v.t. | n.v.t. |
| Frequency | n.v.t. | n.v.t. | n.v.t. |

Meta Insights API gaf een lege response voor yesterday, last_7d en last_30d. De campagne heeft sinds 19 april geen delivery gehad.

### Ad Variant Performance
Geen data beschikbaar. Met PAUSED campagne en nul impressies kunnen de h11 tot h15 varianten niet beoordeeld worden.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health
Domein: www.startyourballoonbusiness.com
Bron: PostHog project "Default project" (id 149694), tijdzone UTC.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 2,3 / dag | n.v.t. | n.v.t. |
| Unique visitors | 0 | 2,1 / dag | n.v.t. | n.v.t. |
| Bounce Rate | n.v.t. | n.v.t. | <55% | n.v.t. |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | n.v.t. |
| Scroll 25% | n.v.t. | n.v.t. | >80% | n.v.t. |
| Scroll 50% | n.v.t. | n.v.t. | >60% | n.v.t. |
| Scroll 75% | n.v.t. | n.v.t. | >40% | n.v.t. |
| Scroll 100% | n.v.t. | n.v.t. | >20% | n.v.t. |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | n.v.t. |

7-dagen pageview verloop op www.startyourballoonbusiness.com:

| Datum | Pageviews | Unique visitors |
|-------|-----------|-----------------|
| 18 mei 2026 | 4 | 3 |
| 19 mei 2026 | 6 | 6 |
| 20 mei 2026 | 3 | 3 |
| 21 mei 2026 | 1 | 1 |
| 22 mei 2026 | 2 | 2 |
| 23 mei 2026 | 0 | 0 |
| 24 mei 2026 | 0 | 0 |

Geen utm_content breakdown beschikbaar; het beetje traffic dat er nog binnenkomt is organisch en zonder UTM tags.

## 4. Funnel Drop-off
Pageview (0) → Scroll 50% (0) → CTA Click (0) → /booking (0)

Funnel niet meetbaar: zonder bezoekers is er geen drop-off te analyseren.

**Grootste lek:** Het lek zit bovenaan, namelijk acquisitie. Er komt geen traffic binnen omdat de ads uit staan.

## 5. Rode Vlaggen
- Campagne "2026: SYBB" staat op PAUSED sinds 19 april 2026 (35+ dagen geen delivery)
- Landingspagina kreeg 0 bezoekers op 23 en 24 mei (twee dagen achter elkaar nul)
- 7-daags pageview gemiddelde is gezakt naar 2,3 per dag, allemaal organisch
- Geen enkele utm_content waarde gezien in de afgelopen 24 uur, dus zelfs eerdere ad cookies converteren niet meer

## 6. Top 3 Acties voor Vandaag
1. **Beslissen of de SYBB campagne weer aan moet**
   Wat: keuze maken tussen relaunch, archiveren of in koelkast laten
   Waarom: campagne is 35+ dagen PAUSED en daarmee staat de hele funnel stil
   Hoe: korte check met Robin over budget en prioriteit voor Q2/Q3 2026
   Verwachte impact: dit deblokkeert alle vervolgmetingen en het rapport zelf
   Escalatie: Geel (Robin goedkeuring vereist)

2. **Bij relaunch eerst pre-flight check op landingspagina en tracking**
   Wat: voor reactivatie verifiëren dat www.startyourballoonbusiness.com nog correct gepixeled is en de UTM conventie (utm_source=meta, utm_medium=cpc, utm_campaign=sybb, utm_content=hXX_bX_ctaX, utm_term=batch_X) gerespecteerd wordt
   Waarom: tijdens de stille periode kan er front-end of GTM drift optreden zonder dat het opvalt
   Hoe: een testbezoek met een test-UTM en valideren dat het event in PostHog landt onder www.startyourballoonbusiness.com
   Verwachte impact: voorkomt dat budget verbrand wordt op een gebroken meetketen
   Escalatie: Groen (auto, gewoon uitvoeren)

3. **Rapportage continueren of bewust opschorten**
   Wat: kiezen of de daily SYBB report blijft draaien op nul-data of pauzeert tot de campagne herleeft
   Waarom: dagelijkse "alles nul" rapporten verlagen de signaal-ruisverhouding; beter wekelijks tot de campagne weer loopt
   Hoe: launchd job tijdelijk uit zetten of frequentie naar weekly bij geen-activiteit
   Verwachte impact: minder ruis in dagelijkse briefings, focus terug op actieve experimenten
   Escalatie: Geel (Robin beslissing)

---

## Data bronnen
- Meta Ads: Pipeboard Meta Ads MCP, account act_567892422940728 (Sempertex Ad Account), campagne id 120239435987290239
- PostHog: project "Default project" id 149694, organization "Sempertex Europe", host filter www.startyourballoonbusiness.com
- Gegenereerd op: 25 mei 2026
- Rapportdatum: 24 mei 2026
