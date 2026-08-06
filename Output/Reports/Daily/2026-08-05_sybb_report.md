# SYBB Daily Report, 5 augustus 2026

> Databronnen: PostHog MCP (organisatie "Sempertex Europe", project "STX EU", id 149694).
> Meta Ads MCP (Pipeboard): **niet beschikbaar**, connector is in deze sessie niet geautoriseerd.
> Gegenereerd op 6 augustus 2026. Geen Google MCPs gebruikt, niet weggeschreven naar de Meta Ads Tracker Google Sheet.

## 1. Samenvatting

Op 5 augustus 2026 was er opnieuw **nul SYBB activiteit op de landing page**. startyourballoonbusiness.com kreeg nul pageviews. De laatste bezoeker op die site was op 31 juli 2026. Dit is de vijfde dag op rij met nul verkeer.

De Meta Ads data kon ik niet ophalen, de Pipeboard connector is niet geautoriseerd. PostHog levert wel onafhankelijke bevestiging dat er geen betaald verkeer was: op 5 augustus is er accountbreed geen enkele pageview met `utm_source=meta` of `utm_medium=cpc` binnengekomen. Dat sluit aan op de meting van 4 augustus, waar de campagne `2026: SYBB` op PAUSED stond met nul delivery sinds april.

Er is wel één ding dat de vorige rapporten misten. **De SYBB workshop wordt op dit moment verkocht via sempertexeurope.com, niet via de landing page.** De event registratiepagina's daar trekken in de week van 30 juli tot en met 5 augustus 13 registratie-pageviews van 12 bezoekers. Klein, maar het is de enige SYBB funnel die daadwerkelijk nog draait. Zie sectie 4.

## 2. Meta Ads Performance

**Geen data beschikbaar.** De Pipeboard Meta Ads MCP is in deze sessie niet geautoriseerd, dus campagne-, ad set- en ad-level insights voor `2026: SYBB` konden niet worden opgehaald. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren (5 aug) | 7d gemiddelde | Trend |
|--------|------------------|---------------|-------|
| Spend | geen data | geen data | n.v.t. |
| Impressions | geen data | geen data | n.v.t. |
| Clicks | geen data | geen data | n.v.t. |
| CTR | geen data | geen data | n.v.t. |
| CPC | geen data | geen data | n.v.t. |
| Frequency | geen data | geen data | n.v.t. |

### Indirecte bevestiging via PostHog

PostHog kan de Meta data niet vervangen, maar wel het belangrijkste feit bevestigen: er kwam geen klik binnen.

UTM verkeer op 5 augustus 2026, alle hosts:

| utm_source | utm_medium | utm_campaign | Pageviews | Bezoekers |
|------------|------------|--------------|-----------|-----------|
| mailjet | email | workshop_tobi_promo_202608 | 42 | 34 |
| chatgpt.com | (geen) | (geen) | 7 | 5 |
| Klaviyo | email | (geen) | 3 | 3 |
| mailjet | email | inspiration_promo_202607 | 1 | 1 |
| partner | referral | distributor_evergreen_202607 | 1 | 1 |
| newsletter | email | fr_client | 1 | 1 |

Nul regels met `meta`, `facebook`, `instagram` of `cpc`. Als de campagne had gedraaid, was hier verkeer verschenen. Dat betekent met redelijke zekerheid: campagne nog steeds PAUSED, nul spend, nul clicks op 5 augustus.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | geen data | geen data | geen data | n.v.t. | n.v.t. |
| h12_b3_cta5 | geen data | geen data | geen data | n.v.t. | n.v.t. |
| h13_b3_cta5 | geen data | geen data | geen data | n.v.t. | n.v.t. |
| h14_b3_cta5 | geen data | geen data | geen data | n.v.t. | n.v.t. |
| h15_b3_cta5 | geen data | geen data | geen data | n.v.t. | n.v.t. |

**Beste variant:** niet te bepalen. Meta data ontbreekt, en PostHog registreerde nul sessies met een `utm_content` waarde op de landing page.
**Slechtste variant:** zelfde reden.

### Laatste bekende performance (april 2026)

