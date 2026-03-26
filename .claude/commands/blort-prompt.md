# BLORT Prompt Generator

Genereer een beknopte, specifieke briefing die Robin direct in BLORT AI kan plakken. BLORT heeft al alle context over Sempertex Europe, de tone of voice, doelgroep en Hormozi frameworks. Geef dus GEEN merkcontext, kleurcodes, fonts of achtergrondinfo mee — alleen de opdracht.

## Input
De gebruiker geeft een korte beschrijving van wat nodig is. Bijvoorbeeld: "YouTube script Link-O-Loon tips", "email flow voor SYBB workshop", "Instagram carrousel pricing tips".

Als er een argument is meegegeven, gebruik dat als briefing: $ARGUMENTS

## Hoe de briefing op te bouwen

Stel jezelf deze vragen en verwerk de antwoorden in de briefing:

1. **Wat** — Welk type content? (script, email flow, social post, carrousel, ad, campagne, thumbnail, banner)
2. **Platform** — Waar wordt het gepubliceerd? (YouTube, Instagram Reel, IG carrousel, TikTok, LinkedIn, Facebook, email, Meta ads)
3. **Onderwerp** — Waarover gaat het specifiek?
4. **Doel** — Wat moet het opleveren? (verkoop, educatie, awareness, lead gen, event tickets, engagement)
5. **Specs** — Harde eisen: lengte/duur, aantal slides, aantal emails, format, afmetingen
6. **Producten/events** — Welke specifieke producten, kleuren, finishes, workshops of events zijn relevant?

Gebruik de kennisbestanden alleen om de juiste productnamen, eventnamen of specifieke details op te zoeken als de gebruiker daar vaag over is:
- `Kennis/Products/producten-overzicht.md` — productnamen en specificaties
- `Kennis/Voorgaande campagnes/campagne-historie.md` — campagne- en eventnamen
- `Content/Scripts/filming-plan-referentie-denise-maart2025.md` — bestaande content formats

## Output format

```
## BLORT Briefing — [korte titel]

**Type:** [content type]
**Platform:** [kanaal/platform]
**Doel:** [wat het moet opleveren]

**Onderwerp:**
[1-3 zinnen over het specifieke onderwerp]

**Specs:**
- [lengte/duur/aantal/format]
- [afmetingen indien visueel]
- [taal]

**Specifiek benoemen:**
- [relevante producten, events, namen, data]

**Script format:**
[Zie hieronder — kort of lang bepaalt het format]

**Hormozi frameworks:**
[Zie hieronder — altijd opnemen, kort houden]

**Aanvullende eisen:**
- [alles wat BLORT moet weten dat niet standaard is]
```

## Hormozi frameworks instructie

Voeg ALTIJD een kort **Hormozi frameworks** blok toe aan de briefing. BLORT heeft de Hormozi kennis, maar moet weten WELKE frameworks relevant zijn voor deze specifieke opdracht. Noem ze kort bij naam — niet uitleggen, alleen activeren.

Kies uit deze frameworks op basis van het content type:

| Content type | Relevante Hormozi frameworks |
|---|---|
| Video script (elke lengte) | Hook types (statement/command/question/conditional/story), WHAT & WHY free — HOW paid, 70-20-10 rule for hooks, SPCL framework |
| Ad / campagne | GOATed Ads assembly (hooks × bodies × CTAs), awareness levels (Schwartz pyramid), 5 ad formats, SPCL framework |
| Email flow | Lead nurture (availability, speed, personalisation, volume), BAMFAM, push/pull incentives |
| Social post / carrousel | Hook-first principle, SPCL framework, 70-20-10 rule for hooks |
| Landing page | Proof, urgency, risk reversal, congruence with ads |

**SPCL is standaard.** Het SPCL framework (Status, Power, Credibility, Likeness) moet bij ALLE content types worden toegepast — het bepaalt welk type invloed de content opbouwt bij de kijker. Vermeld in de briefing altijd welke SPCL-dimensie(s) de content moet versterken.

Formuleer het in de briefing als een korte instructie, bijvoorbeeld:
> Apply Hormozi hook types (write 3 variants: statement, command, conditional). Use the WHAT & WHY free / HOW paid rule for the body. Follow the 70-20-10 rule for hook selection.

Houd het op 1-3 zinnen. Geen uitleg van de frameworks zelf — alleen welke BLORT moet toepassen en hoe.

## Script format instructie

Voeg dit ALTIJD toe aan de briefing als het om een video- of audioscript gaat:

**Als SHORT FORM (Reels, TikTok, Shorts — onder 60s):**
> Write the script word-for-word. Every line should be ready to read or memorise as-is.

**Als LONG FORM (YouTube, Podcast — above 5 min):**
> Do NOT write a word-for-word script. Write a structured roadmap instead:
> - Hook and CTA: write these out word-for-word
> - Body: section titles, talking points as bullets, [DEMO] and [B-ROLL] markers, transition sentences between sections, time estimates per section, key quotes that must be said verbatim
> - The script should read like cue cards, not a teleprompter
>
> **Short form clip suggestions:**
> After the full script, provide 5-15 short form clip opportunities from this video. For each clip:
> - Timestamp / section where the clip lives
> - Working title for the clip
> - Platform(s): Reels, TikTok, Shorts (or all three)
> - Duration estimate (15-60s)
> - The hook for the clip (word-for-word — this is short form, so write it ready to use)
> - Why this moment works as a standalone clip (visual payoff, surprising insight, quotable line, satisfying demo)
>
> Prioritize clips that: have a strong visual moment, contain a standalone tip or insight, feature a surprising result or reveal, or include a quotable one-liner. The clips should work WITHOUT context from the full video.

**Als ADS (Meta ads, YouTube ads — 15-60s):**
> Write the script word-for-word. Every line should be ready to read or memorise as-is.

Bepaal short vs. long op basis van de duur/het platform in de briefing. Als het niet duidelijk is, default naar:
- Reels, TikTok, Shorts → short form → woord-voor-woord
- Ads → ads → woord-voor-woord
- YouTube long form, Podcast → long form → routekaart + short form clip suggesties

## Regels
- Kort en to the point — geen context die BLORT al heeft
- Geen tone of voice uitleg, geen Hormozi uitleg, geen merkbeschrijving
- Geen kleurcodes of font-specs (BLORT kent die)
- Wel specifiek over: productnamen, eventnamen, data, aantallen, lengtes
- De briefing is in het Engels (BLORT werkt in het Engels)
- Als de gebruiker vaag is over het type of platform, vraag door — liever een specifieke briefing dan een vage
