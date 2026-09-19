# SYBB Daily Report: 18 september 2026

## 1. Samenvatting
Vrijdag 18 september leverde de eerste betaalde SYBB-inschrijving sinds 9 september, en meteen de grootste tot nu toe: een Nederlandse bezoeker landde om 22:45 lokale tijd rechtstreeks op de Nederlandse registratiepagina van professional-9, klikte binnen 6 seconden op Registreer, vulde twee deelnemers in (naam, bedrijf, e-mail, telefoon), ging naar de betaling, koos "Kaart" en rondde na 17 minuten af op /shop/confirmation. Geen referrer, geen UTM, eerste bezoek ooit: de link kwam uit een mail, app of chat, niet uit een advertentie. Daarnaast waren er 4 andere echte bezoekers (Nederland, België, Verenigd Koninkrijk) met samen 5 SYBB-pageviews, gemiddeld 11 minuten op de site, nul bounces. Eén van hen, een Google-bezoeker op iPhone, bleef 13 minuten op professional-7 en klikte alleen op het adres in Google Maps (Genk). De 5 andere sessies waren bot-achtige hits uit Mexico, Brazilië, Costa Rica, Colombia en Egypte (1 pageview, 0 kliks, 1 tot 8 seconden). Intern verkeer: nul. De Meta campagne `2026: SYBB` staat op PAUSED (152 dagen), nul betaald verkeer, de landing page startyourballoonbusiness.com staat voor de eenentwintigste dag op 0 bezoekers, en session replay leverde voor de dertiende dag nul opnames. Pipeboard zat op de weeklimiet; alle Meta-cijfers komen uit het extract van 16 september.

## 2. Meta Ads Performance

**Status data:** niet live. De eerste en enige directe Pipeboard-call (campaign-level, 19 augustus t/m 18 september) kreeg `weekly_limit_exceeded`: 30 van 30 executies gebruikt, plan free, resetdatum 21 september 2026 00:00 UTC. Geen verdere Meta-calls gedaan. Campagnestatus en 30d-cijfers overgenomen uit het live extract van 16 september; het ads-rapport van vanochtend bevestigde via PostHog dat het 30d-venster dezelfde (lege) levering bevat.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026 (152 dagen). Alle 7 campagnes in ad account `act_567892422940728` zijn gepauzeerd, de twee Wholesaler Campagnes sinds 4 september. Geen levering, geen spend, op geen enkele campagne.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: op 18 september kwam site-breed (1.654 sessies, 4.136 pageviews) geen enkele sessie binnen met `utm_source` meta, facebook of instagram of met `utm_campaign=sybb`. Er waren 2 organische referrals vanaf facebook.com zonder UTM, geen van beide op een SYBB pagina.

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

Toelichting: ⚪ = geen data. Eenentwintigste dag op rij zonder één sessie op dit domein (sinds 29 augustus, gecontroleerd via de sessions-tabel over 11 t/m 18 september). Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

Interne sessies (9 distinct_ids met pageviews op `edit_translations` of `/odoo` in de laatste 30 dagen) zijn uit alle cijfers gefilterd, ook uit het 7d-gemiddelde. Bot-achtige hits (1 pageview, 0 kliks, 0 tot 8 seconden, hooguit 2 events in de hele projecthistorie) tel ik apart.

