# SYBB Daily Report, 2026-05-03

## 1. Samenvatting
Campagne **2026: SYBB** had op 2026-05-03 **geen activiteit** (status PAUSED sinds 2026-04-19, dag 14 in pauze). Het rolling 7-daags gemiddelde (2026-04-27 t/m 2026-05-03) is dus eveneens nul. PostHog data ontbreekt in deze sessie (PostHog MCP niet beschikbaar), waardoor Landing Page Health en Funnel Drop-off niet ingevuld kunnen worden.

> **Run-context:** strikte run-regel actief, alleen Meta Ads MCP (Pipeboard) is gebruikt. Geen Google MCP's, geen schrijven naar Google Sheet, output uitsluitend lokaal.

---

## 2. Meta Ads Performance

**Campagne ID:** `120239435987290239`, "2026: SYBB", status **PAUSED** (laatste update 2026-04-19, 14 dagen geleden)
**Account:** Sempertex Ad Account (`act_567892422940728`)
**Daily budget op pauze-moment:** €100,00

| Metric | Gisteren (2026-05-03) | 7d gemiddelde (2026-04-27 t/m 2026-05-03) | Trend |
|--------|----------------------|------------------------------------------|-------|
| Spend | €0,00 | €0,00 | flat (paused) |
| Impressions | 0 | 0 | flat (paused) |
| Clicks | 0 | 0 | flat (paused) |
| CTR | n.v.t. | n.v.t. | flat (paused) |
| CPC | n.v.t. | n.v.t. | flat (paused) |
| Frequency | n.v.t. | n.v.t. | flat (paused) |

### Referentie: laatste actieve periode (2026-04-13 t/m 2026-04-19, 7 dagen)
Voor context, dit is de laatste 7-daagse periode waarin de campagne wél liep, vóór de pauze op 2026-04-19.

| Metric | Totaal | Daggemiddelde |
|--------|--------|---------------|
| Spend | €594,24 | €84,89 |
| Impressions | 42.770 | 6.110 |
| Clicks | 941 | 134 |
| Reach | 20.062 | n.v.t. |
| CTR (blended) | 2,20% | n.v.t. |
| CPC (blended) | €0,63 | n.v.t. |
| Frequency (gemiddeld) | 2,13 | n.v.t. |
| Landing page views | 422 | 60 |
| Add to cart | 28 | 4 |
| Initiate checkout | 23 | 3 |
| Purchases (pixel) | 4 | n.v.t. |
| Lead/registration (pixel) | 5 | n.v.t. |

> Pixel-purchase value (€43.750 op CompleteRegistration, €1.473,50 op Purchase) is bekend onbetrouwbaar, zie sectie 5 (rode vlag 2).

### Ad Variant Performance
Geen ad-level data beschikbaar voor 2026-05-03 (campagne paused, geen impressies). Voor de variant-analyse uit de actieve periode is het meest recente referentiepunt het `2026-05-04_ads_report.md` (last 30d ad-level performance):

- **Beste CTR:** H15,B3,CTA5 (BATCH 2 origineel), 6,37% CTR, CPC €0,23 (lage spend)
- **Beste volume + efficiency:** H12,B3,CTA5 (BATCH 2 origineel), CTR 4,73%, CPC €0,29
- **Beste consistente ROAS:** H11,B3,CTA5 (hoofdcampagne, Kopie 1), 4 purchases (€1.473,50) op €521,56 spend = 2,83x
- **Slechtst:** H13,B3,CTA5 (Kopie campagne, adset Kopie 3), CPC €0,93, 1 IC, geen purchases

---

## 3. Landing Page Health
**Niet beschikbaar in deze run.** PostHog MCP is niet geladen in deze sessie. Strikte run-regel staat alleen Meta Ads MCP en PostHog MCP toe; PostHog ontbreekt in de beschikbare tools (search op "posthog" en op "analytics pageview events tracking" gaf geen match).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n.v.t. | n.v.t. | <55% | data ontbreekt |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | data ontbreekt |
| Scroll 25% | n.v.t. | n.v.t. | >80% | data ontbreekt |
| Scroll 50% | n.v.t. | n.v.t. | >60% | data ontbreekt |
| Scroll 75% | n.v.t. | n.v.t. | >40% | data ontbreekt |
| Scroll 100% | n.v.t. | n.v.t. | >20% | data ontbreekt |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | data ontbreekt |

> Om dit blok te vullen, laad PostHog MCP in de sessie of lever de metrics handmatig aan (pageviews, bounce, scroll-distributie, CTA-clicks per `utm_content` voor 2026-05-03).

---

## 4. Funnel Drop-off
Niet berekenbaar zonder PostHog data. Bovendien zou de funnel sowieso leeg zijn voor 2026-05-03, omdat er geen ad-traffic naar de landing page is gestuurd (campagne dag 14 paused). Eventuele pageviews komen uit organisch/direct/legacy bronnen, niet uit de SYBB-campagne.

```
Pageview (n.v.t.) -> Scroll 50% (n.v.t.) -> CTA Click (n.v.t.) -> /booking (n.v.t.)
```

