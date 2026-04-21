# SYBB Daily Report, 2026-04-19

## 1. Samenvatting

Eerste live dag van de hernieuwde SYBB campagne (2026: SYBB, actief onder de naam "2026: SYBB - Kopie" sinds 2026-04-19 14:25). €45,65 spend voor 3.320 impressies en 75 clicks, CTR 2,26%, CPC €0,61. 4 initiate checkouts gerapporteerd door de Meta pixel met een totale action value van €1.400. De campagne start is goed, maar de CPC ligt 22% boven de target van €0,50. H12 is direct de beste variant op CTR, CPC en LPV-rate.

> **Data notitie:** PostHog MCP is in deze omgeving niet beschikbaar. Landing Page metrics in dit rapport (bounce proxy, LPV rate, IC rate) komen uit de Meta Ads pixel, niet uit PostHog. Zodra de PostHog MCP weer draait vullen we sectie 3 en 4 aan met session duration, scroll depth distribution en funnel drop-off per UTM.

## 2. Meta Ads Performance

Campagne: **2026: SYBB - Kopie** (ID 120243293329420239), Sempertex Ad Account (act_567892422940728). De originele "2026: SYBB" campagne staat op PAUSED sinds 2026-04-19 14:29 en wordt niet meegeteld.

| Metric | Gisteren (19-04) | 7d Gemiddelde | Trend |
|--------|------------------|---------------|-------|
| Spend | €45,65 | €45,65 | n.v.t. |
| Impressions | 3.320 | 3.320 | n.v.t. |
| Clicks (all) | 75 | 75 | n.v.t. |
| Link clicks | 49 | 49 | n.v.t. |
| CTR | 2,26% | 2,26% | n.v.t. |
| CPC (all) | €0,61 | €0,61 | n.v.t. |
| Cost per link click | €0,93 | €0,93 | n.v.t. |
| CPM | €13,75 | €13,75 | n.v.t. |
| Reach | 2.745 | 2.745 | n.v.t. |
| Frequency | 1,21 | 1,21 | n.v.t. |
| Landing Page Views | 37 | 37 | n.v.t. |
| Initiate Checkout | 4 | 4 | n.v.t. |
| IC action value | €1.400 | €1.400 | n.v.t. |
| Cost per IC | €11,41 | €11,41 | n.v.t. |

Trend is nog niet bruikbaar: 1 dag live, 7d gemiddelde = dag 1. Vanaf dag 3 wordt de rolling gemiddelde informatief.

### Ad Variant Performance

Let op: bij "Clicks" staan hier link clicks (niet alle clicks), omdat alleen link clicks relevant zijn voor landing page behavior. "LPV rate" = landing_page_view / link_click als proxy voor het omgekeerde van bounce/page-load-failure. Zuivere bounce en scroll depth per UTM vragen PostHog.

| Ad (utm_content proxy) | Impr. | Link clicks | CTR | CPC (link) | LPV | LPV rate | IC |
|------------------------|-------|-------------|-----|-----------|-----|----------|----|
| H11,B3,CTA5 | 1.806 | 25 | 2,21% | €0,92 | 20 | 80,0% | 2 |
| H12,B3,CTA5 | 567 | 8 | 2,82% | €0,96 | 5 | 62,5% | 1 |
| H13,B3,CTA5 | 947 | 16 | 2,01% | €0,93 | 12 | 75,0% | 1 |

**Beste variant: H12,B3,CTA5.** Hoogste CTR (2,82% vs 2,21% en 2,01%), laagste all-clicks CPC (€0,48), en genereerde 1 IC op het laagste budget (€7,70 spend). Kleinste delivery, dus statistisch vroeg om conclusies, maar signaal is duidelijk positief.

**Slechtste variant: H13,B3,CTA5.** Laagste CTR (2,01%), hoogste all-clicks CPC (€0,79) en hoogste CPM (€15,79). Verbrandt budget relatief snel zonder bovengemiddeld te leveren.

