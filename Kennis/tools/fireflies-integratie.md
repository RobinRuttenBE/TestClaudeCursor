# Fireflies.ai Integratie — Meeting Transcripts Pipeline

## Overzicht

Fireflies.ai neemt meetings automatisch op, transcribeert ze en levert transcripts + samenvattingen via een GraphQL API. Claude Code haalt deze op en verwerkt ze naar de kennisbase.

## Architectuur

```
Meeting (Google Meet / Zoom / Teams)
  ↓
Fireflies.ai Bot (fred@fireflies.ai) joins automatisch
  ↓
Fireflies transcribeert + genereert samenvatting
  ↓
Claude Code → fireflies_fetch.py → GraphQL API
  ↓
kennis/content/transcripts/YYYY-MM-DD_meeting-title.md
```

## Setup Stappen

### 1. Fireflies Account

- Maak account aan op https://fireflies.ai
- Plan: Free (800 min opslag, 1 zetel) of Pro ($10/mo, onbeperkt)
- Koppel je Google Calendar zodat Fred automatisch meetings joint

### 2. API Key

- Ga naar https://app.fireflies.ai/integrations
- Klik op "Fireflies API" 
- Kopieer je API key
- Sla op als environment variable:

```bash
# In je .bashrc of .zshrc:
export FIREFLIES_API_KEY="jouw_api_key_hier"

# Of in je project .env:
FIREFLIES_API_KEY=jouw_api_key_hier
```

### 3. Script Installatie

```bash
pip install requests python-dateutil
# Script staat in: scripts/fireflies_fetch.py
```

### 4. Gebruik

```bash
# Toon beschikbare transcripts
python scripts/fireflies_fetch.py list

# Haal laatste 7 dagen op
python scripts/fireflies_fetch.py fetch

# Haal laatste 30 dagen op
python scripts/fireflies_fetch.py fetch --days 30

# Specifiek transcript ophalen
python scripts/fireflies_fetch.py fetch --id "transcript_id_hier"

# Alles ophalen
python scripts/fireflies_fetch.py fetch --all
```

## Output Structuur

Elk transcript wordt opgeslagen als markdown:

```
kennis/content/transcripts/
├── 2026-03-10_weekly-sync-sofie.md
├── 2026-03-12_brand-ambassador-call.md
├── 2026-03-14_denise-content-planning.md
└── ...
```

### Markdown Structuur per Transcript

```markdown
# Meeting Titel

- **Datum**: 2026-03-10
- **Duur**: 45m 12s
- **Organisator**: robin@sempertexeurope.com
- **Deelnemers**: Robin, Sofie, Denise
- **Fireflies ID**: abc123
- **Link**: https://app.fireflies.ai/view/abc123

## Samenvatting
[Automatisch gegenereerd door Fireflies]

## Onderwerpen
[Outline van besproken punten]

## Actiepunten
[Geëxtraheerde action items]

## Keywords
[Relevante termen]

---

## Volledig Transcript
[Speaker-gelabeld transcript met timestamps]
```

## Claude Code Integratie

### Slash Command: /fetch-meetings

Claude Code kan het script aanroepen met:

```bash
python scripts/fireflies_fetch.py fetch --days 7
```

### Gebruik in Claude Code taken

Na het ophalen van transcripts kan Claude Code:

1. **Samenvattingen verrijken** — Fireflies-samenvatting aanvullen met STX EU context
2. **Action items extraheren** — Naar een apart actiepunten-overzicht
3. **Content-ideeën taggen** — Relevante quotes/onderwerpen markeren voor BLORT AI
4. **Kennisbase updaten** — Nieuwe inzichten toevoegen aan relevante kennis-bestanden

### Voorbeeld Claude Code Prompt

```
Lees de nieuwste transcripts in kennis/content/transcripts/ en:
1. Maak een samenvatting per meeting in het Nederlands
2. Extraheer alle actiepunten met verantwoordelijke persoon
3. Markeer content-ideeën die relevant zijn voor social media of podcast
4. Sla de verwerkte samenvatting op in kennis/content/meeting-summaries/
```

## API Details

- **Endpoint**: https://api.fireflies.ai/graphql
- **Auth**: Bearer token in Authorization header
- **Rate limits**: Afhankelijk van plan (Free: beperkt, Pro: ruimer)
- **Data**: Transcripts bevatten sentences met speaker labels, timestamps, sentiment, en NLP-filters (tasks, questions, metrics, pricing, dates)

## Fireflies Instellingen (aanbevolen)

- **Auto-join**: AAN — Fred joint automatisch alle calendar meetings
- **Taal**: Engels of Nederlands (Fireflies ondersteunt beide)
- **Privacy**: Controleer of alle deelnemers akkoord zijn met opname
- **Retentie**: Stel in op basis van GDPR-vereisten

## Kosten

| Plan | Prijs | Opslag | Features |
|------|-------|--------|----------|
| Free | €0 | 800 min | Basis transcriptie, beperkte AI |
| Pro | ~€10/mo | Onbeperkt | Volledige API, AI samenvattingen |
| Business | ~€19/mo | Onbeperkt | Team features, analytics |

Pro is voldoende voor de STX EU use case.
