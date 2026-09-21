# SYBB Daily Report: 20 september 2026

## 1. Samenvatting
Zondag 20 september was de drukste SYBB-dag van de week zonder één inschrijfpoging. Acht externe sessies van acht verschillende personen op de SYBB registratiepagina's (zeven echte bezoeken plus één 6-secondenbounce via ChatGPT), nul kliks op Registreer, nul betalingen. Voor het eerst deze week zat er geen link-preview bot tussen. De kwaliteit van de bezoekers was hoog en dat maakt de nul pijnlijker. De nieuwe wholesaler-lead uit Malta die 's ochtends om 11:13 het distributeursformulier instuurde (na één formulierfout), kwam 's middags terug, klikte op de B2B-registratieknop, bekeek de Lagenda inflators en eindigde een minuut op de Engelse pagina van professional-9. De koper van 18 september kwam drie keer terug, downloadde het combinatiepakket en de catalogus, en klikte om 01:43 's nachts handmatig via Workshops naar professional-7, 8 en 9, de datum die hij zelf geboekt heeft. Twee Nederlandse starters gingen via de tools (kostprijscalculator, kleurtool) en de blog "how to become a balloon artist" naar SYBB, één daarvan las drie FAQ's over kwalificaties en bijbaan voordat zij 13 seconden op professional-8 keek. Twee bestaande klanten (17 en 34 sessies sinds juli en augustus) bekeken professional-7. Een nieuwe Google-bezoeker landde rechtstreeks op de Nederlandse pagina van professional-8 en vertrok naar de Falcone-tour. Meta was vandaag weer live bereikbaar en bevestigt nul levering op `2026: SYBB` over 14 t/m 20 september; de campagne staat 154 dagen op PAUSED. De landing page startyourballoonbusiness.com staat voor de drieëntwintigste dag op 0 bezoekers en session replay leverde voor de vijftiende dag nul opnames.

## 2. Meta Ads Performance

**Status data:** live. De Pipeboard-weeklimiet is vannacht gereset; de directe JSON-RPC route gaf op de eerste call (campaign-level, campagne 120239435987290239, 14 t/m 20 september) direct antwoord: `data: []`, dus geen levering en geen spend. Geen verdere Meta-calls gedaan om de limiet voor de rest van de week te sparen; de campagnestatus komt uit het live ads-rapport van vanochtend (get_campaigns, 7 campagnes).

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026 (154 dagen). Alle 7 campagnes in ad account `act_567892422940728` zijn gepauzeerd, de twee Wholesaler Campagnes sinds 4 september. Geen levering, geen spend, op geen enkele campagne.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: op 20 september kwam site-breed (1.457 sessies, 3.903 pageviews) geen enkele sessie binnen met `utm_source` meta, facebook of instagram of met `utm_campaign=sybb`, en er was geen enkele organische referral vanaf facebook.com of instagram.com. Over 13 t/m 19 september samen (16.413 sessies): 0 betaalde sessies, 8 organische social referrals, geen daarvan op een SYBB pagina. Ter vergelijking: ChatGPT leverde 12 sessies gisteren en 71 in de zeven dagen ervoor, waarvan er gisteren één rechtstreeks op de Franse pagina van professionnel-9 landde.

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

Toelichting: ⚪ = geen data. Drieëntwintigste dag op rij zonder één sessie op dit domein (sinds 29 augustus, gecontroleerd via de sessions-tabel over 13 t/m 20 september). Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

Interne sessies (8 distinct_ids met pageviews op `edit_translations` of `/odoo` in de laatste 30 dagen, één meer dan vorige week) zijn uit alle cijfers gefilterd, ook uit het 7d-gemiddelde. Bot- en link-preview hits (1 pageview, 0 kliks, 0 tot 8 seconden) tel ik apart. De 6-secondenbounce via ChatGPT van gisteren valt technisch in dat botprofiel, maar heeft een `utm_source=chatgpt.com` en een Belgische iPhone met fr-FR, dus ik tel hem als externe bezoeker en vermeld hem apart.

