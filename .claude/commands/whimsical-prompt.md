# Whimsical Prompt Generator

Genereer een kant-en-klare prompt die Robin direct in Whimsical AI kan plakken om een visuele flowchart te maken.

## Input
De gebruiker beschrijft een campagne, funnel of proces. Bijvoorbeeld: "SYBB workshop funnel", "content repurposing flow", "email automation flow".

Als er een argument is meegegeven, gebruik dat als onderwerp: $ARGUMENTS

## Voorbereiding

Lees voor je begint:
1. `Kennis/Brand/kleurcodes.md` — kleurcodes voor styling
2. `.claude/skills/campaign-design/SKILL.md` — funnel structuur

Indien relevant:
- `Kennis/Voorgaande campagnes/campagne-historie.md`
- `Kennis/Products/producten-overzicht.md`

## Prompt structuur

Bouw de Whimsical prompt op met deze onderdelen:

### 1. Flowchart beschrijving
Beschrijf de volledige flow in logische stappen. Whimsical werkt het best met duidelijke, sequentiële instructies.

### 2. Blokken en types
Geef expliciet aan welke bloktypen Whimsical moet gebruiken:
- **Rechthoeken** voor acties en content (bv. "Meta Ad", "Landing Page", "Email")
- **Ruiten** voor beslissingsmomenten (bv. "Opt-in?", "Purchased?")
- **Ovalen/afgerond** voor start- en eindpunten
- **Gestapelde rechthoeken** voor groepen/categorieën

### 3. Verbindingen
Beschrijf welke blokken met welke verbonden zijn en met welk label op de pijl.

### 4. Kleuren (Sempertex brand)
Geef de kleuren mee die Whimsical moet gebruiken:
- Awareness blokken: lichtpaars achtergrond (#f1d9ff)
- Consideration blokken: paars (#6b3fb9) met witte tekst
- Purchase/conversie blokken: magenta (#cd0b5c) met witte tekst
- Post-purchase/satisfaction: goud (#ffdb5a) met donkere tekst
- Beslissingsmomenten: donkerpaars (#1b073d) met witte tekst
- Retargeting/terugloop pijlen: grijs, gestippeld
- Achtergrond secties: lichtgrijs (#f5f3f6)

### 5. Layout
Geef aan:
- Richting: top-to-bottom (standaard) of left-to-right
- Groepering: welke blokken in dezelfde sectie/swimlane horen
- Uitlijning: hoe parallelle flows naast elkaar staan

## Output Format

```
## 🎨 Whimsical Prompt — [beschrijving]

### Kopieer onderstaande prompt naar Whimsical:

---

[De volledige prompt, klaar om te plakken. Schrijf in het Engels — Whimsical werkt het best in het Engels.

Wees expliciet over:
- Elk blok en zijn type (rectangle, diamond, oval)
- Elke verbinding en richting
- Kleuren per blok/sectie (HEX codes)
- Layout richting en groepering
- Labels op pijlen]

---

### Blokkenlijst
| Blok | Type | Kleur | Sectie |
|------|------|-------|--------|
| [naam] | [type] | [HEX] | [fase] |
| ... | ... | ... | ... |

### Verbindingenlijst
| Van | Naar | Label | Stijl |
|-----|------|-------|-------|
| [blok] | [blok] | [label] | [solid/dashed] |
| ... | ... | ... | ... |
```

## Regels
- De Whimsical prompt is altijd in het Engels
- Gebruik ALTIJD de Sempertex kleurcodes (HEX) — geen generieke kleurnamen
- Houd de flowchart leesbaar: max 25-30 blokken
- Beslissingsmomenten (ja/nee splits) zijn cruciaal — altijd opnemen
- Retargeting loops altijd als gestippelde pijlen
- Groepeer blokken per funnel fase met een achtergrondkleur
- Geef Whimsical expliciete instructies — het raadt niet goed als je vaag bent
