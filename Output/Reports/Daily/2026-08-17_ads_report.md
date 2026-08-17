# Meta Ads Rapport, 17 augustus 2026

**Pipeboard is niet geautoriseerd, tiende dag op rij.** Stap 1 tot en met 4 konden niet draaien: geen accounts, campagnes, spend, impressions, CTR, CPC, CPM of ROAS. De sessie is niet-interactief, dus autoriseren kan hier niet. Dat gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

Wat wel kon: PostHog. Hieronder de staat van de bestemming waar je ads straks naartoe gaan.

---

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| Geen data | Pipeboard niet geautoriseerd | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Totaal spend: EUR 0,00 over de laatste 30 dagen.** Dat is geen aanname uit een ontbrekende API. PostHog bevestigt het onafhankelijk: geen enkele sessie in 30 dagen heeft `utm_source=meta` of `utm_medium=cpc`, en de kanaaltabel kent geen Paid Social en geen Paid Search.

### Kanalen, laatste 30 dagen

| Kanaal | Bezoekers | Aandeel |
|---|---|---|
| Direct | 15.753 | 73,2% |
| Referral | 3.451 | 16,0% |
| Organic Search | 1.658 | 7,7% |
| Email | 319 | 1,5% |
| AI | 241 | 1,1% |
| Organic Social | 94 | 0,4% |
| Organic Video | 8 | 0,0% |
| **Paid Social** | **0** | **0,0%** |
| **Paid Search** | **0** | **0,0%** |

---

## De belangrijkste vondst van vandaag

Gisteren noemde ik de hoge bounce op je categoriepagina's een defect. De entry-page data van deze week laat zien wat er precies gebeurt, en het is scherper dan gedacht.

| Entry page | Entries (7d) | Pageviews in die sessies | Pageviews per sessie | Bounce |
|---|---|---|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 283 | 283 | **1,00** | 97,9% |
| /folie-ballonnen | 229 | 229 | **1,00** | 96,5% |
| /en_GB/foil-balloons | 70 | 70 | **1,00** | 94,3% |
| /de/folienballons | 54 | 54 | **1,00** | 90,7% |
| /en_GB/shop/category/printed-latex-2912 | 49 | 49 | **1,00** | 95,9% |

Ter vergelijking, dezelfde week, gezonde pagina's:

| Entry page | Entries | Pageviews in die sessies | Pageviews per sessie | Bounce |
|---|---|---|---|---|
| / (homepage) | 366 | 8.386 | 22,9 | 3,2% |
| /en_GB | 165 | 3.454 | 20,9 | 17,7% |
| /fr/shop | 69 | 1.576 | 22,8 | 5,0% |
| /de/shop | 84 | 1.472 | 17,5 | 8,0% |

Kijk naar die middelste kolom. Wie via de homepage of een shop-overzicht binnenkomt, bekijkt gemiddeld 17 tot 23 pagina's. Wie op een van die vijf categoriepagina's landt, bekijkt er exact één. Niet gemiddeld één komma iets. Precies 1,00, over vijf verschillende pagina's in vier talen.

Dat is geen slechte pagina. Een slechte pagina heeft spreiding: sommige mensen klikken door, de meeste niet, en je komt uit op 1,3 of 1,6 pageviews per sessie. Exact 1,00 over honderden sessies betekent dat er nul doorkliks zijn. Geen enkele. Er zijn twee verklaringen die dat patroon geven: de pagina rendert niet (er is niets om op te klikken), of dit verkeer is niet menselijk en PostHog filtert het niet weg.

Beide verklaringen zijn erg. In het eerste geval verbrand je straks je hele foliebudget. In het tweede geval zijn 685 van je 7-daagse entries nep, en is elke conversieratio die je hierna meet vertekend.

**Dit is het enige wat vandaag telt: open die vijf URL's zelf in een incognitovenster.** Dat kost je twee minuten en beslist welke van de twee verklaringen waar is. Zonder dat antwoord kun je geen budget alloceren en geen benchmark vertrouwen.

---

## Underperformers