| Metric | Gisteren (18 sep) | 7d Gemiddelde (11 t/m 17 sep, extern) | Trend |
|--------|-------------------|---------------------------------------|-------|
| Sessies (sessions-tabel) | 11 | 6,7 (47 totaal) | ↑ |
| Waarvan tab-sluiting zonder pageview | 1 | 1 in 7 dagen | |
| Waarvan intern | 0 | 6 in 7 dagen (uitgefilterd) | |
| Waarvan bot of link-preview | 5 | 16 in 7 dagen (2,3 per dag) | ↑ |
| Echte externe sessies | 5 | 3,4 (24 totaal) | ↑ |
| Externe personen | 5 | 23 in 7 dagen | ↑ |
| Pageviews SYBB pagina's | 11 (6 echt, 5 bot) | n.v.t. | |
| Sessieduur, echte externe sessies | gemiddeld 671s, mediaan 787s | gemiddeld 812s, mediaan 245s | → |
| Pageviews per echte sessie | 13,0 | 17,6 | ↓ |
| Bounce rate (sessions-tabel, sessies met pageview) | 50% (5 van 10, alle vijf bots) | 39% (18 van 46) | ↑ |
| Bounce rate, echte externe sessies | 0% (0 van 5) | 4% (1 van 24) | → |
| Bezoeken van 5 seconden of korter (echt) | 0 van 5 | 2 van 24 | |
| Klik op "Registreer" of "Register" | 1 | 1 in 7 dagen (12 sep) | ↑ |
| Ticket bevestigd | 1 | 1 in 7 dagen | ↑ |
| "Ga naar de betaling" | 1 | 0 | ↑ |
| Betaald workshopticket | **1 sessie, 2 deelnemers** | 0 | ↑ |
| /shop/confirmation zonder ticket | 0 | 2 (14 en 16 sep, webshoporders) | |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers | Aard |
|--------|-----------|-----------|------|
| /event/start-your-balloon-business-professional-9/register (NL) | 1 | 1 | **betaald, 2 tickets** |
| /event/start-your-balloon-business-professional-7/register (NL) | 2 | 2 | echte bezoekers (BE desktop, NL iPhone) |
| /en_GB/event/start-your-balloon-business-professional-7/register | 2 | 2 | echte bezoekers (GB Android, NL iPhone via Google) |
| /en_GB/event/start-your-balloon-business-professional-8/register | 1 | 1 | echte bezoeker (GB Android) |
| /en_GB/event/start-your-balloon-business-professional-9/register | 2 | 2 | bot-hits 05:32 en 05:33 lokale tijd (MX, BR) |
| /fr/event/start-your-balloon-business-professional-48/register | 1 | 1 | bot-hit 09:34 (CO) |
| /fr/event/start-your-balloon-business-professionnel-anglais-2/register | 1 | 1 | bot-hit 10:23 (EG) |
| /de/shop/05102026-start-your-balloon-business-professional-05-06102026-5290 | 1 | 1 | bot-hit 08:03 (CR), webshop-product van 5 en 6 oktober |

De vijf echte sessies van gisteren (tijden lokaal, UTC +2):

| Tijd | Herkomst | Land / device | Pad | Wat gebeurde er |
|------|----------|---------------|-----|-----------------|
| 12:36 tot 12:40 | Direct | GB, Chrome, Android | Home → knop "See the workshops" → /events → professional-7 (50s) → /events → professional-8 (21s) → home → latex shop → /become-a-distributor → latex shop | Vergelijker met groothandelsinteresse. Opende twee SYBB data na elkaar, klikte nergens op Register en ging door naar de distributeurspagina. |
| 14:46 tot 15:03 | Direct, ingelogd | BE, Edge desktop, Windows, terugkerende klant sinds 21 juli (12 sessies) | Home → login → /my → shop (toebehoren, afgeprijsd, folie cijfers) → blog "How to become a balloon artist" (4 min) → blog "How to start a balloon business" (3 min) → blog garland → /events → professional-7 (exit) | Bestaande klant die via twee starter-blogs bij SYBB uitkomt en daar de sessie beëindigt. Geen klik op Registreer. De blogs werken als brug naar de workshop. |
| 18:45 tot 18:58 (tab gesloten 21:14) | Google | NL, Mobile Safari, iPhone | /en_GB/event → pagina 2 → professional-7 (13 minuten) → klik op het adres (Google Maps, Miënbroekstraat 43, Genk) | De langste leestijd van de dag op één SYBB pagina. De enige klik was op de locatie: deze bezoeker checkt de reisafstand. Geen klik op Register. |
| 22:45 tot 23:02 | Direct, eerste bezoek ooit | NL, Safari, nl-NL, schermbreedte 834px (vermoedelijk iPad) | professional-9 (NL) → Registreer (na 6s) → aantal +1 → ticket bevestigd (a-submit) → deelnemer 1 en 2: naam, bedrijf, e-mail, telefoon → "Ga naar de betaling" → /shop/payment → "Kaart" → betalen (22:48) → /payment/status (13 minuten) → /shop/confirmation (23:02) | **Betaalde SYBB-inschrijving, 2 deelnemers, met bedrijfsnaam.** Komt zonder referrer of UTM rechtstreeks op de NL registratiepagina binnen: een gedeelde link uit mail, WhatsApp of een app. Voldoet aan de strikte betaaldefinitie (submit in `#modal_ticket_registration`, "Ga naar de betaling", confirmation). |
| 00:00 tot 00:05 (19 sep lokaal) | Direct, ingelogd | NL, Mobile Safari, iPhone | Home → login → /my → /events → professional-7 (7s) → Falcone-tour → Nozzle Up 2027 spaarplan → France masterclass → Falcone-tour → shop (displays, frames) | Ingelogde klant die de hele kalender doorloopt. SYBB kreeg 7 seconden, de Falcone-tour twee keer. Geen klik op Registreer. |