**Grootste lek:** n.v.t. (geen funnel input vanuit Meta).

---

## 5. Rode Vlaggen

1. **Campagne staat 14 dagen op pauze (sinds 2026-04-19).**
   - Wat: geen ad-traffic naar startyourballoonbusiness.com sinds 14 dagen.
   - Waarom: spend = €0 voor 14 opeenvolgende dagen, terwijl SYBB nog steeds het primaire workshop-funnel is.
   - Impact: pipeline droogt op, booking-volume daalt met een vertraging van ~7 tot 14 dagen, dus piekeffect treedt deze week in.

2. **Tracking-anomalie blijft onopgelost.**
   - Wat: pixel rapporteerde tijdens actieve periode €43.750 op CompleteRegistration (5 events, €8.750 per registratie) en €1.473,50 op 4 Purchases. ROAS-blends boven 40x op campagne-niveau en 200x op één ad zijn niet realistisch.
   - Waarom: gesignaleerd in eerdere ads/sybb rapporten (2026-05-02, 2026-05-04), nog geen audit voltooid.
   - Impact: zonder audit kunnen we ROAS-beslissingen niet vertrouwen bij relaunch, winnaars-keuze blijft op CTR + CPC + IC-volume in plaats van waarde.

3. **PostHog data-pipeline ontbreekt in dit rapport.**
   - Wat: PostHog MCP is niet geladen, LP-health kan niet auto-gerapporteerd worden.
   - Waarom: de skill (`skills/daily-sybb-report/SKILL.md`) rekent op PostHog MCP als data bron; deze is in deze sessie afwezig.
   - Impact: cross-reference (ad CTR vs LP bounce, frequency vs bounce) onmogelijk, halve diagnose. Tweede dag op rij dat dit blok leeg blijft.

---

## 6. Top 3 Acties voor Vandaag

1. **Beslis: relaunch SYBB campagne of definitief afsluiten.** (Rood, strategie)
   - Waarom: 14 dagen geen ad-traffic, pipeline-effect zichtbaar in komende 1 tot 2 weken. Elke dag verder pauze vergroot de gap die later moet worden ingelopen met hogere CPC.
   - Hoe: Robin neemt beslissing. Bij relaunch eerst Actie 2 (tracking-audit) afronden, daarna H12 + H11 winnaars opnieuw activeren met dagelijks budget €40 tot €60 (Hormozi 70/20/10). H15 als spike-test naast (10% budget). H13 (Kopie) niet opnieuw activeren in huidige vorm.
   - Verwachte impact: herstart traffic-flow naar funnel, waardoor PostHog/booking metrics weer leesbaar worden.

2. **Voer pixel/attributie audit uit op de SYBB pixel.** (Oranje, Robin uitvoert)
   - Waarom: €43.750 op 5 CompleteRegistration events en €44.247 op één ad als purchase value duiden op dubbele firing of een verkeerd value-signaal. Niet vertrouwen op ROAS tot opgelost.
   - Hoe: in Meta Events Manager > SYBB pixel > check de Purchase + CompleteRegistration event configuratie en deduplicatie. Test event-tool gebruiken op /booking/thank-you. Vergelijk met Wix order-export voor 2026-04-13 t/m 2026-04-19 (verwachte 4 orders, validatie-totaal).
   - Verwachte impact: betrouwbare ROAS bij relaunch, winnaars op merit kiezen.

3. **PostHog MCP integratie verifiëren in Claude omgeving.** (Geel, Robin goedkeuring)
   - Waarom: SKILL.md verwacht PostHog MCP, maar tool is twee dagen op rij niet aanwezig. Zonder fix levert dit dagelijkse rapport blijvend incomplete data.
   - Hoe: check `.mcp.json` of Claude desktop config voor PostHog server registratie, herstart Claude sessie, valideer met test-call (`mcp__posthog__list_projects` of vergelijkbaar).
   - Verwachte impact: dagelijks rapport kan weer volledig draaien (LP health, funnel, cross-reference), waarde van rapport komt terug op niveau.

---

## Bijlage: Data-bronnen en beperkingen

- **Meta Ads:** Pipeboard MCP, account `act_567892422940728`, campagne `120239435987290239` ("2026: SYBB"). Insights opgevraagd voor 2026-05-03 (single-day, leeg) en 2026-04-27 t/m 2026-05-03 met `time_breakdown=day` (alle 7 dagen leeg). Campagne-status bevestigd via `get_campaigns`: PAUSED, `updated_time` 2026-04-19. Referentieperiode 2026-04-13 t/m 2026-04-19 opgehaald voor context.
- **PostHog:** **Niet opgevraagd**, MCP server niet beschikbaar in deze sessie (`mcp__posthog__*` ontbreekt in tool-lijst, ToolSearch leverde geen match).
- **Google Sheet (Meta Ads Tracker):** **Niet bijgewerkt**, strikte run-regel verbiedt Google MCP-aanroepen voor deze run.
- **Output:** alleen lokaal opgeslagen in `Output/Reports/Daily/2026-05-03_sybb_report.md`.
