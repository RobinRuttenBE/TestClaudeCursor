# SYBB Daily Report: 3 september 2026

## 1. Samenvatting
De SYBB ad campagne staat nog altijd op PAUSED (sinds 19 april 2026) en de landing page startyourballoonbusiness.com kreeg gisteren opnieuw 0 bezoekers. De werkelijke SYBB funnel, de event registratiepagina's op sempertexeurope.com, had gisteren een stille dag: 2 bezoekers in 2 sessies, tegenover een 7-daags gemiddelde van 6,1 bezoekers per dag. Dat is de laagste dag sinds 30 augustus. Beide bezoekers kwamen uit site navigatie, geen ads, geen e-mail, geen UTM's. Conversie blijft onmeetbaar omdat er nog steeds geen registratie-voltooid event bestaat.

## 2. Meta Ads Performance

**Campagne status:** `2026: SYBB` (ID 120239435987290239) staat op **PAUSED**, laatst gewijzigd 19 april 2026. De kopie `2026: SYBB - Kopie` (ID 120243293329420239) staat ook op PAUSED. Beide leverden over 27 augustus t/m 3 september nul impressies en nul spend. Het ad account (act_567892422940728) draait wel twee wholesaler lead-campagnes (LIT €77,71 en SWE €76,08, samen €153,79 gisteren). Dat is een andere funnel en valt buiten dit rapport.

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
| Bezoekers | 0 | 0 | n.v.t. | ⚪ |
| Pageviews | 0 | 0 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = onvoldoende data om een target te beoordelen. De laatste 2 pageviews op de landing page dateren van 28 augustus (één via manage.wix.com en één test-URL met `utm_content=h11_b3_cta5`), die vallen nu buiten het 7-daags venster. Scroll- en CTA-events bestaan niet in het PostHog project. Geen rage clicks, geen session recordings.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (3 sep) | 7d Gemiddelde (27 aug t/m 2 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 2 | 6,1 | ↓ (-67%) |
| Sessies | 2 | 6,4 | ↓ (-69%) |
| Pageviews | 4 | 18,0 (11,3 zonder de uitschieter van 31 aug) | ↓ |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 397s, mediaan 397s | gemiddeld 505s | ↓ (-21%) |
| Bounce rate (zelfde sessies) | 0% | 17% | → |
| Rage clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | n.v.t. | → |

De twee sessies van gisteren:

| Sessie | Herkomst | Instap | Duur | Pagina's | SYBB pagina's bekeken |
|--------|----------|--------|------|----------|-----------------------|
| 1 | Organic Search, BE, mobiel | /de/shop | 730s | 23 | /fr/event/.../professional-47/register (2x) |
| 2 | Direct, BE, mobiel | homepage | 64s | 4 | /event/.../professional-9/register en /event/.../professional-8/register |

Sessie 1 was een shopbezoeker die de FR-registratiepagina van editie 47 onderweg bekeek en eindigde op pagina 3 van de nieuwe producten in de FR-shop. Sessie 2 kwam direct op de homepage binnen, vergeleek editie 8 en 9 en verliet de site op de registratiepagina van editie 9. Geen van beide sessies heeft een session recording.

Over de afgelopen 7 dagen (28 aug t/m 3 sep): 30 unieke bezoekers, 36 sessies en 114 pageviews op registratiepagina's. Herkomst: 24 via site navigatie, 5 direct, 1 via mail.telenet.be. Geen betaald verkeer, geen UTM's.

Verdeling per editie over die 7 dagen (unieke bezoekers, alle talen samen):

| Editie | Bezoekers | Opmerking |
|--------|-----------|-----------|
| Professional 7 | 15 | blijft de trekker |
| Professional 9 | 9 | sinds 27 augustus zichtbaar |
| Professional 8 | 7 | |
| Professional 47 | 5 | sinds 31 augustus zichtbaar, 4 talen |
| Professional 48 | 4 | sinds 31 augustus zichtbaar, 4 talen |
| Professional English 2 | 2 | |

Nieuw ten opzichte van vorige week: de edities 9, 47 en 48 krijgen verkeer. Editie 47 en 48 verschenen op 31 augustus in vier taalvarianten tegelijk, wat wijst op nieuw aangemaakte events. Editie 7 blijft de populairste pagina, maar het aandeel van editie 7 daalt naarmate de nieuwe edities zichtbaar worden.

## 4. Funnel Drop-off
Landing page: niet van toepassing, geen verkeer.

Event funnel sempertexeurope.com:
Registratiepagina view (2 bezoekers, 100%) → registratie voltooid (onbekend, geen event)

**Grootste lek:** onmeetbaar. Tussen de event registratiepagina en de bevestiging staat nog steeds geen meetpunt. De pagina `/registratie-voltooid` is de B2B accountregistratie van de webshop en telt niet als workshopconversie. Gisteren eindigde geen van de 2 SYBB sessies in een accountregistratie.

Nieuw inzicht over de meetbaarheid: `$autocapture` en `$pageleave` draaien site-breed op sempertexeurope.com (gisteren 12.359 en 8.786 events). Bounce rate en sessieduur op de event funnel zijn dus wel betrouwbaar te berekenen. Alleen de conversie zelf ontbreekt.

## 5. Rode Vlaggen 🚩

1. **Bezoekersdip op de registratiepagina's: 2 bezoekers tegenover 6,1 gemiddeld (-67%).** Op deze volumes is één dag geen trend, maar het is de laagste dag sinds 30 augustus en beide bezoekers kwamen via site navigatie. Er is geen enkele actieve bron die verkeer naar de registratiepagina's stuurt.
2. **Rapport meet de verkeerde pagina.** De skill kijkt naar startyourballoonbusiness.com (0 bezoekers in 7 dagen), terwijl de registratiepagina's op sempertexeurope.com 30 bezoekers per week krijgen. Vijfde opeenvolgende rapportage met dit signaal.
3. **Nul conversiemeting op de werkelijke funnel.** 30 bezoekers per week bekijken een registratiepagina en niemand weet hoeveel er inschrijven.
4. **Geen scroll- of CTA-events.** Bij een herstart van de ads is er geen on-page engagement signaal beschikbaar.

Site-breed, buiten SYBB: 73 rage clicks op shop categoriepagina's en `/web/login`. Dat is een webshop signaal, niet SYBB, maar het raakt wel de loginstap die mogelijk vóór de event-inschrijving zit (zie actie 2).

Positief signaal: de custom events blijven groeien (gisteren 3x `newsletter_subscribe`, 1x `wholesaler_form_submit`, 21x `inspiration_download`). De tracking wordt dus uitgebreid, alleen nog niet op de workshopfunnel.

## 6. Top 3 Acties voor Vandaag

1. **Voeg een registratie-voltooid event toe aan de event funnel.**
   Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_submit`) op de bevestigingsstap van de Odoo event-inschrijving, met editie en taal als properties. Niet verwarren met `/registratie-voltooid`, dat is de accountregistratie.
   Waarom: 30 bezoekers per week op registratiepagina's, verdeeld over 6 edities, en nul zicht op inschrijvingen. Met edities 47 en 48 net live is het extra belangrijk te weten welke editie inschrijvingen oplevert.
   Hoe: zelfde methode als `newsletter_subscribe` en `wholesaler_form_submit`, volgens `tracking-standards`.
   Verwachte impact: het rapport kan vanaf dan conversie per editie en per taal tonen.
   Escalatie: Oranje (website aanpassing nodig).

2. **Check of de event-inschrijving een klantaccount vereist.**
   Wat: open als uitgelogde bezoeker `/event/start-your-balloon-business-professional-9/register` en doorloop de inschrijving tot de bevestiging.
   Waarom: eerder eindigden 4 van de 148 SYBB sessies in 30 dagen in een accountregistratie, en `/web/login` staat gisteren tussen de pagina's met rage clicks. Als een account verplicht is, is dat een forse drempel voor starters die nog geen klant zijn.
   Hoe: handmatig, 5 minuten. Bij een verplicht account: overweeg gastinschrijving of maak de accountstap onderdeel van de gemeten funnel.
   Verwachte impact: ofwel een concrete frictie gevonden, ofwel de hypothese uitgesloten.
   Escalatie: Geel (Robin).

3. **Geef de nieuwe edities 47 en 48 één actieve verkeersbron.**
   Wat: één owned push naar de registratiepagina's, bijvoorbeeld een korte vermelding in de eerstvolgende nieuwsbrief en een story met link, beide met UTM's volgens de conventie (`utm_source=newsletter` of `utm_source=instagram`, `utm_campaign=sybb`).
   Waarom: alle 30 bezoekers van de afgelopen week kwamen via site navigatie of direct. Er is geen enkele bron die de nieuwe edities actief onder de aandacht brengt, en gisteren zakte het verkeer naar 2 bezoekers. Een ads-herstart (lifetime CPC €0,21) blijft pas zinvol na actie 1, een owned push kost niets en levert direct een UTM-gesegmenteerd signaal.
   Hoe: nieuwsbrief via Brevo, story via Metricool, URL's via `/utm-generate`.
   Verwachte impact: eerste meetbare bron-segmentatie op de registratiepagina's en een test of de nieuwe edities vraag opwekken.
   Escalatie: Geel (Robin goedkeuring op copy en timing).

---
*Databronnen: Meta Ads via Pipeboard MCP (directe JSON-RPC, account act_567892422940728) en PostHog project "STX EU" (eu.posthog.com, project 149694, tijdzone UTC) via de claude.ai PostHog MCP (HogQL). De geconfigureerde posthog SSE server verbond niet (HTTP 405). Geen Google bronnen gebruikt, niets naar de Google Sheet geschreven. Gegenereerd op 4 september 2026.*
