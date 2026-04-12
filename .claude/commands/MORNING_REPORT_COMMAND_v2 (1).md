# Morning Report — SYBB Performance Briefing

Genereer een dagelijks SYBB performance rapport. Alleen Meta Ads data en PostHog landing page data. Geen agenda, emails, of Drive activiteit.

## Stappen

### 1. Meta Ads Performance
Haal via de Meta Ads MCP (Pipeboard) de performance op voor campagne "2026: SYBB".

**Data ophalen:**
- Campaign level: spend, impressions, clicks, CTR, CPC, CPM, reach, frequency
- Ad level: performance per individuele ad (alle actieve ads, niet alleen ads met delivery)
- Actie-metrics: link clicks, landing page views, video views, post engagement, post reactions, saves, comments
- Pixel events: ViewContent, AddToCart, InitiateCheckout, Purchase (met aantallen en cost per actie)
- Vergelijk met 7-daags gemiddelde waar mogelijk

**Periode:** Gisteren (24u) + lifetime vergelijking

### 2. PostHog Landing Page Analytics
Haal via de PostHog MCP data op voor startyourballoonbusiness.com over de afgelopen 24 uur:
- Totaal pageviews en unieke bezoekers
- Bounce rate
- Gemiddelde sessie duur
- Scroll depth distributie (25%, 50%, 75%, 100%)
- CTA click events
- Aantal nieuwe session recordings
- UTM segmentatie: welke ad variant (utm_content) levert welk gedrag op de LP

**Dag + 7d context (verplicht):** toon voor `bounce rate` en `sessie duur` altijd TWEE waarden: de dagwaarde (gisteren) EN het 7-daags gemiddelde. Format: `Dag: X% · 7d gem: Y%`. Haal beide op via PostHog MCP, de dagwaarde gefilterd op gisteren en het 7d gemiddelde over de afgelopen 7 dagen. Dit geldt ook in de Landing Page Health tabel in de output.

Als er geen traffic was, toon de meest recente data die beschikbaar is.

### 3. Cross-Reference Analyse
Combineer Meta Ads + PostHog data:
- Per ad variant: CTR (Meta) vs Bounce Rate (PostHog) vs Scroll Depth (PostHog)
- Detecteer mismatches: hoge CTR + hoge bounce = ad-pagina mismatch
- Detecteer winnaars: lage CPC + lage bounce + diepe scroll = beste ad-LP combinatie
- Click → LP View drop-off percentage

### 4. Rapport Opslaan
Sla het rapport op in output/reports/daily/YYYY-MM-DD_sybb_report.md

## Output format