| Metric | Gisteren (20 sep) | 7d Gemiddelde (13 t/m 19 sep, extern) | Trend |
|--------|-------------------|---------------------------------------|-------|
| Sessies (sessions-tabel) | 10 | 7,4 (52 totaal) | ↑ |
| Waarvan tab-sluiting zonder pageview | 2 | 1 in 7 dagen | |
| Waarvan intern | 0 | 7 in 7 dagen (uitgefilterd) | |
| Waarvan bot of link-preview | 0 | 20 in 7 dagen (2,9 per dag) | ↓ |
| Echte externe sessies | 8 (7 met interactie, 1 ChatGPT-bounce) | 3,4 (24 totaal) | ↑ |
| Externe personen | 8 | 22 in 7 dagen | ↑ |
| Pageviews SYBB pagina's | 14 (alle echt) | n.v.t. | |
| Sessieduur, echte externe sessies met interactie | gemiddeld 1.084s, mediaan 694s | gemiddeld 579s, mediaan 300s | ↑ |
| Pageviews per echte sessie | 8,4 (mediaan 8) | 15,3 (mediaan 7) | mediaan → |
| Bounce rate (sessions-tabel) | 12,5% (1 van 8, de ChatGPT-bounce) | 38% (20 van 52, allemaal bots) | ↓ |
| Bounce rate, echte externe sessies met interactie | 0% (0 van 7) | 0% (0 van 24) | → |
| Bezoeken van 6 seconden of korter (echt) | 1 van 8 | 1 van 24 | |
| Klik op "Registreer" of "Register" bij SYBB | 0 | 1 in 7 dagen (18 sep) | ↓ |
| Ticket bevestigd | 0 | 1 in 7 dagen | ↓ |
| "Ga naar de betaling" | 0 | 1 in 7 dagen | ↓ |
| Betaald workshopticket | 0 | 1 sessie, 2 deelnemers (18 sep) | ↓ |
| /shop/confirmation zonder ticket | 0 | 2 (14 en 16 sep, webshoporders) | |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers | Aard |
|--------|-----------|-----------|------|
| /en_GB/event/start-your-balloon-business-professional-7/register | 6 | 3 | tools-gebruiker (3x), bestaande klant (1x), koper van 18 sep (2x) |
| /event/start-your-balloon-business-professional-7/register (NL) | 2 | 1 | bestaande klant, circa 10 minuten na de tweede klik |
| /en_GB/event/start-your-balloon-business-professional-8/register | 2 | 2 | blog-lezer (13s), koper van 18 sep (8s) |
| /event/start-your-balloon-business-professional-8/register (NL) | 1 | 1 | nieuwe Google-bezoeker, landingspagina, 23 seconden |
| /en_GB/event/start-your-balloon-business-professional-9/register | 2 | 2 | Malta-lead (circa 1 minuut), koper van 18 sep (einde sessie) |
| /fr/event/start-your-balloon-business-professionnel-9/register | 1 | 1 | ChatGPT-referral (BE, iPhone), 6 seconden |

Professional-7 kreeg 8 van de 14 SYBB pageviews. Het is de bovenste SYBB-kaart in de kalender en daarmee de eerste klik van vrijwel iedereen die via Workshops binnenkomt.

De acht externe sessies van gisteren (tijden lokaal, UTC +2):

