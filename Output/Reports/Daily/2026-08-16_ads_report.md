# Meta Ads Rapport, 16 augustus 2026

**Pipeboard is niet geautoriseerd, negende dag op rij.** Stap 1 tot en met 4 van `/ads-report` konden niet draaien: geen accounts, geen campagnes, geen spend, impressions, CTR, CPC, CPM of ROAS. De Meta Ads MCP staat in deze sessie als "requires authentication" en de sessie is niet-interactief, dus autoriseren kan hier niet. Dat gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

Stap 6 (Google Sheet write) en alle Google MCPs zijn overgeslagen zoals gevraagd. Alles hieronder komt uit PostHog.

---

## Overzicht per campagne

Niet beschikbaar. Geen toegang tot de ad accounts (`act_567892422940728`, `act_607231713057715`).

## Underperformers en top performers

Niet beschikbaar zonder ad-level data.

---

## Wat PostHog wel laat zien

### Er heeft 30 dagen lang geen advertentieverkeer gelopen

UTM-breakdown over de laatste 30 dagen, gesorteerd op bezoekers:

| Bron / Medium / Campagne | Bezoekers | Pageviews |
|---|---|---|
| direct / (none) / (none) | 14.362 | 65.434 |
| referrer: www.sempertexeurope.com | 3.336 | 23.820 |
| referrer: www.google.com | 1.481 | 26.173 |
| chatgpt.com | 242 | 1.229 |
| **mailjet / email / inspiration_promo_202607** | **140** | 300 |
| **Klaviyo / email / (none)** | **109** | 177 |
| **mailjet / email / workshop_tobi_promo_202608** | **46** | 87 |
| Pinterest / organic / (none) | 8 | 10 |

Geen enkele regel met `utm_source=meta`, `utm_medium=cpc` of `utm_campaign=sybb`. Ook geen andere paid bron. **Nul advertentieverkeer in 30 dagen.**

### Belangrijk: je tracking werkt wel

Dit is nieuw ten opzichte van eerdere rapporten. De drie email-campagnes komen netjes binnen mét UTM-parameters. De pipeline van UTM naar PostHog is dus niet stuk. Er is simpelweg geen ad spend. Dat scheelt een hoop diagnose: zodra Pipeboard open is en je een campagne start, ga je die meteen terugzien.

Twee hygiëne-punten in diezelfde tabel:
- `mailjet`, `Klaviyo` en `Pinterest` zijn niet lowercase. Je eigen tracking standard schrijft lowercase voor.
- `Klaviyo / email / (none)` mist een campaign-naam. 109 bezoekers die je niet aan een verzending kunt koppelen.

### Kanalen, laatste 7 dagen

| Kanaal | Bezoekers | Pageviews | Aandeel |
|---|---|---|---|
| Direct | 3.785 | 16.795 | 79,9% |
| Referral | 451 | 6.539 | 9,5% |
| Organic Search | 395 | 7.295 | 8,3% |
| AI | 70 | 249 | 1,5% |
| Organic Social | 18 | 63 | 0,4% |
| Email | 17 | 129 | 0,4% |

Paid Social en Paid Search komen niet voor.

**AI staat nu op 70 bezoekers**, bijna vier keer Organic Social en vier keer Email. Over 30 dagen is ChatGPT alleen goed voor 242 bezoekers. Dat kanaal groeit zonder dat je er iets aan doet en staat nergens in je tracking.

### Punt 2 van de afgelopen twee rapporten is nog steeds niet uitgevoerd

De referrer-exclusies staan niet aan. Laatste 7 dagen:

| Verwijzer | Bezoekers | Pageviews |
|---|---|---|
| www.sempertexeurope.com | 426 | 6.101 |
| rezolvbv-sh-sempertex.odoo.com | 4 | 269 |
| sempertexeurope.shipping-portal.com | 3 | 43 |

Samen 433 van de 451 Referral-bezoekers. **96,0% van je "verwijzend verkeer" zijn je eigen domeinen.** Echt extern verwijzend verkeer is ongeveer 18 bezoekers, niet 451. Odoo doet 269 pageviews op 4 bezoekers, ruim 67 pagina's per bezoeker, dat is een medewerker of een bot.

