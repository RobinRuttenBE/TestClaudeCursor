# SYBB Daily Report: 21 september 2026

## 1. Samenvatting
Maandag 21 september was opnieuw een drukke SYBB-dag zonder één inschrijfpoging: negen externe sessies van acht personen op de SYBB registratiepagina's, 22 SYBB-pageviews, nul kliks op Registreer, nul betalingen. Voor de tweede dag op rij zat er geen link-preview bot tussen, maar wel vier interne sessies (twee daarvan van medewerkers die het bestaande interne filter niet ving) en één bezoeker die de hele site in 13 minuten doorscande. De twee sterkste signalen van de dag zijn allebei twijfelaars zonder vangnet: een Belgische Android-bezoeker die 's ochtends via Google op de Franse pagina van professional-8 landde, drie uur later terugkwam en in negen minuten vijftien keer tussen professional-7, 8 en 9 heen en weer klikte, en een Belgische iPhone-bezoeker die sinds 29 augustus nu al zes keer de Nederlandse pagina van professional-9 heeft geopend, elke keer via de kalender en elke keer zonder te klikken. Daarnaast bekeek een Oostenrijkse klant met twee producten in de mandjes de Duitse pagina van professional-7, een Nederlandse klant met account kwam via Content Day en Nozzle Up bij professional-9 uit, en een bezoeker van Réunion vertrok via professionnel-7 naar de Franse partnersite. Meta bevestigt live nul levering op `2026: SYBB` over 15 t/m 21 september; de campagne staat 155 dagen op PAUSED. De landing page startyourballoonbusiness.com staat voor de vierentwintigste dag op 0 bezoekers en session replay leverde voor de zestiende dag nul opnames.

## 2. Meta Ads Performance

**Status data:** live. Beide MCP-servers (`claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads`) vroegen om autorisatie, wat in deze non-interactieve sessie niet kan; de directe JSON-RPC route werkte direct. Eén call: campaign-level insights voor campagne 120239435987290239 over 15 t/m 21 september met `time_increment: 1`, antwoord `data: []`, dus geen levering en geen spend op geen enkele dag. Geen verdere Meta-calls gedaan om de weeklimiet te sparen (stand na deze run: 12 van 30). Campagnestatus komt uit het live ads-rapport van vanochtend (get_campaigns, 7 campagnes).

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026 (155 dagen). Alle 7 campagnes in ad account `act_567892422940728` zijn gepauzeerd, de twee Wholesaler Campagnes sinds 4 september. Geen levering, geen spend, op geen enkele campagne.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: op 21 september kwam site-breed (2.175 sessies, 8.211 pageviews, waarvan 1.148 sessies bot-achtig) geen enkele sessie binnen met `utm_source` meta, facebook of instagram of met `utm_campaign=sybb`. Er was één organische Facebook-referral (naar /en_GB/inspiration, 31 seconden, geen SYBB pagina). Over 14 t/m 20 september samen (16.115 sessies): 0 betaalde sessies, 3 organische social referrals, geen daarvan op een SYBB pagina. ChatGPT leverde gisteren 9 sessies, geen daarvan op een SYBB pagina; twee ervan eindigden op /registratie (de B2B accountregistratie), één na 10 minuten.

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren. Lifetime referentie voor een herstartbeslissing (13 januari t/m 19 april 2026): €2.485 spend, 297.174 impressies, 10.851 link clicks, 4,06% CTR, €0,21 CPC, 6 aankopen.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bezoekers | 0 | 0 | n.v.t. | ⚪ |
| Pageviews | 0 | 0 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = geen data. Vierentwintigste dag op rij zonder één sessie op dit domein (sinds 29 augustus, gecontroleerd via de sessions-tabel over 14 t/m 21 september). Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

Interne sessies zijn uit alle cijfers gefilterd, ook uit het 7d-gemiddelde. Het interne cohort is vandaag bijgewerkt: de 30-dagenquery op `edit_translations` en `/odoo` pageviews geeft nu 10 distinct_ids (was 8), en daarbovenop vond ik gisteren twee medewerkers die dat filter niet vangt, omdat ze vanuit de Odoo-backend naar de website klikken (referrer `sempertexeurope.com/odoo`) of op de backend-appsknop klikken zonder ooit een `edit_translations` pageview te maken. Beide zijn Belgische Edge- en Chrome-desktopgebruikers met 12 en 28 sessies sinds 18 en 11 september. Samen 12 interne ids. Bot- en link-preview hits (1 pageview, 0 kliks, 0 tot 8 seconden) tel ik apart.

