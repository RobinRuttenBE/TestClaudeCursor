# SYBB Daily Report: 4 september 2026

## 1. Samenvatting
De SYBB ad campagne staat nog altijd op PAUSED (sinds 19 april 2026) en de landing page startyourballoonbusiness.com kreeg gisteren opnieuw 0 bezoekers. De werkelijke SYBB funnel, de event registratiepagina's op sempertexeurope.com, had gisteren 4 bezoekers in 4 sessies, tegenover een 7-daags gemiddelde van 4,9 bezoekers per dag. Dat is een normale stille dag, maar de kwaliteit was slecht: 3 van de 4 sessies waren directe single-page bezoeken van 0 seconden op Engelstalige registratiepagina's, allemaal bounces. Alleen een Duitse bezoeker bekeek de workshop echt, via de event listing. Conversie blijft onmeetbaar omdat er nog steeds geen registratie-voltooid event bestaat. Nieuw signaal: session replay heeft de hele week nul opnames vastgelegd, terwijl het product wel aan staat.

## 2. Meta Ads Performance

**Campagne status:** `2026: SYBB` (ID 120239435987290239) staat op **PAUSED**, laatst gewijzigd 19 april 2026. De kopie `2026: SYBB - Kopie` (ID 120243293329420239) staat ook op PAUSED (laatst gewijzigd 27 augustus). Beide leverden over 28 augustus t/m 4 september nul impressies en nul spend. De twee wholesaler lead-campagnes (LIT en SWE) in het ad account (act_567892422940728) zijn gisteren om 11:50 ook gepauzeerd. Daarmee draait er sinds gisteren geen enkele campagne meer in het account. Zie het ads-rapport van 5 september voor de eindafrekening van de wholesaler campagnes.

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
| Bezoekers | 0 | 2 (beide op 28 aug) | n.v.t. | ⚪ |
| Pageviews | 0 | 2 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = onvoldoende data om een target te beoordelen. De enige 2 pageviews in het 7-daags venster dateren van 28 augustus: één via manage.wix.com en één test-URL met `utm_source=meta`, `utm_campaign=sybb`, `utm_content=h11_b3_cta5`. Dat zijn interne tests, geen publiek verkeer. Scroll- en CTA-events bestaan niet in het PostHog project. Geen rage clicks, geen session recordings.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (4 sep) | 7d Gemiddelde (28 aug t/m 3 sep) | Trend |
|--------|------------------|----------------------------------|-------|
| Bezoekers | 4 | 4,9 | ↓ (-18%) |
| Sessies | 4 | 5,1 | ↓ (-22%) |
| Pageviews | 5 | 16,3 (9,3 zonder de uitschieter van 31 aug) | ↓ |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 17s, mediaan 0s | gemiddeld 536s | ↓ (-97%) |
| Bounce rate (zelfde sessies) | 75% (3 van 4) | 5% (2 van 44) | ↑ |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 | → |

Bezoekers per taalversie gisteren: 3 Engels (en_GB), 1 Duits, 0 Frans, 0 Nederlands. In de 7 dagen ervoor was Nederlands juist de grootste groep (23 van 34 bezoekers).

De vier sessies van gisteren:

| Sessie | Tijd (UTC) | Herkomst | Instap | Duur | Pagina's | SYBB pagina's bekeken |
|--------|------------|----------|--------|------|----------|-----------------------|
| 1 | 13:10 | Direct | /en_GB/event/.../professional-english-2/register | 0s | 1 | professional-english-2 (bounce) |
| 2 | 13:44 | Site navigatie (sempertexeurope.com) | /de/shop/category/latex-ballons-fashion-solid-raspberry | 68s | 8 | /de/.../professionell-7/register en /de/.../professional-48/register, via de event listing en de MBP Prüfung pagina |
| 3 | 13:48 | Direct | /en_GB/event/.../professional-4/register | 0s | 1 | professional-4 (bounce) |
| 4 | 17:51 | Direct | /en_GB/event/.../professional-english-2/register | 0s | 1 | professional-english-2 (bounce) |

Drie sessies landden direct op een Engelstalige registratie-URL zonder referrer en verlieten meteen. Zo'n patroon past bij een link die gedeeld is via e-mail, WhatsApp of een Instagram bio, of bij een link-preview bot. Zonder UTM's is de bron niet te herleiden. De vierde sessie was een echte oriënterende bezoeker uit Duitsland die twee SYBB edities vergeleek naast de MBP Prüfung.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren:
SYBB registratiepagina bekeken (4 bezoekers, 100%) → langer dan 0s op de pagina (1, 25%) → tweede SYBB pagina bekeken (1, 25%) → registratie voltooid (niet meetbaar)

Conversie-proxy (sessies met een SYBB pagina die ook een Odoo account-registratie of webshop bestelling afronden, per memory geen harde workshop-conversie):

