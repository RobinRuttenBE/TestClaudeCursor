# SYBB Daily Report: 10 september 2026

## 1. Samenvatting
Meta Ads campagne `2026: SYBB` staat nog steeds op PAUSED (sinds 19 april 2026, 144 dagen): nul spend, nul impressies, nul clicks, gisteren en in de 7 dagen ervoor. De landing page startyourballoonbusiness.com kreeg voor de dertiende dag op rij 0 bezoekers. De werkelijke SYBB funnel op sempertexeurope.com had gisteren de beste dag van de week: 6 bezoekers in 6 sessies (7d gemiddelde 3,7), vijf echte mensen en één link-preview bot, en drie van de vijf waren terugkerende bezoekers die de workshop al in augustus bekeken. Twee dingen springen eruit. Ten eerste: op 9 september om 07:22 lokale tijd is de eerste volledig meetbare SYBB inschrijving met betaling gelukt (Belgische klant, ingelogd, Bancontact), en die is niet eerder gerapporteerd omdat het SYBB rapport die dag niet beschikbaar was. Daarmee is bewezen dat de event funnel wél een hard conversiepunt heeft: `/shop/confirmation` na de registratiepagina. Ten tweede: gisteravond om 01:30 lokale tijd brak voor de derde keer in vier dagen een bezoeker de inschrijving af, dit keer één stap dieper dan de vorige twee, na het bevestigen van 1 ticket, in de stap waar de deelnemergegevens gevraagd worden. De tab bleef 8 uur open en werd vanochtend om 09:33 gesloten zonder betaling.

## 2. Meta Ads Performance

