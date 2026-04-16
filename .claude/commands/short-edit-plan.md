---
description: Analyseer een short form video + transcript en stel een editing plan voor met hook, overlays, effects en assets. Voor Reels, Shorts en TikToks.
---

# /short-edit-plan

Analyseer een short form video bestand + transcript en stel een volledig editing plan voor.

**Short form = Reels, Shorts, TikToks.** Typisch 15-90 seconden, 9:16 verticaal, fast paced maar niet overladen. Overlays verschijnen alleen waar het script het verdient — geen overbodige visuele ruis.

**Belangrijk:** als de video horizontaal is of langer dan 90 seconden, gebruik `/video-edit-plan` in plaats daarvan.

## Input

De gebruiker geeft:
1. Een video bestand (in `remotion-stx/public/videos/shorts/` of `remotion-stx/public/videos/`)
2. Het volledige transcript (geplakt of als bestand reference)

**Let op:** de video is al gecut en klaar. Jij voegt alleen overlays, effects en branding toe. Captions (woord-voor-woord ondertiteling) worden door de gebruiker zelf achteraf toegevoegd — plan er rekening mee dat de onderste 300px gereserveerd blijft voor captions.

## Proces

1. **Lees referentiebestanden (verplicht):**
   - `.claude/skills/auto-video-editor/SKILL.md` — rol, branding, regels
   - `.claude/skills/stx-overlay-style/SKILL.md` — exacte code-patronen per overlay type
   - `.claude/skills/stx-shortform-style/SKILL.md` — short form specifieke pacing, layout, safe zones, hook regels, nieuwe overlay types (hook-caption, follow-cta)
   - `.claude/skills/auto-video-editor/video-log.md` — leerpunten uit eerdere video's (filter op `[SHORT]` tag voor short form inzichten)
   - `.claude/rules/video-asset-checklist.md` — asset checklist
   - `CLAUDE.md` voor brand context

2. **Lees het transcript volledig** voordat je iets voorstelt. Identificeer:
   - **De hook** (eerste 1-3 seconden) — wat is de opener? Een statement, vraag, belofte, of cijfer?
   - **De payoff** — wat is de kern boodschap? Waarom kijkt iemand dit af?
   - **De CTA** — wat moet de kijker doen na afloop?
   - **Key visuele momenten** — concrete cijfers, tips, product-namen, namen van mensen, statements die versterkt horen te worden met een overlay
   - **Dead air** — momenten waar de spreker gewoon praat zonder visueel anker nodig (laat die leeg, niet geforceerd vullen)

3. **Stel een editing plan voor** volgens onderstaand format. Wacht op goedkeuring of aanpassingen voordat je gaat bouwen.

## Short Form Regels (STRIKT)

- **Formaat**: 9:16, composition 1080x1920 @ 30fps
- **Eerste 3 seconden = HOOK**: altijd een visueel sterk element binnen de eerste 90 frames. Nooit een trage fade-in of stilte. De hook overlay komt binnen 0-15 frames in beeld.
- **Overlay cadence**: 1 overlay per 5-10 seconden, alleen als het script het verdient. Niet forceren. Als 15 seconden niks visueels nodig heeft, laat het rustig.
- **Max 1 overlay tegelijk**: 9:16 is krap, geen ruimte voor stacking.
- **Overlay duration**: 2-5 seconden per overlay.
- **Safe zone onderaan**: onderste 300px (y: 1620-1920) vrijhouden voor user-added captions.
- **Safe zone bovenaan**: bovenste 150px vrijhouden voor platform UI (progress bar, username).
- **Outro**: geen YouTube subscribe bar. Gebruik `follow-cta` type uit `stx-shortform-style`.
- **Pacing**: nooit meer dan 3 effects achter elkaar binnen 6 seconden. Laat de video ademen.
- **Motion design intensiteit**: iets hoger dan long form (kleinere schermen hebben meer motion nodig) maar nooit overweldigend.

## Output

### Sectie: DE HOOK (Moment 1)

Omdat de hook het belangrijkste moment is, beschrijf die uitgebreider dan de rest:

