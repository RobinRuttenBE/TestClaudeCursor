# SYBB Daily Report: 19 september 2026

## 1. Samenvatting
Zaterdag 19 september was een stille dag zonder inschrijfpoging. Drie echte bezoeken van twee personen op de SYBB registratiepagina's, nul kliks op Registreer, nul betalingen. De interessantste bezoeker is een nieuwe Nederlandse desktopgebruiker die 's middags via Google op /events binnenkwam, drie SYBB data na elkaar opende (professional-47, 8 en 9) en vijf minuten op de Engelse pagina van professional-9 bleef zonder te klikken. Vierenhalf uur later kwam dezelfde persoon terug, bekeek de Falcone-tour en het Nozzle Up spaarplan, zette de site op Nederlands en klikte op de kalender op "Genk" bij SYBB, waarna nog 51 seconden op de Nederlandse pagina van professional-9 volgden. Twee keer op één dag terug, en opnieuw is de locatie het element waarop geklikt wordt. De andere echte bezoeker was een bestaande Belgische klant (Frans, iPhone, ingelogd) die de Franse workshopkalender doorliep, SYBB 10 seconden gaf en daarna een eigen order bekeek. Daarnaast twee link-preview hits (Japan en Duitsland, elk precies 1 event in de hele projecthistorie), waarvan één op een pagina die nog nooit eerder in de data voorkwam: /en_GB/start-your-balloon-business-3. Intern verkeer: nul. De Meta campagne `2026: SYBB` staat op PAUSED (153 dagen), nul betaald verkeer, de landing page startyourballoonbusiness.com staat voor de tweeëntwintigste dag op 0 bezoekers, en session replay leverde voor de veertiende dag nul opnames. Pipeboard zat op de weeklimiet; alle Meta-cijfers komen uit het extract van 16 september.

## 2. Meta Ads Performance

**Status data:** niet live. De eerste en enige directe Pipeboard-call (campaign-level, 20 augustus t/m 19 september) kreeg `weekly_limit_exceeded`: 30 van 30 executies gebruikt, plan free, resetdatum 21 september 2026 00:00 UTC. Geen verdere Meta-calls gedaan. Campagnestatus en 30d-cijfers overgenomen uit het live extract van 16 september; het ads-rapport van vanochtend bevestigde via PostHog dat het 30d-venster dezelfde (lege) levering bevat.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026 (153 dagen). Alle 7 campagnes in ad account `act_567892422940728` zijn gepauzeerd, de twee Wholesaler Campagnes sinds 4 september. Geen levering, geen spend, op geen enkele campagne.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: op 19 september kwam site-breed (2.681 sessies, 5.056 pageviews) geen enkele sessie binnen met `utm_source` meta, facebook of instagram of met `utm_campaign=sybb`, en er was ook geen enkele organische referral vanaf facebook.com of instagram.com. Over 12 t/m 19 september samen: 0 betaalde sessies, 9 organische social referrals, geen daarvan op een SYBB pagina.

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

Toelichting: ⚪ = geen data. Tweeëntwintigste dag op rij zonder één sessie op dit domein (sinds 29 augustus, gecontroleerd via de sessions-tabel over 12 t/m 19 september). Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

Interne sessies (7 distinct_ids met pageviews op `edit_translations` of `/odoo` in de laatste 30 dagen) zijn uit alle cijfers gefilterd, ook uit het 7d-gemiddelde. Bot- en link-preview hits (1 pageview, 0 kliks, 0 tot 8 seconden) tel ik apart.