| Metric | Gisteren (21 sep) | 7d Gemiddelde (14 t/m 20 sep, extern) | Trend |
|--------|-------------------|---------------------------------------|-------|
| Sessies (sessions-tabel) | 16 | 8,0 (56 totaal) | ↑ |
| Waarvan tab-sluiting zonder pageview | 3 | 3 in 7 dagen | |
| Waarvan intern | 4 (2 via het oude filter, 2 nieuw herkend) | 7 in 7 dagen (uitgefilterd) | ↑ |
| Waarvan bot of link-preview | 0 | 21 in 7 dagen (3,0 per dag) | ↓ |
| Echte externe sessies | 9 (waarvan 1 site-scanner) | 3,6 (25 totaal) | ↑ |
| Externe personen | 8 | 23 in 7 dagen | ↑ |
| Pageviews SYBB pagina's (extern) | 22 | n.v.t. | |
| Sessieduur, externe sessies | gemiddeld 501s, mediaan 418s | gemiddeld 810s, mediaan 456s | mediaan → |
| Pageviews per externe sessie | 15,9 (mediaan 5) | 14,4 (mediaan 8) | mediaan ↓ |
| Bounce rate, externe sessies | 11% (1 van 9, de 5-secondenblik van de herhaalbezoeker) | 0% (0 van 25) | ↑ |
| Klik op "Registreer" of "Register" bij SYBB | 0 | 1 in 7 dagen (18 sep) | ↓ |
| Ticket bevestigd | 0 | 1 in 7 dagen | ↓ |
| "Ga naar de betaling" | 0 | 1 in 7 dagen | ↓ |
| Betaald workshopticket | 0 | 1 sessie, 2 deelnemers (18 sep) | ↓ |
| /shop/confirmation zonder ticket | 0 | 2 (14 en 16 sep, webshoporders) | |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 (1 rage click van de site-scanner op een Lagenda-productfoto) | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bekeken SYBB pagina's gisteren (alleen extern):

| Pagina | Pageviews | Bezoekers | Aard |
|--------|-----------|-----------|------|
| /en_GB/event/start-your-balloon-business-professional-7/register | 7 | 1 | de Android-vergelijker, zeven keer in vijf minuten |
| /fr/event/start-your-balloon-business-professionnel-7/register | 2 | 2 | Réunion-bezoeker (51s), Android-vergelijker |
| /de/event/start-your-balloon-business-professionell-7/register | 1 | 1 | Oostenrijkse klant, 45 seconden |
| /en_GB/event/start-your-balloon-business-professional-8/register | 5 | 4 | Google-bezoeker via kalender (26s), Android-vergelijker (2x), NL klant via webshop (einde sessie), site-scanner (23s) |
| /fr/event/start-your-balloon-business-professionnel-8/register | 4 | 1 | Android-vergelijker: Google-landing plus twee herladingen, later nog één keer |
| /en_GB/event/start-your-balloon-business-professional-9/register | 1 | 1 | Android-vergelijker |
| /event/start-your-balloon-business-professional-9/register (NL) | 2 | 2 | NL klant via Content Day en Nozzle Up (einde sessie), BE iPhone-herhaalbezoeker (5s) |

Professional-7 kreeg 10 van de 22 SYBB pageviews, professional-8 kreeg er 9, professional-9 kreeg er 3. Opvallend in de elements chain van de kalender: de kaarttitel van professional-7 heeft de klasse `text-muted` en de knop is `btn-light`, terwijl professional-8 en 9 een gewone titel en een `btn-primary` knop hebben. In Odoo Events is dat het uiterlijk van een event waarvan de inschrijving gesloten of volzet is. Als dat klopt, stuurt de bovenste SYBB-kaart bijna de helft van de SYBB-kliks naar een datum die niet meer te boeken is.

De negen externe sessies van gisteren (tijden lokaal, UTC +2):

