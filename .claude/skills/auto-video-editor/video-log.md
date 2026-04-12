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
