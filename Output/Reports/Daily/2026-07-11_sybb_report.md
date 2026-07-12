# SYBB Daily Report — 11 July 2026

> **Databronnen:** Meta Ads MCP (Pipeboard) + PostHog MCP.
> Rapport gegenereerd op 12 July 2026 voor rapportagedag **11 July 2026**.

## 1. Samenvatting

Er is **geen performance te rapporteren voor 11 July 2026**. De campagne `2026: SYBB` staat op **PAUSED** en levert geen advertenties uit. Er is nul spend, nul impressies en nul klikken op de rapportagedag. De laatste keer dat deze campagne data genereerde was de flight van **13 t/m 30 April 2026**; sindsdien ligt hij stil (laatst gewijzigd 19 April 2026, budget volledig resterend).

Daarnaast kon de **PostHog MCP niet worden bereikt** in deze sessie, waardoor er geen landing page data (pageviews, bounce, scroll depth, CTA clicks, session recordings) opgehaald kon worden. Beide databronnen leveren dus op dit moment geen bruikbare dagcijfers.

**Belangrijkste trend:** de SYBB funnel staat volledig stil. Dit is een status-issue, geen performance-issue.

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (ID `120239435987290239`) — **status: PAUSED**, daily budget €100,00 (volledig resterend).

| Metric | Gisteren (11 Jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> Geen delivery op 11 July. Ook het volledige 7-daagse venster (5–11 July) is leeg. Trend is niet betekenisvol zolang de campagne gepauzeerd is.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | 0 | n.v.t. | n.v.t. | geen data | geen data |

> Geen actieve ads op de rapportagedag. LP-kolommen leeg omdat PostHog niet beschikbaar was.

**Beste variant:** n.v.t. — geen delivery.
**Slechtste variant:** n.v.t. — geen delivery.

### Referentie — laatste bekende flight (13–30 April 2026)

Ter context, de laatste periode waarin `2026: SYBB` wél draaide:

| Metric | Waarde (13–30 Apr) |
|--------|--------------------|
| Spend | €594,24 |
| Impressions | 42.770 |
| Clicks | 941 |
| CTR | 2,20% |
| CPC | €0,63 |
| Frequency | 2,13 |
| Landing page views | 422 |
| Add to cart | 28 |
| Initiate checkout | 23 |
| Complete registration | 5 |
| Purchases | 4 (waarde €1.473,50) |

> Deze cijfers zijn **historisch** (April) en dienen alleen als referentie, niet als dagrapport. Let op: de CPC lag toen op €0,63, boven het target van €0,50.

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

> ⚪ = geen data. De PostHog MCP was niet bereikbaar in deze sessie, dus er is geen landing page data voor startyourballoonbusiness.com opgehaald. Zodra de PostHog connector weer beschikbaar is, kan deze sectie gevuld worden.

## 4. Funnel Drop-off

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

> Geen funnel-analyse mogelijk: geen ad traffic (campagne paused) én geen PostHog data. **Grootste lek:** niet meetbaar op dit moment.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne `2026: SYBB` staat op PAUSED** en levert al sinds 30 April 2026 niets uit. Zolang dit zo blijft, is er geen SYBB lead- of salesflow via Meta.
- 🚩 **PostHog MCP niet beschikbaar** in deze sessie. Landing page monitoring ligt stil; ad-pagina mismatches en on-page gedrag kunnen niet gedetecteerd worden.
- ⚠️ **Referentie-alert (historisch):** tijdens de laatste flight lag de CPC op €0,63, ruim boven het target van €0,50. Aandachtspunt bij eventuele herstart.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de status van `2026: SYBB`.** Wat: bepaal of de campagne bewust gepauzeerd is of per ongeluk stil ligt. Waarom: nul delivery sinds 30 April betekent nul SYBB-instroom. Hoe: check in Meta Ads Manager of de pauze intentioneel is; zo niet, heractiveren (budget €100/dag staat klaar). Escalatie: 🟡 Robin goedkeuring — herstart is een budgetbeslissing.

2. **Herstel de PostHog MCP-verbinding.** Wat: zorg dat de PostHog connector weer actief is in de sessie. Waarom: zonder PostHog is er geen landing page health, geen funnel drop-off en geen cross-referencing mogelijk — de halve waarde van dit rapport valt weg. Hoe: PostHog MCP autoriseren/herverbinden in een interactieve sessie. Escalatie: 🟡 Robin actie.

3. **Bij herstart: fix de CPC vóór schaal.** Wat: plan een CPC-optimalisatie op basis van de April-data (€0,63 CPC, boven target). Waarom: opnieuw live gaan met een te dure CPC verbrandt budget. Hoe: hook/creative refresh (70-20-10) en audience-check voordat het volledige dagbudget draait. Escalatie: 🟢 voorbereiden, 🟡 bij live zetten.

---

### Databron-notities

- **Meta Ads (Pipeboard MCP):** account `Sempertex Ad Account` (`act_567892422940728`). Campagne `2026: SYBB` opgehaald op campaign-, ad- en adset-niveau voor 11 July 2026 en het 7-daagse venster — alle drie leeg wegens PAUSED status. Historische April-flight opgehaald als referentie.
- **PostHog MCP:** niet beschikbaar in deze sessie (geen PostHog tools bereikbaar). Geen landing page data opgehaald.
- Conform run-instructie zijn **uitsluitend** de Meta Ads MCP en (poging tot) PostHog MCP gebruikt. Geen Google-diensten aangeroepen; niet naar de Google Sheet tracker geschreven.