| Tijd | Herkomst | Land / device / historie | Pad | Wat gebeurde er |
|------|----------|--------------------------|-----|-----------------|
| 11:07 tot 11:31 en 15:36 tot 15:47 | Direct | MT, Chrome iOS, en-GB, eerste bezoek ooit (09:07 UTC) | Sessie 1: /en_GB → /become-a-distributor → formulierstart 11:09 → formulierfout 11:12 → **inzending 11:13** → /web/reset_password. Sessie 3: /en_GB → Workshops → Shop → klik "Register" (B2B account, 3s op /registratie) → Shop → inflation equipment → Lagenda 12 inflator (5x door de fotocarrousel) → Halloween → latex → pastel matte → Halloween p2 → Workshops → **professional-9 (EN)**, sessie eindigt na circa 1 minuut, tab gesloten 17:25 | De organische wholesaler-inzending uit Malta van vanochtend is dezelfde persoon die 's middags SYBB bekijkt. Hij probeert eerst een account (reset_password, B2B Register) en kijkt daarna naar apparatuur en de workshop. Geen klik op Register bij SYBB. |
| 12:02 tot 12:34 | Terugkeer (referrer sempertexeurope.com) | NL, Chrome desktop Windows, nl, klant sinds 17 aug (29 sessies, 17 dagen, 1 order, 6 keer /my) | shop-categorie latex onbedrukt → 12:24 klik "Workshops" → /events → SYBB professional-7 (NL) → /events → knop op de SYBB-kaart → professional-7 (NL), einde sessie 12:34 | Bestaande klant die vanuit de webshop bewust naar de workshopkalender gaat en twee keer professional-7 opent. Circa 10 minuten op de pagina, geen klik op Registreer. |
| 13:53 tot 13:55 | Google | NL, Chrome Android, nl-NL, eerste bezoek ooit | **landt op professional-8 (NL)** → cookies accepteren → 23s → "Alle Evenementen" → Falcone-tour → 2x klik op de externe link van hahaentertainment | Google stuurt een nieuwe bezoeker rechtstreeks op een SYBB pagina, maar die vertrekt binnen een halve minuut naar de Falcone-workshop en verlaat de site via de partnerlink. |
| 17:20 | ChatGPT (`utm_source=chatgpt.com`) | BE, Mobile Safari iPhone, fr-FR, 2 events in de projecthistorie | /fr/event/start-your-balloon-business-professionnel-9/register, 6 seconden, bounce | Eerste SYBB-sessie ooit met een ChatGPT-UTM. Zes seconden op een Franse registratiepagina is niet genoeg om iets te lezen. |
| 22:30 tot 22:41 | Google | NL, Chrome Android, nl-NL, sinds 1 sep (4 sessies, 2 keer winkelmandje, geen order) | / → "Open de tools" → 11 kleurswatches (Honey Yellow, Rosewood, Violet, Merlot, Cosmo Pink, Fuchsia, Sunset Orange, Black, Urban Grey, Lilac, Mocha) → Kostprijscalculator (materiaal, overhead, winstvermenigvuldiger) → Kleurtool → Workshops → **professional-7 (EN, 2 min)** → MBP Exam → professional-7 → Content Day Winter Wonderland → professional-7 → "See all" → Nozzle Up 2027 spaarplan → Tools → Colour Tool, Saved palettes, segmenten 3/5/3/4 | Iemand die zelf prijzen berekent en kleurpaletten bouwt, en tussendoor drie keer professional-7 opent. Dit is het SYBB-profiel (pillar 7 Pricing, pillar 8 Techniques). Geen klik op Register. |
| 23:28 | Direct | NL, Chrome Android, nl, klant sinds 19 jul (34 sessies, 17 dagen, 3 orders, 11 keer /my) | /en_GB → Workshops → professional-7 (EN), 10 seconden totaal | Bestaande klant die 's avonds even naar de workshop kijkt. Eerder op de dag (14:32) 11 minuten in de webshop. |
| 23:38 tot 00:25 | Direct | NL, Mobile Safari iPhone, nl-NL, sinds 18 sep (2 sessies; eerste bezoek via Google op de Lagenda inflator) | /en_GB → "Open the tools" → Kostencalculator (1 min) → blog "how to become a balloon artist" → 3 FAQ's geopend ("kwalificatie of licentie nodig?", "verschil kunstenaar en decorateur", "als bijbaantje?") → spiraalboog blog (YouTube-klik) → slinger blog (2 FAQ's) → knoop-blog → Workshops → **professional-8 (EN, 13s)** → Content Day (1 min) → Inspiratie → YouTube-kanaal | Een starter die 46 minuten leest over beginnen als ballonartiest en daarna 13 seconden aan SYBB geeft. De blog beantwoordt precies de vragen die SYBB ook beantwoordt, maar linkt niet naar de workshop. |
| 22:54, 23:30 en 01:43 tot 02:07 (21 sep) | Direct, daarna terugkeer | NL, Safari desktop Mac (1194px), nl-NL, **de koper van 18 september** (2 deelnemers, kaartbetaling) | Sessie 1 (213s, 14 pv): / → ... → /inspiration. Sessie 3: /inspiration → tab Downloads (3 kliks) → **download combinations.zip** → Issuu-catalogus → Shop → Workshops → datumbadge professional-7 → knop professional-7 → knop professional-8 → Content Day kaart → **knop professional-9** (de geboekte datum), einde sessie 02:07 | De enige betaler van de week komt drie keer terug, haalt het combinatiepakket en de catalogus op en zoekt daarna via het menu zijn eigen workshopdatum op. Hij komt niet via een link uit een bevestigingsmail binnen. |

