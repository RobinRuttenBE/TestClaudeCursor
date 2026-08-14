# SYBB Daily Report, 13 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, 149694). Meta Ads MCP niet beschikbaar, zie sectie 2.
> **Gegenereerd:** 14 augustus 2026. Alleen PostHog en Meta Ads MCP gebruikt, geen Google MCPs, niets naar de tracker Sheet geschreven.

## 1. Samenvatting

**De landing page meet niets meer en dat is het echte verhaal van vandaag.** `startyourballoonbusiness.com` heeft op 13 augustus nul events verstuurd naar PostHog. Niet weinig, nul. Het laatste event van dat domein kwam binnen op **31 juli 2026 om 21:12 UTC**, dertien volle dagen eerder. Elk cijfer in dit rapport dat over de landing page gaat is daarom niet "slecht", het is onmeetbaar.

Meta Ads is de achtste dag op rij niet op te halen omdat Pipeboard niet geautoriseerd is. Los daarvan staat er ook niets aan: over 13 augustus is er projectbreed nul verkeer met `utm_source=meta`.

De rest van het bedrijf draait gewoon door. Projectbreed 367 bezoekers en 4.398 pageviews, plus 28% bezoekers versus de dag ervoor. De SYBB workshop pagina's op de hoofdsite trokken 2 bezoekers.

## 2. Meta Ads Performance

**Niet beschikbaar.** De Pipeboard Meta Ads MCP vereist autorisatie en deze sessie is niet interactief, dus de OAuth flow kan hier niet draaien. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | geen data | geen data | n.v.t. |
| Impressions | geen data | geen data | n.v.t. |
| Clicks | geen data | geen data | n.v.t. |
| CTR | geen data | geen data | n.v.t. |
| CPC | geen data | geen data | n.v.t. |
| Frequency | geen data | geen data | n.v.t. |

**Maar de autorisatie is niet het echte probleem.** PostHog kan aan de ontvangende kant zien of er advertentieverkeer binnenkomt, en dat kan het onafhankelijk van Pipeboard. Uitkomst voor 13 augustus, alle UTM getagde pageviews in het hele project:

| utm_source | utm_medium | utm_campaign | Pageviews | Bezoekers |
|------------|-----------|--------------|-----------|-----------|
| chatgpt.com | (geen) | (geen) | 8 | 8 |

Dat is de volledige lijst. Geen `meta`, geen `cpc`, geen `sybb`. Ook met een werkende Pipeboard koppeling zou het antwoord vandaag "de campagne staat uit" zijn.

### Ad Variant Performance

Over de **volledige 90 dagen** is er in totaal 5 pageviews met een Meta UTM op de landing page geland. Niet 5 per dag, 5 in totaal.

| Ad (utm_content) | LP pageviews | /checkout pageviews | LP Bounce | LP Scroll 50%+ |
|-------------------|--------------|---------------------|-----------|----------------|
| h11_b3_cta5 | 2 | 1 | niet gemeten | niet gemeten |
| H14,B3,CTA5 | 1 | 1 | niet gemeten | niet gemeten |
| h12 / h13 / h15_b3_cta5 | 0 | 0 | n.v.t. | n.v.t. |

**Beste variant:** niet te bepalen. Bij 2 pageviews is elk verschil ruis.
**Slechtste variant:** niet te bepalen, om dezelfde reden.

Wel bruikbaar signaal: **`H14,B3,CTA5` is in hoofdletters en met komma's getagd.** De conventie in CLAUDE.md is lowercase met underscores, dus `h14_b3_cta5`. PostHog ziet die twee als losse waarden, waardoor dezelfde ad in twee rijen uiteenvalt. Dit stond ook al in het ads rapport van 14 augustus, punt 6.

## 3. Landing Page Health

