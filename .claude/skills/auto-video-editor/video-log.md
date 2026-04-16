# Video Log — Auto Video Editor

Bijgewerkt na elke afgeronde video. Bevat leerpunten voor toekomstige edits.

---

## Format per video

```markdown
## [YYYY-MM-DD] Video naam

**Composition:** `<Composition-id>` in `remotion-stx/src/Root.tsx`
**Bestand:** `remotion-stx/src/overlays/<file>.tsx`
**Totale duur:** XmYs
**Aantal momenten:** N

### Voorgestelde momenten

| # | Type | Status | Notitie |
|---|------|--------|---------|
| 1 | part-intro | ✅ goedgekeurd | direct akkoord |
| 2 | stx-tip | 🔧 aangepast | foto vervangen, positie naar rechts |
| 3 | info-card | ❌ verwijderd | te druk in dat segment |

### Aangepast door gebruiker
- **Moment X**: wat veranderde + waarom
- **Moment Y**: ...

### Direct goedgekeurd
- **Moment X**: wat werkte goed
- **Moment Y**: ...

### Verwijderd
- **Moment X**: reden

### Nieuwe overlay types ontstaan
- `<type-name>` — beschrijving + waar in SKILL.md gedocumenteerd

### Leerpunten voor volgende video's
- ...
```

---

## Logs

## [2026-04-12] Audrey & Robin Part 3 — How to Price Your Balloon Designs

**Composition:** `Audrey-Robin-Part-3` in `remotion-stx/src/Root.tsx`
**Bestand:** `remotion-stx/src/overlays/audrey-robin-part3-overlays.tsx`
**Totale duur:** 11m55s + 3s end screen hold (21540 frames @ 30fps)
**Aantal momenten:** 13

### Voorgestelde momenten

| # | Type | Status | Notitie |
|---|------|--------|---------|
| 1 | part-intro | ✅ goedgekeurd | PART 3 + "How to price your balloon designs" |
| 2 | materialenlijst (cost breakdown) | ✅ goedgekeurd | Foil/Latex/Extras met Audrey Pose.jpg |
| 3 | quote-card (pop in) | ✅ goedgekeurd | Plumber analogy, 7s, geen typewriter |
| 4 | animated-pricing-equation (NEW) | ✅ goedgekeurd | Bottom-left, clicks+woosh, subtle shake, 12s |
| 5 | stx-tip (right) | ✅ goedgekeurd | Perceived value, 7s |
| 6 | typewriter-quote-card | ✅ goedgekeurd | Width 1200, font 56px, 7s |
| 7 | price-ladder-card (NEW) | ✅ goedgekeurd | Links, rechte stapel (geen diagonaal), 7s |
| 8 | text-only-tip | ✅ goedgekeurd | Stop comparing, 6s |
| 9 | stx-tip (right) | ✅ goedgekeurd | Jungle twisting.jpg, 7s |
| 10 | materialenlijst (30s advice) | ✅ goedgekeurd | Bottom-left 4%, scale 0.75, 8s, +10s later |
| 11 | youtube-subscribe | ✅ goedgekeurd | 5s |
| 12 | social-bar | ✅ goedgekeurd | 5s |
| 13 | end-screen | ✅ goedgekeurd | +7s later, THANKS FOR WATCHING + SUBSCRIBE |

### Aangepast door gebruiker (voor build)
- Lower third geschrapt — Robin voegt zelf toe
- Moment 4 (plumber) van typewriter naar gewone pop-in — Robin wil typewriter reserveren voor sterkere quote
- Moment 8 (alternatives) van leerstof-lijst naar price-ladder-card — innovatief + visueel sterker
- Asset swap: jungle twisting.jpg naar Moment 9 (learning) ipv Moment 8 (stop comparing)
- Pricing in pounds, geen euro disclaimer