Drie observaties:

- **De warme bezoekers komen nu van drie kanten, en geen enkele klikt.** Malta (wholesaler-lead), twee tools- en bloggebruikers (starters), twee bestaande klanten, één Google-landing op een SYBB pagina. Zeven echte sessies met een mediaan van 11,5 minuten, nul kliks op Register. Vorige week was het profiel "vergelijkers via de kalender"; gisteren was het "mensen met een reden", en het resultaat is hetzelfde.
- **De koper van 18 september zoekt zijn eigen datum op via het menu.** Drie sessies in één avond, download van het combinatiepakket, de catalogus, en om 01:43 handmatig naar professional-9. Hij landde niet via een link. Dat wijst erop dat de bevestigingsmail hem niet naar de eventpagina brengt, of dat de pagina niet vertelt wat hij na het boeken moet weten (tijd, adres, meenemen, parkeren). Het sluit aan op de locatievraag van 18 en 19 september.
- **Malta koppelt de twee funnels.** De organische distributeursaanvraag (na een formulierfout, de derde fout sinds de pauze) en het SYBB-bezoek zijn één persoon binnen 2,5 uur. Voor een nieuwe wholesaler in een klein land is SYBB het logische onboarding-aanbod. Niets op de site legt die link.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte externe bezoekers:
SYBB registratiepagina bekeken (8 sessies, 100%) → klik op "Registreer" of "Register" (0, 0%) → ticket bevestigd (0) → "Ga naar de betaling" (0) → betaald workshopticket (0)

Event funnel, 13 t/m 19 september (7 dagen, extern, zonder intern verkeer en zonder bots):
SYBB registratiepagina bekeken (24 echte sessies, 100%) → klik op "Registreer" of "Register" bij SYBB (1 sessie, 4%) → ticket bevestigd (1, 100% van de starters) → "Ga naar de betaling" (1, 100%) → betaald (1 sessie, 2 deelnemers, 100% van de betaalstarters)

Inschrijfpogingen per dag:

| Dag | Echte externe sessies | Klik "Registreer" bij SYBB (sessies) | Ticket bevestigd | "Ga naar de betaling" | Betaald | Uitkomst |
|-----|-----------------------|--------------------------------------|------------------|-----------------------|---------|----------|
| 13 sep | 6 | 0 | 0 | 0 | 0 | 1 bezoeker klikte 5 keer op Register, maar bij de France Christmas masterclass |
| 14 sep | 5 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket, 2 interne sessies, 1 bot |
| 15 sep | 1 | 0 | 0 | 0 | 0 | 1 vergelijker, 3 link-previews |
| 16 sep | 3 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket (77 pageviews), 6 bots, 2 intern |
| 17 sep | 1 | 0 | 0 | 0 | 0 | 1 lange leessessie, 3 bots, 3 intern (één meer dan vorige week door het bijgewerkte interne cohort) |
| 18 sep | 5 | 1 | 1 | 1 | **1 (2 deelnemers)** | betaald met kaart, 17 minuten van landing tot bevestiging |
| 19 sep | 3 | 0 | 0 | 0 | 0 | 1 NL vergelijker twee keer terug, 1 BE klant, 2 link-previews |
| 20 sep | 8 | 0 | 0 | 0 | 0 | Malta-lead, 2 starters via tools en blog, 2 klanten, koper van 18 sep 3x terug, 1 Google-landing, 1 ChatGPT-bounce, 0 bots |

