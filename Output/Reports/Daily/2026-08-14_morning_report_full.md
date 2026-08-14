# Morning Report — 2026-08-14

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 14 augustus 2026

**Pipeboard is niet geautoriseerd, zevende dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS, dus de underperformer- en top-performer-secties zijn leeg. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Er draait sowieso niets

Over 90 dagen: **Paid Social 0 bezoekers.** Paid Search 2, Paid Unknown 1. Geen `utm_source=meta`, geen `utm_campaign=sybb` in de data. Zelfs met werkende Pipeboard-toegang zou je vandaag een rapport over nul actieve campagnes krijgen.

De enige getagde campagnes die verkeer opleveren zijn e-mail: `inspiration_promo_202607` (140 bezoekers), Klaviyo (109), `workshop_tobi_promo_202608` (46).

Geen enkele pagina van `startyourballoonbusiness.com` staat in de top 25. Alle 25 posities zijn de hoofdsite.

### Ik nuanceer mijn conclusie van gisteren

Het rapport van 13 augustus noemde de daling van 73,2% "geen meetfout". Kijk naar de laatste 7 dagen versus de 7 daarvoor:

| Metric | Laatste 7d | Vorige 7d | Verschil |
|--------|-----------|-----------|----------|
| Sessies | 4.451 | 7.601 | -41,0% |
| **Pageviews** | **31.017** | **36.656** | **-15,0%** |
| Sessieduur | 5m27s | 3m51s | +42,0% |

Sessies min 41%, pageviews maar min 15%, duur plus 42%. Dat is niet wegvallend verkeer. Dat is minder sessie-fragmentatie: dezelfde mensen, bijna evenveel pagina's, minder losse sessies. **De echte daling in consumptie is ongeveer 15%, niet 73%.** Er is geen acuut lek. Er is een meetprobleem.

### Dat meetprobleem staat er nog steeds

Mijn advies van gisteren, punt 2, is niet uitgevoerd. `www.sempertexeurope.com` is nog altijd je op één na grootste verkeersbron: 665 bezoekers en 6.630 pageviews in een week, 17,1% van je verkeer. Daardoor is Direct kunstmatig 69,9%.

Zet je Meta aan zonder dit te fixen, dan komt een deel van je betaalde bezoekers terug als Direct en reken je de campagne af op een verzonnen cijfer.

### Volgorde

1. Autoriseer Pipeboard
2. **Sluit `sempertexeurope.com`, `mollie.com`, Odoo en shipping-portal uit als verwijzer in PostHog**, instelling van vijf minuten, blokkeert al het andere
3. Conversie-events op de SYBB pagina vóór nieuw budget
4. Herwaardeer de daling pas na stap 2
5. Alles van vóór 13 juli als niet bestaand behandelen
6. UTM lowercase, komma's in `utm_content` naar underscores
7. Organic Search harder inzetten: 1.714 bezoekers, 30.804 pageviews, 4,6% bounce, zonder budget

Punt 2 tot en met 7 hebben Pipeboard niet nodig.

Losse observatie: `/en_GB/latex-balloons/fashion-solid/blue---040-2` haalt 329 bezoekers en exact 329 pageviews, bounce 100,0%. Gratis verkeer dat volledig wegloopt.

