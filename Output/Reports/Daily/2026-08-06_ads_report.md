## Meta Ads Rapport, 6 augustus 2026

**De Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 van het command konden niet draaien. Geen live spend, CTR, CPC of ROAS. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

Er is **nul betaald verkeer** in de laatste 30 dagen. Geen "Paid Social" kanaal, geen enkele hit op `utm_source=meta` of `utm_medium=cpc`. Dat is onafhankelijke bevestiging van de meting van 4 augustus: alles staat op PAUSED, laatste uitgave april 2026.

Landing page over 30 dagen: 13.844 bezoekers, 90.089 pageviews, bounce rate 54,5% (target <55%, net gehaald), gemiddelde sessieduur 4m49s. De vergelijking met de vorige periode die PostHog geeft (+32.862%) is onbruikbaar, want die periode telde maar 42 bezoekers. De tracking ging pas een maand geleden live.

Email is nu het enige kanaal dat presteert: `inspiration_promo_202607` met 15,2% bounce rate, `workshop_tobi_promo_202608` met 22,2%, tegenover 54,5% site-breed. Drie keer zo betrokken als gemiddeld.

### Iets belangrijkers dat ik onderweg vond

`CLAUDE.md` gaat ervan uit dat PostHog **startyourballoonbusiness.com** meet. Dat klopt niet. Er is één organisatie en één project, en de enige hosts die data sturen zijn `www.sempertexeurope.com` en `rezolvbv-sh-sempertex.odoo.com`. De SYBB landingspagina wordt niet gemeten.

Alle SYBB KPI targets uit je CLAUDE.md zijn daarmee op dit moment onmeetbaar. Dat weegt zwaar, want uit het rapport van 4 augustus bleek dat juist die pagina 0,5% naar checkout converteerde tegenover 19,0% bij Nozzle Up. De pagina waar het geld verdampt is precies de pagina die blind is.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert al het andere
2. Zet de pixel op startyourballoonbusiness.com **vóór** je budget aanzet
3. Fix de conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
4. Pas daarna herstarten volgens 70-20-10
5. Tag de Klaviyo mails met `utm_campaign`, 107 bezoekers zijn nu niet toewijsbaar

Rapport staat in `Output/Reports/Daily/2026-08-06_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Let op dat een funnel diagnose met nul spend en nul betaald verkeer weinig oplevert. Zinvoller wordt het zodra de SYBB pixel staat en er weer budget loopt.