| Metric | Gisteren (19 sep) | 7d Gemiddelde (12 t/m 18 sep, extern) | Trend |
|--------|-------------------|---------------------------------------|-------|
| Sessies (sessions-tabel) | 5 | 7,9 (55 totaal) | ↓ |
| Waarvan tab-sluiting zonder pageview | 0 | 1 in 7 dagen | |
| Waarvan intern | 0 | 6 in 7 dagen (uitgefilterd) | |
| Waarvan bot of link-preview | 2 | 20 in 7 dagen (2,9 per dag) | ↓ |
| Echte externe sessies | 3 | 4,0 (28 totaal) | ↓ |
| Externe personen | 2 | 27 in 7 dagen | ↓ |
| Pageviews SYBB pagina's | 7 (5 echt, 2 bot) | n.v.t. | |
| Sessieduur, echte externe sessies | gemiddeld 302s, mediaan 309s | gemiddeld 816s, mediaan 310s | mediaan → |
| Pageviews per echte sessie | 8,3 | 17,4 (mediaan 5,5) | ↓ |
| Bounce rate (sessions-tabel) | 40% (2 van 5, beide bots) | 36% (20 van 55) | → |
| Bounce rate, echte externe sessies | 0% (0 van 3) | 0% (0 van 28) | → |
| Bezoeken van 5 seconden of korter (echt) | 0 van 3 | 1 van 28 | |
| Klik op "Registreer" of "Register" bij SYBB | 0 | 2 in 7 dagen (12 en 18 sep) | ↓ |
| Ticket bevestigd | 0 | 2 in 7 dagen | ↓ |
| "Ga naar de betaling" | 0 | 1 in 7 dagen | ↓ |
| Betaald workshopticket | 0 | 1 sessie, 2 deelnemers (18 sep) | ↓ |
| /shop/confirmation zonder ticket | 0 | 2 (14 en 16 sep, webshoporders) | |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers | Aard |
|--------|-----------|-----------|------|
| /en_GB/event/start-your-balloon-business-professional-9/register | 1 | 1 | echte bezoeker (NL desktop via Google), 5 minuten, geen klik |
| /event/start-your-balloon-business-professional-9/register (NL) | 1 | 1 | dezelfde NL bezoeker, tweede sessie, 51 seconden |
| /en_GB/event/start-your-balloon-business-professional-47/register | 1 | 1 | NL bezoeker, 38 seconden |
| /en_GB/event/start-your-balloon-business-professional-8/register | 1 | 1 | NL bezoeker, 5 seconden |
| /fr/event/start-your-balloon-business-professionnel-8/register | 1 | 1 | echte bezoeker (BE klant, iPhone), 10 seconden |
| /en_GB/start-your-balloon-business-3 | 1 | 1 | link-preview 06:06 lokale tijd (JP, Chrome iOS), pagina nooit eerder gezien in 30 dagen |
| /en_GB/shop/05102026-start-your-balloon-business-professional-05-06102026-5290 | 1 | 1 | link-preview 21:04 (DE, Chrome desktop), webshop-product van 5 en 6 oktober |

De drie echte sessies van gisteren (tijden lokaal, UTC +2):

| Tijd | Herkomst | Land / device | Pad | Wat gebeurde er |
|------|----------|---------------|-----|-----------------|
| 12:46 tot 12:53 | Google | NL, Chrome desktop, Windows, nl-NL, eerste bezoek ooit | /en_GB/events → professional-47 (38s) → /events → professional-8 (5s) → /events → professional-9 (5 min 11s, einde sessie) | Vergelijkt de drie SYBB data op de Engelse kalender en blijft op professional-9 hangen. Geen klik op Register, geen scroll-signaal beschikbaar. |
| 17:17 tot 17:23 | Terugkeer (referrer sempertexeurope.com) | Dezelfde NL persoon | /en_GB/events → Falcone-tour (15s) → /events → Nozzle Up 2027 spaarplan (2 min 54s) → /events → filter "Schedule" geopend → taal naar Nederlands (BE) → /events → klik op "Genk" bij SYBB → NL professional-9 (51s, einde sessie) | Komt 4,5 uur later terug, kijkt nu breder (Falcone, spaarplan), zet de site op Nederlands en gaat via de locatielink terug naar SYBB professional-9. Geen klik op Registreer. Twee bezoeken op één dag aan dezelfde SYBB datum is het warmste signaal van de dag. |
| 19:43 tot 19:46 | Direct, ingelogd | BE, Mobile Safari, iPhone, fr-FR, klant sinds 22 augustus (12 logins) | /fr → "Voir les workshops" → Balloon Twist Masterclass France (17s) → SYBB professionnel-8 (10s) → Examen MBP (1 min) → Nozzle Up spaarplan (8s) → /fr → account → orders → order S05396 | Bestaande Franstalige klant die de kalender scant en dan een eigen order opzoekt. SYBB kreeg 10 seconden, het MBP-examen een minuut. |

