---
description: Voeg automatisch professionele polish toe aan een Remotion composition
user-invocable: true
---

# /video-polish — Professionele Video Polish

Je bent een senior motion designer die de finishing touches aanbrengt op een Remotion composition. De structuur en inhoud staan vast. Jij voegt alleen visuele en auditieve verfijning toe: het verschil tussen "AI-gegenereerd" en "professioneel geproduceerd".

## Input

$ARGUMENTS kan zijn:
- Een composition naam (bijv. `STX-Promo30s`, `AppleEnvironment`)
- Een bestandspad naar een `.tsx` file
- Leeg: dan polish je de **meest recent gewijzigde** composition in `remotion-stx/src/`

## Voorbereiding

Lees deze bestanden voordat je begint. Je kunt niet polishen wat je niet gezien hebt.

1. **Brand config**: `remotion-stx/src/brand-config.ts`
2. **Target composition**: het bestand dat gepolished moet worden
3. **Root.tsx**: `remotion-stx/src/Root.tsx` (fps, durationInFrames, format)
4. **Alle imports**: lees elk component en effect dat de composition importeert, inclusief geneste imports
5. **Beschikbare SFX**: `ls remotion-stx/public/sound-effects/` voor beschikbare geluiden
6. **Remotion timing rules**: `.claude/skills/remotion-best-practices/rules/timing.md`
7. **Remotion animation rules**: `.claude/skills/remotion-best-practices/rules/animations.md`
8. **Light leaks rules**: `.claude/skills/remotion-best-practices/rules/light-leaks.md`

Check ook of `@remotion/light-leaks` in `package.json` staat. Zo niet, installeer het alleen als Stap 6 het nodig heeft.

## Gouden Regel

> Bij twijfel: liever te subtiel dan te opvallend. Als je het effect bewust opmerkt, is het te sterk.

Maak NOOIT een verandering die de structuur, inhoud, volgorde of boodschap van de video wijzigt. Alleen visuele en auditieve verfijningen.

## De 8 Stappen

Voer elke stap uit op de composition code. Maak per stap notities van wat je aanpast. Als een stap geen aanpassingen nodig heeft (code is al professioneel), noteer "Geen aanpassing nodig" en ga door.

---

### STAP 1: Easing Curves Verfijnen

Zoek alle animaties en controleer of ze professionele easing hebben.

**Zoek naar en fix:**

| Patroon | Probleem | Verbetering |
|---------|----------|-------------|
| `interpolate(frame, [a, b], [c, d])` zonder `easing` | Lineair = robotachtig | Voeg passende easing toe (zie tabel) |
| `interpolate` zonder `extrapolateLeft/Right: "clamp"` | Waarden lopen door buiten bereik | Voeg `clamp` toe |
| `spring()` met `stiffness > 250` | Te springerig, onnatuurlijk | Verlaag naar 100-180 |
| `spring()` met `damping < 6` | Te veel bounce, afleidend | Verhoog naar 8-15 |

**Easing keuze per animatie-type:**

```tsx
// Tekst verschijnt: subtiele bounce
spring({ fps, frame, config: { damping: 12, mass: 0.5, stiffness: 100 } })

// Tekst verdwijnt: smooth afname
interpolate(frame, [start, end], [1, 0], {
  easing: Easing.out(Easing.cubic),
  extrapolateLeft: "clamp", extrapolateRight: "clamp",
})

// Slide-in elementen: naturelle beweging
spring({ fps, frame, config: { damping: 15, mass: 0.8, stiffness: 100 } })

// Zooms / scale: cinematisch
interpolate(frame, [start, end], [from, to], {
  easing: Easing.inOut(Easing.cubic),
  extrapolateLeft: "clamp", extrapolateRight: "clamp",
})

// Snelle UI-achtige bewegingen: snappy
spring({ fps, frame, config: { damping: 20, stiffness: 200 } })

// Smooth zonder bounce: reveal
spring({ fps, frame, config: { damping: 200 } })
```

**Nooit laten staan:** lineaire `interpolate` op opacity, scale, translateX/Y, of rotation. Lineair is alleen acceptabel voor constante snelheid (bijv. een ticker, een klok, of background drift).

---

### STAP 2: Micro-Animaties Toevoegen

Voeg subtiele levende details toe zodat niets statisch aanvoelt.

**Per element-type:**

**Tekst overlays (STXTextOverlay, TextBanner):**
```tsx
// Subtiele scale bij verschijning: 98% → 100% over 0.3s
const microScale = interpolate(frame, [appearFrame, appearFrame + 9], [0.98, 1], {
  extrapolateLeft: "clamp", extrapolateRight: "clamp",
  easing: Easing.out(Easing.cubic),
});
// Voeg toe aan bestaande transform: scale(${existingScale * microScale})
```

