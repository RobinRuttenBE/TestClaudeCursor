# SYBB Daily Report — 10 juli 2026

> Gegenereerd op 11 juli 2026. Databronnen: Meta Ads MCP (Pipeboard). PostHog MCP was tijdens deze run niet beschikbaar.

## 1. Samenvatting

Er is **niets te rapporteren over 10 juli** omdat de campagne stilstond. De Meta-campagne **`2026: SYBB` staat op PAUSED** en leverde gisteren nul impressies, nul clicks en nul spend. Ook op accountniveau was er de afgelopen 14 dagen geen delivery, dus er liep geen verkeer naar de landing page. Daarnaast was de **PostHog MCP niet beschikbaar** tijdens deze run (de connector verbond niet en leverde geen tools), waardoor landing page health, bounce rate en scroll depth niet konden worden opgehaald. Dit is de tweede dag op rij met dezelfde situatie (zie 9 juli). Actie #1 blijft een keuze: campagne heractiveren of bewust gepauzeerd laten.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID `120239435987290239`) — **status: PAUSED**
**Ad-account:** Sempertex Ad Account (`act_567892422940728`)

| Metric | Gisteren (10 jul) | 7d Gemiddelde (3–9 jul) | Trend |
|--------|-------------------|--------------------------|-------|
| Spend | €0 | €0 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De campagne heeft in de hele periode 3–10 juli geen delivery gehad. Er valt geen dag-op-dag of variant-analyse te maken.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | geen data | — | — | — | — |

Geen actieve ads, dus geen variant-performance. UTM-cross-referencing met PostHog niet mogelijk (zie sectie 3 + Rode Vlaggen).

### Context: lifetime performance (13 jan → 11 jul 2026)
Ter referentie, de historische cijfers van deze campagne over de volledige looptijd (**niet** gisteren):

| Metric | Lifetime |
|--------|----------|
| Spend | €2.485,04 |
| Impressions | 297.174 |
| Clicks | 12.067 |
| CTR | 4,06% |
| CPC | €0,21 |
| Frequency | 2,24 |
| Landing page views | 6.992 |
| Leads | 15 (CPL €165,67) |
| Add to cart | 53 |
| Initiate checkout | 36 |
| Purchases | 6 (waarde €44.247) |

De historische CTR (4,06%) en CPC (€0,21) zijn sterk t.o.v. de targets (CPC <€0,50). Het probleem zit niet in de ad-performance maar in het feit dat de campagne nu uit staat. De cijfers zijn ongewijzigd t.o.v. gisteren, wat bevestigt dat er sinds de pauze geen nieuwe delivery is geweest.

## 3. Landing Page Health

**Niet beschikbaar.** De PostHog MCP-connector was tijdens deze run niet verbonden en leverde geen tools op. Traffic, bounce rate, session duration en scroll depth voor `startyourballoonbusiness.com` konden niet worden opgehaald.

| Metric | Gisteren | 7d Gem. | Target | Status |
|--------|----------|---------|--------|--------|
| Bounce Rate | geen data | — | <55% | ⚪ n.v.t. |
| Avg Session Duration | geen data | — | >90s | ⚪ n.v.t. |
| Scroll 25% | geen data | — | >80% | ⚪ n.v.t. |
| Scroll 50% | geen data | — | >60% | ⚪ n.v.t. |
| Scroll 75% | geen data | — | >40% | ⚪ n.v.t. |
| Scroll 100% | geen data | — | >20% | ⚪ n.v.t. |
| CTA Click Rate | geen data | — | >4% | ⚪ n.v.t. |

> Opmerking: zelfs met een werkende PostHog-connector zou de landing page gisteren nagenoeg geen ad-verkeer hebben ontvangen, omdat de campagne gepauzeerd is.

## 4. Funnel Drop-off

Niet te berekenen. Zonder Meta-delivery (stap 1: ad-click) én zonder PostHog-data (stappen 2–4: scroll, CTA-click, /booking) is er geen funnel om drop-off op te meten.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — er is geen verkeer.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat op PAUSED** — `2026: SYBB` heeft 0 spend/impressies gehad op 10 juli (en de hele week 3–9 juli). Er loopt geen SYBB-acquisitie. Dit is de belangrijkste bevinding, en de tweede dag op rij.
- 🚩 **PostHog MCP niet beschikbaar** — de connector verbond niet tijdens deze run, dus landing page health kon niet worden gemeten. Structureel risico voor het dagelijkse rapport zolang dit niet is opgelost.
- ℹ️ Er bestaat ook een gepauzeerde kopie `2026: SYBB - Kopie` (ID `120243293329420239`) in het account. Check of dit een bewuste test/duplicaat is of opgeruimd kan worden.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: campagne aan of bewust uit?**
   - **Wat:** Kies of `2026: SYBB` weer op ACTIVE gaat (daily budget staat ingesteld op €100) of bewust gepauzeerd blijft.
   - **Waarom:** 0 spend op 10 juli betekent 0 nieuwe SYBB-leads, nu twee dagen op rij. Als acquisitie de bedoeling is, verlies je elke dag omzetpotentieel; de lifetime-cijfers (CTR 4,06%, CPC €0,21) tonen dat de creatives presteren.
   - **Hoe:** Via Meta Ads Manager de campagne (her)activeren, of hier bevestigen dat pauze gewenst is.
   - **Escalatie:** 🟡 Geel — vereist Robin's goedkeuring (budgetbeslissing).

2. **PostHog-connector herstellen.**
   - **Wat:** Zorg dat de PostHog MCP verbonden en geautoriseerd is, zodat landing page metrics weer opgehaald kunnen worden.
   - **Waarom:** Zonder PostHog mist het rapport de helft van zijn waarde (bounce, scroll, CTA, funnel) en de cross-referentie met Meta-data. Dit is nu twee dagen op rij misgegaan.
   - **Hoe:** In een interactieve sessie via `/mcp` of `claude mcp` de PostHog-connector (opnieuw) autoriseren.
   - **Escalatie:** 🟡 Geel — vereist actie van Robin buiten dit rapport.

3. **Opruimen: dubbele campagne verifiëren.**
   - **Wat:** Controleer of `2026: SYBB - Kopie` nog nodig is.
   - **Waarom:** Dubbele gepauzeerde campagnes maken rapportage en beheer onoverzichtelijk.
   - **Hoe:** In Meta Ads Manager de kopie beoordelen; verwijderen of archiveren indien overbodig.
   - **Escalatie:** 🟢 Groen — laag risico.

---

*Databronnen: Meta Ads MCP (Pipeboard), account `act_567892422940728`, campagne `120239435987290239`. PostHog MCP was niet beschikbaar tijdens deze run. Geen andere bronnen geraadpleegd.*
