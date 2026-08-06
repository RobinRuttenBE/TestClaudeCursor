# Morning Report — 2026-08-06

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 6 augustus 2026

**De Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 van het command konden niet draaien. Geen live spend, CTR, CPC of ROAS. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

Er is **nul betaald verkeer** in de laatste 30 dagen. Geen "Paid Social" kanaal, geen enkele hit op `utm_source=meta` of `utm_medium=cpc`. Dat is onafhankelijke bevestiging van de meting van 4 augustus: alles staat op PAUSED, laatste uitgave april 2026.

Landing page over 30 dagen: 13.844 bezoekers, 90.089 pageviews, bounce rate 54,5% (target <55%, net gehaald), gemiddelde sessieduur 4m49s. De vergelijking met de vorige periode die PostHog geeft (+32.862%) is onbruikbaar, want die periode telde maar 42 bezoekers. De tracking ging pas een maand geleden live.

Email is nu het enige kanaal dat presteert: `inspiration_promo_202607` met 15,2% bounce rate, `workshop_tobi_promo_202608` met 22,2%, tegenover 54,5% site-breed. Drie keer zo betrokken als gemiddeld.

### Iets belangrijkers dat ik onderweg vond

`CLAUDE.md` gaat ervan uit dat PostHog **startyourballoonbusiness.com** meet. Dat klopt niet. Er is één organisatie en één project, en de enige hosts die data sturen zijn `www.sempertexeurope.com` en `rezolvbv-sh-sempertex.odoo.com`. De SYBB landingspagina wordt niet gemeten.

Alle SYBB KPI targets uit je CLAUDE.md zijn daarmee op dit moment onmeetbaar. Dat weegt zwaar, want uit het rapport van 4 augustus bleek dat juist die pagina 0,5% naar checkout converteerde tegenover 19,0% bij Nozzle Up. De pagina waar het geld verdampt is precies de pagina die blind is.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert al het andere
2. Zet de pixel op startyourballoonbusiness.com **vóór** je budget aanzet
3. Fix de conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
4. Pas daarna herstarten volgens 70-20-10
5. Tag de Klaviyo mails met `utm_campaign`, 107 bezoekers zijn nu niet toewijsbaar

Rapport staat in `Output/Reports/Daily/2026-08-06_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Let op dat een funnel diagnose met nul spend en nul betaald verkeer weinig oplevert. Zinvoller wordt het zodra de SYBB pixel staat en er weer budget loopt.

---

Rapport staat in `Output/Reports/Daily/2026-08-05_sybb_report.md`, gecommit en gepusht (`c37bcfb4`).

**Meta Ads ontbreekt.** De Pipeboard connector is in deze sessie niet geautoriseerd en de sessie is non-interactief, dus ik kon geen OAuth doen. Autoriseren kan via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Sectie 2 is daarom gemarkeerd als "geen data" in plaats van ingevuld met aannames. De april 2026 cijfers heb ik overgenomen uit het 4-augustusrapport en expliciet gelabeld als niet-verse data.

**Wat PostHog wel oplevert:**

- startyourballoonbusiness.com had 0 pageviews op 5 augustus. Vijfde dag op rij nul, laatste bezoeker 31 juli.
- Nul betaald verkeer accountbreed op 5 augustus. Geen enkele hit met `utm_source=meta` of `utm_medium=cpc`. Dat bevestigt indirect dat de campagne nog steeds stilstaat.

**Twee dingen die ik onderweg tegenkwam en die zwaarder wegen dan het dagcijfer:**

1. De SYBB workshop wordt nu verkocht via event registratiepagina's op sempertexeurope.com, niet via de landing page. Die trokken 13 registratie-pageviews van 12 bezoekers in de week van 30 juli tot 5 augustus. Klein, maar het is de enige SYBB funnel die draait, en hij komt nergens voor in CLAUDE.md of de skill. Het rapport meet dus elke dag een pagina die stilstaat en negeert de pagina die converteert. Dit heb ik als memory vastgelegd.

2. Het ads-rapport van 6 augustus stelt dat startyourballoonbusiness.com niet gemeten wordt. Dat klopt niet, de pixel staat er en heeft 83 pageviews vastgelegd. Het echte probleem is dat `$autocapture` en `$pageleave` op 10 juli stopten terwijl `$pageview` doorliep tot 31 juli. Dat is een configuratiebreuk, en het betekent dat bounce rate en scroll depth ook na herstart niet te berekenen zijn.

Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven.

---

## Auto-Optimize, 6 augustus 2026

**Nul ads gepauzeerd, en dat is geen goed nieuws.** De Meta Ads MCP is niet geautoriseerd, dus de kill-regels konden helemaal niet draaien. Geen campagnes, geen ads, geen insights, geen `update_ad` calls. Autoriseren kan via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

Belangrijk onderscheid: "geen acties uitgevoerd" betekent hier **niet** "alles presteert goed". Zonder `actions.link_click` en `impressions` per ad is Link CTR niet te berekenen, zonder `spend` per ad geen CPC (link). Beide kill-regels draaien uitsluitend op die link-varianten, dus er viel niets te toetsen.

### Wat PostHog wel bevestigt

Er is nul betaald verkeer in de laatste 3 dagen. Geen Paid Social kanaal, geen enkele hit op `utm_source=meta` of `utm_medium=cpc`.

| Kanaal | Bezoekers | Bounce rate |
|---|---|---|
| Direct | 2.244 | 41,3% |
| Referral | 864 | 76,9% |
| Organic Search | 203 | 3,9% |
| Email | 46 | 18,8% |

De 5 bezoekers via facebook.com referrer zijn organisch, geen ads. Email presteert opnieuw ver boven gemiddeld: `workshop_tobi_promo_202608` haalt 35 bezoekers.

Dit sluit aan op vanochtend en op 4 augustus: alles PAUSED, campagne `2026: SYBB` sinds 19 april.

### Wat er eerst moet gebeuren

1. **Pipeboard autoriseren.** Dit blokkeert alles, elke dag opnieuw.
2. **Pixel op de juiste funnel** vóór je budget aanzet. SYBB loopt sinds 5 augustus via de event registratiepagina's op sempertexeurope.com, niet via de landing page waar CLAUDE.md en de skill van uitgaan.
3. **Conversiewaarde tracking fixen.** Die ROAS van 17,81x is vrijwel zeker een pixelfout. Blijft die staan, dan classificeert 70-20-10 straks ads als Core op basis van verzonnen omzet.

De 70-20-10 kalibratie-TODO staat overigens nog open: de drempels zijn nog op all-clicks gebaseerd en moeten door jou herzien worden voor link metrics.

Rapport staat in `Output/Reports/Daily/2026-08-06_auto_optimize.md`, gecommit en gepusht. Zodra Pipeboard geautoriseerd is kan deze run ongewijzigd opnieuw en levert hij wel echte beslissingen op.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
