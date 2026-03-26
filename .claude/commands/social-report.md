# /social-report — Wekelijks Social Media Rapport

Haal ZELF alle data op via de Instagram/Facebook MCP. Geen handmatige input nodig. Gebruik ALTIJD en ALLEEN het Sempertex Europe account.

## Account IDs (hardcoded)

| Platform | ID |
|----------|----|
| **Instagram Business** | `17841403335662168` |
| **Facebook Page** | `215391235203393` |

**NOOIT andere accounts gebruiken.** Er zijn ook Ambition Avenue en Project accounts gekoppeld — deze NEGEREN.

## Voorbereiding

Bepaal de rapportageperiode:
- **Deze week:** Afgelopen maandag t/m zondag (7 dagen)
- **Vorige week:** De 7 dagen daarvoor (voor vergelijking)
- Gebruik ISO 8601 datums voor alle API calls

Lees de content-memory skill als die beschikbaar is:
- `.claude/skills/content-memory/SKILL.md` — voor het updaten van Content Learnings na het rapport

## Stap 1: Instagram Data Ophalen

### 1a. Account Insights (week overview)
Gebruik `mcp__instagram__instagram_get_account_insights` met:
- userId: `17841403335662168`
- metric: `impressions,reach,profile_views,website_clicks,follower_count`
- period: `day`
- since: [maandag deze week, ISO 8601]
- until: [zondag deze week, ISO 8601]

Haal ook de vorige week op voor vergelijking.

### 1b. Media posts deze week
Gebruik `mcp__instagram__instagram_get_media` met:
- userId: `17841403335662168`
- limit: 25
- fields: `id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count`

Filter op posts binnen de rapportageperiode.

### 1c. Per post: insights
Voor elke post deze week, gebruik `mcp__instagram__instagram_get_media_insights` met:
- mediaId: [post ID]
- metric: `engagement,impressions,reach,saved,shares` (voor IMAGE/CAROUSEL)
- metric: `engagement,impressions,reach,saved,shares,plays` (voor VIDEO/REEL)

### 1d. Stories
Gebruik `mcp__instagram__instagram_get_stories` met userId: `17841403335662168`.

### 1e. Reels
Gebruik `mcp__instagram__instagram_get_reels` met:
- userId: `17841403335662168`
- limit: 10
- fields: `id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count,play_count`

Filter op deze week.

### 1f. Follower data
Gebruik `mcp__instagram__instagram_get_follower_growth` als beschikbaar, anders bereken uit account insights.

## Stap 2: Facebook Data Ophalen

### 2a. Page Insights
Gebruik `mcp__instagram__facebook_get_page_insights` met:
- pageId: `215391235203393`
- metric: `page_impressions,page_engaged_users,page_fans,page_views_total,page_actions_post_reactions_like_total`
- period: `day`
- since: [maandag deze week]
- until: [zondag deze week]

### 2b. Page Posts
Gebruik `mcp__instagram__facebook_get_page_posts` met:
- pageId: `215391235203393`
- limit: 25
- since: [maandag deze week]
- until: [zondag deze week]

### 2c. Per post: insights
Voor elke post, gebruik `mcp__instagram__facebook_get_post_insights` met relevante metrics.

### 2d. Page Reach & Engagement
Gebruik `mcp__instagram__facebook_get_page_reach` en `mcp__instagram__facebook_get_page_engagement` als beschikbaar.

## Stap 3: Data Aggregeren & Rapport Schrijven

Stel het rapport samen in dit EXACTE format:

