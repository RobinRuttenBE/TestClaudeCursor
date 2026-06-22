# SYBB Daily Report: 21 juni 2026

## 1. Samenvatting
Er is gisteren geen SYBB activiteit om te rapporteren. De campagne **`2026: SYBB`** staat op **PAUSED** en heeft op 21 juni 2026 nul impressies, nul clicks en nul spend gedraaid. De laatste actieve maand was april 2026. Daarnaast was de PostHog MCP tijdens deze run niet verbonden, waardoor landing page data (bounce, scroll depth, CTA clicks) niet opgehaald kon worden. Het rapport bevat dus uitsluitend Meta Ads status en een historische referentie.

> **Databron status**
> - Meta Ads (Pipeboard): verbonden. Campagne `2026: SYBB` (ID `120239435987290239`), status PAUSED, daily budget €100.
> - PostHog: **niet beschikbaar** in deze sessie. Geen landing page data opgehaald. Conform de strikte regel voor deze run zijn geen Google of GA4 bronnen als vervanging gebruikt.

## 2. Meta Ads Performance

| Metric | Gisteren (21 jun) | 7d Gemiddelde (15 t/m 21 jun) | Trend |
|--------|----------|---------------|-------|
| Spend | €0 | €0 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De campagne levert sinds 30 april 2026 niets meer af en is op 19 april voor het laatst aangepast. Zowel gisteren als het volledige 7daagse venster (15 t/m 21 juni) tonen nul delivery.

### Ad Variant Performance
Niet van toepassing. Zonder delivery op ad niveau is er geen variant data (h11_b3_cta5, h12_b3_cta5, etc.) voor 21 juni. Cross referencing met landing page gedrag per `utm_content` is daardoor ook niet mogelijk.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

PostHog MCP was niet verbonden tijdens deze run, dus voor startyourballoonbusiness.com is geen traffic, engagement of scroll data beschikbaar. ⚪ = niet gemeten.

## 4. Funnel Drop-off
Niet te berekenen. De funnel (Pageview → Scroll 50% → CTA Click → /booking) vereist PostHog data, die ontbreekt. Bovendien stuurt de gepauzeerde campagne geen verkeer naar de pagina, dus er is naar verwachting ook nauwelijks organische funnel beweging om te meten.

**Grootste lek:** niet te bepalen zonder PostHog data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED.** `2026: SYBB` levert sinds eind april 2026 niets af. Als SYBB acquisitie de bedoeling is, is dit de enige relevante rode vlag van vandaag: er komt nul nieuw verkeer binnen.
- 🚩 **PostHog datapijplijn ontbreekt.** De landing page kant van het dagelijkse rapport kan structureel niet gevuld worden zolang de PostHog MCP niet verbonden is. Dit maakt cross referencing (ad CTR vs bounce, frequency vs bounce) onmogelijk.

Geen andere anomalieën, simpelweg omdat er geen delivery is om te beoordelen (CPC, bounce, frequency, scroll zijn allemaal niet van toepassing).

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de status van `2026: SYBB`.**
   - **Wat:** Bevestig of de campagne bewust gepauzeerd is, of dat hij weer aan moet. Indien activeren: heractiveer in Meta Ads Manager met het €100 daily budget en verse creatives.
   - **Waarom:** Campagne PAUSED sinds eind april, nul delivery 7 dagen op rij. Zonder actieve campagne is er geen dagelijks rapport om te genereren.
   - **Hoe:** Meta Ads Manager (handmatig) of via een geplande relaunch.
   - **Verwachte impact:** Herstel van verkeer naar de SYBB landing page en bruikbare dagelijkse data.
   - **Escalatie level:** 🟡 Geel (Robin goedkeuring nodig voor relaunch en budget).

2. **Herstel de PostHog MCP koppeling.**
   - **Wat:** Verbind de PostHog MCP zodat startyourballoonbusiness.com data (pageviews, bounce, scroll, CTA clicks, session recordings) weer opgehaald kan worden.
   - **Waarom:** De helft van dit rapport (Landing Page Health, Funnel, cross referencing) is afhankelijk van PostHog en kon nu niet gevuld worden.
   - **Hoe:** Controleer de PostHog MCP configuratie in de Claude setup.
   - **Verwachte impact:** Volledige rapporten met landing page en funnel inzicht.
   - **Escalatie level:** 🟡 Geel (technische setup).

3. **Bij relaunch: verifieer UTM tagging en creatives vooraf.**
   - **Wat:** Controleer dat de ad variants (`utm_content=hXX_bX_ctaX`, lowercase, `utm_campaign=sybb`) correct getagd zijn voordat de campagne weer live gaat.
   - **Waarom:** Per UTM rapportage in dit rapport vereist consistente lowercase tagging; dat is alleen zinvol als de tags vanaf dag 1 kloppen.
   - **Hoe:** Volg de UTM conventie uit de tracking standards en de daily-sybb-report skill.
   - **Verwachte impact:** Bruikbare variant en cross reference analyse zodra delivery hervat.
   - **Escalatie level:** 🟢 Groen (voorbereiding).

---

### Historische referentie (laatste actieve maand: april 2026)
Ter context, de laatste maand met delivery. Dit is GEEN data van gisteren.

| Maand | Spend | Impressions | Clicks | CTR | CPC | Frequency | Purchases | Leads |
|-------|-------|-------------|--------|-----|-----|-----------|-----------|-------|
| jan 2026 | €101,74 | 16.268 | 167 | 1,03% | €0,61 | 1,81 | 0 | 0 |
| mrt 2026 | €1.323,83 | 189.067 | 9.965 | 5,27% | €0,13 | 2,07 | 0 | 15 |
| apr 2026 | €1.059,47 | 91.839 | 1.935 | 2,11% | €0,55 | 2,19 | 6 | 6 |

In april liep CPC op naar €0,55 (boven target <€0,50) terwijl CTR daalde van 5,27% (maart) naar 2,11%, een teken van creative fatigue richting het einde van de actieve periode. Bij relaunch zijn verse creatives aan te raden.

---

*Gegenereerd op 22 juni 2026. Bron: Meta Ads MCP (Pipeboard). PostHog niet beschikbaar tijdens deze run.*
