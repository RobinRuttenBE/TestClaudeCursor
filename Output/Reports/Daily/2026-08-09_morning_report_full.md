# Morning Report — 2026-08-09

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Rapport staat in `Output/Reports/Daily/2026-08-08_sybb_report.md`, gecommit en gepusht. Alleen PostHog gebruikt, geen Google MCPs, niets naar de Google Sheet.

**Meta Ads kon ik niet ophalen.** De Pipeboard connector is niet geautoriseerd en deze sessie is non interactief, dus autoriseren kan hier niet. Vierde dag op rij. Sectie 2 en de ad variant tabel staan op "n.b.". Autoriseren gaat via je claude.ai connector instellingen of `/mcp` in een interactieve sessie.

Drie dingen die eruit springen:

**De SYBB landing page ligt 8 dagen op nul,** maar het echte SYBB verkeer loopt via de event registratiepagina's op sempertexeurope.com. Daar was 8 augustus juist goed: 10 pageviews, 5 unieke bezoekers, 5 sessies, ongeveer dubbel het weekgemiddelde, en **nul bounces**. Eén bezoeker besteedde 39 minuten en eindigde op de SYBB register pagina zonder door te klikken.

**Nul registratie voltooiingen site breed,** bij 6 starts. De enige sessie die het formulier bereikte was Frans, met 283 clicks in 1.901 seconden, en rondde niet af. Dat patroon wijst op wrijving in het formulier, niet op afhakende interesse. Dit is actie 1, en de enige in het rapport die direct omzet raakt.

**Direct verkeer is in vier dagen ingestort in kwaliteit:** bounce van 37,0% (5 aug) naar 88,7% (8 aug), sessieduur van 224s naar 50s. Tegelijk zakten checkout pageviews van 77 naar 15. Mijn hypothese is dat een betrokken terugkerend segment is weggevallen waardoor een bodem van bot verkeer het gemiddelde bepaalt, maar die checkout daling maakt een puur meetprobleem minder waarschijnlijk. Ik heb dit expliciet als hypothese gemarkeerd, verifieer voordat je erop stuurt.

Twee kanttekeningen bij het rapport zelf: scroll depth en CTA click rate zijn **niet meetbaar** in dit PostHog project (geen scroll event, geen CTA event, geen scroll kolom op de sessions tabel), dus vier van de zeven Landing Page Health KPI's staan op ⚫ in plaats van een score. En vandaag (9 aug, deels) laat 94,2% bounce met 23s zien, wat ik als vroege waarschuwing heb opgenomen.

---

Het rapport staat in `Output/Reports/Daily/2026-08-09_auto_optimize.md` en is gecommit en gepusht (de auto-sync job pakte het op in commit `2fb8c2bb`).

## Auto-Optimize, 9 augustus 2026

**De run is geblokkeerd.** De Pipeboard Meta Ads connector is niet geautoriseerd in deze sessie, en omdat dit een niet-interactieve sessie is kan ik de OAuth flow hier niet starten. Zonder Meta data kon geen enkele stap van het optimalisatieproces draaien: geen kill regels, geen pauzeringen, geen 70-20-10 classificatie, geen budgetvoorstellen. Derde dag op rij.

**Gepauzeerd: 0 ads.** Let op het verschil: dit is niet "alles presteert goed", dit is "niets is beoordeeld".

### Wat ik wel heb kunnen vaststellen

PostHog bevestigt nul betaald verkeer over de afgelopen 3 dagen. Van 2.662 bezoekers kwam er geen enkele via Paid Social. Het kanaal komt niet eens voor in de verdeling. Direct 72,6%, Referral 18,2%, Organic Search 7,6%. Laatste `meta/cpc/sybb` klik was 1 juli, nu 39 dagen geleden.

Belangrijke beperking daarbij: PostHog ziet klikken, geen spend of impressions. Dus dit bewijst niet dat er nul budget loopt. Een ad kan impressions draaien en geld opmaken zonder een enkele klik, en juist dat scenario is nu onzichtbaar. Dat is precies waar de kill regels voor bestaan.

Daarom staat als voorstel 2 in het rapport: check even handmatig in Ads Manager of er spend loopt op `act_567892422940728` en `act_607231713057715`. Spend groter dan nul met nul klikken betekent direct met de hand pauzeren.

### Wat opviel in de data

De Mailjet campagne `workshop_tobi_promo_202608` bracht 11 bezoekers en is correct getagd op bron, medium en campagne. Klaviyo staat er nog steeds bij als `Klaviyo / email / (none)`, dus zonder `utm_campaign`. Mailjet is hier de standaard die Klaviyo zou moeten volgen.

### Om te ontblokkeren

Autoriseer Pipeboard via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Zolang dat open staat draait dit command elke ochtend leeg en heeft de automatische bewaking geen effect.

Eén ding dat van jou moet komen: de 70-20-10 drempels staan sinds de overstap naar link metrics op 13 april nog gemarkeerd als richtlijn, niet als hard oordeel. Die wil je vastgesteld hebben voordat Pipeboard weer data levert, anders classificeert het systeem op waarden die op een andere metriek zijn geijkt.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
