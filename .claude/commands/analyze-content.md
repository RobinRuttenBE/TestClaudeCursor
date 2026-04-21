# Content Analyse

Analyseer een bestaand stuk content (caption, script, video, post) volledig op kwaliteit en effectiviteit.

## Input
De gebruiker plakt een caption, script, link, of beschrijving van een bestaande post of video.

Als er een argument is meegegeven, gebruik dat als content om te analyseren: $ARGUMENTS

## Voorbereiding

Lees voor je begint:
1. `.claude/skills/content-analysis/SKILL.md` — het volledige analyse framework
2. `Kennis/Brand/tone-of-voice.md` — tone of voice regels
3. `Bronnen/Alex Hormozi/100m-hooks-playbook.md` — hook types en scoring
4. `Content/Transcripts/social-media-strategy-spcl.md` — SPCL framework
5. Indien de content techniek/product/pricing/brand raakt: open `Kennis/Balloon Knowledge/INDEX.md` en lees het relevante bestand. Gebruik dit om inhoudelijke claims te toetsen (klopt de techniek, klopt het pricing-advies, klopt het product-detail) en om de SPCL Credibility-score te onderbouwen.

## Analyse

Voer de volledige analyse uit zoals beschreven in de content-analysis skill:

1. **Hook Analyse** — Identificeer hook type (Hormozi), call out, waarde-belofte, awareness niveau. Score 1-10.
2. **Structuur Analyse** — Check Hook → Content Preview → Body → CTA structuur. Score 1-10.
3. **Tone of Voice Check** — Vergelijk met STX EU brand voice. Score 1-10.
4. **Platform Fit** — Format, duur, tone passend bij het platform? Score 1-10.
5. **SPCL Check** — Welke elementen van Status, Power, Credibility, Likeness zitten erin? Per element kracht 1-5.
6. **Engagement Patronen** — Positieve en negatieve patronen identificeren.
7. **Verbeterpunten** — Concrete suggesties met voorbeelden (geen vage feedback).
8. **Totaalscore** — X/40 met interpretatie.

## Output

Gebruik het output template uit de content-analysis skill. Eindig ALTIJD met:

### Top 3 Verbeterpunten
1. [concreet, met voorbeeld]
2. [concreet, met voorbeeld]
3. [concreet, met voorbeeld]

### Herschreven Hook Suggestie
**Origineel:** "[originele hook]"
**Herschreven (Statement):** "[nieuwe hook variant 1]"
**Herschreven (Conditional):** "[nieuwe hook variant 2]"

## Regels
- Alle 8 onderdelen doorlopen — geen shortcuts
- Scores zijn eerlijk — een 7 is al goed, 10 is uitzonderlijk
- Verbeterpunten zijn concreet met een voorbeeld erbij
- Herschreven hook altijd in twee varianten (verschillende Hormozi types)
- SPCL check is verplicht
- Als het platform niet duidelijk is, vraag ernaar
- Bij meerdere posts: voeg een patronen rapport toe aan het einde
