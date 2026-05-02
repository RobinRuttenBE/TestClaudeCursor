# SYBB Daily Report — 2026-05-01

## 0. Datakwaliteit & Beperkingen
- **Meta Ads (Pipeboard MCP):** OK. Campagne `2026: SYBB` (id 120239435987290239) is **PAUSED** sinds 2026-04-19. Geen spend, impressies of clicks op 2026-05-01.
- **PostHog MCP:** **Niet bereikbaar** ("Failed to connect" bij MCP health check). Landing-page metrics, scroll depth, bounce rate en funnel-data konden niet worden opgehaald.
- Er is dus geen ad-niveau performance om te koppelen aan LP-gedrag. Cross-references (CTR vs bounce, frequency vs scroll, etc.) zijn vandaag niet mogelijk.

## 1. Samenvatting
SYBB-funnel staat stil. Campagne "2026: SYBB" is gepauzeerd sinds 19 april, dus 2026-05-01 telt nul Meta Ads activiteit. PostHog MCP is offline, dus zelfs organisch LP-verkeer kan vandaag niet gerapporteerd worden. Belangrijkste signaal voor vandaag: het funnelinstrumentarium is operationeel niet "uit", maar de aanzet (paid traffic) ontbreekt al twee weken.

## 2. Meta Ads Performance — 2026-05-01

| Metric | Gisteren (2026-05-01) | 7d Gemiddelde (2026-04-25 → 05-01) | Trend |
|--------|----------------------|------------------------------------|-------|
| Spend | €0.00 | €0.00 | → (campagne paused) |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n/a | n/a | → |
| CPC | n/a | n/a | → |
| Frequency | n/a | n/a | → |

**Status campagne `2026: SYBB`:** PAUSED, laatste updated_time 2026-04-19. Daily budget config: €100/dag (10000 cents).
**Variant `2026: SYBB - Kopie` (id 120243293329420239):** ook PAUSED, aangemaakt 2026-04-19, geen spend.

### Ad Variant Performance — 2026-05-01
Niet van toepassing, geen impressies of clicks per ad. Onderstaande historische context dient ter referentie voor wanneer de campagne opnieuw live gaat.

### Historische context (laatste 30 dagen, 2026-04-02 → 2026-05-01)
Periode bevat alleen data van 2026-04-02 t/m 2026-04-19; daarna paused.

| Metric | Waarde |
|--------|--------|
| Spend | €1.059,47 |
| Impressions | 91.839 |
| Reach | 41.851 |
| Clicks | 1.935 |
| Unique clicks | 1.408 |
| CTR | 2,11% |
| CPC | €0,55 |
| CPM | €11,54 |
| Frequency | 2,19 |
| Landing page views | 818 |
| Add to cart | 44 |
| Initiate checkout | 33 |
| Purchases (pixel) | 6 |

CPC zit boven target (<€0,50). Frequency 2,19 nadert de fatigue-grens (3,0). Conversie van click → LP-view → ATC → IC → purchase laat een diepe drop-off zien (1.935 → 818 → 44 → 33 → 6), wat al voor de pauzering een duidelijk middle-of-funnel-lek aangaf.

## 3. Landing Page Health — 2026-05-01
**Niet beschikbaar.** PostHog MCP gaf "Failed to connect" bij health check. Geen pageviews, bounce rate, scroll depth, sessieduur of CTA click rate beschikbaar voor startyourballoonbusiness.com op 2026-05-01.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n/a | n/a | <55% | ⚪ data ontbreekt |
| Avg Session Duration | n/a | n/a | >90s | ⚪ data ontbreekt |
| Scroll 25% | n/a | n/a | >80% | ⚪ data ontbreekt |
| Scroll 50% | n/a | n/a | >60% | ⚪ data ontbreekt |
| Scroll 75% | n/a | n/a | >40% | ⚪ data ontbreekt |
| Scroll 100% | n/a | n/a | >20% | ⚪ data ontbreekt |
| CTA Click Rate | n/a | n/a | >4% | ⚪ data ontbreekt |

