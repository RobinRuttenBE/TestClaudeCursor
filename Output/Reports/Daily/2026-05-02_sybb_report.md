# SYBB Daily Report — 2026-05-02

## 1. Samenvatting
Campagne **2026: SYBB** had op 2026-05-02 **geen activiteit** (status PAUSED sinds 2026-04-19; geen spend, geen impressions, geen clicks). Het rolling 7-daags gemiddelde over 2026-04-26 t/m 2026-05-02 is dus eveneens nul. PostHog data ontbreekt in deze sessie (PostHog MCP niet beschikbaar) — de Landing Page Health en Funnel Drop-off secties kunnen niet ingevuld worden zonder die data.

> **Run-context:** strikte run-regel actief — alleen Meta Ads MCP (Pipeboard) is gebruikt. Geen Google MCP's, geen schrijven naar Google Sheet, output uitsluitend lokaal.

---

## 2. Meta Ads Performance

**Campagne ID:** `120239435987290239` — "2026: SYBB" — status **PAUSED** (laatste update 2026-04-19)
**Account:** Sempertex Ad Account (`act_567892422940728`)

| Metric | Gisteren (2026-05-02) | 7d gemiddelde (2026-04-26 → 2026-05-02) | Trend |
|--------|----------------------|------------------------------------------|-------|
| Spend | €0,00 | €0,00 | → (paused) |
| Impressions | 0 | 0 | → (paused) |
| Clicks | 0 | 0 | → (paused) |
| CTR | n.v.t. | n.v.t. | → (paused) |
| CPC | n.v.t. | n.v.t. | → (paused) |
| Frequency | n.v.t. | n.v.t. | → (paused) |

### Referentie: laatste actieve periode (2026-04-13 → 2026-04-19, 7 dagen)
Voor context: dit is de laatste 7-daagse periode waarin de campagne wél liep, vóór de pauze op 2026-04-19.

| Metric | Totaal | Daggemiddelde |
|--------|--------|---------------|
| Spend | €594,24 | €84,89 |
| Impressions | 42.770 | 6.110 |
| Clicks | 941 | 134 |
| CTR (blended) | 2,20% | — |
| CPC (blended) | €0,63 | — |
| Frequency (gemiddeld) | — | ~1,41 |

### Ad Variant Performance
Geen ad-level data beschikbaar voor 2026-05-02 (campagne paused). Voor de variant-analyse uit de actieve periode, zie het rapport van 2026-05-03 (`2026-05-03_ads_report.md`), dat de last-30d ad-level performance bevat (H11/H12/H13/H14/H15 — H12 en H14 als top performers, H13 als underperformer).

---

## 3. Landing Page Health
**Niet beschikbaar in deze run** — PostHog MCP is niet geladen in deze sessie. Strikte run-regel staat alleen Meta Ads MCP en PostHog MCP toe; PostHog is niet aanwezig in de beschikbare tools.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ data ontbreekt |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ data ontbreekt |
| Scroll 25% | n.v.t. | n.v.t. | >80% | ⚪ data ontbreekt |
| Scroll 50% | n.v.t. | n.v.t. | >60% | ⚪ data ontbreekt |
| Scroll 75% | n.v.t. | n.v.t. | >40% | ⚪ data ontbreekt |
| Scroll 100% | n.v.t. | n.v.t. | >20% | ⚪ data ontbreekt |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | ⚪ data ontbreekt |

> Om dit blok te vullen: laad PostHog MCP in de sessie of lever de metrics handmatig aan (pageviews, bounce, scroll-distributie, CTA-clicks per `utm_content` voor 2026-05-02).

---

## 4. Funnel Drop-off
Niet berekenbaar zonder PostHog data. Bovendien zou de funnel sowieso leeg zijn voor 2026-05-02 omdat er geen ad-traffic naar de landing page is gestuurd — eventuele pageviews komen uit organisch/direct/legacy bronnen, niet uit de SYBB-campagne.

```
Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)
```

**Grootste lek:** n.v.t. (geen funnel input vanuit Meta).