De twee bot-hits hebben het link-preview profiel: precies 1 event in de hele projecthistorie ($pageview zonder $web_vitals of $pageleave), 0 seconden, 0 kliks. Site-breed was gisteren 88% van de sessies van het type "1 pageview, 0 kliks, hooguit 8 seconden" (2.364 van 2.681); dat is een bredere definitie dan de "precies 2 events" crawler van 18 september, dus niet één op één vergelijkbaar met de 262 van dat rapport. Over 12 t/m 19 september schommelt dat aandeel tussen 10% (14 september) en 90% (12 september), dus de sessions-tabel is site-breed onbruikbaar als bezoekersteller zonder deze filter.

Drie observaties:

- **Locatie is opnieuw het klikdoel.** Op 18 september klikte de langste lezer alleen op het adres in Google Maps; gisteren gebruikte de NL bezoeker de plaatsnaam "Genk" op de kalenderkaart als ingang naar de registratiepagina. Twee dagen op rij is de locatie het enige interactieve element dat SYBB-bezoekers aanraken. Actie 3 van gisteren (blok "Locatie en reizen" boven de Registreer-knop) wordt hiermee sterker.
- **Een twee-keer-terug bezoeker zonder vangnet.** De NL persoon bekeek in twee sessies vier SYBB pagina's, 6 minuten in totaal op professional-9, en wisselde bewust naar Nederlands. Er is geen ad-retargeting (campagne PAUSED), geen e-mailadres (geen opt-in op de pagina) en geen replay om te zien waar de blik bleef hangen. Bij een werkende funnel was dit de bezoeker die een "nog twijfels? bel ons" of een brochure-download had moeten krijgen.
- **Onbekende pagina /en_GB/start-your-balloon-business-3.** Deze URL zonder /event/ verscheen gisteren voor het eerst in 30 dagen, via een link-preview uit Japan om 06:06. Het is een Odoo websitepagina (het achtervoegsel -3 is het paginanummer), geen event. Als dit een concept-landingspagina op de hoofdsite is, hoort hij niet gedeeld te worden; als hij gepubliceerd is, hoort hij in de funnel-meting.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte externe bezoekers:
SYBB registratiepagina bekeken (3 sessies, 100%) → klik op "Registreer" (0, 0%) → ticket bevestigd (0) → "Ga naar de betaling" (0) → betaald workshopticket (0)

Event funnel, 12 t/m 18 september (7 dagen, extern, zonder intern verkeer en zonder bots):
SYBB registratiepagina bekeken (28 echte sessies, 100%) → klik op "Registreer" of "Register" bij SYBB (2 sessies, 7%) → ticket bevestigd (2, 100% van de starters) → "Ga naar de betaling" (1, 50%) → betaald (1 sessie, 2 deelnemers, 100% van de betaalstarters)

Inschrijfpogingen per dag:

| Dag | Echte externe sessies | Klik "Registreer" bij SYBB (sessies) | Ticket bevestigd | "Ga naar de betaling" | Betaald | Uitkomst |
|-----|-----------------------|--------------------------------------|------------------|-----------------------|---------|----------|
| 12 sep | 6 | 1 | 1 | 0 | 0 | ticketvenster binnen 4 seconden gesloten, 2 bots |
| 13 sep | 6 | 0 | 0 | 0 | 0 | 1 bezoeker klikte 5 keer op Register, maar bij de France Christmas masterclass |
| 14 sep | 5 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket, 2 interne sessies, 1 bot |
| 15 sep | 1 | 0 | 0 | 0 | 0 | 1 vergelijker, 3 link-previews |
| 16 sep | 3 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket (77 pageviews), 6 bots, 2 intern |
| 17 sep | 2 | 0 | 0 | 0 | 0 | 2 lange leessessies, 3 bots, 2 intern |
| 18 sep | 5 | 1 | 1 | 1 | **1 (2 deelnemers)** | betaald met kaart, 17 minuten van landing tot bevestiging |
| 19 sep | 3 | 0 | 0 | 0 | 0 | 1 NL vergelijker twee keer terug, 1 BE klant, 2 link-previews |

