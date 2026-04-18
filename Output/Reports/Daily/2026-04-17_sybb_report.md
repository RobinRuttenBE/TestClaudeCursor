# SYBB Daily Report, 17 april 2026

## 1. Samenvatting
CTR steeg naar 2,32% (boven 7d gemiddelde) en H12 bewijst zich met CTR 4,24% en CPC €0,32, maar de totale campagne CPC zit op €0,62 (24% boven target) en de volledige bottom funnel stond stil: 0 add to cart, 0 initiated checkout, 0 purchase. H11 slokt 76% van het budget op met CPC €0,72 en geen conversies, terwijl H12 op lage spend (€8,84) het beste presteert. Het lek zit tussen landing page view en view content (90% drop).

## 2. Meta Ads Performance

| Metric | Gisteren (17 apr) | 7d Gemiddelde (10 t/m 16 apr) | Trend |
|--------|-------------------|-------------------------------|-------|
| Spend | €86,54 | €102,21 | ↓ |
| Impressions | 5.993 | 8.761 | ↓ |
| Clicks (all) | 139 | 181 | ↓ |
| Link clicks | 78 | 95,7 | ↓ |
| Landing page views | 63 | 75 | ↓ |
| CTR | 2,32% | 2,07% | ↑ |
| CPC | €0,62 | €0,56 | ↑ |
| Frequency (daily) | 1,39 | 2,15 (7d cum.) | → |
| Reach | 4.306 | 28.540 (7d cum.) | → |
| Add to cart | 0 | 5,1 | ↓ |
| Initiated checkout | 0 | 3,4 | ↓ |
| Complete registration | 0 | 0,9 | ↓ |
| Purchases | 0 | 0,86 | ↓ |

**Opmerking:** 7d gemiddelde berekend uit 10 t/m 16 april totalen (€715,50 spend, 61.326 impressions, 1.267 clicks, 670 link clicks, 525 LP views, 36 ATCs, 24 checkouts, 6 purchases).

### Ad Variant Performance (17 april)

| Ad (utm_content) | Spend | Impressions | Clicks | CTR | CPC | Link clicks | LP Views | ATC | Checkouts | Purchases |
|------------------|-------|-------------|--------|-----|-----|-------------|----------|-----|-----------|-----------|
| h11_b3_cta5 | €65,85 | 4.378 | 91 | 2,08% | €0,72 | 52 | 42 | 0 | 0 | 0 |
| h13_b3_cta5 | €11,85 | 954 | 20 | 2,10% | €0,59 | 10 | 9 | 0 | 0 | 0 |
| h12_b3_cta5 | €8,84 | 661 | 28 | 4,24% | €0,32 | 16 | 12 | 0 | 0 | 0 |

**Beste variant:** H12 is dominant op efficientie. CTR 4,24% (2x gemiddeld), CPC €0,32 (36% onder target), LP view ratio 75% (12 van 16 link clicks). Ondervoedd qua budget (10% van totaal) maar presteert als enige boven target.
**Slechtste variant:** H11 krijgt 76% van de spend maar levert CPC €0,72 (44% boven target) en CTR 2,08%. LP view ratio is gezond (42 van 52, 81%) maar daarna valt alles weg. Geen conversie signaal uit de drukste variant is een budgetallocatie probleem.

## 3. Landing Page Health

> **PostHog MCP niet beschikbaar in deze sessie.** Landing page metrics (bounce rate, scroll depth, session duur, CTA click rate, session recordings) konden niet worden opgehaald. Zelfde situatie als 16 april. Actie 3 uit gisteren staat nog open.

Proxy observaties vanuit Meta pixel data:
- Link clicks, LP views ratio: 78 link clicks, 63 LP views (81%). 19% drop tussen klik en pagina load, mobiele afhaak blijft normaal.
- LP view, view content ratio: 63 LP views, 6 view content events (9,5%). Dit is het duidelijkste signaal dat de pagina niet weet wie door te laten scrollen of dieper te engagen.
- 0 add to cart op 63 LP views is een volledige breuk van de bottom funnel op een dag.

**Action:** PostHog MCP verbinding herstellen vóór volgende run. Zonder LP analytics blijft elke diagnose boven de funnel puur pixel proxy.

## 4. Funnel Drop-off (Meta pixel data)

| Stap | Events | % vs vorige stap |
|------|--------|------------------|
| Link click | 78 | 100% |
| Landing page view | 63 | 81% |
| View content | 6 | 9,5% |
| Add to cart | 0 | 0% |
| Initiated checkout | 0 | — |
| Complete registration | 0 | — |
| Purchase | 0 | — |

**Grootste lek:** LP view naar view content (63 naar 6 = 90% drop). Dit is erger dan gisteren (83% drop) en wijst op een pagina die bezoekers niet genoeg triggert om content engagement te registreren. Daarna is de funnel volledig dood: 0 ATCs is een hard stopsignaal, niet alleen een optimalisatie target.

> **Data caveat:** pixel action_values in 7d data blijven vertekend (€44.247 complete_registration value = niet realistisch). Negeer euro waarden uit pixel events, focus op event counts.

## 5. Rode Vlaggen

- **CPC €0,62 = 24% boven target** (€0,50). H11 tikt €0,72 (+44%), H13 €0,59 (+18%). Alleen H12 zit met €0,32 onder target.
- **Volledige bottom funnel stilstand:** 0 ATC, 0 initiated checkout, 0 purchase op 63 LP views. Eerste nuldag op ATC in de afgelopen 8 dagen (7d gemiddelde: 5,1 ATC/dag).
- **H11 budget efficiency crisis:** 76% van spend (€65,85), hoogste CPC in de campagne, 0 conversies tweede dag op rij.
- **LP view naar view content drop verslechtert:** 83% gisteren, 90% vandaag. De pagina lijkt slechter te gaan, niet beter.
- **Spend daling 15%** vs 7d gemiddelde, combineert met lagere impressies (-32%) en clicks (-23%). Delivery issue of audience fatigue op BATCH 2 adsets.
- **PostHog data ontbreekt 2 dagen op rij.** Blinde vlek op LP kwaliteit wordt structureel.

## 6. Top 3 Acties voor Vandaag

1. **Herbalanceer budget van H11 naar H12.** H11 verbrandt €65,85/dag aan CPC €0,72 zonder conversies, H12 presteert op CTR 4,24% en CPC €0,32 met maar €8,84 budget. Concreet: pause H11 adset of cap op €20/dag, verschuif €30 naar H12 adset. Verwachte impact: gemiddelde CPC daalt onder €0,50, meer link clicks voor zelfde spend. **Escalatie:** Geel (Robin goedkeuring voor budget verschuiving).
2. **Diagnose booking funnel end to end.** 0 ATC op 63 LP views is geen conversion optimalisatie probleem, dat is een stuk funnel. Open startyourballoonbusiness.com, klik CTA, probeer checkout. Check (a) of CTA buttons werken, (b) of de /booking pagina laadt, (c) of er een JS error in console staat. **Escalatie:** Oranje (Wix Editor).
3. **PostHog MCP herstellen, nu urgent.** Twee dagen op rij ontbreekt de LP data. Zonder bounce rate en scroll depth weten we niet waar de 90% LP view naar view content drop vandaan komt (hero faalt? CTA niet zichtbaar? formulier blokkeert?). Fix in .mcp.json of relevante config. **Escalatie:** Groen (auto).

---

**Data bronnen:** Meta Ads MCP (Pipeboard), account act_567892422940728, campagne 2026: SYBB (ID 120239435987290239).
**Datum:** 17 april 2026 (gisteren).
**PostHog:** niet beschikbaar.
