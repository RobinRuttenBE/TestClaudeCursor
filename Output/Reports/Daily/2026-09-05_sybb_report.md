# SYBB Daily Report: 5 september 2026

## 1. Samenvatting
Meta Ads data was vandaag op geen enkele route bereikbaar (Pipeboard MCP vraagt autorisatie, de directe route zit op de weeklimiet van het gratis plan). De laatst bekende stand blijft ongewijzigd: campagne `2026: SYBB` staat sinds 19 april 2026 op PAUSED, 139 dagen, en de 30-daagse extract van 5 september toonde nul spend. De landing page startyourballoonbusiness.com kreeg gisteren opnieuw 0 bezoekers, net als de hele week ervoor. De werkelijke SYBB funnel op sempertexeurope.com had 5 bezoekers in 5 sessies, exact het 7-daags gemiddelde. De kwaliteit was, net als op 4 september, tweedeling: 3 sessies waren directe single-page hits van 0 seconden zonder enig vervolg-event, 2 sessies waren echte bezoekers via de site die de registratiepagina 4 tot 15 seconden bekeken en terugkeerden naar de eventlijst. Conversie blijft onmeetbaar. Nieuw: session replay heeft na 3 september niets meer vastgelegd, terwijl het van 29 augustus tot 3 september duizenden opnames per dag maakte.

## 2. Meta Ads Performance

**Status data:** niet live opgehaald. De Pipeboard MCP (`claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads`) vraagt om autorisatie in deze niet-interactieve sessie. De directe JSON-RPC route antwoordt met "You have reached the weekly limit for AI tool executions on your Free plan on Pipeboard". Onderstaande cijfers zijn de laatst bekende stand uit de 30-daagse extract van 5 september (periode 6 augustus t/m 5 september) en het rapport van 4 september.

**Campagne status (laatst bekend):** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Kopie `2026: SYBB - Kopie` (ID 120243293329420239) ook PAUSED. Sinds 4 september draait er geen enkele campagne meer in ad account act_567892422940728.