Ter referentie, overgenomen uit het rapport van 4 augustus toen de Meta connector wel werkte. Dit is **geen verse data**, het is de laatste maand waarin SYBB daadwerkelijk draaide.

| Metric | April 2026 | Target | Status |
|--------|-----------|--------|--------|
| Spend | €1.059,47 | n.v.t. | |
| Impressions | 91.839 | n.v.t. | |
| Clicks | 1.935 | n.v.t. | |
| CTR | 2,11% | n.v.t. | 🟢 |
| CPC | €0,55 | <€0,50 | 🟡 |
| Frequency | 2,19 | <3,0 | 🟢 |
| Landing page views | 818 | n.v.t. | |
| Purchases | 6 | n.v.t. | |
| Kosten per purchase | €176,58 | n.v.t. | 🔴 |

## 3. Landing Page Health

startyourballoonbusiness.com, 5 augustus 2026.

| Metric | Gisteren | 7d gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 0,1 per dag | n.v.t. | 🔴 |
| Unieke bezoekers | 0 | 0,1 per dag | n.v.t. | 🔴 |
| Sessies | 0 | 0,1 per dag | n.v.t. | 🔴 |
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | niet gemeten | niet gemeten | >80% | ⚫ |
| Scroll 50% | niet gemeten | niet gemeten | >60% | ⚫ |
| Scroll 75% | niet gemeten | niet gemeten | >40% | ⚫ |
| Scroll 100% | niet gemeten | niet gemeten | >20% | ⚫ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚫ |

⚪ = niet meetbaar bij nul sessies, niet slecht presterend.
⚫ = het event bestaat niet in de tracking, ook bij verkeer zou dit leeg blijven.

### Traffic historie, laatste 21 dagen

| Datum | Pageviews | Bezoekers |
|-------|-----------|-----------|
| 5 aug | 0 | 0 |
| 4 aug | 0 | 0 |
| 3 aug | 0 | 0 |
| 2 aug | 0 | 0 |
| 1 aug | 0 | 0 |
| 31 jul | 1 | 1 |
| 30 jul | 0 | 0 |
| 29 jul | 1 | 1 |
| 28 jul | 0 | 0 |
| 27 jul | 1 | 1 |
| 26 jul | 0 | 0 |
| 25 jul | 0 | 0 |
| 24 jul | 0 | 0 |
| 23 jul | 1 | 1 |
| 22 jul | 0 | 0 |
| 21 jul | 1 | 1 |
| 20 jul | 6 | 6 |
| 19 jul | 2 | 2 |
| 18 jul | 3 | 3 |
| 17 jul | 1 | 1 |
| 16 jul | 2 | 2 |

Over 60 dagen: 83 pageviews totaal. Het restverkeer droogde eind juli volledig op.

### Tracking status op de landing page

Wat er in 60 dagen op startyourballoonbusiness.com heeft gevuurd:

| Event | Aantal | Laatst gezien |
|-------|--------|---------------|
| `$pageview` | 83 | 31 juli 2026 |
| `$web_vitals` | 68 | 31 juli 2026 |
| `$autocapture` | 20 | 10 juli 2026 |
| `$pageleave` | 12 | 10 juli 2026 |

Twee dingen vallen op. Er zijn **geen custom events** voor scroll milestones, CTA clicks of `/booking` conversies, dus secties 3 en 4 van dit rapport zijn structureel niet te vullen, ook niet bij herstart van de campagne. En `$autocapture` plus `$pageleave` zijn sinds 10 juli stilgevallen terwijl `$pageview` gewoon doorliep tot 31 juli. Dat wijst op een gewijzigde of kapotte PostHog config op de site, geen ontbrekend verkeer.

### Correctie op het ads rapport van 6 augustus

Het rapport van 6 augustus stelt dat startyourballoonbusiness.com "niet wordt gemeten" door PostHog. Dat klopt niet. De pixel staat er en heeft 83 pageviews vastgelegd, de laatste op 31 juli 2026. Het probleem is niet dat de site blind is, het is dat er geen verkeer meer komt en dat de event-tracking te dun is voor de KPI targets.

## 4. Funnel Drop-off

### Funnel A: de bedoelde SYBB funnel (landing page)

