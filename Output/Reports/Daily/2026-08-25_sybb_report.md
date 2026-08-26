# SYBB Daily Report: 25 augustus 2026

## 1. Samenvatting
Geen activiteit in de SYBB funnel gisteren. De campagne "2026: SYBB" staat sinds april op PAUSED en het hele ad account had op 25 augustus nul spend en nul delivery. De landing page startyourballoonbusiness.com kreeg gisteren 0 bezoekers (2 bezoekers in de hele afgelopen week, beiden gebounced). Dit is een bevestiging van het bekende beeld: SYBB draait momenteel niet als actieve funnel, verkoop loopt via de event pagina's op sempertexeurope.com.

## 2. Meta Ads Performance

**Campagne status:** `2026: SYBB` (ID 120239435987290239) staat op **PAUSED** (laatst gewijzigd 19 april 2026). Ook de kopie-campagne "2026: SYBB - Kopie" is gepauzeerd. Accountniveau check (act_567892422940728) bevestigt: geen enkele campagne leverde gisteren.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | Afgelopen 7d | Target | Status |
|--------|----------|--------------|--------|--------|
| Bezoekers | 0 | 2 | n.v.t. | ⚪ |
| Pageviews | 0 | 2 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | 100% | <55% | ⚪ |
| Avg Session Duration | n.v.t. | 0s | >90s | ⚪ |
| Scroll depth | geen data | geen data | >60% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

Toelichting: met 0 tot 2 bezoekers zijn targets niet zinvol te beoordelen (⚪ = onvoldoende data). PostHog bevat momenteel ook geen scroll depth of CTA click events; de actieve events in het project (wholesaler_*, family_*, calc_*, inspiration_*) horen bij www.sempertexeurope.com, het enige domein dat nog pageviews stuurt. Er is geen utm_campaign property met recente waarden, dus ook geen sybb-getagd verkeer op het hoofddomein.

## 4. Funnel Drop-off
Niet van toepassing: geen verkeer, dus geen funnel om te meten.

## 5. Rode Vlaggen 🚩
Geen performance-anomalieën (er draait niets), maar wel twee structurele signalen:

1. **Skill/tracking mismatch:** de daily-sybb-report skill meet startyourballoonbusiness.com, maar SYBB verkoopt inmiddels via event pagina's op sempertexeurope.com. De rapportage kijkt dus naar een dode pagina.
2. **Ontbrekende events:** scroll depth en CTA click events bestaan niet (meer) in PostHog. Als SYBB ads opnieuw live gaan, is er geen on-page meetinstrumentarium klaar.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de SYBB campagne herstart.**
   Wat: bepaal of en wanneer "2026: SYBB" weer live gaat, en naar welke bestemming (event pagina's op sempertexeurope.com in plaats van de oude LP).
   Waarom: campagne staat al 4+ maanden op PAUSED terwijl het dagelijkse rapport blijft draaien.
   Hoe: strategiebeslissing Robin, daarna Meta Ads Manager.
   Escalatie: Rood (strategie).

2. **Update de daily-sybb-report skill naar de werkelijke funnel.**
   Wat: pas `skills/daily-sybb-report/SKILL.md` aan zodat PostHog queries op de SYBB event pagina's van sempertexeurope.com meten in plaats van startyourballoonbusiness.com.
   Waarom: het rapport meet nu een domein zonder data; het bestaande geheugen bevestigt dat de funnel is verhuisd.
   Hoe: skill-bestand aanpassen, kan direct.
   Escalatie: Geel (Robin goedkeuring op de nieuwe meetdefinitie).

3. **Zet on-page tracking klaar voor een herstart.**
   Wat: scroll depth (25/50/75/100%) en CTA click events implementeren op de SYBB bestemmingspagina's.
   Waarom: deze events ontbreken volledig in PostHog; zonder deze data is het rapport bij een herstart blind op engagement en conversie.
   Hoe: PostHog snippet/event tracking op de event pagina's (Wix), volgens `tracking-standards`.
   Escalatie: Oranje (site-aanpassing nodig).

---
*Databronnen: Meta Ads via Pipeboard (directe JSON-RPC, account act_567892422940728) en PostHog project "STX EU" (eu.posthog.com, project 149694). Gegenereerd op 26 augustus 2026.*