**Status data:** live opgehaald via de directe Pipeboard JSON-RPC route. De `pipeboard-meta-ads` en `claude.ai Pipeboard Meta Ads` MCP servers vragen in deze niet-interactieve sessie om autorisatie, maar de geconfigureerde token werkt direct. Ad account `act_567892422940728`.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Kopie `2026: SYBB - Kopie` (ID 120243293329420239) ook PAUSED. Alle 7 campagnes in het ad account staan op PAUSED. Campagne-insights voor 10 september en voor 3 t/m 9 september geven een lege dataset, en een ad-niveau call op het hele account voor 10 september ook. Er liep gisteren geen enkele advertentie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: van 3 t/m 10 september kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`. Organisch social verkeer (Facebook en Instagram referrals) is vrijwel weg: 188 pageviews op 3 september, 47 op 4 september, 5 op 6 en 9 september, 1 gisteren. Geen van die social pageviews raakte een SYBB pagina.

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren. Lifetime referentie voor een herstartbeslissing (13 januari t/m 19 april 2026): €2.485 spend, 297.174 impressies, 4,06% CTR, €0,21 CPC, 6.992 landing page views, 6 aankopen.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bezoekers | 0 | 0 | n.v.t. | ⚪ |
| Pageviews | 0 | 0 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = geen data. Van 29 augustus t/m 10 september is er op dit domein geen enkel event geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (10 sep) | 7d Gemiddelde (3 t/m 9 sep) | Trend |
|--------|-------------------|------------------------------|-------|
| Bezoekers | 6 | 3,7 | ↑ (+62%) |
| Sessies | 6 | 3,9 | ↑ (+54%) |
| Pageviews SYBB pagina's | 9 | 4,6 | ↑ (+96%) |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 154s, mediaan 132s | gemiddeld 543s, mediaan 46s | mediaan ↑ |
| Bounce rate (zelfde sessies) | 17% (1 van 6) | 37% (10 van 27) | ↓ (goed) |
| Sessies van 0 seconden (bot-patroon) | 1 van 6 | 10 van 27 (37%) | ↓ (goed) |
| Sessies die eindigen op een SYBB pagina | 4 van 6 (67%) | 18 van 27 (67%) | → |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 sinds 4 sep | → |

Het 7-daags gemiddelde van de sessieduur wordt opgetrokken door enkele lange sessies eerder in de week; de mediaan is de eerlijker maat en die verdrievoudigde gisteren. Vier van de vijf echte bezoekers bleven langer dan een minuut.

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /event/start-your-balloon-business-professional-9/register | 4 | 3 |
| /event/start-your-balloon-business-professional-8/register | 1 | 1 |
| /event/start-your-balloon-business-professional-7/register | 1 | 1 |
| /event/start-your-balloon-business-professional-47/register | 1 | 1 |
| /en_GB/event/start-your-balloon-business-professional-47/register | 1 | 1 |
| /de/event/start-your-balloon-business-professional-48/register | 1 | 1 |

De zes sessies van gisteren (tijden UTC, lokale tijd is +2 uur):

| Sessie | Tijd | Herkomst | Land / device | Instap | Duur | Pagina's | Wat gebeurde er |
|--------|------|----------|---------------|--------|------|----------|-----------------|
| 1 | 04:45 | Direct | DE, Mobile Safari | /de | 247s | 15 | Bestaande klant, logde in (Anmelden, /de/my, winkelwagen), bekeek de shop, klikte op "Veranstaltungen" en opende de Duitse SYBB pagina professional-48. Na 13 seconden klikte hij op "Shop" en ging verder met bedrukte latex. Was ook op 4 en 5 september op de site, toen zonder SYBB. |
| 2 | 17:00 | Google | NL, Chrome mobiel | / | 124s | 7 | Klikte op "Workshops", vergeleek professional-7 (25s), professional-47 (16s) en het Nozzle Up 2027 spaarplan (28s), en klikte daar op de link "Start your Balloon Business" naar professional-9. Derde bezoek in vier weken (14 en 21 augustus, toen ook één SYBB pagina). |
| 3 | 17:02 | Vervolg van sessie 2 | NL, Chrome mobiel | professional-9/register | 84s | 2 | Zelfde persoon, nieuwe sessie-id na het accepteren van de cookies. Las professional-9 anderhalve minuut, herlaadde de pagina en vertrok. Geen klik op "Registreer". |
| 4 | 21:30 | Direct | NL, Mobile Safari | professional-8/register | 330s | 2 | Las professional-8 ruim 2,5 minuut, klikte op de link "Start your Balloon Business" en las professional-9 nog 3 minuten. Geen klik op "Registreer". Terugkerende bezoeker, zag op 19 augustus ook al een SYBB pagina. |
| 5 | 22:05 | Direct | PL, Chrome iOS | /en_GB/professional-47/register | 0s | 1 | Eén pageview, geen pageleave, autocapture of web vitals. Link-preview bot op een gedeelde URL, geen mens. |
| 6 | 23:30 | Direct | NL, Mobile Safari | professional-9/register | 139s | 1 | Las 2 minuten, accepteerde cookies, klikte op "Registreer" (opent het ticketvenster), zette het aantal op 1 met de plusknop en klikte op de bevestigknop "Registreer" in het venster. Daarna verscheen de stap voor deelnemergegevens. Geen "Naar betaling", geen betaling. De tab bleef open en werd vanochtend om 07:33 UTC gesloten. |

Sessies 1 t/m 4 en 6 hebben `$pageleave`, `$autocapture` en `$web_vitals`: echte mensen. Alleen sessie 5 is bot-patroon.

Drie observaties:

- **Drie van de vijf echte bezoekers zijn terugkerend.** Sessie 1 (DE klant), sessie 2/3 (NL, derde bezoek sinds 14 augustus) en sessie 4 (NL, tweede bezoek sinds 19 augustus). De workshop staat bij deze mensen op een lijstje, ze komen zelf terug zonder advertenties, maar niemand van hen klikte op "Registreer".
- **De cross-sell naar Nozzle Up werkt in beide richtingen.** Sessie 2 kwam via het Nozzle Up spaarplan op professional-9 terecht via de link "Start your Balloon Business" op die pagina. Sessie 4 gebruikte dezelfde link vanaf professional-8. Die interne link is gisteren twee keer gebruikt en is de enige CTA op de SYBB pagina's die aantoonbaar geklikt wordt.
- **Sessie 6 kwam één stap verder dan de afbrekers van 7 en 8 september.** Toen sloten twee bezoekers het ticketvenster met "Afsluiten" binnen 22 seconden na "Registreer". Gisteren bevestigde de bezoeker 1 ticket en strandde in de stap daarna, de deelnemergegevens. Vergelijk met de enige geslaagde inschrijving van 9 september (zie sectie 4): die persoon was ingelogd als bestaande klant. Alle drie de afbrekers waren anonieme bezoekers.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte bezoekers:
SYBB registratiepagina bekeken (5, 100%) → klik op "Registreer" (1, 20%) → ticket bevestigd (1, 100% van de starters) → "Naar betaling" (0) → /shop/confirmation (0)

Event funnel, 3 t/m 9 september:
SYBB registratiepagina bekeken (26 bezoekers, 100%) → klik op "Registreer" of "Register" (3 sessies, 12%) → "Go to Payment" (1, 33% van de starters) → /shop/confirmation (1, 100% van de betalers)

Inschrijfpogingen per dag:

| Dag | Klik "Registreer" (sessies) | "Afsluiten" | "Go to Payment" | Betaald | Uitkomst |
|-----|------------------------------|-------------|-----------------|---------|----------|
| 7 sep | 1 (desktop Chrome, professional-8) | 1 | 0 | 0 | afgebroken na 22s |
| 8 sep | 1 (Mobile Safari, professional-9) | 1 | 0 | 0 | afgebroken na 10s |
| 9 sep | 1 (Chrome, BE, ingelogd, professional-8) | 0 | 1 | 1 | **betaald via Bancontact, 05:22 UTC** |
| 10 sep | 1 (Mobile Safari, professional-9) | 0 | 0 | 0 | ticket bevestigd, deelnemergegevens niet ingevuld, tab 8 uur open |

**De inschrijving van 9 september is nieuw en niet eerder gerapporteerd.** Een Belgische bestaande klant logde om 05:15 UTC in, bekeek eerst een openstaande factuur, ging via "Workshops" naar professional-8 (27s), bekeek het MBP examen (47s), koos daarna bewust "Start your Balloon Business - Professional", klikte tweemaal "Register", vulde de deelnemergegevens in, klikte "Go to Payment", koos Bancontact en landde via /payment/status op /shop/confirmation. Direct daarna volgde een tweede afrekening via de winkelwagen (Checkout, Bancontact, tweede /shop/confirmation om 05:23 UTC); of dat een tweede ticket of een losse bestelling was is uit de data niet op te maken. De route is daarmee voor het eerst hard bevestigd: `/event/start-your-balloon-business-*/register` → "Go to Payment" → `/shop/payment` → `/payment/status` → `/shop/confirmation`. De aanname uit eerdere rapporten dat de workshopconversie in geen van beide funnels meetbaar is, vervalt: een sessie met een SYBB registratiepagina én een `/shop/confirmation` pageview is een betaalde inschrijving.

**Grootste lek:** de stap na de klik op "Registreer". In vier dagen zijn er vier inschrijfpogingen geweest door vier verschillende bezoekers, en alleen de ingelogde bestaande klant rondde af. De twee "Afsluiten" afbrekers stopten in het ticketvenster, de afbreker van gisteren in de deelnemergegevens. Zonder replay is de oorzaak niet zichtbaar, maar het patroon wijst op de deelnemerstap: die vraagt anonieme bezoekers waarschijnlijk om een account, om te veel velden, of toont daar pas de prijs.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Betaald (/shop/confirmation) | Account-registratie voltooid | Eindigde op SYBB pagina |
|---------|--------------|------------------------------|------------------------------|-------------------------|
| Gisteren | 6 | 0 | 0 | 4 (67%) |
| 3 t/m 9 sep | 27 | 1 | 0 | 18 (67%) |

## 5. Rode Vlaggen 🚩

- **Derde afgebroken inschrijving in vier dagen, nu in de deelnemerstap.** 7 en 8 september: "Registreer" gevolgd door "Afsluiten" binnen 22 seconden. Gisteren: "Registreer", 1 ticket bevestigd, en dan stilte, met een tab die tot vanochtend openstond. Drie anonieme bezoekers, drie devices, drie eventpagina's, nul betalingen. De enige die wel betaalde was ingelogd.
- **Session replay staat nu zeven dagen op nul.** Opnames per dag: 3 september 92, 4 t/m 10 september 0. Vier inschrijfpogingen in vier dagen en geen enkele opname om te zien waar het misgaat.
- **Structureel, ongewijzigd:** SYBB campagne 144 dagen gepauzeerd, landing page 13 dagen op 0 bezoekers, geen scroll- en CTA-events op de landing page, geen Meta-verkeer, social referrals op 1 pageview per dag.
- **Link-preview bots blijven SYBB URL's raken.** 1 van 6 sessies gisteren (PL, Chrome iOS, 0s), 10 van 27 in de week ervoor. Iemand deelt de en_GB en professional-47 links, vermoedelijk in WhatsApp of Messenger.

Niet rood: bounce rate (17%), sessieduur (mediaan 132s), rage en dead clicks (0), en het volume (beste dag van de week). Site-breed is de crawlerpiek voorbij: 4.185 unieke bezoekers bij 8.867 pageviews, ruim 2 pageviews per bezoeker tegenover 12 tot 17 op 8 en 9 september.

## 6. Top 3 Acties voor Vandaag

1. **Doorloop zelf de deelnemerstap van het registratieformulier op mobiel Safari, als uitgelogde bezoeker.** Wat: open in een privévenster op een iPhone /event/start-your-balloon-business-professional-9/register, klik "Registreer", zet het aantal op 1, klik "Registreer" in het venster en noteer exact wat er dan verschijnt: een login-eis, verplichte velden (bedrijfsnaam, btw-nummer?), de prijs, een venster dat niet in het scherm past, of een foutmelding. Doe hetzelfde ingelogd met een klantaccount. Waarom: vier pogingen in vier dagen, alleen de ingelogde klant kwam door "Go to Payment"; gisteren strandde een bezoeker precies in deze stap en liet de tab 8 uur open. Hoe: handmatig, 10 minuten, geen ontwikkelaar nodig. Verwachte impact: directe bevestiging of uitsluiting van een account-eis of formulierprobleem in de enige converterende SYBB stap. Escalatie: Groen.
2. **Maak in PostHog de volledige SYBB funnel aan op de bestaande autocapture-events, nu de route bewezen is.** Wat: vier actions in Data management: `sybb_registration_start` (klik op "Registreer" of "Register" met `data-bs-target="#modal_ticket_registration"` op een /event/start-your-balloon-business* pagina), `sybb_ticket_confirm` (klik op de submit-knop `button.a-submit` met tekst "Registreer" of "Register" op dezelfde pagina's), `sybb_go_to_payment` (klik op "Go to Payment" of "Naar betaling") en `sybb_paid` (pageview `/shop/confirmation` in een sessie met een SYBB pagina). Zet die vier in één funnel-insight. Waarom: de betaling van 9 september laat zien dat elke stap al in autocapture zit; zonder deze actions blijft het rapport handmatig sessies uitpluizen en zijn conversies onzichtbaar, zoals gisteren bleek. Hoe: handmatig in PostHog, 20 minuten, geen code. Verwachte impact: dagelijkse start-, bevestig-, betaal- en afbreekratio vanaf morgen, en een meetbare basis voor elke formulieraanpassing. Escalatie: Groen. Daarna de funneldefinitie in `skills/daily-sybb-report/SKILL.md` aanpassen van landing page naar deze event funnel (Geel).
3. **Session replay herstellen.** Wat: open Project settings, Session replay, op https://eu.posthog.com/project/149694/settings/environment-replay en controleer of recording aan staat, het sampling-percentage en de activity log rond 3 september. Draai daarna één testsessie op professional-9/register tot en met de deelnemerstap en controleer of de opname binnen een uur verschijnt. Waarom: zeven dagen nul opnames en vier inschrijfpogingen waarvan niemand kan zien wat er misging. Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: de volgende afgebroken inschrijving is wel te analyseren. Escalatie: Geel (Robin).

Vervalt uit eerdere rapporten: het verzoek om een apart registratie-voltooid event in de Odoo event flow. `/shop/confirmation` na "Go to Payment" is dat event al.

---

**Databronnen:** Meta Ads live via de directe Pipeboard JSON-RPC route (MCP servers vragen autorisatie in deze niet-interactieve sessie): campagne-lijst, campagne-niveau insights voor 10 september en 3 t/m 9 september, plus één ad-niveau call op account-niveau voor 10 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): pageviews, sessies, autocapture-clicks met elements chain, session replay events en bezoekershistorie. Periode gisteren = 10 september 2026 UTC, 7d = 3 t/m 9 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
