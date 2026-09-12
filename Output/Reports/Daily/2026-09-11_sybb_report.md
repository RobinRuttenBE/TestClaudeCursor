# SYBB Daily Report: 11 september 2026

## 1. Samenvatting
Gisteren was de stilste SYBB dag van de week: nul echte bezoekers op de workshoppagina's. De drie sessies die PostHog telt zijn twee link-preview bots op de nieuwe Engelse eventpagina professional-48 en het sluiten van de tab van de afbreker van 10 september. De Meta campagne `2026: SYBB` staat nog steeds op PAUSED (sinds 19 april, 145 dagen), de landing page startyourballoonbusiness.com staat voor de veertiende dag op 0 bezoekers en session replay staat voor de achtste dag op nul opnames. Meta-cijfers zijn vandaag niet live op te halen: Pipeboard zit op de weeklimiet van het gratis plan tot maandag 14 september. De campagnestatus is vanochtend wel nog live bevestigd in het ads-rapport (alle 7 campagnes PAUSED), en PostHog bevestigt onafhankelijk dat er geen enkele Meta-pageview binnenkwam. Site-breed was gisteren opnieuw een crawlergolf: 6.970 sessies, waarvan 89% een directe sessie van 0 seconden met één pageview.

## 2. Meta Ads Performance

**Status data:** niet live. De Pipeboard route (MCP en directe JSON-RPC) geeft `weekly_limit_exceeded`: 100 van 30 wekelijkse tool-executies gebruikt, reset 14 september 00:00 UTC. De drie dagelijkse rapporten (ads-report, auto-optimize, SYBB) hebben de limiet vanochtend al opgebruikt. Onderstaande cijfers komen uit het 30d-extract van 11 september (leeg voor 13 augustus t/m 11 september) en de live campagnelijst uit het ads-rapport van vanochtend.

**Campagne status:** `2026: SYBB` (ID 120239435987290239) op **PAUSED** sinds 19 april 2026. Alle 7 campagnes in ad account `act_567892422940728` staan op PAUSED, de twee Wholesaler campagnes sinds 4 september. Er liep gisteren geen enkele advertentie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

PostHog bevestigt dit onafhankelijk: van 4 t/m 11 september kwam er op de hele site geen enkele pageview binnen met `utm_source=meta`. Social referrals (Facebook en Instagram) gisteren: 0 pageviews, in de 7 dagen ervoor 58 in totaal, waarvan 47 op 4 september.

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

Toelichting: ⚪ = geen data. Van 29 augustus t/m 11 september is er op dit domein geen enkel event geregistreerd. Scroll- en CTA-events bestaan niet in het project.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (11 sep) | 7d Gemiddelde (4 t/m 10 sep) | Trend |
|--------|-------------------|------------------------------|-------|
| Sessies (sessions-tabel) | 3 | 4,4 | ↓ |
| Echte sessies (duur >0s) | 0 | 2,9 | ↓ |
| Pageviews SYBB pagina's | 2 | 5,3 | ↓ |
| Bezoekers | 2 (beide bot) | 4,3 | ↓ |
| Sessieduur echte sessies | n.v.t. | gemiddeld 739s, mediaan 154s | n.v.t. |
| Bounce rate (alle SYBB sessies) | 100% | 35% (11 van 31) | ↑ (bots) |
| Sessies van 0 seconden (bot-patroon) | 3 van 3 | 11 van 31 (35%) | ↑ |
| Klik op "Registreer" of "Register" | 0 | 4 in 7 dagen | ↓ |
| Betaald (/shop/confirmation in SYBB sessie) | 0 | 1 (9 sep) | → |
| Meta-verkeer (utm_source=meta) | 0 | 0 | → |
| Rage clicks of dead clicks op SYBB pagina's | 0 | 0 | → |
| Session recordings van SYBB sessies | 0 | 0 sinds 4 sep | → |

Bekeken SYBB pagina's gisteren:

| Pagina | Pageviews | Bezoekers |
|--------|-----------|-----------|
| /en_GB/event/start-your-balloon-business-professional-48/register | 2 | 2 |

De drie sessies van gisteren (tijden UTC, lokale tijd is +2 uur):

| Sessie | Tijd | Herkomst | Land / device | Pagina | Duur | Events | Wat gebeurde er |
|--------|------|----------|---------------|--------|------|--------|-----------------|
| 1 | 06:16 | Direct | IT, Chrome iOS | /en_GB/professional-48/register | 0s | 1 pageview | Geen pageleave, autocapture of web vitals. Persoon heeft in het hele project maar één event. Link-preview bot op een gedeelde URL. |
| 2 | 07:33 | n.v.t. | NL, Mobile Safari | /professional-9/register | 0s | 1 pageleave | Geen nieuw bezoek. Dit is dezelfde persoon als de afbreker van 10 september (sessie 6 in dat rapport) die om 09:33 lokale tijd de tab sloot die sinds 01:30 openstond, in de deelnemerstap van het ticketvenster. De persoon kwam daarna niet terug. |
| 3 | 19:51 | Direct | DE, Chrome mobiel | /en_GB/professional-48/register | 0s | 1 pageview | Zelfde bot-patroon als sessie 1. Ook deze persoon heeft maar één event ooit. |

