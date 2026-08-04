# Morning Report — 2026-08-04

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-08-04_ads_report.md` en is gecommit en gepusht.

## Meta Ads Rapport, 4 augustus 2026

**Er draait niets.** Nul euro spend in de laatste 30 én 90 dagen. Alle 5 campagnes staan op PAUSED, laatste uitgave was april 2026. Het account ligt ~3,5 maand stil.

Twee dingen vooraf over de data:
- `act_607231713057715` (Robin Rutten) is **niet toegankelijk** met de huidige Pipeboard token. Als daar iets draait, zie ik het niet.
- Stap 6 (Google Sheet) is overgeslagen zoals gevraagd. Geen Google MCP calls gedaan.

### Laatste bekende performance per campagne

| Campagne | Spend | CTR | CPC | CPM | Aankopen | ROAS |
|----------|-------|-----|-----|-----|----------|------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,81x ⚠️ |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,30x |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,37x |
| 2026: SYBB, Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Drie dingen die eruit springen

**1. De ROAS van SYBB klopt niet.** Van de €44.247 conversiewaarde komt €42.773,50 uit 2 aankopen op één ad. Dat is €21.386 per aankoop vanaf een starter landingspagina. Vrijwel zeker een pixel fout (waarde in centen, of verkeerd ordertotaal). Realistische ROAS zonder die twee: **0,59x**.

**2. De ads werkten, de pagina niet.** Winnende ad H13 leverde 4.063 landing page views voor €421,29 (€0,10 per bezoeker, uitstekend) en daaruit kwamen **nul** checkouts. Campagnebreed: SYBB converteert 0,5% van bezoeker naar checkout, Nozzle Up deed 19,0% met dezelfde pixel. Dat is 38x slechter. Target is >5%.

**3. Kopieën presteren structureel slechter.** Elke "Kopie" adset heeft een hogere CPC dan het origineel: €0,67 vs €0,25, €0,63 vs €0,07, €0,40 vs €0,31. Dezelfde creative, 9x duurder, puur door opnieuw te moeten leren.

### Aanbevelingen

1. **Fix eerst de tracking.** Op deze ROAS kun je niet sturen, en Meta optimaliseert zelf ook op ruis.
2. **Fix de landingspagina voor je budget aanzet.** 99,5% van elke euro verdampt na de klik. Nozzle Up bewees dat 19% haalbaar is.
3. **Herstart 70-20-10:** 70% op H13 (9,8% CTR, €0,07 CPC) en H11 (enige hook met aankopen), 20% varianten op H15, 10% nieuw. Statisch is al getest en werkt niet, blijf bij video.
4. **Archiveer de Kopie campagne.** Werk verder in bestaande adsets.
5. **Zoek uit wat er in april misging.** CPC ging van €0,13 (maart) naar €0,56 (april) binnen één maand.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Ik kan die ook uit PostHog halen als je wilt, dat mag binnen de regels van deze run. Zeg het maar.

---

Rapport staat in `Output/Reports/Daily/2026-08-03_sybb_report.md`, gecommit en gepusht.

## Kort samengevat

**Meta Ads (campagne `2026: SYBB`, id 120239435987290239):** nog steeds PAUSED. Alle zeven dagen in het venster 28 juli t/m 3 augustus gaven een lege dataset terug: nul spend, nul impressies, nul clicks. Budget staat nog op € 100/dag, laatste wijziging 19 april. De duplicaatcampagne `2026: SYBB - Kopie` is ook PAUSED.

**PostHog (`startyourballoonbusiness.com`):** nul pageviews op 3 augustus. Over zeven dagen 2 pageviews van 2 bezoekers, beide direct verkeer. Over 30 dagen 44 pageviews. Geen enkele referral vanaf Facebook of Instagram in 60 dagen.

De tracking zelf is gezond: de webshop deed op 3 augustus 5.540 pageviews van 1.213 bezoekers in hetzelfde project. De nul op SYBB is dus echt, geen meetfout.

**Wat opvalt:** dit rapport is inhoudelijk identiek aan dat van 2 augustus. De drie acties van gisteren staan alle drie nog open. Ik heb de event taxonomy opnieuw gecontroleerd, er is nog steeds geen scroll depth event, geen CTA click event op SYBB, en geen enkele UTM parameter op `$pageview`. Daardoor blijven 7 van de 9 rijen in Landing Page Health onmeetbaar, ook na een herstart.

Twee dingen die ik deze keer scherper heb gekregen:
- De pixel-waardes zijn aantoonbaar fout met een factor 21. April meldt € 7.374,50 per purchase terwijl `add_to_cart` in dezelfde maand € 350,00 per stuk meestuurt. Meta optimaliseert wel op dat signaal.
- Het verlies tussen link click en landing page view was 36,4% in maart. Bij herstart op maart-volume is dat ongeveer € 480 per maand aan budget dat de pagina nooit haalt.

**Twee opmerkingen over de bronnen.** Het PostHog project heet nu "STX EU" in plaats van "Default project" (zelfde id 149694), dus de skill-documentatie loopt daar achter. En de PostHog MCP stond bij aanvang op het project "Ambition Avenue"; ik heb expliciet naar de Sempertex Europe org en project 149694 geschakeld voordat ik data ophaalde.

Alleen Meta Ads MCP en PostHog MCP gebruikt, geen Google MCPs, niet naar de tracker Sheet geschreven.

---

Rapport staat in `Output/Reports/Daily/2026-08-04_auto_optimize.md`, gecommit en gepusht.

## Auto-Optimize, 4 augustus 2026

**Nul automatische acties uitgevoerd, want er zijn nul actieve ads.** Alle 5 campagnes staan op PAUSED, geen impressions en geen spend in de laatste 3, 30 of 90 dagen. Geen enkele kill-regel kan vuren.

Twee dingen vooraf:
- `act_607231713057715` is niet toegankelijk met de huidige Pipeboard token (toegestaan: `act_1489853856181844` en `act_567892422940728`). `act_1489853856181844` is leeg.
- Alleen Meta Ads MCP gebruikt. Geen Google MCP calls, niets naar de tracker Sheet geschreven.

Omdat "niets te doen" geen bruikbaar rapport is, heb ik de 10 historische ads doorgerekend op **link metrics** in plaats van all-clicks, zodat er een gekalibreerde startpositie ligt voor de herstart.

### Wat dat oplevert

De Core-groep is scherp afgebakend. H13 is de duidelijke winner met **10,6% Link CTR en €0,07 CPC (link)**, dat is 2,6x de Link CTR van de nummer twee. H15, H14 en H11 (originelen) halen ook Core. Alle vier Kopie-adsets vallen eruit op CPC.

Slechts 1 van de 10 ads zou een kill-regel triggeren bij herstart as-is (de statische ad, 0,7% Link CTR). Dat bevestigt de diagnose: het probleem zit niet in de ads, het zit na de klik. H13 kocht 6.342 link clicks voor €0,07 per stuk en leverde nul checkouts.

### Twee dingen die opvallen

**De ROAS-data kan niet gebruikt worden om budget te sturen.** Ad H13 in Kopie 3 rapporteert €42.773,50 op €206,99 spend. Die ad heeft objectief zwakke cijfers (1,2% Link CTR, €1,06 CPC), maar de 70-20-10 regel promoveert alles met ROAS > 2x automatisch naar Core. Zonder pixelfix krijgt dus de zwakste ad het grootste budget. Ik stel voor het ROAS-criterium op te schorten tot dit geverifieerd is.

**De historische budgetverdeling was omgekeerd.** €919,81 (37,0%) ging naar Kopieën plus de statische test, samen goed voor 966 link clicks. De vier Core ads kregen €1.075,09 (43,3%) en haalden 9.189 link clicks. Bijna even veel budget, 9,5x minder resultaat.

### 5 voorstellen, geen ervan uitgevoerd

1. Verifieer de pixel voor er budget aan gaat
2. Herstart selectief: €70/€20/€10 op Core/Emerging/Experimental, Kopie-adsets en statisch niet herstarten
3. Fix de landingspagina eerst, dit is de enige hefboom die orde van grootte uitmaakt
4. Drie video-varianten op de H13 hook, in Emerging tot ze eigen data hebben
5. Kalibreer de 70-20-10 drempels (staat als TODO in het command, deze dataset geeft nu een echte basis)

Geef aan welke nummers je wilt uitvoeren. De logische vervolgcheck is PostHog: of de conversie na de klik verbeterd is sinds april, dat bepaalt of voorstel 3 al kan worden afgevinkt.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
