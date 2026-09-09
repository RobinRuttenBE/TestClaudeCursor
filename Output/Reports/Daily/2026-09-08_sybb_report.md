# SYBB Daily Report: 8 september 2026

## 1. Samenvatting
Meta Ads campagne `2026: SYBB` staat nog steeds op PAUSED (sinds 19 april 2026, 142 dagen) en had gisteren, in de 7 dagen ervoor en in de hele periode nul spend, nul impressies en nul clicks. De landing page startyourballoonbusiness.com kreeg voor de elfde dag op rij 0 bezoekers. De werkelijke SYBB funnel op sempertexeurope.com had gisteren 2 bezoekers in 3 sessies, de laagste dag van de week, allebei echte mensen op mobiel. De belangrijkste gebeurtenis: voor de tweede dag op rij brak een bezoeker de inschrijving af met hetzelfde patroon, klik op "Registreer" en tien seconden later op "Afsluiten". Dat is nu twee keer in twee dagen op twee verschillende event pagina's en twee verschillende devices, en er is geen session replay van (vijfde dag op nul). Het registratieformulier is daarmee de meest waarschijnlijke oorzaak van verlies in de enige converterende SYBB funnel.

## 2. Meta Ads Performance

**Status data:** live opgehaald via de directe Pipeboard JSON-RPC route. De `pipeboard-meta-ads` en `claude.ai Pipeboard Meta Ads` MCP servers vragen in deze niet-interactieve sessie om autorisatie, maar de geconfigureerde token werkt direct. Ad account `act_567892422940728`.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Kopie `2026: SYBB - Kopie` (ID 120243293329420239) ook PAUSED. Alle 7 campagnes in het ad account staan op PAUSED. Een insights-call op ad-niveau voor het hele account gaf voor 8 september een lege dataset, dus er liep gisteren geen enkele advertentie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: van 1 t/m 8 september kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`. Ook het organische verkeer vanuit Facebook en Instagram is opgedroogd: 166, 145 en 188 pageviews op 1 t/m 3 september, 47 op 4 september, 5 op 6 september en 0 op 7 en 8 september. Geen van die social pageviews raakte een SYBB pagina.

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

Toelichting: ⚪ = geen data. De laatste pageviews op dit domein waren de twee interne testhits van 28 augustus. Van 29 augustus t/m 8 september is er op dit domein geen enkel event geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (8 sep) | 7d Gemiddelde (1 t/m 7 sep) | Trend |
|--------|------------------|------------------------------|-------|
| Bezoekers | 2 | 5,3 | ↓ (-62%) |
| Sessies | 3 | 6,1 | ↓ (-51%) |
| Pageviews SYBB pagina's | 3 | 7,4 | ↓ (-60%) |
| Sessieduur (sessies die een SYBB pagina raken) | gemiddeld 34s, mediaan 33s | gemiddeld 651s, dagmedianen 0s tot 397s | ↓ |
| Bounce rate (zelfde sessies) | 0% (0 van 3) | 28% (12 van 43) | ↓ (goed) |
| Sessies van 0 seconden (bot-patroon) | 0 van 3 | 12 van 43 (28%) | ↓ (goed) |
| Meta-verkeer (utm_source=meta) | 0 sessies | 0 sessies | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 sinds 4 sep | → |

Het 7-daags gemiddelde van de sessieduur wordt sterk opgetrokken door enkele zeer lange sessies op 2 en 5 september, dus de daling in duur is deels een artefact. Wel echt: gisteren waren alle drie de sessies kort (23s, 33s, 46s), en geen enkele bezoeker las de registratiepagina langer dan een minuut.

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /event/start-your-balloon-business-professional-7/register | 2 | 1 |
| /event/start-your-balloon-business-professional-9/register | 1 | 1 |

De drie sessies van gisteren (twee personen):

| Sessie | Tijd (UTC) | Herkomst | Land / device | Instap | Duur | Pagina's | Wat gebeurde er |
|--------|------------|----------|---------------|--------|------|----------|-----------------|
| 1 | 18:30 | Google | NL, Mobile Safari | /events | 23s | 2 | Accepteerde alle cookies, klikte binnen 18 seconden op "Start your Balloon Business - Professional" in het eventoverzicht en landde op professional-7/register. Geen klik op de pagina zelf. |
| 2 | 19:16 | Zelfde persoon als sessie 1 | NL, Mobile Safari | / | 33s | 3 | Begint met een pageleave van de registratiepagina, die dus 46 minuten open heeft gestaan op de telefoon. Ging daarna naar de homepage, klikte op "Latex Onbedrukt" en bekeek de shopcategorie. Geen terugkeer naar de workshop. |
| 3 | 21:59 | Intern (sempertexeurope.com) | BE, Mobile Safari | /event/start-your-balloon-business-professional-9/register | 46s | 1 | Landde rond middernacht lokale tijd direct op de registratiepagina van professional-9, klikte na 36 seconden op "Registreer" en 10 seconden later op "Afsluiten". Sessie eindigde daar. |

Alle drie hebben `$pageleave`, `$autocapture` en `$web_vitals`. Geen bot-patroon.

Twee observaties:

- **Sessie 3 is een herhaling van sessie 2 van 7 september.** Toen: desktop Chrome, professional-8, tweemaal "Registreer", één klik in het formulier, "Afsluiten" na 22 seconden. Gisteren: Mobile Safari, professional-9, eenmaal "Registreer", "Afsluiten" na 10 seconden. Twee verschillende personen, devices en eventpagina's, hetzelfde eindresultaat. Het formulier zelf, of wat er direct na "Registreer" verschijnt, stoot bezoekers af.
- **Sessie 1 en 2 zijn één persoon die van de workshop naar de webshop overstapte.** Deze bezoeker zocht via Google, koos bewust de Professional workshop, liet de registratiepagina 46 minuten open en ging daarna ballonnen bekijken in plaats van in te schrijven. Interesse is er, de registratiepagina overtuigde niet.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren:
SYBB registratiepagina bekeken (2 bezoekers, 100%) → klik op "Registreer" (1, 50%) → formulier gesloten met "Afsluiten" (1, 100% van de starters) → registratie voltooid (niet meetbaar, 0 proxy-signalen)

Conversie-proxy (sessies met een SYBB pagina die ook een Odoo account-registratie of webshop bestelling afronden; geen harde workshop-conversie):

| Periode | SYBB sessies | Met account-registratie voltooid | Met webshop bestelling | Eindigde op SYBB pagina |
|---------|--------------|----------------------------------|------------------------|-------------------------|
| Gisteren | 3 | 0 | 0 | 2 (67%) |
| 1 t/m 7 sep | 43 | 1 | 1 | 27 (63%) |

**Grootste lek:** de stap na de klik op "Registreer". In twee dagen zijn er drie klikken op "Registreer" geweest (twee op 7 september, één gisteren) door twee verschillende bezoekers, en beide bezoekers sloten het formulier binnen 22 seconden. Er is geen enkel signaal dat iemand het formulier daadwerkelijk heeft ingevuld. Zonder replay en zonder formulier-events blijft de oorzaak gissen: een verplichte login, een prijs die pas in het formulier verschijnt, verplichte velden die op mobiel niet werken, of een popup die op mobiel Safari niet goed rendert.

## 5. Rode Vlaggen 🚩

- **Tweede afgebroken inschrijving in twee dagen, zelfde patroon.** "Registreer" gevolgd door "Afsluiten" binnen 10 seconden, op mobiel Safari, op professional-9. Op 7 september hetzelfde op desktop Chrome, professional-8. Dit is geen toeval meer, dit is een formulierprobleem of een prijsschok.
- **Session replay staat nu vijf dagen op nul.** Opnames per dag: 30 aug 303, 31 aug 2.264, 1 sep 3.876, 2 sep 1.558, 3 sep 92, 4 t/m 8 sep 0. Twee afgebroken inschrijvingen zonder één opname.
- **Laagste SYBB volume van de week.** 2 bezoekers tegenover 5,3 gemiddeld. Organisch social verkeer naar de site (Facebook en Instagram referrals) zakte van 188 pageviews op 3 september naar 0 op 7 en 8 september. Alles hangt nu aan Google en directe links.
- **Structureel, ongewijzigd:** geen registratie-voltooid event, geen scroll- en CTA-events op de landing page, SYBB campagne 142 dagen gepauzeerd, landing page 11 dagen op 0 bezoekers.
- **Site-brede verkeerspiek ebt weg, botverkeer niet.** 560 unieke bezoekers gisteren (923 op 7 september, 7d gemiddelde 6.214), maar nog 6.876 pageviews. Ruim 12 pageviews per bezoeker is een crawler-signatuur. Het SYBB verkeer zelf was gisteren botvrij.

Niet rood: bounce rate en 0-seconden sessies op SYBB pagina's waren gisteren allebei 0 van 3.

## 6. Top 3 Acties voor Vandaag

1. **Doorloop zelf het registratieformulier op mobiel Safari, vandaag.** Wat: open op een iPhone in Safari /event/start-your-balloon-business-professional-9/register, klik "Registreer" en noteer exact wat er verschijnt: een login-eis, een prijs, verplichte velden, een popup die niet past op het scherm, of een foutmelding. Doe hetzelfde op professional-7 en professional-8. Waarom: twee bezoekers in twee dagen sloten het formulier binnen 22 seconden na "Registreer", gisteren op mobiel Safari, de dag ervoor op desktop Chrome. Hoe: handmatig, 10 minuten, geen ontwikkelaar nodig. Verwachte impact: directe bevestiging of uitsluiting van een technisch of prijs-lek in de enige converterende SYBB stap. Escalatie: Groen.
2. **Maak in PostHog twee actions aan op de bestaande autocapture-events: `sybb_registration_start` (klik op "Registreer" op een /event/start-your-balloon-business* pagina) en `sybb_registration_abandon` (klik op "Afsluiten" op dezelfde pagina's).** Wat: Data management, Actions, nieuwe action op basis van element text plus URL-filter. Waarom: autocapture vangt beide klikken al, dus zonder code krijgt het rapport vanaf morgen een start- en afbreek-KPI in plaats van handmatig sessies uitpluizen. Hoe: handmatig in PostHog, 15 minuten. Verwachte impact: dagelijkse start- en afbreekratio, en een trendlijn zodra het formulier wordt aangepast. Escalatie: Groen.
3. **Session replay herstellen.** Wat: open Project settings, Session replay, op https://eu.posthog.com/project/149694/settings/environment-replay en controleer of recording aan staat, het sampling-percentage, en de activity log rond 3 september. Draai daarna één testsessie op professional-9/register, klik op "Registreer" en controleer of de opname binnen een uur verschijnt. Waarom: vijf dagen nul opnames en twee afgebroken inschrijvingen waarvan niemand kan zien wat er misging. Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: de volgende afgebroken inschrijving is wel te analyseren. Escalatie: Geel (Robin).

Blijft staan van eerdere rapporten: een registratie-voltooid event in de Odoo event flow (Oranje, ontwikkelaar). Zolang dat ontbreekt levert dit rapport alleen volume en afbrekingen, geen conversie.

---

**Databronnen:** Meta Ads live via de directe Pipeboard JSON-RPC route (MCP servers vragen autorisatie in deze niet-interactieve sessie); campagne-lijst, campagne-niveau insights voor 8 september en 1 t/m 7 september, plus één ad-niveau call op account-niveau voor 8 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405). Periode gisteren = 8 september 2026 UTC, 7d = 1 t/m 7 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