| Tijd | Herkomst | Land / device / historie | Pad | Wat gebeurde er |
|------|----------|--------------------------|-----|-----------------|
| 04:26 tot 04:28 | Google | BE, Chrome Android, nl-BE, tweede bezoek ooit (eerste op 31 juli) | /en_GB/events → cookies → klik op de kaarttitel van **professional-8 (EN)** → 26s → terug naar /events → Content Day Winter Wonderland → /events | Een vergelijker die 's nachts de kalender afgaat. 72 seconden, 3 kliks, geen klik op Register. |
| 05:46 tot 05:49 | Google | RE (Réunion), Chrome iOS, fr-FR, eerste bezoek ooit | /fr/shop → mobiel menu → "Ateliers" → klik op de kaart van **professionnel-7 (FR)** → 51s → Balloon Twist Masterclass Sempertex France → klik op de externe link naar sempertexfrance.com | Een Franstalige bezoeker uit Réunion die SYBB bekijkt en daarna via de France-masterclass de site verlaat naar de Franse partnersite. Voor hem is Genk waarschijnlijk niet de bedoeling; de Franse pagina zegt niet dat de workshop in België is. |
| 09:32 tot 09:39 en 12:15 tot 12:24 | Google, daarna direct | BE, Chrome Android, en-US, eerste bezoek ooit | Sessie 1: /fr/shop → cookies → **Google-landing op professionnel-8 (FR)** → twee herladingen (07:34:01 direct, 07:34:05 via Google), 7 minuten. Sessie 2: opent professionnel-8 (FR) → "Tous les événements" → professionnel-7 (FR) → lijst → professionnel-8 (FR) → lijst → taalwissel naar Engels → /en_GB/event → France-masterclass → lijst → **professional-8 (EN)** → lijst → **professional-9 (EN)** → lijst → **professional-7 (EN)** → lijst → professional-7 → lijst → professional-8 → lijst → professional-7 → professional-7 (direct) → logo naar /en_GB → professional-7 (direct, twee keer) → professional-7 via de lijst om 12:24, einde sessie | De sterkste SYBB-bezoeker van de dag: 15 pageviews op SYBB pagina's in twee sessies, drie uur uit elkaar. Google zet een Engelstalige Belg op de Franse pagina; zij wisselt zelf naar Engels en klikt dan zeven keer professional-7 open, afgewisseld met 8 en 9. Dat is iemand die de data, talen en locaties tegen elkaar probeert af te wegen en het antwoord niet op één pagina vindt. Geen klik op Register. |
| 12:20 tot 12:32, tab gesloten 14:07 | Direct (terugkeer op een tulle-productpagina) | NL, Samsung Internet Android, nl-NL, sinds 18 sep (5 sessies, 2 dagen, 1x /my, 1x login) | tulle lichtblauw → mobiel menu → Shop → latex → Pastel Dusk → Pastel Dusk Blue → latex → Metallic → Metallic Fuchsia → 7 minuten → mobiel menu → Workshops → klik op de kaarttitel van **professional-8 (EN)**, einde sessie; tab 1 uur 35 later gesloten | Een nieuwe klant met account die na 12 minuten kleuren kiezen bewust naar Workshops gaat en professional-8 opent als laatste pagina. Wat zij daar deed is onzichtbaar: geen kliks, geen replay. |
| 15:44 tot 15:48, tab gesloten 16:33 | Direct (landing op de Content Day registratiepagina) | NL, Edge desktop, nl, klant sinds 15 aug (5 sessies, 3 dagen, 6 logins) | Content Day Winter Wonderland → klik op het Nozzle Up 2027 spaarplan → Workshops → klik op de blauwe knop van **professional-9 (NL)**, einde sessie; tab 45 minuten later gesloten | Een klant die rechtstreeks op een eventpagina binnenkomt (vermoedelijk uit een mail of bookmark), drie events bekijkt en op SYBB professional-9 eindigt. Geen klik op Registreer. |
| 16:41 | Kalender (/events) | BE, Mobile Safari iPhone, nl-NL, sinds 25 aug (7 sessies, 6 dagen, 30 events) | /events → **professional-9 (NL)**, 5 seconden, bounce | De hardnekkigste SYBB-twijfelaar in de data. Deze persoon begon op 25 augustus een B2B accountregistratie (/signup-choice → /registratie), en opende daarna de Nederlandse pagina van professional-9 op 29 augustus (twee keer), 30 augustus, 1 september, 8 september en gisteren. Zes keer dezelfde pagina in vier weken, altijd via de kalender, nooit een klik op Registreer, nooit langer dan een paar seconden. Dit is de eerste bezoeker bij wie ik een terugkeerpatroon over een maand kan aantonen, en de site doet er niets mee. |
| 17:31 tot 17:44 | Google (1s op /de/team), daarna direct | BE, Chrome desktop Mac, browsertaal Turks, sinds 15 sep (6 sessies, 2 dagen; op 15 sep 18 pageviews in 14 minuten, 2x become-a-distributor) | /de → /en_GB/shop → klik "Register" (B2B) → /registratie → shop → tools → shop → Halloween → accessoires → inflators → 5 Lagenda-producten → **rage click op een productfoto** → /events → shop → 6 categorieën → why-sempertex, newsletter, faq, become-a-distributor, algemene voorwaarden, certificaten (heen en weer, 3 tot 5 seconden per pagina) → inspiration → /events → France-masterclass → /events → **professional-8 (EN)**, 23s → /events | 62 pageviews en 70 kliks in 13 minuten, 3 tot 5 seconden per pagina, inclusief voorwaarden en certificaten. Dit is geen ballonartiest die een workshop zoekt maar iemand die de site in kaart brengt (tester, bureau of concurrent). Ik tel deze sessie als extern maar niet als SYBB-prospect. |
| 17:35 tot 18:00 | Terugkeer (referrer sempertexeurope.com, entry op de winkelmand) | AT (Oostenrijk), Edge desktop, de, klant sinds 24 aug (10 sessies, 3 dagen, 11x /my, 1 order) | /de/shop/cart → latex → Mode Solid → Blau 040 → **"In den Warenkorb"** → accessoires → ballongewichten → **"In den Warenkorb"** → folie cijfers → Festipuntos → /my/home → /my/festipunto → Festipuntos → schort, heuptas → Angebote → Veranstaltungen → klik op de kaarttitel van **professionell-7 (DE)** → 45s → "Alle Veranstaltungen" → France-masterclass → shop → /de/tools | Een Duitstalige klant die tijdens het bestellen even de workshopkalender bekijkt, professional-7 in het Duits opent en na 45 seconden terug naar de lijst gaat. Duitse pagina, Belgische locatie, geen klik op Registrieren. |

