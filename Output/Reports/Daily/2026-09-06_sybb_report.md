# SYBB Daily Report: 6 september 2026

## 1. Samenvatting
Meta Ads data was vandaag weer live bereikbaar (Pipeboard weeklimiet gereset op maandag) en bevestigt wat de vorige rapporten alleen konden aannemen: campagne `2026: SYBB` heeft gisteren, in de afgelopen 7 dagen en in de afgelopen 30 dagen nul spend, nul impressies en nul clicks. De campagne staat sinds 19 april 2026 op PAUSED, 140 dagen. De landing page startyourballoonbusiness.com kreeg voor de negende dag op rij 0 bezoekers. De werkelijke SYBB funnel op sempertexeurope.com had gisteren 8 bezoekers in 8 sessies, boven het 7-daags gemiddelde van 5,3. De kwaliteit is opnieuw tweedeling: 4 sessies zijn directe 0-seconden hits zonder vervolg-events (Japan en VS, bot-patroon), 4 sessies zijn echte bezoekers uit het VK, Nederland en België die 1 tot 12 minuten op de site waren en 3 keer hun bezoek op een SYBB registratiepagina eindigden. Of die 3 zich hebben ingeschreven blijft onmeetbaar. Session replay heeft ook gisteren niets vastgelegd, de derde dag op rij.

## 2. Meta Ads Performance

