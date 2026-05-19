# SYBB Daily Report: 18 May 2026

## 1. Samenvatting
De SYBB funnel ligt feitelijk stil. De Meta campagne "2026: SYBB" staat op PAUSED en heeft op 18 mei niets uitgeleverd (€0 spend, 0 impressies, 0 clicks). De landingspagina kreeg slechts 4 pageviews van 3 unieke bezoekers, allemaal via de organische bio link, en niemand bereikte de boekingspagina. Zonder betaald verkeer is er geheel geen acquisitie op dit moment.

## 2. Meta Ads Performance

Campagne: **2026: SYBB** (id 120239435987290239), status **PAUSED**, daily budget €100 (niet actief).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De campagne leverde voor het laatst uit op 19 april 2026 (eenmalig: €43,81 spend, 2.756 impressies, 61 clicks, CTR 2,21%, CPC €0,72). Sindsdien geen delivery. In het volledige 7d venster (11 t/m 17 mei) en op 18 mei was er nul activiteit.

### Ad Variant Performance
Geen ad delivery, dus geen variant data beschikbaar.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen delivery) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t. (campagne gepauzeerd)
**Slechtste variant:** n.v.t. (campagne gepauzeerd)

## 3. Landing Page Health

Bron: PostHog, startyourballoonbusiness.com.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 4 | 5,4 / dag | meten | 🔴 zeer laag |
| Unieke bezoekers | 3 | 3,9 / dag | meten | 🔴 zeer laag |
| Sessies | 3 | 4,4 / dag | meten | 🔴 zeer laag |
| Avg Session Duration | 121s | meten | >90s | 🟢 |
| Median Session Duration | 59s | meten | >90s | 🟡 |
| Bounce Rate | niet gemeten | niet gemeten | <55% | ⚪ geen data |
| Scroll 25 / 50 / 75 / 100% | niet gemeten | niet gemeten | div. | ⚪ geen data |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚪ geen data |

**Datagat:** dit PostHog project legt alleen `$pageview`, `$dead_click` en `$rageclick` vast. Er zijn geen scroll depth events, pageleave events of CTA click events. Daardoor zijn bounce rate, scroll depth en CTA click rate niet te rapporteren. Zie aanbeveling 2.

**7d verloop pageviews:** 11 mei 4, 12 mei 14, 13 mei 1, 14 mei 1, 15 mei 4, 16 mei 7, 17 mei 7. Het volume is structureel zeer laag (piek 14 op 12 mei).

### Verkeersbron (utm_content, gisteren)
| utm_content | Pageviews |
|-------------|-----------|
| bio_link | 4 |

Alle 4 pageviews kwamen via de organische social bio link. Nul paid verkeer (geen h11_b3_cta5 of andere campagne varianten), consistent met de gepauzeerde campagne.

## 4. Funnel Drop-off

Landing page (3 personen, 100%) → /booking (0 personen, 0%)

**Grootste lek:** de stap van landingspagina naar boekingspagina. 100% drop-off, niemand van de 3 bezoekers ging door naar /booking. Bij dit verkeersvolume is dit statistisch niet betekenisvol, maar het bevestigt dat er geen conversie loopt zolang de funnel droog staat.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne PAUSED, nul acquisitie:** geen betaald verkeer op 18 mei en in het hele 7d venster. Dit is de hoofdoorzaak van alle lage cijfers.
- 🚩 **Landingspagina vrijwel zonder verkeer:** 3 unieke bezoekers op een dag. Geen statistische basis voor optimalisatiebeslissingen.
- 🚩 **Nul booking page views** op een dag met bezoekers (lage N, maar 0 conversie).
- 🚩 **Tracking incompleet:** geen scroll, pageleave of CTA events in PostHog. Kernmetrics uit de skill (bounce, scroll depth, CTA click rate) kunnen niet gemeten worden.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over de SYBB campagne (hoogste impact).**
   - Wat: bepaal of "2026: SYBB" weer geactiveerd wordt of bewust gepauzeerd blijft.
   - Waarom: campagne staat op PAUSED, €0 spend, geen acquisitie sinds 19 april. Dit blokkeert de volledige funnel.
   - Hoe: in Meta Ads Manager de campagne en adsets weer op ACTIVE zetten (handmatig, Robin goedkeuring), of expliciet vastleggen dat de pauze gewenst is.
   - Verwachte impact: herstel van verkeer en meetbare funnel data.
   - Escalatie: Geel (Robin goedkeuring).

2. **Repareer de landing page tracking.**
   - Wat: voeg scroll depth, pageleave en CTA click events toe op startyourballoonbusiness.com.
   - Waarom: zonder deze events zijn bounce rate, scroll depth en CTA click rate (kern KPI's uit de skill) blind.
   - Hoe: PostHog autocapture / scroll tracking activeren en CTA knoppen instrumenteren (Wix Editor / dev taak).
   - Verwachte impact: volledige Landing Page Health sectie wordt meetbaar zodra verkeer terugkeert.
   - Escalatie: Oranje (Wix Editor / technische taak).

3. **Houd de organische bio link warm.**
   - Wat: zolang de campagne uit staat, blijf de SYBB bio link inzetten in social content zodat er enige instroom blijft.
   - Waarom: alle 4 pageviews van gisteren kwamen via bio_link; dit is nu het enige acquisitiekanaal.
   - Hoe: bio link prominent houden in Instagram/Facebook profiel en posts (handmatig, content team).
   - Verwachte impact: behoud van minimale funnel instroom tot de campagne herstart.
   - Escalatie: Groen (auto / content team).

---
*Databronnen: Meta Ads MCP (Pipeboard), PostHog MCP. Geen Google bronnen gebruikt. Rapport over 18 mei 2026, gegenereerd 19 mei 2026.*