| Metric | Gisteren (laatst bekend) | 7d Gemiddelde | Trend |
|--------|--------------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt de pauze onafhankelijk van Meta: gisteren kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`, voor geen enkele campagne.

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

Toelichting: ⚪ = geen data. Van 29 augustus t/m 5 september is er geen enkele pageview op het domein startyourballoonbusiness.com geregistreerd. De twee interne testhits van 28 augustus vallen buiten dit venster. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (5 sep) | 7d Gemiddelde (29 aug t/m 4 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 5 | 5,0 | → |
| Sessies | 5 | 5,3 | → (-6%) |
| Pageviews SYBB pagina's | 6 | 14,4 (7,2 zonder de uitschieter van 31 aug) | ↓ |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 2.272s, mediaan 0s | gemiddeld 527s | vertekend, zie toelichting |
| Bounce rate (zelfde sessies) | 60% (3 van 5) | 12% (5 van 43) | ↑ |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | onbekend, zie rode vlaggen | → |

Het gemiddelde van 2.272s wordt volledig gedragen door één sessie van 8.963s (2,5 uur) waarin de bezoeker de tab waarschijnlijk open liet staan. De mediaan van 0s is de eerlijke maat.

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /event/start-your-balloon-business-professional-8/register | 2 | 2 |
| /event/start-your-balloon-business-professional-7/register | 1 | 1 |
| /en_GB/event/start-your-balloon-business-professional-4/register | 1 | 1 |
| /fr/event/start-your-balloon-business-professional-4/register | 1 | 1 |
| /fr/event/start-your-balloon-business-professionnel-8/register | 1 | 1 |

De vijf sessies van gisteren:

| Sessie | Tijd (UTC) | Herkomst | Land / device | Instap | Duur | Pagina's | Wat gebeurde er |
|--------|------------|----------|---------------|--------|------|----------|-----------------|
| 1 | 04:53 | Direct | DE, Chrome mobiel | /fr/.../professional-4/register | 0s | 1 | Bounce. Alleen een pageview, geen pageleave, geen autocapture. |
| 2 | 08:30 | Direct | JP, Chrome mobiel | /fr/.../professionnel-8/register | 0s | 1 | Bounce. Japans IP op een Franse registratiepagina, zelfde leeg eventpatroon. |
| 3 | 14:39 | ntp.msn.com (Edge startpagina) | BE, Edge desktop | / | 2.397s | 19 | Ingelogde klant (/web/login, /my). Via /events naar professional-7 (11s), terug, naar professional-8 (15s), terug, daarna 25 minuten folieballonnen in de shop. Geen bestelling. |
| 4 | 18:19 | Direct | NL, Chrome mobiel | / | 8.963s | 6 | Via /events naar MBP examen 5, terug, naar professional-8 (4s), terug naar /events en gestopt. |
| 5 | 19:17 | Direct | SE, Chrome iOS | /en_GB/.../professional-4/register | 0s | 1 | Bounce. Zelfde leeg patroon als sessie 1 en 2. |

Sessies 1, 2 en 5 hebben alleen een `$pageview` en verder niets: geen `$pageleave`, geen `$autocapture`, geen `$web_vitals`. Sessies 3 en 4 hebben die events wel. Dat verschil is het sterkste bewijs tot nu toe dat de directe 0s-hits geen mensen zijn maar link-preview bots of crawlers die een gedeelde URL openen. De URL `professional-4/register` dook op 4 september ook al zo op.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren:
SYBB registratiepagina bekeken (5 bezoekers, 100%) → langer dan 0s op de pagina (2, 40%) → tweede SYBB pagina bekeken (1, 20%) → registratie voltooid (niet meetbaar)

Conversie-proxy (sessies met een SYBB pagina die ook een Odoo account-registratie of webshop bestelling afronden; geen harde workshop-conversie):

| Periode | SYBB sessies | Met account-registratie voltooid | Met webshop bestelling |
|---------|--------------|----------------------------------|------------------------|
| Gisteren | 5 | 0 | 0 |
| 29 aug t/m 4 sep | 43 | 2 | 1 |

**Grootste lek:** de registratiepagina zelf houdt echte bezoekers niet vast. De twee menselijke bezoekers van gisteren bekeken een SYBB registratiepagina 4, 11 en 15 seconden en klikten telkens terug naar /events. Beiden vergeleken edities (professional-7 versus 8, of SYBB versus MBP examen) en vonden op de pagina blijkbaar niet wat ze zochten om te beslissen. Met n=2 is dit een hypothese, geen conclusie, maar het is hetzelfde patroon als de Duitse bezoeker van 4 september. De structurele lek blijft het ontbrekende meetpunt na de registratiepagina.

## 5. Rode Vlaggen 🚩

- **Meta Ads data onbereikbaar.** MCP vraagt autorisatie, de directe Pipeboard route zit op de weeklimiet van het gratis plan. Dit raakt ook het morning report, het ads-rapport en auto-optimize. Zolang dit niet is opgelost rapporteert elk rapport alleen de stand van 4 september.
- **Session replay is gestopt na 3 september.** Opnames per dag: 29 aug 416, 30 aug 303, 31 aug 2.264, 1 sep 3.876, 2 sep 1.558, 3 sep 92, 4 sep 0, 5 sep 0. Correctie op het rapport van 4 september: dat meldde nul opnames voor 28 augustus t/m 4 september, maar die opnames blijken er nu wel te zijn voor 29 augustus t/m 3 september. Replay-data komt dus met vertraging binnen, of de eerdere query keek verkeerd. Wat vaststaat: de scherpe val op 3 september (92 tegenover 1.558 de dag ervoor bij 6.800 bezoekers) en niets meer daarna. Van de 5 SYBB sessies van gisteren is er geen enkele opgenomen.
- **Bounce rate 60% op SYBB sessies** (3 van 5), gisteren 75% (3 van 4). Onder de 70% drempel maar de tweede dag op rij met dezelfde oorzaak: directe hits zonder referrer, zonder UTM en zonder vervolg-events op `professional-4` en nu ook Franse registratie-URL's. Over twee dagen zijn 6 van de 9 SYBB sessies zo. Dit is verkeer dat ergens buiten de site gedeeld wordt en dat door bots of previews wordt geopend. Attributie lekt zolang die links geen UTM's dragen.
- **Registratiepagina's houden bezoekers 4 tot 15 seconden vast.** Zie sectie 4. Klein signaal, maar consistent over 4 en 5 september.
- **Site-brede verkeerspiek houdt aan.** 7.525 bezoekers gisteren tegenover een baseline van 300 tot 400 vóór 31 augustus. SYBB pagina's zien hier niets van terug (5 van 7.525 bezoekers), dus het is geen campagne- of workshopverkeer. Vertekent alle site-brede ratio's. 86 rage clicks site-breed, geen enkele op SYBB pagina's of op de accountregistratie.
- **Structureel, ongewijzigd:** geen registratie-voltooid event, geen scroll- en CTA-events op de landing page, SYBB campagne 139 dagen gepauzeerd, landing page al 8 dagen op 0 bezoekers.

## 6. Top 3 Acties voor Vandaag

1. **Meta Ads toegang herstellen.** Wat: kies één van drie routes: Pipeboard upgraden naar Pro, in een interactieve sessie `/mcp` draaien en de Pipeboard connector opnieuw autoriseren, of een Meta System User token met `ads_read` in de config zetten als fallback naar de Marketing API. Waarom: zonder Meta-data draaien morning report, ads-rapport, SYBB-rapport en auto-optimize allemaal op cijfers van 4 september. Hoe: handmatig, 10 minuten voor de MCP-route. Verwachte impact: alle dagelijkse rapporten hebben morgen weer live Meta-cijfers. Escalatie: Geel (Robin).
2. **Session replay controleren op de val van 3 september.** Wat: open Project settings → Session replay op https://eu.posthog.com/project/149694/settings/environment-replay en controleer of recording aan staat, het sampling-percentage, en of er op 3 september iets is gewijzigd (activity log). Draai daarna één testsessie op een SYBB registratiepagina en kijk of die verschijnt. Waarom: tot 2 september werden duizenden sessies per dag opgenomen, sinds 4 september nul. Als replay-data alleen vertraagd binnenkomt, is morgen de check: staan er dan opnames voor 4 en 5 september? Hoe: handmatig in PostHog. Verwachte impact: kwalitatieve analyse van SYBB bezoeken wordt weer mogelijk, inclusief de vraag waarom echte bezoekers na 4 tot 15 seconden terugklikken. Escalatie: Geel.
3. **Registratie-voltooid event toevoegen aan de event flow.** Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_complete`) laten vuren op de bevestigingsstap na `/event/*/register`. Waarom: vierde dag op rij dat het rapport alleen volume toont. De proxy (2 accountregistraties en 1 bestelling in 43 SYBB sessies deze week) is geen bewijs van workshopinschrijvingen. Hoe: Odoo website-ontwikkelaar laat het event vuren op de bedankpagina van de event-inschrijving, of via een PostHog action op de bevestigings-URL zodra die bekend is. Verwachte impact: het dagelijkse rapport krijgt een echte conversie-KPI. Escalatie: Oranje (ontwikkelaar nodig).

Kleinere opvolging: vervang de gedeelde registratie-links (`professional-4`, `professional-english-2`, Franse varianten) in nieuwsbrief, Instagram bio en DM's door UTM-getagde versies via `/utm-generate`, zodat bots en echte bezoekers te scheiden zijn.

---

**Databronnen:** Meta Ads niet live bereikbaar (Pipeboard MCP vraagt autorisatie, directe JSON-RPC op weeklimiet); laatst bekende stand uit de 30d extract van 5 september en het rapport van 4 september. PostHog project STX EU (149694) via de claude.ai PostHog connector met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405). Periode gisteren = 5 september 2026 UTC, 7d = 29 augustus t/m 4 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