**H11,B3,CTA5** levert het meeste volume en de beste LPV rate (80%), dus de ad-naar-pagina overgang werkt. Maakt 50% van alle IC conversies (2 van 4).

## 3. Landing Page Health

**PostHog MCP niet beschikbaar in deze omgeving. Deze sectie gebruikt daarom alleen Meta pixel data.**

| Metric | Gisteren | Target | Status | Bron |
|--------|----------|--------|--------|------|
| Link click naar LPV rate | 75,5% (37/49) | >75% | Groen | Meta pixel |
| LPV naar IC rate | 10,8% (4/37) | >5% | Groen | Meta pixel |
| Bounce Rate | geen data | <55% | Onbekend | PostHog |
| Avg Session Duration | geen data | >90s | Onbekend | PostHog |
| Scroll 25% / 50% / 75% / 100% | geen data | >80/60/40/20% | Onbekend | PostHog |
| CTA Click Rate | geen data | >4% | Onbekend | PostHog |

Het feit dat 24,5% van de link clicks nooit als LPV binnenkomt bij Meta (49 link clicks, 37 LPV) is een signaal om scherp in de gaten te houden. Dit kan duiden op trage pageload, ad blockers, of bounces voordat het pixel fires. Zodra PostHog weer draait: cross-check met PostHog pageviews per utm_content.

## 4. Funnel Drop-off (Meta pixel)

```
Impressie          3.320  (100%)
Link click            49  (1,5%   van impressies)
Landing page view     37  (75,5%  van link clicks, CTR * LPV rate = 1,11% impressie > LPV)
Initiate checkout      4  (10,8%  van LPV, 0,12% van impressies)
Purchase          geen data (niet gemeten als IC ≠ purchase)
```

**Grootste lek:** impressie > link click (1,5% CTR), standaard voor koude verkeer. Hierna LPV > IC (10,8%) is feitelijk sterker dan target. De rij om zorgen over te maken is link click > LPV (75,5%), omdat hier zonder PostHog niet zichtbaar is of het technisch verlies (pageload, blockers) of gedrag (instant bounce) is.

## 5. Rode Vlaggen

- **CPC €0,61 boven target €0,50.** Campagne zit in leerfase (dag 1), dus houd aan; als CPC op dag 3 nog boven €0,55 blijft, budget shiften naar H12.
- **H13 CPM €15,79, CPC €0,79, laagste CTR.** Al één flag bij dag 1. Herhaalt dit patroon op dag 2, overweeg pauze.
- **Link click naar LPV gat 24,5%.** Zonder PostHog niet te diagnosticeren. Controleer zodra PostHog beschikbaar is of de echte pageviews op startyourballoonbusiness.com overeenkomen met de 37 LPV van Meta.
- **Frequency 1,21 is niet kritisch** (target <3). Nog geen fatigue risico.

## 6. Top 3 Acties voor Vandaag

1. **PostHog MCP herstellen.** Zonder PostHog verliezen we bounce, scroll, CTA click rate en session recordings, allemaal de helft van de waarde van dit rapport. Actie: check MCP configuratie in `.claude/settings.json` of relevante config, en verifieer dat het PostHog project "Default project" bereikbaar is.
2. **Dag 1 observeren, nog niet optimaliseren.** Laat alle 3 ads draaien tot en met vanavond 2026-04-20 om voldoende signaal per variant op te bouwen. Eerste optimalisatie call op 2026-04-21 ochtend op basis van 48 uur data. Impact: voorkomt premature pauzes bij variance.
3. **Voorbereiden H12 budget shift.** Als H12 op 2026-04-21 nog steeds hoogste CTR en laagste CPC heeft, shift 50% van H13 budget naar H12 en houd H11 gelijk. Verwachte impact: CPC campagne breed omlaag richting €0,50 target.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-19_sybb_report.md`
**Data bronnen:** Meta Ads MCP (Pipeboard), PostHog MCP niet beschikbaar.
**Geen Google MCPs gebruikt.**