---

## 5. Rode Vlaggen 🚩

1. **Campagne staat 13 dagen op pauze (sinds 2026-04-19).**
   - Wat: geen ad-traffic naar startyourballoonbusiness.com sinds 14 dagen.
   - Waarom: spend = €0 voor 14 opeenvolgende dagen, terwijl SYBB nog steeds het primaire workshop-funnel is.
   - Impact: pipeline droogt op — booking-volume daalt met een vertraging van ~7-14 dagen.

2. **Tracking-anomalie blijft onopgelost.**
   - Wat: pixel rapporteerde tijdens actieve periode €44.247 purchase value op campagne-niveau (€7.374/purchase) — 41,76x ROAS is niet realistisch.
   - Waarom: gesignaleerd in het 2026-05-03 rapport, nog geen audit voltooid.
   - Impact: zonder audit kunnen we ROAS-beslissingen niet vertrouwen bij relaunch.

3. **PostHog data-pipeline ontbreekt in dit rapport.**
   - Wat: PostHog MCP is niet geladen — wij kunnen LP-health niet auto-rapporteren.
   - Waarom: de skill rekent op PostHog MCP als data bron; deze is in deze sessie afwezig.
   - Impact: cross-reference (ad CTR vs LP bounce, frequency vs bounce) onmogelijk → halve diagnose.

---

## 6. Top 3 Acties voor Vandaag

1. **Beslis: relaunch SYBB campagne of definitief afsluiten.** (Rood — strategie)
   - Waarom: 14 dagen geen ad-traffic; pipeline-effect wordt zichtbaar in komende 1-2 weken.
   - Hoe: Robin neemt beslissing. Bij relaunch → eerst Actie 2 (tracking-audit) afronden, daarna H12+H14 winnaars opnieuw activeren met dagelijks budget €40-60 (Hormozi 70/20/10).
   - Verwachte impact: herstart traffic-flow naar funnel, waardoor PostHog/booking metrics weer leesbaar worden.

2. **Voer pixel/attributie audit uit op de SYBB pixel.** (Oranje — Robin uitvoert)
   - Waarom: rapport 2026-05-03 toont €44.247 op één ad als purchase value — duidt op dubbele firing of verkeerd value-signaal. Niet vertrouwen op ROAS tot opgelost.
   - Hoe: in Meta Events Manager → SYBB pixel → check de Purchase event configuratie en deduplicatie. Test event-tool gebruiken op /booking/thank-you. Vergelijk met Wix order-export.
   - Verwachte impact: betrouwbare ROAS bij relaunch → kunnen winnaars op merit kiezen.

3. **PostHog MCP integratie verifiëren in Claude omgeving.** (Geel — Robin goedkeuring)
   - Waarom: SKILL.md verwacht PostHog MCP, maar tool is vandaag niet aanwezig. Zonder fix levert dit dagelijkse rapport blijvend incomplete data.
   - Hoe: check `.mcp.json` / Claude desktop config voor PostHog server registratie; herstart Claude sessie; valideer met test-call.
   - Verwachte impact: dagelijks rapport kan weer volledig draaien (LP health + funnel + cross-reference).

---

## Bijlage: Data-bronnen en beperkingen

- **Meta Ads:** Pipeboard MCP, account `act_567892422940728`, campagne `120239435987290239` ("2026: SYBB"). Insights opgevraagd voor 2026-05-02 (single-day) en `last_7d` — beide leeg. `last_30d` met `time_breakdown=day` toont laatste actieve dag = 2026-04-19.
- **PostHog:** **Niet opgevraagd** — MCP server niet beschikbaar in deze sessie (`mcp__posthog__*` ontbreekt in tool-lijst).
- **Google Sheet (Meta Ads Tracker):** **Niet bijgewerkt** — strikte run-regel verbiedt Google MCP-aanroepen voor deze run.
- **Output:** alleen lokaal opgeslagen in `Output/Reports/Daily/2026-05-02_sybb_report.md`.
