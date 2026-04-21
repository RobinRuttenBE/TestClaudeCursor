# SKILL: Content Memory — Sempertex Europe

## Doel
Bouw een data-gedreven kennisbank op van wat werkt en wat niet op social media, puur op basis van CIJFERS die Claude Code zelf kan lezen (engagement, formats, timing, captions). Niet op basis van video-inhoud — dat doet BLORT.

## Account IDs (hardcoded)

| Platform | ID |
|----------|----|
| **Instagram Business** | `17841403335662168` |
| **Facebook Page** | `215391235203393` |

**NOOIT andere accounts gebruiken.**

## Wanneer gebruiken
- **Na elke /social-report:** Update Content Learnings met nieuwe patronen
- **Voor /script-youtube:** Raadpleeg learnings over welke hooks/formats werken
- **Voor /blort-prompt:** Raadpleeg learnings voor context bij content briefings
- **Voor /social-content:** Raadpleeg timing en format patronen
- **Maandelijks:** Genereer Monthly Content Intelligence Report

## Data die Claude Code WEL kan analyseren
- Engagement cijfers (likes, comments, saves, shares, reach, impressions)
- Format performance (reel vs static vs carousel vs story)
- Timing patronen (dag van de week, tijd van de dag)
- Caption hooks (eerste zin van de caption — tekst, niet gesproken)
- Onderwerp tags (afgeleid uit caption tekst)
- Post frequentie en consistentie
- Follower groei trends
- Week-over-week vergelijkingen

## Data die Claude Code NIET kan analyseren
- Gesproken hooks (eerste 3 seconden audio)
- Visuele stijl (setting, beweging, kleurgebruik)
- Tekst overlays in video's
- Thumbnail effectiviteit (visueel)
- Productie kwaliteit
→ **Dit wordt geanalyseerd door BLORT via /blort-social-analyze. Robin voegt het BLORT rapport handmatig toe aan het Google Doc.**

---

## Google Doc: "Content Learnings"

### Structuur van het document

```
# Content Learnings — Sempertex Europe
Laatst bijgewerkt: [datum]

---

## 1. FORMAT PERFORMANCE (cumulatief)

### Engagement rate per format (rolling 4 weken)
| Format | Gem. engagement rate | Gem. reach | Gem. saves | Beste week | Trend |
|--------|---------------------|-----------|-----------|-----------|-------|
| Reel | [x%] | [x] | [x] | Week [x] | ↑/↓/→ |
| Carousel | [x%] | [x] | [x] | Week [x] | ↑/↓/→ |
| Static | [x%] | [x] | [x] | Week [x] | ↑/↓/→ |
| Story | [x%] | [x] | [x] | Week [x] | ↑/↓/→ |

### Conclusie
[Welk format presteert consistent het best? Update elke week.]

---

## 2. TIMING PATRONEN (cumulatief)

### Dag performance (rolling 4 weken)
| Dag | Gem. engagement | Gem. reach | Aantal posts |
|-----|----------------|-----------|-------------|
| Ma | [x] | [x] | [x] |
| Di | [x] | [x] | [x] |
| Wo | [x] | [x] | [x] |
| Do | [x] | [x] | [x] |
| Vr | [x] | [x] | [x] |
| Za | [x] | [x] | [x] |
| Zo | [x] | [x] | [x] |

### Beste posttijden
- Beste dag: [dag]
- Beste tijdslot: [tijd]
- Slechtste dag: [dag]

---

## 3. CAPTION HOOK DATABASE

### Top hooks (gesorteerd op engagement score)
| # | Hook (eerste zin) | Type (Hormozi) | Format | Engagement score | Datum |
|---|-------------------|---------------|--------|-----------------|-------|
| 1 | "[eerste zin]" | [type] | [format] | [score] | [datum] |
| 2 | ... | | | | |
| ... | | | | | |

### Slechtste hooks
| # | Hook (eerste zin) | Type (Hormozi) | Format | Engagement score | Datum |
|---|-------------------|---------------|--------|-----------------|-------|
| 1 | "[eerste zin]" | [type] | [format] | [score] | [datum] |

### Hook type performance
| Hook type | Gem. engagement | Aantal | Voorbeeld (beste) |
|-----------|----------------|--------|-------------------|
| Statement | [x] | [x] | "[voorbeeld]" |
| Command | [x] | [x] | "[voorbeeld]" |
| Question | [x] | [x] | "[voorbeeld]" |
| Exclamation | [x] | [x] | "[voorbeeld]" |
| List/Steps | [x] | [x] | "[voorbeeld]" |
| Story | [x] | [x] | "[voorbeeld]" |
| Conditional | [x] | [x] | "[voorbeeld]" |

---

## 4. ONDERWERP TAGS

### Performance per onderwerp
| Tag | Gem. engagement | Gem. reach | Aantal posts | Trend |
|-----|----------------|-----------|-------------|-------|
| product-demo | [x] | [x] | [x] | ↑/↓/→ |
| workshop-promo | [x] | [x] | [x] | ↑/↓/→ |
| behind-the-scenes | [x] | [x] | [x] | ↑/↓/→ |
| tutorial | [x] | [x] | [x] | ↑/↓/→ |
| event | [x] | [x] | [x] | ↑/↓/→ |
| community | [x] | [x] | [x] | ↑/↓/→ |
| announcement | [x] | [x] | [x] | ↑/↓/→ |

### Tagging regels
Wijs per post een of meer tags toe op basis van de caption:
- **product-demo**: product wordt getoond of getest
- **workshop-promo**: promotie van een workshop of event
- **behind-the-scenes**: intern, team, bedrijfscultuur
- **tutorial**: instructie, how-to, tips
- **event**: live event, beurs, expo
- **community**: user content, testimonials, reposts
- **announcement**: bedrijfsnieuws, launches

**Sub-tagging met Balloon Knowledge:** voor `tutorial`, `product-demo` en `community` posts — scan `Kennis/Balloon Knowledge/INDEX.md` en voeg een specifieke techniek/product sub-tag toe (bv. `tutorial:diamond-weave`, `tutorial:pinch-twist`, `product-demo:link-o-loon`, `tutorial:pricing-strategy`). Maakt het later mogelijk om te zien welke techniek/product cluster consistent presteert — sterker signaal dan de generieke tag alleen.

---

## 5. WEEKLY SNAPSHOTS

### Week [nummer] — [datum]
**Top 3 learnings (data-gebaseerd):**
1. [Learning op basis van cijfers]
2. [Learning op basis van cijfers]
3. [Learning op basis van cijfers]

**Veranderingen t.o.v. vorige week:**
- [Verschil]
- [Verschil]

---

## 6. BLORT VISUELE ANALYSES (handmatig toegevoegd door Robin)

*Robin plakt hier de BLORT analyse rapporten na het draaien van /blort-social-analyze.*

### Week [nummer] — BLORT rapport
[Robin plakt hier het BLORT rapport]

---

## 7. MONTHLY CONTENT INTELLIGENCE REPORT

### [Maand] [Jaar]
*Wordt automatisch gegenereerd op de eerste maandag van elke maand.*

[Zie sectie "Monthly Report" hieronder voor het format]
```

