# SYBB Daily Report: 12 september 2026

## 1. Samenvatting
Gisteren was de drukste SYBB dag van de week op de workshoppagina's: 8 sessies, waarvan 6 van echte mensen (7d gemiddelde 2,7). Daar zat de vijfde inschrijfpoging van de week bij, en die strandde opnieuw op precies dezelfde plek: een Nederlandse bezoeker op mobiel Safari klikte om 06:59 lokale tijd op "Register", bevestigde het ticket en sloot het deelnemersvenster binnen 1 seconde. Vier van de vijf pogingen in zeven dagen eindigen nu bij of direct na de ticketbevestiging; alleen de ingelogde klant van 9 september betaalde. De Meta campagne `2026: SYBB` staat nog steeds op PAUSED (sinds 19 april, 146 dagen), de landing page startyourballoonbusiness.com staat voor de vijftiende dag op 0 bezoekers en er is geen betaald verkeer. Meta-cijfers zijn niet live: Pipeboard zit op de weeklimiet en de resetdatum is opgeschoven naar 21 september. Nieuwe bevinding: session replay is niet "acht dagen op nul", de hele replay-tabel bevat nog maar één opname (29 maart), de opnames van eind augustus zijn verdwenen.

## 2. Meta Ads Performance

**Status data:** niet live. De eerste directe Pipeboard call kreeg `weekly_limit_exceeded` (100 van 30 executies, Free plan). De `reset_date` in het antwoord staat nu op **21 september 2026 00:00 UTC**, een week later dan gisteren gemeld. Cijfers hieronder komen uit het 30d-extract van 11 september (leeg voor 13 augustus t/m 11 september) en de campagnelijst uit het ads-rapport van vanochtend (alle 7 campagnes PAUSED).

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Er liep gisteren geen enkele advertentie in ad account `act_567892422940728`.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: van 5 t/m 12 september kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`, en geen enkele SYBB sessie had Meta als entry source. Social referrals (Facebook en Instagram) gisteren: 0 pageviews, in de 7 dagen ervoor 11 in totaal.

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

Toelichting: ⚪ = geen data. Van 29 augustus t/m 12 september is er op dit domein geen enkel event geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (12 sep) | 7d Gemiddelde (5 t/m 11 sep) | Trend |
|--------|-------------------|------------------------------|-------|
| Sessies (sessions-tabel) | 8 | 4,3 | ↑ |
| Echte sessies (duur >0s) | 6 | 2,7 | ↑ |
| Pageviews SYBB pagina's | 8 | 4,9 | ↑ |
| Bezoekers SYBB pagina's | 8 (2 bot) | 4,0 | ↑ |
| Sessieduur echte sessies | gemiddeld 803s, mediaan 195s | gemiddeld 775s, mediaan 169s | → |
| Bounce rate (alle SYBB sessies) | 25% (2 van 8, beide bot) | 33% (10 van 30) | ↓ |
| Sessies van 0 seconden (bot-patroon) | 2 van 8 | 11 van 30 (37%) | ↓ |
| Klik op "Registreer" of "Register" | 1 | 4 in 7 dagen | ↑ |
| Ticket bevestigd | 1 | 3 in 7 dagen | ↑ |
| "Go to Payment" | 0 | 1 in 7 dagen | → |
| Betaald (/shop/confirmation in SYBB sessie) | 0 | 1 (9 sep) | → |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /event/start-your-balloon-business-professional-7/register | 3 | 3 |
| /event/start-your-balloon-business-professional-9/register | 1 | 1 |
| /en_GB/event/start-your-balloon-business-professional-8/register | 1 | 1 |
| /de/event/start-your-balloon-business-professionell-englisch-2/register | 1 | 1 (bot) |
| /en_GB/event/start-your-balloon-business-professional-47/register | 1 | 1 (bot) |
| /en_GB/shop/05102026-start-your-balloon-business-professional-05-06102026-5290 | 1 | 1 |

De acht sessies van gisteren (tijden UTC, lokale tijd is +2 uur):

| Sessie | Tijd | Herkomst | Land / device | SYBB pagina | Duur | Wat gebeurde er |
|--------|------|----------|---------------|-------------|------|-----------------|
| 1 | 00:06 | Google | BE, Chrome iOS | professional-7 | 471s, 10 pv | Kwam via /events op de registratiepagina, opende het menu, ging naar "Workshops" en browste daarna shopcategorieën (bedrukt latex, toebehoren). Geen klik op Registreer. |
| 2 | 00:09 | Direct | BE, Chrome iOS | professional-7 | 7s | Directe hit op dezelfde pagina, drie minuten na sessie 1, zelfde land en browser. Alleen cookies geaccepteerd. Vermoedelijk dezelfde persoon die de link opnieuw opende (bijvoorbeeld in een andere browsercontext). |
| 3 | 04:59 | Direct | NL, Mobile Safari | en_GB professional-8 | 62s, 2 pv | **Inschrijfpoging.** Cookies geaccepteerd (04:59:20), klik "Register" (04:59:53), ticket bevestigd met de submit-knop in het ticketvenster (04:59:55), sluitknop van het ticketvenster (04:59:58) en één seconde later de sluitknop van het tweede venster, de deelnemerstap (04:59:59). Daarna menu, "Workshops", /en_GB/events, weg om 05:00:20. Nieuwe persoon, geen eerdere events. |
| 4 | 06:16 | Direct | LT, Chrome mobiel | en_GB professional-47 | 0s | 1 pageview, geen pageleave, autocapture of web vitals; persoon heeft in het hele project één event. Link-preview bot. |
| 5 | 10:34 | Direct | NL, Chrome mobiel | professional-7 | 329s, 3 pv | Home, menu, "Workshops", /events, klik op de kaart "Start your balloon business professional 7", daarna 5 minuten en 16 seconden op de registratiepagina zonder één klik. Gelezen en vertrokken. |
| 6 | 21:32 | Direct | IT, Chrome mobiel | de professionell-englisch-2 | 0s | Zelfde bot-patroon als sessie 4, één event ooit. |
| 7 | 23:03 | Direct | DE, Chrome desktop | shop-product SYBB 5 en 6 oktober | 6s, 2 pv | /en_GB naar de **webshop-productpagina** van de workshop van 5 en 6 oktober 2026. Geen add-to-cart, geen pageleave op de productpagina. |
| 8 | 23:29 | Google | RS, Chrome desktop | professional-9 | 3.946s, 88 pv | Uitgebreide shopsessie van 66 minuten (displays, shimmerwalls, Fashion Solid, DIY kits, catalogus 2026) waarin de registratiepagina van professional-9 één keer voorbijkwam. Assortimentsprospect, geen workshoplead. |

Drie observaties:

- **Vijfde afbreker in zeven dagen, en de duidelijkste tot nu toe.** Sessie 3 zag na de ticketbevestiging het deelnemersvenster en sloot het binnen één seconde. Dat is te snel om een formulier te lezen; de bezoeker zag iets waar ze direct van afhaakten (login-eis, prijs, aantal velden, of een venster dat niet in het scherm past). Dit was een gloednieuwe, anonieme bezoeker op mobiel Safari, net als de afbrekers van 8 en 10 september.
- **Er bestaat een tweede verkoopkanaal voor SYBB: een webshop-product.** De productpagina `/en_GB/shop/05102026-start-your-balloon-business-professional-05-06102026-5290` (workshop 5 en 6 oktober 2026) is gisteren voor het eerst sinds 21 augustus bekeken (in 30 dagen: 4 pageviews, 4 bezoekers). Als de workshop zowel via de eventpagina als via de shop te koop is, moet het rapport beide meten en moet duidelijk zijn naar welke van de twee toekomstige ads sturen.
- **Twee mensen lazen de registratiepagina van professional-7 zonder te klikken** (sessies 1 en 5, samen bijna 8 minuten op de pagina). Interesse is er, de pagina zet die niet om in een klik op Registreer.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte bezoekers:
SYBB registratiepagina bekeken (5 sessies, 100%) → klik op "Register" (1, 20%) → ticket bevestigd (1, 100% van de starters) → "Go to Payment" (0) → /shop/confirmation (0)

Event funnel, 5 t/m 11 september (7 dagen):
SYBB registratiepagina bekeken (19 echte sessies, 100%) → klik op "Registreer" of "Register" (4 sessies, 21%) → ticket bevestigd (3, 75% van de starters) → "Go to Payment" (1, 33% van de bevestigers) → /shop/confirmation (1, 100% van de betalers)

Inschrijfpogingen per dag:

| Dag | Klik "Registreer" (sessies) | Ticket bevestigd | Deelnemersvenster gesloten | "Go to Payment" | Betaald | Uitkomst |
|-----|------------------------------|------------------|----------------------------|-----------------|---------|----------|
| 7 sep | 1 (desktop Chrome, professional-8) | 1 | 1 | 0 | 0 | afgebroken na 22s |
| 8 sep | 1 (Mobile Safari, professional-9) | 0 | ticketvenster gesloten | 0 | 0 | afgebroken na 10s |
| 9 sep | 1 (Chrome, BE, ingelogd, en_GB professional-8) | 1 | 0 | 1 | 1 | **betaald via Bancontact** |
| 10 sep | 1 (Mobile Safari, professional-9) | 1 | tab 8 uur open, 11 sep gesloten | 0 | 0 | afgebroken in deelnemerstap |
| 11 sep | 0 | 0 | 0 | 0 | 0 | geen echte bezoekers |
| 12 sep | 1 (Mobile Safari, NL, en_GB professional-8) | 1 | 1 (binnen 1 seconde) | 0 | 0 | afgebroken in deelnemerstap |

**Grootste lek:** de deelnemerstap direct na de ticketbevestiging. Vijf pogingen in zes dagen, vier afbrekers, allemaal anoniem, drie van de vier op mobiel Safari. De enige betaler was een ingelogde bestaande klant. Gisteren voegde daar het hardste bewijs tot nu toe aan toe: sluiten binnen één seconde na het openen van het venster. De hypothese blijft dat het deelnemersformulier anonieme bezoekers om een account of te veel gegevens vraagt, of op mobiel niet bruikbaar is. Zonder opnames blijft dit een hypothese; actie 1 lost dat vandaag op.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echte sessies | Betaald (/shop/confirmation) | Eindigde op SYBB pagina |
|---------|--------------|---------------|------------------------------|-------------------------|
| Gisteren | 8 | 6 | 0 | 5 (2 bot, 1 inschrijfpoging, 2 lezers) |
| 5 t/m 11 sep | 30 | 19 | 1 | n.v.t. |

Warme pool (laatste 30 dagen, 13 augustus t/m 12 september): 132 personen bekeken een SYBB registratiepagina, 9 daarvan op meer dan één dag en 3 op drie of meer dagen. Dat is de retargeting-doelgroep zodra de campagne herstart.

## 5. Rode Vlaggen 🚩

- **Vierde afbreker in de deelnemerstap, in één seconde.** Sessie 3 is het sterkste signaal tot nu toe dat de stap na de ticketbevestiging kapot of afschrikwekkend is voor anonieme mobiele bezoekers. Vier van vijf pogingen deze week verloren op dezelfde plek.
- **Session replay bevat geen opnames meer.** De tabel `session_replay_events` bevat in het hele project nog precies één opname (29 maart 2026). De 416 tot 3.876 opnames per dag die op 6 september nog geteld werden voor 29 augustus t/m 3 september zijn verdwenen. Dat wijst op retentie van minder dan 30 dagen, een opgeschoonde omgeving, of een uitgeschakelde recording plus een verlopen bewaartermijn. De vijf inschrijfpogingen van deze week zijn geen van alle terug te kijken.
- **Meta-data niet bereikbaar tot 21 september.** Pipeboard weeklimiet: 100 van 30 executies gebruikt; de resetdatum schoof op van 14 naar 21 september. Zolang alles op PAUSED staat is dit geen budgetrisico, maar bij een herstart is er geen dagelijkse ad-level data.
- **Crawlergolf site-breed houdt aan.** Gisteren 7.607 pageviews van 5.784 bezoekers in 5.834 sessies; 5.326 sessies (91%) zijn direct, 0 seconden en hooguit één pageview (nagemeten 13 september 's middags, eerdere telling 5.319). Derde dag op rij (10 sep 85%, 11 sep 88%). De SYBB-cijfers hierboven zijn er niet door geraakt omdat die per sessie zijn gefilterd.
- **Structureel, ongewijzigd:** SYBB campagne 146 dagen gepauzeerd, landing page 15 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer, social referrals op 0.
- **Link-preview bots blijven nieuwe URL's raken.** Gisteren professional-47 (en_GB) vanuit Litouwen en professionell-englisch-2 (de) vanuit Italië. Iemand deelt deze links; de ontvangers klikten niet door.

Niet rood: rage en dead clicks (0), bounce rate van echte SYBB sessies (0 van 6), en het bezoekersvolume, dat gisteren juist het hoogste van de week was.

## 6. Top 3 Acties voor Vandaag

1. **Doorloop zelf de deelnemerstap op een iPhone in Safari, uitgelogd, op de Engelse pagina van professional-8.** Wat: open in een privévenster https://www.sempertexeurope.com/en_GB/event/start-your-balloon-business-professional-8/register, klik "Register", zet het aantal op 1, klik "Register" in het ticketvenster en maak een screenshot van wat er dan precies verschijnt: login-eis, verplichte velden (bedrijfsnaam, btw-nummer?), prijs, een venster dat buiten het scherm valt, of een foutmelding. Herhaal ingelogd. Waarom: dit staat voor de derde dag op één; gisteren sloot een nieuwe bezoeker dit venster binnen één seconde, en vier van vijf pogingen deze week strandden hier. Hoe: handmatig, 10 minuten. Verwachte impact: bevestiging of uitsluiting van een account-eis of formulierprobleem in de enige converterende SYBB stap; als het een account-eis is, is een gastoptie of een uitleg boven het formulier de fix. Escalatie: Groen.
2. **Controleer de replay-instellingen en de bewaartermijn in PostHog.** Wat: open https://eu.posthog.com/project/149694/settings/environment-replay en https://eu.posthog.com/project/149694/replay/home, controleer of "Record user sessions" aan staat, het sampling-percentage, de minimale sessieduur, de URL-triggers en de retentie. Doe daarna de testsessie uit actie 1 en check binnen een uur of de opname verschijnt. Waarom: de replay-tabel is leeg tot op één opname in maart; de opnames van eind augustus zijn weg, dus dit is meer dan "recording staat uit". Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: de eerstvolgende inschrijfpoging is wel te analyseren. Escalatie: Geel (Robin).
3. **Bepaal het canonieke SYBB verkoopkanaal: eventpagina of webshop-product.** Wat: controleer in Odoo of het shop-product "Start Your Balloon Business Professional 5 en 6 oktober 2026" (id 5290) bewust naast de event-registratie bestaat, en welke van de twee de ads en de e-mails straks als bestemming krijgen. Zet daarna het shop-product wel of niet in de SYBB funneldefinitie van `skills/daily-sybb-report/SKILL.md`. Waarom: gisteren kwam de eerste bezoeker sinds 21 augustus op dat shop-product terecht, en het rapport telt dat kanaal nu niet als funnelstap. Twee routes zonder keuze splitsen straks ook de conversiedata. Hoe: 15 minuten in Odoo plus een skill-aanpassing. Verwachte impact: één meetbare funnel per workshopdatum in plaats van twee halve. Escalatie: Geel (Robin beslist).

Blijft open uit eerdere rapporten: de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`), één gedeelde en gecachte Meta-call per dag voor de drie rapporten (of een Pipeboard Pro-plan) vóór de reset van 21 september, en het aanpassen van de funneldefinitie in de skill van landing page naar event funnel.