```
## 📊 SYBB Rapport — [datum]

### ⚡ Samenvatting
[2-3 zinnen: kernbevinding van de dag]

### 🚩 Rode Vlaggen
[Alleen tonen als er anomalieën zijn]
- [vlag + data + aanbeveling]

### 📈 Meta Ads Performance
| Metric | Gisteren | 7d Gem. | Trend | Target | Status |
|--------|----------|---------|-------|--------|--------|
| Spend | €X | €X | ↑/↓/→ | — | — |
| Impressions | X | X | ↑/↓/→ | — | — |
| Link Clicks | X | X | ↑/↓/→ | — | — |
| CTR | X% | X% | ↑/↓/→ | >1% | 🟢/🔴 |
| CPC | €X | €X | ↑/↓/→ | <€0.50 | 🟢/🔴 |
| Frequency | X | X | ↑/↓/→ | <3.5 | 🟢/🔴 |
| LP Views | X | X | ↑/↓/→ | — | — |

### 🎬 Ad Variant Performance
| Ad (utm_content) | Spend | Clicks | CTR | CPC | LP Views | IC (InitCheckout) | ATC (AddToCart) | Purchases | LP Bounce | LP Scroll 50%+ | Flag |
|-------------------|-------|--------|-----|-----|----------|-------|-----------|---------|-----------|----------------|------|
[per ad variant, zowel Meta als PostHog data gecombineerd]

**Beste variant:** [welke en waarom]
**Slechtste variant:** [welke en waarom]
**Delivery check:** [welke ads krijgen delivery en welke niet]

#### Gepauzeerde ads (restspend)
Check de status van elke ad via de Meta Ads MCP. Als een ad op `PAUSED` staat maar nog spend toont in de rapportageperiode, label deze als `GEPAUZEERD, restspend €X` in de Flag kolom. Toon gepauzeerde ads apart onder de actieve ads tabel, niet ertussen. Gebruik dezelfde kolomstructuur als de actieve ads tabel. Als er geen gepauzeerde ads met restspend zijn: "Geen gepauzeerde ads met restspend in deze periode."

### 📡 Pixel Events
| Event | Aantal | Cost per Event | Trend |
|-------|--------|----------------|-------|
| ViewContent | X | €X | ↑/↓/→ |
| AddToCart | X | €X | ↑/↓/→ |
| InitiateCheckout | X | €X | ↑/↓/→ |
| Purchase | X | €X | ↑/↓/→ |

### 🌐 Landing Page Health (PostHog)
| Metric | Gisteren | Target | Status |
|--------|----------|--------|--------|
| Bezoekers | X | — | — |
| Bounce Rate | X% | <55% | 🟢/🟡/🔴 |
| Avg Session Duration | Xs | >90s | 🟢/🟡/🔴 |
| Scroll 25% | X% | >80% | 🟢/🟡/🔴 |
| Scroll 50% | X% | >60% | 🟢/🟡/🔴 |
| Scroll 75% | X% | >40% | 🟢/🟡/🔴 |
| Scroll 100% | X% | >20% | 🟢/🟡/🔴 |
| CTA Click Rate | X% | >4% | 🟢/🟡/🔴 |
(alleen tonen als PostHog custom events geconfigureerd zijn, anders: "Niet geconfigureerd")

**Session recordings:** X nieuwe opnames

### 🎯 Top 3 Acties
1. [Actie — wat, waarom, hoe, verwachte impact]
2. [Actie]
3. [Actie]
```

## Data Integriteit Regels (KRITIEK)

### SANITY CHECKS (verplicht voor elk rapport)
1. **Purchase waarde check (multi-ticket aware):** SYBB ticket prijs is €350 ex BTW tot €423,50 incl BTW. Een purchase kan 1 of meerdere tickets bevatten, dus de gemiddelde waarde per purchase moet een veelvoud van de ticket prijs zijn. Bereken `purchase_value / aantal_purchases` en check of het roughly past in de reeks `~€350, ~€423, ~€700, ~€847, ~€1050, ~€1270, ~€1400, ~€1694, ~€1750, ~€2117, ...` (veelvouden van €350 ex of €423,50 incl) met 15% marge. Als het NIET past: meld "PIXEL DATAFOUT, purchase waarde onrealistisch, verifieer met Wix orders" en toon het purchase aantal als `? (verifieer Wix)` in ALLE tabellen waar het voorkomt (Pixel Events, Ad Variant Performance, Samenvatting). Gebruik GEEN geschatte waarde, laat het veld leeg of markeer als onbekend tot Wix bevestigt.
2. **Purchase aantal check:** vermeld NOOIT een purchase aantal zonder de sanity check. Vraag altijd expliciet: "Verifieer het aantal purchases met Wix orders."
3. **Gemiddelde spend:** bereken ALLEEN over dagen met spend >€0. Tel gepauzeerde dagen NIET mee. Vermeld altijd het aantal actieve dagen.
4. **PostHog data is VERPLICHT.** Haal ALTIJD PostHog data op via de PostHog MCP als onderdeel van elk rapport. Als de PostHog MCP niet bereikbaar is, meld dit als EERSTE rode vlag met de tekst: "🚩 MCP ERROR, geen LP data beschikbaar". Verplichte PostHog metrics: visitors, pageviews, sessions, bounce rate, avg sessie duur, device breakdown.
5. **Cross-reference Meta LP views ↔ PostHog sessions:** vergelijk Meta landing_page_view met PostHog sessions gefilterd op `utm_source=meta` (case-insensitive) voor dezelfde periode. Als het verschil >30% is, meld: "DATA MISMATCH, Meta LP views vs PostHog sessions wijken X% af" en benoem mogelijke oorzaken (pixel blocking, session cutoff, UTM case inconsistency).
6. **Onlogische metrics:** elke metric die onlogisch lijkt (ROAS >100x, CPC <€0.01, bounce >99%) moet geflagged worden als "MOGELIJKE DATAFOUT, verifieer handmatig".

