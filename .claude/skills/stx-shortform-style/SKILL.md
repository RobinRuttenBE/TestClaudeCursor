# STX Short Form Style Guide

Deze skill bevat alle short form specifieke regels, patronen, overlay types en uitzonderingen. Gebruik dit **naast** `stx-overlay-style/SKILL.md` wanneer je aan een short form video werkt (Reels, Shorts, TikToks).

Als je long form editing doet, negeer deze skill — gebruik alleen `stx-overlay-style`.

## Taalregel voor short form overlay tekst

**Alle Engelstalige short form overlay tekst (hook captions, follow-cta, stx-tip, etc.): UK spelling, altijd.** Colour, favourite, realise, organise, centre, behaviour, catalogue. Nooit US spelling. Volledige regels in `Kennis/Brand/tone-of-voice.md`.

## Short Form vs Long Form — Kernverschillen

| Aspect | Long Form | Short Form |
|--------|-----------|------------|
| Formaat | 3840x2160 of 1920x1080 (16:9 horizontaal) | 1080x1920 (9:16 verticaal) |
| Duur | 3-20 minuten | 15-90 seconden |
| Platform | YouTube primair | Reels, Shorts, TikTok |
| Overlay cadence | Max 1 effect per 30-60s na eerste minuut | 1 effect per 5-10s |
| Overlay duration | 4-10 seconden | 2-5 seconden |
| Max overlays tegelijk | 2 | 1 |
| Opening | Rustige intro met lower-third mogelijk | HOOK verplicht binnen 0-3 seconden |
| Outro | youtube-subscribe + social-bar + end-screen | Simpele follow CTA of @handle |
| Muziek volume | -20 tot -24dB | -18 tot -22dB (iets luider) |
| Saturatie grade | 1.15 | 1.20 (kleinere schermen maken kleur platter) |
| Caption layer | Niet gebruikt | Gereserveerd voor user-added captions onderaan |

## Het 9:16 Frame — Safe Zones

Het 1080x1920 frame is verdeeld in drie zones:

```
┌─────────────────────┐  ← 0px
│                     │
│   PLATFORM UI ZONE  │  ← 150px
│   (username, tijd)  │
├─────────────────────┤
│                     │
│                     │
│   OVERLAY ZONE      │
│   (veilig gebied)   │
│                     │
│                     │
│                     │
├─────────────────────┤  ← 1620px
│   CAPTIONS ZONE     │
│   (user-added)      │
└─────────────────────┘  ← 1920px
```

- **Top safe zone (0-150px)**: GEEN overlays. Platform UI (Instagram username, TikTok progress bar, Shorts timer) leeft hier.
- **Middle overlay zone (150-1620px)**: alle overlays plaatsen hier. Dit is 1470px hoog = ~76% van het frame.
- **Bottom captions zone (1620-1920px)**: GEEN overlays. Gereserveerd voor word-by-word captions die de gebruiker achteraf in Instagram/CapCut/etc. toevoegt.

**Centrale positie**: de "hero zone" waar het oog eerst landt is tussen 600px en 1200px vanaf de top — plaats hier de belangrijkste elementen (hooks, key statements, product shots).

## De Hook (Eerste 3 Seconden)

De hook is het belangrijkste element van elke short. Als de hook faalt, scrolt de kijker weg in <2 seconden.

### Hook anatomie

Elke hook bestaat uit drie lagen:

1. **Visual anchor** (verschijnt frame 0-5)
   - Kan zijn: de spreker in beeld, een close-up product shot, een dramatisch frame van de afgewerkte design
   - Het eerste frame is NOOIT zwart, NOOIT een fade-in van niets