```
# 📱 Weekly Social Report — Week [nummer] ([maandag] t/m [zondag])

---

## INSTAGRAM — @sempertexeurope

### WEEKLY OVERVIEW
| Metric | Deze week | Vorige week | Verschil |
|--------|-----------|-------------|----------|
| Total views (impressions) | [x] | [x] | [+/-x%] |
| Total reach (unieke accounts) | [x] | [x] | [+/-x%] |
| Followers gained | [x] | [x] | [+/-x] |
| Followers lost | [x] | [x] | [+/-x] |
| Net followers | [+/-x] | [+/-x] | [+/-x] |
| Profile visits | [x] | [x] | [+/-x%] |
| Link clicks (bio) | [x] | [x] | [+/-x%] |

### CONTENT PERFORMANCE
| Metric | Aantal |
|--------|--------|
| Posts deze week | [x] |
| Reels deze week | [x] |
| Stories deze week | [x] |
| Carousels deze week | [x] |

### ENGAGEMENT
| Metric | Deze week | Vorige week | Verschil |
|--------|-----------|-------------|----------|
| Total likes | [x] | [x] | [+/-x%] |
| Total comments | [x] | [x] | [+/-x%] |
| Total saves | [x] | [x] | [+/-x%] |
| Total shares | [x] | [x] | [+/-x%] |
| Engagement rate | [x%] | [x%] | [+/-x pp] |

*Engagement rate = (likes + comments + saves + shares) / reach × 100*

### TOP 5 POSTS (op engagement)
| # | Type | Datum | Likes | Comments | Saves | Shares | Reach | Caption (eerste 50 tekens) | Link |
|---|------|-------|-------|----------|-------|--------|-------|---------------------------|------|
| 1 | [type] | [datum] | [x] | [x] | [x] | [x] | [x] | "[caption...]" | [permalink] |
| ... | | | | | | | | | |

### BOTTOM 5 POSTS (op engagement)
| # | Type | Datum | Likes | Comments | Saves | Shares | Reach | Caption (eerste 50 tekens) | Link |
|---|------|-------|-------|----------|-------|--------|-------|---------------------------|------|
| 1 | [type] | [datum] | [x] | [x] | [x] | [x] | [x] | "[caption...]" | [permalink] |
| ... | | | | | | | | | |

### PATRONEN (puur data, geen inhoudelijke analyse)
**Format performance:**
| Format | Gem. engagement rate | Gem. reach | Aantal |
|--------|---------------------|-----------|--------|
| Reel | [x%] | [x] | [x] |
| Carousel | [x%] | [x] | [x] |
| Static image | [x%] | [x] | [x] |

**Timing performance:**
| Dag | Gem. engagement | Beste post |
|-----|----------------|-----------|
| Ma | [x] | [caption snippet] |
| Di | [x] | ... |
| ... | | |

**Beste posttijd:** [dag + tijd] op basis van de data

**Week-over-week trends:**
- [Trend 1 op basis van cijfers]
- [Trend 2 op basis van cijfers]
- [Trend 3 op basis van cijfers]

---

## FACEBOOK — Sempertex Europe

### WEEKLY OVERVIEW
| Metric | Deze week | Vorige week | Verschil |
|--------|-----------|-------------|----------|
| Page impressions | [x] | [x] | [+/-x%] |
| Page reach | [x] | [x] | [+/-x%] |
| Page fans (totaal) | [x] | [x] | [+/-x] |
| Page views | [x] | [x] | [+/-x%] |
| Engaged users | [x] | [x] | [+/-x%] |

### CONTENT PERFORMANCE
| Metric | Aantal |
|--------|--------|
| Posts deze week | [x] |
| Videos deze week | [x] |

### ENGAGEMENT
| Metric | Deze week | Vorige week | Verschil |
|--------|-----------|-------------|----------|
| Total reactions | [x] | [x] | [+/-x%] |
| Total comments | [x] | [x] | [+/-x%] |
| Total shares | [x] | [x] | [+/-x%] |
| Engagement rate | [x%] | [x%] | [+/-x pp] |

### TOP 5 POSTS (op engagement)
[Zelfde tabel als Instagram]

### BOTTOM 5 POSTS (op engagement)
[Zelfde tabel als Instagram]

---

## CROSS-PLATFORM SAMENVATTING

| Metric | Instagram | Facebook | Totaal |
|--------|-----------|----------|--------|
| Total reach | [x] | [x] | [x] |
| Total engagement | [x] | [x] | [x] |
| Posts | [x] | [x] | [x] |
| Net followers/fans | [+/-x] | [+/-x] | [+/-x] |

**Key takeaways (puur data-gebaseerd):**
1. [Observatie op basis van cijfers]
2. [Observatie op basis van cijfers]
3. [Observatie op basis van cijfers]

⚠️ **Inhoudelijke analyse (hooks, visuele stijl, waarom iets werkt) kan Claude Code NIET doen — gebruik /blort-social-analyze voor video-analyse door BLORT.**
```

## Stap 4: Schrijf naar Google Sheet

Gebruik de Google Sheets MCP om data te schrijven naar de spreadsheet "Social Media Tracker":
1. Zoek of de spreadsheet bestaat via `mcp__google__drive_files_search` met query `name = 'Social Media Tracker' and mimeType = 'application/vnd.google-apps.spreadsheet'`
2. Als deze niet bestaat, maak hem aan
3. Schrijf data naar aparte tabs:
   - **Instagram Weekly** — weekoverzicht metrics per week (append een rij per week)
   - **Facebook Weekly** — weekoverzicht metrics per week
   - **Instagram Posts** — alle individuele post data (append rijen)
   - **Facebook Posts** — alle individuele post data
   - **Cross-Platform** — cross-platform samenvatting per week

## Stap 5: Update Content Learnings

Na het schrijven van het rapport:
1. Roep de content-memory skill aan (zie `.claude/skills/content-memory/SKILL.md`)
2. Update het Google Doc "Content Learnings" met de nieuwe patronen uit de data
3. Categoriseer: format performance, timing trends, caption hook patronen (eerste zin)

## Stap 6: Toon het rapport

Print het volledige rapport in de chat zodat Robin het direct kan lezen.

## Error handling

- Als een specifieke metric niet beschikbaar is via de API, noteer "N/A (niet beschikbaar via API)" en ga door
- Als er geen posts zijn in de rapportageperiode, vermeld dit
- Als de vergelijking met vorige week niet mogelijk is (eerste rapport), vermeld "Geen vorige week data — baseline wordt opgeslagen"
- Gebruik NOOIT een ander account ID dan de hardcoded Sempertex Europe IDs

## Regels
- ALTIJD Instagram ID `17841403335662168` en Facebook Page ID `215391235203393`
- NOOIT andere accounts gebruiken
- NOOIT video's inhoudelijk analyseren — Claude Code kan geen video's bekijken
- Patronen ALLEEN op basis van cijfers, formats, timing en captions (tekst)
- Verwijs naar /blort-social-analyze voor inhoudelijke video-analyse
- Schrijf het rapport in het Nederlands
- Alle data naar Google Sheet