### Link clicks, niet all clicks (KRITIEK voor Meta Ads data)
Meta's standaard `clicks` veld is ALL clicks (inclusief likes, comments, profile clicks). Dit is GEEN doorklikratio en mag NOOIT als zodanig gerapporteerd worden.

Bij het ophalen van Meta Ads data via de MCP, gebruik ALTIJD deze metrics:
- **Clicks:** gebruik `actions.link_click`, NIET het veld `clicks`.
- **Link CTR (doorklikratio):** bereken als `link_clicks / impressions × 100`. NIET de standaard `ctr` die Meta teruggeeft, want dat is all clicks CTR.
- **CPC (link):** bereken als `spend / link_clicks`. NIET `spend / all_clicks` en NIET Meta's standaard `cpc` veld.

**Labels (verplicht):**
- Schrijf altijd `Link CTR` of `All Clicks CTR`, nooit kaal `CTR`.
- Schrijf altijd `CPC (link)` of `CPC (all)`, nooit kaal `CPC`.
- Als je beide wilt tonen voor context, label ze expliciet als twee aparte rijen.
- Rode vlag triggers gebruiken ALTIJD de link-variant: Link CTR <1%, CPC (link) >€0.50.

### Correcte labels en event namen (verplicht)
- Gebruik NOOIT het woord "leads". Gebruik de exacte Meta event namen: `InitiateCheckout`, `AddToCart`, `Purchase`.
- Meta's "Gestart betaalproces" = `InitiateCheckout`, NIET een lead.
- "Results" in Meta Ads Manager = het conversie-event van de campagne (momenteel: `InitiateCheckout`). Benoem dit expliciet.
- Lifetime "leads" bestaan niet, het waren `InitiateCheckout` events.
- Gebruik NOOIT kaal "CTR": schrijf `Link CTR` of `All Clicks CTR`.
- Gebruik NOOIT kaal "CPC": schrijf `CPC (link)` of `CPC (all)`.
- Gebruik NOOIT "purchases" zonder de purchase sanity check (zie boven).

### Databron verplicht bij elk datapunt
- Elk datapunt moet een bron vermelden: (Meta Ads MCP) of (PostHog MCP)
- Als een getal berekend/afgeleid is, vermeld de berekening
- Meng NOOIT Meta ad metrics met LP metrics zonder expliciete markering

### Gemiddelde spend berekening
- Bereken gemiddelde spend ALLEEN over ACTIEVE dagen (dagen met spend > €0)
- Tel gepauzeerde dagen (spend = €0) NIET mee in het gemiddelde
- Vermeld altijd expliciet: "Gemiddelde spend: €X/dag over Y actieve dagen" — niet over de volledige 30d window
- Dit geldt voor alle spend-gemiddelden: campagne, adset, en ad niveau

### Minimum data drempels
- PostHog LP metrics (bounce, scroll, sessie duur): toon ALLEEN als er minimaal 50 sessies zijn. Anders: "Onvoldoende data (X sessies)"
- CTA click rate op LP: toon ALLEEN als PostHog custom events geconfigureerd zijn. Anders: "Niet geconfigureerd"
- Meld altijd het aantal sessies/datapunten waarop een metric gebaseerd is

### Geen verzonnen metrics
- Rapporteer NOOIT een metric die niet direct uit een MCP tool komt
- Als je een metric niet kunt ophalen, zeg "Data niet beschikbaar" — verzin geen schattingen
- "CTA Click Rate" = PostHog click events op de LP, NIET Meta ad CTR

## Algemene Regels
- Schrijf in het Nederlands
- Wees bondig — geen fluff, geen disclaimers
- Toon ALLE actieve ads, ook als ze geen delivery krijgen
- Vergelijk altijd met 7-daags gemiddelde
- Rode vlaggen triggers: `CPC (link)` >€0.50, `Link CTR` <1%, bounce >70%, scroll <50% bij >60% bezoekers, frequency >3, 0 delivery op actieve ads, link click → LP view drop >20%
- Sla het rapport op in output/reports/daily/
- Als PostHog geen data heeft, vermeld dit en toon alleen Meta Ads data