**Geen enkele metric in deze tabel is meetbaar voor 13 augustus.** De reden verschilt per rij en dat verschil is belangrijk.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 0 | n.v.t. | 🔴 tracking dood |
| Bounce Rate | onmeetbaar | onmeetbaar | <55% | 🔴 tracking dood |
| Avg Session Duration | onmeetbaar | onmeetbaar | >90s | 🔴 tracking dood |
| Scroll 25% | **nooit gemeten** | nooit gemeten | >80% | 🔴 event bestaat niet |
| Scroll 50% | **nooit gemeten** | nooit gemeten | >60% | 🔴 event bestaat niet |
| Scroll 75% | **nooit gemeten** | nooit gemeten | >40% | 🔴 event bestaat niet |
| Scroll 100% | **nooit gemeten** | nooit gemeten | >20% | 🔴 event bestaat niet |
| CTA Click Rate | onmeetbaar sinds 10 juli | onmeetbaar | >4% | 🔴 tracking dood |

### Wat er precies stuk is

Alle events die het domein `startyourballoonbusiness.com` ooit heeft gestuurd, met de laatste ontvangst:

| Event | Totaal (90d) | Laatste keer ontvangen |
|-------|--------------|------------------------|
| `$pageview` | 131 | **31 juli 2026, 21:12 UTC** |
| `$web_vitals` | 126 | 31 juli 2026, 21:12 UTC |
| `$autocapture` | 50 | **10 juli 2026, 14:22 UTC** |
| `$pageleave` | 23 | 10 juli 2026, 14:23 UTC |

Hieruit volgen drie losse storingen, van oud naar nieuw:

1. **Sinds 10 juli: geen `$autocapture` en geen `$pageleave` meer.** Zonder `$pageleave` kan PostHog geen sessieduur en geen betrouwbare bounce rate berekenen. Zonder `$autocapture` worden CTA clicks niet vastgelegd. De CTA Click Rate target van >4% is dus al vijf weken niet te toetsen.
2. **Sinds 1 augustus: helemaal niets meer.** Ook de pageviews stopten. Dit wijst op een verwijderde of gebroken PostHog snippet op de site, niet op een instellingsprobleem.
3. **Scroll depth is er nooit geweest.** In de volledige event taxonomie van het project komt geen enkel scroll event voor. De vier scroll targets in de skill en in CLAUDE.md meten iets dat nooit is geïnstrumenteerd.

Ter vergelijking, in de periode dat de meting nog liep was het volume al zeer laag: over 90 dagen 131 pageviews, met dagpieken van 6 tot 9 en veel dagen op 1.

## 4. Funnel Drop-off

Niet te berekenen. Stap 1 levert nul op, en stap 2 van de funnel in de skill, scroll voorbij 50%, bestaat niet als event.

```
Pageview (0)  ->  Scroll 50% (event bestaat niet)  ->  CTA Click (dood sinds 10 juli)  ->  /booking (0)
```

**Grootste lek:** de meting zelf. Er is op dit moment geen enkel punt in deze funnel waar je een lek zou kunnen zien.

### De funnel die wel draait

Volgens de projectkennis verkoopt SYBB via de event pagina's op `sempertexeurope.com`, niet via de landing page. Die pagina's meten wel gewoon door.

| Dag | Pageviews | Bezoekers |
|-----|-----------|-----------|
| **13 aug (gisteren)** | **2** | **2** |
| 12 aug | 1 | 1 |
| 11 aug | 1 | 1 |
| 10 aug | 88 | 6 |
| 9 aug | 3 | 3 |
| 8 aug | 8 | 4 |
| 7 aug | 10 | 4 |

7d gemiddelde pageviews 16,1, maar dat gemiddelde is vervuild door 10 augustus, waar 6 bezoekers samen 88 pageviews maakten. De **mediaan van 3 pageviews en 3 bezoekers** is de eerlijkere vergelijking. Gisteren zat met 2 en 2 daar net onder, wat binnen de normale dagruis van dit volume valt.

Gisteren geraakt: `/event/start-your-balloon-business-professional-7/register` en `/event/start-your-balloon-business-professional-9/register`, elk 1 bezoeker.

## 5. Rode Vlaggen 🚩