Geen ad-level data beschikbaar, dus geen CPC-, CTR-, frequency- of CPM-flags. De drempels uit stap 5 (CPC boven EUR 0,50, CTR onder 1,0%, frequency boven 3,5, CPM boven EUR 15,00) staan klaar voor de eerste run met werkende Pipeboard-toegang.

De underperformers die ik wel kan aanwijzen zitten op de site:

- **/en_GB/shop/category/foil-balloons-2915**, 97,9% bounce op 283 entries. Dit is je grootste Engelstalige folie-instap en hij levert nul doorkliks.
- **/folie-ballonnen**, 96,5% bounce op 229 entries. Zelfde patroon, Nederlandse versie.
- **/de/shop/category/latex-ballons-2911**, 100,0% bounce op 114 bezoekers.
- **/en_GB/shop/category/latex-balloons-2911**, 82,1% bounce, maar wel 109 pageviews op 55 entries. Deze doet het meetbaar beter en gedraagt zich als een echte pagina met een echt probleem.

---

## Top performers

- **Beste bounce**: homepage `/`, 3,2% op 378 bezoekers. Gezond.
- **Beste diepte**: homepage, 22,9 pageviews per sessie.
- **Beste kanaal zonder budget**: AI, 241 bezoekers in 30 dagen. ChatGPT stuurt 238 daarvan. Volledig gratis en niemand stuurt het aan.
- **Beste betaalde kanaal**: niet van toepassing, er is geen betaald kanaal.

---

## Punt 2 staat er nu vier rapporten op rij

De referrer-exclusies zijn nog steeds niet aangezet. Over 30 dagen: 3.451 Referral-bezoekers, waarvan `www.sempertexeurope.com` 3.337, Odoo 18 en de shipping-portal 10. Samen 3.365.

**97,5% van je "verwijzend verkeer" is je eigen domein.** Echt extern verkeer: ongeveer 86 bezoekers in een maand.

Dat is vijf minuten werk in PostHog en het is een voorwaarde voor elk attributieoordeel dat je hierna velt.

---

## Wat wel goed staat

De UTM-pipeline werkt. Drie email-campagnes komen met tags binnen: `mailjet / email / inspiration_promo_202607` (140 bezoekers), `Klaviyo / email / (none)` (109) en `mailjet / email / workshop_tobi_promo_202608` (46). Zodra er een euro naar Meta gaat, zie je die sessies terug.

Twee onopgeloste slordigheden: `mailjet`, `Klaviyo` en `Pinterest` zijn niet lowercase, en de 109 Klaviyo-bezoekers hebben nog steeds geen campaign-naam.

---

## Samenvatting

- **Totaal spend**: EUR 0,00 (periode: laatste 30 dagen)
- **Beste performer**: homepage, 3,2% bounce en 22,9 pageviews per sessie. Bewijs dat de site werkt voor wie normaal binnenkomt.
- **Slechtste performer**: `/en_GB/shop/category/foil-balloons-2915`, 283 entries met exact 1,00 pageview per sessie. Nul doorkliks is geen conversieprobleem, dat is een defect of nepverkeer.
- **Aanbeveling**: 70-20-10 gaat over budget verdelen over bewezen winnaars. Je hebt nog geen enkele winnaar, en belangrijker, je weet nog niet of je bestemmingspagina's überhaupt laden. Dat is geen optimalisatievraag maar een voorwaarde. Geen euro naar Meta tot je die vijf URL's zelf hebt geopend en de referrer-exclusies aanstaan.

### Volgorde

1. **Open de vijf URL's in incognito.** Twee minuten. Beslist alles daarna.
2. Referrer-exclusies aan in PostHog. Vijf minuten.
3. Autoriseer Pipeboard via je claude.ai connector instellingen.
4. Conversie-events op de SYBB event-pagina's voordat er budget in gaat.
5. UTM lowercase afdwingen, campaign verplicht stellen in Klaviyo.
6. AI-kanaal onderzoeken. 242 bezoekers per maand die je gratis krijgt.

### Google Sheet

Overgeslagen op verzoek. Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-08-17_ads_report.md`.
