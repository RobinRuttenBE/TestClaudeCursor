## Meta Ads Rapport, 18 augustus 2026

**Pipeboard is niet geautoriseerd, elfde dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. Autoriseren kan niet vanuit deze niet-interactieve sessie, dat gaat via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs overgeslagen zoals gevraagd.

Totaal spend: **EUR 0,00** over 30 dagen. PostHog bevestigt dat: geen Paid Social en geen Paid Search in de kanaaltabel, geen enkele sessie met `utm_source=meta` of `utm_medium=cpc`.

| Kanaal (30d) | Bezoekers | Aandeel |
|---|---|---|
| Direct | 16.021 | 73,4% |
| Referral | 3.466 | 15,9% |
| Organic Search | 1.666 | 7,6% |
| Email | 320 | 1,5% |
| AI | 245 | 1,1% |
| Organic Social | 95 | 0,4% |
| **Paid Social** | **0** | **0%** |
| **Paid Search** | **0** | **0%** |

---

### Correctie op gisteren, en de echte oorzaak

Gisteren noemde ik vijf categoriepagina's met exact 1,00 pageview per sessie en adviseerde ik je die URL's in incognito te openen. **Doe dat niet, de pagina's zijn niet stuk.** De 1,00 is geen eigenschap van die pagina's. Het is een eigenschap van bepaalde landen.

Kijk naar dezelfde ratio per land, 7 dagen:

| Land | Bezoekers | Pageviews | Views per bezoeker |
|---|---|---|---|
| België | 301 | 8.566 | **28,5** |
| Nederland | 365 | 7.579 | **20,8** |
| Duitsland | 271 | 4.350 | **16,1** |
| Frankrijk | 174 | 1.987 | **11,4** |
| Groot-Brittannië | 588 | 1.990 | 3,4 |
| Brazilië | 448 | 448 | **1,00** |
| **Seychellen** | **287** | **287** | **1,00** |
| Argentinië | 189 | 189 | **1,00** |
| Colombia | 148 | 149 | 1,01 |
| Mexico | 124 | 128 | 1,03 |
| Venezuela | 101 | 101 | **1,00** |
| Vietnam | 99 | 99 | **1,00** |
| Bangladesh | 99 | 101 | 1,02 |

Je Europese markten doen 11 tot 28 pageviews per bezoeker. Een tweede groep landen doet er exact één, tot op de eenheid nauwkeurig, over duizenden sessies.

**De Seychellen zijn het bewijs.** 287 bezoekers in 7 dagen, uit een land met ongeveer 100.000 inwoners. Dat is meer dan Frankrijk (174) en bijna evenveel als Duitsland (271), voor een Europese B2B ballondistributeur. De Seychellen zijn een bekende vestigingsplaats voor VPS en proxy hosting. Dit is geen publiek, dit is infrastructuur.

Twee onafhankelijke checks bevestigen het:

**Browsers.** In dit segment: Chrome 363, Firefox 206, Edge 118. Nul Safari. Nul Mobile Safari. Nul Samsung Internet. Nul mobiel, in 687 sessies. Op je hele site is ongeveer 7% mobiel, dus je zou er circa 48 verwachten. Nul is geen toeval. Firefox staat daarnaast op 30% in dit segment tegen 19,8% sitewide, en op de echte markt rond 3%.

**Bounce.** Alle betrokken pagina's zitten tussen 90% en 100%, terwijl je homepage op 3,2% zit met 24 pageviews per sessie.

---

### Wat dit kost aan je cijfers

Dit is het punt dat er toe doet. Ik heb de 12 verdachte landen uit je 7 daagse cijfers gehaald, VS bewust behouden omdat daar echte klanten tussen zitten:

| Metric (7d) | Zoals gerapporteerd | Zonder botverkeer | Verschil |
|---|---|---|---|
| Bezoekers | 5.606 | 3.731 | **33,4% was geen mens** |
| Pageviews | 32.599 | 30.683 | 5,9% |
| Sessieduur | 223,7s | **406,5s** | **+82%** |
| Bounce rate | 52,3% | **45,6%** | **6,7 punten beter** |

Haal je de VS er ook uit, dan wordt het 3.371 bezoekers, 43,6% bounce en 440,5 seconden.

Je site presteert dus aanzienlijk beter dan je dashboard laat zien. Je echte bounce rate zit rond 45%, niet 56%. Je echte sessieduur is bijna zeven minuten, niet vier. Eén derde van je bezoekersaantal bestaat niet.

En dit is precies de reden om het nu op te lossen, niet later. Zodra je Meta ads gaat draaien, vergelijk je de landingspaginacijfers met een nulmeting die 33% vervuild is. Elke conclusie over adprestatie wordt dan verkeerd, in beide richtingen.

---

### Punt 3, vijfde rapport op rij

3.466 Referral bezoekers over 30 dagen, waarvan 3.381 van je eigen domeinen (sempertexeurope.com 3.354, Odoo 18, shipping-portal 9). **97,5% van je verwijzend verkeer is jezelf.** Echt extern: circa 85 bezoekers per maand.

### Wat wel werkt

De UTM pipeline. Drie emailcampagnes komen netjes getagd binnen (mailjet `inspiration_promo_202607` 141 en `workshop_tobi_promo_202608` 46, Klaviyo 109). Zodra er spend is, zie je het terug. Nog steeds open: lowercase afdwingen (Klaviyo en Pinterest komen met hoofdletter binnen, mailjet niet), en Klaviyo mist nog altijd een campaign naam.

### Aanbeveling

70-20-10 verdeelt budget over bewezen winnaars. Je hebt er nog geen, en tot vandaag wist je niet dat een derde van je verkeersdata onzin is. Dat is geen optimalisatievraag maar een meetvraag, en die gaat voor.

Volgorde:

1. **Botfilter in PostHog.** Sluit de 12 landen uit, of beter, filter op de combinatie 1 pageview plus geen mobiel. Dit is vandaag te doen en herstelt je hele nulmeting.
2. **Referrer exclusies** voor je eigen domeinen, punt 3 hierboven.
3. **Pipeboard autoriseren**, elf dagen open.
4. Conversie events op de SYBB event pagina's.
5. UTM opschonen, lowercase plus Klaviyo campaign naam.
6. AI kanaal onderzoeken, 242 gratis bezoekers per maand uit ChatGPT.

Geen euro naar Meta tot 1 en 2 staan. Je zou anders betalen om verkeer te meten met een kapotte meetlat.