Zolang dit aanstaat is elke referral-analyse waardeloos en is je sessie-telling opgeblazen.

### De daling blijft een meetartefact

| Metric | Laatste 7d | Vorige 7d | Verschil |
|---|---|---|---|
| Bezoekers | 4.543 | 6.788 | -33,0% |
| **Pageviews** | **31.097** | **35.893** | **-13,0%** |
| Sessies | 5.249 | 7.588 | -31,0% |
| Sessieduur | 4m26s | 3m04s | **+45,0%** |
| Bounce rate | 50,9% | 56,6% | -5,7pp |

Zelfde patroon als gisteren, iets minder extreem. Bezoekers min 33%, pageviews maar min 13%, duur plus 45%, bounce omlaag. Was je echt een derde van je publiek kwijt, dan waren de pageviews meegezakt. **Je reële daling ligt rond de 13%**, grotendeels seizoen. De rest is identity resolution die dezelfde mensen nu als één persoon telt.

### Pagina's met een bounce die geld kost

Top pagina's, laatste 7 dagen, bounce rate erbij:

| Pagina | Bezoekers | Bounce |
|---|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 197 | **98,3%** |
| /folie-ballonnen | 149 | **95,9%** |
| /de/shop/category/latex-ballons-2911 | 95 | **100,0%** |
| /en_GB/shop/category/latex-balloons-2911 | 132 | **78,9%** |
| /shop/category/latex-onbedrukt-2911 | 203 | **73,9%** |
| /shop | 308 | 43,1% |
| /en_GB/shop | 179 | 30,7% |
| / (homepage) | 376 | 2,9% |

De Engelse en Duitse categoriepagina's bouncen bijna volledig, terwijl de Nederlandse `/shop` op 43% zit en de homepage op 3%. Dat is geen toeval en geen seizoen. Er zit iets mis met de anderstalige categoriepagina's: lege categorie, verkeerde taal-redirect, of prijzen die niet laden. **Dit zijn 570+ bezoekers per week die direct wegklikken op precies de pagina's waar je straks ads naartoe wilt sturen.**

### De SYBB landing page haalt de top 15 niet

`startyourballoonbusiness.com` komt niet voor in de vijftien best bezochte pagina's. Consistent met wat we eerder vaststelden: SYBB verkoopt via de event-pagina's op sempertexeurope.com, niet via de losse landing page.

---

## Samenvatting

- **Totaal spend:** onbekend, geen Pipeboard-toegang. Vermoedelijk €0,00, want er is 30 dagen lang geen paid verkeer binnengekomen.
- **Beste performer:** het AI-kanaal, 242 bezoekers in 30 dagen tegen nul inspanning en nul kosten.
- **Slechtste performer:** de anderstalige categoriepagina's, tot 100% bounce.
- **Blokkade:** autorisatie, negen dagen.

## Volgorde voor vandaag

1. **Autoriseer Pipeboard.** Negen dagen is lang genoeg.
2. **Zet de referrer-exclusies aan in PostHog** voor `sempertexeurope.com`, `odoo.com`, `shipping-portal.com` en `mollie.com`. Vijf minuten werk, en tot dat gebeurt is elk kanaalrapport dat je krijgt vervuild.
3. **Onderzoek de bounce op `/en_GB/shop/category/foil-balloons-2915` en `/folie-ballonnen`.** Open ze zelf. 98% bounce op 197 bezoekers is een kapotte pagina, geen slecht publiek.
4. Conversie-events op de SYBB event-pagina's vóór er budget in gaat.
5. UTM-hygiëne: lowercase afdwingen, campaign-naam verplicht in Klaviyo.
6. Onderzoek het AI-kanaal.

Punt 2 tot en met 6 hebben Pipeboard niet nodig.

**Aanbeveling:** geen euro naar Meta tot punt 2 en 3 staan. Hormozi's 70-20-10 gaat over budget verschuiven naar bewezen winnaars. Je kunt op dit moment niet zien welke 70% bewezen is, en de pagina's waar je verkeer naartoe stuurt lekken bij 98%. Ads inzetten op een lekkende bak is de duurste manier om te leren dat de bak lekt.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
