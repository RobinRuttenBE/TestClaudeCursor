---
description: Search and download Lottie animations from LottieFiles
user-invocable: true
---

# /fetch-lottie — Search & Download Lottie Animations

## Instructies

Je hebt de LottieFiles MCP server beschikbaar met deze tools:
- `search_animations` — zoek Lottie animaties op keyword
- `get_animation_details` — haal details + JSON URL op voor een specifieke animatie
- `get_popular_animations` — bekijk trending animaties

## Workflow

### 1. Zoek animaties
Gebruik de MCP tool `search_animations` met de zoekterm die de gebruiker opgeeft.

Als de gebruiker geen zoekterm geeft, vraag ernaar.

### 2. Toon resultaten
Toon de top 5 resultaten in een overzichtelijke lijst:
```
1. [Naam] — Tags: tag1, tag2
   Preview: [URL]
   ID: [id]
```

### 3. Laat gebruiker kiezen
Vraag welke animatie(s) gedownload moeten worden en in welke categorie:
- `transitions/` — overgangseffecten (swipes, fades, wipes)
- `icons/` — iconen (star, heart, check, etc.)
- `backgrounds/` — achtergrond animaties (particles, gradients)
- `effects/` — visuele effecten (sparkles, glow, burst)
- `ui-elements/` — UI componenten (loading, notification, toggle)
- `text-effects/` — tekst animaties (underline, highlight, emphasis)

Als de categorie niet duidelijk is, stel er een voor op basis van de animatie.

### 4. Download
1. Gebruik `get_animation_details` om de JSON URL te krijgen
2. Download het .json bestand met curl/fetch
3. Sla op in `remotion-stx/public/animations/[categorie]/[beschrijvende-naam].json`
4. Bestandsnaam: lowercase, kebab-case, beschrijvend (bijv. `arrow-pointing-right.json`)

### 5. Update animation-index.json
Voeg de nieuwe animatie toe aan `remotion-stx/public/animations/animation-index.json`:
```json
{
  "id": "beschrijvende-naam",
  "name": "Beschrijvende Naam",
  "category": "categorie",
  "path": "animations/categorie/beschrijvende-naam.json",
  "source": "lottiefiles",
  "sourceId": "[lottiefiles-id]",
  "sourceUrl": "[lottiefiles-url]",
  "tags": ["tag1", "tag2"],
  "addedAt": "[datum]"
}
```

### 6. Bevestig
Toon een samenvatting:
```
Downloaded: [naam]
Locatie: remotion-stx/public/animations/[categorie]/[bestand].json
Gebruik in Remotion:
  import animationData from "../../public/animations/[categorie]/[bestand].json";
  // of via staticFile():
  const path = staticFile("animations/[categorie]/[bestand].json");
```

## Voorbeeld gebruik

Gebruiker: `/fetch-lottie arrow animation`

1. Zoek "arrow animation" via MCP
2. Toon top 5 resultaten
3. Gebruiker kiest #2
4. Download naar `public/animations/icons/arrow-right.json`
5. Update index
6. Bevestig met pad en import voorbeeld

## Batch modus

Als de gebruiker meerdere animaties tegelijk wil downloaden:
1. Zoek per keyword
2. Toon alle resultaten gegroepeerd
3. Laat per groep kiezen
4. Download alles in een keer
5. Update index met alle nieuwe entries