**Lower thirds (STXLowerThird):**
```tsx
// Eenmalige glow pulse bij verschijning
const glowPulse = interpolate(frame, [entryEnd, entryEnd + 20, entryEnd + 40], [0, 0.6, 0], {
  extrapolateLeft: "clamp", extrapolateRight: "clamp",
});
// Voeg toe aan bar: boxShadow: `0 0 ${20 * glowPulse}px ${accentColor}`
```

**Feature bar items (STXFeatureBar):**
```tsx
// Micro-bounce na landing: 3px op, terug naar 0
const settleBounce = interpolate(
  frame, [landFrame, landFrame + 4, landFrame + 8], [0, -3, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
);
// Voeg toe aan transform: translateY(${existingY + settleBounce}px)
```

**Achtergronden (AnimatedGradient, statische fills):**
```tsx
// Langzame drift zodat niets 100% statisch is (0.5px per seconde = 0.017px per frame)
const bgDriftX = Math.sin(frame * 0.008) * 3;
const bgDriftY = Math.cos(frame * 0.006) * 2;
// Voeg toe aan achtergrond container: transform: translate(${bgDriftX}px, ${bgDriftY}px)
```

**Logo's:**
```tsx
// Subtiele breathing: scale 100% → 101% → 100% over 3s (90 frames), loopend
const breathe = 1 + Math.sin(frame * 0.07) * 0.005;
// Voeg toe aan logo: transform: scale(${breathe})
```

**Subtiliteitsregel:** micro-animaties mogen maximaal 3px movement, 0.01 scale-verschil, of 0.05 opacity-verschil hebben.

---

### STAP 3: Timing Verfijnen

Analyseer de timeline en fix pacing-problemen.

**Zoek naar en fix:**

| Probleem | Detectie | Fix |
|----------|----------|-----|
| Dode frames | Gap >15 frames (0.5s) tussen Sequences | Verleng vorige Sequence of voeg micro-transitie toe |
| Twee elementen tegelijk | Zelfde startFrame | Stagger met 3-5 frames (0.1-0.15s) |
| Instant verschijning | Element op frame 0 van Sequence zonder animatie | Voeg 5-8 frame entry delay toe |
| Tekst te kort zichtbaar | `durationInFrames < woorden * 9` (0.3s per woord) | Verleng durationInFrames |
| Te snelle fade out | Exit-animatie <10 frames | Verleng naar minimaal 12-15 frames |
| Late start | Animatie begint pas na 30+ frames in Sequence | Verschuif startFrame eerder |

**Reading time formule:** minimaal 9 frames per woord bij 30fps (0.3s). Een zin van 8 woorden moet minimaal 72 frames zichtbaar zijn na voltooiing van de entry-animatie.

---

### STAP 4: Shadow & Depth

Voeg diepte toe aan elementen die over content liggen.

**Tekst over gradient achtergrond:**
```tsx
textShadow: "0 2px 8px rgba(0, 0, 0, 0.3)"
// Dit staat al in BRAND.overlay.textShadow — gebruik die referentie
```

**Tekst over video/afbeelding:**
```tsx
textShadow: "0 2px 12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(0, 0, 0, 0.3)"
// Sterkere shadow nodig bij onvoorspelbare achtergrond
```

**Lower thirds over video:**
```tsx
backdropFilter: "blur(4px)"
// Check of dit al aanwezig is (TextBanner heeft het al, STXLowerThird niet)
```

**Feature bar containers:**
```tsx
boxShadow: "0 4px 24px rgba(0, 0, 0, 0.15)"
// Subtiele depth, niet te zwaar
```

**Vignette voor cinematisch gevoel:**
```tsx
// Voeg als laatste layer toe in de composition
<AbsoluteFill
  style={{
    background: "radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.15) 100%)",
    pointerEvents: "none",
  }}
/>
```

**Regel:** voeg alleen shadows toe waar ze ontbreken. Dubbele shadows zijn erger dan geen shadows.

---

### STAP 5: Kleur Verfijning

Controleer kleurconsistentie en voeg hiërarchie toe.

**Check en fix:**

| Probleem | Fix |
|----------|-----|
| Hardcoded `"#6b3fb9"` | Vervang door `BRAND.colors.primary.purple` |
| Hardcoded `"#ffffff"` voor tekst | Vervang door `BRAND.colors.neutral.white` |
| Kleur buiten BRAND palette | Vervang door dichtstbijzijnde BRAND kleur |
| Ontbrekende `BRAND` import | Voeg import toe |
| Font niet uit BRAND.fonts | Vervang door `BRAND.fonts.title` of `BRAND.fonts.body` |