### Aangepast door gebruiker (na eerste review)
- Muziekvolume te hoog — verlaagd van -22dB naar -26dB
- Alle overlays te lang in beeld — alles naar 5-8s (was 20-25s)
- M4 pricing formula: pops bij tekst vervangen door clicks, bass hit op x2 vervangen door woosh, shake 75% zachter, positie naar bottom-left zodat hoofden zichtbaar blijven
- M6 quote card te groot — 30% kleiner (width 2600 → 1200, font 120 → 56)
- M7 price ladder: diagonale trappen → rechte stapel, rechts → links
- M10 30s advice: 10s later starten, 25% kleiner (scale 0.75), naar bottom-left 4%
- M13 end screen: 7s later beginnen
- Closing sequence (YT + social + end): allemaal korter (5s / 5s / auto)

### Nieuwe overlay types ontstaan
- `animated-pricing-equation` — animated equation builder met stagger yellow blocks, woosh op x2, magenta accent. Bottom-left positie. Clicks voor componenten, niet pops.
- `price-ladder-card` — verticale prijstiers, left-side panel, stagger slide-in from left, gelijke breedte per stap (geen diagonaal)
- `text-only-tip` — stx-tip variant zonder foto, met focus/eye icon in paarse strip

### Direct goedgekeurd (geen aanpassingen)
- Moment 1 (part-intro): direct akkoord
- Moment 2 (cost breakdown): direct akkoord
- Moment 9 (always learning): direct akkoord

### Leerpunten voor volgende video's
- Robin verwacht 1-2 innovatieve momenten per video — altijd voorstellen
- Lower third wordt handmatig toegevoegd — niet meenemen in plan
- Pricing in lokale valuta laten staan, geen disclaimers — audience begrijpt het
- Lijst > quote voor praktisch advies, quote > lijst voor emotionele momenten
- YouTube subscribe + social bar + end screen als vaste closing sequence in die volgorde
- **TIMING: overlays maximaal 5-8 seconden in beeld. 20-25s is veel te lang. Robin wil kort en krachtig.**
- **MUZIEK: -22dB is te luid. Start met -26dB als standaard.**
- **GROOTTE: overlays moeten NOOIT de hoofden van sprekers bedekken. Positioneer bottom-left of bottom-right, niet center.**
- **SHAKE: subtiel houden. Max 1.5-2px op kaart, nooit 4-6px. Robin vindt hard schudden extreem.**
- **SFX: bij tekst die verschijnt = clicks, niet pops. Pops voor hele kader verschijnen. Woosh voor grote impact momenten.**
- **DIAGONAAL: Robin wil geen diagonale/trap layouts. Houd lijsten en stapels recht en geordend.**
- **SCALE: bij "kleiner maken" is 0.75 (25% kleiner) een goede standaard. Niet alles hoeft fullsize.**

---

## [2026-04-15] Denise Twisting Compilation — Balloon Twisting 101

**Composition:** `Denise-Twisting-Compilation` in `remotion-stx/src/Root.tsx`
**Bestand:** `remotion-stx/src/overlays/denise-twisting-compilation-overlays.tsx`
**Totale duur:** 15m54s (28609 frames @ 30fps)
**Aantal momenten:** 22 (M1-M22) + 5 step-transition overlays

### Voorgestelde momenten

