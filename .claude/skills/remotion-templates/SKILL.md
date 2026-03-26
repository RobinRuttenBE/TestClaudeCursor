---
name: remotion-templates
description: Sempertex Europe branded Remotion video templates — alle beschikbare compositions, parameters en render instructies
type: skill
---

# SKILL: Remotion Templates — Sempertex Europe

## Overzicht

Dit project bevat 5 branded Remotion compositions voor Sempertex Europe video productie.
Alle templates leven in `remotion-stx/src/` en gebruiken de gedeelde brand config uit `remotion-stx/src/brand-config.ts`.

## Beschikbare Templates

### 1. STX-Intro
**Bestand:** `remotion-stx/src/STX-Intro.tsx`
**Duur:** 5 seconden (150 frames @ 30fps)
**Formaat:** 1920x1080

Animated intro met logo en tagline.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `tagline` | string | "From balloon artists, for balloon artists." | Tekst onder het logo |
| `logoSrc` | string | `logos/sempertex-logo.png` | Pad naar logo in public/ |
| `soundEffect` | string | undefined | Pad naar woosh sound in public/ |

**Animaties:**
- Logo: spring animatie (fade in + scale) vanaf frame 10
- Tagline: slide in van onder vanaf frame 40
- Achtergrond: gradient #6b3fb9 → #1b073d

---

### 2. STX-Outro
**Bestand:** `remotion-stx/src/STX-Outro.tsx`
**Duur:** 5 seconden (150 frames @ 30fps)
**Formaat:** 1920x1080

Outro met social media links en website.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `showInstagram` | boolean | true | Toon Instagram icon |
| `showFacebook` | boolean | true | Toon Facebook icon |
| `showYoutube` | boolean | true | Toon YouTube icon |
| `websiteUrl` | string | "www.sempertexeurope.com" | Website URL tekst |
| `logoSrc` | string | `logos/stx-eu-logo.png` | Pad naar logo in public/ |

**Animaties:**
- "Follow us" tekst: fade in
- Social icons: staggered fade in
- Website URL: fade in
- Hele scene: fade out in laatste 30 frames

---

### 3. STX-LowerThird
**Bestand:** `remotion-stx/src/STX-LowerThird.tsx`
**Duur:** 5 seconden (150 frames @ 30fps)
**Formaat:** 1920x1080 (transparante achtergrond)

Lower third overlay voor namen en titels. Transparante achtergrond zodat dit over video gelegd kan worden.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `name` | string | **verplicht** | Naam van de persoon |
| `title` | string | **verplicht** | Functietitel |
| `durationInFrames` | number | 150 | Totale duur (voor exit animatie timing) |
| `accentColor` | string | "#6b3fb9" | Kleur van de accent bar |

**Animaties:**
- Bar: inschuiven van links met ease-out
- Accent bar: iets vertraagd inschuiven
- Tekst: fade in na bar
- Exit: uitschuiven naar links

---

### 4. STX-TextOverlay
**Bestand:** `remotion-stx/src/STX-TextOverlay.tsx`
**Duur:** 5 seconden (150 frames @ 30fps)
**Formaat:** 1920x1080

Key quote overlay met verschillende tekst animaties.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `text` | string | **verplicht** | De quote/tekst om te tonen |
| `fontSize` | number | 64 | Tekstgrootte in px |
| `animation` | "word-by-word" \| "fade-in" \| "typewriter" | "word-by-word" | Animatie type |
| `gradient` | [string, string] | ["#6b3fb9", "#1b073d"] | Achtergrond gradient |
| `textColor` | string | "#ffffff" | Tekstkleur |

**Animatie types:**
- **word-by-word:** Elk woord verschijnt apart met slide-up effect (6 frames per woord)
- **fade-in:** Hele tekst faded in met subtiele scale
- **typewriter:** Tekst verschijnt karakter voor karakter met knipperende cursor

---

