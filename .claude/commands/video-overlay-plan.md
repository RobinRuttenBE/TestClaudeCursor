# Video Overlay Plan — Transcript Analyse & Remotion Code Generator

Analyseer een video transcript en stel automatisch overlays, transities en effecten voor op basis van de beschikbare Remotion templates.

## Input
De gebruiker geeft een transcript van een gecut video met timestamps. Formaat kan variëren:
- `[00:00]` of `[0:00]` of `00:00 -` of `(00:00)` — allemaal acceptabel
- Sprekersnamen zijn optioneel maar worden gebruikt voor lower thirds
- $ARGUMENTS kan een pad naar een transcript-bestand bevatten

Als $ARGUMENTS een bestandspad is, lees dat bestand eerst.

## Voorbereiding

Lees voor je begint:
1. `.claude/skills/remotion-templates/SKILL.md` — alle beschikbare Remotion templates en hun parameters
2. `Kennis/Brand/tone-of-voice.md` — voor het beoordelen van key quotes
3. `Kennis/Balloon Knowledge/INDEX.md` — gebruik om techniek/product-momenten in het transcript correct te benoemen in text overlays en feature bars (juiste vakterm = hogere autoriteit). Bv. "Diamond Weave", "Pinch Twist", "Link-O-Loon", "Ultra Pump", "Reflex Crystal".

## Stap 1: Analyse

Analyseer het transcript op deze 6 elementen:

### 1. Lower Thirds (STX-LowerThird)
- Eerste keer dat elke spreker aan het woord is
- Detecteer namen uit het transcript of vraag ernaar
- Stel naam + functietitel voor

### 2. Text Overlays (STX-TextOverlay)
Identificeer momenten die versterkt worden door tekst op scherm:
- **Key quotes** — krachtige uitspraken die blijven hangen
- **Tips & takeaways** — concrete adviezen die de kijker moet onthouden
- **Data points** — getallen, percentages, statistieken
- **Definities** — als een vakterm wordt uitgelegd
- Max 8-10 woorden per overlay, kies het meest impactvolle deel van de zin
- Kies `animation` type: `letter-slide` voor impactvolle quotes, `fade-in` voor rustigere momenten, `word-by-word` voor lijsten

### 3. Feature Bars (STX-FeatureBar)
- Momenten waarop de spreker een opsomming doet ("ten eerste... ten tweede... ten derde...")
- Lijsten van voordelen, stappen, of eigenschappen
- Min 2, max 5 items per feature bar
- Kies een passende emoji-icon per item

### 4. Zoom/Scale effecten
- Emotionele momenten of emphasis (dichter inzoomen)
- Grappige momenten (snelle zoom in)
- "Aha" momenten (langzame zoom)
- Specificeer: `slow-zoom-in`, `quick-zoom`, `zoom-out`

### 5. Transities (SwipeTransition)
- Topic wisselingen in het gesprek
- Overgang van intro naar body content
- Overgang van het ene onderwerp naar het andere
- Kies richting (`left`, `right`, `up`) en kleur die bij de sfeer past

### 6. Sound Effects
- Bij elke text overlay verschijning: subtle `woosh`
- Bij feature bar items: `pop` of `click`
- Bij transities: `swipe`
- Bij emphasis momenten: `riser` of `impact`
- Annoteer alleen — de daadwerkelijke sound files moeten in `public/sound-effects/` staan

## Stap 2: Output — Overlay Plan Tabel

Presenteer het plan als een geordende tabel:

```
# 🎬 Video Overlay Plan: [video titel/onderwerp]

Totale duur: [duur]
Aantal overlays: [X]

| # | Timestamp | Type | Inhoud | Duur | Effect | Notities |
|---|-----------|------|--------|------|--------|----------|
| 1 | 0:05 | Lower Third | Robin Rutten — Head of Marketing | 5s | slide-in-left | Eerste keer spreker |
| 2 | 0:12 | Text Overlay | "Quality starts with the right material" | 3s | letter-slide | Key quote |
| 3 | 0:30 | Transition | — | 0.3s | swipe-left (magenta) | Topic wissel |
| 4 | 0:45 | Feature Bar | 🎈 9 finishes · 🌿 FSC · 🎨 160+ colors | 8s | slide-right + bounce | Opsomming |
| 5 | 1:15 | Zoom | — | 2s | slow-zoom-in | Emotioneel moment |
| 6 | 1:20 | Sound Effect | woosh | 0.3s | — | Bij overlay #7 |
```

Na de tabel, vraag:
> "Review het plan en pas aan waar nodig. Zeg **voer uit** als je tevreden bent, dan schrijf ik de Remotion composition."

## Stap 3: Uitvoering (na "voer uit")

Wanneer de gebruiker "voer uit" zegt (of iets vergelijkbaars zoals "go", "doe het", "execute"):

### 3a. Genereer de Remotion composition

Maak een nieuw bestand `remotion-stx/src/overlays/[video-naam]-overlays.tsx` met:

```tsx
import { AbsoluteFill, Sequence, Video, staticFile } from "remotion";
import { STXLowerThird } from "../STX-LowerThird";
import { STXTextOverlay } from "../STX-TextOverlay";
import { STXFeatureBar } from "../STX-FeatureBar";
import { SwipeTransition } from "../effects/SwipeTransition";
// ... andere imports

export const [VideoNaam]Overlays: React.FC<{ videoSrc: string }> = ({ videoSrc }) => {
  return (
    <AbsoluteFill>
      {/* Base video */}
      <Video src={staticFile(videoSrc)} />

      {/* Overlays op basis van het goedgekeurde plan */}
      <Sequence from={[timestamp_in_frames]} durationInFrames={[duur_in_frames]}>
        {/* Component met juiste props */}
      </Sequence>

      {/* ... alle overlays */}
    </AbsoluteFill>
  );
};
```

**Timestamp conversie:** Zet timestamps om naar frames via `seconds * 30` (bij 30fps).

### 3b. Registreer in Root.tsx

Voeg een nieuwe `<Composition>` toe in `remotion-stx/src/Root.tsx` met:
- `id`: `[VideoNaam]-Overlays`
- `durationInFrames`: totale video duur in frames
- `fps`: 30
- `width`/`height`: 1920x1080
- `defaultProps`: `{ videoSrc: "pad-naar-video.mp4" }`

### 3c. Bevestig aan de gebruiker

Na het schrijven van de code:
1. Run `npx tsc --noEmit` om te checken dat alles compileert
2. Geef de gebruiker:
   - Pad naar het gegenereerde bestand
   - Instructie om de raw video in `public/` te plaatsen
   - Command om te previewen: `cd remotion-stx && npm run dev`
   - Command om te renderen: `npx remotion render [VideoNaam]-Overlays out/[video-naam]-overlays.mp4`

## Regels
- Niet te veel overlays — max 1 per 15-20 seconden gemiddeld, tenzij de content het vereist
- Lower thirds altijd bij de EERSTE keer dat iemand spreekt, niet bij elke keer
- Text overlays: alleen de meest impactvolle quotes, niet elke zin
- Feature bars: alleen bij echte opsommingen (3+ items)
- Zooms: spaarzaam gebruiken voor maximaal effect
- Transities: alleen bij duidelijke topic wisselingen
- Alle tekst in het Engels (tenzij het transcript in een andere taal is en de gebruiker dat wil behouden)
- **UK spelling, altijd.** Colour, favourite, realise, organise, centre, behaviour, catalogue. Nooit US spelling. Volledige regels in `Kennis/Brand/tone-of-voice.md`.
- Gebruik altijd Sempertex brand kleuren en fonts via de BRAND config