Twee observaties:

- **De Engelse pagina van event professional-48 wordt sinds gisteren ergens gedeeld.** Event 48 bestond in PostHog alleen als Duitse variant (bekeken door een Duitse klant op 10 september, en via de site-navigatie op 31 augustus en 4 september). Gisteren kwamen de eerste twee directe hits op de en_GB URL binnen, allebei bots uit Italië en Duitsland. Iemand heeft de link gedeeld, vermoedelijk in WhatsApp, Messenger of een e-mail, en de ontvangers hebben nog niet geklikt. Als dat een interne deel-actie was (bijvoorbeeld een uitnodiging voor de nieuwe datum), is het goed om te weten dat alleen de previews geteld zijn.
- **De afbreker van 10 september is definitief weg.** De tab ging na 8 uur dicht zonder betaling en er was gisteren geen tweede poging. Omdat de bezoeker anoniem was, is er geen manier om deze persoon te bereiken.

## 4. Funnel Drop-off

Landing page funnel (startyourballoonbusiness.com):
Pageview (0) → Scroll 50% (geen event) → CTA click (geen event) → /booking (0)

Event funnel (sempertexeurope.com), gisteren, alleen echte bezoekers:
SYBB registratiepagina bekeken (0) → klik op "Registreer" (0) → ticket bevestigd (0) → "Naar betaling" (0) → /shop/confirmation (0)

Event funnel, 4 t/m 10 september (7 dagen):
SYBB registratiepagina bekeken (20 echte sessies, 100%) → klik op "Registreer" of "Register" (4 sessies, 20%) → ticket bevestigd (3, 75% van de starters) → "Go to Payment" (1, 33% van de bevestigers) → /shop/confirmation (1, 100% van de betalers)

Inschrijfpogingen per dag:

| Dag | Klik "Registreer" (sessies) | "Afsluiten" | Ticket bevestigd | "Go to Payment" | Betaald | Uitkomst |
|-----|------------------------------|-------------|------------------|-----------------|---------|----------|
| 7 sep | 1 (desktop Chrome, professional-8) | 1 | 1 | 0 | 0 | afgebroken na 22s |
| 8 sep | 1 (Mobile Safari, professional-9) | 1 | 0 | 0 | 0 | afgebroken na 10s |
| 9 sep | 1 (Chrome, BE, ingelogd, en_GB professional-8) | 0 | 1 | 1 | 1 | **betaald via Bancontact** |
| 10 sep | 1 (Mobile Safari, professional-9) | 0 | 1 | 0 | 0 | deelnemerstap, tab 8 uur open, gisteren 09:33 gesloten |
| 11 sep | 0 | 0 | 0 | 0 | 0 | geen echte bezoekers |

**Grootste lek:** ongewijzigd, de stap na "Registreer". Van vier pogingen in de afgelopen week rondde alleen de ingelogde bestaande klant af. Gisteren kwam er geen nieuwe datapunt bij, dus de hypothese uit het vorige rapport staat nog open: de deelnemerstap vraagt anonieme bezoekers waarschijnlijk om een account, te veel velden, of toont daar pas de prijs. Nul opnames maken het onmogelijk om dit uit de data te halen.

Conversie-proxy (sessies met een SYBB pagina):

| Periode | SYBB sessies | Echte sessies | Betaald (/shop/confirmation) | Eindigde op SYBB pagina |
|---------|--------------|---------------|------------------------------|-------------------------|
| Gisteren | 3 | 0 | 0 | 3 (allemaal bot of tab-sluiting) |
| 4 t/m 10 sep | 31 | 20 | 1 | 21 (68%) |

Warme pool (laatste 30 dagen, 12 augustus t/m 11 september): 128 personen bekeken een SYBB registratiepagina, 10 daarvan op meer dan één dag en 3 op drie of meer dagen. Dat is de retargeting-doelgroep zodra de campagne herstart.

## 5. Rode Vlaggen 🚩

