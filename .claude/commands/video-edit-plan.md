---
description: Analyseer een video + transcript en stel een volledig editing plan voor met overlays, effects, assets en muziek.
---

# /video-edit-plan

Analyseer een video bestand + transcript en stel een volledig editing plan voor.

## Input

De gebruiker geeft:
1. Een video bestand (in `remotion-stx/public/videos/`)
2. Het volledige transcript (geplakt of als bestand reference in `remotion-stx/public/videos/Scripts/`)

## Proces

1. **Lees referentiebestanden:**
   - `.claude/skills/auto-video-editor/SKILL.md` — rol, branding, regels
   - `.claude/skills/stx-overlay-style/SKILL.md` — exacte code-patronen per overlay type
   - `.claude/skills/auto-video-editor/video-log.md` — leerpunten uit eerdere video's
   - `.claude/rules/video-asset-checklist.md` — asset checklist
   - `CLAUDE.md` voor brand context
   - `Kennis/Balloon Knowledge/INDEX.md` — gebruik om techniek/product-momenten in het transcript te herkennen en correct te benoemen in overlay teksten (bv. "diamond weave", "20-bubble star", "Link-O-Loon column", "deep tulip twist"). Zorgt voor accurate vakterm in lower thirds, tips en feature bars.

2. **Lees het transcript volledig** voordat je iets voorstelt. Identificeer:
   - Hoofdonderwerp en doelpubliek
   - Energie / pacing van de spreker
   - Natuurlijke "beats" (intro, opbouw, key moments, climax, outro)
   - Concrete momenten die om een visueel anker vragen (lijsten, tips, quotes, producten, vragen)

3. **Stel een editing plan voor** volgens onderstaand format. Wacht op goedkeuring of aanpassingen voordat je gaat bouwen.

## Output

### Hoofdtabel

| # | Timestamp | Type | Inhoud | Effect in/uit | Geluid | Assets nodig |
|---|-----------|------|--------|--------------|--------|--------------|
| 1 | 0:00-0:05 | part-intro | "PART X" + "How to..." | Pop in stagger / swipe right | Pop x4 + woosh | Geen — bouw zelf |
| 2 | ... | ... | ... | ... | ... | ... |

Houd de tabel beknopt — details kunnen onder.

### Sectie: ASSETS DIE IK VAN JOU NODIG HEB

Lijst per asset met **specifieke** beschrijving:

- **Foto van het eindresultaat van Audrey's design** (close-up, goed belicht) — voor Moment 4
- **Screenshot van de Sempertex Europe homepage** met scroll positie op de Ultra Pump sectie — voor Moment 8
- ... etc

Voor elke asset: **wat exact** + **waar** + **welk moment** + **waarom**.

### Sectie: ASSETS DIE IK ZELF REGEL

Lijst van wat Claude Code zelf bouwt zonder input:

- Animaties (Lottie via `/find-assets` of via Remotion components)
- Gradiënten en achtergrond effecten
- Tekst overlays
- Sound effects (uit bestaande library of via `/find-assets`)
- Color grade

### Sectie: ACHTERGRONDMUZIEK

- **Track:** welke track uit `public/sound-effects/` of `public/music/`
- **Volume:** standaard target volume (-20 tot -24dB)
- **Timing:** start, fade in, eventuele boost momenten, fade out
- **Loop:** wel/niet enabled

### Sectie: COLOUR GRADING

Beschrijving van de grading die wordt toegepast — standaard `contrast(1.08) saturate(1.15)` tenzij de video specifieke aanpassing nodig heeft.

### Sectie: SUGGESTIES VOOR MOTION DESIGN

Creatieve suggesties die de video naar een hoger niveau tillen — los van de standaard momenten:

- Eventuele Ken Burns zooms op statische beelden
- Lottie animaties die context toevoegen
- Achtergrond effecten die de hele video versterken
- Welke screenshots of templates nuttig zouden zijn

### Sectie: GESCHATTE SCOPE

- Aantal momenten
- Aantal nieuwe overlay types (indien relevant)
- Aantal assets nodig van gebruiker
- Aantal assets te downloaden

## Regels

- **Wacht altijd op goedkeuring** voordat je gaat bouwen
- **Stel eerst voor**, ga niet meteen bouwen
- Geef de gebruiker de kans om momenten te schrappen, toe te voegen of aan te passen
- Wees specifiek over assets — geen "een foto" maar "close-up van de twist techniek met linker hand zichtbaar"
- Als een moment niet in een bestaand overlay type past, **stel een nieuw type voor** met korte beschrijving — documenteer pas na goedkeuring
- Pacing volgen uit `auto-video-editor/SKILL.md` — eerste 30-60s veel energie, daarna 1 effect per 30-60s, laatste 30s sluit de loop
- **Overlay tekst in UK English.** Colour, favourite, realise, organise, centre, behaviour, catalogue. Nooit US spelling, tenzij het transcript specifiek anderstalig is en de gebruiker dat behouden wil. Volledige regels in `Kennis/Brand/tone-of-voice.md`.

## Na goedkeuring

Werk de momenten één voor één af:

1. Bouw moment in `remotion-stx/src/overlays/` (of update bestaand bestand)
2. Run `/video-review` per moment
3. Wacht op gebruiker feedback of `ja` / `nee` op WARN/FIX items
4. Pas aan en doorgaan naar volgend moment
5. Aan het einde: `/video-polish` voor de hele compositie, dan finale `/video-review`
6. Update `video-log.md` met wat gewerkt heeft en wat niet
