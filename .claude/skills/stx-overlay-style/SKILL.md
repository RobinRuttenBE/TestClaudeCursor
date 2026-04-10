---
name: stx-overlay-style
description: Stijlreferentie voor alle Sempertex Europe video overlays. Bevat exacte kleuren, fonts, animaties, timing en code-patronen. Standaard bij elk nieuw overlay moment.
type: skill
---

# SKILL: STX Overlay Style Reference

Referentiebestand voor de visuele stijl van Remotion video overlays bij Sempertex Europe.
Gebaseerd op de goedgekeurde stijl uit `remotion-stx/src/overlays/denise-overlays.tsx`.

**Gebruik dit als standaard bij elk nieuw overlay moment, tenzij de gebruiker expliciet iets anders aangeeft.**

---

## 1. ALGEMENE STIJL

### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Panel slide in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Video shift in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Wipe reveal bar recede | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Accent line expand | out cubic | `Easing.out(Easing.cubic)` |
| Titel verschijning | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |

### Animatie Snelheden (bij 30fps)

| Animatie | Frames | Seconden |
|----------|--------|----------|
| Panel slide in/uit | 14 | ~0.47s |
| Video shift in/uit | 14 | ~0.47s |
| Wipe bar verschijning | 4 | ~0.13s |
| Wipe bar recede | 28 | ~0.93s |
| Accent line expand | 20 | ~0.67s |
| Titel spring settle | ~18 | ~0.6s |

### Schaduwen & Glow

| Element | Waarde |
|---------|--------|
| Panel rechterrand | `linear-gradient(to right, rgba(0,0,0,0.12), transparent)` op een 30px brede div rechts van het panel |
| Wipe bar glow (tijdens recede) | `boxShadow: 0 0 16px ${barColor}80` |
| Wipe bar glow (statisch) | geen |

### Subtiele Shake (continu)

Twee overlappende sin/cos golven op de content container. Nauwelijks zichtbaar, geeft constant leven.

```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
// Toegepast als: transform: translate(${shakeX}px, ${shakeY}px)
```

Amplitude: ~1.5px horizontaal, ~1px verticaal. Onzichtbaar bij stilstaand beeld, voelbaar bij afspelen.

### Standaard Margins & Padding

| Element | Waarde |
|---------|--------|
| Panel content padding | `100px 50px 100px 60px` (top right bottom left) |
| Tussen titel en lijst | `marginTop: 40` op lijst container |
| Titel accent line | `marginTop: 16` |
| Groot item (product code) | `marginBottom: 8` (kort, want sub-item volgt) |
| Klein item (kleur detail) | `marginBottom: 28` (meer ruimte voor scheiding) |
| Titel achtergrondblok | `padding: 8px 28px` |

---

## 2. KLEUREN

Alle kleuren komen uit `BRAND` in `remotion-stx/src/brand-config.ts`.

### Overlay Kleurgebruik

| Element | Kleur | BRAND referentie | HEX |
|---------|-------|-----------------|-----|
| Titel tekst | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Titel achtergrondblok | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Accent line | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Wipe bar (even items: 0, 2) | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Wipe bar (oneven items: 1, 3) | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Groot item tekst (product code) | Black | `BRAND.colors.neutral.black` | #000000 |
| Klein item tekst (detail) | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Panel achtergrond basis | Lavender | `BRAND.colors.primary.lavender` | #f1d9ff |
| Particles | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |

---

## 3. ACHTERGROND STIJL

### Layout: Side Panel

Het overlay is GEEN fullscreen. Het is een panel aan de linkerkant van het scherm.

```
Panel breedte: 680px (~35% van 1920px)
Video shift: 180px naar rechts
Video scale: 1.08x (voorkomt zwarte randen)
```

De video schuift naar rechts om ruimte te maken. De spreker (in het midden) blijft zichtbaar rechts.

### Frosted Glass Layer

Eerste laag op het panel. Blurt de verschoven video die achter het panel zichtbaar is.

```tsx
backdropFilter: "blur(50px) brightness(1.1) saturate(1.2)",
WebkitBackdropFilter: "blur(50px) brightness(1.1) saturate(1.2)",
```

Constante waarden, geen animatie (panel is off-screen wanneer niet zichtbaar).

### Gradient Overlay

Drie lagen over de frosted glass:

```tsx
background: `
  radial-gradient(
    ellipse at 20% 20%,
    rgba(107, 63, 185, 0.25) 0%,      // Purple glow linksboven
    transparent 60%
  ),
  radial-gradient(
    ellipse at 50% 90%,
    rgba(205, 11, 92, 0.15) 0%,        // Magenta glow linksonder
    transparent 50%
  ),
  linear-gradient(
    180deg,
    ${BRAND.colors.primary.lavender}d0 0%,    // Lavender 81% opacity
    ${BRAND.colors.primary.lavender}e8 50%,   // Lavender 91% opacity
    ${BRAND.colors.neutral.white}d0 100%      // Wit 81% opacity
  )
`
```

### Soft Shadow (rechterrand panel)

Aparte div rechts van het panel voor zachte overgang naar video:

```tsx
{
  position: "absolute",
  top: 0,
  right: -30,
  width: 30,
  height: "100%",
  background: "linear-gradient(to right, rgba(0,0,0,0.12), transparent)",
  pointerEvents: "none",
}
```

### Particles

Contained binnen het panel (overflow hidden wrapper).

```tsx
<Particles
  count={20}
  color={BRAND.colors.primary.purple}   // #6b3fb9
  maxOpacity={0.2}
  seed={77}
  speedMultiplier={2.5}
/>
```

Particle component: `remotion-stx/src/effects/Particles.tsx`

---

## 4. TITEL STIJL

### Font & Kleur

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 96
fontWeight: 800  // ExtraBold
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 5
```

### Geel Achtergrondblok

De titel staat in een inline-block element met gele achtergrond:

```tsx
<div style={{ display: "inline-block", backgroundColor: BRAND.colors.secondary.yellow, padding: "8px 28px" }}>
  <div style={{ fontFamily, fontSize, fontWeight, color, letterSpacing }}>
    TITEL TEKST
  </div>