De vijf bot-hits hebben een ander profiel dan de link-previews van 15 t/m 17 september: elk precies 2 events ($pageview plus $web_vitals, dus JavaScript draaide), geen $pageleave, geen kliks, 1 tot 8 seconden, desktop Firefox of Chrome, alle vijf "direct", verspreid over vijf uur en vier verschillende SYBB-URL's inclusief het Duitse webshop-product. Dat wijst op een crawler met headless browser die de sitemap afloopt, niet op iemand die een link deelt. Site-breed waren 262 van de 1.654 sessies (16%) van dit type.

Drie observaties:

- **De koper kwam niet via de kalender maar via een directe link.** Alle vier de niet-kopers gisteren kwamen via /events of Google en vergeleken; de koper landde rechtstreeks op de NL registratiepagina, wist wat ze wilde en had binnen 2 minuten twee deelnemers ingevuld. Dat is hetzelfde patroon als de betaling van 9 september (ingelogd, doelgericht). De registratiepagina converteert prima zodra iemand met intentie binnenkomt; het lek zit bij de aanvoer en bij de vergelijkers op de kalender.
- **Dertien minuten in /payment/status.** Van "betalen" (22:48:19) tot de bevestiging (23:02:31) zat de koper 13 minuten op de statuspagina. Bij de betaling van 9 september (Bancontact) ging dat sneller. Kaartbetaling met 3D Secure kan dit verklaren, maar het is ook het moment waarop een minder vastberaden koper afhaakt. Even nakijken bij de payment provider of de status-polling van Odoo hier traag was.
- **Locatie is een vraag.** De Google-bezoeker las 13 minuten en klikte alleen op het adres. De GB-bezoeker opende twee data en ging weg. Op de registratiepagina staat het adres als kale Maps-link; er staat niets over parkeren, reistijd vanuit Nederland of Duitsland, of overnachten.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte externe bezoekers:
SYBB registratiepagina bekeken (5 sessies, 100%) → klik op "Registreer" (1, 20%) → ticket bevestigd (1, 100% van de starters) → "Ga naar de betaling" (1, 100%) → betaald workshopticket (1 sessie, 2 deelnemers, 100%)

Event funnel, 11 t/m 17 september (7 dagen, extern, zonder intern verkeer en zonder bots):
SYBB registratiepagina bekeken (24 echte sessies, 100%) → klik op "Registreer" of "Register" (1 sessie, 4%) → ticket bevestigd (1, 100% van de starters) → "Go to Payment" (0) → betaald (0)

Inschrijfpogingen per dag:

| Dag | Echte externe sessies | Klik "Registreer" (sessies) | Ticket bevestigd | "Ga naar de betaling" | Betaald | Uitkomst |
|-----|-----------------------|------------------------------|------------------|-----------------------|---------|----------|
| 11 sep | 0 | 0 | 0 | 0 | 0 | 2 bot-hits, 1 tab-sluiting |
| 12 sep | 6 | 1 (Mobile Safari, en_GB professional-8) | 1 | 0 | 0 | ticketvenster binnen 4 seconden gesloten |
| 13 sep | 6 | 0 | 0 | 0 | 0 | 1 bezoeker klikte wel op Register, maar bij de France Christmas masterclass |
| 14 sep | 6 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket, 2 bounces van 5s |
| 15 sep | 1 | 0 | 0 | 0 | 0 | 1 vergelijker, 3 link-previews |
| 16 sep | 3 | 0 | 0 | 0 | 0 | 1 webshoporder zonder ticket (77 pageviews), 6 bot-hits |
| 17 sep | 2 | 0 | 0 | 0 | 0 | 2 lange leessessies (84 en 8 minuten), 3 bot-hits |
| 18 sep | 5 | 1 (Safari, NL professional-9) | 1 | 1 | **1 (2 deelnemers)** | **betaald met kaart, 17 minuten van landing tot bevestiging** |

