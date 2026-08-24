# SYBB Daily Report: 2026-08-23

## 1. Samenvatting
De campagne "2026: SYBB" staat sinds 19 april 2026 op PAUSED in Meta Ads Manager. Er was op 23 augustus geen spend, geen impressies en geen kliks, en ook de 7 dagen ervoor (16 t/m 22 augustus) was er nul activiteit. De landing page startyourballoonbusiness.com kreeg gisteren 2 directe bezoeken (geen ad traffic), tegenover 0 bezoeken in de 7 dagen ervoor. Er valt vandaag dus niets te optimaliseren aan ads of pagina. De kernvraag is strategisch: hervatten we de SYBB campagne, of leggen we de rapportage om naar de event pagina's op sempertexeurope.com waar SYBB inmiddels via verkoopt?

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (ID 120239435987290239), status: **PAUSED** (sinds 2026-04-19), dagbudget €100.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads, dus geen variant data. De variantentabel (h11 t/m h15) is niet van toepassing zolang de campagne gepauzeerd is.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

Opmerking: de kopie-campagne "2026: SYBB - Kopie" (aangemaakt 19 april) staat eveneens op PAUSED.

## 3. Landing Page Health

startyourballoonbusiness.com, bron: PostHog project "STX EU".

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bezoekers | 2 | 0 | n.v.t. | ⚪ |
| Pageviews | 2 | 0 | n.v.t. | ⚪ |
| Bounce Rate | 100% | geen data | <55% | ⚪ |
| Avg Session Duration | 0s | geen data | >90s | ⚪ |
| Scroll depth (25/50/75/100%) | onvoldoende data | geen data | zie targets | ⚪ |
| CTA Click Rate | 0% (0 clicks) | geen data | >4% | ⚪ |

Status ⚪ betekent: sample te klein voor een oordeel. Twee bezoeken zeggen niets over paginakwaliteit.

**Herkomst van de 2 bezoeken:** referrer `$direct`, maar mét `utm_content=h11_b3_cta5` in de URL. Dat is dus geen live ad traffic (er draaien geen ads), maar iemand die een oude getagde ad-URL heropende, bijvoorbeeld via browsergeschiedenis, een bookmark of een gedeelde link. Positief detail: de UTM capture op de pagina werkt nog correct.

## 4. Funnel Drop-off
Niet berekend. Met 2 sessies en 0 CTA clicks is een funnel analyse statistisch betekenisloos.

Pageview (2) → Scroll 50% (geen data) → CTA Click (0) → /booking (0)

**Grootste lek:** n.v.t. bij deze volumes.

## 5. Rode Vlaggen 🚩
- **Campagne al ruim 4 maanden gepauzeerd** terwijl de daily report flow nog draait alsof de campagne live is. Dit is geen performance probleem maar een systeem-mismatch.
- **De skill-aanname klopt niet meer met de werkelijkheid:** SYBB verkoopt inmiddels via event pagina's op sempertexeurope.com, niet via de landing page startyourballoonbusiness.com. Alle recente PostHog events (wholesaler_*, family_*, calc_*) zitten op sempertexeurope.com.
- Geen CPC-, frequency- of bounce-alerts, want er is geen data om op te alerten.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de toekomst van dit rapport.**
   Wat: kies tussen (a) SYBB campagne hervatten, (b) de daily-sybb-report skill ombouwen naar de event pagina funnel op sempertexeurope.com, of (c) het dagelijkse rapport pauzeren tot de campagne weer live gaat.
   Waarom: 4+ maanden nul data betekent dat elk dagelijks rapport nu lege tabellen produceert.
   Hoe: strategiekeuze door Robin, daarna skill/command aanpassen.
   Verwachte impact: rapportage meet weer iets dat er toe doet.
   Escalatie: 🔴 Rood (strategie).

2. **Bij hervatting: begin met de bewezen winnaar-set, niet met alle varianten.**
   Wat: als de campagne weer aan gaat, herstart met de best presterende hooks uit de laatste actieve periode en het 70-20-10 principe.
   Waarom: na 4 maanden pauze is de auction learning weg, klein herstarten beperkt verspilling.
   Hoe: Meta Ads Manager, bestaande campagne reactiveren of de Kopie-versie inzetten.
   Verwachte impact: snellere terugkeer naar rendabele CPC.
   Escalatie: 🟡 Geel (Robin goedkeuring).

3. **Niets wijzigen aan de landing page.**
   Wat: geen copy-, CTA- of structuurwijzigingen op startyourballoonbusiness.com op basis van deze data.
   Waarom: 2 directe bezoeken met 100% bounce is ruis, geen signaal.
   Hoe: geen actie.
   Verwachte impact: voorkomt optimaliseren op toeval.
   Escalatie: 🟢 Groen.

---
*Databronnen: Meta Ads via Pipeboard (act_567892422940728, directe JSON-RPC calls), PostHog project STX EU (id 149694). Gegenereerd op 2026-08-24.*
