## Meta Ads Rapport, 13 augustus 2026

**Meta Ads data ontbreekt, zesde dag op rij.** Pipeboard is niet geautoriseerd in deze sessie, dus stap 1 tot en met 4 konden niet draaien. Geen campagne-, ad set- of ad-data, en dus ook geen underperformers, top performers of ROAS. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

PostHog bevestigt dat er niets draait: laatste betaalde klik **14 juli 2026**, dertig dagen geleden. Geen Paid Social in de kanaalverdeling. SYBB landing page ligt stil sinds 31 juli.

### Ik trek de conclusie van 11 en 12 augustus in

Die rapporten meldden "sessies dalen acht dagen op rij, er ging iets kapot rond 3 augustus". Dat klopt niet. **PostHog meet vóór 13 juli 7 tot 17 sessies per week.** De tracking op de hoofdsite is toen pas live gegaan. De stijging van 298 naar 974 sessies per dag in de weken daarna is de uitrol van de pixel, geen groei. Er is geen periode om 3 augustus mee te vergelijken.

### Wat wél echt is

Sessies zakten van 1.270 (3 aug) naar 340 (12 aug), min 73,2%. Dat is geen meetfout: Organic Search via Google blijft in dezelfde periode vlak rond 50 tot 90 sessies per dag. Lag de pixel eruit, dan was Google mee gedaald.

### Het probleem dat alles blokkeert

**Je op één na grootste verkeersbron is je eigen domein.** `www.sempertexeurope.com` levert 1.124 sessies in vier dagen, ruim een kwart van je totaal. Sessies breken op tijdens het bezoek, waarschijnlijk bij interne navigatie en bij terugkeer van Mollie.

Daardoor is je sessietelling opgeblazen, is die 4,5% bounce rate op Organic Search een artefact (een opgebroken sessie kan per definitie niet bouncen), en verdwijnt de oorspronkelijke bron van elke opgebroken sessie naar Direct. Dat verklaart waarom Direct 68,6% van je verkeer lijkt te zijn.

Zolang dit staat kun je geen campagne eerlijk beoordelen. Je zou Meta straks afrekenen op cijfers die het systeem zelf verzint.

### Volgorde

1. Autoriseer Pipeboard
2. **Sluit `sempertexeurope.com`, `mollie.com` en de Odoo domeinen uit als verwijzer in PostHog**, dit blokkeert alle andere analyse
3. Herwaardeer de verkeersdaling pas daarna
4. Behandel alles van vóór 13 juli als niet bestaand
5. Conversie events op de SYBB pagina vóór herstart
6. UTM casing lowercase, komma's in `utm_content` naar underscores
7. Klaviyo mails taggen, Email bouncet op 18,5%
8. Organic Search harder inzetten, 1.659 bezoekers en 29.487 pageviews zonder budget

Punt 2 tot en met 8 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-13_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend, een stille landing page en gebroken sessie-attributie levert een funnel diagnose nu geen betrouwbaar antwoord op. Ik zou eerst punt 2 fixen.