---

## Update Procedure (na elke /social-report)

### Stap 1: Zoek het Google Doc
Gebruik `mcp__google__drive_files_search` met query: `name = 'Content Learnings' and mimeType = 'application/vnd.google-apps.document'`

Als het niet bestaat, maak het aan met `mcp__google__docs_document_create` en vul de basisstructuur in.

### Stap 2: Lees huidige data
Gebruik `mcp__google__docs_document_get` om de huidige inhoud te lezen.

### Stap 3: Update secties
Op basis van de nieuwe /social-report data:

1. **Format performance tabel** — herbereken rolling 4-weken gemiddelden
2. **Timing patronen** — voeg nieuwe datapunten toe
3. **Caption hook database** — voeg nieuwe hooks toe met hun scores
4. **Onderwerp tags** — tag nieuwe posts en update gemiddelden
5. **Weekly snapshot** — voeg een nieuwe week-entry toe

### Stap 4: Schrijf updates
Gebruik `mcp__google__docs_document_update` om de wijzigingen door te voeren.

---

## Monthly Content Intelligence Report

Op de eerste maandag van elke maand, genereer automatisch:

```
# Monthly Content Intelligence Report — [Maand] [Jaar]

## Executive Summary
- Totaal posts: [x]
- Totaal reach: [x]
- Gemiddelde engagement rate: [x%]
- Net followers: [+/-x]
- Best performing format: [type]
- Best performing dag: [dag]

## Format Trends (maand)
[Tabel met per-format performance]

## Top 10 Posts van de Maand
[Tabel met top 10 op engagement score]

## Hook Analyse
- Meest gebruikte hook type: [type] ([x]×)
- Best presterende hook type: [type] (gem. score: [x])
- Beste individuele hook: "[tekst]"

## Timing Insights
- Beste dag: [dag] (gem. engagement: [x])
- Beste tijdslot: [tijd]
- Optimal post frequentie: [x] posts/week

## Onderwerp Performance
[Tabel met per-tag performance]

## Vergelijking met Vorige Maand
| Metric | Vorige maand | Deze maand | Verschil |
|--------|-------------|-----------|----------|
| ... | | | |

## Aanbevelingen (data-gebaseerd)
1. **Format:** [aanbeveling op basis van trends]
2. **Timing:** [aanbeveling op basis van trends]
3. **Hooks:** [aanbeveling op basis van trends]
4. **Frequentie:** [aanbeveling op basis van trends]

## Open vragen voor BLORT analyse
[Vragen die alleen door visuele analyse beantwoord kunnen worden]
```

---

## Integratie met andere commands

### /script-youtube
Voordat een script wordt geschreven:
1. Raadpleeg Content Learnings → Caption Hook Database → welke hook types scoren het best
2. Gebruik de best presterende hook types als suggestie
3. Vermeld: "Op basis van Content Learnings scoort [hook type] het best (gem. score: [x])"

### /blort-prompt
Voordat een briefing wordt geschreven:
1. Raadpleeg Content Learnings → Format Performance → welk format presteert het best
2. Raadpleeg → Timing Patronen → wanneer posten
3. Raadpleeg → Onderwerp Tags → welke onderwerpen scoren het best
4. Verwerk deze inzichten in de briefing

### /social-content
Bij het plannen van social content:
1. Raadpleeg alle secties van Content Learnings
2. Baseer format, timing en hook suggesties op de data

---

## Regels
- ALTIJD Instagram ID `17841403335662168` en Facebook Page ID `215391235203393`
- NOOIT video-inhoud analyseren — alleen cijfers, formats, timing en caption tekst
- ALTIJD onderscheid maken tussen "data-gebaseerd" (Claude Code) en "visueel-gebaseerd" (BLORT)
- Content Learnings is een levend document — update na ELKE /social-report
- Monthly report wordt automatisch gegenereerd op de eerste maandag van de maand
- Alle data-conclusies moeten onderbouwd zijn met specifieke cijfers
- Als er te weinig data is voor een conclusie (minder dan 4 weken), vermeld dit expliciet