Rapport staat in `Output/Reports/Daily/2026-08-14_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport staat in `Output/Reports/Daily/2026-08-13_sybb_report.md`, gecommit en gepusht.

**Twee dingen die je moet weten voordat je het leest.**

**Meta Ads kon ik niet ophalen.** De Pipeboard MCP vereist autorisatie en deze sessie is niet interactief, dus de OAuth flow kan hier niet draaien. Dat regel je via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Dit is de achtste dag op rij.

Maar dat is niet je probleem. PostHog kan aan de ontvangende kant zien of er advertentieverkeer binnenkomt, onafhankelijk van Pipeboard. Op 13 augustus was de volledige lijst UTM getagd verkeer in het hele project: `chatgpt.com`, 8 pageviews. Geen `meta`, geen `sybb`. Ook met werkende Pipeboard toegang was het antwoord vandaag "de campagne staat uit".

**De landing page meet al twee weken niets.** Dit is de echte vondst. `startyourballoonbusiness.com` heeft op 13 augustus nul events gestuurd. Het laatste event van dat domein kwam binnen op 31 juli om 21:12 UTC.

Het zijn drie losse storingen, geen één:

1. Sinds **10 juli** geen `$autocapture` en `$pageleave` meer. Daardoor zijn CTA clicks, sessieduur en bounce rate al vijf weken onmeetbaar.
2. Sinds **1 augustus** ook geen pageviews meer. Dat wijst op een verwijderde of gebroken snippet, niet op een instelling.
3. **Scroll depth is nooit geïnstrumenteerd.** Er bestaat geen enkel scroll event in de taxonomie van het project. De vier scroll targets in de skill en in CLAUDE.md toetsen data die er nooit is geweest.

Ik heb de rapportstructuur uit de skill volledig aangehouden, maar de tabellen staan vol "onmeetbaar" in plaats van cijfers. Het verschil tussen "tracking dood" en "event bestaat niet" staat er per rij bij, want dat zijn verschillende reparaties.

Wat ik er wel bij heb gezet: de funnel die volgens je projectkennis wél draait, de SYBB event register pagina's op `sempertexeurope.com`. Gisteren 2 bezoekers, tegen een 7-daagse mediaan van 3. Normale ruis op dat volume. Let op dat het 7d gemiddelde van 16,1 pageviews misleidend is, 10 augustus had 6 bezoekers die samen 88 pageviews maakten.

Eén ding heb ik niet gedaan omdat het buiten je vraag viel: de skill zelf aanpassen. De scroll targets en de landing page funnel definitie kloppen niet meer met de werkelijkheid. Dat staat als actie 3 in het rapport, met jouw goedkeuring op de nieuwe funnel definitie. Zeg het als je wilt dat ik dat nu doorvoer.

---

Rapport staat in `Output/Reports/Daily/2026-08-14_auto_optimize.md`, gecommit en gepusht.

## Kort samengevat

**Geen ads gepauzeerd, geen acties uitgevoerd.** Pipeboard is niet geautoriseerd, zevende dag op rij. Zonder `get_insights` is er geen `actions.link_click`, dus geen Link CTR en geen CPC (link), en de kill-regels draaien uitsluitend op die twee. Stap 1 tot en met 6 van het command konden niet draaien.

Wat ik wél kon doen: PostHog werkt, dus ik heb dezelfde 3-daagse window zelf gecontroleerd om te zien of er überhaupt betaald verkeer bestaat.

**Paid Social, Paid Search en Paid Unknown zijn alle drie afwezig.** Over 1.167 bezoekers in 3 dagen komt `utm_source=meta` nergens voor, `utm_campaign=sybb` evenmin. De acht bezoekers via facebook.com en instagram.com zijn ongetagd organisch verkeer.

Dat betekent iets belangrijks: het autorisatieprobleem verbergt geen campagne die geld verbrandt. Ook met werkende toegang zou dit rapport vandaag over nul actieve ads gaan.

**Wat wel aandacht vraagt:** `www.sempertexeurope.com` staat nog steeds als verwijzer naar je eigen site, 250 bezoekers en 21,5% van al je verkeer in 3 dagen. Plus Odoo, Mollie en de shipping-portal. Dit stond ook in de rapporten van 13 en 14 augustus en is nog niet uitgevoerd. Zolang het blijft staan, wordt Direct opgeblazen naar 55,4% en lekt je eerste Meta-verkeer daar straks deels in weg.

Punt 2 (interne domeinen uitsluiten), 3 (conversie-events op SYBB) en 4 (UTM-conventie in de templates) kan ik direct oppakken, die hebben Pipeboard niet nodig. Punt 1, het autoriseren zelf, moet via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Deze sessie is niet interactief, dus die flow kan ik niet voor je starten.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
