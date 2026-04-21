# BLORT Content Analyse Prompt Generator

Genereer een gestructureerde analyse-prompt die Robin in BLORT AI plakt om bestaande content te laten analyseren. BLORT kan video's bekijken en heeft alle context over Sempertex Europe, Hormozi frameworks en de SPCL methode.

Geef GEEN merkcontext, tone of voice uitleg of framework-uitleg mee — alleen de analyse-opdracht met het juiste output format.

## Account IDs (hardcoded)

Als Instagram/Facebook content wordt geanalyseerd, gebruik ALTIJD en ALLEEN het Sempertex Europe account:

| Platform | ID |
|----------|----|
| **Instagram Business** | `17841403335662168` |
| **Facebook Page** | `215391235203393` |

**NOOIT andere accounts gebruiken.** Als Instagram data moet worden opgehaald (bv. "onze laatste 10 Reels"), gebruik `mcp__instagram__instagram_get_media` met userId `17841403335662168`.

## Input
De gebruiker beschrijft welke content geanalyseerd moet worden. Bijvoorbeeld: "onze laatste 10 Instagram Reels", "top 5 YouTube video's", "alle SYBB ads", "deze 3 posts [links]".

Als er een argument is meegegeven, gebruik dat als input: $ARGUMENTS

## Voorbereiding

Lees indien relevant om specifieke namen/details op te zoeken:
- `Kennis/Voorgaande campagnes/campagne-historie.md` — campagnenamen en details
- `Kennis/Products/producten-overzicht.md` — productnamen
- `.claude/skills/content-memory/SKILL.md` — raadpleeg Content Learnings voor context
- `Kennis/Balloon Knowledge/INDEX.md` — gebruik om techniek-namen/product-vocab correct te benoemen in de BLORT prompt (bv. "diamond weave panel", "20-bubble star", "Link-O-Loon column"). BLORT analyseert beter als de juiste vakterm in de instructie staat.

## Hoe de prompt op te bouwen

Stel jezelf deze vragen:

1. **Wat** — Welke content? (Reels, YouTube video's, ads, carrousels, emails, posts)
2. **Hoeveel** — Hoeveel stuks moeten geanalyseerd worden?
3. **Platform** — Op welk platform staat de content?
4. **Doel** — Wat wil Robin leren? (patronen vinden, hooks verbeteren, structuur checken, alles)
5. **Vergelijking** — Moet er vergeleken worden? (top vs. bottom performers, oud vs. nieuw, per platform)

## Output format

De prompt voor BLORT moet ALTIJD in het Engels zijn en dit format volgen:

```
## BLORT Analyse Prompt — [korte beschrijving]

### Kopieer onderstaande prompt naar BLORT:

---

Analyze the following [aantal] [content type] from Sempertex Europe's [platform] account.

**What to analyze:** [specifieke beschrijving van welke content — bv. "our last 10 Instagram Reels" of "the SYBB campaign ads"]

**For EACH piece of content, provide:**

**1. Hook Analysis**
- Hook type (classify as: Statement / Command / Question / Conditional / List / Story / Exclamation)
- Call out: does it address the target audience directly? Does the viewer think "this is about me"?
- Value promise: is there an implicit or explicit promise of value?
- First 3 seconds verdict: scroll-stopper or skip?
- Awareness level the hook targets (Most Aware / Product Aware / Solution Aware / Problem Aware / Unaware)
- **Hook score: X/10**

**2. Structure**
- Does it follow Hook → Content Preview → Body → CTA?
- Is the pacing right for the platform?
- Is the CTA clear and does it follow the pattern: confirm value → follow us → products available → link?
- **Structure score: X/10**

**3. Tone of Voice**
- Does it match the Sempertex brand? (professional but warm, confident not arrogant, educational, positive, community-focused, specific not generic)
- Any red flags? (mentioning competitors, "cheap/budget" language, corporate speak, fake urgency)
- **Brand fit score: X/10**

**4. SPCL Score**
Rate each element 0-5:
- **S — Status:** Does it demonstrate control over scarce resources or show results?
- **P — Power:** Does it give concrete instructions the viewer can follow for results?
- **C — Credibility:** Is there third-party proof? Reviews, results, external validation?
- **L — Likeness:** Is it authentic? Does it speak the audience's language? Show the human side?

**5. Platform Fit**
- Is the format correct for [platform]? (duration, aspect ratio, pacing, features used)
- **Platform fit score: X/10**

**6. Total Score: X/40**

---

**AFTER analyzing all [aantal] pieces, provide a PATTERNS REPORT:**

**Hook Patterns**
- Which hook types appear most in the top performers?
- Which hook types appear most in the worst performers?
- Most effective hooks (quote them verbatim)

**Content Pillar Performance**
- Rank which pillars perform best: Product showcase / Education / Inspiration / Community / Brand positioning / Entertainment

**What Top Performers Have in Common**
- List the 3-5 shared traits of the highest-scoring content

**What Worst Performers Have in Common**
- List the 3-5 shared traits of the lowest-scoring content

**Recurring Issues**
- Which improvement areas keep coming back across multiple pieces?

---

**CONCLUSION — Give me:**

**Top 3 Patterns to REPEAT** (with specific examples from the analyzed content)

**Top 3 Patterns to STOP** (with specific examples from the analyzed content)

**5 Concrete Content Ideas** based on what works — each idea should include:
- Working title
- Platform
- Hook suggestion (using the best-performing hook type)
- Which SPCL elements to emphasize
- Why this idea is likely to work (based on the patterns found)

---

Format the entire analysis as a structured report with clear headers. Use tables where possible. Be specific and actionable — no vague feedback.

---
```

## Aanpassingen per situatie

Pas de prompt aan op basis van de input:

**Als het om ads gaat**, voeg toe:
> Also analyze: ad format (Demonstration / Testimonial / Education / Story / Faceless), awareness level targeting, and CTA effectiveness (does it show what happens after clicking?).

**Als er een vergelijking gevraagd wordt** (top vs. bottom), voeg toe:
> Split the analysis into two groups: TOP PERFORMERS and BOTTOM PERFORMERS. After analyzing individually, do a comparative analysis: what specifically separates the winners from the losers?

**Als het om één specifiek stuk content gaat** (niet een batch), laat het patronen rapport weg en voeg toe:
> After the analysis, provide: 3 specific improvement suggestions with rewritten examples, and 2 alternative hook suggestions (different Hormozi hook types).

## Regels
- De BLORT prompt is altijd in het Engels
- Geen Hormozi uitleg — BLORT kent de frameworks, alleen het format en de opdracht geven
- Geen tone of voice beschrijving — alleen de checklist-items waartegen BLORT moet toetsen
- Geen merkcontext meegeven — BLORT heeft dit al
- Wel specifiek over: welke content, hoeveel stuks, welk platform, welk account
- Het output format is cruciaal — BLORT moet exact weten HOE het de analyse moet structureren
- Als de gebruiker vaag is over welke content, vraag door