### 5. STX-FeatureBar
**Bestand:** `remotion-stx/src/STX-FeatureBar.tsx`
**Duur:** 6 seconden (180 frames @ 30fps)
**Formaat:** 1920x1080

Animated bullet points / feature list.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `items` | { icon: string, text: string }[] | **verplicht** | Lijst van features (max 5 aanbevolen) |
| `title` | string | undefined | Optionele titel boven de items |
| `gradient` | [string, string] | ["#6b3fb9", "#1b073d"] | Achtergrond gradient |
| `accentColor` | string | "#ffdb5a" | Kleur van de icon cirkels |

**Animaties:**
- Titel: fade in
- Items: staggered slide in van links met spring animatie (20 frames tussen items)
- Elke item heeft een gekleurde cirkel met icon en tekst

---

## Brand Config

De gedeelde brand config staat in `remotion-stx/src/brand-config.ts` en bevat:
- **Kleuren:** primary (purple, lavender, magenta), secondary (yellow, darkPurple)
- **Fonts:** Rethink Sans (titels/CTA), Lato (body)
- **Logo paden:** sempertex-logo.png, stx-eu-logo.png
- **Animatie defaults:** spring config, fade/slide duraties
- **Gradients:** primary, magenta, warm
- **Video formaten:** landscape (1920x1080), portrait (1080x1920), square (1080x1080)

## Assets

Assets staan in `remotion-stx/public/`:
```
public/
├── logos/          Sempertex logo, STX EU logo
├── fonts/          Rethink Sans, Lato
├── images/         Product foto's, team foto's
├── b-roll/         Korte video clips
├── sound-effects/  Woosh, click, riser, transition sounds
├── music/          Achtergrondmuziek tracks
└── brand/          Gradient achtergronden, patroon overlays
```

## Render Instructies

### Preview in Remotion Studio
```bash
cd remotion-stx && npm run dev
```

### Render als MP4
```bash
cd remotion-stx
npx remotion render STX-Intro out/stx-intro.mp4
npx remotion render STX-Outro out/stx-outro.mp4
npx remotion render STX-LowerThird out/stx-lowerthird.webm  # WebM voor transparantie
npx remotion render STX-TextOverlay out/stx-textoverlay.mp4
npx remotion render STX-FeatureBar out/stx-featurebar.mp4
```

### Render met custom props
```bash
npx remotion render STX-TextOverlay out/quote.mp4 --props='{"text":"Your custom quote here","animation":"typewriter"}'
```

### LowerThird met transparantie (voor overlay)
```bash
npx remotion render STX-LowerThird out/lowerthird.webm --codec=vp8
```

## Wanneer welke template gebruiken

| Situatie | Template |
|----------|----------|
| Begin van elke video | STX-Intro |
| Einde van elke video | STX-Outro |
| Persoon in beeld identificeren | STX-LowerThird |
| Belangrijke quote/uitspraak highlighten | STX-TextOverlay |
| Opsomming van features/voordelen | STX-FeatureBar |
| Animatie showcase / Lottie demo | STX-LottieShowcase |

---

### 6. STX-LottieShowcase
**Bestand:** `remotion-stx/src/STX-LottieShowcase.tsx`
**Duur:** 5 seconden (150 frames @ 30fps)
**Formaat:** 1920x1080

Showcase template met Lottie animatie, titel en ondertitel. Gebruik als basis voor elk component dat animated visuals nodig heeft.

**Props:**
| Prop | Type | Default | Beschrijving |
|------|------|---------|--------------|
| `animationPath` | string | `animations/icons/star.json` | Pad naar Lottie JSON in public/ |
| `title` | string | "Animated Visuals" | Hoofdtekst |
| `subtitle` | string | "Lottie animations in Remotion" | Ondertekst |
| `gradient` | [string, string] | BRAND.gradients.primary | Achtergrond gradient |

