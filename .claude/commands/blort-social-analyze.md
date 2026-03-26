# /blort-social-analyze — BLORT Social Content Analyse Prompt Generator

Genereer een BLORT prompt op basis van de engagement data uit /social-report. BLORT kan wél video's bekijken — Claude Code niet. Claude Code levert de DATA (top 5 en bottom 5 posts), BLORT doet de VISUELE analyse.

## Account IDs (hardcoded)

| Platform | ID |
|----------|----|
| **Instagram Business** | `17841403335662168` |
| **Facebook Page** | `215391235203393` |

**NOOIT andere accounts gebruiken.**

## Stap 1: Data ophalen

Haal de laatste week aan posts op met engagement data. Gebruik ALLEEN het Sempertex Europe account.

### Instagram posts
Gebruik `mcp__instagram__instagram_get_media` met:
- userId: `17841403335662168`
- limit: 25
- fields: `id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count`

### Per post: insights
Voor elke post, gebruik `mcp__instagram__instagram_get_media_insights` met:
- mediaId: [post ID]
- metric: `engagement,impressions,reach,saved,shares` (IMAGE/CAROUSEL)
- metric: `engagement,impressions,reach,saved,shares,plays` (VIDEO)

### Reels
Gebruik `mcp__instagram__instagram_get_reels` met:
- userId: `17841403335662168`
- limit: 10
- fields: `id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count,play_count`

## Stap 2: Rangschik op engagement

Bereken per post een engagement score:
```
engagement_score = likes + (comments × 3) + (saves × 5) + (shares × 5)
```
*Comments, saves en shares wegen zwaarder omdat ze meer intentie tonen.*

Sorteer alle posts op engagement_score en selecteer:
- **Top 5** — hoogste engagement
- **Bottom 5** — laagste engagement

## Stap 3: Toon data-overzicht

Voordat je de BLORT prompt genereert, toon eerst het data-overzicht aan Robin:

```
## Data overzicht — [periode]

### TOP 5 posts (hoogste engagement)
| # | Type | Datum | Likes | Comments | Saves | Shares | Score | Link |
|---|------|-------|-------|----------|-------|--------|-------|------|
| 1 | ... | ... | ... | ... | ... | ... | ... | [link] |

### BOTTOM 5 posts (laagste engagement)
| # | Type | Datum | Likes | Comments | Saves | Shares | Score | Link |
|---|------|-------|-------|----------|-------|--------|-------|------|
| 1 | ... | ... | ... | ... | ... | ... | ... | [link] |
```

## Stap 4: Genereer BLORT prompt

Genereer de volgende BLORT prompt in het Engels. Vul de [variabelen] in met de echte data en links.

```
## BLORT Social Analyse Prompt — Week [nummer]

### Kopieer onderstaande prompt naar BLORT:

---

I need you to visually analyze 10 Instagram posts from Sempertex Europe (@sempertexeurope). I'm splitting them into TOP 5 (highest engagement) and BOTTOM 5 (lowest engagement) so we can find what works visually.

**IMPORTANT: You CAN watch the videos. Claude Code cannot. That's why this analysis is done by you.**

---

## TOP 5 POSTS (highest engagement this week)

[Voor elke post:]

### Post [#]: [media_type] — Posted [datum]
- **Link:** [permalink]
- **Caption:** "[volledige caption]"
- **Engagement data:** [likes] likes, [comments] comments, [saves] saves, [shares] shares
- **Engagement score:** [score]
- **Reach:** [reach] | **Impressions:** [impressions]

[Herhaal voor alle 5]

---

## BOTTOM 5 POSTS (lowest engagement this week)

[Zelfde format als top 5]

---

## WHAT I NEED YOU TO ANALYZE

**For EACH of the 10 posts, analyze:**

### Visual Analysis
1. **Setting & Background:** What does the visual environment look like? (studio, outdoor, warehouse, office, event)
2. **Movement & Energy:** Is there movement? Fast cuts? Slow reveal? Static?
3. **Text Overlays:** Are there text overlays? What do they say? Are they readable?
4. **Color palette:** Does it match the Sempertex brand colors? (purple primary, warm tones)
5. **Thumbnail/First frame:** Would this stop your scroll? Why or why not?
6. **Production quality:** Professional, semi-pro, or raw/authentic?
7. **People:** Who appears? How many? What are they doing? Are they relatable to balloon professionals?

### Spoken Hook (first 3 seconds)
1. **What is said** in the first 3 seconds? (transcribe it)
2. **Hook type** (classify: Statement / Command / Question / Conditional / List / Story / Exclamation)
3. **Does the hook match the visual?** (or is there a disconnect?)
4. **Scroll-stopper verdict:** Would YOU stop scrolling? Why?

### SPCL Elements (visual)
- **S — Status:** Do the visuals show expertise, resources, or impressive results?
- **P — Power:** Do the visuals demonstrate something the viewer can replicate?
- **C — Credibility:** Is there visual proof? (product quality, event scale, professional setup)
- **L — Likeness:** Does it feel authentic and relatable to the target audience (balloon artists)?

---

## PATTERNS REPORT (after analyzing all 10)

### What TOP performers have in common visually
- List 3-5 visual patterns shared by the top 5

### What BOTTOM performers have in common visually
- List 3-5 visual patterns shared by the bottom 5

### Hook Analysis Cross-Post
- Which spoken hook types score highest?
- Which visual hooks (first frame) stop the scroll?
- Is there a correlation between hook type and engagement?

### Visual Style Recommendations
Based on the patterns found:
1. **3 visual elements to ALWAYS include** (based on top performers)
2. **3 visual elements to AVOID** (based on bottom performers)
3. **Ideal visual formula** for a Sempertex Europe reel (setting + movement + text + hook)

### Content Ideas
Based on the visual patterns that work, suggest 5 new content ideas:
- Each with a visual concept (describe the shot/setup)
- A spoken hook for the first 3 seconds
- Which SPCL elements it would hit
- Why it would likely perform well (based on the patterns)

---

Format everything as a structured report with clear headers and tables where possible. Be specific — reference the actual posts by number when making comparisons.

---
```

## Stap 5: Context toevoegen

Voeg onder de BLORT prompt toe:

```
---

### Extra context voor Robin:

**Data samenvatting:**
- Totaal posts geanalyseerd: [x]
- Gemiddelde engagement score: [x]
- Beste format deze week: [type] (gem. score: [x])
- Slechtste format deze week: [type] (gem. score: [x])

**Tip:** Plak de bovenstaande prompt in BLORT. BLORT zal de video's bekijken en de visuele analyse doen. Voeg het BLORT rapport daarna toe aan het Google Doc "Content Learnings" onder de sectie "BLORT Visuele Analyses".
```

## Regels
- ALTIJD Instagram ID `17841403335662168` — geen andere accounts
- Claude Code analyseert GEEN video-inhoud — alleen data (cijfers, captions, formats, timing)
- BLORT doet de visuele analyse — deze command levert alleen de data en genereert de prompt
- De BLORT prompt is ALTIJD in het Engels
- Geen Hormozi of tone of voice uitleg in de prompt — BLORT kent dit al
- Vul ALTIJD de echte data, links en captions in — geen placeholders
- Als er een argument is meegegeven ($ARGUMENTS), gebruik dat als aanvullende context (bv. "focus op reels" of "vergelijk met vorige maand")
