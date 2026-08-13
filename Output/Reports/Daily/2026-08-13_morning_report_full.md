# Morning Report — 2026-08-13

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 13 augustus 2026

**Meta Ads data ontbreekt, zesde dag op rij.** Pipeboard is niet geautoriseerd in deze sessie, dus stap 1 tot en met 4 konden niet draaien. Geen campagne-, ad set- of ad-data, en dus ook geen underperformers, top performers of ROAS. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

PostHog bevestigt dat er niets draait: laatste betaalde klik **14 juli 2026**, dertig dagen geleden. Geen Paid Social in de kanaalverdeling. SYBB landing page ligt stil sinds 31 juli.

### Ik trek de conclusie van 11 en 12 augustus in

Die rapporten meldden "sessies dalen acht dagen op rij, er ging iets kapot rond 3 augustus". Dat klopt niet. **PostHog meet vóór 13 juli 7 tot 17 sessies per week.** De tracking op de hoofdsite is toen pas live gegaan. De stijging van 298 naar 974 sessies per dag in de weken daarna is de uitrol van de pixel, geen groei. Er is geen periode om 3 augustus mee te vergelijken.

### Wat wél echt is

Sessies zakten van 1.270 (3 aug) naar 340 (12 aug), min 73,2%. Dat is geen meetfout: Organic Search via Google blijft in dezelfde periode vlak rond 50 tot 90 sessies per dag. Lag de pixel eruit, dan was Google mee gedaald.

### Het probleem dat alles blokkeert

**Je op één na grootste verkeersbron is je eigen domein.** `www.sempertexeurope.com` levert 1.124 sessies in vier dagen, ruim een kwart van je totaal. Sessies breken op tijdens het bezoek, waarschijnlijk bij interne navigatie en bij terugkeer van Mollie.

Daardoor is je sessietelling opgeblazen, is die 4,5% bounce rate op Organic Search een artefact (een opgebroken sessie kan per definitie niet bouncen), en verdwijnt de oorspronkelijke bron van elke opgebroken sessie naar Direct. Dat verklaart waarom Direct 68,6% van je verkeer lijkt te zijn.

Zolang dit staat kun je geen campagne eerlijk beoordelen. Je zou Meta straks afrekenen op cijfers die het systeem zelf verzint.

### Volgorde

1. Autoriseer Pipeboard
2. **Sluit `sempertexeurope.com`, `mollie.com` en de Odoo domeinen uit als verwijzer in PostHog**, dit blokkeert alle andere analyse
3. Herwaardeer de verkeersdaling pas daarna
4. Behandel alles van vóór 13 juli als niet bestaand
5. Conversie events op de SYBB pagina vóór herstart
6. UTM casing lowercase, komma's in `utm_content` naar underscores
7. Klaviyo mails taggen, Email bouncet op 18,5%
8. Organic Search harder inzetten, 1.659 bezoekers en 29.487 pageviews zonder budget

Punt 2 tot en met 8 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-13_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend, een stille landing page en gebroken sessie-attributie levert een funnel diagnose nu geen betrouwbaar antwoord op. Ik zou eerst punt 2 fixen.

---

Report saved to `Output/Reports/Daily/2026-08-12_sybb_report.md`, committed and pushed.

**One part of the request I could not fulfil:** the Pipeboard Meta Ads MCP requires OAuth authorisation and this session is non-interactive, so no Meta Ads data could be fetched. Section 2 is filled with `n.b.` placeholders. Authorise via your claude.ai connector settings or `/mcp` in an interactive session. This is the eighth consecutive day without Meta data.

PostHog delivered fully. Only the two permitted MCPs were used, no Google MCPs, nothing written to the tracker sheet.

**What the data says for 12 August:**

- **SYBB landing page: zero events.** Twelfth silent day. Last event on `startyourballoonbusiness.com` was 31 July. Separately, I re-verified the taxonomy: there is no scroll-depth event or property, no CTA click event, and no `/booking` page in this project. The scroll and CTA targets in the skill are not measurable even if traffic returns.
- **SYBB traffic ran through the event pages** on sempertexeurope.com: one pageview, one visitor, on the German `professionell-7/register` page. Cleaned weekly average is about 5/day, not the raw 16.7 (10 August was inflated by a single visitor).
- **The headline quality numbers are fake-good.** Bounce fell to 11.4% and session duration rose to 604s, but 165 of 457 sessions (36.1%) have your own domain as referrer. Fragmented sessions cannot bounce, so worse tracking produces prettier numbers. I flagged this rather than reporting it as improvement.
- **Sessions declined for a 9th straight day**, 1,338 (3 Aug) to 457, −65.8%. Organic Search held roughly flat, so the pixel is intact and the decline is real.
- **Zero paid traffic confirmed independently:** no Paid Social channel, no `utm_source=meta`, no clicks on any of the five ad variants. So the missing Pipeboard data does not change the conclusion for this date.

The top action is unchanged from yesterday's ads report and still unactioned: exclude `sempertexeurope.com`, `mollie.com` and the Odoo domains as referrers in PostHog. Until that is done, no campaign can be judged fairly on these numbers.

One incidental find worth your time: 50 of the day's 116 rageclicks came from `/en_GB/shop` from just two people, plus 10 more on one rose gold 32" category. That concentration suggests a single broken element rather than general friction.

---

## Auto-Optimize 13 augustus 2026: niet uitgevoerd

**Meta Ads MCP (Pipeboard) is niet geautoriseerd.** Zonder impressions, `actions.link_click` en spend hebben de kill-regels geen invoer, en `update_ad` is niet beschikbaar. Dus zelfs een terechte pauze had ik niet kunnen doorvoeren.

**0 ads geëvalueerd, 0 gepauzeerd.** Belangrijk: dat is niet hetzelfde als "alles presteert goed". Er is geen enkele ad beoordeeld.

### Wat PostHog wél laat zien (laatste 3 dagen, 1.299 sessies)

Geen betaald verkeer, punt. Nul Paid Social, nul Paid Search, nul `meta / cpc / sybb` sessies. De 5 Facebook-verwijzingen zijn organisch. Consistent met de laatste betaalde klik op 14 juli.

Kanalen: Direct 59,0%, Referral 19,5%, Organic Search 17,5%, AI 2,7%, Email 0,7%, Organic Social 0,7%.

Het self-referral probleem uit het ochtendrapport staat er nog: `www.sempertexeurope.com` levert 236 sessies (18,2%). Daarnaast zie ik Mollie, Odoo en het shipping-portal als verwijzer terugkomen.

### Wat blind blijft

Of er nog ACTIVE ads in Meta staan die budget verbranden zonder clicks te leveren, kan ik niet zien. Dat is precies het scenario waarvoor dit command bestaat.

### Voorstellen

1. **Autoriseer Pipeboard** (claude.ai connector instellingen of `/mcp`). Ik kan dit niet zelf.
2. **Referral exclusions in PostHog**: `sempertexeurope.com`, `mollie.com`, de Odoo en shipping-portal domeinen. Doe je dit niet vóór de herstart, dan reken je Meta af op verzonnen cijfers.
3. **Conversie events op de SYBB pagina** vóór herstart, anders blijft ROAS leeg en werkt de 70% Core regel ook ná autorisatie niet.
4. **70-20-10 drempels herzien voor link metrics.** Die TODO staat nog open in het command, ze zijn nog gekalibreerd op all-clicks.

Punt 2, 3 en 4 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-13_auto_optimize.md`, gecommit en gepusht. Geen Google MCPs aangeroepen, niet naar de Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
