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
