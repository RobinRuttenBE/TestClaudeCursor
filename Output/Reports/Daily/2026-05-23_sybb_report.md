# SYBB Daily Report — 23 May 2026

## 1. Samenvatting
Stille dag. De Meta Ads campagne "2026: SYBB" stond gisteren op PAUSED, dus geen spend, impressies of clicks. De landing page startyourballoonbusiness.com kreeg gisteren 0 pageviews. De funnel ligt momenteel volledig stil; de enige reguliere verkeersbronnen in de afgelopen week waren Instagram en Facebook bio-links plus directe traffic, geen betaalde acquisitie.

## 2. Meta Ads Performance

Campagne **`2026: SYBB`** (ID `120239435987290239`) — status: **PAUSED** sinds 19 April 2026.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n/a | n/a | → |
| CPC | n/a | n/a | → |
| Frequency | n/a | n/a | → |

> Geen insights data beschikbaar via Pipeboard. De campagne draait al >5 weken niet. Er is ook een duplicaat `2026: SYBB - Kopie` (ID `120243293329420239`) aangemaakt op 19 April, eveneens PAUSED.

### Ad Variant Performance
Niet van toepassing. Geen actieve ads, dus geen utm_content varianten (h11..h15) hebben gisteren verkeer gegenereerd.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

### Verkeer per dag (afgelopen 14 dagen)
| Dag | Pageviews | Sessions | Visitors |
|-----|-----------|----------|----------|
| 10 mei | 3 | 3 | 3 |
| 11 mei | 4 | 4 | 4 |
| 12 mei | 14 | 10 | 8 |
| 13 mei | 1 | 1 | 1 |
| 14 mei | 1 | 1 | 1 |
| 15 mei | 4 | 3 | 3 |
| 16 mei | 7 | 6 | 4 |
| 17 mei | 7 | 6 | 6 |
| 18 mei | 4 | 3 | 3 |
| 19 mei | 6 | 6 | 6 |
| 20 mei | 3 | 3 | 3 |
| 21 mei | 1 | 1 | 1 |
| 22 mei | 2 | 2 | 2 |
| **23 mei** | **0** | **0** | **0** |

### KPI overzicht
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 3,3 | meten | 🔴 |
| Sessions | 0 | 3,0 | meten | 🔴 |
| Bounce Rate | n/a | ~90% (19 van 21 sessies één pv) | <55% | 🔴 |
| Avg Session Duration | n/a | $session_duration niet ingevuld | >90s | ⚠️ niet gemeten |
| Scroll 25/50/75/100% | n/a | geen scroll event in PostHog | meten | ⚠️ niet gemeten |
| CTA Click Rate | n/a | geen click/CTA event in PostHog | >4% | ⚠️ niet gemeten |

> **Meetgap:** Scroll depth, CTA clicks en sessieduur worden niet getrackt. Er zijn alleen `$pageview` events; geen autocapture clicks en geen scroll milestone events op www.startyourballoonbusiness.com.

## 4. Funnel Drop-off (laatste 7 dagen, 17–23 mei)

| Stap | Sessions | % van top |
|------|----------|-----------|
| Homepage `/` pageview | 20 | 100% |
| `/product-page/start-your-balloon-business-professional` | 1 | 5% |
| `/booking` pageview | 1 | 5% |
| `/checkout` pageview | 1 | 5% |

```
/ (20) ──► /product-page (1)  ──► /booking (1) ──► /checkout (1)
            -95%                    flat            flat
```

**Grootste lek:** 95% van de homepage bezoekers gaat nooit verder dan `/`. Op één sessie na verlaten alle bezoekers de site zonder een productpagina, booking of checkout te zien.

## 5. Cross-reference Meta Ads × Landing Page
- **Ad CTR vs LP Bounce:** niet te berekenen — geen ad activiteit.
- **Verkeersbron 7d (PostHog UTM):**
  - `instagram` / `sybb` / `bio_link`: 9 pageviews
  - `(direct)`: 9 pageviews
  - `facebook` / `sybb` / `bio_link`: 5 pageviews
- 100% van het traceerbare verkeer komt uit social bio-links en directe traffic. Geen Meta Ads attributie de afgelopen week.

