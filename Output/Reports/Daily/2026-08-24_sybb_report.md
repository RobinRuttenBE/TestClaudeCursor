# SYBB Daily Report — 2026-08-24

## 1. Samenvatting
Er draaide gisteren geen enkele Meta ad: de campagne "2026: SYBB" (en het hele ad account) staat op PAUSED en had nul spend, impressies en clicks over de volledige afgelopen 7 dagen. De landing page startyourballoonbusiness.com ontvangt sinds eind juli geen verkeer meer. Het enige echte SYBB signaal komt van de organische event-registratiepagina's op sempertexeurope.com: 13 pageviews van 10 unieke bezoekers gisteren, de beste dag van de week.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID 120239435987290239), status **PAUSED** sinds 19 april 2026.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Ook accountbreed (act_567892422940728) was er nul delivery in de periode 18 t/m 24 augustus. De kopie-campagne "2026: SYBB - Kopie" staat eveneens op PAUSED.

### Ad Variant Performance
Niet van toepassing: geen enkele ad had delivery, dus er is geen data per utm_content variant (h11 t/m h15).

## 3. Landing Page Health (startyourballoonbusiness.com)
**Geen data.** PostHog registreert in dit project momenteel uitsluitend verkeer op www.sempertexeurope.com. De landing page heeft sinds 31 juli 2026 nul verkeer, en de events die deze sectie nodig heeft (scroll depth, CTA clicks, /booking visits) bestaan niet in de projecttaxonomie. Ook UTM properties ontbreken volledig op de pageview events, dus segmentatie per ad variant is niet mogelijk.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll depth (25/50/75/100%) | niet gemeten | niet gemeten | zie targets | ⚪ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚪ |

### Context: sempertexeurope.com sitebreed (ter referentie)
| Metric | Gisteren | 7d totaal/gemiddelde |
|--------|----------|----------------------|
| Unieke bezoekers | 4.638 | 13.515 |
| Pageviews | 12.004 | 46.218 |
| Sessies | 4.739 | 14.403 |
| Bounce rate | 87,2% | 80,5% |
| Gem. sessieduur | 72s | 173s |

Gisteren had de hoofdsite opvallend veel bezoekers (ca. 2,4x het daggemiddelde) maar met veel hogere bounce (87% vs 80%) en minder dan de helft van de normale sessieduur. Dat patroon past bij een piek van laagwaardig of bot-verkeer, of een verkeersbron die niet matcht met de content.

## 4. Funnel Drop-off
**Niet meetbaar.** De werkelijke SYBB funnel loopt via de event-registratiepagina's op sempertexeurope.com (`/event/start-your-balloon-business-professional-7/register` en de Duitse variant). Tussen de registratiepagina en een bevestiging bestaat geen meetpunt: er is geen "registratie voltooid" event in PostHog. Het enige harde conversie-event in het project is `/shop/confirmation`, en dat is de webshop.

### SYBB event-pagina verkeer (organisch, sempertexeurope.com)
| Datum | Pageviews | Unieke bezoekers |
|-------|-----------|------------------|
| 18 aug | 13 | 9 |
| 19 aug | 10 | 8 |
| 20 aug | 6 | 4 |
| 21 aug | 9 | 9 |
| 22 aug | 3 | 2 |
| 23 aug | 1 | 1 |
| **24 aug** | **13** | **10** |
| 7d gemiddelde | 7,9/dag | 6,1/dag |

Gisteren was de beste dag van de week qua interesse in de workshop, zonder enige ad spend.

## 5. Rode Vlaggen 🚩
1. **Het rapport meet de verkeerde funnel.** De skill gaat uit van startyourballoonbusiness.com met utm_content varianten en een /booking conversie. Die pagina krijgt nul verkeer en die events bestaan niet. De echte funnel (event-registratiepagina's) heeft geen conversie-event, dus conversie is nergens te berekenen.
2. **Campagne al 4+ maanden gepauzeerd.** "2026: SYBB" staat sinds 19 april op PAUSED. Zolang dit zo is, levert de Meta-sectie van dit rapport structureel nullen op.
3. **Sitebrede bounce-piek gisteren.** 87,2% bounce bij 4.638 bezoekers en een gehalveerde sessieduur op sempertexeurope.com. Valt buiten SYBB scope maar verdient een korte check (botverkeer of een verkeersbron-mismatch).

## 6. Top 3 Acties voor Vandaag
1. **Beslis over de campagnestatus.** Wat: bepaal of "2026: SYBB" gereactiveerd wordt (met nieuwe landingsbestemming: de event-registratiepagina's) of dat het dagelijkse rapport wordt omgebouwd naar de organische event funnel. Waarom: 7 dagen nul delivery maakt elke ads-sectie leeg. Hoe: keuze Robin, daarna campagne-instellingen in Meta Ads Manager. Verwachte impact: het rapport meet weer iets dat bestaat. Escalatie: Rood (strategie).
2. **Voeg een registratie-conversie-event toe.** Wat: een `sybb_registration_submit` (of vergelijkbaar) event op de event-registratiepagina's van sempertexeurope.com. Waarom: er staat nu geen enkel meetpunt tussen registratiepagina en bevestiging, dus conversie is onmeetbaar. Hoe: PostHog snippet of autocapture action op de submit-knop van `/event/start-your-balloon-business-*/register`. Verwachte impact: funnel drop-off wordt eindelijk berekenbaar. Escalatie: Geel (Robin goedkeuring, daarna implementatie).
3. **Check de bounce-piek van gisteren op de hoofdsite.** Wat: bekijk in PostHog web analytics de verkeersbronnen en botclassificatie ($virt_traffic_type) voor 24 augustus. Waarom: 2,4x normaal bezoekersvolume met 87% bounce en 72s sessieduur wijst op laagwaardig verkeer. Hoe: PostHog web analytics, breakdown op referring domain en traffic type. Verwachte impact: uitsluiten dat er een trackingprobleem of botgolf speelt. Escalatie: Groen (auto/analyse).

---
*Databronnen: Meta Ads via Pipeboard (directe JSON-RPC, account act_567892422940728) en PostHog project "STX EU" (eu.posthog.com, project 149694). Geen Google services gebruikt. Gegenereerd op 2026-08-25.*
