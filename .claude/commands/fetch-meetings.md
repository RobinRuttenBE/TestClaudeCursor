# /fetch-meetings

Haal de nieuwste meeting transcripts op van Fireflies.ai en verwerk ze voor de kennisbase.

## Stappen

1. Voer `python scripts/fireflies_fetch.py fetch --days 7` uit om nieuwe transcripts op te halen
2. Lees de opgehaalde bestanden in `kennis/content/transcripts/`
3. Voor elk nieuw transcript:
   a. Maak een verrijkte Nederlandse samenvatting (gebruik de Fireflies summary als basis)
   b. Extraheer actiepunten met verantwoordelijke persoon en deadline (indien genoemd)
   c. Identificeer content-ideeën die relevant zijn voor:
      - Social media posts
      - Podcast onderwerpen
      - YouTube video hooks
      - Email campagnes
   d. Sla de verwerkte samenvatting op in `kennis/content/meeting-summaries/YYYY-MM-DD_titel.md`
4. Update `kennis/content/meeting-summaries/INDEX.md` met de nieuwe entries
5. Print een overzicht van wat er is opgehaald en verwerkt

## Context

- Lees `kennis/brand/tone-of-voice.md` voor schrijfstijl
- Lees `kennis/brand/identity.md` voor merkcontext
- Transcripts bevatten meetings met team (Sofie, Denise, ambassadeurs) en externe partijen
- Focus op actionable takeaways, niet op letterlijke weergave

## Output formaat meeting-summary

```markdown
# [Meeting Titel] — [Datum]

**Deelnemers**: [namen]
**Duur**: [duur]

## TL;DR
[2-3 zinnen kernboodschap]

## Belangrijkste Beslissingen
- [beslissing 1]
- [beslissing 2]

## Actiepunten
| Wie | Wat | Deadline |
|-----|-----|----------|
| Robin | ... | ... |
| Sofie | ... | ... |

## Content Ideeën
- 📱 **Social**: [idee]
- 🎙 **Podcast**: [idee]  
- 🎬 **Video**: [idee]

## Relevante Context voor Kennisbase
[Nieuwe inzichten die relevant zijn voor bestaande kennisbestanden]
```
