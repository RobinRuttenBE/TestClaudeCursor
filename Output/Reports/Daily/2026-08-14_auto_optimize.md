Rapport staat in `Output/Reports/Daily/2026-08-14_auto_optimize.md`, gecommit en gepusht.

## Kort samengevat

**Geen ads gepauzeerd, geen acties uitgevoerd.** Pipeboard is niet geautoriseerd, zevende dag op rij. Zonder `get_insights` is er geen `actions.link_click`, dus geen Link CTR en geen CPC (link), en de kill-regels draaien uitsluitend op die twee. Stap 1 tot en met 6 van het command konden niet draaien.

Wat ik wél kon doen: PostHog werkt, dus ik heb dezelfde 3-daagse window zelf gecontroleerd om te zien of er überhaupt betaald verkeer bestaat.

**Paid Social, Paid Search en Paid Unknown zijn alle drie afwezig.** Over 1.167 bezoekers in 3 dagen komt `utm_source=meta` nergens voor, `utm_campaign=sybb` evenmin. De acht bezoekers via facebook.com en instagram.com zijn ongetagd organisch verkeer.

Dat betekent iets belangrijks: het autorisatieprobleem verbergt geen campagne die geld verbrandt. Ook met werkende toegang zou dit rapport vandaag over nul actieve ads gaan.

**Wat wel aandacht vraagt:** `www.sempertexeurope.com` staat nog steeds als verwijzer naar je eigen site, 250 bezoekers en 21,5% van al je verkeer in 3 dagen. Plus Odoo, Mollie en de shipping-portal. Dit stond ook in de rapporten van 13 en 14 augustus en is nog niet uitgevoerd. Zolang het blijft staan, wordt Direct opgeblazen naar 55,4% en lekt je eerste Meta-verkeer daar straks deels in weg.

Punt 2 (interne domeinen uitsluiten), 3 (conversie-events op SYBB) en 4 (UTM-conventie in de templates) kan ik direct oppakken, die hebben Pipeboard niet nodig. Punt 1, het autoriseren zelf, moet via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Deze sessie is niet interactief, dus die flow kan ik niet voor je starten.