| # | Type | Status | Notitie |
|---|------|--------|---------|
| 1 | text-burst-title | 🔧 aangepast | tekst groter (180→260), start naar frame 0 |
| 2 | stx-tip (icon) | 🔧 aangepast | foto was broken (Team foto_s leeg), balloon-icon i.p.v. foto |
| 3 | typewriter-quote-card | 🔧 aangepast | eerder + korter zodat 'ie weg is vóór logo intro; typing sfx cut-off |
| 4 | stx-tip (N260 Honey) | 🔧 aangepast | "260Q" → "N260" (Q is Qualatex) |
| 5 | tool-comparison-card | 🔧 aangepast | lager op scherm (bottom 10%), eerlijkere hand-pump vergelijking |
| 6 | gradient-info-card | 🔧 aangepast | verplaatst naar M7's slot (verwisseling) |
| 7 | text-only-tip | 🔧 aangepast | verplaatst naar M6's oude slot (verwisseling) |
| 8 | materialenlijst | 🔧 aangepast | timing naar ~4:11 (was 4:05) |
| 9 | typewriter-quote-card | 🔧 aangepast | later + typing sfx cut-off |
| 10 | section-badge + photo | 🔧 aangepast | balloon dog photo toegevoegd, timing naar ~5:36 |
| 11 | gradient-info-card | 🔧 aangepast | eerder (~6:04) + slechts één click sfx |
| 12 | stx-tip (260 in use) | 🔧 aangepast | object-position 80% 50% om subject 30% naar links te shiften |
| 13 | text-only-tip (balloon) | 🔧 aangepast | eye-icon → balloon-icon (past bij "lift before twist") |
| 14 | gradient-info-card | 🔧 aangepast | center → center-left, 10% groter (scaleFactor 1.1) |
| 15 | gradient-info-card | 🔧 aangepast | center → bottom positie, timing naar ~10:18 |
| 16 | stx-tip | 🔧 aangepast | Audrey foto → `Denise Pinch Twist.jpg` |
| 17 | stx-tip | 🔧 aangepast | Audrey foto → `Denise Pinch Twist 2.jpg` |
| 18 | materialenlijst | ✅ goedgekeurd | timing auto-geshift voor nieuw segment layout |
| 19 | typewriter-quote-card | 🔧 aangepast | typing sfx cut-off |
| 20 | youtube-subscribe | ✅ goedgekeurd | auto-geshift |
| 21 | social-bar | ✅ goedgekeurd | auto-geshift |
| 22 | end-screen | 🔧 aangepast | 50% grotere tekst (200→300), "SUBSCRIBE FOR MORE" button, dynamic glow sweep, 5s duration, muziek-boost bij fade-in |

### Nieuwe overlay types ontstaan
- `step-transition-overlay` — grote "PART X →" badge bovenaan scherm bij elke segment-overgang. Dur 60f, geel/dark-purple, met arrow. Komt 20f vóór start van nieuw segment. Gebruikt bij P2-P6 transitions in multi-segment edits.

### Aangepast door gebruiker (initial feedback round)

**M1 — Text Burst Title**
- Tekst veel groter (180 → 260). Start vanaf frame 0 ipv frame 120. Pop/swipe sfx volumes verlaagd.

**M2 — Sempertex Tip "Welcome"**
- Circle frame was leeg (Team foto_s/LOL Denise PP.png bestaat niet, Team foto_s folder is leeg). `SempertexTipOverlay` uitgebreid met `icon?: React.ReactNode` prop. Welcome balloon-icon als fallback.

**M3/M9/M19 — Typewriter cards**
- SFX_TYPING liep door tot eind van de audio file. Nu gewrapped in `<Sequence durationInFrames={76}>` zodat 'ie stopt precies wanneer de tekst klaar is met typen. 76 frames = van local 10 tot local 86 (LINE1_START → LINE2_END).
- M3 specifiek: moest volledig weg zijn voordat logo intro start (frame 732). Nieuwe start 540, dur 170, volledig weggeswipet bij frame 710.

**Logo intro → Part 1 cross-fade**
- Video segmenten overlappen nu met `CROSS_FADE` (8f) zodat de cross-fade gebeurt mét beide video's tegelijk zichtbaar. Geen dark-purple gap meer. Geldt voor alle opeenvolgende segmenten.

**Dead space tussen segmenten**
- `SEG_P1_DURATION` stond op 5670 geschat, werkelijke file is 5201 frames — dat leverde 469 frames (15.6s) bevroren frame op tussen Part 1 eind en Part 2 start. Met `@remotion/media-parser` → `parseMedia({ fields: { slowDurationInSeconds: true } })` nu alle 8 videobestanden exact gemeten. Nieuwe TOTAL_FRAMES: 28609 (was 29010).

**M4 — N260 Honey (NIET 260Q!)**
- "260Q Honey Yellow" → "N260 Honey Yellow". `Q` is Qualatex, concurrent. Sempertex-sizing altijd met `N`-prefix. Opgeslagen als feedback memory. SKILL.md Kleuren-sectie uitgebreid met product-name rule.

**M5 — Tool Comparison Card**
- Positie: center → bottom 10% van scherm, horizontaal gecentreerd
- Hand Pump bullets: alle drie CrossIcon's ("Little pauses", "Uneven dents", ...) vervangen door CheckIcon bullets ("Travel-ready, no power", "Full tactile control", "Silent & always ready"). Beide tools presenteren als eerlijke keuze ipv hand pump downplayen.
- `CrossIcon` helper weggehaald (niet meer gebruikt). `magenta` kleur var ook verwijderd.