Drie observaties:

- **Twee twijfelaars met een duidelijk patroon, nul vangnet.** De Android-vergelijker (15 SYBB pageviews, twee sessies, drie uur ertussen) en de iPhone-herhaalbezoeker (zes bezoeken aan professional-9 sinds 29 augustus) zijn precies de mensen voor wie een "Hou me op de hoogte" of "Stel je vraag" op de registratiepagina bedoeld is. Zij komen terug, ze klikken nooit op Registreer, en na elk bezoek is er niets om op te volgen. Het opt-in punt staat sinds 19 september open en heeft vandaag zijn sterkste bewijs.
- **De vergelijker vindt het antwoord niet op één pagina.** Zeven keer professional-7 openen, afgewisseld met 8 en 9 en de lijst, betekent dat de pagina's onderling niet vertellen waarin ze verschillen (datum, taal van de dag, locatie, prijs, beschikbaarheid). Samen met de `text-muted` titel en `btn-light` knop van professional-7 in de kalender is het beeld: de meest bekeken datum is mogelijk niet meer boekbaar, en de andere twee leggen niet uit waarom je die zou kiezen.
- **Vier van de zestien sessies waren intern, en het bestaande filter miste er twee.** De referrer `sempertexeurope.com/odoo` en de backend-appsknop (`o_frontend_to_backend_apps_btn`) in de elements chain zijn een betrouwbaarder kenmerk dan `edit_translations`. Zonder die correctie had het rapport vandaag 11 externe sessies en twee extra "lange leessessies" gemeld.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte externe bezoekers:
SYBB registratiepagina bekeken (9 sessies, 100%) → klik op "Registreer" of "Register" (0, 0%) → ticket bevestigd (0) → "Ga naar de betaling" (0) → betaald workshopticket (0)

Event funnel, 14 t/m 20 september (7 dagen, extern, zonder intern verkeer en zonder bots):
SYBB registratiepagina bekeken (25 echte sessies, 100%) → klik op "Registreer" of "Register" bij SYBB (1 sessie, 4%) → ticket bevestigd (1, 100% van de starters) → "Ga naar de betaling" (1, 100%) → betaald (1 sessie, 2 deelnemers, 100% van de betaalstarters)

