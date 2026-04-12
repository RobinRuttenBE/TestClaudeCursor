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
| 1 | part-intro | Gebouwd | PART 3 + "How to price your balloon designs" |
| 2 | materialenlijst (cost breakdown) | Gebouwd | Foil/Latex/Extras met Audrey Pose.jpg |
| 3 | quote-card (pop in) | Gebouwd | Plumber analogy, geen typewriter |
| 4 | animated-pricing-equation (NEW) | Gebouwd | TIME + MATERIALS + OVERHEADS x 2 = YOUR PRICE |
| 5 | stx-tip (right) | Gebouwd | Perceived value met Wedding.jpg |
| 6 | typewriter-quote-card | Gebouwd | "never go up" met yellow highlight + ding |
| 7 | price-ladder-card (NEW) | Gebouwd | Descending: 50/40/25 pound |
| 8 | text-only-tip | Gebouwd | Stop comparing, eye icon, geen foto |
| 9 | stx-tip (right) | Gebouwd | Audrey learning twisting met Jungle twisting.jpg |
| 10 | materialenlijst (30s advice) | Gebouwd | Niche/Products/Education met nummers |
| 11 | youtube-subscribe | Gebouwd | Standaard closing sequence |
| 12 | social-bar | Gebouwd | IG + FB handles |
| 13 | end-screen | Gebouwd | THANKS FOR WATCHING + SUBSCRIBE (laatste deel) |

### Aangepast door gebruiker (voor build)
- Lower third geschrapt — Robin voegt zelf toe
- Moment 4 (plumber) van typewriter naar gewone pop-in — Robin wil typewriter reserveren voor sterkere quote
- Moment 8 (alternatives) van leerstof-lijst naar price-ladder-card — innovatief + visueel sterker
- Asset swap: jungle twisting.jpg naar Moment 9 (learning) ipv Moment 8 (stop comparing)
- Pricing in pounds, geen euro disclaimer

### Nieuwe overlay types ontstaan
- `animated-pricing-equation` — animated equation builder met stagger yellow blocks, bass hit op x 2, magenta accent
- `price-ladder-card` — descending stepped price tiers, right-side panel, stagger slide-in from right
- `text-only-tip` — stx-tip variant zonder foto, met focus/eye icon in paarse strip

### Leerpunten voor volgende video's
- Robin verwacht 1-2 innovatieve momenten per video — altijd voorstellen
- Lower third wordt handmatig toegevoegd — niet meenemen in plan
- Pricing in lokale valuta laten staan, geen disclaimers — audience begrijpt het
- Lijst > quote voor praktisch advies, quote > lijst voor emotionele momenten
- YouTube subscribe + social bar + end screen als vaste closing sequence in die volgorde
