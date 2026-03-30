# Morning Report — Dagelijkse Briefing

Genereer een ochtendrapport voor Robin (Head of Marketing, Sempertex Europe). Haal de volgende informatie op en vat samen in een overzichtelijk Nederlands rapport:

## Stappen

### 1. Agenda vandaag
Gebruik `mcp__google__calendar_events_list` met calendar_id "primary", time_min = vandaag 00:00 (RFC3339), time_max = vandaag 23:59 (RFC3339). Haal max 20 events op.

### 2. Laatste emails
Gebruik `mcp__google__gmail_messages_list` met max_results 5. Lees vervolgens elk bericht met `mcp__google__gmail_message_get` om de inhoud te bekijken.

### 3. Recente Drive activiteit
Gebruik `mcp__google__drive_files_list` met page_size 10 om recent gewijzigde bestanden te zien.

### 4. Meta Ads Performance (SYBB)
Haal via de Meta Ads MCP (Pipeboard) de performance op voor campagne "2026: SYBB" over de afgelopen 24 uur. Als de campagne gepauzeerd is, haal lifetime/last 30 days data op en meld dat er geen actieve spend is.

### 5. PostHog Landing Page Analytics (SYBB)
Haal via de PostHog MCP de volgende data op voor startyourballoonbusiness.com over de afgelopen 24 uur:

- Totaal pageviews en unieke bezoekers
- Bounce rate
- Scroll depth distributie (25%, 50%, 75%, 100%)
- Sessie duur gemiddelde
- CTA click events (als geconfigureerd)
- Aantal nieuwe session recordings

Als er geen traffic was (campagne gepauzeerd), meld dit en toon de meest recente data die beschikbaar is.

### 6. SYBB Excel Tracker Updaten
Werk de Meta Ads Tracker Excel bij volgens de formatting regels in `skills/meta-ads-tracker-excel/SKILL.md`. Voeg nieuwe rijen toe aan het Weekly Report sheet met zowel Meta Ads als PostHog data per ad variant.

## Output format

Schrijf het rapport in dit format:

```
## Ochtendrapport — [datum]

### Agenda vandaag
- [tijd] — [event naam] (locatie/link indien beschikbaar)
- ...
(of: "Geen afspraken vandaag — focus dag!")

### Laatste 5 emails
- **[afzender]** — [onderwerp] → [1-zin samenvatting van de inhoud]
- ...

### Recente Drive activiteit
- [bestandsnaam] — laatst gewijzigd [datum/tijd]
- ...

### Meta Ads Performance — SYBB
| Metric | Gisteren | 7d Gem. | Trend |
|--------|----------|---------|-------|
| Spend | €X | €X | ↑/↓/→ |
| Clicks | X | X | ↑/↓/→ |
| CTR | X% | X% | ↑/↓/→ |
| CPC | €X | €X | ↑/↓/→ |

**Beste ad:** [variant] — [waarom]
**Slechtste ad:** [variant] — [waarom]
(of: "Campagne PAUSED sinds [datum] — geen actieve spend")

### Landing Page Health — PostHog
| Metric | Gisteren | Target | Status |
|--------|----------|--------|--------|
| Bezoekers | X | — | — |
| Bounce Rate | X% | <55% | groen/geel/rood |
| Scroll 50%+ | X% | >60% | groen/geel/rood |
| Scroll 100% | X% | >20% | groen/geel/rood |
| CTA Click Rate | X% | >4% | groen/geel/rood |
| Sessie duur | Xs | >90s | groen/geel/rood |

**Session recordings:** X nieuwe opnames beschikbaar
(of: "Geen traffic gisteren — laatste data van [datum]")

### Rode Vlaggen
[Alleen tonen als er anomalieën zijn — zie triggers in skills/daily-sybb-report/SKILL.md]
- [vlag 1]
- [vlag 2]
(of: "Geen rode vlaggen vandaag")

### Funnel Diagnose
[Als er een actieve Meta Ads campagne draait: draai automatisch /funnel-diagnose en toon hier de verkorte versie]
- Funnel tabel (6 stappen met status)
- #1 bottleneck
- Belangrijkste actiepunt
(of: "Geen actieve campagnes — geen funnel data")

### Top 3 Acties voor Vandaag
1. [Meest urgente actie — gebaseerd op ads + landing page data + agenda]
2. [Tweede actie]
3. [Derde actie]
Prioriteit gebaseerd op: impact x snelheid van implementatie
```

## Regels
- Schrijf in het Nederlands
- Wees bondig maar informatief
- Markeer urgente items (deadlines, belangrijke meetings) met !!
- Als er geen data beschikbaar is voor een sectie, geef dat netjes aan
- Sla het volledige rapport ook op in `output/reports/daily/YYYY-MM-DD_sybb_report.md`
- Update de Meta Ads Tracker Excel volgens `skills/meta-ads-tracker-excel/SKILL.md`
- Gebruik de cross-referencing logic uit `skills/daily-sybb-report/SKILL.md`: combineer Meta Ads data met PostHog data om ad-pagina mismatches te detecteren