De vier Register-, plus- en betaalkliks van 18 september zijn gisteren opnieuw geverifieerd over alle 34 externe sessies van 14 t/m 21 september: het blijven de enige inschrijfkliks op een SYBB pagina in acht dagen.

Inschrijfpogingen per dag:

| Dag | Echte externe sessies | Klik "Registreer" bij SYBB (sessies) | Ticket bevestigd | "Ga naar de betaling" | Betaald | Uitkomst |
|-----|-----------------------|--------------------------------------|------------------|-----------------------|---------|----------|
| 14 sep | 5 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket, 2 interne sessies, 1 bot |
| 15 sep | 1 | 0 | 0 | 0 | 0 | 1 vergelijker, 3 link-previews |
| 16 sep | 3 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket (77 pageviews), 6 bots, 2 intern |
| 17 sep | 1 | 0 | 0 | 0 | 0 | 1 lange leessessie, 3 bots, 3 intern |
| 18 sep | 5 | 1 | 1 | 1 | **1 (2 deelnemers)** | betaald met kaart, 17 minuten van landing tot bevestiging |
| 19 sep | 3 | 0 | 0 | 0 | 0 | 1 NL vergelijker twee keer terug, 1 BE klant, 2 link-previews |
| 20 sep | 7 | 0 | 0 | 0 | 0 | Malta-lead, 2 starters via tools en blog, 2 klanten, koper van 18 sep 3x terug, 1 Google-landing; de ChatGPT-bounce van 6s valt in het botfilter |
| 21 sep | 9 | 0 | 0 | 0 | 0 | Android-vergelijker 2x, iPhone-herhaalbezoeker (6e keer), AT klant, 2 NL klanten, Réunion, Google-vergelijker, 1 site-scanner, 4 intern, 0 bots |

**Grootste lek:** ongewijzigd de stap van "pagina bekeken" naar "klik op Registreer": 1 van 25 in de week ervoor, 0 van 9 gisteren. Wie klikt, komt door. Gisteren voegt daar een nuance aan toe: het lek zit niet alleen op de pagina zelf, maar ook tussen de pagina's. De vergelijker springt tussen drie data zonder te kiezen, en de bovenste kaart in de kalender lijkt een gesloten datum te zijn.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echt extern | Betaald workshopticket | /shop/confirmation zonder ticket | Eindigde op SYBB pagina |
|---------|--------------|-------------|------------------------|----------------------------------|-------------------------|
| Gisteren | 16 | 9 | 0 | 0 | 5 (professional-7 EN 1x, professional-8 EN 1x, professional-9 NL 2x, plus 3 tab-sluitingen op 7, 8 en 9) |
| 14 t/m 20 sep | 56 | 25 | 1 (2 deelnemers) | 2 | n.v.t. |

Warme pool (laatste 30 dagen, 22 augustus t/m 21 september): 162 personen in 200 sessies bekeken een SYBB registratiepagina. Daar zitten 12 interne distinct_ids, 73 bot- of preview-sessies en 16 tab-sluitingen in, dus reken op circa 90 echte personen als retargeting-doelgroep bij herstart, waarvan er nu 2 betaald hebben. Vijf van de 200 sessies raakten /shop/confirmation: 2 echte tickets (9 en 18 september) en 3 webshoporders. Geen enkele sessie in 30 dagen kwam via `utm_source=meta`.

## 5. Rode Vlaggen 🚩

