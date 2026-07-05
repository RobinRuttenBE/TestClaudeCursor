# SYBB Daily Report — 4 July 2026

> Gegenereerd op 5 July 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP.

## 1. Samenvatting

Er is **geen advertentieactiviteit** te rapporteren voor 4 juli. De campagne `2026: SYBB` staat op **PAUSED** en heeft gisteren (en de hele afgelopen 7 dagen) nul impressies, clicks en spend gedraaid. De laatste maand met daadwerkelijke delivery was **april 2026**. Daarnaast kon de **PostHog data niet worden opgehaald**: de PostHog MCP was deze sessie niet beschikbaar, dus er is geen landing page data. Netto: geen live funnel om te beoordelen. De belangrijkste actie ligt op operationeel niveau (campagne herstarten of tracking herstellen), niet op optimalisatie.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID `120239435987290239`) — status **PAUSED**, dagbudget €100,00, objective OUTCOME_SALES.

| Metric | Gisteren (4 jul) | 7d Gemiddelde (27 jun–3 jul) | Trend |
|--------|------------------|------------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Geen delivery.** De Meta Insights API gaf een lege dataset terug voor zowel 4 juli als het 7-daagse referentievenster. De campagne draait niet.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | — | — | — | — | — |

Geen actieve ads → geen variant-data. Ad-level insights voor 4 juli waren leeg.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

### Historische context (laatste actieve periode)

Ter referentie — de campagne heeft in 2026 gedraaid in de volgende maanden (bron: Meta Insights, `maximum` breakdown):

| Maand | Spend | Impressions | Clicks | CTR | CPC |
|-------|-------|-------------|--------|-----|-----|
| Jan 2026 | €101,74 | 16.268 | 167 | 1,03% | €0,61 |
| Mrt 2026 | €1.323,83 | 189.067 | 9.965 | 5,27% | €0,13 |
| Apr 2026 | €1.059,47 | 91.839 | 1.935 | 2,11% | €0,55 |

Sinds april 2026 is er geen spend meer geregistreerd op deze campagne.

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

**PostHog data niet beschikbaar.** De PostHog MCP server heeft deze sessie geen tools aangeleverd (verbinding niet voltooid). Er kon dus geen pageview-, bounce-, scroll- of CTA-data voor startyourballoonbusiness.com worden opgehaald. ⚪ = geen meting.

## 4. Funnel Drop-off

```
Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)
```

Niet te berekenen: zowel Meta Ads (0 traffic) als PostHog (geen data) ontbreken. Zonder ad-traffic én zonder landing page events is er geen funnel om door te meten.

**Grootste lek:** n.v.t.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat op PAUSED** — `2026: SYBB` levert geen traffic. Als dit onbedoeld is, is dit de meest urgente fix (0 nieuwe SYBB-leads zolang dit zo blijft).
- 🚩 **PostHog MCP niet verbonden** — landing page tracking/rapportage is deze run blind. Kan geen ad-pagina mismatches of on-page gedrag monitoren.
- ℹ️ Geen CPC-, frequency- of bounce-anomalieën te melden, simpelweg omdat er geen data is (niet omdat alles gezond is).

## 6. Top 3 Acties voor Vandaag

1. **Bevestig de status van `2026: SYBB` en herstart indien bedoeld actief.** Waarom: campagne staat op PAUSED met €0 delivery sinds april; elke dag pauze = 0 SYBB-instroom. Hoe: check in Meta Ads Manager of de pauze bewust is (seizoen/budget) of per ongeluk; zo bewust → noteer geplande herstartdatum, zo onbedoeld → heractiveer. Escalatie: Geel (Robin goedkeuring vóór heractivatie i.v.m. budget).
2. **Herstel de PostHog MCP-verbinding.** Waarom: zonder PostHog is het dagelijkse rapport half blind (geen bounce/scroll/CTA/funnel). Hoe: PostHog MCP opnieuw autoriseren/verbinden via `/mcp` in een interactieve sessie, daarna een testrun draaien. Escalatie: Groen (technische fix, geen strategie).
3. **Plan de volgende SYBB-flight en tracking-check.** Waarom: bij heractivatie moet UTM-tagging (utm_content = hXX_bX_ctaX) en de Meta Pixel weer kloppen zodat het rapport meteen zinvol is. Hoe: run `/tracking-check` op startyourballoonbusiness.com en valideer UTM-conventie vóór de eerste nieuwe ad live gaat. Escalatie: Geel.

---

### Databron-status
- **Meta Ads (Pipeboard MCP):** ✅ verbonden — campagne bevestigd PAUSED, 0 delivery in rapportvenster.
- **PostHog MCP:** ❌ niet beschikbaar deze sessie — geen landing page data opgehaald.