**M6/M7 swap**
- M6 (nozzle trick, "Tying Trick") is vollediger nozzle-moment, hoort bij later in Part 1. M7 (count pumps) past bij pomp-setup, hoort eerder. Gewisseld via timestamps: M7 naar oude M6 slot (frame 2673), M6 naar oude M7 slot (frame 4473). Beide blijven enabled.

**M8** — later, ~4:11 ipv 4:05. Timing auto-converted via content-offset in nieuwe timeline.

**M9** — later, ~5:05. + typing sfx cut-off.

**M10 — Section Badge Balloon Dog**
- `SectionBadge` uitgebreid met optionele `imageSrc` prop die rechts van de label een ronde foto toont (geel border, `objectFit: contain` zodat hele balloon zichtbaar blijft). `images/Balloon dog.png` gebruikt.

**M11** — eerder (~6:04). Van twee click sfx naar één.

**M12** — nu op oude M11 tijd (~6:38). Foto (260 in use.png) 30% naar links geshift via nieuwe `imageObjectPosition="80% 50%"` prop op `SempertexTipOverlay`.

**M13** — later (~8:33). `TextOnlyTipOverlay` heeft nu `icon` prop met `"eye" | "balloon"` variant — balloon SVG gebruikt voor "Lift before you twist" (past bij lift-onderwerp, eye past niet).

**M14 — Shake Test**
- `GradientInfoCard` uitgebreid met `position="center-left"` en `scaleFactor` prop (1.1 = 10% groter). M14 was center, nu center-left, 10% groter.

**M15 — Rule of Thumb**
- `GradientInfoCard` `position="bottom"` toegevoegd (bottom:10%, horizontaal gecentreerd). M15 was center, nu bottom. Timing later (~10:18).

**M16/M17 — Image swaps**
- Audrey twisting tip 3/4 PNG's vervangen door de nieuwe `Denise Pinch Twist.jpg` en `Denise Pinch Twist 2.jpg` die Robin zelf heeft toegevoegd in `public/images/`. Audrey foto's zijn ongepast omdat Denise de spreker is.

**M22 — End Screen (groot redesign)**
- Start na volledige Part 6 (niet meer vroegtijdig cut off). Overlapt laatste CROSS_FADE van P6 zodat P6 naadloos fade't in de outro.
- Tekst 50% groter (200 → 300). Button "SUBSCRIBE" → "SUBSCRIBE FOR MORE". Button font iets kleiner (120 → 110) om breder label te accommoderen.
- Dynamic radial glow sweep over de purple achtergrond: loopt elke 90 frames diagonal over het scherm met `mixBlendMode: screen`. Maakt het outro card ademend/levendig.
- Duur: 510 → 150 frames (5s ipv 17s). Robin: outro 5 seconden is genoeg.
- Muziek bump: volume ramps van MUSIC_VOLUME (×1) naar MUSIC_VOLUME × 2.1 wanneer outro fade-in begint.

### Step overlays tussen parts
- Nieuw type `step-transition-overlay` toegevoegd voor elke segment-overgang. Grote gele "PART X" badge + witte arrow bovenaan scherm, 60 frames duration, start 20f vóór nieuw segment. Gebruikt bij P2/P3/P4/P5/P6 transitions. Met kleine woosh-in sfx.

### Global changes
- **Music volume:** 0.05 → 0.035 (-26 → -29 dB). Overall rustiger.
- **SFX volume multiplier:** alle individuele volumes vervangen door `SFX` object met gereduceerde waardes (pop 0.6→0.38, woosh 0.5→0.32, click 0.5→0.32, ding 0.55→0.38, typing 0.4→0.28). Uniform quieter.
- **Music curve:** extra boost bij outro fade-in (×2.1) naast de bestaande boost tijdens logo intro (×2.2).

