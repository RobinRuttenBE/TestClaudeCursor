# Daily SYBB Report Skill

## Purpose
Generate a comprehensive daily performance report for the SYBB (Start Your Balloon Business) workshop funnel by combining Meta Ads performance data with PostHog landing page analytics. The report identifies what's working, what's not, and provides prioritized actions.

## When to Use
- Every morning when the laptop wakes from sleep (automated trigger)
- When Robin asks for a SYBB performance update
- When Robin asks "hoe doet SYBB het?" or "SYBB rapport" or "landing page performance"

## Data Sources

### 1. Meta Ads (via Pipeboard Meta Ads MCP)
**Campaign name:** `2026: SYBB`

Fetch the following for yesterday (or specified date range):
- Campaign level: total spend, impressions, clicks, CTR, CPC, conversions
- Ad set level: spend, CPC, CTR per ad set
- Ad level: performance per individual ad (identify by utm_content: h11_b3_cta5, h12_b3_cta5, etc.)
- Frequency: average frequency per ad set (ad fatigue indicator)

### 2. PostHog (via PostHog MCP)
**Project:** Default project (SYBB Landing Page)
**Site:** startyourballoonbusiness.com

Fetch the following for yesterday (or specified date range):

**Traffic & Engagement:**
- Total pageviews and unique visitors on startyourballoonbusiness.com
- Bounce rate (single page sessions / total sessions)
- Average session duration
- Scroll depth distribution (% users reaching 25%, 50%, 75%, 100%)

**UTM Segmentation:**
- Break down all metrics by utm_content to see which ad variant drives the best on-page behavior
- Compare bounce rate per utm_content variant
- Compare scroll depth per utm_content variant

**Funnel Analysis (if sufficient data):**
- Step 1: Pageview on startyourballoonbusiness.com
- Step 2: Scroll past 50%
- Step 3: Click on "Book Now" CTA (or any CTA click)
- Step 4: Pageview on /booking
- Calculate drop-off % between each step

**Session Recordings:**
- Count of new session recordings available
- Flag any sessions with rage clicks or dead clicks

## Report Structure

Generate the report in markdown with the following sections:

```
# SYBB Daily Report — [DATUM]

## 1. Samenvatting
[2-3 zinnen: gaat het goed of slecht? belangrijkste trend?]

## 2. Meta Ads Performance
| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €X | €X | ↑/↓/→ |
| Impressions | X | X | ↑/↓/→ |
| Clicks | X | X | ↑/↓/→ |
| CTR | X% | X% | ↑/↓/→ |
| CPC | €X | €X | ↑/↓/→ |
| Frequency | X | X | ↑/↓/→ |

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | X | X% | €X | X% | X% |
| h12_b3_cta5 | X | X% | €X | X% | X% |
| h13_b3_cta5 | X | X% | €X | X% | X% |
| h14_b3_cta5 | X | X% | €X | X% | X% |
| h15_b3_cta5 | X | X% | €X | X% | X% |

**Beste variant:** [welke en waarom]
**Slechtste variant:** [welke en waarom]

## 3. Landing Page Health
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | X% | X% | <55% | 🟢/🟡/🔴 |
| Avg Session Duration | Xs | Xs | >90s | 🟢/🟡/🔴 |
| Scroll 25% | X% | X% | >80% | 🟢/🟡/🔴 |
| Scroll 50% | X% | X% | >60% | 🟢/🟡/🔴 |
| Scroll 75% | X% | X% | >40% | 🟢/🟡/🔴 |
| Scroll 100% | X% | X% | >20% | 🟢/🟡/🔴 |
| CTA Click Rate | X% | X% | >4% | 🟢/🟡/🔴 |

## 4. Funnel Drop-off
[Visuele funnel met drop-off percentages per stap]
Pageview (100%) → Scroll 50% (X%) → CTA Click (X%) → /booking (X%)

**Grootste lek:** [waar verlies je de meeste mensen?]

## 5. Rode Vlaggen 🚩
[Alleen tonen als er anomalieën zijn]
- CPC stijging >20% vs 7d gemiddelde
- Bounce rate >70% op een specifiek UTM segment
- Scroll depth <50% bij >60% van bezoekers
- Frequency >3 (ad fatigue)
- Nul CTA clicks op een dag met >50 bezoekers

## 6. Top 3 Acties voor Vandaag
1. [Meest urgente actie — concreet en specifiek]
2. [Tweede actie]
3. [Derde actie]

Prioriteit gebaseerd op: impact × snelheid van implementatie
```