**Grootste lek:** ongewijzigd de stap van "pagina bekeken" naar "klik op Registreer": 1 van 24 in de week ervoor, 0 van 8 gisteren. Wie klikt, komt door: de enige starter van de week betaalde. Gisteren is de eerste dag waarop de bezoekers niet als vergelijkers via de kalender binnenkwamen maar met een eigen aanleiding (formulier, tools, blog, eerdere aankoop), en ook zij stoppen op de pagina zelf. Dat versmalt het probleem tot de registratiepagina: wat er staat, en wat er niet staat (locatie, programma, prijs zichtbaar zonder ticketvenster).

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echt extern | Betaald workshopticket | /shop/confirmation zonder ticket | Eindigde op SYBB pagina |
|---------|--------------|-------------|------------------------|----------------------------------|-------------------------|
| Gisteren | 10 | 8 | 0 | 0 | 6 (professional-7 3x, professional-9 3x incl. de 2 tab-sluitingen) |
| 13 t/m 19 sep | 52 | 24 | 1 (2 deelnemers) | 2 | n.v.t. |

Warme pool (laatste 30 dagen, 21 augustus t/m 20 september): 160 personen in 193 sessies bekeken een SYBB registratiepagina. Daar zitten 8 interne distinct_ids, 64 bot- of preview-sessies en 12 tab-sluitingen in, dus reken op circa 90 echte personen als retargeting-doelgroep bij herstart, waarvan er nu 2 betaald hebben. Vijf van de 193 sessies raakten /shop/confirmation: 2 echte tickets (9 en 18 september) en 3 webshoporders.

## 5. Rode Vlaggen 🚩

- **Nul inschrijfpogingen bij 8 externe bezoeken, waarvan 5 met een duidelijke aanleiding.** Een verse wholesaler-lead, twee starters die eerst de kostprijscalculator en de starter-blog gebruikten, en twee terugkerende klanten. Mediaan 11,5 minuten op de site, 0 kliks op Register. De pagina zelf houdt ze tegen, niet de aanvoer.
- **De koper van 18 september navigeert handmatig naar zijn geboekte datum.** Drie bezoeken in één avond zonder inkomende link, eindigend op professional-9. Controleer wat de bevestigingsmail bevat en of de eventpagina de praktische info na boeking geeft.
- **Derde wholesaler-formulierfout sinds de pauze, ditmaal bij Malta.** De inzending lukte na 1 minuut alsnog, maar het formulier hapert zonder betaald verkeer nog steeds (18 september Letland, 20 september tweemaal Malta: fout en daarna inzending).
- **Starter-blog en tools linken niet naar SYBB.** Twee bezoekers gingen gisteren via /tools en /blog/how-to-become-a-balloon-artist naar de workshopkalender, op eigen kracht en via het menu. De blog beantwoordt de FAQ "heb je een kwalificatie nodig?" zonder de workshop te noemen.
- **Session replay vijftiende dag op nul.** 13 t/m 20 september nul opnames in `session_replay_events`. Ook de sessies van Malta en de teruggekeerde koper zijn niet terug te kijken.
- **Structureel, ongewijzigd:** SYBB campagne 154 dagen gepauzeerd, landing page 23 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer.

Niet rood: bots (0 gisteren, tegen 2,9 per dag vorige week), intern verkeer (0 sessies gisteren), rage en dead clicks op SYBB pagina's (0), CPC en frequency (geen levering), vals-positieve conversies (0), bounce rate bij echte bezoekers (0%). De Pipeboard-limiet is gereset en de Meta-route werkt weer.

