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
| Ad (utm_content) | Spend | Clicks | CTR | CPC | LP Views | Leads | LP Bounce | LP Scroll 50%+ | Flag |
|-------------------|-------|--------|-----|-----|----------|-------|-----------|----------------|------|
[per ad variant, zowel Meta als PostHog data gecombineerd]

**Beste variant:** [welke en waarom]
**Slechtste variant:** [welke en waarom]
**Delivery check:** [welke ads krijgen delivery en welke niet]

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

**Session recordings:** X nieuwe opnames

### 🎯 Top 3 Acties
1. [Actie — wat, waarom, hoe, verwachte impact]
2. [Actie]
3. [Actie]
```

## Regels
- Schrijf in het Nederlands
- Wees bondig — geen fluff, geen disclaimers
- Toon ALLE actieve ads, ook als ze geen delivery krijgen
- Vergelijk altijd met 7-daags gemiddelde
- Rode vlaggen triggers: CPC >€0.50, CTR <1%, bounce >70%, scroll <50% bij >60% bezoekers, frequency >3, 0 delivery op actieve ads, click→LP view drop >20%
- Sla het rapport op in output/reports/daily/
- Als PostHog geen data heeft (bv. net geïnstalleerd), vermeld dit en toon alleen Meta Ads data