---

**Databronnen:** Meta Ads niet live: Pipeboard (MCP vroeg om autorisatie, directe JSON-RPC route gaf `weekly_limit_exceeded`, reset 21 september 2026 00:00 UTC); campagnestatus uit het live ads-rapport van 13 september en het 30d-extract van 11 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): pageviews, sessies, autocapture-clicks met elements chain, session replay events, session recordings endpoint en persoonshistorie. Periode gisteren = 12 september 2026 UTC, 7d = 5 t/m 11 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.

**Herverificatie 13 september 2026 (middagrun):** alle PostHog-cijfers opnieuw opgehaald en ongewijzigd bevestigd: 8 SYBB sessies (6 echt, 2 bounces, 0 met Meta als entry), 7d-basis 30 sessies (19 echt), dezelfde 6 SYBB pagina's, dezelfde klikreeks van de inschrijfpoging om 04:59 UTC, 0 betalingen gisteren tegen 1 in de 7 dagen ervoor, 0 rage of dead clicks, 0 events op startyourballoonbusiness.com sinds 29 augustus, 0 pageviews met `utm_source=meta` sinds 5 september, en nog altijd precies 1 opname in `session_replay_events` (29 maart). De ene Facebook-sessie van gisteren (20:44 UTC, m.facebook.com) had 0 pageviews en raakte geen SYBB pagina. Pipeboard gaf opnieuw `weekly_limit_exceeded` met `reset_date` 21 september 2026 00:00 UTC.
