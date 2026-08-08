## Meta Ads Rapport, 8 augustus 2026

**De Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 konden niet draaien. Geen spend, CTR, CPC of ROAS. Tweede dag op rij. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

**Nul betaald verkeer** in 30 dagen. Er is geen Paid Social kanaal. Ik heb zes maanden UTM historie doorzocht en de laatste betaalde klik dateert van **1 juli 2026, 38 dagen geleden.**

Site breed over 30 dagen: 15.379 bezoekers, 99.218 pageviews, bounce rate 56,0%, gemiddelde sessieduur 4m39s. Die bounce rate stond op 6 augustus nog op 54,5%, dus hij is net over je 55% target geschoven.

Email blijft het enige kanaal dat presteert: 15,2% en 22,5% bounce tegenover 56,0% site breed.

### Twee dingen die ik onderweg vond

**Je UTM casing splitst de attributie.** Er lopen twee varianten naast elkaar: `meta/cpc/sybb` met 1.141 personen en `META/cpc/SYBB` met 189. PostHog telt dat als twee bronnen. De uppercase variant is de recentste, dus de fout zit in de laatst gebouwde ads. Bij herstart zit 14% van je betaalde verkeer in een aparte bucket.

**Correctie op mijn rapport van 6 augustus:** ik schreef toen dat startyourballoonbusiness.com niet gemeten wordt. Dat klopt niet. De pixel staat er wel en stuurt data, 81 events van 32 personen, laatste hit 31 juli. Wat ontbreekt is verkeer, niet meting. Wel zie ik alleen pageviews en autocapture, geen expliciete CTA of booking events. Dat is wat er nog moet gebeuren voor je die 0,5% checkout conversie kunt diagnosticeren.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert al het andere
2. Fix UTM casing naar lowercase in alle ad URLs
3. Zet conversie events op de SYBB pagina, de pixel meet nu alleen pageviews
4. Verifieer conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
5. Tag de Klaviyo mails met `utm_campaign`, 107 bezoekers zijn nu niet toewijsbaar
6. Pas daarna herstarten volgens 70-20-10, met budget naar de bewezen `meta/cpc/sybb` hooks

Rapport staat in `Output/Reports/Daily/2026-08-08_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend levert een funnel diagnose nu weinig op. Zinvoller zodra er weer budget loopt.