## Analysis Logic

### Trend Indicators
- ↑ = >10% stijging vs 7d gemiddelde
- ↓ = >10% daling vs 7d gemiddelde
- → = stabiel (binnen 10%)

### Status Indicators
- 🟢 = op of boven target
- 🟡 = binnen 20% van target
- 🔴 = meer dan 20% onder target

### Red Flag Triggers
Automatisch rapporteren als:
1. **CPC > €0.50** — boven target, ad optimalisatie nodig
2. **Bounce rate > 70%** per UTM segment — ad-pagina mismatch
3. **Scroll depth < 50%** bij >60% bezoekers — hero/eerste sectie faalt
4. **CTA click rate < 2%** — CTA copy/positie/kleur probleem
5. **Frequency > 3.0** — ad fatigue, nieuwe creatives nodig
6. **Sectie skip rate > 80%** — sectie verwijderen of verplaatsen
7. **CPC stijging > 20%** vs 7-daags gemiddelde — alert

### Actionable Recommendations Framework
Elke aanbeveling moet bevatten:
- **Wat:** concrete beschrijving van de actie
- **Waarom:** welke data punt triggert dit
- **Hoe:** implementatie instructie (Wix MCP, handmatig, Meta Ads Manager)
- **Verwachte impact:** wat verwacht je dat er verbetert
- **Escalatie level:** Groen (auto), Geel (Robin goedkeuring), Oranje (Wix Editor), Rood (strategie)

## Historical Data

### Report Storage
Save each report to the project folder:
```
testclaudecursor/
  output/
    reports/
      daily/
        YYYY-MM-DD_sybb_report.md
      weekly/
        YYYY-WXX_sybb_summary.md
```

### Weekly Summary
Every Monday, generate a weekly summary that:
- Compares this week vs last week on all KPIs
- Identifies the best and worst performing day
- Identifies the best and worst performing ad variant
- Shows trend direction for each KPI
- Provides 3 strategic recommendations for the coming week

## Cross-Referencing Logic

The power of this report is combining BOTH data sources. Key cross-references:

1. **Ad CTR vs LP Bounce:** High CTR + High Bounce = misleading ad or ad-page mismatch
2. **Ad CTR vs LP Scroll Depth:** High CTR + Low Scroll = people click but page doesn't engage
3. **Ad CPC vs LP Conversion:** Low CPC + Low Conversion = cheap traffic but wrong audience
4. **Ad Variant vs LP Behavior:** Which utm_content drives the deepest engagement, not just clicks?
5. **Frequency vs Bounce:** Rising frequency + rising bounce = audience is saturated

Always highlight these cross-references when patterns emerge.

## Language
- Report in Dutch (Robin's primary language)
- Technical terms (CPC, CTR, bounce rate) in English (industry standard)
- Recommendations in Dutch with concrete next steps

## Example Prompt to Generate Report
```
Genereer het dagelijkse SYBB rapport voor gisteren.
Haal Meta Ads data op voor campagne "2026: SYBB" via de Meta Ads MCP.
Haal PostHog data op voor startyourballoonbusiness.com via de PostHog MCP.
Combineer beide databronnen en volg de rapportstructuur uit de daily-sybb-report skill.
Sla het rapport op in output/reports/daily/[datum]_sybb_report.md.
```