Controlepunt, niet rood: op /en_GB pagina's verschenen gisteren Nederlandse teksten in de elements chain (FAQ-titels op de Engelse blog "how to become a balloon artist", "Kostencalculator" op /en_GB/tools, "Inspiratie" in de navigatie). Mogelijk ontbrekende vertalingen in Odoo, mogelijk browser-i18n van de tools. Even nakijken op een Engelse browser.

## 6. Top 3 Acties voor Vandaag

1. **Bel of mail de Malta-lead vandaag en neem SYBB mee in het aanbod.** Wat: bij de opvolging van de distributeursaanvraag van 20 september 11:13 (Malta, formulierfout om 11:12, inzending om 11:13) expliciet SYBB professional-9 noemen als onboarding voor een nieuwe markt, plus een antwoord op de accountvraag (de persoon probeerde een wachtwoordreset en klikte op de B2B-registratieknop zonder het formulier in te vullen). Waarom: dezelfde persoon bekeek 2,5 uur na de inzending de Lagenda inflators en professional-9; dat is de eerste keer dat de wholesaler-funnel en de SYBB-funnel in één bezoeker samenkomen. Hoe: handmatig, sales, 20 minuten; de PostHog persoon is `01a0be12-0945-7989-b3e4-2aadffaf06ed`, de inzending staat in het Odoo formulier van 20 september. Verwachte impact: één warme lead die anders in de gewone wholesaler-wachtrij belandt, met een concrete kans op een SYBB-ticket uit een nieuw land. Escalatie: Groen (opvolging) en Geel (SYBB-aanbod in de mail).
2. **Controleer de bevestigingsmail en zet de praktische info na boeking op de eventpagina.** Wat: open de Odoo bevestigingsmail van de inschrijving van 18 september (2 deelnemers, professional-9) en check of er een directe link naar de eventpagina in staat en of tijd, adres Miënbroekstraat 43 Genk, parkeren, reistijd en "wat neem je mee" erin staan. Zet diezelfde info als blok "Praktisch" op de vier SYBB registratiepagina's (NL, EN, DE, FR), direct onder de datum, boven de Registreer-knop. Waarom: de koper kwam gisteren drie keer terug en klikte om 01:43 handmatig via Workshops naar zijn geboekte datum; dat doe je alleen als de mail je niet brengt waar je moet zijn. Bovendien was de locatie op 18 en 19 september al het enige klikdoel van de bezoekers. Dit vervangt actie 1 van 19 september (blok "Locatie en reizen") en maakt hem breder. Hoe: Odoo Events, e-mailsjabloon van de registratiebevestiging controleren (15 minuten), tekstblok in de website-editor in vier taalversies (45 minuten). Verwachte impact: kopers hoeven niet te zoeken, en twijfelaars zien vóór het ticketvenster wat de dag inhoudt. Escalatie: Geel (Robin keurt de tekst goed), Oranje voor de editorwijziging.
3. **Zet een SYBB-blok in de kostprijscalculator en in de blog "how to become a balloon artist".** Wat: onder de uitkomst van de kostprijscalculator op /tools en /en_GB/tools één zin plus knop: "Wil je dit leren toepassen op je hele business? Start Your Balloon Business, volgende datum [datum], Genk." Hetzelfde blok onder de FAQ "Heb je een kwalificatie of licentie nodig?" in de blog, in alle taalversies, met een rechtstreekse link naar de eerstvolgende SYBB registratiepagina (niet naar /events). Waarom: twee van de zeven echte bezoekers gisteren gingen tools → blog → SYBB op eigen kracht en gaven de workshoppagina daarna 13 seconden tot 2 minuten; de content die hun vraag beantwoordt, wijst nu niet naar het product dat de vraag oplost. Dit is het open punt "in de starter-blogs rechtstreeks naar de eerstvolgende SYBB datum linken", nu met bewijs. Hoe: Odoo website-editor, twee pagina's plus de blog, 1 uur; hook uit `Bronnen/Sempertex Europe/sybb-8-pillars.md` pillar 7 (Pricing). Verwachte impact: de warmste organische bezoekers (rekenaars en lezers) krijgen de workshop aangeboden op het moment dat ze de vraag stellen, in plaats van via drie menuklikken. Escalatie: Geel (tekst) en Oranje (plaatsing).

