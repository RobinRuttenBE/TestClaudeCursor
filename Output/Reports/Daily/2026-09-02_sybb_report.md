# SYBB Daily Report: 2 september 2026

## 1. Samenvatting
De SYBB ad campagne staat nog altijd op PAUSED (sinds 19 april 2026) en de landing page startyourballoonbusiness.com kreeg gisteren opnieuw 0 bezoekers. De werkelijke SYBB funnel, de event registratiepagina's op sempertexeurope.com, kreeg gisteren 5 bezoekers in 6 sessies, iets onder het 7-daags gemiddelde van 5,7 bezoekers per dag. Al dat verkeer komt uit site navigatie, geen ads, geen e-mail, geen UTM's. Conversie blijft onmeetbaar: de pagina `/registratie-voltooid` die gisteren in een SYBB sessie opdook, blijkt de B2B accountregistratie van de webshop te zijn, niet de workshopinschrijving.

## 2. Meta Ads Performance

**Campagne status:** `2026: SYBB` (ID 120239435987290239) staat op **PAUSED**, laatst gewijzigd 19 april 2026. De kopie `2026: SYBB - Kopie` (ID 120243293329420239) staat ook op PAUSED. Beide leverden over 26 augustus t/m 2 september nul impressies en nul spend. Het ad account (act_567892422940728) draait wel twee wholesaler lead-campagnes (LIT en SWE, samen €125,88 gisteren), dat is een andere funnel en valt buiten dit rapport.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren.

Ter referentie voor een herstartbeslissing, lifetime cijfers van de campagne (13 januari t/m 19 april 2026):

| Spend | Impressions | Link clicks | CTR | CPC | LPV | Purchases |
|-------|-------------|-------------|-----|-----|-----|-----------|
| €2.485,04 | 297.174 | 10.851 | 4,06% | €0,21 | 6.992 | 6 |