## 6. Rode Vlaggen
- 🚩 **Campagne PAUSED** — `2026: SYBB` (en de kopie) staan al sinds 19 April uit. Geen acquisitie pipeline actief.
- 🚩 **Nul pageviews gisteren** — eerste dag in de afgelopen 14 dagen met 0 traffic.
- 🚩 **Bounce ~90% over 7d** — 19 van 21 sessies bekijken één pagina en vertrekken.
- 🚩 **Funnel drop-off 95% op homepage** — slechts 1 sessie in 7 dagen bereikt een productpagina, booking of checkout.
- 🚩 **Geen scroll/CTA/sessieduur tracking** — kan ad-pagina mismatches niet diagnosticeren, key SYBB skill KPIs ontbreken.

## 7. Top 3 Acties voor Vandaag

### 1. Beslissen: campagne hervatten of herzien
- **Wat:** maak een go/no-go knoop over `2026: SYBB`. Of unpause met huidige creatives, of bevries definitief en start nieuwe campagne met verse hooks.
- **Waarom:** vijf weken pauze + 0 traffic gisteren betekent dat het hele SYBB funnel-mechaniek stilstaat. Zonder verkeer geen leerdata, geen leads, geen workshop sales.
- **Hoe:** Meta Ads Manager → campagne `120239435987290239`. Vóór unpause: check budget (huidig daily budget €100), check ad set status, en check of er nog actieve ads in zitten. Overweeg klein dagbudget (€20–30) om eerst de pipeline te testen.
- **Verwachte impact:** terug naar baseline 50–200 pv/dag zodra de campagne weer loopt.
- **Escalatie:** 🟡 Geel — Robin goedkeuring vereist (budgetbeslissing).

### 2. Implementeer scroll depth en CTA click tracking
- **Wat:** Voeg `$autocapture` toe (of expliciete `posthog.capture('cta_click')` events) en scroll milestone events (25/50/75/100%) in de Wix theme van startyourballoonbusiness.com.
- **Waarom:** de SKILL specificeert scroll 25/50/75/100 en CTA click rate als kern KPIs, maar geen van beide is gemeten. Daardoor zijn 4 van de 7 KPI rijen in deze rapportage leeg. Zonder dit signaal kun je geen ad-pagina mismatch diagnosticeren.
- **Hoe:** in PostHog Web SDK config `autocapture: true` zetten en in de Wix custom code een scroll listener toevoegen die `posthog.capture('scroll_depth', { milestone: 25/50/75/100 })` vuurt. Voor CTA: voeg een `data-cta` attribute toe op de "Book Now" knoppen en capture clicks expliciet.
- **Verwachte impact:** funnel rapportage gaat van 2 KPIs naar 7 KPIs gevuld; binnen 7 dagen real bounce/scroll signal beschikbaar.
- **Escalatie:** 🟠 Oranje — Wix Editor + PostHog config nodig.

### 3. Onderzoek de 95% homepage-only drop-off
- **Wat:** kijk de 2 multi-pageview sessies in PostHog session recordings terug en vergelijk met de 19 single-page bounces. Zoek wat de wel-doorklikkers anders deden.
- **Waarom:** zelfs zonder ads is 5% homepage→product CR extreem laag voor warme social/direct traffic. De homepage levert het verhaal duidelijk niet af.
- **Hoe:** PostHog → Session replays → filter `$host = www.startyourballoonbusiness.com`, periode 17–23 mei. Markeer of bezoekers (a) niet ver scrollen, (b) wel scrollen maar geen CTA klikken, of (c) wegklikken bij specifieke sectie. Hypothese: hero CTA is niet sterk genoeg of de "Book Now" zit te ver onder de fold.
- **Verwachte impact:** kwalitatieve input voor een homepage hero/CTA herziening voor de relaunch.
- **Escalatie:** 🟢 Groen — kan Robin direct in PostHog UI doen.

---
**Bron:** Meta Ads via Pipeboard MCP (account `act_567892422940728`, Sempertex Ad Account) + PostHog MCP (project 149694, Sempertex Europe). Geen Google Sheet update uitgevoerd conform run-instructies.