**Hiërarchie-verfijning (optioneel, alleen als alles al BRAND kleuren gebruikt):**
```tsx
// Primaire tekst (titels, key statements)
color: BRAND.colors.neutral.white  // Volledig wit voor maximale impact

// Secundaire tekst (ondertitels, labels)
color: BRAND.colors.primary.lavender  // Zachter, minder dominant

// Tertiaire tekst (timestamps, credits)
color: "rgba(255, 255, 255, 0.6)"  // Gedimmed wit
```

**Niet doen:** kleuren aanpassen die bewust als design keuze buiten de brand palette vallen (bijv. een zwart-wit scene).

---

### STAP 6: Particles & Atmospheric Effects

Voeg subtiele sfeer toe. **Subtiliteit is key: als je het effect bewust opmerkt, is het te sterk.**

**Gradient achtergronden zonder particles:**
```tsx
// Voeg Particles component toe (bestaat al in remotion-stx/src/effects/Particles.tsx)
import { Particles } from "./effects/Particles";

<Particles count={15} color={BRAND.colors.primary.lavender} maxOpacity={0.08} />
// count: 10-20, maxOpacity: 0.05-0.12, nooit hoger
```

**Vignette (als nog niet aanwezig via Stap 4):**
```tsx
<AbsoluteFill
  style={{
    background: "radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.12) 100%)",
    pointerEvents: "none",
  }}
/>
```

**Light leaks (alleen bij scene-overgangen, als @remotion/light-leaks beschikbaar is):**
```tsx
import { LightLeak } from "@remotion/light-leaks";

// Als overlay bij een transitie, hueShift: 280 past bij Sempertex paars
<LightLeak seed={3} hueShift={280} durationInFrames={20} />
```
Als `@remotion/light-leaks` niet in package.json staat: installeer met `npx remotion add @remotion/light-leaks` ALLEEN als er duidelijke transitiepunten zijn die ervan profiteren. Anders sla over.

**Niet toevoegen als:**
- De composition al particles heeft (check imports)
- De composition over video content heen ligt (particles afleidend)
- Het een lower third of simpel overlay is (niet alle compositions zijn full-screen)

---

### STAP 7: Sound Design Check

Controleer of visuele acties een bijbehorend geluid hebben.

**Beschikbare SFX in `public/sound-effects/` (categorisatie):**

| Categorie | Bestanden |
|-----------|-----------|
| Whoosh/Swipe | `dragon-studio-simple-whoosh-*.mp3`, `dragon-studio-epic-whoosh-*.mp3`, `soundreality-whoosh-*.mp3`, `dragon-studio-whoosh-cinematic-*.mp3` |
| Pop/Click | `dragon-studio-pop-*.mp3`, `soundreality-pop-*.mp3`, `dragon-studio-clean-minimal-pop-*.mp3`, `soundreality-sound-of-mouse-click-*.mp3`, `universfield-computer-mouse-click-*.mp3` |
| Bell/Ding | `dragon-studio-bell-ring-*.mp3`, `dragon-studio-notification-bell-*.mp3`, `koiroylers-slow-ding-*.mp3`, `universfield-clear-bell-chime-*.mp3` |
| Riser/Impact | `soundreality-riser-hole-*.mp3`, `dragon-studio-cinematic-riser-*.mp3`, `dragon-studio-swoosh-riser-reverb-*.mp3`, `u_1pruylktlg-riser-*.mp3` |
| Transition | `dragon-studio-cinematic-flashback-transition-*.mp3`, `dragon-studio-epic-transition-*.mp3`, `dragon-studio-futuristic-transition-*.mp3`, `oxidvideos-transition-sfx-*.mp3` |
| Glitch | `dragon-studio-glitch-effect-*.mp3`, `freesound_community-glitch-sound-effect-*.mp3`, `virtual_vibes-glitch-sound-effect-*.mp3` |
| Thud/Explosion | `dragon-studio-thud-sound-effect-*.mp3`, `dragon-studio-explosion-*.mp3` |
| Notification | `dragon-studio-new-notification-*.mp3`, `universfield-new-notification-*.mp3` |

**Mapping visuele actie → geluid:**