## 4. Funnel Drop-off
Niet te berekenen voor 2026-05-01 (geen Meta-traffic, geen PostHog-data). De 30d-snapshot hierboven (1.935 → 818 → 33 → 6) blijft het laatst bekende beeld; bij heractivatie eerst funnel-tracking valideren voor je budget verhoogt.

## 5. Rode Vlaggen
- 🚩 **Campagne `2026: SYBB` is 12+ dagen paused** (sinds 2026-04-19). SYBB-funnel ontvangt geen paid traffic. Als dit niet bewust strategisch is, gaat momentum en pixel learning verloren.
- 🚩 **PostHog MCP is offline.** Je kunt momenteel geen LP-data lezen via Claude. Dit blokkeert alle daily-report cross-references zolang de connectie down is.
- 🚩 **30d historische CPC €0,55** > target €0,50 (10% over). Bij heractivatie vrijwel zeker eerst iteratie nodig op hooks/audience.
- 🚩 **30d frequency 2,19** richting fatigue zone (>3,0). Bij re-launch nieuwe creatives klaarzetten.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: heractiveren of bewust on hold houden?**
   - **Wat:** vandaag een duidelijke beslissing nemen op de status van campagne `2026: SYBB`.
   - **Waarom:** de campagne is 12+ dagen paused; dat is geen rapporteerbare staat meer, dat is een strategiekeuze.
   - **Hoe:** (a) als heractiveren — open Meta Ads Manager, check eerst de variant `2026: SYBB - Kopie` configuratie, vervang/refresh creatives gegeven freq 2,19 en CPC €0,55, hervat met €100/dag testbudget op de 5 utm_content varianten (h11–h15). (b) als bewust pauze — leg vast in `Kennis/Voorgaande campagnes/campagne-historie.md` waarom en tot wanneer.
   - **Verwachte impact:** zonder paid input is er niets te optimaliseren in de daily report; deze beslissing deblokkeert het hele systeem.
   - **Escalatie level:** Rood (strategie — Robin).

2. **Fix PostHog MCP connectie.**
   - **Wat:** PostHog MCP server `https://mcp.posthog.com/mcp` reconnecten.
   - **Waarom:** zonder PostHog kan de daily-sybb-report skill geen LP-health, scroll, bounce of funnel rapporteren — kerncompetentie van het rapport valt weg.
   - **Hoe:** check `~/.claude/settings.json` of `.claude/settings.local.json` voor PostHog MCP config; valideer API key en project token; herstart Claude Code; verifieer met `claude mcp list`. Als het remote-token verlopen is, vernieuwen via PostHog dashboard → Settings → Personal API Keys.
   - **Verwachte impact:** vanaf morgen weer volledige cross-reference rapporten. Zonder dit blijft het rapport beperkt tot Meta-only.
   - **Escalatie level:** Geel (Robin goedkeuring nodig voor token-rotatie).

3. **Bereid re-launch creatives en utm-tagging voor.**
   - **Wat:** nieuwe creative-batch klaarzetten voor wanneer de campagne weer aan gaat, gebaseerd op de SYBB 8 pillars.
   - **Waarom:** vorige run liet CPC boven target (€0,55) en frequency 2,19 zien — gewoon dezelfde ads herstarten produceert dezelfde resultaten. 70-20-10: 70% bewezen hooks (h11–h15 die het best presteerden in maart-april), 20% varianten, 10% experiment.
   - **Hoe:** zie `Bronnen/Sempertex Europe/sybb-8-pillars.md` voor pillar-mapping; lever 5 nieuwe hook varianten (h16–h20) volgens utm-conventie `utm_content=hXX_bX_ctaX`; check `tracking-standards` skill voor exacte UTM-formattering; gebruik `/ad-combinator` voor angle-generatie.
   - **Verwachte impact:** lager CPC bij re-launch, lagere fatigue, betere LP cross-reference data.
   - **Escalatie level:** Geel (Robin valideert hooks voor productie).

---

**Bronnen:** Meta Ads MCP (Pipeboard, account `act_567892422940728`, campagne id `120239435987290239`).
**Niet beschikbaar vandaag:** PostHog MCP (connection failure).