Pageview (0) → Scroll 50% (0) → CTA Click (0) → /booking (0)

**Grootste lek:** de funnel start niet. Er is geen instroom, dus geen lek te meten. Het probleem zit bovenstrooms bij een gepauzeerde campagne.

### Funnel B: de SYBB funnel die wél draait (sempertexeurope.com)

De workshop wordt op dit moment via de event pagina's op de hoofdsite verkocht. Dit staat nergens in de skill of in CLAUDE.md beschreven, maar het is waar de SYBB conversies nu vandaan komen.

Pagina's: `/event/start-your-balloon-business-professional-7/register` en `/de/event/start-your-balloon-business-professionell-7/register`.

| Datum | Event pagina views | Register views | Bezoekers |
|-------|--------------------|----------------|-----------|
| 5 aug | 0 | 2 | 2 |
| 4 aug | 1 | 3 | 2 |
| 3 aug | 0 | 3 | 3 |
| 2 aug | 0 | 3 | 2 |
| 1 aug | 1 | 0 | 1 |
| 31 jul | 2 | 2 | 3 |
| 30 jul | 0 | 1 | 1 |
| **Totaal 7d** | **4** | **14** | **12** |

Van die 14 register views over 7 dagen zat er 1 op de interne Odoo omgeving (`rezolvbv-sh-sempertex.odoo.com`), dus 13 op de publieke site.

**Op 5 augustus specifiek:** 2 register views, waarvan 1 intern op Odoo. Er bleef dus één echte bezoeker over. Die kwam direct binnen, bekeek 17 pagina's in één sessie, doorliep meerdere shop categorieën plus de partner- en events pagina, en raakte de SYBB registratiepagina één keer aan. Geen aankoop. Dat is geen ad-funnel, dat is een bestaande klant die rondkijkt.

**Grootste lek in funnel B:** er is vrijwel geen instroom naar de event pagina's. 4 event pagina views tegenover 14 register views over een week betekent dat mensen rechtstreeks op de registratielink landen, waarschijnlijk vanuit e-mail of de events overzichtspagina. De verkooppagina zelf wordt overgeslagen, dus er is geen moment waarop de workshop wordt verkocht voordat om de inschrijving wordt gevraagd.

## 5. Rode Vlaggen 🚩

1. **Meta Ads data ontbreekt volledig.** De Pipeboard connector is niet geautoriseerd. Dit is het derde rapport op rij zonder live Meta data. Zolang dit blijft, is elk ads-rapport half werk en kan geen enkele CPC-, frequency- of variant-analyse worden gedraaid.

2. **Landing page verkeer staat vijf dagen op nul.** Laatste bezoeker 31 juli 2026. Sinds april geen spend. De pagina staat live maar krijgt geen enkele bezoeker, ook niet organisch of via social.

3. **De landing page tracking is stukgelopen, niet alleen dun.** `$autocapture` en `$pageleave` stopten op 10 juli terwijl `$pageview` doorliep tot 31 juli. Dat is een configuratiebreuk, geen verkeersprobleem. Bounce rate is hierdoor niet te berekenen, en dat blijft zo na herstart.

4. **De SYBB funnel is verhuisd zonder dat de meetopzet meeging.** CLAUDE.md en de daily-sybb-report skill gaan uit van startyourballoonbusiness.com met `utm_content` varianten en een `/booking` conversie. De werkelijke verkoop loopt via event registratiepagina's op sempertexeurope.com. Zolang die mismatch bestaat, meet dit rapport elke dag een pagina die niets doet en negeert het de pagina die wel converteert.

5. **De registratiepagina wordt bereikt zonder verkooppagina.** 14 register views tegenover 4 event pagina views over 7 dagen. Bezoekers krijgen de inschrijving voorgeschoteld zonder de argumentatie te hebben gezien.

## 6. Top 3 Acties voor Vandaag

### 1. Autoriseer de Pipeboard Meta Ads connector