- **Nul inschrijfpogingen bij 9 externe bezoeken, voor de derde dag op rij.** 20 september 7, 21 september 9, samen 16 echte sessies zonder één klik op Registreer. De enige klik van de week blijft die van de betaler van 18 september.
- **De herhaalbezoeker van professional-9 is voor de zesde keer vertrokken zonder spoor.** BE, iPhone, sinds 25 augustus: zes bezoeken aan dezelfde Nederlandse pagina, nooit een klik. Zonder e-mail opt-in of vraagknop op de pagina blijft dit onzichtbaar voor sales.
- **Professional-7 lijkt gesloten en staat bovenaan.** `text-muted` titel en `btn-light` knop in de kalender, terwijl 8 en 9 `btn-primary` hebben. Professional-7 kreeg gisteren 10 van de 22 SYBB pageviews. Controleer vandaag of de inschrijving dicht is; zo ja, dan staat de meest geklikte SYBB-kaart op een doodlopende datum.
- **Google zet Belgische bezoekers op de Franse en Duitse pagina's.** De Android-vergelijker (en-US) landde op /fr, de Réunion-bezoeker vertrok via professionnel-7 naar sempertexfrance.com, de Oostenrijkse klant las professionell-7 in het Duits. Geen van die taalversies zegt dat de workshop in Genk is en in welke taal de dag gegeven wordt. De vergelijker moest zelf naar Engels wisselen.
- **Intern cohort onvolledig.** Twee medewerkers (BE, Edge en Chrome desktop, 12 en 28 sessies sinds 18 en 11 september) worden niet gevangen door het `edit_translations`/`/odoo` pageview-filter en zaten gisteren voor 18 minuten in de SYBB-cijfers. Het cohort staat nu op 12 ids en is nog steeds niet in PostHog zelf gemarkeerd.
- **Session replay zestiende dag op nul.** 14 t/m 21 september nul opnames in `session_replay_events`. De 9 minuten van de vergelijker op professional-7, 8 en 9 zijn niet terug te kijken.
- **Structureel, ongewijzigd:** SYBB campagne 155 dagen gepauzeerd, landing page 24 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer.

Niet rood: bots (0 gisteren, tegen 3,0 per dag vorige week), rage en dead clicks op SYBB pagina's (0; de ene rage click van de site-scanner zat op een Lagenda-productfoto), CPC en frequency (geen levering), vals-positieve conversies (0), wholesaler-formulier (gisteren 4 pageviews in 3 sessies, geen starts, geen fouten, geen inzendingen), PostHog events-tabel (antwoordde vandaag weer binnen 1 seconde, na de hangers van vanochtend).

## 6. Top 3 Acties voor Vandaag

1. **Zet vandaag een "Hou me op de hoogte" opt-in op de vier SYBB registratiepagina's.** Wat: één regel plus e-mailveld direct onder de datum en boven de Registreer-knop, in NL, EN, DE en FR: "Nog niet zeker? Laat je e-mail achter en we sturen je het programma, de prijs en de eerstvolgende data." Koppel de inzendingen aan een Odoo mailinglijst "SYBB twijfelaars" en laat sales binnen 24 uur handmatig opvolgen. Waarom: gisteren twee bewijsbare twijfelaars zonder vangnet: de Android-vergelijker met 15 SYBB pageviews in twee sessies en de iPhone-bezoeker die professional-9 sinds 29 augustus zes keer heeft geopend. Beide vertrokken zonder spoor, net als de 7 warme bezoekers van 20 september. Dit is actie 2 van 19 september, nu met het sterkste bewijs tot nu toe. Hoe: Odoo website-editor, formulierblok (snippet "Formulier") op de vier eventpagina's, 1 uur inclusief vertalingen; de bevestigingstekst met het programma en de prijs komt uit `Bronnen/Sempertex Europe/sybb-8-pillars.md` (pillar 1 Mindset als opening). Verwachte impact: van de circa 4 echte SYBB-bezoekers per dag houd je er 1 tot 2 per week vast als opvolgbare lead, waar het nu nul is. Escalatie: Oranje (editorwijziging), Geel voor de tekst.
2. **Controleer of professional-7 nog boekbaar is en herschik de kalender.** Wat: open /events en /en_GB/events op een niet-ingelogde browser en check de SYBB-kaart van professional-7: is de inschrijving gesloten of volzet, dan de kaart markeren als "Volzet" of "Inschrijving gesloten" en professional-8 en 9 erboven zetten; blijft hij open, dan de knop op `btn-primary` zetten zoals bij 8 en 9. Waarom: in de elements chain van gisteren heeft de titel van professional-7 de klasse `text-muted` en de knop `btn-light`, het Odoo-uiterlijk van een gesloten event, terwijl professional-7 als bovenste kaart 10 van de 22 SYBB pageviews kreeg en de vergelijker er zeven keer op klikte. Hoe: Odoo Events, event professional-7 openen, registratiestatus en volgorde in de kalender (15 minuten); als het event dicht is, in de website-editor de kaartvolgorde aanpassen (30 minuten). Verwachte impact: elke SYBB-klik uit de kalender komt op een boekbare datum terecht, en de vergelijker hoeft niet meer te raden welke datum nog kan. Escalatie: Geel (check), Oranje (herschikken).
3. **Zet op elke SYBB registratiepagina een blok "Alle data op een rij" met taal, locatie, prijs en beschikbaarheid.** Wat: een tabel direct onder de intro op de pagina's van professional-7, 8 en 9 (alle taalversies): datum, taal van de dag (Nederlands, Engels), locatie Miënbroekstraat 43 Genk (met "België" erbij voor de FR- en DE-versies), prijs per deelnemer, aantal plaatsen nog vrij, en een knop per datum. Waarom: de Android-vergelijker klikte gisteren in negen minuten vijftien keer tussen 7, 8, 9 en de lijst, wisselde zelf van Frans naar Engels en vond blijkbaar nergens het overzicht; de Réunion-bezoeker en de Oostenrijkse klant lazen de FR- en DE-versie zonder te zien dat de workshop in België is. Dit combineert het locatieblok van 19 september en het "Praktisch"-blok van 20 september tot één vergelijkingsblok. Hoe: Odoo website-editor, één tabel-snippet gekopieerd naar drie events in vier talen (1,5 uur); beschikbaarheid komt uit de ticketinstellingen van het event. Verwachte impact: de keuze tussen data gebeurt op de pagina in plaats van door heen en weer klikken, en anderstalige bezoekers weten direct of Genk voor hen haalbaar is. Escalatie: Geel (tekst en prijs), Oranje (plaatsing).