**Status data:** live opgehaald via de directe Pipeboard JSON-RPC route (de `pipeboard-meta-ads` en `claude.ai Pipeboard Meta Ads` MCP servers vragen in deze niet-interactieve sessie nog steeds om autorisatie, maar de geconfigureerde token werkt direct). Ad account `act_567892422940728`.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Kopie `2026: SYBB - Kopie` (ID 120243293329420239) ook PAUSED. Alle 7 campagnes in het ad account staan op PAUSED, inclusief de wholesaler campagnes SWE en LIT.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De insights-call voor gisteren, voor 30 augustus t/m 5 september en voor 8 augustus t/m 6 september gaf voor beide SYBB campagnes een lege dataset. PostHog bevestigt dit onafhankelijk: in de afgelopen 8 dagen kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`, voor geen enkele campagne.

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

Toelichting: ⚪ = geen data. De laatste pageviews op dit domein waren de twee interne testhits van 28 augustus. Van 29 augustus t/m 6 september is er niets geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (6 sep) | 7d Gemiddelde (30 aug t/m 5 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 8 | 4,7 | ↑ (+70%) |
| Sessies | 8 | 5,3 | ↑ (+51%) |
| Pageviews SYBB pagina's | 8 | 13,0 (7,0 zonder de uitschieter van 31 aug) | ↓ (↑ +14% zonder uitschieter) |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 158s, mediaan 61s | gemiddeld 825s, mediaan 236s | ↓ |
| Bounce rate (zelfde sessies) | 50% (4 van 8) | 22% (8 van 37) | ↑ |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 sinds 4 sep | → |

De daling in sessieduur en de stijging in bounce rate komen volledig van de 4 bot-sessies. De 4 menselijke sessies duurden 121s, 169s, 233s en 740s (mediaan 201s), ruim boven de 90s target.

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /de/event/start-your-balloon-business-professionell-8/register | 2 | 2 |
| /event/start-your-balloon-business-professional-9/register | 1 | 1 |
| /en_GB/event/start-your-balloon-business-professional-9/register | 1 | 1 |
| /event/start-your-balloon-business-professional-8/register | 1 | 1 |
| /event/start-your-balloon-business-professional-7/register | 1 | 1 |
| /en_GB/event/start-your-balloon-business-professional-english-2/register | 1 | 1 |
| /fr/event/start-your-balloon-business-professional-4/register | 1 | 1 |

De acht sessies van gisteren:

| Sessie | Tijd (UTC) | Herkomst | Land / device | Instap | Duur | Pagina's | Wat gebeurde er |
|--------|------------|----------|---------------|--------|------|----------|-----------------|
| 1 | 01:13 | Direct | JP, Chrome mobiel | /fr/.../professional-4/register | 0s | 1 | Bounce. Alleen een pageview, geen pageleave, geen autocapture, geen web vitals. |
| 2 | 02:53 | Direct | US, Chrome iOS | /de/.../professionell-8/register | 0s | 1 | Bounce. Zelfde leeg eventpatroon. |
| 3 | 10:46 | proballoonshop.co.uk | GB, Mobile Safari | /en_GB/inspiration | 740s | 4 | Echte bezoeker. Inspiratiepagina (2 inspiration_view), calculator gebruikt (6x calc_mix, 1x calc_swap), naar /become-a-distributor, naar /events, eindigde op professional-9/register. Tot 9 minuten op of na de registratiepagina. |
| 4 | 13:38 | Direct | JP, Chrome mobiel | /en_GB/.../professional-english-2/register | 0s | 1 | Bounce. Leeg eventpatroon. |
| 5 | 13:52 | Google | NL, Chrome mobiel | / | 169s | 7 | Echte bezoeker. Via shop (toebehoren) naar /events, bekeek Alberto Falcone tour (2x) en Twist Masterclass, eindigde op professional-7/register. |
| 6 | 14:45 | Direct | JP, Chrome iOS | /de/.../professionell-8/register | 0s | 1 | Bounce. Leeg eventpatroon. |
| 7 | 17:22 | Google | BE, Chrome mobiel | / | 233s | 11 | Echte bezoeker. Shopbrowsen (afgeprijsd, Fashion Solid Lilac R36), /contactus, /events, professional-8/register (69s), daarna naar MPB examen 10 en gestopt. |
| 8 | 18:03 | Direct | NL, Samsung Internet | /event/.../professional-9/register | 121s | 1 | Echte bezoeker via een gedeelde link. Landde direct op de registratiepagina, bleef 2 minuten, 1 klik (autocapture), pageleave aanwezig. |

Sessies 1, 2, 4 en 6 hebben alleen een `$pageview` en verder niets. Sessies 3, 5, 7 en 8 hebben `$pageleave`, `$autocapture` en `$web_vitals`. Dat is hetzelfde onderscheid als op 4 en 5 september: de directe 0s-hits uit Japan en de VS op Franse, Duitse en Engelse registratie-URL's zijn link-preview bots of crawlers, geen mensen. Over drie dagen zijn 10 van de 17 SYBB sessies zo.

Opvallend in sessie 3: een bezoeker uit het VK komt binnen via proballoonshop.co.uk, gebruikt de mengcalculator, bekijkt de distributeurspagina en eindigt op de Engelse SYBB registratie. Dat is het profiel van een startende professional of kleine retailer die zowel inkoop als opleiding overweegt.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren:
SYBB registratiepagina bekeken (8 bezoekers, 100%) → langer dan 0s op de pagina (4, 50%) → sessie beëindigd op een SYBB registratiepagina (3, 38%) → registratie voltooid (niet meetbaar)

Conversie-proxy (sessies met een SYBB pagina die ook een Odoo account-registratie of webshop bestelling afronden; geen harde workshop-conversie):

| Periode | SYBB sessies | Met account-registratie voltooid | Met webshop bestelling |
|---------|--------------|----------------------------------|------------------------|
| Gisteren | 8 | 0 | 0 |
| 30 aug t/m 5 sep | 37 | 1 | 2 |

**Grootste lek:** het ontbrekende meetpunt na de registratiepagina. Gisteren is een beter voorbeeld dan de dagen ervoor: 3 van de 4 echte bezoekers eindigden hun sessie op een SYBB registratiepagina (sessies 3, 5 en 8), en sessie 8 bleef er 2 minuten en klikte één keer. Dat kan een ingevulde inschrijving zijn of een afgebroken formulier, en het rapport kan het verschil niet zien. Het gedrag van 4 en 5 september (4 tot 15 seconden en terugklikken) herhaalde zich alleen bij sessie 7, die na 69 seconden doorging naar het MPB examen.

## 5. Rode Vlaggen 🚩

- **Session replay is nu drie dagen op nul.** Opnames per dag: 29 aug 416, 30 aug 303, 31 aug 2.264, 1 sep 3.876, 2 sep 1.558, 3 sep 92, 4 sep 0, 5 sep 0, 6 sep 0. Het vorige rapport hield de mogelijkheid open dat replay-data vertraagd binnenkomt. Voor 4 september is er na drie dagen nog steeds niets, dus vertraging is als verklaring vrijwel afgevallen. Geen van de 4 menselijke SYBB sessies van gisteren is opgenomen.
- **Bot-aandeel in SYBB verkeer stijgt.** 4 van 8 sessies gisteren (50%), tegenover 3 van 5 op 5 september en 3 van 4 op 4 september. Alle vier zijn directe hits zonder referrer, zonder UTM en zonder vervolg-events, uit Japan en de VS, op gedeelde registratie-URL's (`professional-4` Frans, `professionell-8` Duits 2x, `professional-english-2`). Zolang die links geen UTM's dragen vervuilen ze de bounce rate en is de bron onvindbaar.
- **Bounce rate 50% op SYBB sessies**, tegenover 22% over de 7 dagen ervoor. Onder de 70% drempel, en volledig verklaard door de bots hierboven. De menselijke bounce rate is 0 van 4.
- **Structureel, ongewijzigd:** geen registratie-voltooid event, geen scroll- en CTA-events op de landing page, SYBB campagne 140 dagen gepauzeerd, landing page 9 dagen op 0 bezoekers.
- **Site-brede verkeerspiek houdt aan.** 5.887 bezoekers gisteren tegenover een baseline van 300 tot 400 vóór 31 augustus (7d gemiddelde 6.223). SYBB pagina's zien hier niets van terug (8 van 5.887). Vertekent alle site-brede ratio's.

Niet meer rood: Meta Ads toegang. De directe Pipeboard route werkt weer sinds de reset van de weeklimiet op maandag. Houd het aantal calls per run laag (campagne-niveau plus één ad-niveau call), anders gaat de limiet later in de week weer dicht.

## 6. Top 3 Acties voor Vandaag

1. **Session replay herstellen.** Wat: open Project settings, Session replay, op https://eu.posthog.com/project/149694/settings/environment-replay en controleer of recording aan staat, het sampling-percentage, en de activity log rond 3 september. Draai daarna één testsessie op een SYBB registratiepagina en controleer of die binnen een uur verschijnt. Waarom: drie dagen nul opnames na duizenden per dag, en vertraagde verwerking is nu vrijwel uitgesloten. Zonder replay is niet te zien wat sessie 8 gisteren twee minuten op de registratiepagina deed. Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: kwalitatieve analyse van SYBB bezoeken wordt weer mogelijk. Escalatie: Geel (Robin).
2. **Registratie-voltooid event toevoegen aan de event flow.** Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_complete`) laten vuren op de bevestigingsstap na `/event/*/register`. Waarom: gisteren eindigden 3 echte bezoekers op een registratiepagina en het rapport kan niet zeggen of dat 3 inschrijvingen of 3 afhakers zijn. De proxy (1 accountregistratie en 2 bestellingen in 37 SYBB sessies deze week) is geen bewijs van workshopinschrijvingen. Hoe: Odoo website-ontwikkelaar laat het event vuren op de bedankpagina van de event-inschrijving, of via een PostHog action op de bevestigings-URL zodra die bekend is. Verwachte impact: het dagelijkse rapport krijgt een echte conversie-KPI. Escalatie: Oranje (ontwikkelaar nodig).
3. **Gedeelde registratie-links UTM-taggen.** Wat: vervang de kale links naar `professional-4` (Frans), `professionell-8` (Duits), `professional-english-2` en `professional-9` in nieuwsbrief, Instagram bio, WhatsApp en DM's door UTM-getagde versies via `/utm-generate` (bijvoorbeeld `utm_source=whatsapp` of `utm_source=newsletter`, `utm_campaign=sybb`). Waarom: 10 van de 17 SYBB sessies in drie dagen zijn directe hits zonder bron, en ook de echte bezoeker van sessie 8 kwam via een onbekende directe link. Hoe: handmatig, 20 minuten. Verwachte impact: bots en echte bezoekers worden per bron scheidbaar en de bounce rate van de SYBB funnel wordt weer een bruikbare maat. Escalatie: Groen.

Kleinere opvolging: controleer of proballoonshop.co.uk een partner of klant is die naar sempertexeurope.com linkt. De bezoeker van sessie 3 combineerde calculator, distributeurspagina en SYBB registratie, precies het profiel dat de wholesaler campagne en SYBB allebei zoeken.

---

**Databronnen:** Meta Ads live via de directe Pipeboard JSON-RPC route (MCP servers vragen autorisatie in deze niet-interactieve sessie); campagne-niveau insights voor 6 september, 30 augustus t/m 5 september en 8 augustus t/m 6 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405). Periode gisteren = 6 september 2026 UTC, 7d = 30 augustus t/m 5 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