**Grootste lek:** ongewijzigd de stap van "pagina bekeken" naar "klik op Registreer": 2 van 28 in de week ervoor, 0 van 3 gisteren. Wie klikt, komt sinds 12 september door: beide starters bevestigden het ticket en de starter van 18 september betaalde. Gisteren kwamen beide echte bezoekers via de kalender (/events) binnen en vergeleken, precies het profiel dat de afgelopen twee weken nooit klikt. Beide betalers van deze maand (9 en 18 september) landden juist rechtstreeks op de registratiepagina.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echt extern | Betaald workshopticket | /shop/confirmation zonder ticket | Eindigde op SYBB pagina |
|---------|--------------|-------------|------------------------|----------------------------------|-------------------------|
| Gisteren | 5 | 3 | 0 | 0 | 4 (2 bots, 2 keer de NL bezoeker op professional-9) |
| 12 t/m 18 sep | 55 | 28 | 1 (2 deelnemers) | 2 | n.v.t. |

Warme pool (laatste 30 dagen, 20 augustus t/m 19 september): 158 personen in 187 sessies bekeken een SYBB registratiepagina. Daar zitten 7 interne distinct_ids en minstens 27 bot- of preview-hits in (2 gisteren, 20 vorige week, 5 eerder), dus reken op circa 120 echte personen als retargeting-doelgroep bij herstart, waarvan er nu 2 betaald hebben. Vijf van de 187 sessies eindigden op /shop/confirmation: 2 echte tickets (9 en 18 september) en 3 webshoporders.

## 5. Rode Vlaggen 🚩

- **Nul inschrijfpogingen bij 3 echte bezoeken, en de warmste bezoeker van de dag is onbereikbaar.** De NL desktopgebruiker kwam twee keer terug op professional-9 en heeft geen enkel vangnet gehad: geen retargeting, geen e-mail, geen brochure, geen chat. Elke dag zonder opt-in op de registratiepagina lekt dit soort bezoekers weg.
- **Locatie is twee dagen op rij het enige klikdoel.** Gisteren "Genk" op de kalenderkaart, eergisteren het adres in Google Maps. Op de registratiepagina staat niets over parkeren, reistijd of overnachten.
- **Onbekende pagina /en_GB/start-your-balloon-business-3 in de data.** Eerste vertoning ooit, via een link-preview uit Japan. Onduidelijk of dit een gepubliceerde pagina is.
- **Session replay veertiende dag op nul.** 12 t/m 19 september nul opnames in `session_replay_events`. Ook de dubbele sessie van gisteren is niet terug te kijken.
- **Pipeboard weeklimiet dicht tot maandag 21 september.** Eerste call van deze run faalde direct (30 van 30). Alle Meta-cijfers komen uit het extract van 16 september; bij een stilstaande campagne is dat geen informatieverlies.
- **Structureel, ongewijzigd:** SYBB campagne 153 dagen gepauzeerd, landing page 22 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer.

Niet rood: intern verkeer (0 sessies gisteren), rage en dead clicks op SYBB pagina's (0), CPC en frequency (geen levering), vals-positieve conversies (0), bounce rate bij echte bezoekers (0%, zowel gisteren als over 7 dagen). Bots (2 gisteren) lagen onder het weekgemiddelde van 2,9 per dag.

## 6. Top 3 Acties voor Vandaag