| Periode | SYBB sessies | Met account-registratie voltooid | Met webshop bestelling |
|---------|--------------|----------------------------------|------------------------|
| Gisteren | 4 | 0 | 0 |
| 28 aug t/m 3 sep | 42 | 2 | 1 |

**Grootste lek:** de instap zelf. 3 van de 4 bezoekers verlieten de registratiepagina binnen 0 seconden. Op dagen met echt verkeer (28 aug t/m 3 sep) was de bounce rate 5%, dus dit is een bron-probleem, geen pagina-probleem. De structurele lek blijft het ontbrekende meetpunt na de registratiepagina.

## 5. Rode Vlaggen 🚩

- **Session replay legt niets vast.** 0 opnames op 4 september en 0 opnames over de volledige periode 28 augustus t/m 4 september, terwijl session replay in het project aan staat en de site 4.106 bezoekers had gisteren. Dat wijst op een uitgeschakelde of geblokkeerde replay-configuratie (sampling op 0%, consent-blokkade, of domein-filter). Zonder replays is kwalitatieve analyse van SYBB sessies onmogelijk.
- **Bounce rate 75% op SYBB sessies** (3 van 4). Boven de 70% drempel, maar met n=4 en alle drie via directe links zonder UTM. Behandelen als bron-signaal, niet als pagina-signaal.
- **Onherleidbaar direct verkeer op Engelse registratiepagina's.** Drie directe hits op `professional-english-2` en `professional-4` zonder UTM's. Als deze links ergens actief gedeeld worden (nieuwsbrief, Instagram bio, WhatsApp), lekt de attributie.
- **Rage clicks op de accountregistratie.** Site-breed 54 rage clicks gisteren, met `/registratie` (6 clicks, 2 personen) en `/fr/registratie` (3 clicks) bovenaan. Dat is de Odoo klantaccount-flow, geen SYBB pagina, maar de hypothese uit eerdere rapporten is dat een workshopinschrijving een klantaccount vereist. Frictie daar raakt de SYBB funnel indirect.
- **Site-brede verkeerspiek blijft aan.** 4.106 bezoekers gisteren tegenover een baseline van 300 tot 500 vóór 31 augustus (piek 13.686 op 1 september). SYBB pagina's zien hier niets van terug, dus het lijkt geen campagneverkeer. Valt buiten dit rapport, maar vertekent alle site-brede ratio's.
- **Structureel:** geen registratie-voltooid event, geen scroll- en CTA-events op de landing page, SYBB campagne al 138 dagen gepauzeerd. Ongewijzigd sinds vorige rapporten.

## 6. Top 3 Acties voor Vandaag

1. **Session replay controleren in PostHog.** Wat: open Project settings → Session replay en controleer of recording aan staat, wat het sampling-percentage is en of er een URL- of consent-trigger is die sempertexeurope.com blokkeert. Waarom: 0 opnames in 8 dagen bij duizenden bezoekers is geen toeval. Hoe: handmatig in PostHog (https://eu.posthog.com/project/149694/settings/environment-replay), daarna één testsessie op een SYBB registratiepagina draaien en checken of die verschijnt. Verwachte impact: kwalitatieve inzichten in SYBB bezoekgedrag worden weer mogelijk. Escalatie: Geel (Robin doet dit zelf, 10 minuten).
2. **Bron van de directe Engelse registratie-links achterhalen.** Wat: controleer of de URL's `/en_GB/event/start-your-balloon-business-professional-english-2/register` en `/en_GB/event/start-your-balloon-business-professional-4/register` recent gedeeld zijn in een nieuwsbrief, Instagram bio of story, of in DM's. Waarom: 3 van 4 SYBB bezoekers gisteren kwamen via die directe links en bounceden op 0s, wat ook op link-preview bots kan wijzen. Hoe: check Brevo campagnes en de Instagram bio-link handmatig, vervang gedeelde links door UTM-getagde versies via `/utm-generate`. Verwachte impact: attributie van SYBB verkeer klopt weer en bot-hits zijn te scheiden van echte bezoekers. Escalatie: Geel.
3. **Registratie-voltooid event toevoegen aan de event flow.** Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_complete`) laten vuren op de bevestigingsstap na `/event/*/register`. Waarom: dit is de derde dag op rij dat het rapport alleen volume kan tonen en geen conversie. De 2 account-registraties en 1 bestelling in SYBB sessies deze week zijn een proxy, geen bewijs. Hoe: Odoo website-ontwikkelaar laat het event vuren op de bedankpagina van de event-inschrijving, of via een PostHog action op de bevestigings-URL zodra die bekend is. Verwachte impact: het dagelijkse rapport krijgt een echte conversie-KPI. Escalatie: Oranje (ontwikkelaar nodig).

---

**Databronnen:** Meta Ads via Pipeboard (directe JSON-RPC, MCP meldde "requires authentication"), PostHog project STX EU (149694) via de claude.ai PostHog connector met HogQL. Periode gisteren = 4 september 2026 UTC, 7d = 28 augustus t/m 3 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
