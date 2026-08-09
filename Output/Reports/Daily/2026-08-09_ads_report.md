## Meta Ads Rapport, 9 augustus 2026

**De Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 konden niet draaien. Geen spend, CTR, CPC of ROAS. Derde dag op rij. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

**Nul betaald verkeer, 39 dagen.** Laatste `meta/cpc/sybb` klik: 1 juli 2026, 16:42. Geen Paid Social kanaal in 30 dagen. Ook je organische social tagging is stil sinds 14 juli.

Site breed over 30 dagen: 16.030 bezoekers, 101.897 pageviews, bounce rate 56,7%, sessieduur 4m35s. Die bounce rate loopt gestaag op, 54,5% op 6 augustus, 56,0% op 8 augustus, nu 56,7%.

### Twee dingen die er vandaag uit springen

**De SYBB landing page ligt negen dagen volledig stil.** Laatste event op startyourballoonbusiness.com is 31 juli, 2 events van 1 persoon. Daarna niets. De pixel werkt, dat stelde ik gisteren al vast. Wat ontbreekt is verkeer, en zonder ads komt er letterlijk niemand.

**Je sessieduur is deze week met 34% ingezakt,** van 4m40s naar 3m06s, bij gelijk bezoekersaantal. Tegelijk verbeterde de bounce rate van 60,0% naar 55,3%. Dat ziet er goed uit maar is het niet: mensen klikken wél door naar een tweede pagina, maar haken sneller af. Bounce rate verbergt hier wat er gebeurt. Dit staat los van de ads situatie en verdient apart onderzoek.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert al het andere
2. Fix UTM casing naar lowercase in alle ad URLs
3. Zet conversie events op de SYBB pagina, de pixel meet nu alleen pageviews
4. Verifieer conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
5. Tag de Klaviyo mails met `utm_campaign`, 107 bezoekers zijn nu niet toewijsbaar
6. Onderzoek de sessieduur daling
7. Pas daarna herstarten volgens 70-20-10, budget naar de bewezen `meta/cpc/sybb` hooks

Punt 2 tot en met 5 kun je nu al doen, die hebben Pipeboard niet nodig. Dan staat je meting klaar zodra er weer budget loopt.

Rapport staat in `Output/Reports/Daily/2026-08-09_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend en nul bezoekers op de landing page levert een funnel diagnose nu niets op. Zinvol zodra er weer verkeer is.