### Leerpunten voor volgende video's
- **METEN, niet schatten.** Bij multi-segment concatenation altijd eerst `@remotion/media-parser` durations meten. Schattingen uit transcripts creëren bevroren frames die uren aan de klant verspelen.
- **Segmenten moeten overlappen met CROSS_FADE.** Zonder overlap zie je de achtergrond-kleur tussen clips flashen.
- **Step overlays bij segment transitions** voor long-form compilaties — markeren duidelijk welke part begint, voorkomen dat de kijker "kwijtraakt" welke van de 6-7 videos ie kijkt.
- **Typewriter sfx MOET cut-off krijgen** via `<Sequence durationInFrames={N}>` wrapper. Nooit de hele sfx file laten uitspelen — dat is hinderlijk.
- **Typewriter overlays NIET laten overlappen met logo intro** — plan de swipe-out zodat 'ie volledig weg is voordat de logo aan de volgende scene begint.
- **Image bestanden checken voordat je ze gebruikt.** Als een folder leeg is (zoals `Team foto_s/`), de Img renderen werkt niet — val terug op icon.
- **Nooit "Q" suffix bij Sempertex ballonnen.** Altijd N260/N350/etc. Q is Qualatex.
- **Hand pump vs. electric inflator: eerlijke vergelijking, niet een afvallen.** Beide hebben use cases. Hand pump: travel-ready, silent, tactile, no power. Electric: speed, consistency, sizing.
- **End screen = 5 seconden, niet 15-17.** Robin vindt lange outros saai.
- **SFX volume default te hoog.** Houd in het 0.28-0.40 bereik.
- **`imageObjectPosition` prop** op tip-overlay is nuttig wanneer subject niet gecentreerd in bronfoto is — eenvoudiger dan foto cropper.
- **Eye-icon wordt overgebruikt.** Als de boodschap over een fysieke actie gaat (lift, pinch, twist), kies een actie-passende icon (balloon voor lift, hand voor pinch, etc.).

### Tweede feedback ronde (2026-04-16)

**M2 + M13 — Balloon icon → Sempertex Flor logo**
- Balloon SVG iconen vervangen door `logos/Flor logo.png` (transparante achtergrond). De flor is het officiele merk-embleem. `TextOnlyTipOverlay` uitgebreid met `icon="flor"` optie.

**M10 — Balloon Dog badge redesign**
- Afbeelding onder de tekst (verticale layout ipv horizontaal naast elkaar)
- Veel groter: 1040×780px (was 230×230 cirkel)
- Rechthoekig met afgeronde hoeken (24px radius)
- Paarse gloed rand die pulseert (`boxShadow: purple cc/66`)
- `objectFit: cover` voor professionelere look

**Achtergrondmuziek — root cause fix**
- `<Audio loop>` volume callback `(f)` geeft het frame BINNEN het audiobestand (reset elke loop), NIET het compositie-frame. Hierdoor vuurden de outro-boost keyframes (frame 28459) nooit.
- Fix: `useCurrentFrame()` voor compositie-frame, volume als getal meegeven.
- Logo intro boost: 0.35 (was MUSIC_VOLUME × 2.2 = 0.077)
- Outro card boost: 0.45 (was MUSIC_VOLUME × 2.1 = 0.074)

**Audio gap bij transities — NIET in code fixbaar**
- Geprobeerd: OffthreadVideo muten + aparte Audio elementen → veroorzaakte volume-sprongen bij segment overgangen (video files hebben verschillende audio levels)
- Geprobeerd: volume={opacity} op OffthreadVideo → verdubbelt audio bij overlap
- Conclusie: audio gap is een Remotion Studio preview artifact (browser video decode latency). Verschijnt NIET in de gerenderde output. NIET proberen op te lossen in code.

### Extra leerpunten
- **`<Audio loop>` volume callback:** `f` is het AUDIO FILE frame, niet het compositie-frame. Bij looped audio met compositie-brede volume curves ALTIJD `useCurrentFrame()` gebruiken en volume als getal meegeven.
- **NOOIT OffthreadVideo muten + aparte Audio:** veroorzaakt volume-sprongen bij elke segment transition. Video files hebben verschillende audio levels.
- **Gebruik Sempertex Flor logo** (`logos/Flor logo.png`) als decoratief icoon in overlays, niet custom balloon SVGs.
- **SectionBadge afbeeldingen groot genoeg.** 230px cirkel is te klein/onprofessioneel. Minimaal 1000px breed voor foto-referenties.