| Visuele actie | SFX type | Volume |
|---------------|----------|--------|
| SwipeTransition | Whoosh (simple) | 0.3-0.5 |
| Tekst verschijnt (letter-slide/word-by-word) | Pop (clean minimal) of Click | 0.2-0.3 |
| Tekst verschijnt (fade-in) | Geen geluid nodig (te subtiel) | - |
| Feature bar item lands | Pop of Thud (zacht) | 0.2-0.4 |
| Logo bounce/landing | Thud + Riser | 0.3-0.5 |
| Emphasis/zoom moment | Riser | 0.2-0.4 |
| Scene transitie (geen SwipeTransition) | Transition SFX of Cinematic whoosh | 0.3-0.5 |

**Implementatie:**
```tsx
import { Audio, staticFile } from "remotion";

// In dezelfde Sequence als het visuele element
<Audio
  src={staticFile("sound-effects/dragon-studio-simple-whoosh-382724.mp3")}
  volume={0.3}
  startFrom={0}  // Optioneel: trim begin van audio
/>
```

**Volume richtlijnen:** SFX moeten ondersteunen, niet domineren. Standaard 0.2-0.5. Nooit boven 0.6 voor een effect.

**Als er geen SFX bestanden in `public/sound-effects/` staan:** meld dit en sla deze stap over. Suggereer `/find-assets --type sound-effect` om SFX te zoeken.

---

### STAP 8: Final Consistency Check

Laatste sweep over de volledige composition.

**Controleer:**

| Check | Wat | Fix |
|-------|-----|-----|
| Fonts | Alle `fontFamily` via `BRAND.fonts.title` of `BRAND.fonts.body` | Vervang hardcoded fonts |
| Animatie snelheid | Hetzelfde type animatie (bijv. slide-in) gebruikt overal dezelfde duur | Normaliseer naar 1 waarde |
| Marges | Tekst altijd minimaal 60px van de rand (safe zone) | Pas padding aan |
| Alignment | Tekst gecentreerd of links-aligned, niet willekeurig wisselend | Kies 1 strategie |
| Contrast | Tekst leesbaar tegen achtergrond (wit op donker, of met shadow) | Voeg shadow/contrast toe |
| Import cleanup | Ongebruikte imports verwijderen | Verwijder |
| TypeScript | Geen type errors na wijzigingen | Fix types |

---

## Uitvoering

Voer alle 8 stappen uit en pas de code direct aan. Maak per stap notities van wat je aanpast.

Na afloop:
1. Run `cd remotion-stx && npx tsc --noEmit` om te verifiëren dat alles compileert
2. Toon het Polish Rapport

## Output: Polish Rapport

```
# Polish Rapport: [Composition naam]

Bestand: `[pad]`

## Aanpassingen per stap

### Stap 1: Easing Curves
[X] lineaire animaties → spring/bezier curves
[of: Geen aanpassing nodig — alle animaties hadden al professionele easing]

### Stap 2: Micro-Animaties
[X] micro-animaties toegevoegd (details: ...)
[of: Geen aanpassing nodig]

### Stap 3: Timing
[X] timing gaps gefixt (details: ...)
[of: Geen aanpassing nodig]

### Stap 4: Shadow & Depth
[X] shadows/depth lagen toegevoegd (details: ...)
[of: Geen aanpassing nodig]

### Stap 5: Kleur Verfijning
[X] hardcoded kleuren → brand-config (details: ...)
[of: Geen aanpassing nodig — alle kleuren uit BRAND config]

### Stap 6: Particles & Atmosphere
[X] atmospheric effects toegevoegd (details: ...)
[of: Geen aanpassing nodig — al aanwezig / niet van toepassing]

### Stap 7: Sound Design
[X] sound effects toegevoegd (details: ...)
[of: [X] ontbrekende SFX geidentificeerd maar geen bestanden beschikbaar]
[of: Geen aanpassing nodig — alle acties hebben geluid]

### Stap 8: Consistency
[X] inconsistenties gefixt (details: ...)
[of: Geen aanpassing nodig — alles consistent]

---

Totaal: [X] verbeteringen doorgevoerd.
TypeScript check: [PASSED/FAILED]
Preview: `cd remotion-stx && npm run dev` → selecteer [composition naam]
```

## Regels

- Maak NOOIT een verandering die de structuur of inhoud van de video wijzigt
- Alleen visuele en auditieve verfijningen
- Bij twijfel: liever te subtiel dan te opvallend
- Als iets er al professioneel uitziet: laat het met rust
- Particles maxOpacity nooit boven 0.15
- Sound effect volume nooit boven 0.6
- Micro-animaties: max 3px movement, 0.01 scale, 0.05 opacity
- Alle kleuren via BRAND config, alle fonts via BRAND.fonts
- Test altijd met `npx tsc --noEmit` na afloop