- 🚩 **Landing page stuurt 13 dagen geen enkel event.** Laatste signaal 31 juli 21:12 UTC. Dit is de meest urgente vlag en hij dekt alle andere landing page vlaggen af.
- 🚩 **CTA clicks en sessieduur al onmeetbaar sinds 10 juli.** `$autocapture` en `$pageleave` vielen drie weken eerder uit dan de pageviews. Dit is een aparte storing, niet hetzelfde probleem.
- 🚩 **Scroll depth is nooit geïnstrumenteerd.** Vier van de zeven targets in de skill toetsen data die niet bestaat. Dit is een fout in de skill, niet in de site.
- 🚩 **Nul Meta verkeer op 13 augustus, projectbreed.** De campagne staat uit of tagt niet.
- 🚩 **Pipeboard achtste dag niet geautoriseerd.** Blokkeert alle spend, CPC, CTR en frequency data, dus ook de ad fatigue check.
- 🚩 **UTM conventie wordt geschonden.** `H14,B3,CTA5` in hoofdletters met komma's splitst dezelfde ad in twee segmenten.
- ℹ️ Ter context, projectbreed steeg de bounce rate op 13 augustus naar 36,8% vanaf 15,9% de dag ervoor, en de sessieduur daalde 35% naar 399s. Bezoekers stegen wel 28% naar 367. Dit gaat over de hoofdsite en staat los van SYBB.

## 6. Top 3 Acties voor Vandaag

### 1. Zet de PostHog snippet terug op startyourballoonbusiness.com

- **Wat:** controleer of de PostHog tracking snippet nog in de site head staat en of `phc_yosUlZYJ35Lkjw3qfcwu4cm4x07lF7cIY17F8AqIpNB` nog de gebruikte project key is. Kijk daarna apart of `$autocapture` en `$pageleave` aan staan in de SDK config, want die vielen eerder uit dan de rest.
- **Waarom:** laatste event 31 juli 21:12 UTC, dertien dagen stilte. Autocapture al stil sinds 10 juli.
- **Hoe:** Wix Editor, site instellingen, custom code in de head. Twee losse checks, want het zijn twee storingen.
- **Verwachte impact:** zonder dit is elk volgend SYBB rapport net zo leeg als dit. Dit blokkeert alles.
- **Escalatie:** 🟠 Oranje, Wix Editor.

### 2. Houd het Meta budget dicht tot meting 1 werkt

- **Wat:** zet de campagne `2026: SYBB` niet aan, ook niet als Pipeboard vandaag geautoriseerd wordt.
- **Waarom:** je zou betalen voor klikken naar een pagina die niets terugmeldt. In 90 dagen zijn er 5 Meta pageviews geland, en zelfs die kun je nu niet beoordelen op bounce, scroll of CTA.
- **Hoe:** Meta Ads Manager, campagne op pauze laten. Autoriseer Pipeboard wel alvast, dat kost niets.
- **Verwachte impact:** voorkomt dat je budget uitgeeft aan verkeer dat je per definitie niet kunt evalueren.
- **Escalatie:** 🟡 Geel, jouw goedkeuring.

### 3. Repareer de skill, niet alleen de site

- **Wat:** twee correcties in `skills/daily-sybb-report/SKILL.md`. Voeg scroll depth events toe aan de site of haal de vier scroll targets uit de skill, en verleg de funnel definitie naar de event register pagina's op `sempertexeurope.com`.
- **Waarom:** de skill meet nu een landing page funnel die volgens de projectkennis niet de verkoopfunnel is, en toetst vier scroll targets waarvoor nooit een event bestond. Ook na reparatie van punt 1 blijft dat rapport half leeg.
- **Hoe:** scroll tracking via PostHog custom events of de scroll autocapture optie. Skill handmatig aanpassen.
- **Verwachte impact:** het rapport gaat vanaf dan over de funnel die daadwerkelijk omzet maakt.
- **Escalatie:** 🟡 Geel, jouw goedkeuring op de nieuwe funnel definitie.

---

**Volgorde:** 1 blokkeert alles. 3 kan parallel, want die heeft Pipeboard noch de site fix nodig. 2 is een beslissing die je vandaag neemt en niets kost.
