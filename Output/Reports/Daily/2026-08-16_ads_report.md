## Meta Ads Rapport, 16 augustus 2026

**Pipeboard is niet geautoriseerd, negende dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. De sessie is niet-interactief, dus ik kan hier niet autoriseren. Dat gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs overgeslagen zoals gevraagd.

### Nul advertentieverkeer in 30 dagen

De UTM-breakdown bevat geen enkele regel met `utm_source=meta` of `utm_medium=cpc`. Paid Social en Paid Search komen niet voor in de kanaaltabel. Zelfs met werkende Pipeboard-toegang krijg je een rapport over nul actieve campagnes.

### Nieuw: je tracking werkt wel

Drie email-campagnes komen netjes binnen mét UTM's: `mailjet / email / inspiration_promo_202607` (140 bezoekers), `Klaviyo / email / (none)` (109), `mailjet / email / workshop_tobi_promo_202608` (46). De pipeline van UTM naar PostHog is dus niet stuk, er is alleen geen spend. Zodra je een campagne start zie je die meteen terug.

Wel twee slordigheden: `mailjet`, `Klaviyo` en `Pinterest` zijn niet lowercase, en die 109 Klaviyo-bezoekers hebben geen campaign-naam.

### Punt 2 staat er nu drie rapporten op rij

De referrer-exclusies zijn nog steeds niet aangezet. Van je 451 Referral-bezoekers komen er 433 van je eigen domeinen (sempertexeurope.com 426, Odoo 4, shipping-portal 3). **96,0% van je "verwijzend verkeer" is jezelf.** Echt extern: ongeveer 18 bezoekers.

### Nieuw en dit kost geld

| Pagina | Bezoekers | Bounce |
|---|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 197 | **98,3%** |
| /folie-ballonnen | 149 | **95,9%** |
| /de/shop/category/latex-ballons-2911 | 95 | **100,0%** |
| /shop (NL) | 308 | 43,1% |
| / (homepage) | 376 | 2,9% |

De Engelse en Duitse categoriepagina's bouncen bijna volledig, de Nederlandse `/shop` zit op 43% en de homepage op 3%. Dat is geen seizoen en geen slecht publiek, dat is een kapotte pagina. 570+ bezoekers per week klikken direct weg op precies de pagina's waar je straks ads naartoe stuurt.

### De daling blijft een meetartefact

Bezoekers -33,0%, pageviews maar -13,0%, sessieduur +45,0%, bounce -5,7pp. Was je een derde van je publiek kwijt, dan waren de pageviews meegezakt. Je reële daling is ongeveer 13%.

### Volgorde

1. Autoriseer Pipeboard
2. Referrer-exclusies aan in PostHog, vijf minuten
3. **Open zelf `/en_GB/shop/category/foil-balloons-2915` en `/folie-ballonnen`**, 98% bounce is een defect
4. Conversie-events op de SYBB event-pagina's vóór er budget in gaat
5. UTM lowercase afdwingen, campaign verplicht in Klaviyo
6. AI-kanaal onderzoeken, 242 bezoekers in 30 dagen gratis

**Aanbeveling:** geen euro naar Meta tot punt 2 en 3 staan. Ads op een lekkende bak zetten is de duurste manier om te leren dat de bak lekt.

Rapport staat in `Output/Reports/Daily/2026-08-16_ads_report.md`, gecommit en gepusht (`7230f982`).

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