De CPC lag ruim onder de target van €0,50. Het probleem zat niet in de ads maar in de conversie na de klik: 6 aankopen op bijna 7.000 landing page views.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | Afgelopen 7d | Target | Status |
|--------|----------|--------------|--------|--------|
| Bezoekers | 0 | 2 | n.v.t. | ⚪ |
| Pageviews | 0 | 2 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = onvoldoende data om een target te beoordelen. De enige 2 bezoekers van de week zijn dezelfde als in het rapport van gisteren (28 augustus, één via manage.wix.com en één test-URL met `utm_content=h11_b3_cta5`). Scroll- en CTA-events bestaan niet in het PostHog project. Geen rage clicks, geen session recordings met de landing page als startpagina.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (2 sep) | 7d Gemiddelde (26 aug t/m 1 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 5 | 5,7 | ↓ (-12%) |
| Sessies | 6 | 5,9 | → |
| Pageviews | 12 | 16,6 (9,7 zonder de uitschieter van 31 aug) | → |
| Sessieduur (sessies die een SYBB pagina raken) | mediaan 353s, gemiddeld 1.070s | gemiddeld 444s | ↑ |
| Bounce rate (zelfde sessies) | 0% | 19% | → |
| Rage clicks | 0 | 0 | → |

Het gemiddelde van gisteren is vertekend door één sessie van 98 minuten die via Google op een Nozzle Up productpagina binnenkwam en 23 pagina's bekeek. De mediaan van 353 seconden is de betere maat.

Verdeling gisteren per pagina:

| Registratiepagina | Bezoekers | Pageviews | Land | Device | Herkomst |
|-------------------|-----------|-----------|------|--------|----------|
| /event/.../professional-7/register | 4 | 8 | NL, BE | desktop, mobiel | site navigatie |
| /en_GB/event/.../professional-7/register | 1 | 2 | BE | mobiel | site navigatie |
| /en_GB/event/.../professional-8/register | 1 | 1 | BE | mobiel | site navigatie |
| /fr/event/.../professionnel-7/register | 1 | 1 | FR | desktop | site navigatie |

Editie 7 blijft de trekker: 4 van de 5 bezoekers bekeken een editie 7 pagina. Eén Belgische mobiele bezoeker vergeleek editie 7 en 8 in het Engels, verspreid over 4 uur. Geen enkele bezoeker had UTM parameters.

Over de hele week (26 aug t/m 2 sep): 45 unieke bezoekers op registratiepagina's. Herkomst: 27 via site navigatie, 11 direct, 2 via chatgpt.com, 1 via mail.telenet.be. Geen betaald verkeer.

## 4. Funnel Drop-off
Landing page: niet van toepassing, geen verkeer.

Event funnel sempertexeurope.com:
Registratiepagina view (5 bezoekers, 100%) → registratie voltooid (onbekend, geen event)

**Grootste lek:** onmeetbaar. Belangrijke correctie op een verleidelijke aanname: de pagina's `/registratie` en `/registratie-voltooid` (alle talen) zijn de B2B klantaccount-registratie van de Odoo webshop. De flow is `/web/login` → `/registratie` → `/registratie-voltooid`, en de referrers zijn uitsluitend die accountpagina's. Dat is dus geen workshopconversie. Tussen de event registratiepagina en de bevestiging staat nog steeds geen meetpunt.

Wel een opvallend kruisverband: in de afgelopen 30 dagen eindigden 4 van de 148 sessies met een SYBB registratiepagina ook in een voltooide accountregistratie (2,7%), gisteren nog één. Mogelijke verklaring: de event-inschrijving vereist een klantaccount, waardoor bezoekers eerst een account moeten aanmaken. Dat is niet bevestigd uit de data en vraagt een handmatige check (zie actie 2).

## 5. Rode Vlaggen 🚩
Geen performance-anomalieën in de ads (er draait niets voor SYBB). Structurele signalen, nu voor de vierde opeenvolgende rapportage:

1. **Rapport meet de verkeerde pagina.** De skill kijkt naar startyourballoonbusiness.com (0 bezoekers), terwijl de registratiepagina's op sempertexeurope.com dagelijks 5 tot 10 bezoekers krijgen.
2. **Nul conversiemeting op de werkelijke funnel.** 45 bezoekers per week bekijken een registratiepagina en niemand weet hoeveel er inschrijven. De schijnbare conversiepagina `/registratie-voltooid` is een andere funnel.
3. **Geen scroll- of CTA-events.** Bij een herstart van de ads is er geen on-page engagement signaal beschikbaar.

Positief signaal: er verschijnen wel nieuwe custom events in het project (`instagram_click` sinds 1 september, `newsletter_subscribe` sinds 3 september). De tracking wordt dus uitgebreid, alleen nog niet op de workshopfunnel.

## 6. Top 3 Acties voor Vandaag

1. **Voeg een registratie-voltooid event toe aan de event funnel.**
   Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_submit`) op de bevestigingsstap van de Odoo event-inschrijving, met editie en taal als properties. Niet verwarren met `/registratie-voltooid`, dat is de accountregistratie.
   Waarom: 5 bezoekers gisteren, 45 in een week, 148 sessies in 30 dagen op registratiepagina's en nul zicht op inschrijvingen. Dit is het enige ontbrekende meetpunt om conversie te rapporteren.
   Hoe: zelfde methode als `newsletter_subscribe` en `instagram_click`, die deze week zijn toegevoegd, volgens `tracking-standards`.
   Verwachte impact: het rapport kan vanaf dan conversie per editie en per taal tonen.
   Escalatie: Oranje (website aanpassing nodig).

2. **Check of de event-inschrijving een klantaccount vereist.**
   Wat: open als uitgelogde bezoeker `/event/start-your-balloon-business-professional-7/register` en doorloop de inschrijving tot de bevestiging.
   Waarom: 4 van de 148 SYBB sessies in 30 dagen eindigden in een accountregistratie. Als een account verplicht is, is dat een forse drempel voor starters die nog geen klant zijn, en dan verklaart dat een deel van het lek.
   Hoe: handmatig, 5 minuten. Bij een verplicht account: overweeg gastinschrijving of maak de accountstap onderdeel van de gemeten funnel.
   Verwachte impact: ofwel een concrete frictie gevonden, ofwel de hypothese uitgesloten.
   Escalatie: Geel (Robin).

3. **Herdefinieer de daily-sybb-report skill op de event registratiepagina's.**
   Wat: pas `skills/daily-sybb-report/SKILL.md` aan zodat sectie 3 en 4 standaard de paden `/event/start-your-balloon-business-*/register` (alle talen) meten, met sessieduur, bounce en pageviews per editie. De landing page wordt een bijlage tot de campagne herstart.
   Waarom: het rapport meet nu vier dagen op rij een dode pagina, en de bruikbare data zit in een subsectie.
   Hoe: skill-bestand aanpassen, kan direct na goedkeuring.
   Verwachte impact: het rapport gaat over de funnel die bezoekers heeft. Een herstart van `2026: SYBB` (lifetime CPC €0,21) blijft pas zinvol na actie 1, anders draait de campagne opnieuw blind.
   Escalatie: Geel (Robin goedkeuring op de nieuwe meetdefinitie).

---
*Databronnen: Meta Ads via Pipeboard MCP (directe JSON-RPC, account act_567892422940728) en PostHog project "STX EU" (eu.posthog.com, project 149694, tijdzone UTC). De PostHog MCP server verbond niet (DNS fout en HTTP 405), de geconfigureerde MCP token is gebruikt voor directe HogQL queries op dezelfde data. Geen Google bronnen gebruikt, niets naar de Google Sheet geschreven. Gegenereerd op 3 september 2026.*
