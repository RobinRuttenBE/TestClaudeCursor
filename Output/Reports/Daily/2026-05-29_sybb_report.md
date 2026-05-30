# SYBB Daily Report — 29 May 2026

## 1. Samenvatting
De SYBB funnel ligt feitelijk stil. De Meta campagne `2026: SYBB` staat op PAUSED (sinds 19 april 2026) en heeft gisteren geen enkele euro uitgegeven, geen impressies en geen clicks geleverd. De landing page (startyourballoonbusiness.com) kreeg gisteren 0 bezoekers, en over de afgelopen 7 dagen samen slechts 9 pageviews. Er is dus geen performance om te optimaliseren, alleen een campagne die weer aangezet moet worden.

> **Databron status:** Meta Ads MCP (Pipeboard) en PostHog MCP gebruikt. Geen Google bronnen geraadpleegd.

## 2. Meta Ads Performance

Campagne `2026: SYBB` (id `120239435987290239`, account Sempertex Ad Account) heeft status **PAUSED**, laatst gewijzigd 19 april 2026. Geen levering op 29 mei 2026, en geen levering in de volledige 7-daagse vergelijkingsperiode (22 t/m 28 mei).

| Metric | Gisteren (29 mei) | 7d Gemiddelde (22-28 mei) | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads, dus geen variant-data (h11_b3_cta5 t/m h15_b3_cta5 leverden niets gisteren).

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen levering) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t. (geen levering)
**Slechtste variant:** n.v.t. (geen levering)

**Context, laatste keer dat de campagne wel liep:** de week van 19-25 april 2026 (€43,81 spend, 2.756 impressies, CTR 2,21%, CPC €0,72). De sterkste week dit jaar was 1-7 maart (CTR 6,26%, CPC €0,11). Sinds half april staat alles stil.

## 3. Landing Page Health

Gisteren 0 pageviews op startyourballoonbusiness.com, dus geen engagement-metrics te berekenen (bounce, scroll, sessieduur, CTA). De cijfers hieronder reflecteren die leegte.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | ~1,3 / dag | meten | 🔴 |
| Unique visitors | 0 | ~1,1 / dag | meten | 🔴 |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ geen data |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ geen data |
| Scroll 25% | n.v.t. | n.v.t. | >80% | ⚪ geen data |
| Scroll 50% | n.v.t. | n.v.t. | >60% | ⚪ geen data |
| Scroll 75% | n.v.t. | n.v.t. | >40% | ⚪ geen data |
| Scroll 100% | n.v.t. | n.v.t. | >20% | ⚪ geen data |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | ⚪ geen data |

**Pageviews per dag (PostHog, host www.startyourballoonbusiness.com):**
- 22 mei: 2 | 23 mei: 0 | 24 mei: 0 | 25 mei: 0 | 26 mei: 3 | 27 mei: 1 | 28 mei: 3 | 29 mei: 0

Let op: de landing page lijkt alleen `$pageview` te tracken. Er zijn geen scroll-depth of CTA-click events in PostHog aanwezig, dus zelfs met verkeer kan de scroll/CTA-rij van dit rapport nu niet gevuld worden. Dit is een tracking-gat dat los van de campagne-pauze opgelost moet worden.

## 4. Funnel Drop-off
Geen funnel te berekenen, er was gisteren geen instroom.

Pageview (0) → Scroll 50% (geen event) → CTA Click (geen event) → /booking (0)

**Grootste lek:** het lek zit bovenaan de funnel: er komt niemand binnen omdat de campagne uit staat.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne PAUSED sinds 19 april 2026.** Geen ad-levering op 29 mei en in de hele 7d-periode. Dit is de hoofdoorzaak van alle nullen.
- 🚩 **Landing page vrijwel zonder verkeer.** 0 bezoekers gisteren, ~9 in 7 dagen. Wat er binnenkomt is waarschijnlijk organisch of direct, niet vanuit Meta.
- 🚩 **Tracking-gat op de landing page.** Geen scroll-depth en geen CTA-click events in PostHog. Het rapport kan engagement en CTA dus niet meten, ook niet zodra het verkeer terugkomt.

## 6. Top 3 Acties voor Vandaag

1. **Beslis of de SYBB campagne weer aan gaat (en zet hem aan).**
   - **Wat:** campagne `2026: SYBB` reactiveren in Meta Ads Manager, of bewust besluiten hem uit te laten.
   - **Waarom:** PAUSED sinds 19 april, €0 spend, 0 clicks. Zonder dit besluit blijft de hele funnel leeg en heeft dit rapport geen data.
   - **Hoe:** Meta Ads Manager, campagne op ACTIVE zetten. Check vooraf budget (staat op €100/dag daily budget) en of de beste creatives uit maart (CTR 6,26%) nog actief zijn.
   - **Verwachte impact:** verkeer en funnel-data komen terug, optimalisatie wordt weer mogelijk.
   - **Escalatie level:** 🟡 Robin goedkeuring (budget-beslissing).

2. **Dicht het tracking-gat op de landing page.**
   - **Wat:** scroll-depth tracking en CTA-click events toevoegen op startyourballoonbusiness.com.
   - **Waarom:** PostHog tracket nu alleen `$pageview`. Bounce, scroll en CTA-rijen blijven anders leeg, ook met verkeer.
   - **Hoe:** Wix Editor of via de PostHog autocapture/scroll-config; CTA-knop een herkenbaar event laten vuren.
   - **Verwachte impact:** volledig invulbaar dagrapport zodra de campagne weer loopt.
   - **Escalatie level:** 🟠 Wix Editor.

3. **Bevestig de UTM-tagging op de actieve ad-links voordat je heropent.**
   - **Wat:** controleer dat alle SYBB ad-links de UTM-conventie volgen (`utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`).
   - **Waarom:** zonder correcte `utm_content` kan straks geen variant-prestatie per ad gekoppeld worden aan landing-page gedrag.
   - **Hoe:** check de link-URLs van de ads in Ads Manager tegen de tracking-standaard.
   - **Verwachte impact:** zuivere cross-referencing tussen Meta-variant en LP-gedrag vanaf dag 1 van heropening.
   - **Escalatie level:** 🟢 auto / Robin check.

---

*Databronnen: Meta Ads MCP (Pipeboard), campagne `2026: SYBB`. PostHog MCP, project "Default project", host www.startyourballoonbusiness.com. Rapport gegenereerd 30 mei 2026 voor rapportdatum 29 mei 2026.*
