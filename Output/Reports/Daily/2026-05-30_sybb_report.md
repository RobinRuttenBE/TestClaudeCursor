# SYBB Daily Report — 30 May 2026

## 1. Samenvatting
Er valt voor 30 mei weinig te rapporteren, en dat is zelf het belangrijkste signaal: de campagne `2026: SYBB` staat op **PAUSED** en heeft de hele maand mei €0 uitgegeven (daily budget €100, volledig budget_remaining). De landing page kreeg gisteren **0 pageviews**. Met andere woorden: er draait op dit moment geen acquisitie op de SYBB funnel. De data hieronder bevestigt dat; er is geen performance om te optimaliseren tot de campagne weer aan gaat.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID 120239435987290239). Status: **PAUSED**. Daily budget €100, budget_remaining €100. Insights over 1 t/m 30 mei gaven een lege dataset terug: geen spend, impressions, clicks of conversies.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> Let op: er bestaat ook een tweede, eveneens gepauzeerde campagne `2026: SYBB - Kopie` (ID 120243293329420239). Beide staan uit.

### Ad Variant Performance
Geen actieve ads, dus geen variant-data (h11 t/m h15) beschikbaar. Zodra de campagne weer loopt vult deze tabel zich vanzelf.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen actieve ads) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t. (campagne gepauzeerd)
**Slechtste variant:** n.v.t. (campagne gepauzeerd)

## 3. Landing Page Health
Bron: PostHog, host `www.startyourballoonbusiness.com`.

Pageviews per dag deze week: 23 mei 0, 24 mei 0, 25 mei 0, 26 mei 3, 27 mei 1, 28 mei 3, 29 mei 0, **30 mei 0**. De 7 pageviews van de week kwamen uit: 3 zonder UTM (direct/organisch), 2 met `utm_source=facebook` + `utm_campaign=sybb`, en 2 met `utm_source=youtube` + `utm_campaign=sybb`. Geen enkele view kwam van `utm_source=meta`, en geen enkele was van 30 mei. Dat klopt met een gepauzeerde Meta-campagne.

Met 0 bezoekers op 30 mei is er geen betrouwbare bounce rate, scroll depth of CTA click rate te berekenen. De statussen hieronder staan daarom op "geen data", niet rood: er is simpelweg geen verkeer om te meten.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | ~1/dag | meten | ⚪ geen verkeer |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ geen data |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ geen data |
| Scroll 25% | n.v.t. | n.v.t. | >80% | ⚪ geen data |
| Scroll 50% | n.v.t. | n.v.t. | >60% | ⚪ geen data |
| Scroll 75% | n.v.t. | n.v.t. | >40% | ⚪ geen data |
| Scroll 100% | n.v.t. | n.v.t. | >20% | ⚪ geen data |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | ⚪ geen data |

Opmerking: ik kon de scroll depth en CTA click events niet apart valideren in PostHog, maar met 0 bezoekers maakt dat voor 30 mei niet uit. Bij hervatting van de campagne moet dit gecontroleerd worden.

## 4. Funnel Drop-off
Niet van toepassing: geen ad-verkeer en 0 landingen op 30 mei, dus geen funnel te tekenen.

Pageview (0) → Scroll 50% (0) → CTA Click (0) → /booking (0)

**Grootste lek:** n.v.t. Het "lek" zit vóór de funnel: de kraan staat dicht omdat de campagne uit staat.

## 5. Rode Vlaggen 🚩
- **Campagne `2026: SYBB` staat op PAUSED** en geeft de hele maand mei €0 uit. Als dit onbedoeld is, is dit de enige actie die telt: geen ads = geen leads = geen workshop-verkoop.
- **0 pageviews op de landing page op 30 mei**, en slechts 7 organische views over de hele week. De funnel ontvangt praktisch geen verkeer.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of `2026: SYBB` weer aan moet.** Wat: campagne (en/of de Kopie) heractiveren in Meta Ads Manager, of bewust uit laten. Waarom: hij staat op PAUSED met €0 spend in mei, dus er komt nu niets binnen. Verwachte impact: zonder dit blijft alle SYBB-rapportage leeg. Escalatie: Geel (Robin beslist).
2. **Check tracking vóór heractivatie.** Wat: bij het weer aanzetten direct controleren of `utm_source=meta` verkeer in PostHog binnenkomt op `www.startyourballoonbusiness.com` en of scroll/CTA events vuren. Waarom: deze week was 100% van het verkeer untagged, dus de UTM-keten en events zijn nog niet geverifieerd onder live verkeer. Verwachte impact: betrouwbare funnel-data vanaf dag 1. Escalatie: Geel.
3. **Geen optimalisatie nu.** Wat: geen budget- of biedaanpassingen doen zolang de campagne uit staat. Waarom: er is geen performance-data om op te sturen. Verwachte impact: voorkomt beslissingen op lege data. Escalatie: Groen.

---
*Databronnen: Meta Ads MCP (Pipeboard), campagne `2026: SYBB` (PAUSED, account act_567892422940728). PostHog MCP, project "Default project", host www.startyourballoonbusiness.com. Geen Google bronnen gebruikt.*
