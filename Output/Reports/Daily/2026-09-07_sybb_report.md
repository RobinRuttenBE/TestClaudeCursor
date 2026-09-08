# SYBB Daily Report: 7 september 2026

## 1. Samenvatting
Meta Ads campagne `2026: SYBB` staat nog steeds op PAUSED (sinds 19 april 2026, 141 dagen) en had gisteren, in de 7 dagen ervoor en in de hele periode nul spend, nul impressies en nul clicks. De landing page startyourballoonbusiness.com kreeg voor de tiende dag op rij 0 bezoekers. De werkelijke SYBB funnel op sempertexeurope.com had gisteren 3 bezoekers in 3 sessies, alle drie uit België en alle drie echte mensen; voor het eerst sinds 3 september zaten er geen bot-hits tussen. De kwaliteit was hoog: één bezoeker klikte op het telefoonnummer op de registratiepagina, één opende het registratieformulier tweemaal en sloot het weer, en één las de Franse registratiepagina drie minuten lang. Of iemand zich heeft ingeschreven blijft onmeetbaar. Session replay staat nu vier dagen op nul.

## 2. Meta Ads Performance

**Status data:** live opgehaald via de directe Pipeboard JSON-RPC route. De `pipeboard-meta-ads` en `claude.ai Pipeboard Meta Ads` MCP servers vragen in deze niet-interactieve sessie om autorisatie, maar de geconfigureerde token werkt direct. De weeklimiet van het gratis plan is op maandag gereset. Ad account `act_567892422940728`.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Kopie `2026: SYBB - Kopie` (ID 120243293329420239) ook PAUSED sinds 27 augustus. Alle 7 campagnes in het ad account staan op PAUSED, de wholesaler campagnes SWE en LIT sinds 4 september.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De insights-call voor 7 september en voor 31 augustus t/m 6 september gaf een lege dataset. PostHog bevestigt dit onafhankelijk: in de afgelopen 8 dagen kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`.

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren. Lifetime referentie voor een herstartbeslissing (13 januari t/m 19 april 2026) staat in het rapport van 4 september: €2.485 spend, 4,06% CTR, €0,21 CPC, 6.992 landing page views, 6 aankopen.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bezoekers | 0 | 0 | n.v.t. | ⚪ |
| Pageviews | 0 | 0 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = geen data. De laatste pageviews op dit domein waren de twee interne testhits van 28 augustus. Van 29 augustus t/m 7 september is er niets geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (7 sep) | 7d Gemiddelde (31 aug t/m 6 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 3 | 6,1 | ↓ (-51%) |
| Sessies | 3 | 7,3 | ↓ (-59%) |
| Pageviews SYBB pagina's | 3 | 15,3 (8,2 zonder de uitschieter van 31 aug) | ↓ |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 87s, mediaan 53s | gemiddeld 637s, mediaan 134s | ↓ |
| Bounce rate (zelfde sessies) | 0% (0 van 3) | 24% (12 van 51) | ↓ (goed) |
| Sessies van 0 seconden (bot-patroon) | 0 van 3 | 14 van 51 (27%) | ↓ (goed) |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 sinds 4 sep | → |

Het lagere volume is echt, maar de daling in sessieduur is deels een artefact: het 7-daags gemiddelde wordt opgetrokken door enkele zeer lange sessies (2 en 5 september). De mediaan van 53s gisteren ligt onder de 90s target, maar de drie sessies waren kort en doelgericht, geen afhakers. Zie de tabel hieronder.

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /event/start-your-balloon-business-professional-7/register | 1 | 1 |
| /event/start-your-balloon-business-professional-8/register | 1 | 1 |
| /fr/event/start-your-balloon-business-professionnel-9/register | 1 | 1 |

De drie sessies van gisteren:

| Sessie | Tijd (UTC) | Herkomst | Land / device | Instap | Duur | Pagina's | Wat gebeurde er |
|--------|------------|----------|---------------|--------|------|----------|-----------------|
| 1 | 09:53 | Google | BE, Mobile Safari | / | 27s | 3 | Klikte binnen 4 seconden op "Workshops" in het menu, koos op /events de september-datum, landde op professional-7/register en klikte daar op het telefoonnummer +32 89 23 57 58. Sessie eindigde op de registratiepagina. |
| 2 | 09:58 | Direct | BE, Chrome desktop | / | 53s | 4 | Klikte op "Workshops", accepteerde alleen essentiële cookies, klikte "Tickets kopen" bij professional-8, klikte tweemaal op "Registreer", klikte nog eens in het formulier, en sloot het met "Afsluiten". Ging terug naar /events en stopte. |
| 3 | 11:57 | Google | BE, Chrome mobiel | /fr/.../professionnel-9/register | 182s | 1 | Landde vanuit Google direct op de Franse registratiepagina, accepteerde cookies en bleef 3 minuten lezen. Geen klik op registreren. Pageleave aanwezig, dus een echte bezoeker. |

Alle drie hebben `$pageleave`, `$autocapture` en `$web_vitals`. Geen enkele sessie vertoont het lege eventpatroon van de Japanse en Amerikaanse link-preview bots van 4, 5 en 6 september.

Opvallend: sessies 1 en 2 komen allebei uit België, starten 5 minuten na elkaar op de homepage en klikken allebei direct op "Workshops". Het is een onbevestigde maar plausibele lezing dat dit dezelfde persoon is die eerst op de telefoon het nummer aanklikte en daarna op de desktop het formulier probeerde. Als dat klopt, dan heeft één geïnteresseerde gisteren tweemaal geprobeerd contact te leggen of in te schrijven, en is beide keren zonder meetbaar resultaat gestopt.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren:
SYBB registratiepagina bekeken (3 bezoekers, 100%) → interactie op de registratiepagina (2, 67%: telefoonnummer en Registreer-knop) → sessie beëindigd op een SYBB registratiepagina (2, 67%) → registratie voltooid (niet meetbaar)

Conversie-proxy (sessies met een SYBB pagina die ook een Odoo account-registratie of webshop bestelling afronden; geen harde workshop-conversie):

| Periode | SYBB sessies | Met account-registratie voltooid | Met webshop bestelling | Eindigde op SYBB pagina |
|---------|--------------|----------------------------------|------------------------|-------------------------|
| Gisteren | 3 | 0 | 0 | 2 (67%) |
| 31 aug t/m 6 sep | 51 | 1 | 1 | 33 (65%) |

**Grootste lek:** sessie 2 is het duidelijkste voorbeeld tot nu toe van een afgebroken inschrijving. De bezoeker klikte tweemaal op "Registreer", deed nog één klik in het formulier en sloot het binnen 22 seconden met "Afsluiten". Dat is geen bot en geen toevallige klik, dat is iemand die wilde inschrijven en stopte. Zonder session replay en zonder formulier-events is niet te zien waarom: een verplicht account, een onduidelijk veld, een prijs die pas in het formulier zichtbaar werd, of een browserprobleem. Dit is precies het gat dat de acties van gisteren (replay herstellen, registratie-event toevoegen) moeten dichten.

## 5. Rode Vlaggen 🚩

- **Session replay is nu vier dagen op nul.** Opnames per dag: 31 aug 2.264, 1 sep 3.876, 2 sep 1.558, 3 sep 92, 4 t/m 7 sep 0. Vertraagde verwerking is als verklaring afgevallen. Sessie 2 van gisteren (afgebroken inschrijving) is precies het soort sessie waarvoor replay bedoeld is, en er is geen opname van.
- **Afgebroken inschrijving zonder verklaring.** Sessie 2: tweemaal "Registreer", daarna "Afsluiten". Geen formulier-events, geen replay, geen bevestigingsevent. Het rapport kan niet zeggen of het formulier faalde of de bezoeker afhaakte.
- **Volume laag.** 3 SYBB sessies tegenover 7,3 gemiddeld, de laagste dag sinds 3 september (2). Zonder betaald verkeer is het volume volledig afhankelijk van organisch zoekverkeer en directe links. Twee van de drie bezoekers kwamen gisteren via Google.
- **Structureel, ongewijzigd:** geen registratie-voltooid event, geen scroll- en CTA-events op de landing page, SYBB campagne 141 dagen gepauzeerd, landing page 10 dagen op 0 bezoekers.
- **Site-brede verkeerspiek lijkt af te lopen.** 923 unieke bezoekers gisteren tegenover 5.887 op 6 september en een 7d gemiddelde van 7.019. Nog boven de baseline van 300 tot 400 van vóór 31 augustus, maar de scherpe daling wijst erop dat de bron van de piek (vermoedelijk crawlers) wegvalt. Pageviews bleven wel hoog (6.242 bij 923 bezoekers), dus een deel van het botverkeer loopt nog.

Niet meer rood: bot-aandeel in SYBB verkeer. Na 10 van 17 bot-sessies op 4 t/m 6 september was het gisteren 0 van 3. De directe hits uit Japan en de VS zijn gestopt, mogelijk omdat de gedeelde links niet meer actief rondgaan.

## 6. Top 3 Acties voor Vandaag

1. **Session replay herstellen, nu met een concrete aanleiding.** Wat: open Project settings, Session replay, op https://eu.posthog.com/project/149694/settings/environment-replay en controleer of recording aan staat, het sampling-percentage, en de activity log rond 3 september. Draai daarna één testsessie op /event/start-your-balloon-business-professional-8/register, klik op "Registreer" en controleer of de opname binnen een uur verschijnt. Waarom: vier dagen nul opnames, en gisteren een afgebroken inschrijving die alleen met replay te verklaren was. Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: de volgende afgebroken inschrijving is wel te analyseren. Escalatie: Geel (Robin).
2. **Zelf het registratieformulier van professional-8 doorlopen op desktop.** Wat: open in een incognitovenster /event/start-your-balloon-business-professional-8/register, klik "Registreer" en noteer wat er gebeurt: is er een verplichte login, welke velden zijn er, staat de prijs erin, werkt de knop bij "alleen essentiële cookies". Waarom: sessie 2 sloot het formulier binnen 22 seconden na tweemaal klikken op "Registreer", met alleen essentiële cookies geaccepteerd. Als het formulier bij die cookie-instelling hapert of een account eist, dan verliest elke bezoeker die dat pad volgt. Hoe: handmatig, 5 minuten, zonder ontwikkelaar. Verwachte impact: directe bevestiging of uitsluiting van een technisch lek in de enige converterende SYBB pagina. Escalatie: Groen.
3. **Registratie-voltooid event toevoegen aan de event flow.** Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_complete`) laten vuren op de bevestigingsstap na `/event/*/register`, plus een `sybb_registration_start` op de klik op "Registreer". Waarom: gisteren klikten 2 van 3 bezoekers op de registratiepagina (telefoonnummer, Registreer) en het rapport kan niet zeggen wat het opleverde. De proxy (1 accountregistratie en 1 bestelling in 51 SYBB sessies deze week) is geen bewijs van workshopinschrijvingen. Hoe: Odoo website-ontwikkelaar laat de events vuren, of via een PostHog action op de "Registreer"-knop (autocapture vangt die klik al, dus de start-actie is direct in PostHog aan te maken zonder code). Verwachte impact: het dagelijkse rapport krijgt een echte start- en conversie-KPI. Escalatie: Oranje (ontwikkelaar voor de voltooiing), Groen (start-actie in PostHog).

Kleinere opvolging: de klik op het telefoonnummer in sessie 1 is een contactpoging die buiten alle systemen valt. Vraag intern of er gisteren rond 11:53 lokale tijd een telefoontje over de SYBB workshop is binnengekomen. Als ja, dan is dat de eerste bevestigde SYBB lead van deze week.

---

**Databronnen:** Meta Ads live via de directe Pipeboard JSON-RPC route (MCP servers vragen autorisatie in deze niet-interactieve sessie); campagne-lijst plus campagne-niveau insights voor 7 september en 31 augustus t/m 6 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405). Periode gisteren = 7 september 2026 UTC, 7d = 31 augustus t/m 6 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