1. **Zet vandaag het blok "Locatie en reizen" op de vier SYBB registratiepagina's.** Wat: op elke SYBB registratiepagina (NL, EN, DE, FR) direct onder de datum een kort blok met: adres Miënbroekstraat 43, Genk, of parkeren gratis is, reistijd vanuit Eindhoven, Antwerpen, Aken en Maastricht, en één zin over overnachten in de buurt. Waarom: twee dagen op rij is de locatie het enige element waarop SYBB-bezoekers klikken (gisteren "Genk" op de kalenderkaart, eergisteren het adres in Maps), en de NL bezoeker van gisteren kwam er zelfs twee keer voor terug. Hoe: Odoo website-editor, tekstblok in de vier taalversies plakken, 45 minuten. Verwachte impact: de reisvraag wordt op de pagina beantwoord in plaats van dat de bezoeker naar Google Maps vertrekt en niet terugkomt. Escalatie: Geel (Robin keurt de tekst goed). Dit was actie 3 van 18 september en is nu urgenter.
2. **Zet een e-mail opt-in op de SYBB registratiepagina's voor twijfelaars.** Wat: onder de Registreer-knop een tweede, lichte call-to-action: "Nog niet zeker? Ontvang het programma en de prijs per mail" met alleen een e-mailveld (Odoo formulier of Brevo embed), gekoppeld aan een korte follow-up van drie mails (programma, verhaal van een deelnemer, laatste plaatsen). Waarom: gisteren bekeek één persoon in twee sessies vier SYBB pagina's en 6 minuten professional-9 zonder dat er iets van die interesse bewaard is; in de week ervoor gebeurde dat bij 26 van 28 echte sessies. Zonder ads is dit de enige manier om de warme pool (circa 120 personen in 30 dagen) vast te houden. Hoe: Odoo formulierblok of Brevo formulier op de vier taalversies, follow-up schrijven via /email-write, 2 uur totaal. Verwachte impact: bij 5% opt-in op 28 echte sessies per week zijn dat 1 tot 2 adressen per week, meer dan de huidige 0 en bij herstart van de ads het fundament voor de nurture. Escalatie: Geel voor de opt-in, Oranje voor de formulierplaatsing in de Odoo editor.
3. **Controleer wat /en_GB/start-your-balloon-business-3 is en zet session replay aan.** Wat: open in Odoo Website de paginalijst en zoek "start-your-balloon-business"; check of pagina -3 gepubliceerd is, wat erop staat en of hij bedoeld is als vervanger van startyourballoonbusiness.com. Depubliceer hem als het een concept is, of neem hem op in de meting als hij live hoort te zijn. Zet daarna https://eu.posthog.com/project/149694/settings/environment-replay op "Record user sessions" met 100% sampling en 30 dagen retentie en controleer of er een URL-filter of minimumduur staat die sempertexeurope.com uitsluit. Waarom: een SYBB-pagina buiten de event-funnel is gisteren voor het eerst opgedoken via een gedeelde link, en replay staat veertien dagen op nul terwijl de dubbele sessie van gisteren precies het gedrag is dat je wilt terugkijken. Hoe: handmatig, 20 minuten. Verwachte impact: geen onbedoeld gedeelde conceptpagina, en de eerstvolgende inschrijfpoging is terugkijkbaar. Escalatie: Groen voor de check, Geel voor de replay-instellingen.

Blijft open uit eerdere rapporten: de inschrijving van 18 september in Odoo controleren en de koper vragen waar de link vandaan kwam (actie 1 van gisteren), de betaalstap testen op de wachttijd van 13 minuten op /payment/status (actie 2 van gisteren), SYBB een eigen blok bovenaan /events geven in plaats van een kaart tussen de rest (gisteren opnieuw twee vergelijkers via de kalender), in de starter-blogs rechtstreeks naar de eerstvolgende SYBB datum linken, bepalen of het webshop-product van 5 en 6 oktober (id 5290) naast de event-registratie het canonieke verkoopkanaal is (gisteren één link-preview, geen echte bezoeker), de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`), het interne cohort in de PostHog projectinstellingen markeren, één gedeelde en gecachte Meta-call per dag voor de drie rapporten, en het aanpassen van de funneldefinitie in `skills/daily-sybb-report/SKILL.md` van landing page naar event funnel.

---

**Databronnen:** Meta Ads via Pipeboard (MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` vroegen om autorisatie, niet mogelijk in deze non-interactieve sessie; de directe JSON-RPC route kreeg op de eerste call `weekly_limit_exceeded` 30/30 met resetdatum 21 september 2026 00:00 UTC; campagnestatus en 30d-cijfers overgenomen uit het extract van 16 september, bevestigd via het ads-rapport van 20 september). PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): sessions-tabel per dag en per sessie voor 12 t/m 19 september (SYBB pagina's, landing page, site-breed met entry-source en bot-telling), pageviews en autocapture met elements chain per sessie voor de 5 sessies van gisteren, Register-, ticket- en betaalkliks over de externe sessies van 12 t/m 18 september, persoonshistorie van de vier distinct_ids van gisteren, lijst interne distinct_ids (30 dagen), rage en dead clicks, session replay events, 30d warme pool en de historie van de pagina's professional-47 en start-your-balloon-business-3. Twaalf queries, alle onder 3 seconden. Periode gisteren = 19 september 2026 UTC, 7d = 12 t/m 18 september 2026 (extern, zonder intern verkeer en zonder bots). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