**Grootste lek:** nog altijd de stap van "pagina bekeken" naar "klik op Registreer": 1 van 24 in de week ervoor, 1 van 5 gisteren. Wie klikt, komt sinds 12 september ook door: de twee starters van 12 en 18 september bevestigden allebei het ticket, en de starter van gisteren betaalde. Van de 4 niet-kopers gisteren waren er 3 vergelijkers via /events (SYBB kreeg 7, 21, 50 en 50 seconden) en 1 lezer die de locatie checkte. Het deelnemersvenster, dat vorige week 3 van 4 starters kostte, was gisteren geen probleem: twee deelnemers in 1 minuut 50 ingevuld.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echt extern | Betaald workshopticket | /shop/confirmation zonder ticket | Eindigde op SYBB pagina |
|---------|--------------|-------------|------------------------|----------------------------------|-------------------------|
| Gisteren | 11 | 5 | 1 (2 deelnemers) | 0 | 6 (5 bots, 1 BE klant na de blogs) |
| 11 t/m 17 sep | 47 | 24 | 0 | 2 | n.v.t. |

Warme pool (laatste 30 dagen, 19 augustus t/m 18 september): 155 personen in 173 sessies bekeken een SYBB registratiepagina (345 pageviews). Daar zitten 9 interne distinct_ids en zeker 26 bot- of preview-hits in (5 gisteren, 16 vorige week, 5 eerder), dus reken op circa 120 echte personen als retargeting-doelgroep bij herstart, waarvan er nu 2 betaald hebben.

## 5. Rode Vlaggen 🚩

- **De enige conversie van de maand is niet terug te kijken.** Session replay leverde 10 t/m 18 september nul opnames (dertiende dag). De betaalde sessie van gisteren, inclusief de 13 minuten op /payment/status, staat alleen als event-reeks in PostHog.
- **Dertien minuten tussen betalen en bevestiging.** 22:48:19 klik op betalen, 22:49:12 /payment/status, 23:02:31 /shop/confirmation. Als dit de wachttijd van de provider of van Odoo's status-polling is, verliest een twijfelende koper hier zijn ticket.
- **Klikratio op Registreer blijft onder 5% over de week.** 1 van 24 echte bezoekers in 11 t/m 17 september, gisteren 1 van 5. Vergelijkers via /events geven SYBB structureel de minste tijd (gisteren 7 tot 50 seconden tegen minuten op de Falcone-tour).
- **Nieuwe crawlergolf op de SYBB-URL's.** 5 bot-hits gisteren uit MX, BR, CR, CO en EG met een headless-browser profiel ($web_vitals zonder $pageleave), na 16 preview- en bot-hits vorige week. Ze vervuilen de bounce rate van de sessions-tabel (50% gisteren, 0% bij echte bezoekers).
- **Pipeboard weeklimiet dicht tot maandag 21 september.** Eerste call van deze run faalde direct (30 van 30). Alle Meta-cijfers komen uit het extract van 16 september; bij een stilstaande campagne is dat geen informatieverlies, maar bij herstart wel.
- **Structureel, ongewijzigd:** SYBB campagne 152 dagen gepauzeerd, landing page 21 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer.

Niet rood: intern verkeer (0 sessies gisteren), rage en dead clicks op SYBB pagina's (0), CPC en frequency (geen levering), vals-positieve conversies (0 gisteren, de confirmation van gisteren is een echt ticket).

## 6. Top 3 Acties voor Vandaag