- **Exacte tekst** (max 6-8 woorden, liefst 3-6)
- **Hook content type** (payoff belofte, counter-intuitive claim, credibility stat, curiosity gap, direct callout, testimonial fragment, product news) — zie `stx-shortform-style/SKILL.md` sectie "Hook content types"
- **Layout**: positie op 9:16 frame (meestal top-center y: 300-500px), fontSize (110-140px), Rethink Sans Extra Bold, geel vak (#ffdb5a) met donkerpaarse tekst OF donkerpaars (#1b073d) vak met witte tekst
- **Animatie**: pop scale 0 → 115% → 100% binnen 15 frames, spring `{ damping: 10, stiffness: 140 }`
- **Visuele backup**: subtle shake 2-3px, gradient flash, of floating particles
- **Waarom deze hook werkt** voor dit onderwerp en doelpubliek (balloon artists, decorateurs, problem solvers)

### Hoofdtabel

| # | Timestamp | Type | Inhoud | Effect in/uit | Geluid | Assets nodig |
|---|-----------|------|--------|---------------|--------|--------------|
| 1 | 0:00-0:03 | hook-caption | "I booked 40 weddings in 2025" | Pop in 0→115→100% / fade out | Bass hit + woosh | Geen — bouw zelf |
| 2 | 0:08-0:12 | stx-tip | "Inflate to 5 inch for consistency" | Slide in rechts / slide out | Soft pop | public/images/[...] |
| 3 | ... | ... | ... | ... | ... | ... |

### Sectie: ASSETS DIE IK VAN JOU NODIG HEB

Lijst per asset met **specifieke** beschrijving:

- **Close-up foto van de afgewerkte design** (goed belicht, 9:16 friendly crop — vertical of square werkt, landscape niet) — voor Moment 3
- **Product foto van Reflex Galaxy Blue** (witte achtergrond, 9:16 crop) — voor Moment 5
- ... etc

Voor elke asset: **wat exact** + **waar** + **welk moment** + **waarom** + **crop oriëntatie**.

### Sectie: ASSETS DIE IK ZELF REGEL

- Animaties (Lottie via `/find-assets` of programmatisch in Remotion)
- Gradiënten en achtergrond effecten
- Tekst overlays (inclusief hook-caption en follow-cta)
- Sound effects (uit bestaande library in `public/sound-effects/`)
- Color grade

### Sectie: ACHTERGRONDMUZIEK

- **Track**: welke track past bij de energie
- **Volume**: -18 tot -22dB
- **Timing**: start vanaf frame 0, geen fade-in
- **Fade out**: korte fade (15 frames) of hard cut
- **Loop**: meestal niet nodig bij <60s

### Sectie: COLOUR GRADING

Standaard `contrast(1.08) saturate(1.20)`. Bij specifieke sfeer pas aan.

### Sectie: SUGGESTIES VOOR MOTION DESIGN

- Ken Burns zoom op statische shots
- Gradient flash op emphasis momenten
- Subtle shake bij impactvolle claims
- Floating particles op rustige momenten
- Scene transitions met swipe bij topic wissels

### Sectie: GESCHATTE SCOPE

- Aantal momenten
- Aantal nieuwe overlay types (normaal 0 — hergebruik uit `stx-overlay-style` en `stx-shortform-style`)
- Aantal assets nodig van gebruiker
- Aantal assets te downloaden
- Geschatte build tijd

## Regels

- **Wacht altijd op goedkeuring** voordat je gaat bouwen
- **Stel eerst voor**, ga niet meteen bouwen
- Geef de gebruiker de kans om momenten te schrappen, toe te voegen of aan te passen
- Wees specifiek over assets — geen "een foto" maar "close-up met 9:16 vertical crop, goede belichting"
- Als een moment niet in een bestaand overlay type past, **stel een nieuw type voor** met korte beschrijving — documenteer pas na goedkeuring in `stx-shortform-style/SKILL.md`
- **Geen captions voorstellen** — gebruiker voegt die zelf achteraf toe
- **Geen overlay plaatsen op y < 150 of y > 1620** — safe zones
- **Hook is verplicht** — elke short begint met een hook-caption binnen 0-3 seconden
- **Stick tot bestaande overlay types waar mogelijk** — consistentie met branding is cruciaal

## Na goedkeuring

### Stap 0: Composition Setup (eerst checken)

Voordat je momenten bouwt, zorg dat de Remotion composition klaar staat:

1. **Check of `STX-Short-Template.tsx` bestaat** in `remotion-stx/src/compositions/`:
   - Zo niet: maak het aan met deze specs:
     - Dimensions: 1080 × 1920
     - FPS: 30
     - Basis component die `<Video>` rendert met safe zone dev guides (zichtbaar alleen in dev mode, zie `stx-shortform-style/SKILL.md` sectie "Remotion Composition Template")
     - Exports een `STXShortComponent` met `videoSrc` prop

2. **Maak een nieuwe composition aan voor deze specifieke short** in `remotion-stx/src/compositions/` met naam `STX-Short-[onderwerp].tsx`:
   - Importeert de overlays uit `remotion-stx/src/overlays/shorts/`
   - Rendert video + overlays in correcte Sequence timing

3. **Registreer in `remotion-stx/src/Root.tsx`**:
   ```tsx
   <Composition
     id="STX-Short-[NAAM]"
     component={STXShort[Naam]Component}
     durationInFrames={[video duur in frames, = seconden * 30]}
     fps={30}
     width={1080}
     height={1920}
     defaultProps={{ videoSrc: "videos/shorts/[bestand].mp4" }}
   />
   ```

4. **Verify composition opent correct** in Remotion Studio voordat je overlays gaat bouwen. Als de composition breekt, fix het eerst.

5. **Safe zone guides**: bevestig dat de dev-mode safe zone guides zichtbaar zijn in Remotion Studio zodat je tijdens bouwen kan zien waar de verboden zones zijn. Zie template in `stx-shortform-style/SKILL.md`.

### Stap 1+: Momenten bouwen

Werk de momenten één voor één af:

1. Bouw moment in `remotion-stx/src/overlays/shorts/` (aparte folder van long form overlays)
2. Import in de `STX-Short-[onderwerp].tsx` composition
3. Run `/video-review` per moment
4. Wacht op gebruiker feedback of `ja` / `nee` op WARN/FIX items
5. Pas aan en doorgaan naar volgend moment
6. Aan het einde: `/video-polish` voor de hele compositie, dan finale `/video-review`
7. Update `video-log.md` met short form specifieke learnings — markeer entries met `[SHORT]` tag zodat long form learnings niet vermengd raken

### Stap laatste: Render

Na goedkeuring: render in 1080x1920 MP4 naar `remotion-stx/out/shorts/[naam].mp4`. Lever het bestandspad aan de gebruiker zodat hij de captions kan toevoegen in CapCut of Instagram.
