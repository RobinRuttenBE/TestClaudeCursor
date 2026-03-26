# /find-assets -- Zoek en download gratis stock assets

Gebruiker wil stock assets zoeken en downloaden voor Remotion video's.

## Jouw taak

1. Lees het verzoek van de gebruiker en bepaal de juiste parameters:
   - `--query` : zoekterm (verplicht)
   - `--type` : icon | music | sound-effect | texture | background (default: icon)
   - `--count` : 1-20 (default: 5)
   - `--source` : pexels | unsplash | pixabay | all (default: all)

2. Voer het script uit:
   ```bash
   cd remotion-stx && npx tsx scripts/find-assets.ts --query "..." --type ... --count ... --source ...
   ```

3. Toon resultaten als tabel met: bestandsnaam, bron, maker, Remotion import pad

4. Bij geblokkeerde zoekopdrachten (ballonnen, video), leg uit waarom en verwijs naar eigen assets

## Bronnen per type

| Type | Pixabay | Pexels | Unsplash |
|------|---------|--------|----------|
| icon | vectors | - | - |
| music | audio (>30s) | - | - |
| sound-effect | audio (<=10s) | - | - |
| background | - | photos | photos |
| texture | - | photos | photos |

## Voorbeelden

**Gebruiker:** "Ik zoek pijl iconen"
```bash
cd remotion-stx && npx tsx scripts/find-assets.ts --query "arrow icon" --type icon --count 5 --source pixabay
```

**Gebruiker:** "Achtergrondmuziek, iets vrolijks"
```bash
cd remotion-stx && npx tsx scripts/find-assets.ts --query "upbeat happy" --type music --count 5 --source pixabay
```

**Gebruiker:** "Whoosh geluidseffecten voor transities"
```bash
cd remotion-stx && npx tsx scripts/find-assets.ts --query "whoosh transition" --type sound-effect --count 5 --source pixabay
```

**Gebruiker:** "Donkere abstracte achtergrond"
```bash
cd remotion-stx && npx tsx scripts/find-assets.ts --query "abstract dark purple" --type background --count 5 --source unsplash
```

**Gebruiker:** "Textuur voor overlay"
```bash
cd remotion-stx && npx tsx scripts/find-assets.ts --query "grunge texture" --type texture --count 3 --source pexels
```

## Na het downloaden

Toon altijd:
- Tabel met resultaten (bestandsnaam | bron | maker)
- Remotion import: `staticFile("icons/stock/arrow-icon/pixabay-arrow-icon-01.png")`
- Tip: asset-index.json is bijgewerkt

## Geblokkeerde zoekopdrachten

Als de gebruiker zoekt naar ballonnen, latex, helium, etc.:
> "Ballongerelateerde content is eigen Sempertex materiaal. Productfoto's staan in `public/images/`. Stock assets worden alleen gebruikt voor ondersteunende elementen zoals iconen, muziek, achtergronden en texturen."

Als de gebruiker video's wil:
> "Video downloads worden niet ondersteund. Eigen B-roll staat in `public/b-roll/`. Gebruik `/fetch-lottie` voor animaties."

$ARGUMENTS
