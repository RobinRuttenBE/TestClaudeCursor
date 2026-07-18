# SYBB Daily Report — 17 July 2026

> Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP. Rapport gegenereerd op 18 July 2026.

## 1. Samenvatting
Er viel gisteren niets te rapporteren op advertentievlak: de campagne **"2026: SYBB"** stond de hele dag op **PAUSED** en had **nul impressies, nul clicks en nul spend**. De campagne draait feitelijk niet meer sinds eind april 2026 (laatste delivery 19–30 april). De landing page kant kon deze run **niet** worden opgehaald: de **PostHog MCP is niet verbonden** in deze sessie, dus er is geen bounce rate / scroll depth / CTA data beschikbaar. Netto: geen actief funnelverkeer, geen actiegerichte data.

## 2. Meta Ads Performance

**Campagne:** 2026: SYBB (`120239435987290239`) — status **PAUSED**, dagbudget €100,00 (inactief)

| Metric | Gisteren (17 jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n/a | n/a | → |
| CPC | n/a | n/a | → |
| Frequency | n/a | n/a | → |

*Geen delivery in de periode 11–17 juli. Alle waarden zijn nul omdat de campagne gepauzeerd is.*

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | geen actieve ads | — | — | geen PostHog data | geen PostHog data |

**Beste variant:** n.v.t. — geen actieve ads gisteren.
**Slechtste variant:** n.v.t. — geen actieve ads gisteren.

### Context (laatste delivery)
Ter referentie, de laatste keer dat de campagne wél liep (19–30 april 2026):
- Impressions: 2.756 · Clicks: 61 · Spend: €43,81
- CTR: 2,21% · CPC: €0,72 · Frequency: 1,35
- Landing page views: 34 · Initiate checkouts: 2

Deze cijfers zijn puur historisch en zeggen niets over gisteren.

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

⚪ = **geen data**. De PostHog MCP is niet verbonden in deze sessie, dus startyourballoonbusiness.com kon niet worden uitgevraagd. Zonder actief advertentieverkeer zou het volume sowieso verwaarloosbaar zijn geweest.

## 4. Funnel Drop-off
Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** niet te bepalen — geen advertentieverkeer en geen PostHog data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne inactief:** "2026: SYBB" staat op PAUSED en levert al sinds ~1 mei 2026 geen verkeer. Er wordt momenteel geen budget richting de SYBB funnel gestuurd.
- 🚩 **PostHog databron ontbreekt:** de PostHog MCP is niet gekoppeld in deze sessie. Zolang dit niet is opgelost, kan het dagelijkse rapport de landing page kant (bounce, scroll, CTA, funnel) niet meten of cross-referencen — de kern van dit rapport valt daarmee weg.

## 6. Top 3 Acties voor Vandaag
1. **Besluit over de SYBB campagne.** Bepaal of "2026: SYBB" weer aan moet (reactiveren + nieuwe/refreshed creatives) of dat de focus elders ligt. Nu staat er budget gereserveerd (€100/dag) dat niets doet. *Escalatie: Rood (strategie).*
2. **PostHog MCP koppelen.** Verbind de PostHog MCP zodat de landing page metrics weer opgehaald kunnen worden; zonder deze bron levert dit dagrapport structureel maar halve waarde. *Escalatie: Geel (Robin actie).*
3. **Rapport-scope bevestigen.** Als de campagne bewust uit staat, overweeg het dagelijkse SYBB rapport te pauzeren of om te zetten naar een "wake on activity" trigger tot er weer een actieve campagne draait, om lege rapporten te voorkomen. *Escalatie: Geel (Robin goedkeuring).*

---
*Meta Ads data via Pipeboard MCP (account: Sempertex Ad Account, act_567892422940728). PostHog data: niet beschikbaar (MCP niet verbonden). Geen Google-diensten gebruikt voor dit rapport.*