2. **Hook caption** (verschijnt frame 5-20)
   - Grote tekst, top-center positie (y: 300-500px)
   - Max 6-8 woorden, liefst 3-6
   - Font: Rethink Sans Extra Bold, 110-140px
   - Contrast: wit op donkerpaars (#1b073d) vak, OF donkerpaars op geel (#ffdb5a) vak
   - Animatie: pop in scale 0% → 115% → 100% met spring overshoot, binnen 15 frames (0.5s)

3. **Supporting motion** (doorlopend tijdens hook)
   - Subtle shake op de caption (2-3px amplitude, 0.5Hz)
   - Of: gradient flash achter de tekst die 1x over het vak zweept
   - Of: floating particles achter het vak

### Hook content types

Welk soort hook past bij welk content type:

| Content type | Hook style | Voorbeeld |
|--------------|-----------|-----------|
| Tutorial | Payoff belofte | "Perfect Link-O-Loon in 60 seconds" |
| Tip/insight | Counter-intuitive claim | "Stop using a regular pump" |
| Product showcase | Arrival/news | "New: Reflex Galaxy Blue" |
| Artist feature | Credibility stat | "She books 40 weddings a year" |
| Design reveal | Curiosity gap | "This took 4 hours" |
| Mistake/warning | Direct callout | "You're inflating wrong" |
| Testimonial/social proof | Quote fragment | "I 3x'd my bookings" |

### Wat een hook NOOIT doet

- Begin met "Hi guys" of "Today I'm going to show you" — dood
- Fade in van zwart — dood
- Stille pauze van >10 frames voor de eerste beweging — dood
- Logo intro van meer dan 15 frames — dood
- Disclaimer of context eerst — dood

## Overlay Cadence

### De 5-10s regel

1 overlay per 5-10 seconden, MAAR alleen wanneer het script het verdient. Forceer niks.

Wel een overlay bij:
- Concrete cijfer of percentage
- Specifieke tip of actie
- Product naam die voor het eerst valt
- Key statement die de payoff ondersteunt
- Topic wissel
- Call-to-action

Geen overlay bij:
- Generic praten ("so what I like to do is...")
- Filler zinnen
- Herhalingen van wat visueel al duidelijk is

### Ademruimte

Elke 6-8 seconden moet er minstens 1-2 seconden ZIJN zonder overlay. Dit is rust. Zonder rust wordt de video overladen en voelt hij goedkoop.

Nooit 3 overlays achter elkaar binnen 6 seconden. Als een moment dat vereist, gebruik 1 overlay met meer informatie erin (bijv. één info-card met 3 bullet points) ipv 3 losse overlays.

## Bestaande Overlay Types in Short Form

### Wel gebruiken — werkt goed op 9:16

- **stx-tip** — werkt perfect, foto rechts/onder, tekst links/boven
- **info-card** — centraal geplaatst, kleiner formaat dan long form (80% breedte ipv 60%)
- **question-card** — prima, past goed in hero zone
- **quote-card** — werkt, houd quote kort (max 12 woorden)
- **design-showcase** — uitstekend, 9:16 crops vaak natuurlijker dan 16:9
- **product-showcase** — werkt, maar max 2 producten in een carousel (niet 4)
- **cta-card** — aangepast formaat, zie `follow-cta` type hieronder
- **part-intro** — alleen bij multi-part series, minder snel inzetten dan long form

### Aangepast gebruiken

- **step-overlay** — NIET 50/50 split zoals long form (video schuift opzij). In plaats daarvan: step badge links-boven + tip-tekst rechts-onder, video blijft vol in beeld.
- **materialenlijst** — alleen als de lijst kort is (max 3 items). Voor 4+ items: gebruik info-card of split over meerdere momenten.

### NIET gebruiken — werkt niet op 9:16

- **youtube-subscribe** — dit is YouTube-specifiek, heeft geen plek op Reels/TikTok
- **social-bar** — vervangen door `follow-cta` (zie hieronder)
- **end-screen** met "PART X OUT NEXT WEEK" — fout format, fout platform
- **browser-animation** — te veel detail voor klein scherm, laptop frame past niet
- **email-cta** — email composer past niet op 9:16, te veel tekst
- **lower-third** — ongebruikelijk op shorts; als naam nodig is, gebruik tekst badge bovenaan

## Nieuwe Overlay Types voor Short Form

### hook-caption

Fullscreen-width tekst vak, top-center (y: 300-500px), maximum impact.

**Layout:**
- Horizontaal gecentreerd
- Breedte: 900px max (padding 90px aan weerszijden)
- Achtergrond: geel vak (#ffdb5a) met rounded corners 40px, OF donkerpaars vak (#1b073d)
- Tekst: Rethink Sans Extra Bold, 110-140px
- Kleur: donkerpaars (#1b073d) op geel, OF wit op donkerpaars
- Padding binnen vak: 40px verticaal, 60px horizontaal

**Animatie:**
- IN: pop scale 0 → 115% → 100%, spring `{ damping: 10, stiffness: 140 }`, duur 15 frames
- TIJDENS: subtle shake 2-3px of geen beweging
- UIT: scale 100% → 105% → 0% + opacity fade, duur 8 frames

**Duur op scherm:** 2-3 seconden, niet langer — kijker heeft hook al gelezen.

**Geluid:** bass hit + zachte woosh bij in-effect. Geen geluid bij uit-effect.

### follow-cta

Kleine badge op de laatste 2-3 seconden van de short. Vervanger voor long form social-bar.

**Layout:**
- Positie: middle-bottom, y: 1450-1550 (net boven captions zone)
- Formaat: kleine rechthoek, 600px breed, 120px hoog
- Achtergrond: donkerpaars (#1b073d) met subtiele neon glow
- Tekst: "Follow @sempertexeurope" in Rethink Sans Bold, 42px, wit
- Icoon: Instagram + TikTok iconen links van de tekst

**Animatie:**
- IN: slide up vanaf onder het frame, 12 frames, spring
- UIT: geen — blijft staan tot einde video
- Subtle breathing: scale 100% → 101% → 100%, 2s cycle

**Geluid:** soft woosh bij in-effect.

## Pacing Voorbeelden per Video Duur

### 30 seconden short

```
0:00-0:03   HOOK          hook-caption
0:03-0:08   (ademen)      geen overlay, spreker bouwt op
0:08-0:12   KEY POINT     stx-tip of info-card
0:12-0:18   (ademen)      geen overlay
0:18-0:22   SECOND POINT  design-showcase of quote-card
0:22-0:27   (ademen)
0:27-0:30   CTA           follow-cta (blijft tot einde)
```
Totaal: 3 overlays + outro CTA = 4 visuele momenten.

### 60 seconden short

```
0:00-0:03   HOOK          hook-caption
0:03-0:10   (ademen)
0:10-0:14   POINT 1       stx-tip
0:14-0:22   (ademen)
0:22-0:26   POINT 2       info-card
0:26-0:34   (ademen)
0:34-0:38   POINT 3       design-showcase of product-showcase
0:38-0:47   (ademen)
0:47-0:52   PAYOFF        quote-card met key statement
0:52-1:00   CTA           follow-cta
```
Totaal: 5 overlays + outro CTA = 6 visuele momenten.

### 90 seconden short

Vergelijkbaar met 60s maar met 1-2 extra points en mogelijk 1 topic transition. Max 7-8 overlays totaal.

## Remotion Composition Template

Nieuwe compositions voor shorts moeten dit template volgen:

```tsx
import { Composition, AbsoluteFill, Video, staticFile } from "remotion";

// Registratie in Root.tsx:
<Composition
  id="STX-Short-[NAAM]"
  component={STXShortComponent}
  durationInFrames={[duur in frames, bijv. 1800 voor 60s]}
  fps={30}
  width={1080}
  height={1920}
  defaultProps={{ videoSrc: "videos/shorts/[bestand].mp4" }}
/>
```

**Safe zone dev guides** (alleen in development mode, niet in final render):

```tsx
{process.env.NODE_ENV === "development" && (
  <AbsoluteFill style={{ pointerEvents: "none", zIndex: 9999 }}>
    {/* Top platform UI zone */}
    <div style={{
      position: "absolute", top: 0, left: 0, right: 0, height: 150,
      border: "2px dashed rgba(255,0,0,0.3)",
      background: "rgba(255,0,0,0.05)",
    }} />
    {/* Bottom captions zone */}
    <div style={{
      position: "absolute", bottom: 0, left: 0, right: 0, height: 300,
      border: "2px dashed rgba(0,255,0,0.3)",
      background: "rgba(0,255,0,0.05)",
    }} />
  </AbsoluteFill>
)}
```

Dit laat tijdens ontwikkeling de safe zones zien zodat overlays niet per ongeluk in verboden zones belanden.

## Common Mistakes in Short Form

- **Trage hook** — fade-in van 20+ frames, disclaimer vooraf, "hi guys" opener. De eerste 15 frames moeten knallen.
- **Te veel overlays** — elke 2 seconden iets nieuws = overweldigend, goedkoop gevoel. Houd 5-10s cadence aan.
- **Overlay in captions zone** — onderste 300px moet vrij blijven. Test altijd of de overlay bottom edge boven y=1620 zit.
- **Overlay in platform UI zone** — bovenste 150px blijft vrij. Username van Instagram overlapt anders met je tekst.
- **16:9 assets hergebruikt** — foto's van long form zijn horizontaal, werken slecht op 9:16. Vraag om aparte shorts-crops.
- **Long form outro** — "PART 2 OUT NEXT WEEK" is YouTube-taal. Shorts krijgen een simpele `follow-cta`.
- **Text te klein** — op mobiel is 48px tekst onleesbaar. Minimum 64px voor body, 90px+ voor headers.
- **Muziek te stil** — long form muziek (-24dB) is te zacht voor shorts. Gebruik -18 tot -22dB.
- **Geen ademruimte** — overlays kleven aan elkaar zonder pauze. Plan 1-2 seconden lucht tussen overlays.
- **Branding vergeten** — korte video betekent niet dat branding niet nodig is. Minstens 1 geel vak patroon per short.

## Integratie met Bestaande Skills

- **stx-overlay-style** blijft de authority voor code-patronen per overlay type. Deze skill voegt alleen de short form uitzonderingen toe.
- **auto-video-editor** — zelfde rol, zelfde regels, zelfde branding. Alleen format en pacing wijken af.
- **video-log** — short form learnings taggen met `[SHORT]` prefix zodat ze niet vermengd raken met long form inzichten.
- **Kennis/Balloon Knowledge/INDEX.md** — bij hook-caption en stx-tip overlays voor techniek/product content: gebruik de exacte vakterm uit het juiste bestand (bv. "20-bubble star", "Diamond Weave", "Link-O-Loon Column", "Deep Tulip Twist", "Pinch Twist") in plaats van algemene beschrijvingen. Vakterm in 3-6 woorden hook = scroll-stopper voor de juiste audience (artists, twisters, decorators). Match Hook content type (zie tabel boven) met de techniek-categorie uit INDEX.md.

## Workflow voor nieuwe short form overlay type

Als tijdens een short form video een nieuw patroon ontstaat dat Robin of Tijl wil bewaren:

1. Documenteer tijdelijk in deze skill onder "Nieuwe Overlay Types voor Short Form"
2. Na 2-3 succesvolle toepassingen in verschillende shorts: valideer het patroon
3. Promoveer naar `stx-overlay-style/SKILL.md` als volwaardig overlay type, met `[short-form]` tag indien alleen daar bruikbaar
4. Voeg toe aan `stx-overlay-types-reference.md` quick reference tabel
