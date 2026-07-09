# SYBB Daily Report — 8 July 2026

> Databronnen deze run: Meta Ads MCP (Pipeboard) + PostHog MCP. Geen Google-bronnen gebruikt.

## 1. Samenvatting
Er valt vandaag weinig te rapporteren, en dat is zelf het belangrijkste signaal. De campagne **2026: SYBB** stond gisteren op **PAUSED** en heeft nul delivery gedraaid (geen spend, impressions of clicks), niet alleen op 8 juli maar in de volledige laatste 30 dagen. De landing page data kon deze run niet opgehaald worden omdat de PostHog MCP geen tools beschikbaar stelde (zie Rode Vlaggen). Netto: de funnel staat stil en er komt op dit moment geen betaald verkeer binnen.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID `120239435987290239`), account Sempertex Ad Account (`act_567892422940728`).
Status: **PAUSED** (laatst gewijzigd 20 April 2026). Daily budget ingesteld op €100,00.

| Metric | Gisteren (8 jul) | 7d Gemiddelde (1 t/m 7 jul) | Trend |
|--------|------------------|------------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Insights API gaf voor elke dag van 1 t/m 8 juli een lege dataset terug. Een controle over de laatste 30 dagen bevestigt hetzelfde: geen enkele delivery. Dit is consistent met de PAUSED status.

### Ad Variant Performance
Geen data. De campagne leverde gisteren geen enkele ad uit, dus er zijn geen `utm_content` varianten (h11_b3_cta5 e.d.) om te vergelijken.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health
**Niet beschikbaar deze run.** De PostHog MCP leverde geen tools op (server verbonden maar geen tools blootgesteld). Landing page metrics voor startyourballoonbusiness.com konden daardoor niet opgehaald worden.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

Opmerking: ook mét een werkende PostHog verbinding zou het verkeer uit deze campagne nul zijn, omdat er geen ads draaien. Eventueel organisch of overig verkeer op de landing page is niet meegenomen omdat de bron niet bereikbaar was.

## 4. Funnel Drop-off
Niet te berekenen. Zonder Meta delivery en zonder PostHog data is er geen funnel om door te rekenen.

Pageview (geen data) → Scroll 50% (geen data) → CTA Click (geen data) → /booking (geen data)

**Grootste lek:** De funnel start niet. Het "lek" zit vóór stap 1: er wordt geen verkeer ingekocht.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSED en levert niets.** Nul delivery op 8 juli en over de volledige laatste 30 dagen. Als de intentie was dat SYBB liep, dan lekt hier elke dag potentieel verkeer en pipeline weg.
- 🚩 **PostHog MCP niet beschikbaar.** De server was verbonden maar stelde geen tools beschikbaar (meerdere zoekpogingen gaven geen resultaat). Landing page health kon niet gemeten worden. Dit blokkeert de cross-reference analyse die de kern van dit rapport vormt.
- ℹ️ Er bestaat een tweede campagne `2026: SYBB - Kopie` (ID `120243293329420239`), eveneens PAUSED. Controleer of niet per ongeluk de verkeerde campagne bedoeld is om te activeren.

## 6. Top 3 Acties voor Vandaag
1. **Bepaal of SYBB actief hoort te zijn en zet de juiste campagne live.**
   - **Wat:** Beslis of `2026: SYBB` weer moet draaien. Zo ja, activeer de campagne (niet de "- Kopie" variant, tenzij die bewust de nieuwe is).
   - **Waarom:** Nul delivery over 30 dagen betekent nul betaald verkeer naar de workshop funnel.
   - **Hoe:** Meta Ads Manager, campagne `2026: SYBB` op ACTIVE. Check vooraf budget (€100/dag ingesteld) en of de ad sets nog actuele creatives en UTMs hebben.
   - **Verwachte impact:** Herstart van verkeer en meetbare funnel data.
   - **Escalatie level:** Geel (Robin goedkeuring: budget en timing).

2. **Herstel de PostHog MCP verbinding.**
   - **Wat:** Zorg dat de PostHog MCP tools weer beschikbaar zijn zodat landing page data opgehaald kan worden.
   - **Waarom:** Zonder PostHog is de helft van dit rapport blind en werkt de cross-reference analyse (ad vs landing gedrag) niet.
   - **Hoe:** Controleer de MCP configuratie en authenticatie in een interactieve sessie (`/mcp` of `claude mcp`). Draai daarna dit rapport opnieuw.
   - **Verwachte impact:** Volledige rapportage inclusief bounce, scroll en CTA data.
   - **Escalatie level:** Geel.

3. **Verifieer creatives, UTMs en landing page vóór heractivatie.**
   - **Wat:** Loop de ad sets van `2026: SYBB` na op geldige `utm_content` tagging (h11_b3_cta5 conventie) en check dat startyourballoonbusiness.com laadt en de PostHog tracking actief is.
   - **Waarom:** Een campagne heractiveren met verouderde creatives of gebroken tracking verspilt budget en levert weer geen bruikbare data.
   - **Hoe:** Meta Ads Manager voor UTMs, handmatige check van de landing page, `/tracking-check` voor pixel en events.
   - **Verwachte impact:** Schone data vanaf dag 1 na heractivatie.
   - **Escalatie level:** Groen tot Geel.

---
*Gegenereerd op 9 July 2026. Meta Ads via Pipeboard MCP. PostHog MCP was niet beschikbaar tijdens deze run; landing page secties zijn daardoor onvolledig.*