- **Nul echte SYBB bezoekers gisteren.** Eerste dag sinds 4 september zonder een mens op een workshoppagina. Het 7-daags gemiddelde van 2,9 echte sessies per dag laat zien hoe dun het organische verkeer is zonder advertenties; één stille dag zet de funnel direct op nul.
- **Meta-data niet bereikbaar tot maandag.** Pipeboard weeklimiet: 100 van 30 executies gebruikt, reset 14 september. Drie dagelijkse rapporten die elk drie tot vier calls doen, branden de limiet in twee dagen op. Zolang alles op PAUSED staat is dit geen risico voor het budget, maar bij een herstart moet er een oplossing zijn (zie actie 3).
- **Session replay staat nu acht dagen op nul.** Opnames per dag: 3 september 92, 4 t/m 11 september 0. Vier inschrijfpogingen in de afgelopen week zonder één opname.
- **Crawlergolf site-breed.** Gisteren 10.515 pageviews van 6.840 bezoekers in 6.970 sessies; 6.234 sessies (89%) zijn direct, 0 seconden en één pageview. Zelfde patroon als 5 en 6 september. Dit vervuilt elk site-breed cijfer (bounce rate, bezoekers) in PostHog en Web Analytics; de SYBB-cijfers hierboven zijn er niet door geraakt omdat die per sessie zijn gefilterd.
- **Structureel, ongewijzigd:** SYBB campagne 145 dagen gepauzeerd, landing page 14 dagen op 0 bezoekers, geen scroll- en CTA-events, geen Meta-verkeer, social referrals op 0.
- **Link-preview bots raken nu ook professional-48 (en_GB).** Twee van drie sessies gisteren. Iemand deelt deze URL sinds gisteren.

Niet rood: rage en dead clicks (0), en de 7d bounce rate van echte SYBB sessies (mediaan sessieduur 154s).

## 6. Top 3 Acties voor Vandaag

1. **Doorloop zelf de deelnemerstap van het registratieformulier op mobiel Safari, als uitgelogde bezoeker.** Wat: open in een privévenster op een iPhone /event/start-your-balloon-business-professional-9/register, klik "Registreer", zet het aantal op 1, klik "Registreer" in het venster en noteer exact wat er verschijnt: een login-eis, verplichte velden (bedrijfsnaam, btw-nummer?), de prijs, een venster dat niet in het scherm past, of een foutmelding. Doe hetzelfde ingelogd. Waarom: dit stond gisteren al op één en is nog niet gebeurd; drie van vier pogingen deze week strandden hier of één stap eerder, en de afbreker van 10 september is nu definitief weg. Hoe: handmatig, 10 minuten. Verwachte impact: bevestiging of uitsluiting van een account-eis of formulierprobleem in de enige converterende SYBB stap. Escalatie: Groen.
2. **Session replay herstellen en direct testen.** Wat: open https://eu.posthog.com/project/149694/settings/environment-replay, controleer of recording aan staat, het sampling-percentage, en de activity log rond 3 september (de laatste dag met opnames). Combineer dit met actie 1: doe de testsessie op professional-9 en controleer binnen een uur of de opname verschijnt. Waarom: acht dagen nul opnames; zonder replay is elke volgende afbreker opnieuw onverklaarbaar. Hoe: handmatig in PostHog, 10 minuten. Verwachte impact: de eerstvolgende inschrijfpoging is wel te analyseren. Escalatie: Geel (Robin).
3. **Pipeboard-verbruik terugbrengen voor de reset van maandag.** Wat: laat de drie dagelijkse rapporten (ads-report, auto-optimize, SYBB) één gedeelde Meta-call per dag doen en de output in een lokaal bestand cachen (`Output/Reports/Daily/YYYY-MM-DD_sybb_meta_30d.md` bestaat daar al voor), zodat het verbruik van ruim 9 calls per dag naar 1 tot 2 gaat en de limiet van 30 per week een volle week meegaat. Als de campagnes herstarten is een Pro-plan alsnog nodig, want dan is dagelijkse ad-level data onmisbaar. Waarom: de limiet was zaterdagochtend al vol (100 van 30), waardoor dit rapport en het ads-rapport op cijfers van eerder draaien. Hoe: aanpassing in `scripts/morning-report.sh` en de drie skill-instructies, of Pro-upgrade via https://pipeboard.co/pricing. Verwachte impact: live Meta-cijfers in elk rapport, ook op vrijdag en zaterdag. Escalatie: Geel (Robin beslist tussen cachen of upgraden).

Blijft open uit eerdere rapporten: de vier PostHog actions voor de SYBB funnel (`sybb_registration_start`, `sybb_ticket_confirm`, `sybb_go_to_payment`, `sybb_paid`) en het aanpassen van de funneldefinitie in `skills/daily-sybb-report/SKILL.md` van landing page naar event funnel.

---

**Databronnen:** Meta Ads niet live: Pipeboard (MCP en directe JSON-RPC route) op de weeklimiet van het gratis plan (reset 14 september 2026); campagnestatus uit het live ads-rapport van 12 september 09:48 en het 30d-extract van 11 september. PostHog project STX EU (149694) via de REST API met HogQL (de geconfigureerde `posthog` MCP gaf HTTP 405): pageviews, sessies, autocapture-clicks met elements chain, session replay events en persoonshistorie. Periode gisteren = 11 september 2026 UTC, 7d = 4 t/m 10 september 2026. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.