Blijft open uit eerdere rapporten: de e-mail opt-in voor twijfelaars op de SYBB registratiepagina's (actie 2 van 19 september, gisteren opnieuw 7 warme bezoekers zonder vangnet), controleren wat /en_GB/start-your-balloon-business-3 is (gisteren geen nieuwe hits), session replay aanzetten op https://eu.posthog.com/project/149694/settings/environment-replay, de inschrijving van 18 september in Odoo controleren en de koper vragen waar de link vandaan kwam (nu te combineren met actie 2), de betaalstap testen op de wachttijd van 13 minuten op /payment/status, SYBB een eigen blok bovenaan /events geven (professional-7 vangt als bovenste kaart 8 van de 14 pageviews), het wholesaler-formulierlek dichten (derde fout sinds de pauze), bepalen of het webshop-product van 5 en 6 oktober (id 5290) naast de event-registratie het canonieke verkoopkanaal is, de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`), het interne cohort (nu 8 distinct_ids) in de PostHog projectinstellingen markeren, één gedeelde en gecachte Meta-call per dag voor de drie rapporten, en het aanpassen van de funneldefinitie in `skills/daily-sybb-report/SKILL.md` van landing page naar event funnel.

---

**Databronnen:** Meta Ads via Pipeboard (MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` vroegen om autorisatie, niet mogelijk in deze non-interactieve sessie; de directe JSON-RPC route werkte na de reset van de weeklimiet: één call, campaign-level insights voor campagne 120239435987290239 over 14 t/m 20 september, antwoord `data: []`; campagnestatus uit het live ads-rapport van 21 september). PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): sessions-tabel per sessie voor 13 t/m 20 september (SYBB pagina's, 62 rijen), landing page per dag, site-breed per dag met entry-source, ChatGPT- en bot-telling, session replay events per dag, 30d warme pool, interne distinct_ids (30 dagen, 8 ids), pageviews en autocapture met elements chain voor de 10 sessies van gisteren (twee queries, de eerste kapte af op 100 rijen), Register-, ticket- en betaalkliks over de externe sessies van 13 t/m 20 september, rage en dead clicks, persoonshistorie van de 9 distinct_ids van gisteren, profielkenmerken (/my, login, confirmation, tools, blog, wholesaler-events) voor 7 personen, hun overige sessies van 18 t/m 20 september, en de wholesaler-formulierevents van 18 t/m 20 september. Vijftien queries, alle onder 3 seconden. Periode gisteren = 20 september 2026 UTC, 7d = 13 t/m 19 september 2026 (extern, zonder intern verkeer en zonder bots). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt, geen weekoverzicht geschreven (output beperkt tot de daily-map).

**Herverificatie (tweede run, 21 september 2026, ca. 13:30 UTC):** het rapport bestond al volledig bij de start van deze run en is niet opnieuw opgebouwd. Kerncijfers opnieuw gecontroleerd met drie PostHog sessions-queries (samen 5,7 seconden) en één Pipeboard-testcall (1,7 seconden), alle vier via de directe routes omdat beide MCP-servers ook nu niet verbonden: SYBB sessies 20 september 10 (waarvan 2 tab-sluitingen met 0 pageviews, 8 externe personen, 1 via chatgpt.com), landing page startyourballoonbusiness.com 13 t/m 20 september 0 sessies, site-breed 20 september 1.457 sessies en 3.903 pageviews met 0 Meta-UTM, 0 sybb-UTM, 0 social referrals en 12 ChatGPT-sessies, Meta campaign-level insights voor 20 september `data: []`. Alle cijfers identiek aan het rapport hierboven. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