1. **Controleer de inschrijving van gisteravond in Odoo en vraag de koper waar de link vandaan kwam.** Wat: open in Odoo Evenementen de registraties van "Start Your Balloon Business Professional" (event 9, Nederlandse pagina) van 18 september rond 23:00 en check dat de kaartbetaling van 22:48 is verwerkt en dat beide deelnemers een bevestiging hebben gekregen. Stuur vandaag nog een persoonlijk welkomstbericht met één vraag: "Hoe kwam je bij deze pagina terecht?" Noteer het antwoord in `Kennis/Voorgaande campagnes/campagne-historie.md` onder SYBB. Waarom: dit is de tweede betaling van de maand en de eerste met twee deelnemers; de bron is onbekend (direct, geen UTM) en dat is precies het kanaal dat zonder ads nog werkt. Hoe: handmatig, 15 minuten. Verwachte impact: één bevestigde aanvoerbron voor SYBB buiten Meta, en zekerheid dat de 13 minuten op /payment/status geen half verwerkte betaling verbergt. Escalatie: Groen.
2. **Zet session replay aan en test tegelijk de betaalstap op een kaartbetaling.** Wat: open https://eu.posthog.com/project/149694/settings/environment-replay en zet "Record user sessions" aan met 100% sampling en minimaal 30 dagen retentie; check of er een URL-filter of minimale duur staat die sempertexeurope.com uitsluit. Doorloop daarna zelf op een iPad of iPhone in een privévenster https://www.sempertexeurope.com/event/start-your-balloon-business-professional-9/register tot en met /shop/payment, kies "Kaart" en noteer hoe lang /payment/status duurt voordat de bevestiging verschijnt (afbreken vóór de daadwerkelijke afschrijving als testbetalingen niet mogelijk zijn). Waarom: dertien dagen nul opnames, en de enige conversie van de maand had 13 minuten wachttijd die niemand kan terugkijken. Hoe: handmatig, 20 minuten. Verwachte impact: de eerstvolgende inschrijfpoging is terugkijkbaar, en je weet of de wachttijd bij de provider zit (Rood: escaleren naar de payment provider) of bij Odoo (Oranje). Escalatie: Geel voor de replay-instellingen, Oranje als de betaalstap aangepast moet worden.
3. **Zet een blok "Locatie en reizen" boven de Registreer-knop en link vanuit de twee starter-blogs rechtstreeks naar SYBB.** Wat: op elke SYBB registratiepagina (NL, EN, DE, FR) direct onder de datum een kort blok met: adres Miënbroekstraat 43, Genk, gratis parkeren ja of nee, reistijd vanuit Eindhoven, Antwerpen, Aken en Maastricht, en een zin over overnachten. In de blogs "How to become a balloon artist" en "How to start a balloon business" (NL en EN) een vaste call-to-action naar de eerstvolgende SYBB datum in plaats van naar /events. Waarom: gisteren was de enige klik van de langste lezer het adres in Google Maps, en de BE-klant kwam via die twee blogs bij SYBB uit maar strandde op de pagina. Vorige week gebeurde hetzelfde bij de vergelijkers. Hoe: Odoo website-editor, tekstblok kopiëren naar de vier taalversies, 45 minuten. Verwachte impact: minder afhakers die de reis niet kunnen inschatten, en een directe route van blog naar registratie in plaats van via de kalender waar SYBB de vergelijking verliest. Escalatie: Geel (Robin keurt tekst goed).

Blijft open uit eerdere rapporten: SYBB een eigen blok bovenaan /events geven in plaats van een kaart tussen de rest (actie 2 van 15 september, gisteren opnieuw 3 vergelijkers), bepalen of het webshop-product van 5 en 6 oktober (id 5290) naast de event-registratie het canonieke verkoopkanaal is (gisteren kreeg het één bot-hit, geen echte bezoeker), de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`), het interne cohort in de PostHog projectinstellingen markeren, één gedeelde en gecachte Meta-call per dag voor de drie rapporten, en het aanpassen van de funneldefinitie in `skills/daily-sybb-report/SKILL.md` van landing page naar event funnel.

---

**Databronnen:** Meta Ads via Pipeboard (MCP-servers `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads` vroegen om autorisatie, niet mogelijk in deze non-interactieve sessie; de directe JSON-RPC route kreeg op de eerste call `weekly_limit_exceeded` 30/30 met resetdatum 21 september 2026; campagnestatus en 30d-cijfers overgenomen uit het extract van 16 september, bevestigd via het ads-rapport van 19 september 08:00). PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): sessions-tabel per dag en per sessie voor 11 t/m 18 september, pageviews en autocapture met elements chain per sessie, volledige event-timeline van de betaalde sessie, persoonshistorie van alle tien distinct_ids van gisteren, lijst interne distinct_ids (30 dagen), rage en dead clicks, session replay events, site-brede entry-source en bot-telling via de sessions-tabel (een pageview-query op de events-tabel over 8 dagen liep op de maximale uitvoertijd). Periode gisteren = 18 september 2026 UTC, 7d = 11 t/m 17 september 2026 (extern, zonder intern verkeer en zonder bots). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