</div>
```

### Accent Line Onder Titel

Expandeert van 0% naar 100% breedte (max 300px), vanuit links. Geel.

```tsx
// Timing: start na FADE_DURATION + 8 frames
// Duur: 20 frames
// Easing: Easing.out(Easing.cubic)
// Kleur: BRAND.colors.secondary.yellow
// Hoogte: 3px
// marginTop: 16px
```

### Titel Entrance Animatie

Spring animatie met fade in:

```tsx
const titleSpring = spring({
  frame: frame - FADE_DURATION,  // Start na panel is ingeschoven
  fps,
  config: { damping: 14, mass: 0.5, stiffness: 120 },
});
const titleY = interpolate(titleSpring, [0, 1], [-30, 0]);    // Slide van boven
const titleOpacity = interpolate(titleSpring, [0, 0.5], [0, 1], {
  extrapolateRight: "clamp",
});
```

### Font Loading

Fonts worden geladen via FontFace API met delayRender/continueRender:

```tsx
new FontFace("Rethink Sans", `url('${staticFile("fonts/RethinkSans-ExtraBold.ttf")}')`, { weight: "800" })
new FontFace("Rethink Sans", `url('${staticFile("fonts/RethinkSans-BoldItalic.ttf")}')`, { weight: "700", style: "italic" })
```

---

## 5. LIJST/TEKST ONTHULLING STIJL

### Twee Tekstgroottes (hierarchie)

| Type | fontSize | fontWeight | fontStyle | Kleur | Prefix | Voorbeeld |
|------|----------|------------|-----------|-------|--------|-----------|
| `large` | 72 | 800 (ExtraBold) | italic | black (#000) | geen | LOL12, R5 |
| `small` | 34 | 700 (Bold) | italic | purple (#6b3fb9) | bullet (U+2022) | Pastel Matte Pink |

Beide types gebruiken `fontFamily: "Rethink Sans, sans-serif"`.

### Wipe Reveal Mechanisme

De onthulling werkt in twee fasen:

**Fase 1: Bar verschijnt (4 frames)**
Volle breedte gekleurde bar verschijnt over de tekst.

```tsx
const barAppear = interpolate(
  frame, [startFrame, startFrame + 4], [0, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
```

**Fase 2: Bar recede (28 frames)**
Bar krimpt van links naar rechts. Tekst wordt onthuld achter de linkerrand van de bar. Een 4% accent bar blijft over aan het einde.

```tsx
const recedeProgress = interpolate(
  frame,
  [startFrame + 4, startFrame + 4 + 28],
  [0, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);

const textRevealPercent = recedeProgress * 100;
const textClipRight = 100 - textRevealPercent;   // clipPath: inset(0 ${textClipRight}% 0 0)

const ACCENT_WIDTH = 4;  // percentage dat overblijft
const barLeftEdge = recedeProgress * (100 - ACCENT_WIDTH);
const barWidthPercent = 100 - barLeftEdge;
```

**Glow tijdens recede:**
```tsx
boxShadow: isReceding ? `0 0 16px ${barColor}80` : "none"
```

### Bar Kleuren (alterneren)

```tsx
barColor={i % 2 === 0 ? BRAND.colors.secondary.yellow : BRAND.colors.primary.purple}
```

Even items (0, 2) = geel, oneven items (1, 3) = paars.

### Stagger Timing

Items verschijnen op specifieke relatieve frames binnen de overlay Sequence. De timing wordt bepaald door het videomoment waarop het item relevant is.

Typische spacing: 30-60 frames (1-2s) tussen items, afhankelijk van de spreker.

---

## 6. TRANSITIE STIJL

### Panel Slide (IN en UIT)

Geen fade/opacity. Het panel schuift als geheel van links het scherm in, en weer uit.

```tsx
const panelSlideX = interpolate(
  frame,
  [0, FADE_DURATION, OVERLAY_DURATION - FADE_DURATION, OVERLAY_DURATION],
  [-PANEL_WIDTH, 0, 0, -PANEL_WIDTH],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);
// Toegepast als: transform: translateX(${panelSlideX}px)
```

### Video Shift (synced met panel)

Video schuift naar rechts om ruimte te maken. Zelfde timing en easing als panel slide.

```tsx
// In de parent composition (absolute frames):
const videoShiftX = interpolate(
  frame,
  [OVERLAY_START, OVERLAY_START + FADE_DURATION,
   OVERLAY_START + OVERLAY_DURATION - FADE_DURATION, OVERLAY_START + OVERLAY_DURATION],
  [0, VIDEO_SHIFT, VIDEO_SHIFT, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);

const videoScale = interpolate(
  frame,
  [OVERLAY_START, OVERLAY_START + FADE_DURATION,
   OVERLAY_START + OVERLAY_DURATION - FADE_DURATION, OVERLAY_START + OVERLAY_DURATION],
  [1, 1.08, 1.08, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);
// Toegepast als: transform: translateX(${videoShiftX}px) scale(${videoScale})
// transformOrigin: "center center"
```

### Timing Constanten

```tsx
const FADE_DURATION = 14;       // Slide in/uit duur in frames (~0.47s)
const PANEL_WIDTH = 680;        // Panel breedte in px
const VIDEO_SHIFT = 180;        // Video verschuiving in px
```

---

## 7. SOUND DESIGN STIJL

Momenteel zijn er GEEN geluidseffecten actief (bewust verwijderd op verzoek).

Als geluiden in de toekomst gewenst zijn, gebruik dan deze richtlijnen:

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Panel slide in | Soft whoosh | 0.5 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` |
| Wipe reveal per regel | Subtle pop | 0.3 | `sound-effects/dragon-studio-clean-minimal-pop-467466.mp3` |
| Panel slide uit | Soft whoosh | 0.5 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` |

Geluiden plaatsen als `<Audio>` in `<Sequence>` elementen in de parent composition (niet in het panel component), zodat ze niet afgekapt worden door de overlay Sequence duur.

---

## 8. COMPOSITIE STRUCTUUR

### Bestandsstructuur

```
remotion-stx/src/overlays/denise-overlays.tsx   // Hoofd-compositie
remotion-stx/src/effects/Particles.tsx           // Particle effect (speedMultiplier prop)
remotion-stx/src/effects/CameraBurn.tsx          // NIET MEER GEBRUIKT (legacy)
remotion-stx/src/brand-config.ts                 // Kleuren, fonts, animatie defaults
```

### Component Hierarchie

```
DeniseOverlays (parent, registered in Root.tsx)
  |- FontLoader (laadt custom fonts via FontFace API)
  |- AbsoluteFill
      |- Video (met translateX + scale animatie)
      |- Sequence (overlay timing)
          |- MaterialsPanel
              |- Frosted glass div (backdrop-filter)
              |- Gradient overlay div
              |- Right edge shadow div
              |- Particles (in overflow hidden wrapper)
              |- Content div (met shake transform)
                  |- Titel blok (geel achtergrond + dark purple tekst)
                  |- AccentLine
                  |- Items lijst
                      |- WipeRevealLine (per item)
```

---

## OVERLAY TYPES

### TYPE: materialenlijst

**WANNEER:** Spreker somt materialen, ingredienten, gereedschap, of items op

**LAYOUT:** Side panel links (~35% scherm), video schuift naar rechts

**BEVAT:**
- Frosted glass achtergrond met gradient overlay
- Floating particles (paars, snel)
- Subtiele content shake
- Titel in geel blok met dark purple tekst + accent line
- Lijst items met wipe-reveal (full bar -> recede -> accent)
- Twee hierarchie niveaus: groot (product/item naam) en klein (detail/kleur/spec)
- Alternerende bar kleuren (geel/paars)
- Panel slide in/uit synced met video shift

**TRANSITIE:** Panel schuift van links, video schuift naar rechts (geen fade)

**REFERENTIE:** `remotion-stx/src/overlays/denise-overlays.tsx` (MaterialsPanel component)

**REGISTRATIE:** Composition `Denise-Overlays` in `remotion-stx/src/Root.tsx`

---

### TYPE: tip-overlay

**WANNEER:** Spreker geeft een tip, advies, best practice, of product-specifieke aanbeveling

**LAYOUT:** Linksonder het scherm (~30% breedte, ~30% hoogte). Positie: `bottom: 10%, left: 5%`. Video blijft ongewijzigd (geen shift). Denise/spreker volledig zichtbaar.

**STRUCTUUR:** Horizontaal blok van drie aaneengesloten secties:

```
[ Product foto ] [ Tekstvak ] [ Logo ]
```

**BEVAT:**

#### Foto-sectie (links)
- Achtergrond: purple (`BRAND.colors.primary.purple` / #6b3fb9)
- Ronde productfoto (130x130px) met gele border (`4px solid BRAND.colors.secondary.yellow`)
- Gele accent lijn boven foto (60% breedte, links uitgelijnd, `alignSelf: "flex-start"`)
- Gele accent lijn onder foto (60% breedte, rechts uitgelijnd, `alignSelf: "flex-end"`)
- Breedte sectie: 170px, padding: `12px 16px`

#### Tekstvak (midden)
- Achtergrond: lavender (`BRAND.colors.primary.lavender` / #f1d9ff)
- Padding: `24px 28px`, maxWidth: 420px
- **Titel:** Rethink Sans Bold 36px, dark purple (`BRAND.colors.secondary.darkPurple`), lineHeight 1.2
- **Underline:** 4px hoog, paars (`BRAND.colors.primary.purple`), full width, marginBottom 12px
- **Body:** Rethink Sans Bold 28px, zwart (`BRAND.colors.neutral.black`), lineHeight 1.4

#### Logo-sectie (rechts)
- Achtergrond: wit (`BRAND.colors.neutral.white`)
- Breedte: 130px, padding: `16px 20px`
- Logo via `<Img src={staticFile("logos/Flor logo.png")}` />`, objectFit: contain

#### Blok container
- `borderRadius: 12`, `overflow: "hidden"`
- `transformOrigin: "bottom left"`

#### Animaties

**Pop in (spring bounce):**
```tsx
const popIn = spring({
  frame,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});
// Schaalt van 0 → ~1.12 → 1.0 (natuurlijke overshoot)
```

**Pop out (eased):**
```tsx
const exitScale = interpolate(
  frame,
  [M4_DURATION - 12, M4_DURATION - 12 + 4, M4_DURATION],
  [1, 1.12, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic) },
);
// 12 frames totaal, 4 frames overshoot naar 1.12, dan naar 0
```

**Scale breathe (continu):**
```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.005;
// Amplitude: 0.5%, langzame cyclus. Nauwelijks zichtbaar maar geeft leven.
```

**Pulserende glow (continu):**
```tsx
const glowOpacity = interpolate(Math.sin(frame * 0.06), [-1, 1], [0.15, 0.4]);
const glowShadow = `
  0 8px 32px rgba(0,0,0,0.25),
  0 0 24px rgba(107, 63, 185, ${glowOpacity}),
  0 0 48px rgba(107, 63, 185, ${glowOpacity * 0.5})
`;
// Paarse gloed pulseert rond het hele blok. Vervangt shake effect.
```

**Gecombineerde transform:**
```tsx
transform: `scale(${scale * breathe})`
```

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M4_DURATION | 300 frames (10s) | Totale overlay duur |
| M4_EXIT_FRAMES | 12 frames (~0.4s) | Pop-out duur |
| Spring settle | ~25 frames (~0.8s) | Pop-in tot rust |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Pop in | Soft pop | 0.18 | `sound-effects/soundreality-pop-423717.mp3` |
| Pop out | Camera click | 0.8 | `sound-effects/freesound_community-iphone-camera-capture-6448.mp3` |

Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Foto achtergrond | Purple | #6b3fb9 |
| Foto border | Yellow | #ffdb5a |
| Accent lijnen | Yellow | #ffdb5a |
| Tekstvak achtergrond | Lavender | #f1d9ff |
| Titel tekst | Dark Purple | #1b073d |
| Titel underline | Purple | #6b3fb9 |
| Body tekst | Black | #000000 |
| Logo achtergrond | White | #ffffff |
| Glow kleur | Purple | rgb(107, 63, 185) |

**TRANSITIE:** Scale pop in/out met spring bounce (geen slide, geen fade)

**REFERENTIE:** `remotion-stx/src/overlays/denise-overlays.tsx` (TipOverlay component)

**REGISTRATIE:** Moment 4 in Composition `Denise-Overlays`, Sequence from={1410}

---

### TYPE: step-overlay

**WANNEER:** Spreker begint een stap in een tutorial of proces. Gebruikt om een duidelijke stap-aanduiding te tonen met korte instructie en optionele tip.

**LAYOUT:** Side panel links (50% scherm / 960px), video schuift naar rechts en neemt de andere 50% in. Denise/spreker wordt gecentreerd in de rechterhelft.

```
Panel breedte: 960px (50% van 1920px)
Video shift: 480px naar rechts (centreert spreker in rechterhelft)
Video scale: 1.05x (voorkomt zwarte randen bij grotere shift)
```

**STRUCTUUR:** Verticale layout met drie secties:

```
┌─────────────────────────┐
│                         │
│        STEP 1           │  ← Titel: groot, gecentreerd, bovenaan
│     ━━━━━━━━━━━         │  ← Dikke gele accent line, gecentreerd
│                         │
│  Build the base of      │  ← Subtitle: wipe-reveal
│  your design.           │
│                         │
│  • Tip: When making     │  ← Tip: wipe-reveal, lagere opacity
│  big designs like...    │
│                         │
│      [STX EU logo]      │  ← Logo: gecentreerd, onderaan
│                         │
└─────────────────────────┘
```

**BEVAT:**

#### Achtergrond (lavender, licht)

Frosted glass + lavender gradient. Lichte achtergrond voor donkere tekst (tegenovergestelde van materialenlijst).

**Frosted glass:**
```tsx
backdropFilter: "blur(50px) brightness(1.1) saturate(1.2)",
WebkitBackdropFilter: "blur(50px) brightness(1.1) saturate(1.2)",
```

**Gradient overlay:**
```tsx
background: `
  radial-gradient(
    ellipse at 20% 20%,
    rgba(107, 63, 185, 0.15) 0%,        // Subtiele purple glow linksboven
    transparent 60%
  ),
  radial-gradient(
    ellipse at 50% 90%,
    rgba(205, 11, 92, 0.08) 0%,          // Zeer subtiele magenta glow onder
    transparent 50%
  ),
  linear-gradient(
    180deg,
    ${BRAND.colors.primary.lavender}d0 0%,    // Lavender 81% opacity
    ${BRAND.colors.primary.lavender}e8 50%,   // Lavender 91% opacity
    ${BRAND.colors.neutral.white}d0 100%      // Wit 81% opacity
  )
`
```

Zelfde frosted glass + gradient constructie als materialenlijst, maar met lavender tint (niet donker paars). Radial gradients zijn zachter (0.15 en 0.08 i.p.v. 0.25 en 0.15).

#### Titel

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 192
fontWeight: 800  // ExtraBold
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 8
lineHeight: 1.1
textAlign: "center"
```

Altijd UPPERCASE (bijv. "STEP 1", "STEP 2"). Geen geel achtergrondblok (anders dan materialenlijst). Tekst staat direct op de lavender achtergrond.

**Titel entrance:** Spring animatie met fade + slide van boven:
```tsx
const titleSpring = spring({
  frame: frame - M5_FADE,
  fps,
  config: { damping: 14, mass: 0.5, stiffness: 120 },
});
const titleY = interpolate(titleSpring, [0, 1], [-30, 0]);
const titleOpacity = interpolate(titleSpring, [0, 0.5], [0, 1], {
  extrapolateRight: "clamp",
});
```

#### Gele Accent Line (onder titel)

Dikke gele balk, gecentreerd onder de titel. Expandeert van 0% naar 100% breedte.

```tsx
// Timing: start na M5_FADE + 18 frames, duur 20 frames
// Easing: Easing.out(Easing.cubic)
// maxWidth: 500px
// height: 24px
// borderRadius: 4px
// Kleur: BRAND.colors.secondary.yellow (#ffdb5a)
// Positie: display flex, justifyContent center, marginTop 16px
```

#### Subtitle & Tip tekst

Beide gebruiken het wipe-reveal mechanisme (StepWipeRevealLine), identiek aan de materialenlijst maar met dark purple tekst op lavender achtergrond.

| Element | Font | fontSize | fontWeight | Kleur | Opacity | Bar kleur |
|---------|------|----------|------------|-------|---------|-----------|
| Subtitle | Rethink Sans | 48 | 800 (ExtraBold) | Dark Purple (#1b073d) | 1.0 | Purple (#6b3fb9) |
| Tip | Rethink Sans | 32 | 800 (ExtraBold) | Dark Purple (#1b073d) | 0.7 | Yellow (#ffdb5a) |

Tip tekst begint met bullet point prefix (`\u2022  Tip:`).

**Wipe-reveal stagger timing (relatief binnen overlay Sequence):**

| Element | startFrame | Beschrijving |
|---------|------------|-------------|
| Titel | M5_FADE + 3 (frame 18) | Direct na panel settle |
| Subtitle | M5_FADE + 25 (frame 40) | Na titel zichtbaar |
| Tip | M5_FADE + 40 (frame 55) | Na subtitle zichtbaar |

#### Logo (onderaan)

Sempertex Europe logo, gecentreerd aan de onderkant van het panel.

```tsx
<Img
  src={staticFile("logos/STX EU.png")}
  style={{ height: 100, objectFit: "contain" }}
/>
// Container: display flex, justifyContent center, paddingBottom 20px
```

**Logo fade-in:**
```tsx
const logoOpacity = interpolate(
  frame,
  [M5_FADE + 10, M5_FADE + 25],
  [0, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
```

#### Particles & Shake

Zelfde als materialenlijst, maar met andere seed en iets lagere opacity:

```tsx
<Particles
  count={20}
  color={BRAND.colors.primary.purple}   // #6b3fb9
  maxOpacity={0.15}                      // iets lager dan materialenlijst (0.2)
  seed={55}                              // andere seed voor uniek patroon
  speedMultiplier={2.5}
/>
```

Shake identiek aan materialenlijst:
```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
```

#### Padding

```tsx
padding: "80px 60px 60px 80px"  // top right bottom left
```

Iets krapper dan materialenlijst (80px top i.p.v. 100px) vanwege de grotere titel.

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Panel slide in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Video shift in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Accent line expand | out cubic | `Easing.out(Easing.cubic)` |
| Titel verschijning | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |
| Wipe bar recede | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Logo fade-in | linear | geen easing (simpele opacity interpolatie) |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M5_DURATION | 240 frames (8s) | Totale overlay duur |
| M5_FADE | 15 frames (0.5s) | Slide in/uit duur |
| M5_PANEL_WIDTH | 960px | Panel breedte (50% scherm) |
| M5_VIDEO_SHIFT | 480px | Video verschuiving naar rechts |
| M5_VIDEO_SCALE | 1.05x | Video schaal tijdens shift |
| Accent line expand | 20 frames (~0.67s) | Van 0% naar 100% breedte |
| Logo fade-in | 15 frames (0.5s) | Opacity 0 naar 1 |

#### Sound Design

Geen geluidseffecten. Bewust verwijderd om de tutorial-stap rustig en informatief te houden.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Panel achtergrond | Lavender gradient | #f1d9ff |
| Titel tekst | Dark Purple | #1b073d |
| Subtitle tekst | Dark Purple | #1b073d |
| Tip tekst | Dark Purple (70% opacity) | #1b073d |
| Accent line | Yellow | #ffdb5a |
| Wipe bar (subtitle) | Purple | #6b3fb9 |
| Wipe bar (tip) | Yellow | #ffdb5a |
| Particles | Purple | #6b3fb9 |
| Panel rechterrand schaduw | Zwart 12% opacity | rgba(0,0,0,0.12) |

#### Video Shift (synced met panel)

Grotere shift dan materialenlijst omdat het panel 50% inneemt i.p.v. 35%.

```tsx
// In de parent composition (absolute frames):
const m5ShiftX = interpolate(
  frame,
  [M5_START, M5_START + M5_FADE,
   M5_START + M5_DURATION - M5_FADE, M5_START + M5_DURATION],
  [0, M5_VIDEO_SHIFT, M5_VIDEO_SHIFT, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);

const m5Scale = interpolate(
  frame,
  [M5_START, M5_START + M5_FADE,
   M5_START + M5_DURATION - M5_FADE, M5_START + M5_DURATION],
  [1, M5_VIDEO_SCALE, M5_VIDEO_SCALE, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);
```

Video shifts worden gecombineerd met andere momenten via optelling (shifts overlappen niet):
```tsx
const videoShiftX = m3ShiftX + m5ShiftX;
const videoScale = m3Scale * m5Scale;
```

**TRANSITIE:** Panel schuift van links, video schuift naar rechts (geen fade). Zelfde mechanisme als materialenlijst maar met grotere shift.

**REFERENTIE:** `remotion-stx/src/overlays/denise-overlays.tsx` (StepOverlay + StepWipeRevealLine componenten)

**REGISTRATIE:** Moment 5 in Composition `Denise-Overlays`, Sequence from={2910}

---

### TYPE: info-card

**WANNEER:** Spreker licht een specifiek onderdeel, concept of techniek toe die extra context nodig heeft. Informatieve pop-up met meer tekst dan een tip-overlay, inclusief teleprompter-effect voor langere uitleg.

**LAYOUT:** Floating kaart, NIET fullscreen. Video van spreker blijft volledig zichtbaar op de achtergrond (geen video shift).

```
Positie: left 5%, verticaal gecentreerd (top: 50%, translateY: -50%)
Breedte: 504px (~26% van 1920px)
Hoogte: 454px (~42% van 1080px)
Border-radius: 20px
Overflow: hidden
```

De kaart zweeft over de video. Denise/spreker is rechts volledig zichtbaar.

**STRUCTUUR:** Verticale layout met twee secties:

```
┌─────────────────────────────────┐
│                                 │
│    ┌───────────────────┐        │
│    │     COLUMN        │        │  ← Gele badge, gecentreerd
│    └───────────────────┘        │
│                                 │
│   This part is essential to     │  ← Tekst 1 (verschijnt met kaart)
│   create your structure         │
│                                 │
│          ↕ scroll ↕             │  ← Teleprompter effect na 2s
│                                 │
│   Use four rings in total...    │  ← Tekst 2 (scrollt in van onder)
│                                 │
│          [particles]            │
└─────────────────────────────────┘
```

**BEVAT:**

#### Achtergrond (lavender, licht)

Lavender gradient met subtiele purple glow. Lichter dan de step-overlay gradient.

```tsx
background: `
  radial-gradient(
    ellipse at 30% 30%,
    rgba(107, 63, 185, 0.12) 0%,
    transparent 60%
  ),
  linear-gradient(
    180deg,
    ${BRAND.colors.primary.lavender} 0%,
    ${BRAND.colors.primary.lavender}e0 100%
  )
`
```

#### Particles (kaart achtergrond)

Contained binnen de kaart (overflow hidden + borderRadius 20px). Minder particles dan panel-overlays.

```tsx
<Particles
  count={12}
  color={BRAND.colors.primary.purple}   // #6b3fb9
  maxOpacity={0.12}
  seed={99}
  speedMultiplier={1.5}
/>
```

#### Titel Badge (geel, gecentreerd)

Geel achtergrondblok met rounded corners, gecentreerd in de kaart. Bevat eigen particles.

```tsx
// Badge container
alignSelf: "center"
borderRadius: 12
marginBottom: 24

// Badge achtergrond
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "10px 32px"

// Badge particles
<Particles count={6} color={BRAND.colors.primary.purple} maxOpacity={0.15} seed={42} speedMultiplier={1} />

// Titel tekst
fontFamily: "Rethink Sans, sans-serif"
fontSize: 53
fontWeight: 800  // ExtraBold
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 4
```

Altijd UPPERCASE (bijv. "COLUMN", "TECHNIQUE").

#### Body Tekst (teleprompter scroll)

Twee teksten in een overflow-hidden container. Tekst 1 verschijnt met de kaart. Na 2 seconden start het teleprompter-effect: tekst 1 scrollt omhoog en vervaagt, tekst 2 scrollt van onder in.

**Font:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 30
fontWeight: 700  // Bold
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple  // #1b073d
lineHeight: 1.5
textAlign: "center"
```

**Teleprompter mechanisme:**
```tsx
const scrollProgress = interpolate(
  frame,
  [M7_SCROLL_START, M7_SCROLL_START + M7_SCROLL_DURATION],
  [0, 1],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);

// Tekst 1: scrollt omhoog, vervaagt
const text1Y = interpolate(scrollProgress, [0, 1], [0, -80]);
const text1Opacity = interpolate(scrollProgress, [0, 0.7], [1, 0], {
  extrapolateRight: "clamp",
});

// Tekst 2: scrollt omhoog in beeld
const text2Y = interpolate(scrollProgress, [0, 1], [80, 0]);
const text2Opacity = interpolate(scrollProgress, [0.3, 1], [0, 1], {
  extrapolateLeft: "clamp",
});
```

Beide teksten staan `position: absolute` in dezelfde container. De scroll is smooth (inOut cubic) en leesbaar.

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Pop in | spring | `{ damping: 10, mass: 0.4, stiffness: 160 }` |
| Pop out | in cubic | `Easing.in(Easing.cubic)` |
| Teleprompter scroll | inOut cubic | `Easing.inOut(Easing.cubic)` |

#### Animaties

**Pop in (spring bounce):**
```tsx
const popIn = spring({
  frame,
  fps,
  config: { damping: 10, mass: 0.4, stiffness: 160 },
});
// Schaalt van 0 → ~1.1 → 1.0 (natuurlijke overshoot)
```

**Pop out (eased):**
```tsx
const exitScale = interpolate(
  frame,
  [M7_DURATION - M7_EXIT_FRAMES, M7_DURATION - M7_EXIT_FRAMES + 3, M7_DURATION],
  [1, 1.1, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic) },
);
// 9 frames totaal, 3 frames overshoot naar 1.1, dan naar 0
```

**Scale breathe (continu):**
```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.003;
// Amplitude: 0.3%, langzame cyclus. Nauwelijks zichtbaar maar geeft leven.
```

**Pulserende glow (continu):**
```tsx
const glowOpacity = interpolate(Math.sin(frame * 0.06), [-1, 1], [0.1, 0.3]);
const glowShadow = `0 8px 40px rgba(0,0,0,0.2), 0 0 24px rgba(107, 63, 185, ${glowOpacity})`;
// Paarse gloed pulseert rond de kaart.
```

**Gecombineerde transform:**
```tsx
transform: `translateY(-50%) scale(${scale * breathe})`
transformOrigin: "center center"
```

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M7_DURATION | 240 frames (8s) | Totale overlay duur |
| M7_EXIT_FRAMES | 9 frames (~0.3s) | Pop-out duur |
| M7_SCROLL_START | 60 frames (2s) | Teleprompter start na pop-in |
| M7_SCROLL_DURATION | 60 frames (2s) | Teleprompter transitie duur |
| Spring settle | ~15 frames (~0.5s) | Pop-in tot rust |
| M7_CARD_WIDTH | 504px | Kaart breedte (~26% scherm) |
| M7_CARD_HEIGHT | 454px | Kaart hoogte (~42% scherm) |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Pop in | Pop | 0.2 | `sound-effects/dragon-studio-pop-402324.mp3` |
| Pop out | Clean minimal pop | 0.25 | `sound-effects/dragon-studio-clean-minimal-pop-467466.mp3` |

Geen geluid bij teleprompter scroll. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Kaart achtergrond | Lavender gradient | #f1d9ff |
| Badge achtergrond | Yellow | #ffdb5a |
| Titel tekst | Dark Purple | #1b073d |
| Body tekst | Dark Purple | #1b073d |
| Particles (kaart) | Purple | #6b3fb9 |
| Particles (badge) | Purple | #6b3fb9 |
| Glow kleur | Purple | rgb(107, 63, 185) |
| Schaduw | Zwart 20% | rgba(0,0,0,0.2) |

#### Padding

```tsx
// Kaart content
padding: "30px 32px"

// Badge
padding: "10px 32px"
```

**TRANSITIE:** Scale pop in/out met spring bounce (geen slide, geen fade). Zelfde mechanisme als tip-overlay maar met andere spring config (damping 10 vs 8, stiffness 160 vs 180).

**REFERENTIE:** `remotion-stx/src/overlays/denise-overlays.tsx` (InfoCard component)

**REGISTRATIE:** Moment 7 in Composition `Denise-Overlays`, Sequence from={7440}

---

### TYPE: browser-animation

**WANNEER:** CTA moment waarin de kijker naar een website wordt geleid. Simuleert een browser-ervaring met Google zoeken, navigatie door pagina's, en eindigt bij een registratie/CTA knop.

**LAYOUT:** Fullscreen (1920x1080). Bedekt de hele video. Geen video shift, geen panel.

**STRUCTUUR:** Vier fasen in een gesimuleerde browser window:

```
┌─────────────────────────────────────────────┐
│ ● ● ●  │ sempertexeurope.com               │ ← Browser chrome (48px)
├─────────────────────────────────────────────┤
│                                             │
│   Fase 1: Google homepage + typewriter      │
│   Fase 2: Zoekresultaten screenshot         │
│   Fase 3: Homepage screenshot + zoom        │
│   Fase 4: Workshop pagina + zoom + arrow    │
│                                             │
│                      ↖ cursor               │
└─────────────────────────────────────────────┘
```

**BEVAT:**

#### Browser Chrome (bovenaan)

```tsx
height: 48
backgroundColor: "#e8e8e8"
// Traffic lights: #ff5f57, #febc2e, #28c840 (12px circles)
// Address bar: wit, borderRadius 8, fontSize 14, system-ui font
// URL verandert per fase
```

#### Fase 1: Google Homepage (programmatisch)

Programmatisch gebouwde Google homepage met:
- Google logo tekst (92px, gekleurde letters)
- Zoekbalk (55% breed, borderRadius 28, boxShadow)
- Typewriter effect: letters verschijnen 1 voor 1 met blinkende cursor

```tsx
const charsPerFrame = SEARCH_TEXT.length / 50; // ~1.7s om te typen
const typedChars = Math.floor((frame - typeStartFrame) * charsPerFrame);
```

#### Fase 2-4: Screenshots

Screenshots worden geladen via `<Img src={staticFile(...)} />` met `objectFit: "cover"`.

| Fase | Screenshot | Zoom | Zoom origin |
|------|-----------|------|-------------|
| 2 | google-search-result-page.png | geen | - |
| 3 | stx-homepage.png | 1.0 → 1.1 | center top |
| 4 | stx-lol-workshop.png | 1.1 → 1.4 | 35% 72% (richting register knop) |

#### Page Load Flash

Witte flash bij elke pagina-transitie:
```tsx
const pageFlash = interpolate(
  frame,
  [START, START + 2, START + 6],
  [0, 1, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
// Witte div met opacity = pageFlash over de content
```

#### Lottie Arrow (Fase 4)

Arrow pointing animatie die naar de register knop wijst.

```tsx
// Verschijnt 30 frames na fase 4 start
// Spring pop-in: { damping: 8, mass: 0.4, stiffness: 180 }
// Pulsating scale: 1 + sin(frame * 0.15) * 0.08
// Positie: left 30%, top 67%
// Rotatie: -90deg
// Bron: animations/arrows/arrow-pointing.json
```

#### SVG Cursor

Programmatische SVG cursor (wit met zwarte rand, 28x38px).

**Beweging:** Smoothstep interpolatie tussen waypoints:
```tsx
const eased = progress * progress * (3 - 2 * progress); // smoothstep
cursorX = from.x + (to.x - from.x) * eased;
```

**Klik animatie:** Cursor schaalt naar 0.85 gedurende 4 frames bij klik.

**Cursor posities (px, relatief aan 1920x1080):**

| Actie | x | y | Frame |
|-------|---|---|-------|
| Start | 960 | 540 | 0 |
| Klik zoekbalk | 960 | 607 | FADE + 15 |
| Klik zoekresultaat | 495 | 362 | FADE + 90 + 30 |
| Klik workshop banner | 720 | 744 | FADE + 150 + 65 |
| Register knop | 580 | 680 | FADE + 255 + 15 |

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Scale in | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |
| Scale out | in cubic | `Easing.in(Easing.cubic)` |
| Homepage zoom | linear (interpolate) | geen easing |
| Workshop zoom | linear (interpolate) | geen easing |
| Arrow pop-in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Cursor beweging | smoothstep | `p*p*(3-2*p)` |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| FADE | 15 frames (0.5s) | Scale in/out duur |
| Fase 1 | 90 frames (3s) | Google homepage + typewriter |
| Fase 2 | 60 frames (2s) | Zoekresultaten |
| Fase 3 | 90 frames (3s) | Sempertex homepage + zoom |
| Fase 4 | 105 frames (3.5s) | Workshop pagina + arrow |
| Totaal | 360 frames (12s) | Volledige overlay duur |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Scale in | Fast whoosh | 0.35 | `sound-effects/dragon-studio-epic-whoosh-478371.mp3` | 5 frames voor overlay start |
| Klik zoekbalk | Mouse click | 0.2 | `sound-effects/universfield-computer-mouse-click-352734.mp3` | FADE + 15 |
| Typewriter | Keyboard typing | 0.15 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | FADE + 20, duur 50 frames |
| Klik zoekresultaat | Mouse click | 0.2 | `sound-effects/soundreality-sound-of-mouse-click-4-478760.mp3` | FADE + 120 |
| Klik workshop | Mouse click | 0.2 | `sound-effects/universfield-computer-mouse-click-351398.mp3` | FADE + 225 |
| Scale out | Swoosh | 0.4 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` | duration - FADE |

Drie verschillende click sounds voor variatie. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition (niet in het BrowserAnimation component).

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Browser chrome | Grijs | #e8e8e8 |
| Address bar | Wit | #ffffff |
| Traffic light rood | Rood | #ff5f57 |
| Traffic light geel | Geel | #febc2e |
| Traffic light groen | Groen | #28c840 |
| Google blauw | Blauw | #4285F4 |
| Google rood | Rood | #EA4335 |
| Google geel | Geel | #FBBC05 |
| Google groen | Groen | #34A853 |
| Zoekbalk border | Grijs | #dfe1e5 |
| Tekst kleur | Donkergrijs | #202124 |
| Page flash | Wit | #ffffff |
| Cursor | Wit + zwarte rand | #fff / #000 |

Niet-brand kleuren zijn bewust: ze simuleren echte browser/Google UI voor herkenning.

**TRANSITIE:** Scale in/out met spring (geen slide). Fullscreen overlay bedekt de hele video.

**REFERENTIE:** `remotion-stx/src/overlays/browser-animation.tsx` (BrowserAnimation component)

**REGISTRATIE:** Moment 20 in Composition `Denise-Overlays`, Sequence from={26940}

---

### TYPE: leerstof-lijst

**WANNEER:** Overzicht van wat de kijker gaat leren, opsomming van vaardigheden/technieken. Vergelijkbaar met materialenlijst maar met donkerder thematiek en een bonus-item highlight.

**LAYOUT:** Side panel links (~40% scherm / 780px), video schuift naar rechts.

```
Panel breedte: 780px (~40% van 1920px)
Video shift: 200px naar rechts
Video scale: 1.06x
```

**STRUCTUUR:**

```
┌────────────────────────────┐
│                            │
│  WHAT YOU'LL               │  ← Titel: 2 regels, strakke lineHeight
│  LEARN                     │
│  ━━━━━━━━━                 │  ← Gele accent line
│                            │
│  Curved edges              │  ← Wipe reveal items
│  Cross weave               │
│  Grid wall                 │
│  Zig zag weave             │
│  Bonus: pricing & upscaling│  ← Magenta + pulserende scale
│                            │
│       [particles]          │
└────────────────────────────┘
```

**BEVAT:**

#### Achtergrond (lavender, licht)

Zelfde frosted glass + lavender gradient als step-overlay type:

```tsx
backdropFilter: "blur(50px) brightness(1.1) saturate(1.2)"
background: lavender gradient (${BRAND.colors.primary.lavender})
```

#### Titel

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 72
fontWeight: 800
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 4
lineHeight: 1.05  // strak, "LEARN" dicht onder "WHAT YOU'LL"
```

Met gele accent line eronder (zelfde als materialenlijst type).

#### Lijst Items (wipe reveal)

Zelfde wipe-reveal mechanisme als materialenlijst, maar:
- Alle items dezelfde grootte (48px, weight 800, italic)
- Kleur: dark purple (#1b073d)
- Stagger: 30 frames (1 seconde) tussen items
- Alternerende bar kleuren (geel/paars)

#### Bonus Item (laatste regel)

Het laatste item krijgt speciale behandeling:
- Tekst kleur: magenta (`BRAND.colors.primary.magenta` / #cd0b5c)
- Bar kleur: magenta
- Na volledig onthuld: pulserende scale animatie

```tsx
const bonusPulse = 1 + Math.sin((frame - revealEnd) * 0.12) * 0.05;
// Amplitude: 5%, frequentie: ~0.6Hz
// transformOrigin: "left center"
```

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M21_DURATION | 270 frames (9s) | Totale overlay duur |
| M21_FADE | 14 frames (~0.47s) | Slide in/uit |
| M21_PANEL_WIDTH | 780px | Panel breedte (~40%) |
| M21_VIDEO_SHIFT | 200px | Video verschuiving |
| Item stagger | 30 frames (1s) | Tussen elk item |

#### Sound Design

Geen geluidseffecten.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Panel achtergrond | Lavender gradient | #f1d9ff |
| Titel tekst | Dark Purple | #1b073d |
| Item tekst | Dark Purple | #1b073d |
| Bonus item tekst | Magenta | #cd0b5c |
| Bonus bar | Magenta | #cd0b5c |
| Accent line | Yellow | #ffdb5a |
| Wipe bars (even) | Yellow | #ffdb5a |
| Wipe bars (oneven) | Purple | #6b3fb9 |
| Particles | Purple | #6b3fb9 |

**TRANSITIE:** Panel schuift van links, video schuift naar rechts (zelfde als materialenlijst).

**REFERENTIE:** `remotion-stx/src/overlays/denise-overlays.tsx` (WhatYoullLearnPanel component)

**REGISTRATIE:** Moment 21 in Composition `Denise-Overlays`, Sequence from={27510}

---

### TYPE: youtube-subscribe

**WANNEER:** CTA moment aan het einde van een video om kijkers te vragen het YouTube kanaal te volgen. Simuleert de YouTube subscribe flow met interactieve cursor. **Altijd in STX branding (lavender achtergrond, dark purple tekst, gele subscribe knop).**

**LAYOUT:** Floating bar onderaan het scherm, horizontaal gecentreerd. Video blijft volledig zichtbaar erachter.

```
Positie: bottom 120px, left 50%, translateX(-50%)
Achtergrond: Lavender (#f1d9ff / BRAND.colors.primary.lavender)
Border-radius: 20px
Padding: 18px 30px
Base scale: 2.5x
Z-index: 50
```

**STRUCTUUR:** Horizontale bar met vier elementen:

```
┌──────────────────────────────────────────────┐
│  ▶ YouTube  │  @sempertexeurope  │ Subscribe │ 🔔 │
└──────────────────────────────────────────────┘
  ↑ Lavender achtergrond, STX branded kleuren
```

**BEVAT:**

#### YouTube Icoon (SVG, branded)

Programmatisch SVG: dark purple afgeronde rechthoek met witte play triangle.

```tsx
<svg width="45" height="33" viewBox="0 0 36 26">
  <rect width="36" height="26" rx="6" fill={BRAND.colors.secondary.darkPurple} />
  <path d="M14 7L25 13L14 19V7Z" fill="white" />
</svg>
```

#### Channel Naam

```tsx
fontFamily: "Lato, sans-serif"
fontSize: 25
fontWeight: 700
color: BRAND.colors.secondary.darkPurple  // #1b073d
whiteSpace: "nowrap"
```

#### Subscribe Knop (branded)

State change na klik:
- **Voor klik:** backgroundColor `BRAND.colors.secondary.yellow` (#ffdb5a), tekst "Subscribe" in dark purple
- **Na klik:** backgroundColor `BRAND.colors.primary.purple` (#6b3fb9), tekst "Subscribed" in wit
- **Klik animatie:** scale 1 → 0.95 → 1 over 6 frames

```tsx
borderRadius: 25
padding: "10px 25px"
fontSize: 20, fontWeight: 700
// Voor: color BRAND.colors.secondary.darkPurple
// Na: color BRAND.colors.neutral.white
```

#### Notification Bell (SVG, magenta)

Altijd SVG (geen Lottie, want witte Lottie is onzichtbaar op lavender achtergrond).
- Breedte: 35x35px
- Kleur: magenta (`BRAND.colors.primary.magenta` / #cd0b5c)
- Na klik: wiggle rotatie animatie

```tsx
<svg width="35" height="35" viewBox="0 0 24 24" fill={BRAND.colors.primary.magenta}>
  <path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.63-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z" />
</svg>
```

**Bell wiggle (multi-keyframe):**
```tsx
const bellWiggle = interpolate(
  frame,
  [+4, +8, +12, +16, +20, +24, +28],
  [-15, 15, -12, 12, -8, 5, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
// transformOrigin: "top center"
```

#### SVG Cursor

Zelfde cursor als browser-animation type (wit, zwarte rand, 30x40px).
- Smoothstep beweging tussen waypoints
- Klik: scale 0.85 gedurende 4 frames
- Zichtbaar alleen tijdens interactiefasen (niet tijdens hold/exit)

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Pop in van onder | spring | `{ damping: 10, mass: 0.4, stiffness: 160 }` |
| Slide out naar onder | in cubic | `Easing.in(Easing.cubic)` |
| Subscribe knop klik | linear (multi-keyframe) | 1 → 0.95 → 1 |
| Bell wiggle | linear (multi-keyframe) | -15° → 15° → ... → 0° |
| Cursor beweging | smoothstep | `p*p*(3-2*p)` |

#### Animatie Sequentie

| Fase | Frame | Duur | Beschrijving |
|------|-------|------|-------------|
| Pop in | 0-9 | 0.3s | Bar springt omhoog van onder (translateY 250 → 0) |
| Cursor → Subscribe | 14-30 | 0.5s | Cursor beweegt naar subscribe knop |
| Subscribe klik | 30 | instant | Knop verandert geel → paars, tekst → "Subscribed" |
| Cursor → Bell | 30-45 | 0.5s | Cursor beweegt naar belletje |
| Bell klik + wiggle | 45-73 | ~0.9s | Klik + 7-keyframe wiggle rotatie |
| Hold | 73-105 | ~1s | Alles stilstand |
| Slide out | 105-120 | 0.5s | Bar slide naar beneden + fade out |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| POP_IN_END | 9 frames (0.3s) | Pop-in animatie klaar |
| SUBSCRIBE_CLICK | 30 frames (1s) | Subscribe knop klik |
| BELL_CLICK | 45 frames (1.5s) | Bell klik |
| HOLD_END | 105 frames (3.5s) | Begin slide out |
| SLIDE_OUT_DURATION | 15 frames (0.5s) | Slide out duur |
| Totaal | 120 frames (4s) | Volledige overlay duur |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Pop in | Notification ding | 0.3 | `sound-effects/dragon-studio-notification-bell-sound-1-376885.mp3` |
| Subscribe klik | Mouse click | 0.2 | `sound-effects/universfield-computer-mouse-click-352734.mp3` |
| Bell klik | Bell ring | 0.25 | `sound-effects/dragon-studio-bell-ring-390294.mp3` |
| Slide out | Fast whoosh | 0.3 | `sound-effects/dragon-studio-epic-whoosh-478371.mp3` |

Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Bar achtergrond | Lavender | #f1d9ff |
| YouTube icoon | Dark Purple | #1b073d |
| YouTube play triangle | Wit | #ffffff |
| Channel naam | Dark Purple | #1b073d |
| Subscribe knop (voor) | Yellow | #ffdb5a |
| Subscribe knop tekst (voor) | Dark Purple | #1b073d |
| Subscribe knop (na) | Purple | #6b3fb9 |
| Subscribe knop tekst (na) | Wit | #ffffff |
| Bell icoon | Magenta | #cd0b5c |
| Cursor | Wit + zwarte rand | #fff / #000 |

Alle kleuren zijn STX branded. Platform iconen (YouTube play) behouden herkenbare vorm maar in brand kleuren.

**TRANSITIE:** Pop in van onder (spring) + slide out naar onder (eased). Geen fullscreen overlay, video blijft zichtbaar. Scale 2.5x voor zichtbaarheid op 4K.

**REFERENTIE:** `remotion-stx/src/overlays/youtube-subscribe.tsx` (YouTubeSubscribe component, branded versie)

**REGISTRATIE:** Moment 22 in Composition `Denise-Overlays` + Moment 21 in Composition `Audrey-Robin-Q`

---

### TYPE: social-bar

**WANNEER:** CTA moment om kijkers naar social media kanalen te leiden. Floating bar bovenaan het scherm met platform iconen en kanaal naam. **Altijd in STX branding (lavender achtergrond, dark purple tekst).**

**LAYOUT:** Floating bar bovenaan het scherm, horizontaal gecentreerd. Video blijft volledig zichtbaar erachter.

```
Positie: top 94px, left 50%, translateX(-50%)
Achtergrond: Lavender (#f1d9ff / BRAND.colors.primary.lavender)
Border-radius: 16px
Padding: 15px 30px
Base scale: 2.5x
Z-index: 50
```

**STRUCTUUR:** Horizontale bar met vijf elementen:

```
┌───────────────────────────────────────────────────┐
│  📷 Instagram  │  📘 Facebook  @sempertexeurope  Follow us │
└───────────────────────────────────────────────────┘
  ↑ Lavender achtergrond, STX branded kleuren
```

**BEVAT:**

#### Instagram Icoon (SVG, gradient)

Programmatische SVG (30x30px) met radial gradient. Platform kleuren behouden voor herkenning.

```tsx
<radialGradient id="ig-branded-grad" cx="30%" cy="107%" r="150%">
  <stop offset="0%" stopColor="#fdf497" />
  <stop offset="5%" stopColor="#fdf497" />
  <stop offset="45%" stopColor="#fd5949" />
  <stop offset="60%" stopColor="#d6249f" />
  <stop offset="90%" stopColor="#285AEB" />
</radialGradient>
```

#### Divider

```tsx
width: 1
height: 24
backgroundColor: "rgba(27, 7, 61, 0.25)"  // dark purple 25% opacity
```

#### Facebook Icoon (SVG)

Programmatische SVG (30x30px): blauwe afgeronde rechthoek (#1877F2) met witte "f" path. Platform kleur behouden.

#### Channel Naam

```tsx
fontFamily: "Lato, sans-serif"
fontSize: 22
fontWeight: 700
color: BRAND.colors.secondary.darkPurple  // #1b073d
whiteSpace: "nowrap"
```

#### Follow Us Tekst

```tsx
fontFamily: "Lato, sans-serif"
fontSize: 18
fontWeight: 700
color: BRAND.colors.primary.purple  // #6b3fb9
whiteSpace: "nowrap"
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Slide in van boven | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |
| Pop out | in cubic | `Easing.in(Easing.cubic)` |

#### Animaties

**Slide in (spring):**
```tsx
const slideIn = spring({
  frame,
  fps,
  config: { damping: 14, mass: 0.5, stiffness: 120 },
});
const slideInY = interpolate(slideIn, [0, 1], [-120, 0]);
```

**Pop out (3-keyframe):**
```tsx
const popOut = interpolate(
  frame,
  [holdEnd, holdEnd + 3, holdEnd + 9],
  [1, 1.05, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic) },
);
```

**Gecombineerde transform:**
```tsx
transform: `translateX(-50%) translateY(${translateY}px) scale(${scale * 2.5})`
// 2.5x scale voor zichtbaarheid op 4K
```

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| POP_OUT_FRAMES | 9 frames (0.3s) | Pop-out duur |
| Spring settle | ~12 frames (~0.4s) | Slide-in tot rust |
| Hold | ~102 frames (~3.4s) | Stilstand |
| Totaal | 120 frames (4s) | Volledige overlay duur |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Verschijning | Mouse click | 0.25 | `sound-effects/soundreality-sound-of-mouse-click-4-478760.mp3` |
| Pop out | Soft pop | 0.2 | `sound-effects/soundreality-pop-423717.mp3` |

Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Bar achtergrond | Lavender | #f1d9ff |
| Instagram gradient | Platform kleuren | #fdf497 -> #fd5949 -> #d6249f -> #285AEB |
| Facebook achtergrond | Facebook Blauw | #1877F2 |
| Icoon details | Wit | #ffffff |
| Divider | Dark Purple 25% opacity | rgba(27, 7, 61, 0.25) |
| Channel naam | Dark Purple | #1b073d |
| Follow us tekst | Purple | #6b3fb9 |
| Bar glow | Purple | rgba(107,63,185,0.2) |

Lavender achtergrond consistent met youtube-subscribe type. IG/FB iconen behouden platform kleuren voor herkenning, overige elementen zijn STX branded.

**TRANSITIE:** Slide in van boven (spring) + pop out (scale 1→1.05→0). Video blijft volledig zichtbaar. Scale 2.5x voor zichtbaarheid op 4K.

**REFERENTIE:** `remotion-stx/src/overlays/social-bar.tsx` (SocialBar component, branded versie)

**REGISTRATIE:** Moment 23 in Composition `Denise-Overlays` + Moment 22 in Composition `Audrey-Robin-Q`

---

### TYPE: part-intro

**WANNEER:** Begin van een nieuwe video die deel is van een serie (Part 2, Part 3, etc.). Toont serie-context, video-onderwerp en cross-promotie naar de vorige aflevering. Vervangt de video volledig in de eerste 5 seconden voor maximale scroll-stop.

**LAYOUT:** Fullscreen overlay over de hele video. Geen panel, geen video shift. Video loopt eronder maar is volledig bedekt tot de swipe-out. Verticale layout, alles gecentreerd.

```
┌─────────────────────────────────────┐
│                                     │
│   HOW TO BECOME A BALLOON ARTIST    │  ← Header (wit)
│                                     │
│   ┌─────────────────────────────┐   │
│   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │
│   │░░░░░░░░PART 2░░░░░░░░░░░░░░░│   │  ← Geel highlight blok,
│   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │     dark purple tekst
│   └─────────────────────────────┘   │
│                                     │
│   ▶  Watch Part 1 on YouTube...     │  ← Subtitle (wit) + YT icoon
│                                     │
│         @sempertexeurope            │  ← Handle (wit)
│         ━━━━━━━━━━━━━━━              │  ← Gele branding streep
│                                     │
└─────────────────────────────────────┘
```

**BEVAT:**

#### Achtergrond Stack (van onder naar boven, allemaal `<AbsoluteFill>`)

1. **Base gradient** — radial purple ellipse + linear purple→darkPurple
   ```tsx
   background: `
     radial-gradient(ellipse 80% 60% at 50% 45%, ${BRAND.colors.primary.purple} 0%, transparent 70%),
     linear-gradient(180deg, ${BRAND.colors.primary.purple} 0%, ${BRAND.colors.secondary.darkPurple} 100%)
   `
   ```

2. **Roterende conic gradient** — diepe ambient draaiing, `mixBlendMode: screen`, opacity 0.85
   ```tsx
   const conicAngle = (frame * 0.6) % 360;
   background: `conic-gradient(from ${conicAngle}deg at 50% 50%, ${purple}00, ${magenta}22, ${lavender}1a, ${purple}00, ${yellow}14, ${purple}00)`
   ```

3. **Drie driftende blobs** (magenta, lavender, yellow accent) — sin/cos paden, `mixBlendMode: screen`
   ```tsx
   const blob1X = 50 + Math.sin(frame * 0.025) * 18;
   const blob1Y = 45 + Math.cos(frame * 0.022) * 14;
   const blob2X = 30 + Math.cos(frame * 0.018) * 22;
   const blob2Y = 60 + Math.sin(frame * 0.024) * 16;
   const blob3X = 75 + Math.sin(frame * 0.02 + 1.5) * 16;
   const blob3Y = 35 + Math.cos(frame * 0.019 + 1) * 18;
   ```
   Blob 1 (magenta): `radial-gradient(ellipse 45% 40% at ${blob1X}% ${blob1Y}%, ${magenta}3a 0%, transparent 65%)`
   Blob 2 (lavender): `radial-gradient(ellipse 38% 32% at ${blob2X}% ${blob2Y}%, ${lavender}28 0%, transparent 60%)`
   Blob 3 (yellow): `radial-gradient(ellipse 30% 26% at ${blob3X}% ${blob3Y}%, ${yellow}1f 0%, transparent 55%)`

4. **Sweeping diagonal light streak** — één pass over 5s, hoek 105°
   ```tsx
   const streakX = interpolate(frame, [0, 150], [-30, 130], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
   background: `linear-gradient(105deg, transparent ${streakX - 8}%, ${lavender}22 ${streakX}%, ${white}10 ${streakX + 2}%, transparent ${streakX + 10}%)`
   ```

5. **Particles** — twee lagen voor diepte
   - Layer 1: 45 lavender particles, `speedMultiplier: 1.8`, `maxOpacity: 0.35`, seed 42
   - Layer 2: 20 yellow particles, `speedMultiplier: 0.9`, `maxOpacity: 0.28`, seed 117

6. **Vignette** — randen donkerder voor focus naar centrum
   ```tsx
   background: `radial-gradient(ellipse 90% 70% at 50% 50%, transparent 50%, rgba(0,0,0,0.35) 100%)`
   ```

#### Header (boven het titelblok)
- Tekst: bijvoorbeeld `"HOW TO BECOME A BALLOON ARTIST"`
- Font: Rethink Sans Bold (700), 110px
- Kleur: wit (`BRAND.colors.neutral.white`)
- letterSpacing: 6, lineHeight: 1
- textShadow: `0 4px 20px rgba(0,0,0,0.55)`
- whiteSpace: nowrap, textAlign: center
- Pop-in: spring `{ damping: 12, mass: 0.5, stiffness: 140 }`

#### Geel highlight blok met titel
- Achtergrond: `BRAND.colors.secondary.yellow`
- Padding: `40px 140px 56px` (extra bottom voor optisch midden door descenders)
- boxShadow: `0 24px 80px rgba(0,0,0,0.45)`
- Wipe reveal van links naar rechts via `clipPath: inset(0 ${100 - blockReveal}% 0 0)`
- Titel binnenin: Rethink Sans Extra Bold (800), 540px, dark purple (`BRAND.colors.secondary.darkPurple`), letterSpacing 14, lineHeight 1, whiteSpace nowrap
- Pop-in: spring `{ damping: 10, mass: 0.55, stiffness: 145 }` met natuurlijke overshoot
- Wipe reveal duur: 14 frames (~0.47s), easing `Easing.out(Easing.cubic)`
- Breathing tijdens hold: `1 + Math.sin((frame - breatheStart) * 0.06) * 0.012` (start 20 frames na pop-in)

#### Subtitle row (YouTube cross-promo)
- Layout: horizontale flex, gap 36
- Linker icoon: rode YouTube SVG, size 120px (rood `#FF0000` is intentioneel — platform brand kleur)
- Tekst: bijvoorbeeld `"Watch Part 1 on our YouTube channel"`
- Font: Lato Bold (700), 110px
- Kleur: wit
- letterSpacing: 1, textShadow: `0 4px 16px rgba(0,0,0,0.5)`
- Pop-in: spring `{ damping: 11, mass: 0.5, stiffness: 140 }`

#### Handle + gele branding streep
- Handle tekst: bijvoorbeeld `"@sempertexeurope"`
- Font: Rethink Sans Bold (700), 96px
- Kleur: wit (NIET geel — geel is gereserveerd voor highlight blok en accent line)
- letterSpacing: 2, textShadow: `0 4px 20px rgba(0,0,0,0.55)`
- Branding streep eronder:
  - Width: 720px, height: 10px
  - Backgroundcolor: `BRAND.colors.secondary.yellow`
  - borderRadius: 5
  - boxShadow: `0 0 24px ${yellow}80` (subtiele glow)
  - Expand-from-center via `clipPath: inset(0 ${(100 - lineWidth) / 2}% 0 ${(100 - lineWidth) / 2}%)`
- Streep expand: 16 frames, easing `Easing.out(Easing.cubic)`, start 6 frames na handle pop-in
- Container gap tussen handle en streep: 24px
- Hele blok pop-in: spring `{ damping: 11, mass: 0.5, stiffness: 140 }`

#### Content container
```tsx
display: "flex",
flexDirection: "column",
alignItems: "center",
justifyContent: "center",
gap: 64,
```

#### Animaties Samenvatting

| Element | Type | Easing / Spring config |
|---------|------|------------------------|
| Header pop in | spring | `{ damping: 12, mass: 0.5, stiffness: 140 }` |
| Title pop in | spring (overshoot) | `{ damping: 10, mass: 0.55, stiffness: 145 }` |
| Yellow block wipe reveal | interpolate | `Easing.out(Easing.cubic)` over 14 frames |
| Subtitle pop in | spring | `{ damping: 11, mass: 0.5, stiffness: 140 }` |
| Handle pop in | spring | `{ damping: 11, mass: 0.5, stiffness: 140 }` |
| Branding line expand | interpolate | `Easing.out(Easing.cubic)` over 16 frames |
| Title breathing | sin wave | amplitude 0.012, frequentie 0.06 |
| Conic background rotate | linear | `(frame * 0.6) % 360` graden/frame |
| Blob drift | sin/cos | freq 0.018-0.025, amplitude 14-22% |
| Light streak sweep | interpolate | linear over 150 frames, één pass |
| Swipe out | interpolate | `Easing.inOut(Easing.cubic)`, 15 frames, translateX → `width * 1.2` |

> **Belangrijke regel:** Gebruik één enkele spring voor pop-ins met natuurlijke overshoot. Combineer NOOIT een springy spring met een keyframe overshoot in interpolate (`[0, 0.55, 1] → [0, 1.1, 1]`) — dat veroorzaakt dubbele bounce wobble.

#### Timing

| Constante | Frame | Tijd | Beschrijving |
|-----------|-------|------|-------------|
| `M1_HEADER_IN` | 6 | 0:00.2 | Header pop-in start |
| `M1_TITLE_IN` | 18 | 0:00.6 | PART X + geel blok wipe reveal |
| `M1_SUBTITLE_IN` | 33 | 0:01.1 | Subtitle + YouTube icoon |
| `M1_HANDLE_IN` | 48 | 0:01.6 | Handle + branding streep |
| Hold | 48-135 | 1.6-4.5s | Statisch met breathing + bewegende achtergrond |
| `M1_SWIPE_OUT_START` | 135 | 0:04.5 | Swipe rechts uit beeld |
| `M1_SWIPE_OUT_DURATION` | 15 | ~0.5s | Duur van swipe |
| `M1_END_FRAME` | 150 | 0:05 | Overlay verdwenen, video volledig zichtbaar |

> Stagger tussen elementen: ~12-15 frames (~0.4-0.5s). Eerste pop-in bij frame 6 (0.2s) voor sterke scroll-stop — vermijdt 0.5s "leeg" gradient bij start.

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Header pop in | Soft pop | 0.45 | `sound-effects/soundreality-pop-423717.mp3` |
| Title pop in | Soft pop | 0.55 | `sound-effects/soundreality-pop-423717.mp3` |
| Subtitle pop in | Soft pop | 0.5 | `sound-effects/soundreality-pop-423717.mp3` |
| Handle pop in | Soft pop | 0.5 | `sound-effects/soundreality-pop-423717.mp3` |
| Swipe out | Whoosh | 0.55 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` |

> Whoosh start 2 frames vóór de visuele swipe (`from={M1_SWIPE_OUT_START - 2}`) voor correcte ear-eye sync. Title pop heeft iets hoger volume (0.55) dan de andere voor optische emphasis op het hoofdelement.

#### Kleuren Samenvatting

| Element | Kleur | BRAND referentie | HEX |
|---------|-------|-----------------|-----|
| Base gradient top | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Base gradient bottom | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Highlight blok achtergrond | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| PART X tekst | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Header tekst | White | `BRAND.colors.neutral.white` | #ffffff |
| Subtitle tekst | White | `BRAND.colors.neutral.white` | #ffffff |
| Handle tekst | White | `BRAND.colors.neutral.white` | #ffffff |
| Branding streep | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Blob 1 | Magenta @ alpha 3a | `BRAND.colors.primary.magenta` | #cd0b5c |
| Blob 2 | Lavender @ alpha 28 | `BRAND.colors.primary.lavender` | #f1d9ff |
| Blob 3 | Yellow @ alpha 1f | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Particles layer 1 | Lavender | `BRAND.colors.primary.lavender` | #f1d9ff |
| Particles layer 2 | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| YouTube icoon | YouTube Red | hardcoded (platform brand) | #FF0000 |

#### Regels voor kleurgebruik

- **Geel** alleen voor: highlight blok achter PART X titel, branding streep onder handle, subtle blob accent, particle layer 2. NIET voor tekst.
- **Wit** voor alle leesbare tekst (header, subtitle, handle).
- **Dark purple** voor de PART X tekst binnen het gele blok (maximaal contrast).
- Achtergrond mag nooit pure zwart zijn — altijd purple variants voor brand consistency.

**TRANSITIE:** Stagger pop-ins van boven naar onder met spring + wipe reveal op het highlight blok. Continue achtergrondbeweging via roterende conic, driftende blobs, sweeping streak en particles. Swipe-out naar rechts (`Easing.inOut(Easing.cubic)`) voor de hele content stack inclusief achtergrond, zodat de onderliggende video schoon zichtbaar wordt.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-part2-overlays.tsx` (`Moment1PartIntro` component)

**REGISTRATIE:** Moment 1 in Composition `Audrey-Robin-Part-2` in `remotion-stx/src/Root.tsx`

---

### TYPE: labeled-photo-carousel

**WANNEER:** Spreker noemt een serie projecten, design types of voorbeelden waarvan elk een eigen titel/label heeft (bijv. "number stack, corporate design 1, corporate design 2"). Sequentiële carousel waar elke foto met label binnenglijdt, even blijft staan en weer wegglijdt voordat de volgende komt.

**LAYOUT:** Linksonder, 5% van de rand. Kaart blijft op één positie staan; alle foto's verschijnen op dezelfde plek. Video blijft volledig zichtbaar (geen panel, geen shift).

```
Positie: left 5%, bottom 5%
Kaart breedte: 836px (~22% van 3840px)
Kaart hoogte: 836px (vierkant)
Label boven kaart, gap 28px
transformOrigin: "bottom left"
```

**STRUCTUUR:** Verticaal stack per item: geel label blok bovenaan, photo card eronder. Beide bewegen samen als één unit.

```
┌──────────────────────┐
│   Number Stack       │  ← Geel label blok, dark purple tekst
└──────────────────────┘
┌──────────────────────┐
│                      │
│                      │
│      Foto            │  ← Vierkante photo card,
│   (objectFit: cover) │     paarse rand met neon glow
│                      │
│                      │
└──────────────────────┘
```

**BEVAT:**

#### Yellow label blok (bovenaan)
- Achtergrond: `BRAND.colors.secondary.yellow` (#ffdb5a)
- Padding: `26px 56px`
- borderRadius: 18
- boxShadow: depth + subtiele yellow glow puls
  ```tsx
  boxShadow: `
    0 12px 32px rgba(0,0,0,0.45),
    0 0 ${50 * glowPulse}px ${yellow}55
  `
  ```
- Tekst:
  - Font: Rethink Sans Extra Bold (800), 76px
  - Kleur: `BRAND.colors.secondary.darkPurple` (#1b073d)
  - letterSpacing: 2, lineHeight: 1, whiteSpace: nowrap
  - Geen text shadow nodig (hoog contrast)

#### Photo card (onderaan)
- width: 836px, height: 836px (vierkant)
- borderRadius: 36
- border: `12px solid ${purple}` (`BRAND.colors.primary.purple`, #6b3fb9)
- backgroundColor: `BRAND.colors.secondary.darkPurple` (val-back als img laadt)
- overflow: hidden
- Neon glow box-shadow met pulse:
  ```tsx
  boxShadow: `
    0 0 ${88 * glowPulse}px ${purple}cc,
    0 0 ${44 * glowPulse}px ${purple}aa,
    0 0 ${176 * glowPulse}px ${purple}55,
    0 24px 70px rgba(0,0,0,0.65)
  `
  ```
- Img: `width: 100%, height: 100%, objectFit: cover`

#### Container (label + card)
```tsx
position: "absolute",
left: "5%",
bottom: "5%",
display: "flex",
flexDirection: "column",
alignItems: "flex-start",
gap: 28,
transform: `translate(${translateX}px, ${floatY}px) scale(${cardScale})`,
transformOrigin: "bottom left",
```

#### Animaties

**Swipe in van links:**
```tsx
const inX = interpolate(
  frame,
  [inFrame, inFrame + 12], // 12 frames = 0.4s
  [M3_OFFSCREEN_X, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);

// M3_OFFSCREEN_X = -(card_width + 600) → ver genoeg uit beeld
// inclusief het label dat boven uitsteekt
```

**Swipe out naar links:**
```tsx
const outX = interpolate(
  frame,
  [outFrame, outFrame + 9], // 9 frames = 0.3s
  [0, M3_OFFSCREEN_X],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);

const translateX = frame < outFrame ? inX : outX;
```

**Entry scale pop (weight bij landing):**
```tsx
const entryScale = interpolate(
  frame,
  [inFrame, inFrame + 14],
  [0.92, 1],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);
```

**Exit scale (subtle shrink):**
```tsx
const exitScale = interpolate(
  frame,
  [outFrame, outFrame + 9],
  [1, 0.94],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);

const cardScale = frame < outFrame ? entryScale : exitScale;
```

**Float Y (loopend, zichtbaar op 4K):**
```tsx
const localFrame = frame - inFrame;
const floatY = Math.sin(localFrame * 0.05) * 28;
```

**Neon glow puls (loopend):**
```tsx
const glowPulse = 0.8 + Math.sin(localFrame * 0.08) * 0.2;
// Bereik: 0.6 → 1.0
```

#### Animatie Samenvatting

| Element | Type | Easing / Spring config |
|---------|------|------------------------|
| Swipe in van links | interpolate | `Easing.out(Easing.cubic)` over 12 frames |
| Swipe out naar links | interpolate | `Easing.in(Easing.cubic)` over 9 frames |
| Entry scale pop | interpolate | `Easing.out(Easing.cubic)` 0.92→1 over 14 frames |
| Exit scale shrink | interpolate | `Easing.in(Easing.cubic)` 1→0.94 over 9 frames |
| Float Y loop | sin wave | freq 0.05, amplitude 28px |
| Neon glow puls | sin wave | freq 0.08, amplitude ±0.2 op base 0.8 |

> **Belangrijke regels:**
> - Geen `<Sequence>` wrapping om de cards. Sequences resetten de lokale frame naar 0, waardoor checks op globale `inFrame` waarden (zoals 720) altijd falen. Render de showcase component **direct** in de main `<AbsoluteFill>` zodat `useCurrentFrame()` globale frames teruggeeft.
> - Alle 5 transforms (inX/outX, entry/exit scale, floatY) op één container — niet op kind elementen verspreiden.
> - `M3_OFFSCREEN_X` moet groter zijn dan de card-breedte alleen, want het label kan zijwaarts uitsteken bij grote tekst. Gebruik `-(card_width + 600)` als veilige marge.

#### Timing per kaart

| Constante | Frames | Tijd | Beschrijving |
|-----------|--------|------|-------------|
| `M3_SWIPE_IN_FRAMES` | 12 | 0.4s | Swipe in duur |
| `M3_SWIPE_OUT_FRAMES` | 9 | 0.3s | Swipe out duur |
| Hold tussen in en out | variabel | 3-4s | Per kaart configureerbaar |
| Gap tussen opeenvolgende kaarten | 6 | 0.2s | Mini ademruimte |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Swipe in (snap) | Transition snap | 0.55 | `sound-effects/oxidvideos-transition-sfx-2-409073.mp3` |
| Swipe out (whoosh) | Whoosh end | 0.45 | `sound-effects/soundreality-whoosh-end-384629.mp3` |

> SFX `<Sequence>` start 1 frame vóór de visuele move (`from={photo.inFrame - 1}`) voor correcte ear-eye sync. Snap whoosh past beter dan een trage cinematic whoosh — sneller en scherper voor snelle slide-in.

#### Kleuren Samenvatting

| Element | Kleur | BRAND referentie | HEX |
|---------|-------|-----------------|-----|
| Label achtergrond | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Label tekst | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Card border | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Card backgroundColor | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Glow kleur | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Label glow accent | Yellow @ alpha 55 | `BRAND.colors.secondary.yellow` | #ffdb5a |

**TRANSITIE:** Card group (label + photo) glijdt met scale-pop in van links, houdt 3-4s vast met float + glow puls, glijdt weg naar links met subtle shrink. Geen video shift. Geen panel. De photo card blijft op één positie — alleen de inhoud verandert per kaart.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-part2-overlays.tsx` (`Moment3PhotoCard` + `Moment3DesignShowcase` componenten)

**REGISTRATIE:** Moment 3 in Composition `Audrey-Robin-Part-2`. Cards staan **direct** in `<AbsoluteFill>`, niet in een `<Sequence>` wrapper. SFX wel in eigen `<Sequence from={photo.inFrame - 1}>`.

---

### TYPE: stacked-product-showcase

**WANNEER:** Spreker presenteert een productlijn of design serie waar je meerdere foto's wilt tonen die thematisch bij één titel horen. Bijvoorbeeld: een product range + voorbeeld design, of een collectie + toepassing. Eén titel boven, twee of meer photo cards verticaal gestapeld.

**LAYOUT:** Linkerkant van het scherm, verticaal gecentreerd. Verticale stack met vaste paddingLeft van 5%. Kaders matchen de **echte aspect ratio** van de foto's — niet geforceerd vierkant.

```
Positie: paddingLeft 5%, vertical center (flex column, justifyContent: center)
Card width: 520px (vast)
Card height: berekend per foto via Math.round(width * h/w)
Title block boven Group 1
Gap tussen Group 1 en Group 2: 40px
Gap title ↔ photo binnen Group 1: 26px
```

**STRUCTUUR:** Twee verticaal gestapelde groepen:

```
┌─────────────────────────┐
│  Silk Range             │  ← Geel title block, dark purple tekst
└─────────────────────────┘
┌─────────────────────────┐
│                         │
│                         │
│   Range product foto    │  ← Card 1, paarse rand,
│   (aspect-correct)      │     hoogte berekend uit aspect ratio
│                         │
│                         │
└─────────────────────────┘

         (gap 40px)

┌─────────────────────────┐
│                         │
│                         │
│   Design foto           │  ← Card 2, paarse rand,
│   (aspect-correct)      │     hoogte berekend uit aspect ratio
│                         │
│                         │
└─────────────────────────┘
```

**BEVAT:**

#### Yellow title block (bovenaan)
- Achtergrond: `BRAND.colors.secondary.yellow`
- Padding: `28px 64px`
- borderRadius: 22
- boxShadow: depth + subtiele yellow glow puls
  ```tsx
  boxShadow: `
    0 14px 44px rgba(0,0,0,0.5),
    0 0 ${60 * glowPulse}px ${yellow}55
  `
  ```
- Tekst:
  - Font: Rethink Sans Extra Bold (800), **108px** (boven 4K threshold van 96)
  - Kleur: `BRAND.colors.secondary.darkPurple`
  - letterSpacing: 4, lineHeight: 1, whiteSpace: nowrap

#### Photo cards (aspect-correct)

**Aspect ratio rule:** Vóór het bouwen, lees de echte pixel dimensies van elke foto en bereken de card hoogte:

```tsx
const M4_CARD_WIDTH = 520;
const M4_RANGE_HEIGHT = Math.round(M4_CARD_WIDTH * (1024 / 761));  // 700
const M4_DESIGN_HEIGHT = Math.round(M4_CARD_WIDTH * (1440 / 1080)); // 693
```

Zo blijft de kader altijd in sync met de foto en hoeft `objectFit: cover` niet te croppen.

**Base card style:**
```tsx
const baseCardStyle: React.CSSProperties = {
  width: M4_CARD_WIDTH,
  borderRadius: 32,
  border: `12px solid ${purple}`,
  boxShadow: `
    0 0 ${80 * glowPulse}px ${purple}cc,
    0 0 ${40 * glowPulse}px ${purple}aa,
    0 0 ${160 * glowPulse}px ${purple}55,
    0 24px 70px rgba(0,0,0,0.65)
  `,
  overflow: "hidden",
  backgroundColor: BRAND.colors.secondary.darkPurple,
};
```

Per card override `height` via prop. Zelfde border + glow stijl als labeled-photo-carousel maar zonder de extra borderRadius/border verschillen.

#### Wit-naar-lavender achtergrond preprocessing

Wanneer een product foto een witte achtergrond heeft die je wilt vervangen door een brand kleur (bijv. `BRAND.colors.primary.lavender` #f1d9ff): **niet** `mix-blend-mode: multiply` gebruiken — dat tint ook de ballonnen zelf.

In plaats daarvan: pre-processing script om witte pixels écht transparant te maken:

```js
// Eénmalig draaien om _alpha variant aan te maken
const sharp = require('sharp');
sharp('public/images/Silk range.png')
  .ensureAlpha()
  .raw()
  .toBuffer({ resolveWithObject: true })
  .then(({ data, info }) => {
    for (let i = 0; i < data.length; i += 4) {
      const r = data[i], g = data[i+1], b = data[i+2];
      // Threshold: bijna-witte pixels worden volledig transparant
      if (r > 240 && g > 240 && b > 240) {
        data[i+3] = 0;
      }
    }
    return sharp(data, { raw: { width: info.width, height: info.height, channels: 4 } })
      .png()
      .toFile('public/images/Silk range_alpha.png');
  });
```

Daarna in de card:
```tsx
<div style={{
  ...baseCardStyle,
  backgroundColor: BRAND.colors.primary.lavender, // toont door transparante pixels
}}>
  <Img
    src={staticFile("images/Silk range_alpha.png")}
    style={{ width: "100%", height: "100%", objectFit: "cover" }}
  />
</div>
```

Bewaar zowel de originele als de `_alpha.png` variant; gebruik origineel waar geen kleur-replacement nodig is.

#### Container

```tsx
<AbsoluteFill style={{
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "flex-start",
  paddingLeft: "5%",
  gap: 40,
}}>
```

#### Animaties

**Pop in (single spring met natuurlijke overshoot):**
```tsx
const popIn = spring({
  frame: frame - inFrame,
  fps,
  config: { damping: 10, mass: 0.55, stiffness: 145 },
});
```

> Geen interpolate-overshoot keyframes combineren met spring — dat geeft dubbele bounce. Single spring met deze config produceert een natuurlijke overshoot tot ~1.08 die settled op 1.0.

**Pop out (keyframe interpolate):**
```tsx
const popOut = interpolate(
  frame,
  [outStart, outStart + 3, outStart + 9],
  [1, 1.05, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);

const scale = frame < outStart ? popIn : popOut;
```

Switch op `outStart` is naadloos omdat popIn dan al settled op 1 is en popOut start op 1.

**Float Y (loopend, met phase offset per card):**
```tsx
const float1 = Math.sin((frame - rangeIn) * 0.05) * 28;
const float2 = Math.sin((frame - designIn) * 0.05 + 1.2) * 28;
```

Phase offset (`+1.2`) op tweede card voorkomt dat ze in unison drijven.

**Glow puls (gedeeld over alle elementen):**
```tsx
const glowPulse = 0.85 + Math.sin(frame * 0.07) * 0.15;
// Bereik: 0.7 → 1.0
```

**Helper functie voor pop scale (gedeeld door title + cards):**
```tsx
const computeM4PopScale = (
  frame: number,
  fps: number,
  inFrame: number,
  outStart: number,
  outDuration: number,
) => {
  const popIn = spring({
    frame: frame - inFrame,
    fps,
    config: { damping: 10, mass: 0.55, stiffness: 145 },
  });
  const popOut = interpolate(
    frame,
    [outStart, outStart + 3, outStart + outDuration],
    [1, 1.05, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: Easing.in(Easing.cubic),
    },
  );
  return frame < outStart ? popIn : popOut;
};
```

> Naam met `compute*` prefix — niet `use*` — want het is geen React hook (geen useState/useEffect). De `use*` naam zou React's exhaustive deps lint triggeren.

#### Animatie Samenvatting

| Element | Type | Easing / Spring config |
|---------|------|------------------------|
| Pop in (title + cards) | spring | `{ damping: 10, mass: 0.55, stiffness: 145 }` |
| Pop out (synced) | interpolate | keyframes `[1, 1.05, 0]` over 9 frames, `Easing.in(Easing.cubic)` |
| Float Y (per card) | sin wave | freq 0.05, amplitude 28px, phase offset op tweede card |
| Glow puls | sin wave | freq 0.07, amplitude ±0.15 op base 0.85 |
| Title transformOrigin | — | "left center" — schaal vanaf links |
| Card transformOrigin | — | "left center" |

#### Timing

| Constante | Frame | Tijd | Beschrijving |
|-----------|-------|------|-------------|
| Title in | inFrame | 0:00 (relatief) | Eerste pop-in |
| Card 1 in | +9 | +0.3s | Range photo pop-in |
| Card 2 in | +18 | +0.6s | Design photo pop-in |
| Hold | tot outStart | 4-5s typisch | Statisch met float + glow |
| Pop out start | outStart | — | Synced exit voor alle 3 |
| Pop out duur | 9 frames | 0.3s | Allemaal samen weg |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Title pop in | Pop | 0.55 | `sound-effects/soundreality-pop-423717.mp3` |
| Card 1 pop in | Pop | 0.5 | `sound-effects/soundreality-pop-423717.mp3` |
| Card 2 pop in | Pop | 0.5 | `sound-effects/soundreality-pop-423717.mp3` |
| Synced pop out | Pop | 0.5 | `sound-effects/soundreality-pop-423717.mp3` |

> Title iets luider (0.55) dan de cards (0.5) voor optische emphasis. Synced pop out gebruikt één pop SFX voor alle 3 elementen samen — voelt als een coherente "groep verdwijnt".

#### Kleuren Samenvatting

| Element | Kleur | BRAND referentie | HEX |
|---------|-------|-----------------|-----|
| Title block achtergrond | Yellow | `BRAND.colors.secondary.yellow` | #ffdb5a |
| Title tekst | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Card border | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Card glow | Purple | `BRAND.colors.primary.purple` | #6b3fb9 |
| Card backgroundColor (algemeen) | Dark Purple | `BRAND.colors.secondary.darkPurple` | #1b073d |
| Card backgroundColor (wit-vervanging) | Lavender | `BRAND.colors.primary.lavender` | #f1d9ff |
| Title yellow glow accent | Yellow @ alpha 55 | `BRAND.colors.secondary.yellow` | #ffdb5a |

#### Regels

- **Geen magenta** (`BRAND.colors.primary.magenta` / #cd0b5c) in dit type. Title blijft strikt geel met dark purple tekst voor consistente "highlight" branding.
- **Aspect ratio matchen**: lees pixel dimensies vóór het bouwen via `sips -g pixelWidth -g pixelHeight`. Gebruik `Math.round(width * h/w)` voor card hoogte.
- **Witte achtergrond vervangen**: nooit `mix-blend-mode: multiply` — gebruik altijd het sharp pre-processing script om transparante alpha variant te genereren.
- **Geen `<Sequence>` wrapper** rond de showcase component zelf — render direct in `<AbsoluteFill>` zodat globale frames werken.

**TRANSITIE:** Stagger pop-ins met spring (title → card 1 → card 2 met 0.3s tussen elk), 4-5s hold met float + glow puls, synced pop-out met scale 1 → 1.05 → 0. Cards blijven op één plek — geen slide.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-part2-overlays.tsx` (`Moment4SilkRange` component + `computeM4PopScale` helper)

**REGISTRATIE:** Moment 4 in Composition `Audrey-Robin-Part-2`. Render direct in `<AbsoluteFill>`, SFX in eigen `<Sequence>` blokken op het hoofdniveau.

---

## 9. ACHTERGROND MUZIEK

### Standaard Track

**Bestand:** `sound-effects/the_mountain-background-music-487009.mp3`

Kalme, ambient track. Geschikt voor tutorials en educatieve video's. Niet te druk, blijft op de achtergrond.

### Implementatie

```tsx
<Sequence from={660}>
  <Audio
    src={staticFile("sound-effects/the_mountain-background-music-487009.mp3")}
    loop
    volume={(f) => {
      const FADE_IN_FRAMES = 30;
      const FADE_OUT_START = totalDuration - startFrame - 150;
      const FADE_OUT_FRAMES = 150;
      const TARGET_VOLUME = 0.03;

      if (f < FADE_IN_FRAMES) {
        return (f / FADE_IN_FRAMES) * TARGET_VOLUME;
      }
      if (f > FADE_OUT_START) {
        const fadeProgress = Math.min(1, (f - FADE_OUT_START) / FADE_OUT_FRAMES);
        return TARGET_VOLUME * (1 - fadeProgress);
      }
      return TARGET_VOLUME;
    }}
  />
</Sequence>
```

### Instellingen

| Parameter | Waarde | Beschrijving |
|-----------|--------|-------------|
| Start | frame 660 (0:22) | Na intro, wanneer spreker begint |
| Fade-in | 30 frames (1s) | Volume 0 → 0.03 |
| Target volume | 0.03 | ~-30dB onder spraak. Nauwelijks hoorbaar. |
| Loop | `loop` prop | Herhaalt naadloos als track korter is dan video |
| Fade-out | 150 frames (5s) | Laatste 5 seconden, volume 0.03 → 0 |

### Regels

- Muziek mag NOOIT luider zijn dan spraak
- Volume 0.03 is de goedgekeurde standaard voor tutorials met spraak
- Gebruik `volume={(f) => ...}` callback voor dynamische fade in/out
- Start na de intro (niet bij frame 0)
- Fade-out altijd over de laatste 5 seconden

---

### TYPE: design-showcase

**WANNEER:** Spreker toont portfolio werk, eerder gemaakte ontwerpen, of voorbeelden van resultaten. Meerdere afbeeldingen worden sequentieel getoond als ingekaderde foto's met datum-badges.

**LAYOUT:** Floating kaart linksonder het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: bottom 5%, left 5%
Kaart breedte: ~1197px (~31% van 3840px)
Kaart hoogte: ~898px (~42% van 2160px)
transformOrigin: "bottom left"
```

De kaarten verschijnen sequentieel. Elke kaart swipe in van links, houdt vast, en swipe uit naar rechts. De volgende kaart verschijnt direct na het verdwijnen van de vorige.

**STRUCTUUR:** Per design een floating kaart met datum badge:

```
                              ┌──────────────┐
                              │ January 2026 │  ← Gele badge, rechtsboven
┌─────────────────────────────┴──────────────┤
│                                            │
│                                            │
│          Design afbeelding                 │  ← objectFit: cover
│          (ingekaderd)                      │
│                                            │
│                                            │
└────────────────────────────────────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Kaart Frame

Afbeelding binnen een kader met paarse rand en neon glow effect.

```tsx
border: `8px solid ${BRAND.colors.primary.purple}`  // #6b3fb9
borderRadius: 20
overflow: "hidden"
```

**Afbeelding:**
```tsx
<Img
  src={staticFile(design.imageSrc)}
  style={{ width: "100%", height: "100%", objectFit: "cover" }}
/>
```

#### Neon Glow (pulserend, 3 lagen)

Drie box-shadow lagen met pulserende opacity voor neon effect:

```tsx
const glowOpacity = interpolate(
  Math.sin(frame * 0.06),
  [-1, 1],
  [0.5, 0.85],
);

boxShadow: [
  `0 0 30px rgba(107, 63, 185, ${glowOpacity})`,       // Laag 1: tight glow
  `0 0 80px rgba(107, 63, 185, ${glowOpacity * 0.5})`,  // Laag 2: medium glow
  `0 0 140px rgba(107, 63, 185, ${glowOpacity * 0.25})`, // Laag 3: atmospheric glow
  "0 12px 40px rgba(0, 0, 0, 0.3)",                      // Drop shadow
].join(", ")
```

Opacity pulseert tussen 0.5 en 0.85 via sinusgolf. Geeft een levend neon-bord effect rond het kader.

#### Datum Badge (rechtsboven van kaart)

Geel blok met datum tekst, zweeft boven de rechterbovenhoek van het kader.

```tsx
position: "absolute"
top: -18
right: -12
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
color: BRAND.colors.secondary.darkPurple         // #1b073d
padding: "20px 48px"
borderRadius: 12
fontFamily: "Rethink Sans, sans-serif"
fontSize: 104
fontWeight: 800  // ExtraBold
boxShadow: "0 4px 12px rgba(0, 0, 0, 0.15)"
whiteSpace: "nowrap"
```

Klein maar leesbaar. Niet dominant ten opzichte van de afbeelding.

#### Wobbly Shake (continu)

Drie overlappende sinusgolven per as voor organisch wiebel-effect. De kaart beweegt constant licht alsof hij aan een muur hangt en zachtjes schommelt.

```tsx
// Horizontale wobble (~8px totale amplitude)
const wobbleX =
  Math.sin(frame * 0.15) * 4 +
  Math.sin(frame * 0.23) * 2.5 +
  Math.sin(frame * 0.37) * 1.5;

// Verticale wobble (~3.5px totale amplitude)
const wobbleY =
  Math.cos(frame * 0.12) * 2 +
  Math.cos(frame * 0.19) * 1.5;

// Rotatie wobble (~0.65 graden totale amplitude)
const wobbleRotate =
  Math.sin(frame * 0.1) * 0.4 +
  Math.sin(frame * 0.18) * 0.25;
```

Toegepast op de container transform samen met swipe en breathe:
```tsx
transform: `translateX(${translateX + wobbleX}px) translateY(${wobbleY}px) rotate(${wobbleRotate}deg) scale(${breathe})`
```

#### Breathe (continu)

```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.008;
// Amplitude: 0.8%, langzame cyclus. Zichtbaar subtiel op scherm.
```

#### Swipe In/Out Animaties

**Swipe in van links (12 frames / 0.4s):**
```tsx
const SWIPE_FRAMES = 12;

const swipeInX = interpolate(
  frame,
  [inFrame, inFrame + SWIPE_FRAMES],
  [-(cardWidth + screenWidth * 0.05 + 40), 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

**Swipe out naar rechts (12 frames / 0.4s):**
```tsx
const swipeOutX = interpolate(
  frame,
  [holdEndFrame, holdEndFrame + SWIPE_FRAMES],
  [0, screenWidth],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

Kaart start volledig buiten scherm links en schuift naar rustpositie. Bij exit schuift hij volledig naar rechts buiten scherm.

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Swipe in | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Swipe out | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Neon glow puls | sinusgolf | `Math.sin(frame * 0.06)` |
| Wobble | sinusgolf (3 lagen) | Zie wobble sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |

#### Sequentie Timing (meerdere kaarten)

Kaarten worden sequentieel getoond. Elke kaart heeft een `inFrame` (swipe in start) en `holdEndFrame` (swipe out start). De gap tussen kaarten is typisch 12 frames (0.4s), zodat de vorige kaart net uit beeld is als de volgende binnenkomt.

**Voorbeeld timing bij 3 designs (30fps):**

| Design | inFrame | holdEndFrame | Hold duur | Beschrijving |
|--------|---------|-------------|-----------|-------------|
| 1 | 750 (0:25.0) | 837 (0:27.9) | 75 frames (2.5s) | Swipe in, hold, swipe out |
| 2 | 849 (0:28.3) | 936 (0:31.2) | 75 frames (2.5s) | Swipe in, hold, swipe out |
| 3 | 948 (0:31.6) | 1035 (0:34.5) | 75 frames (2.5s) | Swipe in, hold, swipe out |

Gap tussen kaarten: 12 frames (= SWIPE_FRAMES, zodat exit van kaart N eindigt precies wanneer entry van kaart N+1 begint).

#### Timing Constanten

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| SWIPE_FRAMES | 12 frames (0.4s) | Duur swipe in en swipe out |
| Hold per kaart | ~75 frames (~2.5s) | Kaart zichtbaar in rustpositie |
| Gap tussen kaarten | 12 frames (0.4s) | Tijd tussen holdEnd van vorige en inFrame van volgende |
| Totaal per kaart | ~99 frames (~3.3s) | Swipe in + hold + swipe out |
| Standaard kaart breedte | 1197px | ~31% van 3840px scherm |
| Standaard kaart hoogte | 898px | ~42% van 2160px scherm |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Swipe in (per kaart) | Soft whoosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` |
| Swipe out (per kaart) | Soft whoosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` |

Twee verschillende whoosh sounds voor in/out variatie. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition (niet in het DesignShowcase component).

```tsx
{designs.map((design, i) => (
  <Sequence key={`sfx-${i}`} from={0} durationInFrames={lastDesign.holdEndFrame + 30}>
    <Sequence from={design.inFrame} durationInFrames={20}>
      <Audio src={staticFile(SFX_WOOSH_IN)} volume={0.25} />
    </Sequence>
    <Sequence from={design.holdEndFrame} durationInFrames={20}>
      <Audio src={staticFile(SFX_WOOSH_OUT)} volume={0.25} />
    </Sequence>
  </Sequence>
))}
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Kaart rand | Purple | #6b3fb9 |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |
| Badge achtergrond | Yellow | #ffdb5a |
| Badge tekst | Dark Purple | #1b073d |
| Badge schaduw | Zwart 15% | rgba(0, 0, 0, 0.15) |

#### Schema (Remotion Studio bewerkbaar)

```typescript
const DesignShowcaseItem = z.object({
  imageSrc: z.string(),
  dateLabel: z.string(),
  inFrame: z.number(),
  holdEndFrame: z.number(),
});

// In parent schema:
m1Enabled: z.boolean(),
m1Designs: z.array(DesignShowcaseItem),
m1CardWidth: z.number().optional(),
m1CardHeight: z.number().optional(),
```

Elke design is individueel bewerkbaar in Remotion Studio: afbeelding, datum tekst, en timing.

**TRANSITIE:** Swipe in van links, swipe out naar rechts (Easing.inOut cubic). Continu wobbly shake + breathe + neon glow puls tijdens hold. Geen video shift.

**REFERENTIE:** `remotion-stx/src/overlays/design-showcase.tsx` (DesignShowcase + DesignCard componenten)

**REGISTRATIE:** Moment 1 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: google-search-card

**WANNEER:** Spreker stelt een vraag, of het moment vraagt om een visuele "hoe doe je dit?" / "wat is dit?" context. Simuleert een compact Google zoekvenster als floating pop-up kaart met typewriter effect. Lichter en compacter dan het fullscreen `browser-animation` type.

**LAYOUT:** Floating kaart aan de linkerkant van het scherm, verticaal gecentreerd. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: left 8%, top 50%, translateY(-50%)
Kaart breedte: ~34% van scherm (width * 0.34)
transformOrigin: "center center"
```

De kaart zweeft over de video. Spreker is rechts volledig zichtbaar.

**STRUCTUUR:**

```
┌─────────────────────────────────┐
│                                 │
│           G o o g l e           │  ← Google logo (gekleurde letters)
│                                 │
│  ┌───────────────────────���─┐    │
│  │ 🔍 How to make balloon… │▏│  │  ← Search bar + typewriter + cursor
│  └─────────────────────────┘    │
│                                 │
└─────────────────────────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Kaart Container

Witte kaart met paarse rand en neon glow. Rondere hoeken dan design-showcase.

```tsx
backgroundColor: BRAND.colors.neutral.white  // #ffffff
borderRadius: 32
border: `4px solid ${BRAND.colors.primary.purple}`  // #6b3fb9
padding: "48px 56px"
display: "flex"
flexDirection: "column"
alignItems: "center"
gap: 36
```

#### Neon Glow (pulserend, 2 lagen + drop shadow)

```tsx
const glowPulse = interpolate(
  Math.sin(frame * 0.08),
  [-1, 1],
  [0.7, 1],
);

boxShadow: [
  `0 0 ${10 * glowPulse}px rgba(107, 63, 185, 0.8)`,   // Laag 1: tight glow
  `0 0 ${30 * glowPulse}px rgba(107, 63, 185, 0.4)`,   // Laag 2: atmospheric glow
  "0 12px 40px rgba(0, 0, 0, 0.25)",                     // Drop shadow
].join(", ")
```

Glow pulseert via sinusgolf (frequentie 0.08). Range 0.7-1.0 (subtieler dan design-showcase 0.5-0.85).

#### Google Logo (programmatisch)

Gekleurde letters, zelfde als in `browser-animation` type maar kleiner.

```tsx
fontSize: 80
fontWeight: 700
fontFamily: "system-ui, sans-serif"
letterSpacing: -1
// Kleuren per letter: #4285F4, #EA4335, #FBBC05, #4285F4, #34A853, #EA4335
```

#### Search Bar

Gestileerde zoekbalk met search icon links, mic icon rechts, en getypte tekst in het midden.

```tsx
width: "100%"
height: 72
border: "2px solid #dfe1e5"
borderRadius: 36
padding: "0 24px"
gap: 16
backgroundColor: BRAND.colors.neutral.white  // #ffffff
boxShadow: "0 2px 8px rgba(0, 0, 0, 0.06)"
```

**Tekst in search bar:**
```tsx
fontSize: 28
fontFamily: "system-ui, sans-serif"
color: "#202124"
overflow: "hidden"
whiteSpace: "nowrap"
```

**Search icon (links):** SVG magnifying glass, 36px, fill `#9aa0a6`
**Mic icon (rechts):** SVG microphone, 32px, fill `#4285f4` (body) + `#34a853` (base)

#### Typewriter Effect

Tekst verschijnt karakter voor karakter na de scale-in animatie. Blinkende cursor geeft het gevoel dat er live wordt getypt.

```tsx
const TYPE_START_DELAY = 12;  // frames na scale-in voordat typen begint
const typeDuration = 40;      // ~1.3s om volledige tekst te typen

const typeStart = inFrame + QCARD_SCALE_IN_FRAMES + TYPE_START_DELAY;
const charsPerFrame = text.length / typeDuration;
const typedChars = Math.min(
  text.length,
  Math.max(0, Math.floor((frame - typeStart) * charsPerFrame)),
);
const displayText = text.slice(0, typedChars);
```

**Blinkende cursor:**
```tsx
const isTyping = frame >= typeStart && typedChars < text.length;
const cursorBlink = Math.sin(frame * 0.3) > 0;
const showCursor = frame >= inFrame + QCARD_SCALE_IN_FRAMES && (isTyping || cursorBlink);

// Cursor element: 2px breed, 28px hoog, #202124, marginLeft 1px
```

Cursor is altijd zichtbaar tijdens typen. Na typen blinkt de cursor via sinusgolf.

#### Shake (continu)

Twee overlappende sinusgolven per as. Subtieler dan design-showcase wobble (~2px totale amplitude vs ~8px). Geeft het gevoel van een neon sign met energie.

```tsx
const shakeX =
  Math.sin(frame * 0.15) * 1.2 +
  Math.sin(frame * 0.27) * 0.8;
// Totale amplitude: ~2px horizontaal

const shakeY =
  Math.cos(frame * 0.12) * 1 +
  Math.cos(frame * 0.21) * 0.6;
// Totale amplitude: ~1.6px verticaal
```

#### Breathe (continu)

```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.008;
// Amplitude: 0.8%, langzame cyclus. Consistent met design-showcase type.
```

#### Scale In Animatie (0.3s)

Kaart schaalt vanuit het midden met een subtiele rotatie. Voelt alsof de kaart wordt "opengeklikt".

```tsx
const QCARD_SCALE_IN_FRAMES = 9; // 0.3s bij 30fps

const scaleIn = interpolate(
  frame,
  [inFrame, inFrame + QCARD_SCALE_IN_FRAMES],
  [0, 1],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);

const rotationIn = interpolate(
  frame,
  [inFrame, inFrame + QCARD_SCALE_IN_FRAMES],
  [-3, 0],  // Subtiele rotatie van -3 graden naar 0
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);
```

Geen spring, geen bounce. Snelle ease-out scale met rotatie correctie. Strakker dan de pop-in van tip-overlay of info-card.

#### Swipe Out naar Links (0.4s)

```tsx
const QCARD_SWIPE_OUT_FRAMES = 12; // 0.4s bij 30fps

const swipeOutX = interpolate(
  frame,
  [holdEndFrame, holdEndFrame + QCARD_SWIPE_OUT_FRAMES],
  [0, -(cardWidth + width * 0.12)],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

Kaart schuift naar links buiten beeld. Bewust links (dezelfde kant als waar hij staat), niet naar rechts.

#### Gecombineerde Transform

```tsx
transform: [
  "translateY(-50%)",                          // Verticaal centreren
  `translateX(${translateX + shakeX}px)`,       // Swipe out + shake
  `translateY(${shakeY}px)`,                    // Shake verticaal
  `scale(${scale})`,                            // Scale in of breathe
  `rotate(${rotation}deg)`,                     // Rotatie bij scale in
].join(" ")
transformOrigin: "center center"
```

Scale wordt overschreven door `scaleIn` tijdens in-animatie, `breathe` tijdens hold.

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Scale in | out cubic | `Easing.out(Easing.cubic)` |
| Rotation in | out cubic | `Easing.out(Easing.cubic)` |
| Swipe out | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Neon glow puls | sinusgolf | `Math.sin(frame * 0.08)` |
| Shake | sinusgolf (2 lagen) | Zie shake sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Cursor blink | sinusgolf | `Math.sin(frame * 0.3)` |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| QCARD_SCALE_IN_FRAMES | 9 frames (0.3s) | Scale in + rotation duur |
| QCARD_SWIPE_OUT_FRAMES | 12 frames (0.4s) | Swipe out duur |
| TYPE_START_DELAY | 12 frames (0.4s) | Delay na scale-in voordat typewriter start |
| typeDuration | 40 frames (~1.3s) | Duur typewriter effect |
| Hold | ~90 frames (~3s) | Afhankelijk van in/holdEnd configuratie |
| Totaal | ~102 frames (~3.4s) | Scale in + hold + swipe out |

#### Animatie Sequentie (typisch voorbeeld)

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Scale in + rotation | 0-9 | 0.3s | Kaart schaalt van 0 naar 1 met -3 naar 0 graden |
| Wacht | 9-21 | 0.4s | Kaart zichtbaar, cursor blinkt, nog geen tekst |
| Typewriter | 21-61 | ~1.3s | Tekst verschijnt karakter voor karakter |
| Hold met volledige tekst | 61-90 | ~1s | Tekst compleet, cursor blinkt |
| Swipe out | 90-102 | 0.4s | Kaart schuift naar links uit beeld |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Scale in | Mouse click | 0.25 | `sound-effects/universfield-computer-mouse-click-351398.mp3` | Bij inFrame |
| Typewriter | Keyboard typing | 0.12 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | Na scale-in + TYPE_START_DELAY, duur 43 frames |
| Swipe out | Bamboo whoosh | 0.2 | `sound-effects/soundreality-whoosh-bamboo-389752.mp3` | Bij holdEndFrame |

Drie geluiden: klik opent de kaart, typing geeft het gevoel van live zoeken, zachte whoosh bij exit. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition (niet in het GoogleSearchCard component).

```tsx
{/* M3 sound effects: click open + typing + soft woosh out */}
<Sequence from={props.m3InFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_CLICK_OPEN)} volume={0.25} />
</Sequence>
<Sequence from={props.m3InFrame + QCARD_SCALE_IN_FRAMES + TYPE_START_DELAY} durationInFrames={43}>
  <Audio src={staticFile(SFX_TYPING)} volume={0.12} />
</Sequence>
<Sequence from={props.m3HoldEndFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_SOFT_WOOSH)} volume={0.2} />
</Sequence>
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Kaart achtergrond | White | #ffffff |
| Kaart rand | Purple | #6b3fb9 |
| Neon glow (2 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 25% | rgba(0, 0, 0, 0.25) |
| Google blauw | Blauw | #4285F4 |
| Google rood | Rood | #EA4335 |
| Google geel | Geel | #FBBC05 |
| Google groen | Groen | #34A853 |
| Search bar border | Grijs | #dfe1e5 |
| Search bar shadow | Zwart 6% | rgba(0, 0, 0, 0.06) |
| Search icon | Grijs | #9aa0a6 |
| Mic icon body | Blauw | #4285f4 |
| Mic icon base | Groen | #34a853 |
| Getypte tekst | Donkergrijs | #202124 |
| Cursor | Donkergrijs | #202124 |

Niet-brand kleuren (Google UI kleuren) zijn bewust: ze simuleren een echte Google zoekbalk voor directe herkenning.

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m3Enabled: z.boolean(),
m3Text: z.string(),
m3InFrame: z.number(),
m3HoldEndFrame: z.number(),
```

Zoektekst, timing en aan/uit zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met browser-animation type

| Aspect | google-search-card | browser-animation |
|--------|-------------------|-------------------|
| Layout | Floating kaart (~34% scherm) | Fullscreen |
| Fasen | 1 (search bar met typewriter) | 4 (Google, resultaten, homepage, workshop) |
| Interactie | Geen cursor, alleen typewriter | Cursor + klik interacties |
| Doel | Visuele vraag-context | CTA naar website |
| Duur | ~3s | ~12s |
| In-animatie | Scale + rotation (ease-out) | Scale (spring) |
| Uit-animatie | Swipe links | Scale out |

**TRANSITIE:** Scale in vanuit midden met rotatie (ease-out cubic, 0.3s) + swipe out naar links (inOut cubic, 0.4s). Video blijft volledig zichtbaar. Continu shake + breathe + neon glow puls tijdens hold.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (GoogleSearchCard component)

**REGISTRATIE:** Moment 3 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: thought-bubble-tip

**WANNEER:** Spreker stelt een vraag aan de kijker, vraagt om interactie (comments, reacties), of er is een moment van reflectie/nieuwsgierigheid. Variant op het tip-overlay type maar dan als "vraag-kaart" met een thought bubble icoon.

**LAYOUT:** Floating kaart linksonder het scherm met een thought bubble erboven. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie tekstvak: bottom 10%, left 5%
transformOrigin: "bottom left"
Thought bubble: top -300px, left 20px (relatief aan tekstvak)
```

De spreker is rechts volledig zichtbaar.

**STRUCTUUR:**

```
        ┌─────────────┐
        │   💭  ?     │  ← Thought bubble PNG + vraagteken
        └─────────────┘
           ↑ popt apart in

┌──────────────────────────────┐
│  ┌──────────┐                │
│  │ QUESTION │                │  ← Geel kader, ALL CAPS, ExtraBold Italic
│  └──────────┘                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━   │  ← Paarse lijn (dubbel dik)
│                              │
│  When did you become a       │  ← Body tekst, Rethink Sans Bold
│  balloon artist? Let us      │
│  know in the comments!       │
│                              │
└──────────────────────────────┘
  ↑ Lavender achtergrond + paarse glow
```

**BEVAT:**

#### Thought Bubble (boven tekstvak)

PNG asset met spring pop-in animatie. Bevat een geanimeerd vraagteken.

```tsx
// Positie relatief aan tekstvak
position: "absolute"
top: -300
left: 20
width: 420
height: 420
transformOrigin: "bottom right"

// Asset
<Img src={staticFile("icons/Thought bubble.png")} />
```

**Vraagteken binnenin:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 156
fontWeight: 800
color: BRAND.colors.primary.purple  // #6b3fb9
// Gecentreerd: top 50%, left 50%, translate(-50%, -55%)
```

Het vraagteken popt apart in na de bubble (eigen spring animatie).

#### Tekstvak (lavender, stx-tip stijl)

Gebaseerd op het middelste vak van het tip-overlay type, maar als standalone kaart.

```tsx
backgroundColor: BRAND.colors.primary.lavender  // #f1d9ff
padding: "58px 67px"
maxWidth: 1152
borderRadius: 29
```

**Pulserende glow (continu):**
```tsx
const glowOpacity = interpolate(Math.sin(frame * 0.06), [-1, 1], [0.15, 0.4]);
boxShadow: [
  "0 8px 32px rgba(0,0,0,0.25)",
  `0 0 24px rgba(107, 63, 185, ${glowOpacity})`,
  `0 0 48px rgba(107, 63, 185, ${glowOpacity * 0.5})`,
].join(", ")
```

#### Titel (in geel kader, ALL CAPS, ExtraBold Italic)

Geel achtergrondblok consistent met materialenlijst-type titel, maar met italic stijl.

```tsx
// Geel kader
display: "inline-block"
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "10px 38px"
borderRadius: 6
marginBottom: 14

// Titel tekst
fontFamily: "Rethink Sans, sans-serif"
fontSize: 86
fontWeight: 800  // ExtraBold
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple  // #1b073d
lineHeight: 1.2
letterSpacing: 4
WebkitTextStroke: `2px ${BRAND.colors.secondary.darkPurple}`  // extra bold effect
```

Altijd ALL CAPS (bijv. "QUESTION"). De `WebkitTextStroke` in dezelfde kleur als de tekst maakt de letters visueel dikker dan fontWeight 800 alleen.

#### Paarse Lijn (dubbel dik)

```tsx
width: "100%"
height: 8  // dubbel dik t.o.v. standaard tip-overlay (4px)
backgroundColor: BRAND.colors.primary.purple  // #6b3fb9
marginBottom: 29
```

#### Body Tekst

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 67
fontWeight: 700  // Bold
color: BRAND.colors.neutral.black  // #000000
lineHeight: 1.4
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Tekstvak pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Pop out | in cubic (3-keyframe) | `Easing.in(Easing.cubic)` |
| Thought bubble pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Vraagteken pop in | spring | `{ damping: 12, mass: 0.3, stiffness: 160 }` |
| Wobble rotatie | sinusgolf (2 lagen) | `Math.sin(frame * 0.05) * 1 + Math.sin(frame * 0.09) * 0.4` |
| Wobble translateY | sinusgolf (2 lagen) | `Math.cos(frame * 0.06) * 2 + Math.cos(frame * 0.1) * 0.8` |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Glow puls | sinusgolf | `Math.sin(frame * 0.06)` |

#### Animaties

**Fase 1: Tekstvak pop in (spring bounce):**
```tsx
const boxPopIn = spring({
  frame,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});
// Schaalt van 0 -> ~1.1 -> 1.0 (natuurlijke overshoot)
```

**Fase 2: Thought bubble verschijnt (na tekstvak):**
```tsx
const M5_BUBBLE_START = 9; // start na box pop-in settle

const bubbleScale = spring({
  frame: frame - M5_BUBBLE_START,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});

// Vraagteken popt apart in na bubble:
const M5_QM_START = M5_BUBBLE_START + 6; // frame 15

const qmSpring = spring({
  frame: frame - M5_QM_START,
  fps,
  config: { damping: 12, mass: 0.3, stiffness: 160 },
});
```

**Fase 3: Wobble tijdens hold (continu):**
```tsx
const wobbleRotation =
  Math.sin(frame * 0.05) * 1 +
  Math.sin(frame * 0.09) * 0.4;
// Totale amplitude: ~1.4 graden, langzame heen-en-weer

const wobbleY =
  Math.cos(frame * 0.06) * 2 +
  Math.cos(frame * 0.1) * 0.8;
// Totale amplitude: ~2.8px verticaal
```

Toegepast op de gehele container (tekstvak + thought bubble bewegen samen).

**Scale breathe (continu):**
```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.005;
// Amplitude: 0.5%, langzame cyclus. Consistent met tip-overlay type.
```

**Fase 4: Pop out (3-keyframe):**
```tsx
const M5_EXIT_FRAMES = 9; // 0.3s
const exitStart = duration - M5_EXIT_FRAMES;

const exitScale = interpolate(
  frame,
  [exitStart, exitStart + 3, duration],
  [1, 1.05, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);
// 9 frames totaal: 3 frames overshoot naar 1.05, dan naar 0
```

**Gecombineerde transform:**
```tsx
transform: [
  `scale(${mainScale * breathe})`,
  `translateY(${wobbleY}px)`,
  `rotate(${wobbleRotation}deg)`,
].join(" ")
transformOrigin: "bottom left"
```

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Tekstvak pop in | 0-~25 | ~0.8s | Spring bounce 0 -> 1.1 -> 1.0 |
| Thought bubble pop in | 9-~25 | ~0.5s | Bubble PNG schaalt in met spring |
| Vraagteken pop | 15-~25 | ~0.3s | Vraagteken schaalt apart in |
| Hold met wobble | ~25-171 | ~4.9s | Alles wiebelt subtiel heen en weer |
| Pop out | 171-180 | 0.3s | Alles tegelijk scale 1 -> 1.05 -> 0 |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M5_EXIT_FRAMES | 9 frames (0.3s) | Pop-out duur |
| M5_BUBBLE_START | 9 frames (0.3s) | Thought bubble verschijnt na box pop-in |
| M5_QM_START | 15 frames (0.5s) | Vraagteken verschijnt na bubble |
| Wobble rotatie amplitude | ~1.4 graden | Subtiele heen-en-weer |
| Wobble Y amplitude | ~2.8px | Subtiele verticale beweging |
| Breathe amplitude | 0.5% | Nauwelijks zichtbaar maar geeft leven |
| Standaard duur | 180 frames (6s) | Configureerbaar via schema |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Tekstvak pop in | Soft pop | 0.2 | `sound-effects/soundreality-pop-423717.mp3` | Bij startFrame |
| Thought bubble pop | Pop | 0.15 | `sound-effects/dragon-studio-pop-402324.mp3` | startFrame + 9 |
| Pop out | Soft pop | 0.2 | `sound-effects/soundreality-pop-423717.mp3` | startFrame + duration - 9 |

Twee verschillende pop sounds voor variatie (soundreality-pop voor box in/out, dragon-studio-pop voor bubble). Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition (niet in het ThoughtBubbleTip component).

```tsx
{/* Box pop in */}
<Sequence from={props.m5StartFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_POP)} volume={0.2} />
</Sequence>
{/* Thought bubble pop */}
<Sequence from={props.m5StartFrame + M5_BUBBLE_START} durationInFrames={15}>
  <Audio src={staticFile(SFX_POP_IN)} volume={0.15} />
</Sequence>
{/* Pop out */}
<Sequence from={props.m5StartFrame + props.m5DurationFrames - M5_EXIT_FRAMES} durationInFrames={20}>
  <Audio src={staticFile(SFX_POP)} volume={0.2} />
</Sequence>
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Tekstvak achtergrond | Lavender | #f1d9ff |
| Titel kader achtergrond | Yellow | #ffdb5a |
| Titel tekst | Dark Purple | #1b073d |
| Titel text-stroke | Dark Purple | #1b073d |
| Paarse lijn | Purple | #6b3fb9 |
| Body tekst | Black | #000000 |
| Vraagteken | Purple | #6b3fb9 |
| Glow kleur | Purple | rgb(107, 63, 185) |
| Schaduw | Zwart 25% | rgba(0, 0, 0, 0.25) |

#### Assets

| Asset | Pad | Beschrijving |
|-------|-----|-------------|
| Thought bubble | `public/icons/Thought bubble.png` | Thought bubble icoon met trailing bolletjes |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m5Enabled: z.boolean(),
m5Text: z.string(),
m5StartFrame: z.number(),
m5DurationFrames: z.number(),
```

Tekst, timing en aan/uit zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met tip-overlay type

| Aspect | thought-bubble-tip | tip-overlay |
|--------|-------------------|-------------|
| Layout | Standalone kaart + thought bubble | 3-sectie blok (foto, tekst, logo) |
| Positie | bottom 10%, left 5% | bottom 10%, left 5% (zelfde) |
| Titel stijl | ALL CAPS, ExtraBold Italic, geel kader, text-stroke | Bold, geen kader |
| Lijn | 8px dik (dubbel) | 4px dik |
| Thought bubble | Ja (PNG + vraagteken) | Nee |
| Animatie hold | Wobble rotatie + translateY | Breathe + glow (geen wobble) |
| In-animatie | Spring pop (zelfde config) | Spring pop (zelfde config) |
| Uit-animatie | Pop out 1 -> 1.05 -> 0 | Pop out 1 -> 1.12 -> 0 |
| Doel | Vraag aan kijker, interactie trigger | Tip, advies, product info |

**TRANSITIE:** Spring pop in (0.3s) met thought bubble die apart verschijnt (0.3s na box). Continu wobble + breathe + glow puls tijdens hold. Pop out alles tegelijk (0.3s). Video blijft volledig zichtbaar.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (ThoughtBubbleTip component)

**REGISTRATIE:** Moment 5 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: video-card

**WANNEER:** Een kort videofragment wordt getoond als reactie, gag, voorbeeld, of context bij wat de spreker zegt. De video speelt af binnenin een branded kader met titel erboven. Gedempt (muted), puur visueel.

**LAYOUT:** Floating kaart linksonder het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: bottom 5%, left 5%
Kaart breedte: 20% van scherm (width * 0.2)
Aspect ratio: 9:16 (verticaal, portrait)
Kaart hoogte: cardWidth * (16/9)
```

De kaart is verticaal (portrait) en compact. Spreker is rechts volledig zichtbaar.

**STRUCTUUR:**

```
┌────────────────┐
│ LIKE THIS? 😂  │  ← Lavender badge, ALL CAPS, ExtraBold Italic + emoji normal
└────────────────┘
┌────────────────┐
│                │
│   ┌────────┐   │
│   │ VIDEO  │   │  ← Afspelende video (muted)
│   │ 9:16   │   │
│   │        │   │
│   └────────┘   │
│                │
└────────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Titel Badge (boven kader)

Lavender kader met tekst in ExtraBold Italic. Emoji's worden apart gerenderd in normale stijl (niet italic).

```tsx
// Badge container
display: "inline-block"
backgroundColor: BRAND.colors.primary.lavender  // #f1d9ff
padding: "12px 40px"
borderRadius: 12
marginBottom: 24

// Tekst (zonder emoji)
fontFamily: "Rethink Sans, sans-serif"
fontSize: 80
fontWeight: 800  // ExtraBold
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple  // #1b073d
textTransform: "uppercase"
letterSpacing: 3
WebkitTextStroke: `1px ${BRAND.colors.secondary.darkPurple}`  // extra bold effect

// Emoji (apart, niet italic)
fontStyle: "normal"
fontSize: 80
letterSpacing: 0
WebkitTextStroke: "0px"
```

**Emoji splitsing:** Tekst en emoji worden automatisch gesplitst via Unicode regex:
```tsx
// Tekst zonder emoji
{title.replace(/\p{Emoji_Presentation}/gu, "")}
// Alleen emoji
{title.match(/\p{Emoji_Presentation}/gu)?.join("") ?? ""}
```

Dit voorkomt dat emoji's italic worden gerenderd (ziet er raar uit).

#### Video Kader

Verticaal kader (9:16 portrait) met paarse rand en 3-laags neon glow, identiek aan design-showcase type.

```tsx
width: width * 0.2
height: cardWidth * (16 / 9)  // 9:16 portrait
border: `8px solid ${BRAND.colors.primary.purple}`  // #6b3fb9
borderRadius: 24
overflow: "hidden"
```

**Neon glow (pulserend, 3 lagen + drop shadow):**
```tsx
const glowOpacity = interpolate(
  Math.sin(frame * 0.06),
  [-1, 1],
  [0.5, 0.85],
);

boxShadow: [
  `0 0 30px rgba(107, 63, 185, ${glowOpacity})`,
  `0 0 80px rgba(107, 63, 185, ${glowOpacity * 0.5})`,
  `0 0 140px rgba(107, 63, 185, ${glowOpacity * 0.25})`,
  "0 12px 40px rgba(0, 0, 0, 0.3)",
].join(", ")
```

Glow puls identiek aan design-showcase type (range 0.5-0.85, frequentie 0.06).

#### Embedded Video

Video speelt af binnenin het kader, gedempt (geen audio track).

```tsx
<OffthreadVideo
  src={staticFile(videoSrc)}
  muted
  style={{
    width: "100%",
    height: "100%",
    objectFit: "cover",
  }}
/>
```

Video start direct wanneer de Sequence begint (inclusief tijdens slide-in). De `muted` prop zorgt dat er geen audio van de embedded video wordt afgespeeld.

#### Shake (continu, SKILL standaard)

Twee overlappende sinusgolven per as. Gebruikt de standaard SKILL shake frequenties.

```tsx
const shakeX =
  Math.sin(frame * 0.08) * 1 +
  Math.sin(frame * 0.13) * 0.5;
// Totale amplitude: ~1.5px horizontaal

const shakeY =
  Math.cos(frame * 0.06) * 0.7 +
  Math.cos(frame * 0.11) * 0.3;
// Totale amplitude: ~1px verticaal
```

Identiek aan de SKILL standaard shake (sectie 1, "Subtiele Shake").

#### Slide In van Boven (0.4s)

```tsx
const M7_SLIDE_FRAMES = 12; // 0.4s bij 30fps

const slideInY = interpolate(
  frame,
  [0, M7_SLIDE_FRAMES],
  [-cardHeight - 400, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

Kaart start volledig boven het scherm (negatieve Y) en schuift naar rustpositie.

#### Slide Out naar Beneden (0.4s)

```tsx
const slideOutY = interpolate(
  frame,
  [slideOutStart, duration],
  [0, height],  // naar onder het scherm
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

Kaart schuift naar beneden buiten beeld. Zelfde richting als de zwaartekracht (natuurlijk aanvoelend).

#### Gecombineerde Transform

```tsx
transform: [
  `translateY(${translateY}px)`,   // Slide in/out
  `translateX(${shakeX}px)`,       // Shake horizontaal
  `translateY(${shakeY}px)`,       // Shake verticaal
].join(" ")
```

Geen scale, geen rotation. Puur verticale slide + subtiele shake.

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Slide in van boven | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Slide out naar beneden | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Neon glow puls | sinusgolf | `Math.sin(frame * 0.06)` |
| Shake | sinusgolf (2 lagen) | Zie shake sectie |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M7_SLIDE_FRAMES | 12 frames (0.4s) | Slide in en slide out duur |
| Hold | 90 frames (3s) | Video speelt 3 seconden |
| Totaal | 114 frames (3.8s) | Slide in + hold + slide out |
| Kaart breedte | width * 0.2 | ~20% van scherm |
| Aspect ratio | 9:16 (portrait) | Verticaal kader |

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Slide in | 0-12 | 0.4s | Kaart schuift van boven naar rustpositie |
| Hold + video speelt | 12-102 | 3s | Video speelt af, shake + glow actief |
| Slide out | 102-114 | 0.4s | Kaart schuift naar beneden uit beeld |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Slide in | Swipe woosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` | Bij startFrame |
| Slide out | Swipe woosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` | startFrame + duration - 12 |

Twee verschillende whoosh sounds voor in/out variatie (zelfde paar als design-showcase type). Geen geluid tijdens de hold, de video zelf is gedempt. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

```tsx
{/* Slide in woosh */}
<Sequence from={props.m7StartFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_WOOSH_IN)} volume={0.25} />
</Sequence>
{/* Slide out woosh */}
<Sequence from={props.m7StartFrame + props.m7DurationFrames - M7_SLIDE_FRAMES} durationInFrames={20}>
  <Audio src={staticFile(SFX_WOOSH_OUT)} volume={0.25} />
</Sequence>
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Badge achtergrond | Lavender | #f1d9ff |
| Titel tekst | Dark Purple | #1b073d |
| Titel text-stroke | Dark Purple | #1b073d |
| Video kader rand | Purple | #6b3fb9 |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m7Enabled: z.boolean(),
m7VideoSrc: z.string(),
m7Title: z.string(),
m7StartFrame: z.number(),
m7DurationFrames: z.number(),
```

Video bron, titel, timing en aan/uit zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met design-showcase type

| Aspect | video-card | design-showcase |
|--------|-----------|-----------------|
| Inhoud | Afspelende video (muted) | Statische afbeelding |
| Orientatie | Verticaal (9:16 portrait) | Horizontaal (~4:3) |
| Breedte | 20% scherm | ~31% scherm |
| Titel | Lavender badge boven kader | Gele datum badge rechtsboven |
| Titel stijl | ExtraBold Italic, ALL CAPS, emoji split | ExtraBold, gewone tekst |
| In-animatie | Slide van boven (inOut cubic) | Swipe van links (inOut cubic) |
| Uit-animatie | Slide naar beneden | Swipe naar rechts |
| Shake | SKILL standaard (~1.5px) | Wobbly shake (~8px) |
| Audio | Geen (video muted) | Geen |

**TRANSITIE:** Slide in van boven + slide out naar beneden (inOut cubic, 0.4s). Geen scale, geen rotation. Video speelt af tijdens volledige zichtbaarheid. Continu shake + neon glow puls.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (VideoCard component)

**REGISTRATIE:** Moment 7 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: insta-photo-card

**WANNEER:** Foto van een persoon of evenement wordt getoond met hun Instagram handle en naam. Variant op het design-showcase type maar met typewriter Instagram badge, Lottie pijl, en persoonsnaam. Gebruikt voor shout-outs, credits, of het tonen van werk van anderen.

**LAYOUT:** Floating kaart linksonder het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: bottom 5%, left 5%
Kaart breedte: 1197px (~31% van 3840px)
Kaart hoogte: 898px (~42% van 2160px)
transformOrigin: "bottom left"
```

Zelfde kaartformaat als design-showcase type.

**STRUCTUUR:**

```
                                ┌────────────────────┐
                                │ 📷 @pinktree...    │  ← IG badge + typewriter handle
┌───────────────────────────────┴────────────────────┤
│                                                    │  ← Pijl + naam langs
│                                                    │     rechterrand
│          Foto (objectFit: cover)                   │  ← ⟵ "Paula Ardron-Gemmell"
│                                                    │
│                                                    │
└────────────────────────────────────────────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Foto Kader

Identiek aan design-showcase type: afbeelding in kader met paarse rand en 3-laags neon glow.

```tsx
width: 1197
height: 898
border: `8px solid ${BRAND.colors.primary.purple}`  // #6b3fb9
borderRadius: 20
overflow: "hidden"
```

**Neon glow (pulserend, 3 lagen + drop shadow):**
```tsx
const glowOpacity = interpolate(
  Math.sin(frame * 0.06),
  [-1, 1],
  [0.5, 0.85],
);

boxShadow: [
  `0 0 30px rgba(107, 63, 185, ${glowOpacity})`,
  `0 0 80px rgba(107, 63, 185, ${glowOpacity * 0.5})`,
  `0 0 140px rgba(107, 63, 185, ${glowOpacity * 0.25})`,
  "0 12px 40px rgba(0, 0, 0, 0.3)",
].join(", ")
```

Identiek aan design-showcase type.

#### Instagram Badge (rechtsboven, typewriter)

Gele badge met Instagram icoon en handle die letter voor letter verschijnt. Badge zelf verschijnt met een snelle opacity fade na de pop-in.

```tsx
// Badge container
position: "absolute"
top: -18
right: -12
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
color: BRAND.colors.secondary.darkPurple         // #1b073d
padding: "20px 48px"
borderRadius: 12
fontFamily: "Rethink Sans, sans-serif"
fontSize: 104
fontWeight: 800
boxShadow: "0 4px 12px rgba(0, 0, 0, 0.15)"
whiteSpace: "nowrap"
display: "flex"
alignItems: "center"
gap: 24
```

Zelfde styling als design-showcase datum badge, maar met IG icoon + typewriter tekst.

**Badge fade-in:**
```tsx
const badgeOpacity = interpolate(
  frame,
  [M8_POP_IN_FRAMES, M8_POP_IN_FRAMES + 3],
  [0, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
// 3 frames fade (0.1s), begint direct na pop-in settle
```

**Instagram icoon:** SVG met radial gradient (zelfde als in design-showcase), 80x80px. Gradient ID `ig-m8-grad` (uniek om SVG conflicten te voorkomen).

**Typewriter effect:**
```tsx
const M8_TYPE_START = 9;     // 0.3s na pop-in
const M8_TYPE_DURATION = 30; // ~1s om volledige handle te typen

const typeStart = M8_POP_IN_FRAMES + M8_TYPE_START;
const charsPerFrame = handle.length / M8_TYPE_DURATION;
const typedChars = Math.min(
  handle.length,
  Math.max(0, Math.floor((frame - typeStart) * charsPerFrame)),
);
const displayHandle = handle.slice(0, typedChars);
```

Handle verschijnt karakter voor karakter. Geen blinkende cursor (anders dan google-search-card type).

#### Naam Label + Lottie Pijl (rechterrand)

Verschijnt na de badge, dicht langs de rechterrand van het kader. Lottie pijl wijst naar links (naar de foto), naam staat rechts ernaast.

```tsx
const M8_NAME_START = 18; // 0.6s na entry, na badge is gesetteld

// Positie: dicht langs rechterrand van het kader
position: "absolute"
right: -24
top: "35%"
transform: `translateX(100%) scale(${nameSpring})`
transformOrigin: "left center"
paddingLeft: 12  // 12px afstand tot kaderrand
```

**Naam spring pop-in:**
```tsx
const nameSpring = spring({
  frame: frame - M8_NAME_START,
  fps,
  config: { damping: 10, mass: 0.4, stiffness: 160 },
});
```

**Lottie pijl:**
```tsx
// Asset: animations/arrows/arrow-pointing.json
width: 100
height: 100
transform: `rotate(180deg) scale(${arrowPulse})`  // 180deg = wijst naar links

// Pulserende scale
const arrowPulse = 1 + Math.sin((frame - M8_NAME_START) * 0.15) * 0.06;
// Amplitude: 6%, frequentie 0.15. Trekt aandacht naar de naam.
```

**Naam tekst:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 72
fontWeight: 800  // ExtraBold
fontStyle: "italic"
color: BRAND.colors.neutral.white  // #ffffff
textShadow: "0 4px 16px rgba(0, 0, 0, 0.5)"
whiteSpace: "nowrap"
```

#### Wobbly Shake (continu)

Identiek aan design-showcase type: drie overlappende sinusgolven per as.

```tsx
const wobbleX =
  Math.sin(frame * 0.15) * 4 +
  Math.sin(frame * 0.23) * 2.5 +
  Math.sin(frame * 0.37) * 1.5;
// Totale amplitude: ~8px horizontaal

const wobbleY =
  Math.cos(frame * 0.12) * 2 +
  Math.cos(frame * 0.19) * 1.5;
// Totale amplitude: ~3.5px verticaal

const wobbleRotate =
  Math.sin(frame * 0.1) * 0.4 +
  Math.sin(frame * 0.18) * 0.25;
// Totale amplitude: ~0.65 graden
```

#### Breathe (continu)

```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.008;
// Amplitude: 0.8%. Consistent met design-showcase type.
```

#### Pop In (spring, 0.3s)

```tsx
const M8_POP_IN_FRAMES = 9;

const popIn = spring({
  frame,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});
// Schaalt van 0 -> ~1.1 -> 1.0 (natuurlijke overshoot)
```

Identieke spring config als DesignPopCard (M2).

#### Pop Out (3-keyframe, 0.3s)

```tsx
const M8_POP_OUT_FRAMES = 9;
const exitStart = duration - M8_POP_OUT_FRAMES;

const popOut = interpolate(
  frame,
  [exitStart, exitStart + 3, duration],
  [1, 1.05, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);
// 9 frames: 3 frames overshoot naar 1.05, dan naar 0
```

#### Gecombineerde Transform

```tsx
transform: [
  `translateX(${wobbleX}px)`,
  `translateY(${wobbleY}px)`,
  `rotate(${wobbleRotate}deg)`,
  `scale(${scale * breathe})`,
].join(" ")
transformOrigin: "bottom left"
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Pop out | in cubic (3-keyframe) | `Easing.in(Easing.cubic)` |
| Badge fade-in | linear (3 frames) | `interpolate` zonder easing |
| Naam pop-in | spring | `{ damping: 10, mass: 0.4, stiffness: 160 }` |
| Wobble | sinusgolf (3 lagen) | Zie wobble sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Glow puls | sinusgolf | `Math.sin(frame * 0.06)` |
| Arrow puls | sinusgolf | `Math.sin(frame * 0.15)` |

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Kaart pop in | 0-~25 | ~0.8s | Spring bounce 0 -> 1.1 -> 1.0 |
| Badge fade in | 9-12 | 0.1s | Gele badge verschijnt (opacity 0 -> 1) |
| Handle typewriter | 18-48 | ~1s | Instagram handle typt letter voor letter |
| Naam + pijl pop in | 18-~30 | ~0.4s | Spring pop langs rechterrand |
| Hold met wobble | ~48-111 | ~2.1s | Alles zichtbaar, wobble + breathe + glow |
| Pop out | 111-120 | 0.3s | Alles tegelijk scale 1 -> 1.05 -> 0 |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M8_POP_IN_FRAMES | 9 frames (0.3s) | Pop-in duur |
| M8_POP_OUT_FRAMES | 9 frames (0.3s) | Pop-out duur |
| M8_TYPE_START | 9 frames (0.3s) | Delay na pop-in voor typewriter start |
| M8_TYPE_DURATION | 30 frames (~1s) | Typewriter duur |
| M8_NAME_START | 18 frames (0.6s) | Naam + pijl verschijnt |
| Standaard duur | 120 frames (4s) | Configureerbaar via schema |
| Kaart breedte | 1197px | ~31% van 3840px |
| Kaart hoogte | 898px | ~42% van 2160px |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Pop in | Click open | 0.25 | `sound-effects/universfield-computer-mouse-click-351398.mp3` | Bij startFrame |
| Typewriter | Keyboard typing | 0.1 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | startFrame + 18, duur 35 frames |
| Pop out | Click out | 0.25 | `sound-effects/universfield-computer-mouse-click-352734.mp3` | startFrame + duration - 9 |

Click sounds (niet wooshes of pops) passen bij het "foto openen/sluiten" karakter. Typing SFX op laag volume (0.1) voor subtiliteit. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

```tsx
{/* Click in */}
<Sequence from={props.m8StartFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_CLICK_OPEN)} volume={0.25} />
</Sequence>
{/* Typewriter for handle */}
<Sequence from={props.m8StartFrame + M8_POP_IN_FRAMES + M8_TYPE_START} durationInFrames={M8_TYPE_DURATION + 5}>
  <Audio src={staticFile(SFX_TYPING)} volume={0.1} />
</Sequence>
{/* Click out */}
<Sequence from={props.m8StartFrame + props.m8DurationFrames - M8_POP_OUT_FRAMES} durationInFrames={20}>
  <Audio src={staticFile(SFX_CLICK_OUT)} volume={0.25} />
</Sequence>
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Kaart rand | Purple | #6b3fb9 |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |
| Badge achtergrond | Yellow | #ffdb5a |
| Badge tekst | Dark Purple | #1b073d |
| Badge schaduw | Zwart 15% | rgba(0, 0, 0, 0.15) |
| IG icoon gradient | Platform kleuren | #fdf497 -> #fd5949 -> #d6249f -> #285AEB |
| Naam tekst | White | #ffffff |
| Naam text-shadow | Zwart 50% | rgba(0, 0, 0, 0.5) |

#### Assets

| Asset | Pad | Beschrijving |
|-------|-----|-------------|
| Arrow pointing | `public/animations/arrows/arrow-pointing.json` | Lottie pijl animatie, geroteerd 180deg om naar links te wijzen |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m8Enabled: z.boolean(),
m8ImageSrc: z.string(),
m8Handle: z.string(),
m8Name: z.string(),
m8StartFrame: z.number(),
m8DurationFrames: z.number(),
```

Foto, Instagram handle, persoonsnaam, timing en aan/uit zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met design-showcase type

| Aspect | insta-photo-card | design-showcase |
|--------|-----------------|-----------------|
| Positie | bottom left 5% (vast) | bottom left 5% (vast) |
| Badge inhoud | IG icoon + typewriter handle | Datum tekst (statisch) |
| Naam label | Ja (Lottie pijl + naam langs rechterrand) | Nee |
| In-animatie | Pop (spring) | Swipe van links |
| Uit-animatie | Pop (3-keyframe) | Swipe naar rechts |
| Meerdere kaarten | Nee (enkele foto) | Ja (sequentieel) |
| Typewriter | Ja (handle) | Nee |
| Sound | Clicks + typing | Wooshes |

#### Verschil met design-pop-card type (M2)

| Aspect | insta-photo-card | design-pop-card |
|--------|-----------------|-----------------|
| Positie | bottom left 5% | bottom right 5% |
| Badge | IG icoon + typewriter handle | IG icoon + statische handle |
| Naam label | Ja (pijl + naam) | Nee |
| Wobble | Ja (3-laags) | Ja (3-laags, identiek) |
| Pop config | Identiek | Identiek |
| Kaart formaat | 1197x898 | 1077x970 |

**TRANSITIE:** Pop in met spring bounce (0.3s) + pop out 3-keyframe (0.3s). Badge verschijnt na pop-in met typewriter handle. Naam + Lottie pijl verschijnt langs rechterrand na badge settle. Continu wobbly shake + breathe + neon glow puls.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (InstaPhotoCard component)

**REGISTRATIE:** Moment 8 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: event-list-panel

**WANNEER:** Een opsomming van evenementen, workshops, locaties, of andere sequentiele items die een voor een verschijnen met een teleprompter-scroll effect. Variant op het materialenlijst type maar met verticale entry-animatie (items swipen van boven naar beneden) en een scrollende lijst i.p.v. statische items.

**LAYOUT:** Side panel links (~35% scherm), video schuift naar rechts. Fullscreen hoogte. Identiek aan materialenlijst type.

```
Panel breedte: 1360px (~35% van 3840px)
Video shift: 360px naar rechts
Video scale: 1.08x (voorkomt zwarte randen)
```

Video schuift naar rechts om ruimte te maken, synced met panel slide via `VideoWithShift` component.

**STRUCTUUR:**

```
┌──────────────────────────────────┐
│  [frosted glass + gradient]      │
│  [particles]                     │
│                                  │
│  ┌─────────────────────────────┐ │
│  │ BALLOON WORKSHOPS & EVENTS │ │  ← Geel titelblok, ExtraBold + text-stroke
│  └─────────────────────────────┘ │
│  ━━━━━━━━━━━━                    │  ← Gele accent line
│                                  │
│  ▐████ Nozzle Up Convention      │  ← Wipe-reveal, swiped in van boven
│  ▐████ MBP Exams                 │  ← Volgt met stagger
│  ▐████ IBC Convention            │  ← Oudere entries scrollen omhoog + fade
│  ▐████ NABAS Training Days       │
│  ▐████ BAPIA Training Days       │
│  ▐████ & More! View Calendar     │  ← Magenta, pulserend
│                                  │
│         [STX EU logo]            │  ← Gecentreerd onderaan
└──────────────────────────────────┘
```

**BEVAT:**

#### Achtergrond (materialenlijst stijl)

Identiek aan het materialenlijst type: frosted glass + lavender gradient + particles + rechterrand schaduw.

**Frosted glass:**
```tsx
backdropFilter: "blur(50px) brightness(1.1) saturate(1.2)"
WebkitBackdropFilter: "blur(50px) brightness(1.1) saturate(1.2)"
```

**Gradient overlay:** Drie lagen (purple glow linksboven, magenta glow linksonder, lavender lineaire gradient). Exact als materialenlijst.

**Rechterrand schaduw:** 60px breed (2x van 1080p 30px).

**Particles:**
```tsx
<Particles count={20} color={BRAND.colors.primary.purple} maxOpacity={0.2} seed={88} speedMultiplier={2.5} />
```

#### Titel (geel blok, ExtraBold + text-stroke)

```tsx
// Geel blok
display: "inline-block"
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "16px 56px"

// Titel tekst
fontFamily: "Rethink Sans, sans-serif"
fontSize: 84
fontWeight: 800
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 5
WebkitTextStroke: `2px ${BRAND.colors.secondary.darkPurple}`  // extra bold effect
```

**Titel entrance:** Spring animatie met fade + slide van boven:
```tsx
const titleSpring = spring({
  frame: frame - M10_FADE,
  fps,
  config: { damping: 14, mass: 0.5, stiffness: 120 },
});
const titleY = interpolate(titleSpring, [0, 1], [-60, 0]);
const titleOpacity = interpolate(titleSpring, [0, 0.5], [0, 1], {
  extrapolateRight: "clamp",
});
```

#### Accent Line (geel, expanderend)

```tsx
// Timing: start na M10_FADE + 8 frames, duur 20 frames
// Easing: Easing.out(Easing.cubic)
// Kleur: BRAND.colors.secondary.yellow
// Hoogte: 6px
// maxWidth: 600px
// marginTop: 16px
```

#### Event Entries (teleprompter stijl met wipe-reveal)

Elke entry is een slot van 150px hoogte. Items verschijnen een voor een met een verticale swipe van boven. Wanneer meer dan 3 items zichtbaar zijn, scrollen oudere items omhoog en faden uit.

**Entry swipe in (van boven):**
```tsx
const M10_ENTRY_SLIDE_FRAMES = 10; // 0.33s per entry

const entryProgress = interpolate(
  frame,
  [entryFrame, entryFrame + M10_ENTRY_SLIDE_FRAMES],
  [0, 1],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);
// translateY: (1 - entryProgress) * -80px (schuift van boven naar positie)
```

**Teleprompter scroll:**
```tsx
const M10_VISIBLE_SLOTS = 3;

// Aantal entries dat na dit item verscheen
const entriesAfterThis = events.filter(
  (e) => e.relativeFrame > entryFrame && frame >= e.relativeFrame,
).length;
const scrollOffset = entriesAfterThis * SLOT_HEIGHT * 0.6;

// Fade out oudste entries
const fadeStart = Math.max(0, entriesAfterThis - M10_VISIBLE_SLOTS + 1);
const entryOpacity = fadeStart > 0
  ? interpolate(fadeStart, [0, 2], [1, 0], { ... })
  : 1;
```

Oudere entries schuiven langzaam omhoog (scrollOffset) en faden uit wanneer meer dan 3 entries na hen zijn verschenen.

**Wipe-reveal bar (per entry):**
Identiek mechanisme als materialenlijst type: bar verschijnt (4 frames), recede naar links (28 frames), tekst wordt onthuld via clipPath.

```tsx
// Bar appear: 4 frames, linear
// Bar recede: 28 frames, Easing.inOut(Easing.cubic)
// Text reveal via: clipPath: `inset(0 ${100 - textReveal}% 0 0)`
// 4% accent bar blijft over
// Glow tijdens recede: boxShadow: `0 0 16px ${barColor}80`
```

**Bar kleuren (alterneren + magenta voor laatste):**
```tsx
const barColor = isLastEntry
  ? BRAND.colors.primary.magenta   // #cd0b5c (laatste entry)
  : i % 2 === 0
    ? BRAND.colors.secondary.yellow  // #ffdb5a (even)
    : BRAND.colors.primary.purple;   // #6b3fb9 (oneven)
```

#### Laatste Entry (CTA highlight)

De laatste entry ("& More! View Calendar") krijgt speciale behandeling:
- Tekst kleur: magenta (`BRAND.colors.primary.magenta` / #cd0b5c)
- Wipe bar kleur: magenta
- Na volledig onthuld: pulserende scale animatie

```tsx
// Pulsating scale na wipe-reveal compleet
transform: isLastEntry && barRecede >= 1
  ? `scale(${1 + Math.sin((frame - entryFrame - 32) * 0.12) * 0.04})`
  : undefined
transformOrigin: "left center"
// Amplitude: 4%, frequentie 0.12
```

#### Entry Tekst Stijl

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 94
fontWeight: 800  // ExtraBold
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple  // #1b073d (of magenta voor laatste)
```

#### Logo (onderaan panel)

Sempertex Europe logo, gecentreerd aan de onderkant.

```tsx
<Img
  src={staticFile("logos/STX EU.png")}
  style={{ height: 140, objectFit: "contain" }}
/>
// Container: display flex, justifyContent center, paddingTop 40
```

#### Staggered Exit (bottom-to-top)

Alle entries swipen snel naar links uit beeld, gestaffeld van onder naar boven (0.1s per entry). Titel verdwijnt als laatste met het panel slide.

```tsx
const M10_EXIT_STAGGER = 3; // 0.1s per entry

// Exit index: bottom entries exit first
const exitIndex = events.length - 1 - i;
const entryExitStart = exitStart + exitIndex * M10_EXIT_STAGGER;

const exitX = interpolate(
  frame,
  [entryExitStart, entryExitStart + 8],
  [0, -M10_PANEL_WIDTH],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);
```

#### Video Shift (synced met panel)

Via `VideoWithShift` wrapper component. Video schuift naar rechts en schaalt op wanneer panel zichtbaar is.

```tsx
// In VideoWithShift component:
shiftX = interpolate(
  frame,
  [m10Start, m10Start + M10_FADE, m10Start + m10Duration - M10_FADE, m10Start + m10Duration],
  [0, M10_VIDEO_SHIFT, M10_VIDEO_SHIFT, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);
shiftScale = interpolate(
  frame,
  [m10Start, m10Start + M10_FADE, m10Start + m10Duration - M10_FADE, m10Start + m10Duration],
  [1, 1.08, 1.08, 1],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) },
);
```

#### Shake (continu, SKILL standaard)

```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
```

Identiek aan de SKILL standaard shake (sectie 1).

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Panel slide in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Video shift in/uit | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Titel verschijning | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |
| Accent line expand | out cubic | `Easing.out(Easing.cubic)` |
| Entry swipe in | out cubic | `Easing.out(Easing.cubic)` |
| Wipe bar recede | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Entry staggered exit | in cubic | `Easing.in(Easing.cubic)` |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M10_FADE | 12 frames (0.4s) | Panel slide in/uit |
| M10_PANEL_WIDTH | 1360px | ~35% van 3840px |
| M10_VIDEO_SHIFT | 360px | Video verschuiving naar rechts |
| M10_ENTRY_SLIDE_FRAMES | 10 frames (0.33s) | Per entry swipe-in |
| M10_EXIT_STAGGER | 3 frames (0.1s) | Tussen elke entry exit |
| M10_VISIBLE_SLOTS | 3 | Max zichtbare entries voor scroll |
| SLOT_HEIGHT | 150px | Hoogte per entry slot |
| Entry stagger | 36 frames (~1.2s) | Tijd tussen entries |
| Wipe bar appear | 4 frames | Bar verschijnt |
| Wipe bar recede | 28 frames | Bar krimpt, tekst onthuld |
| Standaard duur | 291 frames (~9.7s) | Configureerbaar via schema |

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Panel slide in + video shift | 0-12 | 0.4s | Panel schuift van links, video naar rechts |
| Titel spring | 12-~30 | ~0.6s | Titel fade + slide van boven |
| Accent line | 20-40 | 0.67s | Gele lijn expandeert |
| Entry 1: Nozzle Up Convention | 30 | wipe 32f | Swipe in + wipe reveal (geel) |
| Entry 2: MBP Exams | 66 | wipe 32f | Swipe in + wipe reveal (paars) |
| Entry 3: IBC Convention | 102 | wipe 32f | Swipe in, entries 1 begint te scrollen |
| Entry 4: NABAS Training Days | 138 | wipe 32f | Scroll + fade op oudste entries |
| Entry 5: BAPIA Training Days | 174 | wipe 32f | Teleprompter scroll door |
| Entry 6: & More! View Calendar | 210 | wipe 32f | Magenta bar + pulsating text na reveal |
| Hold | 242-~270 | ~1s | Extra hold na laatste entry (0.5s) |
| Staggered exit | ~270-279 | ~0.3s | Entries swipen naar links (bottom-to-top) |
| Panel slide out + video terug | 279-291 | 0.4s | Panel schuift weg, video terug |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Panel slide in | Soft woosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` | Bij startFrame |
| Entry 1-5 verschijnt | Subtle tick | 0.08 | `sound-effects/dragon-studio-clean-minimal-pop-467466.mp3` | Per entry relativeFrame |
| Laatste entry (CTA) | Ding | 0.2 | `sound-effects/koiroylers-slow-ding-354125.mp3` | relativeFrame laatste entry |
| Staggered exit | Soft woosh | 0.21 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` | startFrame + duration - 12 |

Ticks zijn zacht (0.08) om niet te overweldigen bij 5 entries. De ding op de laatste entry is luider (0.2) als accent/afsluiter. Exit woosh bewust 30% stiller (0.21 i.p.v. 0.3) om niet te abrupt te zijn.

```tsx
{/* Tick per entry */}
{props.m10Events.map((event, i) => (
  <Sequence
    key={`m10-tick-${i}`}
    from={props.m10StartFrame + event.relativeFrame}
    durationInFrames={15}
  >
    <Audio
      src={staticFile(i === props.m10Events.length - 1 ? SFX_DING : SFX_TICK)}
      volume={i === props.m10Events.length - 1 ? 0.2 : 0.08}
    />
  </Sequence>
))}
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Panel achtergrond | Lavender gradient | #f1d9ff |
| Titel blok | Yellow | #ffdb5a |
| Titel tekst + text-stroke | Dark Purple | #1b073d |
| Accent line | Yellow | #ffdb5a |
| Wipe bar (even entries) | Yellow | #ffdb5a |
| Wipe bar (oneven entries) | Purple | #6b3fb9 |
| Wipe bar (laatste entry) | Magenta | #cd0b5c |
| Entry tekst | Dark Purple | #1b073d |
| Laatste entry tekst | Magenta | #cd0b5c |
| Particles | Purple | #6b3fb9 |
| Rechterrand schaduw | Zwart 12% | rgba(0,0,0,0.12) |

#### Assets

| Asset | Pad | Beschrijving |
|-------|-----|-------------|
| STX EU logo | `public/logos/STX EU.png` | Sempertex Europe logo, gecentreerd onderaan panel |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m10Enabled: z.boolean(),
m10Title: z.string(),
m10Events: z.array(z.object({
  name: z.string(),
  relativeFrame: z.number(),
})),
m10StartFrame: z.number(),
m10DurationFrames: z.number(),
```

Titel, events (naam + timing per entry), start en duur zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met materialenlijst type

| Aspect | event-list-panel | materialenlijst |
|--------|-----------------|-----------------|
| Canvas | 3840x2160 (4K) | 1920x1080 |
| Panel breedte | 1360px (~35%) | 680px (~35%) |
| Entry beweging | Verticaal (swipe van boven) | Statisch (wipe-reveal alleen) |
| Teleprompter scroll | Ja (oudere entries scrollen omhoog + fade) | Nee (alle items statisch) |
| Laatste entry | Magenta + pulsating scale | Geen speciale behandeling |
| Logo | Ja (STX EU onderaan) | Nee |
| Tekst stijl | ExtraBold Italic 94px | ExtraBold/Bold, twee groottes |
| Titel | ExtraBold + WebkitTextStroke | ExtraBold (geen text-stroke) |
| Exit | Staggered per entry (bottom-to-top) | Panel slide als geheel |
| Video shift | Via VideoWithShift component | Direct op video transform |

**TRANSITIE:** Panel schuift van links (inOut cubic, 0.4s), video schuift naar rechts (synced). Entries verschijnen een voor een met verticale swipe + wipe-reveal. Teleprompter scroll voor oudere entries. Staggered exit per entry (bottom-to-top, 0.1s stagger). Panel schuift als laatste weg.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (EventListPanel + VideoWithShift componenten)

**REGISTRATIE:** Moment 10 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: thought-bubble-tip-right

**WANNEER:** Gespiegelde versie van thought-bubble-tip. Gebruikt wanneer de linkerhelft van het scherm bezet is door de spreker, of als visuele afwisseling na een eerder thought-bubble-tip moment aan de linkerkant. Vraag aan de kijker, interactie trigger.

**LAYOUT:** Floating kaart rechtsonder het scherm met een thought bubble linksboven van het kader (gespiegeld t.o.v. thought-bubble-tip). Video blijft volledig zichtbaar erachter.

```
Positie tekstvak: bottom 10%, right 5%
transformOrigin: "bottom right"
Thought bubble: top -300px, right 700px (ver naar links, aan linkerrand van kader)
Bubble scaleX(-1) voor horizontale mirror
```

De spreker is links volledig zichtbaar.

**STRUCTUUR:**

```
┌─────────────┐
│   💭  ?     │  ← Thought bubble PNG (horizontaal gespiegeld) + vraagteken
└─────────────┘
    ↑ Aan linkerrand van kader, gespiegeld

                ┌──────────────────────────────┐
                │  ┌────────────────┐          │
                │  │ WHAT ABOUT YOU?│          │  ← Geel kader, ALL CAPS, ExtraBold Italic
                │  └────────────────┘          │
                │  ━━━━━━━━━━━━━━━━━━━━━━━━━   │
                │                              │
                │  We'd love to know what your │
                │  first design was! Let us    │
                │  know in the comments 👇     │  ← Emoji apart (niet italic)
                │                              │
                └──────────────────────────────┘
                  ↑ Lavender achtergrond + paarse glow
```

**BEVAT:**

#### Thought Bubble (linksboven van kader, gespiegeld)

PNG asset horizontaal gespiegeld via `scaleX(-1)`. Gepositioneerd ver naar links (`right: 700`) zodat de bubble aan de linkerrand van het tekstvak zweeft.

```tsx
position: "absolute"
top: -300
right: 700   // ver naar links, aan de rand van het kader
width: 420
height: 420
transform: `scale(${bubbleScale}) scaleX(-1)`  // horizontaal gespiegeld
transformOrigin: "bottom left"
```

**Vraagteken (un-mirrored):**
```tsx
transform: `translate(-50%, -75%) scaleX(-1) scale(${qmSpring})`
// -75% = hoger gepositioneerd dan origineel (-55%)
// scaleX(-1) = un-mirror zodat "?" leesbaar blijft
fontFamily: "Rethink Sans, sans-serif"
fontSize: 156
fontWeight: 800
color: BRAND.colors.primary.purple  // #6b3fb9
```

#### Tekstvak

Identiek aan thought-bubble-tip type. Lavender achtergrond, gele titel badge, paarse underline.

```tsx
backgroundColor: BRAND.colors.primary.lavender  // #f1d9ff
padding: "58px 67px"
maxWidth: 1152
borderRadius: 29
```

#### Titel

```tsx
// "WHAT ABOUT YOU?" in geel kader
fontSize: 86
fontWeight: 800
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple
WebkitTextStroke: `2px ${BRAND.colors.secondary.darkPurple}`
```

#### Body Tekst + Emoji Splitsing

Emoji's worden apart gerenderd om italic styling te voorkomen.

```tsx
// Tekst zonder emoji
const textOnly = text.replace(/\p{Emoji_Presentation}/gu, "");
const emojiOnly = text.match(/\p{Emoji_Presentation}/gu)?.join("") ?? "";

// Body tekst
fontSize: 67, fontWeight: 700, color: BRAND.colors.neutral.black

// Emoji apart
{emojiOnly && <span style={{ fontSize: 80 }}>{emojiOnly}</span>}
```

#### Wobble (gespiegeld)

Rotatie is gespiegeld (negatief) t.o.v. thought-bubble-tip zodat de beweging natuurlijk aanvoelt vanuit de rechterhoek.

```tsx
transform: [
  `scale(${mainScale * breathe})`,
  `translateY(${wobbleY}px)`,
  `rotate(${-wobbleRotation}deg)`,  // negatief = gespiegelde wobble
].join(" ")
transformOrigin: "bottom right"
```

#### Easing Curves

Identiek aan thought-bubble-tip type:

| Context | Easing | Code |
|---------|--------|------|
| Tekstvak pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Pop out | in cubic (3-keyframe) | `Easing.in(Easing.cubic)` |
| Thought bubble pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Vraagteken pop in | spring | `{ damping: 12, mass: 0.3, stiffness: 160 }` |
| Wobble rotatie | sinusgolf (2 lagen) | Negatief van origineel |
| Wobble translateY | sinusgolf (2 lagen) | Identiek aan origineel |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Glow puls | sinusgolf | `Math.sin(frame * 0.06)` |

#### Timing

Identiek aan thought-bubble-tip type:

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M5_EXIT_FRAMES | 9 frames (0.3s) | Pop-out duur |
| M5_BUBBLE_START | 9 frames (0.3s) | Thought bubble verschijnt na box pop-in |
| M5_QM_START | 15 frames (0.5s) | Vraagteken verschijnt na bubble |
| Standaard duur | 180 frames (6s) | Configureerbaar via schema |

#### Sound Design

Identiek aan thought-bubble-tip type:

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Tekstvak pop in | Soft pop | 0.2 | `sound-effects/soundreality-pop-423717.mp3` |
| Thought bubble pop | Pop | 0.15 | `sound-effects/dragon-studio-pop-402324.mp3` |
| Pop out | Soft pop | 0.2 | `sound-effects/soundreality-pop-423717.mp3` |

#### Kleuren Samenvatting

Identiek aan thought-bubble-tip type:

| Element | Kleur | HEX |
|---------|-------|-----|
| Tekstvak achtergrond | Lavender | #f1d9ff |
| Titel kader achtergrond | Yellow | #ffdb5a |
| Titel tekst + text-stroke | Dark Purple | #1b073d |
| Paarse lijn | Purple | #6b3fb9 |
| Body tekst | Black | #000000 |
| Vraagteken | Purple | #6b3fb9 |
| Glow kleur | Purple | rgb(107, 63, 185) |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m11Enabled: z.boolean(),
m11Text: z.string(),
m11StartFrame: z.number(),
m11DurationFrames: z.number(),
```

#### Verschil met thought-bubble-tip type

| Aspect | thought-bubble-tip-right | thought-bubble-tip |
|--------|-------------------------|-------------------|
| Positie | bottom 10%, right 5% | bottom 10%, left 5% |
| transformOrigin | bottom right | bottom left |
| Thought bubble positie | right 700 (linkerrand kader) | left 20 (linkerrand kader) |
| Bubble mirror | scaleX(-1) | geen mirror |
| Vraagteken Y-offset | -75% (hoger) | -55% |
| Wobble rotatie | Negatief (gespiegeld) | Positief |
| Emoji | Ja (apart gerenderd, niet italic) | Nee |
| Titel | "WHAT ABOUT YOU?" | "QUESTION" |

**TRANSITIE:** Spring pop in (0.3s) met thought bubble die apart verschijnt (gespiegeld, 0.3s na box). Continu wobble (gespiegeld) + breathe + glow puls tijdens hold. Pop out alles tegelijk (0.3s). Video blijft volledig zichtbaar.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (ThoughtBubbleTipRight component)

**REGISTRATIE:** Moment 11 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: titled-photo-card

**WANNEER:** Een foto wordt getoond met een korte titel/label erboven. Simpelste foto-overlay variant: geen Instagram handle, geen typewriter, geen pijl. Gebruikt voor throwbacks, simpele foto-referenties, of wanneer de context al duidelijk is uit de spraak.

**LAYOUT:** Floating kaart linksonder het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: bottom 5%, left 5%
Kaart breedte: 1000px (~26% van 3840px)
Kaart hoogte: 1300px (~60% van 2160px)
Aspect ratio: ~3:4 (portrait, langwerpig in de hoogte)
transformOrigin: "bottom left"
```

Portrait orientatie om designs en personen in volle lengte te tonen.

**STRUCTUUR:**

```
┌──────────────┐
│  5 years ago │  ← Gele badge boven kader
└──────────────┘
┌──────────────┐
│              │
│              │
│    Foto      │  ← Portrait (3:4), objectFit cover
│   (tall)     │
│              │
│              │
└──────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Titel Badge (boven kader)

Geel blok met titel, los boven het fotokader.

```tsx
display: "inline-block"
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "20px 48px"
borderRadius: 12
marginBottom: 24
boxShadow: "0 4px 12px rgba(0, 0, 0, 0.15)"
```

**Titel tekst:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 104
fontWeight: 700  // Bold
color: BRAND.colors.secondary.darkPurple  // #1b073d
whiteSpace: "nowrap"
```

Consistent met design-showcase datum badge styling.

#### Foto Kader (portrait)

Portrait-georienteerd kader met paarse rand en 3-laags neon glow.

```tsx
width: 1000
height: 1300
border: `8px solid ${BRAND.colors.primary.purple}`  // #6b3fb9
borderRadius: 20
overflow: "hidden"
```

**Neon glow (pulserend, 3 lagen + drop shadow):**
```tsx
const glowOpacity = interpolate(
  Math.sin(frame * 0.06),
  [-1, 1],
  [0.5, 0.85],
);

boxShadow: [
  `0 0 30px rgba(107, 63, 185, ${glowOpacity})`,
  `0 0 80px rgba(107, 63, 185, ${glowOpacity * 0.5})`,
  `0 0 140px rgba(107, 63, 185, ${glowOpacity * 0.25})`,
  "0 12px 40px rgba(0, 0, 0, 0.3)",
].join(", ")
```

Identiek aan design-showcase type.

**Afbeelding:**
```tsx
<Img src={staticFile(imageSrc)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
```

#### Wobbly Shake (continu)

Identiek aan design-showcase type (3-laags sinusgolven).

```tsx
const wobbleX = Math.sin(frame * 0.15) * 4 + Math.sin(frame * 0.23) * 2.5 + Math.sin(frame * 0.37) * 1.5;
const wobbleY = Math.cos(frame * 0.12) * 2 + Math.cos(frame * 0.19) * 1.5;
const wobbleRotate = Math.sin(frame * 0.1) * 0.4 + Math.sin(frame * 0.18) * 0.25;
```

#### Breathe (continu)

```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.008;
// Amplitude: 0.8%. Consistent met design-showcase type.
```

#### Pop In (spring, 0.3s)

```tsx
const popIn = spring({
  frame,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});
```

#### Pop Out (3-keyframe, 0.3s)

```tsx
const M12_POP_OUT_FRAMES = 9;
const exitStart = duration - M12_POP_OUT_FRAMES;

const popOut = interpolate(
  frame,
  [exitStart, exitStart + 3, duration],
  [1, 1.05, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);
```

#### Gecombineerde Transform

```tsx
transform: [
  `translateX(${wobbleX}px)`,
  `translateY(${wobbleY}px)`,
  `rotate(${wobbleRotate}deg)`,
  `scale(${scale * breathe})`,
].join(" ")
transformOrigin: "bottom left"
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Pop in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Pop out | in cubic (3-keyframe) | `Easing.in(Easing.cubic)` |
| Wobble | sinusgolf (3 lagen) | Zie wobble sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Glow puls | sinusgolf | `Math.sin(frame * 0.06)` |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M12_POP_OUT_FRAMES | 9 frames (0.3s) | Pop-out duur |
| Spring settle | ~25 frames (~0.8s) | Pop-in tot rust |
| Standaard duur | 120 frames (4s) | Configureerbaar via schema |
| Kaart breedte | 1000px | ~26% van 3840px |
| Kaart hoogte | 1300px | ~60% van 2160px (portrait) |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Pop in | Click open | 0.25 | `sound-effects/universfield-computer-mouse-click-351398.mp3` |
| Pop out | Click out | 0.25 | `sound-effects/universfield-computer-mouse-click-352734.mp3` |

Click sounds passend bij het "foto openen/sluiten" karakter. Geluiden staan als `<Audio>` in `<Sequence>` elementen in de parent composition.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Badge achtergrond | Yellow | #ffdb5a |
| Badge tekst | Dark Purple | #1b073d |
| Badge schaduw | Zwart 15% | rgba(0, 0, 0, 0.15) |
| Kaart rand | Purple | #6b3fb9 |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m12Enabled: z.boolean(),
m12ImageSrc: z.string(),
m12Title: z.string(),
m12StartFrame: z.number(),
m12DurationFrames: z.number(),
```

#### Verschil met design-showcase en insta-photo-card types

| Aspect | titled-photo-card | design-showcase | insta-photo-card |
|--------|------------------|-----------------|-----------------|
| Orientatie | Portrait (1000x1300) | Landscape (1197x898) | Landscape (1197x898) |
| Badge | Titel boven kader (geel) | Datum rechtsboven (geel) | IG handle rechtsboven (geel) |
| Badge positie | Los boven | Overlapt bovenhoek | Overlapt bovenhoek |
| Typewriter | Nee | Nee | Ja (handle) |
| Naam + pijl | Nee | Nee | Ja |
| In-animatie | Pop (spring) | Swipe van links | Pop (spring) |
| Uit-animatie | Pop (3-keyframe) | Swipe naar rechts | Pop (3-keyframe) |
| Meerdere kaarten | Nee | Ja (sequentieel) | Nee |
| Complexiteit | Laag | Medium | Hoog |

**TRANSITIE:** Pop in met spring bounce (0.3s) + pop out 3-keyframe (0.3s). Continu wobbly shake + breathe + neon glow puls. Video blijft volledig zichtbaar.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (TitledPhotoCard component)

**REGISTRATIE:** Moment 12 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: cta-card

**WANNEER:** Call-to-action moment met een duidelijke boodschap + URL/website verwijzing. Twee gestapelde elementen: een tekst-kaart met gradient achtergrond en daaronder een Google zoekbalk met typewriter effect. Gebruikt om de kijker naar een specifieke pagina te leiden.

**LAYOUT:** Linkerkant van het scherm, verticaal gecentreerd. Video blijft rechts zichtbaar (geen video shift, geen panel).

```
Positie: left 5%, top 50%, translateY(-50%)
maxWidth: 40% van scherm
Twee elementen verticaal gestapeld met 40px gap
```

**STRUCTUUR:**

```
┌────────────────────────────────────┐
│                                    │
│  Don't know where to start?       │  ← Titel: Rethink Sans Bold, wit
│                                    │
│  Try our Start Your Balloon       │  ← Subtitel: Lato Regular, wit
│  Business Course                   │     Accent tekst in geel
│                                    │
└────────────────────────────────────┘
  ↑ Purple -> Dark Purple gradient (135deg)

┌────────────────────────────────────┐
│ 🔍 startyourballoonbusiness.com  │ │  ← Google search bar + typewriter
└────────────────────────────────────┘
  ↑ Witte bar, Google UI styling
```

**BEVAT:**

#### Element 1: CTA Tekst Card

Gradient achtergrond van purple naar dark purple, eerste keer dat een gradient achtergrond als floating kaart wordt gebruikt.

```tsx
background: `linear-gradient(135deg, ${BRAND.colors.primary.purple}, ${BRAND.colors.secondary.darkPurple})`
borderRadius: 32
padding: "60px 72px"
boxShadow: "0 12px 48px rgba(0, 0, 0, 0.3)"
```

**Titel:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 80
fontWeight: 700
color: BRAND.colors.neutral.white  // #ffffff
lineHeight: 1.2
marginBottom: 24
```

**Subtitel:**
```tsx
fontFamily: "Lato, sans-serif"
fontSize: 48
fontWeight: 400
color: BRAND.colors.neutral.white  // #ffffff
lineHeight: 1.4
```

**Accent tekst (inline span in subtitel):**
```tsx
color: BRAND.colors.secondary.yellow  // #ffdb5a
fontWeight: 700
```

Font-pairing: Rethink Sans (titel) + Lato (subtitel) is de correcte brand combinatie.

#### Element 2: Google Search Bar

Standalone zoekbalk met typewriter effect. Hergebruikt GoogleSearchIcon en GoogleMicIcon SVG's.

```tsx
backgroundColor: BRAND.colors.neutral.white
borderRadius: 36
padding: "0 32px"
height: 80
border: "2px solid #dfe1e5"
boxShadow: "0 4px 16px rgba(0, 0, 0, 0.12)"
```

**Typewriter:**
```tsx
const M15_TYPE_START = M15_E2_START + M15_E2_SCALE_FRAMES; // frame 54
const M15_TYPE_DURATION = 45; // ~1.5s

const charsPerFrame = searchText.length / M15_TYPE_DURATION;
const typedChars = Math.min(
  searchText.length,
  Math.max(0, Math.floor((frame - M15_TYPE_START) * charsPerFrame)),
);
```

**Blinkende cursor:** Zelfde patroon als google-search-card type (`Math.sin(frame * 0.3) > 0`).

**Zoektekst font:**
```tsx
fontSize: 32
fontFamily: "system-ui, sans-serif"
color: "#202124"
```

#### Element 1 In-Animatie: Drop from Top (spring, 0.4s)

```tsx
const e1DropIn = spring({
  frame,
  fps,
  config: { damping: 12, mass: 0.5, stiffness: 140 },
});
const e1Y = interpolate(e1DropIn, [0, 1], [-600, 0]);
```

Conservatievere spring dan tip-overlay (damping 12 vs 8) voor een "landing" gevoel met subtiele overshoot.

#### Element 2 In-Animatie: Scale Up (ease-out, 0.3s)

Verschijnt 1.5s na Element 1.

```tsx
const M15_E2_START = 45; // 1.5s delay
const M15_E2_SCALE_FRAMES = 9; // 0.3s

const e2Scale = interpolate(
  frame,
  [M15_E2_START, M15_E2_START + M15_E2_SCALE_FRAMES],
  [0, 1],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  },
);
```

#### Shared Exit: Slide Up Together (0.3s)

Beide elementen swipen samen naar boven uit beeld via de parent container. Geen individuele exit-animaties.

```tsx
const M15_EXIT_FRAMES = 9; // 0.3s
const exitStart = duration - M15_EXIT_FRAMES;

const exitY = interpolate(
  frame,
  [exitStart, duration],
  [0, -800],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.cubic),
  },
);

// Toegepast op parent container:
translateY(${shakeY + (frame >= exitStart ? exitY : 0)}px)
```

#### Shake (continu, SKILL standaard)

```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| E1 drop in | spring | `{ damping: 12, mass: 0.5, stiffness: 140 }` |
| E2 scale in | out cubic | `Easing.out(Easing.cubic)` |
| Shared exit (slide up) | in cubic | `Easing.in(Easing.cubic)` |
| Cursor blink | sinusgolf | `Math.sin(frame * 0.3)` |
| Shake | sinusgolf (2 lagen) | SKILL standaard |

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| E1 drop in | 0-~25 | ~0.8s | CTA card dropt van boven met spring bounce |
| E2 scale in | 45-54 | 0.3s | Google search bar schaalt vanuit midden |
| Typewriter | 54-99 | ~1.5s | URL typt letter voor letter |
| Hold | 99-141 | ~1.4s | Beide elementen zichtbaar, shake actief |
| Shared exit | 141-150 | 0.3s | Alles tegelijk naar boven uit beeld |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M15_E2_START | 45 frames (1.5s) | Delay voor E2 verschijning |
| M15_E2_SCALE_FRAMES | 9 frames (0.3s) | E2 scale-in duur |
| M15_TYPE_START | 54 frames (1.8s) | Typewriter start (na E2 settle) |
| M15_TYPE_DURATION | 45 frames (~1.5s) | Typewriter duur |
| M15_EXIT_FRAMES | 9 frames (0.3s) | Shared exit duur |
| Standaard duur | 150 frames (5s) | Configureerbaar via schema |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| E1 drop in | Click open | 0.25 | `sound-effects/universfield-computer-mouse-click-351398.mp3` | Bij startFrame |
| Typewriter | Keyboard typing | 0.1 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | TYPE_START - 20 frames (vroeg starten), duur TYPE_DURATION + 25 |
| Shared exit | Woosh | 0.25 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` | startFrame + duration - 9 |

Typing SFX start 20 frames voor de visuele typewriter voor een natuurlijker gevoel. Simpel geluidspalet: click in, typing tijdens, woosh uit.

```tsx
{/* Click in */}
<Sequence from={props.m15StartFrame} durationInFrames={20}>
  <Audio src={staticFile(SFX_CLICK_OPEN)} volume={0.25} />
</Sequence>
{/* Typewriter (starts 20 frames early) */}
<Sequence from={props.m15StartFrame + M15_TYPE_START - 20} durationInFrames={M15_TYPE_DURATION + 25}>
  <Audio src={staticFile(SFX_TYPING)} volume={0.1} />
</Sequence>
{/* Shared exit woosh */}
<Sequence from={props.m15StartFrame + props.m15DurationFrames - M15_EXIT_FRAMES} durationInFrames={20}>
  <Audio src={staticFile(SFX_WOOSH_OUT)} volume={0.25} />
</Sequence>
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| E1 gradient start | Purple | #6b3fb9 |
| E1 gradient end | Dark Purple | #1b073d |
| E1 titel tekst | White | #ffffff |
| E1 subtitel tekst | White | #ffffff |
| E1 accent tekst | Yellow | #ffdb5a |
| E1 drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |
| E2 achtergrond | White | #ffffff |
| E2 border | Grijs | #dfe1e5 |
| E2 shadow | Zwart 12% | rgba(0, 0, 0, 0.12) |
| Search icon | Grijs | #9aa0a6 |
| Mic icon | Blauw/Groen | #4285f4 / #34a853 |
| Getypte tekst | Donkergrijs | #202124 |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m15Enabled: z.boolean(),
m15Title: z.string(),
m15Subtitle: z.string(),
m15AccentText: z.string(),
m15SearchText: z.string(),
m15StartFrame: z.number(),
m15DurationFrames: z.number(),
```

Titel, subtitel, accent tekst, zoektekst, timing en aan/uit zijn individueel bewerkbaar in Remotion Studio.

#### Verschil met google-search-card type

| Aspect | cta-card | google-search-card |
|--------|---------|-------------------|
| Elementen | 2 (tekst card + search bar) | 1 (search bar in kaart) |
| Achtergrond | Gradient card (purple -> darkPurple) | Witte kaart met paarse rand |
| Tekst | Titel (Rethink) + subtitel (Lato) + accent | Alleen getypte zoektekst |
| Google logo | Nee | Ja |
| Search bar | Standalone onder de card | Binnenin de kaart |
| In-animatie E1 | Spring drop van boven | Scale + rotation |
| In-animatie E2 | Scale up (1.5s delay) | N/A (1 element) |
| Uit-animatie | Shared slide up | Swipe naar links |
| Doel | CTA met URL verwijzing | Visuele vraag-context |
| Font-pairing | Rethink Sans + Lato | system-ui (Google UI) |

**TRANSITIE:** Element 1 dropt van boven met spring bounce (0.4s). Element 2 schaalt vanuit midden (0.3s, 1.5s na E1). Typewriter typt URL (~1.5s). Shared exit: beide elementen swipen samen naar boven (in cubic, 0.3s). Continu SKILL standaard shake.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (CTACard component)

**REGISTRATIE:** Moment 15 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: email-cta

**WANNEER:** Interactieve call-to-action die de kijker aanmoedigt een email te sturen. Multi-fase overlay met een vraag-kaart, een programmatische email composer, typewriter effect, cursor interactie, en send bevestiging. Het meest complexe overlay type.

**LAYOUT:** Midden van het scherm, verticaal gecentreerd. Video blijft op de achtergrond zichtbaar (geen panel, geen video shift).

```
Positie: left 50%, top 50%, translate(-50%, -50%)
Twee elementen verticaal gestapeld met 40px gap
Email composer: 2200px breed (~57% van 3840px)
```

**STRUCTUUR (4 fasen):**

```
Fase 1 (0-2s):
┌──────────────────────────────────┐
│  What would you like to learn?   │  ← Typewriter effect
│                            ▏     │
└──────────────────────────────────┘

Fase 2 (2-3.5s):
┌──────────────────────────────────────────┐
│  What would you like to learn?           │  ← Kader groeit 130%
│                                          │
│  Send us an email at                     │  ← Extra tekst faded in
│  hello2@sempertexeurope.com              │     Email in geel accent
│  of what tutorials you'd like to see     │
└──────────────────────────────────────────┘

Fase 3 (4.3-8.3s):
┌─────────────────────────────────────────┐
│ ● ● ●  New Message                     │  ← Gmail-stijl email composer
├─────────────────────────────────────────┤
│ To: hello2@sempertexeurope.com          │
│ Subject: Tutorial request               │
│                                         │
│ Could you please make a tutorial on...  │  ← Typewriter effect (~2.5s)
│                                         │
│ [Send]  Message sent successfully ✓     │  ← Glow pulse, klik, bevestiging
└─────────────────────────────────────────┘

┌────────────────────────────────┐
│  (vraag-kaart, 90% kleiner,   │  ← Verschoven naar ~10% van onderrand
│   onderaan het scherm)         │
└────────────────────────────────┘

Fase 4 (8.3-8.8s):
Alles swiped naar rechts uit beeld
```

**BEVAT:**

#### Fase 1: Vraag Pop-in + Typewriter (0-2s)

Gradient kaart popt in met spring bounce, titel verschijnt via typewriter.

**Kaart:**
```tsx
background: `linear-gradient(135deg, ${BRAND.colors.primary.purple}, ${BRAND.colors.secondary.darkPurple})`
borderRadius: 32
padding: "48px 64px"
boxShadow: "0 12px 48px rgba(0, 0, 0, 0.3)"
maxWidth: 1200
textAlign: "center"
```

**Pop-in:**
```tsx
const questionPopIn = spring({
  frame,
  fps,
  config: { damping: 8, mass: 0.4, stiffness: 180 },
});
```

**Typewriter (vraag):**
```tsx
const q1TypeStart = 9; // na pop settle
const q1TypeDuration = 35; // ~1.2s
// "What would you like to learn?"
```

**Titel font:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 80
fontWeight: 700
color: BRAND.colors.neutral.white
```

#### Fase 2: Kaart Groeit + Extra Tekst (2-3.5s)

Kaart schaalt smooth naar 130% en extra tekst faded in.

```tsx
const cardScale = interpolate(
  frame,
  [M18_PHASE1_END, M18_PHASE2_END],
  [1, 1.3],
  { easing: Easing.inOut(Easing.cubic) },
);

const extraTextOpacity = interpolate(
  frame,
  [M18_PHASE1_END + 15, M18_PHASE2_END],
  [0, 1],
);
```

**Extra tekst:**
```tsx
fontFamily: "Lato, sans-serif"
fontSize: 44
fontWeight: 400
color: BRAND.colors.neutral.white
// Email adres in accent kleur:
color: BRAND.colors.secondary.yellow, fontWeight: 700
```

#### Fase 3: Email Composer (4.3-8.3s)

Vraag-kaart schuift naar beneden (1060px, ~10% van onderrand) en krimpt 10%. Email composer popt in vanuit midden.

**Kaart shift + shrink:**
```tsx
const questionShiftY = interpolate(
  frame,
  [M18_EMAIL_START, M18_EMAIL_START + 12],
  [0, 1060],
  { easing: Easing.inOut(Easing.cubic) },
);

const cardShrink = interpolate(
  frame,
  [M18_EMAIL_START, M18_EMAIL_START + 12],
  [1, 0.9],
  { easing: Easing.inOut(Easing.cubic) },
);
```

**Email composer (Gmail-stijl, 2x geschaald voor 4K):**
```tsx
width: 2200
borderRadius: 32
boxShadow: "0 16px 80px rgba(0, 0, 0, 0.2)"
```

Programmatisch gebouwde email UI met:
- **Header bar:** Grijs (#f1f3f4) met traffic lights (24px) en "New Message" tekst (32px)
- **To veld:** fontSize 36, system-ui
- **Subject veld:** fontSize 36, system-ui
- **Body:** fontSize 40, system-ui, typewriter effect (~2.5s, 75 frames)
- **Blinkende cursor:** 4px breed, 44px hoog, #202124

**Send knop:**
- Pre-click: blauw (#1a73e8) met glow pulse (`Math.sin(frame * 0.15)`, range 0.3-0.8)
- Klik animatie: scale 1 -> 0.95 -> 1 (6 frames)
- Post-click: groen (#34a853), tekst "Sent!"
- "Message sent successfully" bevestiging faded in (8 frames)

**SVG Cursor (zelfde als browser-animation type):**
```tsx
// Smoothstep beweging naar Send knop
const eased = p * p * (3 - 2 * p);
cursorX: 600 -> 1040
cursorY: 760 -> 860
// Klik: scale 0.85 gedurende 4 frames
```

#### Fase 4: Exit (0.5s)

Alles swiped samen naar rechts uit beeld.

```tsx
const M18_EXIT_FRAMES = 15; // 0.5s

const exitX = interpolate(
  frame,
  [M18_EXIT_START, M18_EXIT_START + M18_EXIT_FRAMES],
  [0, 2500],
  { easing: Easing.in(Easing.cubic) },
);
```

#### Shake (continu, SKILL standaard)

```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Vraag pop-in | spring | `{ damping: 8, mass: 0.4, stiffness: 180 }` |
| Card scale (fase 2) | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Extra tekst fade | linear | geen easing |
| Question shift down | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Card shrink | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Email scale in | out cubic | `Easing.out(Easing.cubic)` |
| Send button click | linear (3-keyframe) | 1 -> 0.95 -> 1 |
| Send glow pulse | sinusgolf | `Math.sin(frame * 0.15)` |
| Cursor movement | smoothstep | `p*p*(3-2*p)` |
| Exit swipe right | in cubic | `Easing.in(Easing.cubic)` |

#### Animatie Sequentie

| Fase | Relatief frame | Duur | Beschrijving |
|------|---------------|------|-------------|
| Vraag pop-in | 0-~25 | ~0.8s | Spring bounce kaart verschijnt |
| Vraag typewriter | 9-44 | ~1.2s | "What would you like to learn?" typt |
| Card groeit | 60-105 | 1.5s | Kaart schaalt 1x -> 1.3x |
| Extra tekst fade | 75-105 | 1s | Subtitel met email adres verschijnt |
| Kaart shift down | 129-141 | 0.4s | Kaart schuift 1060px naar beneden + krimpt 10% |
| Email popup | 129-138 | 0.3s | Email composer schaalt vanuit midden |
| Email typewriter | 139-214 | 2.5s | Email body typt |
| Send glow pulse | 214-224 | 0.3s | Send knop pulseert blauw |
| Cursor -> Send | 219-222 | 0.1s | Cursor beweegt naar knop |
| Send klik | 224 | instant | Knop groen, "Sent!", bevestiging fade |
| Hold | 224-249 | 0.8s | Bevestiging zichtbaar |
| Exit swipe right | 249-264 | 0.5s | Alles swiped naar rechts |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M18_PHASE1_END | 60 frames (2s) | Einde fase 1 |
| M18_PHASE2_END | 105 frames (3.5s) | Einde fase 2 |
| M18_EMAIL_START | 129 frames (4.3s) | Email popup + kaart shift |
| M18_TYPE2_START | 139 frames (4.6s) | Email body typewriter start |
| M18_TYPE2_DURATION | 75 frames (2.5s) | Email typewriter duur |
| M18_SEND_CLICK | 224 frames (7.5s) | Send knop klik |
| M18_EXIT_START | 249 frames (8.3s) | Exit start |
| M18_EXIT_FRAMES | 15 frames (0.5s) | Exit duur |
| questionShiftY | 1060px | Kaart verschuiving naar beneden |
| cardShrink | 0.9 (10% kleiner) | Kaart verkleining bij shift |
| Standaard duur | 264 frames (8.8s) | Configureerbaar via schema |

#### Sound Design

| Actie | Geluid | Volume | Pad | Timing |
|-------|--------|--------|-----|--------|
| Vraag pop-in | Woosh in | 0.25 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` | Bij startFrame |
| Vraag typewriter | Typing | 0.08 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | startFrame - 11, duur 60f (20f vroeg) |
| Email typewriter | Typing | 0.1 | `sound-effects/dragon-studio-keyboard-typing-sound-effect-335503.mp3` | TYPE2_START - 20, duur TYPE2_DURATION + 25 (20f vroeg) |
| Send klik | Click | 0.2 | `sound-effects/universfield-computer-mouse-click-351398.mp3` | SEND_CLICK |
| Verzonden | Ding | 0.15 | `sound-effects/koiroylers-slow-ding-354125.mp3` | SEND_CLICK + 10 |
| Exit swipe | Woosh out | 0.25 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` | EXIT_START |

Twee typewriter SFX's starten bewust 20 frames voor de visuele typewriter voor een natuurlijker gevoel. Ding als positieve bevestiging na send.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Vraag gradient start | Purple | #6b3fb9 |
| Vraag gradient end | Dark Purple | #1b073d |
| Vraag titel | White | #ffffff |
| Extra tekst | White | #ffffff |
| Email accent | Yellow | #ffdb5a |
| Email composer bg | White | #ffffff |
| Email header | Grijs | #f1f3f4 |
| Traffic lights | Rood/Geel/Groen | #ff5f57 / #febc2e / #28c840 |
| Email tekst | Donkergrijs | #202124 |
| Email labels | Grijs | #5f6368 |
| Send knop (pre) | Blauw | #1a73e8 |
| Send knop (post) | Groen | #34a853 |
| Bevestiging tekst | Groen | #34a853 |
| Cursor | Wit + zwart | #fff / #000 |

Email UI kleuren zijn bewust Gmail platform-standaard voor herkenning.

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m18Enabled: z.boolean(),
m18StartFrame: z.number(),
m18DurationFrames: z.number(),
```

Minimaal schema: teksten zijn hardcoded in het component (QUESTION_TEXT, EMAIL_TO, EMAIL_SUBJECT, EMAIL_BODY) omdat ze specifiek zijn voor dit CTA moment.

#### Verschil met browser-animation en cta-card types

| Aspect | email-cta | browser-animation | cta-card |
|--------|----------|-------------------|---------|
| Fasen | 4 (vraag, groei, email, exit) | 4 (Google, results, home, workshop) | 2 (tekst + search) |
| Layout | Midden scherm | Fullscreen | Links 5% |
| Email composer | Ja (programmatisch Gmail) | Nee | Nee |
| Typewriter | 2x (vraag + email body) | 1x (zoektekst) | 1x (URL) |
| Cursor | Ja (smoothstep naar Send) | Ja (smoothstep door pagina's) | Nee |
| Interactie | Send klik + bevestiging | Page clicks + navigatie | Geen |
| Card shift | Ja (naar beneden + shrink) | Nee | Nee |
| Exit | Swipe rechts | Scale out | Slide up |
| Duur | ~8.8s | ~12s | ~5s |
| Complexiteit | Zeer hoog | Hoog | Medium |

**TRANSITIE:** Fase 1: spring pop-in + typewriter (2s). Fase 2: card groeit 130% + extra tekst fade (1.5s). Fase 3: card shift naar beneden (1060px) + shrink 10%, email popt in met typewriter + cursor + send klik + bevestiging (4s). Fase 4: alles swiped naar rechts (0.5s). Continu SKILL standaard shake.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (EmailCTA + EmailCursor componenten)

**REGISTRATIE:** Moment 18 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: event-photo-card

**WANNEER:** Een evenement of locatie wordt getoond met een foto en een branded titel badge erboven. Swipe in/out variant (niet pop). Gebruikt voor evenementen, conferenties, of locaties die visueel gepresenteerd worden.

**LAYOUT:** Floating kaart linksonder het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: bottom 5%, left 5%
Kaart breedte: 1197px (~31% van 3840px)
Kaart hoogte: 898px (~42% van 2160px)
transformOrigin: "bottom left"
```

**STRUCTUUR:**

```
┌──────────────────────────────┐
│ British Balloon Bash 2025    │  ← Gele badge, dicht op kader (16px gap)
└──────────────────────────────┘
┌──────────────────────────────┐
│                              │
│        Event foto            │  ← objectFit: cover
│                              │
└──────────────────────────────┘
  ↑ Paarse rand met neon glow
```

**BEVAT:**

#### Titel Badge (boven kader)

Geel blok met event naam, direct boven het fotokader.

```tsx
display: "inline-block"
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "16px 48px"
borderRadius: 12
boxShadow: "0 4px 12px rgba(0, 0, 0, 0.15)"
marginBottom: 16  // dicht op kader
```

**Titel tekst:**
```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 96
fontWeight: 700  // Bold
color: BRAND.colors.secondary.darkPurple  // #1b073d
lineHeight: 1.2
```

Consistent met materialenlijst en titled-photo-card titel badge styling (geel + dark purple).

#### Foto Kader

Landscape kader met paarse rand en 3-laags neon glow.

```tsx
width: 1197
height: 898
border: `8px solid ${BRAND.colors.primary.purple}`
borderRadius: 20
overflow: "hidden"
```

**Neon glow:** Identiek aan design-showcase type (range 0.5-0.85, frequentie 0.06).

#### Wobbly Shake (continu)

Identiek aan design-showcase type (3-laags sinusgolven).

```tsx
const wobbleX = Math.sin(frame * 0.15) * 4 + Math.sin(frame * 0.23) * 2.5 + Math.sin(frame * 0.37) * 1.5;
const wobbleY = Math.cos(frame * 0.12) * 2 + Math.cos(frame * 0.19) * 1.5;
const wobbleRotate = Math.sin(frame * 0.1) * 0.4 + Math.sin(frame * 0.18) * 0.25;
```

#### Breathe (continu)

```tsx
const breathe = 1 + Math.sin(frame * 0.04) * 0.008;
```

#### Swipe In van Links (0.4s)

```tsx
const M19_SWIPE_FRAMES = 12;

const swipeInX = interpolate(
  frame,
  [0, M19_SWIPE_FRAMES],
  [offScreenLeft, 0],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
// offScreenLeft = -(cardWidth + screenWidth * 0.05 + 40)
```

#### Swipe Out naar Links (0.4s)

```tsx
const swipeOutX = interpolate(
  frame,
  [duration - M19_SWIPE_FRAMES, duration],
  [0, offScreenLeft],
  {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  },
);
```

Zelfde richting als entry (links uit, links in). Consistent met design-showcase swipe patroon.

#### Gecombineerde Transform

```tsx
transform: [
  `translateX(${translateX + wobbleX}px)`,
  `translateY(${wobbleY}px)`,
  `rotate(${wobbleRotate}deg)`,
  `scale(${breathe})`,
].join(" ")
transformOrigin: "bottom left"
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Swipe in | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Swipe out | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Neon glow puls | sinusgolf | `Math.sin(frame * 0.06)` |
| Wobble | sinusgolf (3 lagen) | Zie wobble sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M19_SWIPE_FRAMES | 12 frames (0.4s) | Swipe in en swipe out duur |
| Hold | ~81 frames (~2.7s) | Kaart zichtbaar in rustpositie |
| Standaard duur | 105 frames (3.5s) | Configureerbaar via schema |
| Kaart breedte | 1197px | ~31% van 3840px |
| Kaart hoogte | 898px | ~42% van 2160px |
| Badge gap | 16px | Afstand badge tot kader |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Swipe in | Woosh in | 0.25 | `sound-effects/dragon-studio-simple-whoosh-02-433006.mp3` |
| Swipe out | Woosh out | 0.25 | `sound-effects/dragon-studio-simple-whoosh-382724.mp3` |

Twee woosh sounds voor in/out variatie. Zelfde SFX paar als design-showcase (M1). Passend bij het swipe karakter.

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Badge achtergrond | Yellow | #ffdb5a |
| Badge tekst | Dark Purple | #1b073d |
| Badge schaduw | Zwart 15% | rgba(0, 0, 0, 0.15) |
| Kaart rand | Purple | #6b3fb9 |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m19Enabled: z.boolean(),
m19ImageSrc: z.string(),
m19Title: z.string(),
m19Subtitle: z.string(),  // unused but kept for flexibility
m19StartFrame: z.number(),
m19DurationFrames: z.number(),
```

#### Verschil met design-showcase en titled-photo-card types

| Aspect | event-photo-card | design-showcase | titled-photo-card |
|--------|-----------------|-----------------|------------------|
| In-animatie | Swipe van links | Swipe van links | Pop (spring) |
| Uit-animatie | Swipe naar links | Swipe naar rechts | Pop (3-keyframe) |
| Exit richting | Zelfde als entry (links) | Tegenovergesteld (rechts) | Geen richting (scale) |
| Badge positie | Boven kader (los, 16px gap) | Rechtsboven op kader | Boven kader (los, 24px gap) |
| Badge inhoud | Event naam | Datum | Vrije titel |
| Orientatie | Landscape (1197x898) | Landscape (1197x898) | Portrait (1000x1300) |
| Meerdere kaarten | Nee | Ja (sequentieel) | Nee |
| Badge stijl | Geel + dark purple + rounded | Geel + dark purple + rounded | Geel + dark purple + rounded |

**TRANSITIE:** Swipe in van links (inOut cubic, 0.4s) + swipe out naar links (inOut cubic, 0.4s). Continu wobbly shake + breathe + neon glow puls. Video blijft volledig zichtbaar.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (EventPhotoCard component)

**REGISTRATIE:** Moment 19 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`

---

### TYPE: product-showcase-carousel

**WANNEER:** Meerdere producten worden sequentieel getoond in een carousel. Elk product swiped individueel in en uit onder een vaste titel. Gebruikt voor product releases, nieuwe kleuren, of collectie-overzichten.

**LAYOUT:** Linksboven het scherm. Video blijft volledig zichtbaar erachter (geen video shift, geen panel).

```
Positie: top 5%, left 5%
Kaart breedte: 22% van scherm (width * 0.22)
Kaart formaat: vierkant (cardWidth x cardWidth)
Producten verschijnen onder de vaste titel
```

**STRUCTUUR:**

```
┌──────────────────────────────┐
│ LATEST BALLOON RELEASES      │  ← Geel titelblok, ExtraBold Italic + text-stroke
└──────────────────────────────┘    Blijft staan gedurende hele moment

┌──────────────┐
│              │
│  🎈 Product  │  ← Vierkant kader, lavender achtergrond
│    foto      │     Product PNG met transparante/lavender bg
│              │
└──────────────┘
  ↑ Paarse rand + neon glow

Reflex Galaxy Blue             ← Product naam: groot, wit, Bold
┌──────────────────┐
│ January 2026     │           ← Datum: lavender badge, paars tekst
└──────────────────┘
```

Producten wisselen via swipe (links in, links uit). Elk product ~2s zichtbaar.

**BEVAT:**

#### Persistente Titel (blijft gedurende hele carousel)

Geel blok met ExtraBold Italic tekst + text-stroke voor extra vet effect.

```tsx
// Geel blok
display: "inline-block"
backgroundColor: BRAND.colors.secondary.yellow  // #ffdb5a
padding: "16px 56px"

// Titel tekst
fontFamily: "Rethink Sans, sans-serif"
fontSize: 84
fontWeight: 800  // ExtraBold
fontStyle: "italic"
color: BRAND.colors.secondary.darkPurple  // #1b073d
letterSpacing: 5
WebkitTextStroke: `2px ${BRAND.colors.secondary.darkPurple}`  // extra bold effect
```

**Titel entrance:** Spring (damping 14, stiffness 120) met slide van boven + fade.

**Titel fade-out:** Lineaire fade (9 frames) na de laatste product exit.
```tsx
const titleFadeOut = interpolate(
  frame,
  [lastProduct.holdEndFrame + M20_SWIPE_FRAMES, lastProduct.holdEndFrame + M20_SWIPE_FRAMES + 9],
  [1, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);
```

#### Product Kaart (vierkant, lavender achtergrond)

```tsx
width: cardWidth  // width * 0.22
height: cardWidth  // vierkant
border: `8px solid ${BRAND.colors.primary.purple}`
borderRadius: 24
overflow: "hidden"
backgroundColor: BRAND.colors.primary.lavender  // #f1d9ff
display: "flex"
alignItems: "center"
justifyContent: "center"
```

Product afbeelding met `objectFit: "contain"` op 85% van kader (padding effect).

**Neon glow:** Identiek aan design-showcase (3 lagen, range 0.5-0.85).

**Product afbeeldingen:** PNG's met witte achtergrond vervangen door lavender (#f1d9ff) via image processing (sharp). Opgeslagen in `public/images/Product foto's/All Products/`.

#### Product Naam (onder kader)

```tsx
fontFamily: "Rethink Sans, sans-serif"
fontSize: 128
fontWeight: 700  // Bold
color: BRAND.colors.neutral.white  // #ffffff
textShadow: "0 4px 16px rgba(0, 0, 0, 0.5)"
```

#### Release Datum (onder naam, lavender badge)

Paarse tekst op lavender achtergrond badge voor leesbaarheid.

```tsx
// Badge container
display: "inline-block"
backgroundColor: BRAND.colors.primary.lavender  // #f1d9ff
padding: "8px 24px"
borderRadius: 8
marginTop: 8

// Datum tekst
fontFamily: "Lato, sans-serif"
fontSize: 80
fontWeight: 700
color: BRAND.colors.primary.purple  // #6b3fb9
```

#### Per-Product Swipe (0.3s in, 0.3s out)

```tsx
const M20_SWIPE_FRAMES = 9; // 0.3s

// Swipe in from left
const swipeInX = interpolate(
  frame,
  [inFrame, inFrame + M20_SWIPE_FRAMES],
  [offScreenLeft, 0],
  { easing: Easing.inOut(Easing.cubic) },
);

// Swipe out to left
const swipeOutX = interpolate(
  frame,
  [holdEndFrame, holdEndFrame + M20_SWIPE_FRAMES],
  [0, offScreenLeft],
  { easing: Easing.inOut(Easing.cubic) },
);
```

Elk product swiped individueel. De vorige is al weg voordat de volgende binnenkomt (9 frame gap).

#### Wobble + Breathe (per product, tijdens hold)

Subtielere wobble dan design-showcase (2-laags i.p.v. 3-laags, lagere amplitude).

```tsx
const wobbleX = Math.sin(frame * 0.15) * 3 + Math.sin(frame * 0.23) * 2;
// ~5px amplitude (vs ~8px bij design-showcase)

const wobbleY = Math.cos(frame * 0.12) * 1.5 + Math.cos(frame * 0.19) * 1;
// ~2.5px amplitude

const breathe = 1 + Math.sin(frame * 0.04) * 0.006;
// 0.6% amplitude (vs 0.8% bij design-showcase)
```

#### Shake (SKILL standaard, op parent container)

```tsx
const shakeX = Math.sin(frame * 0.08) * 1 + Math.sin(frame * 0.13) * 0.5;
const shakeY = Math.cos(frame * 0.06) * 0.7 + Math.cos(frame * 0.11) * 0.3;
```

#### Easing Curves

| Context | Easing | Code |
|---------|--------|------|
| Titel entrance | spring | `{ damping: 14, mass: 0.5, stiffness: 120 }` |
| Titel fade-out | linear | `interpolate` zonder easing |
| Product swipe in | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Product swipe out | inOut cubic | `Easing.inOut(Easing.cubic)` |
| Neon glow puls | sinusgolf | `Math.sin(frame * 0.06)` |
| Wobble | sinusgolf (2 lagen) | Zie wobble sectie |
| Breathe | sinusgolf | `Math.sin(frame * 0.04)` |
| Shake | sinusgolf (2 lagen) | SKILL standaard |

#### Sequentie Timing (4 producten)

| Product | inFrame | holdEndFrame | Hold | Beschrijving |
|---------|---------|-------------|------|-------------|
| 1: Reflex Galaxy Blue | 30 | 81 | 42f (1.4s) | Swipe in, hold, swipe out |
| 2: Pastel Matte Nude | 99 | 150 | 42f (1.4s) | 9f gap, swipe in |
| 3: Fashion Mocha | 168 | 219 | 42f (1.4s) | 9f gap, swipe in |
| 4: Silk Midnight Grey | 237 | 288 | 42f (1.4s) | 9f gap, swipe in |
| Titel fade-out | 297-306 | | 9f | Fade na laatste exit |

Gap tussen producten: 9 frames (= M20_SWIPE_FRAMES, zodat exit van product N eindigt precies wanneer entry van product N+1 begint).

#### Timing

| Constante | Waarde | Beschrijving |
|-----------|--------|-------------|
| M20_SWIPE_FRAMES | 9 frames (0.3s) | Per-product swipe in/out duur |
| Hold per product | ~42 frames (~1.4s) | Product zichtbaar in rustpositie |
| Gap tussen producten | 9 frames (0.3s) | Exit vorige + entry volgende |
| Titel fade-out | 9 frames (0.3s) | Fade na laatste product exit |
| Standaard duur | 300 frames (10s) | 4 producten + titel fade |
| Kaart breedte | width * 0.22 | ~22% van scherm |
| Kaart formaat | vierkant | cardWidth x cardWidth |

#### Sound Design

| Actie | Geluid | Volume | Pad |
|-------|--------|--------|-----|
| Product swipe in (per stuk) | Click open | 0.2 | `sound-effects/universfield-computer-mouse-click-351398.mp3` |
| Product swipe out (per stuk) | Click out | 0.2 | `sound-effects/universfield-computer-mouse-click-352734.mp3` |

8 totale events (4 producten x 2 clicks). Click sounds passen bij het "bladeren door een catalogus" gevoel.

```tsx
{props.m20Products.map((product, i) => (
  <Sequence key={`m20-sfx-${i}`} from={props.m20StartFrame} durationInFrames={props.m20DurationFrames}>
    <Sequence from={product.inFrame} durationInFrames={15}>
      <Audio src={staticFile(SFX_CLICK_OPEN)} volume={0.2} />
    </Sequence>
    <Sequence from={product.holdEndFrame} durationInFrames={15}>
      <Audio src={staticFile(SFX_CLICK_OUT)} volume={0.2} />
    </Sequence>
  </Sequence>
))}
```

#### Kleuren Samenvatting

| Element | Kleur | HEX |
|---------|-------|-----|
| Titel blok | Yellow | #ffdb5a |
| Titel tekst + text-stroke | Dark Purple | #1b073d |
| Kaart rand | Purple | #6b3fb9 |
| Kaart achtergrond | Lavender | #f1d9ff |
| Neon glow (3 lagen) | Purple | rgb(107, 63, 185) |
| Product naam | White | #ffffff |
| Datum badge achtergrond | Lavender | #f1d9ff |
| Datum tekst | Purple | #6b3fb9 |
| Drop shadow | Zwart 30% | rgba(0, 0, 0, 0.3) |

#### Image Processing

Product afbeeldingen worden voorbewerkt: witte achtergrond (pixels > 245 op alle kanalen) wordt vervangen door lavender (#f1d9ff). Verwerkt via sharp/node script, opgeslagen als PNG.

```
Origineel: public/images/Product foto's/All Products/Blue.jpg  (wit achtergrond)
Verwerkt:  public/images/Product foto's/All Products/Blue.png  (lavender achtergrond)
```

#### Schema (Remotion Studio bewerkbaar)

```typescript
// In parent schema (AudreyRobinOverlaysSchema):
m20Enabled: z.boolean(),
m20Title: z.string(),
m20Products: z.array(z.object({
  imageSrc: z.string(),
  name: z.string(),
  date: z.string(),
  inFrame: z.number(),
  holdEndFrame: z.number(),
})),
m20StartFrame: z.number(),
m20DurationFrames: z.number(),
```

Titel, producten (afbeelding, naam, datum, timing), start en duur zijn individueel bewerkbaar. Producten kunnen worden toegevoegd of verwijderd.

#### Verschil met design-showcase type

| Aspect | product-showcase-carousel | design-showcase |
|--------|--------------------------|-----------------|
| Positie | top 5%, left 5% | bottom 5%, left 5% |
| Kaart formaat | Vierkant (22% breed) | Landscape (31% breed) |
| Kaart achtergrond | Lavender (#f1d9ff) | Transparant (foto vult kader) |
| Afbeelding | objectFit contain (85%) | objectFit cover (100%) |
| Persistente titel | Ja (geel blok, italic, text-stroke) | Nee |
| Badge | Geen (naam + datum onder kader) | Datum rechtsboven op kader |
| Datum styling | Lavender badge + paarse tekst | Geel badge + dark purple tekst |
| Wobble | 2-laags, ~5px | 3-laags, ~8px |
| Breathe | 0.6% | 0.8% |
| Titel fade-out | Ja (na laatste product) | Nee |
| Swipe richting | Links in, links uit | Links in, rechts uit |

**TRANSITIE:** Persistente titel verschijnt met spring. Producten swipen sequentieel van links in/uit (inOut cubic, 0.3s). Na laatste product: titel faded uit (0.3s). Continu wobble + breathe + neon glow + SKILL shake.

**REFERENTIE:** `remotion-stx/src/overlays/audrey-robin-overlays.tsx` (ProductShowcase component)

**REGISTRATIE:** Moment 20 in Composition `Audrey-Robin-Q`, via parent `remotion-stx/src/overlays/audrey-robin-overlays.tsx`