**Wat:** Autoriseer de Pipeboard connector zodat Meta Ads data weer opgehaald kan worden.
**Waarom:** Drie rapporten op rij zonder Meta data. Sectie 2 van dit rapport, het volledige ads-rapport en elke variant-analyse zijn hierdoor geblokkeerd. Het is de goedkoopste blokkade om weg te nemen.
**Hoe:** Via je claude.ai connector instellingen, of `/mcp` in een interactieve Claude Code sessie.
**Verwachte impact:** Sectie 2 wordt weer meetbaar. Zonder dit blijft elke uitspraak over campagnestatus indirect afgeleid uit PostHog.
**Escalatie level:** Geel, vereist een handeling van Robin, maar kost twee minuten.

### 2. Beslis welke pagina de SYBB funnel is, en meet die

**Wat:** Kies expliciet of SYBB via startyourballoonbusiness.com of via de event pagina's op sempertexeurope.com loopt. Pas daarna CLAUDE.md en `skills/daily-sybb-report/SKILL.md` aan op die keuze.
**Waarom:** Dit rapport meet nu elke dag een pagina met nul verkeer, terwijl de enige echte SYBB activiteit, 13 registratie-pageviews in een week, op de hoofdsite plaatsvindt en nergens in de rapportstructuur voorkomt.
**Hoe:** Als de landing page de funnel blijft, moet die weer verkeer krijgen en moet de tracking gerepareerd. Als de event pagina's de funnel zijn, moet de skill herschreven naar die paden en moet er een conversie-event op de registratiebevestiging.
**Verwachte impact:** Het rapport gaat over de pagina waar geld verdiend wordt in plaats van over een pagina die stilstaat.
**Escalatie level:** Rood, dit is een strategiebeslissing en raakt de hele rapportagestructuur.

### 3. Repareer de tracking voordat er weer budget op gaat

**Wat:** Zoek uit waarom `$autocapture` en `$pageleave` op 10 juli stopten op startyourballoonbusiness.com. Voeg custom events toe voor scroll milestones (25/50/75/100%), CTA clicks en een conversie op de registratiebevestiging.
**Waarom:** In 60 dagen 12 `$pageleave` events tegenover 83 pageviews, en geen enkel scroll- of CTA-event. De KPI targets uit CLAUDE.md, bounce <55%, scroll >60%, CTA click rate >4%, zijn op dit moment simpelweg niet te berekenen. Budget aanzetten zonder dit te fixen levert opnieuw een blinde maand op.
**Hoe:** PostHog snippet en autocapture config op de site controleren, daarna de custom events toevoegen. Dezelfde events op de event registratiepagina's van sempertexeurope.com zetten als actie 2 die kant op valt.
**Verwachte impact:** Vanaf dag één na herstart bruikbare data in plaats van blinde vlekken. Dit is de voorwaarde om überhaupt te kunnen optimaliseren.
**Escalatie level:** Oranje, vereist aanpassing aan de site.

---

## Databronnen en verificatie

| Bron | Query | Uitkomst |
|------|-------|----------|
| Meta Ads (Pipeboard) | Campagne insights `2026: SYBB`, 5 aug | **Niet uitgevoerd**, connector niet geautoriseerd |
| PostHog | Hosts met pageviews, 60 dagen | `startyourballoonbusiness.com` 83 pageviews, laatste 31 jul 2026 |
| PostHog | Daily pageviews/bezoekers/sessies op SYBB host, 16 jul t/m 5 aug | 0 op 1 t/m 5 aug, laatste verkeer 31 jul |
| PostHog | Event types op SYBB host, 60 dagen | Alleen `$pageview` (83), `$web_vitals` (68), `$autocapture` (20), `$pageleave` (12) |
| PostHog | UTM verkeer alle hosts, 5 aug | 6 bronnen, allemaal email/referral/AI. Nul meta, nul cpc |
| PostHog | Paden met `start-your-balloon-business`, 30 jul t/m 5 aug | 14 register views, 4 event pagina views, 12 bezoekers |
| PostHog | Host-split SYBB event paden, 7 dagen | 13 publiek op sempertexeurope.com, 1 intern op Odoo |
| PostHog | Sessiereconstructie SYBB register bezoekers, 5 aug | 1 interne Odoo hit, 1 echte sessie van 17 pageviews, geen aankoop |

Geen Google MCPs aangeroepen. Niet weggeschreven naar de Meta Ads Tracker Google Sheet.