**Animaties:**
- Lottie: spring scale-in vanaf frame 5
- Titel: spring slide-in van links vanaf frame 20
- Ondertitel: fade in vanaf frame 45
- Hele scene: fade out in laatste 30 frames

**Helper hook:** `useLottieAnimation(path)` laadt een Lottie JSON uit public/ met correcte delayRender/continueRender handling. Herbruikbaar in andere componenten.

---

## Lottie Animatie Bibliotheek

18 Lottie animaties beschikbaar in `remotion-stx/public/animations/`:

| Categorie | Bestanden | Gebruik |
|-----------|-----------|---------|
| `arrows/` | arrow-pointing, swipe-arrow, direction-indicator | Pijlen, richtingaanwijzers |
| `transitions/` | swipe-transition, fade-transition, wipe-transition | Overgangen tussen scenes |
| `ui-elements/` | checkmark-success, loading-spinner, notification-bell | UI feedback elementen |
| `backgrounds/` | particles, gradient-flow, light-leak | Achtergrond animaties |
| `icons/` | star, heart, thumbs-up | Geanimeerde iconen |
| `text-effects/` | underline-draw, highlight, circle-emphasis | Tekst accentuering |

**Index:** `remotion-stx/public/animations/animation-index.json`
**Meer downloaden:** Gebruik `/fetch-lottie` om nieuwe animaties te zoeken en downloaden.

### Lottie gebruiken in een component

```tsx
import { Lottie, LottieAnimationData } from "@remotion/lottie";
import { useEffect, useState } from "react";
import { cancelRender, continueRender, delayRender, staticFile } from "remotion";

// Laad een Lottie JSON uit public/
function useLottieAnimation(path: string) {
  const [handle] = useState(() => delayRender(`Loading Lottie: ${path}`));
  const [data, setData] = useState<LottieAnimationData | null>(null);
  useEffect(() => {
    fetch(staticFile(path))
      .then((res) => res.json())
      .then((json) => { setData(json); continueRender(handle); })
      .catch((err) => { cancelRender(err); });
  }, [handle, path]);
  return data;
}

// Gebruik in je component:
const animationData = useLottieAnimation("animations/icons/star.json");
if (!animationData) return null;
return <Lottie animationData={animationData} style={{ width: 400, height: 400 }} />;
```

---

## Design Richtlijnen

### Animated visuals boven alleen tekst
Gebruik Lottie animaties om visuele interesse te creeren. Een compositie met alleen tekst op een gradient is saai. Voeg altijd minstens een van deze toe:
- Lottie animatie als visueel element
- Geanimeerde achtergrond (particles, gradient-flow)
- Icoon animaties bij bullet points (in plaats van emoji)
- Overgangseffecten tussen scenes

### Geen overmatig emoji gebruik
Emoji in video compositions ziet er onprofessioneel uit. Gebruik in plaats daarvan:
- Lottie icoon animaties (star, heart, checkmark)
- SVG iconen
- Geanimeerde vormen en lijnen

**Slecht:** `{ icon: "🎈", text: "Premium latex" }`
**Goed:** Een Lottie animatie of SVG icoon als visueel element

### Combineer tekst + motion
Elk nieuw template moet minstens een vorm van animated visual bevatten naast tekst. Denk aan:
- Achtergrond Lottie (particles, gradient-flow) achter tekst
- Icoon animatie naast de titel
- Text-effect Lottie (underline, highlight) als accent
- Overgang Lottie tussen secties

## Nieuwe templates toevoegen

1. Maak een nieuw bestand `remotion-stx/src/STX-NieuweTemplate.tsx`
2. Importeer `BRAND` uit `./brand-config` voor consistente styling
3. Overweeg Lottie animaties te gebruiken (zie Lottie bibliotheek hierboven)
4. Voeg een `<Composition>` toe in `remotion-stx/src/Root.tsx`
5. Update deze SKILL.md met de nieuwe template documentatie