Blijft open uit eerdere rapporten: de opvolging van de Malta-lead van 20 september met SYBB in het aanbod (actie 1 van gisteren, geen nieuw bezoek van die persoon gezien), de bevestigingsmail van de inschrijving van 18 september controleren op een directe link en praktische info (actie 2 van gisteren, nu deels in actie 3 hierboven), een SYBB-blok in de kostprijscalculator en de blog "how to become a balloon artist" (actie 3 van gisteren), controleren wat /en_GB/start-your-balloon-business-3 is (gisteren geen nieuwe hits), session replay aanzetten op https://eu.posthog.com/project/149694/settings/environment-replay (zestiende dag), het interne cohort (nu 12 distinct_ids, inclusief de twee via de Odoo-referrer herkende medewerkers) in de PostHog projectinstellingen markeren, de betaalstap testen op de wachttijd van 13 minuten op /payment/status, het wholesaler-formulierlek dichten (gisteren geen nieuwe fout), bepalen of het webshop-product van 5 en 6 oktober (id 5290) naast de event-registratie het canonieke verkoopkanaal is, de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`), één gedeelde en gecachte Meta-call per dag voor de drie rapporten, en het aanpassen van de funneldefinitie in `skills/daily-sybb-report/SKILL.md` van landing page naar event funnel.

---

**Databronnen:** Meta Ads via Pipeboard (MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` vroegen om autorisatie, niet mogelijk in deze non-interactieve sessie; de directe JSON-RPC route werkte: één call, campaign-level insights voor campagne 120239435987290239 over 15 t/m 21 september met `time_increment: 1`, antwoord `data: []` in 2,2 seconden; campagnestatus uit het live ads-rapport van 22 september; Pipeboard-weekverbruik na deze run 12 van 30). PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): sessions-tabel per sessie voor 21 september (16 rijen) en 14 t/m 20 september (56 rijen), landing page per dag, site-breed per dag met entry-source, ChatGPT- en bot-telling, session replay events per dag, intern cohort (30 dagen, 10 ids via pageviews), pageviews en autocapture met elements chain voor de 11 niet-interne sessies van gisteren (vier queries, gesplitst om de limiet van 100 rijen te vermijden), persoonsprofielen voor 13 distinct_ids sinds 1 juni, sessies met SYBB pagina en /shop/confirmation over 14 t/m 21 september, 30d warme pool, wholesaler-events van 21 september, de volledige pageview-historie van de iPhone-herhaalbezoeker, de sessies van de site-scanner sinds 1 september, Register-, ticket- en betaalkliks over alle 34 externe sessies van 14 t/m 21 september, de social referral en de ChatGPT-sessies van gisteren. Zeventien queries, alle onder 2,5 seconden; de events-tabel antwoordde weer normaal na de hangers van vanochtend. Periode gisteren = 21 september 2026 UTC, 7d = 14 t/m 20 september 2026 (extern, zonder intern verkeer en zonder bots). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt, geen weekoverzicht geschreven (output beperkt tot de daily-map).
