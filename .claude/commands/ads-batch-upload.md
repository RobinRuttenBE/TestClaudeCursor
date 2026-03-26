# /ads-batch-upload — Batch Ad Upload vanuit Google Drive

Lees een campagne-map uit Google Drive ("Ad Creatives"), upload alle assets naar Meta Ads, en maak campagnes + ad sets + ads aan. Alles op PAUSED — pas na expliciete goedkeuring van Robin wordt er iets live gezet.

## Verwachte mapstructuur in Google Drive

```
Ad Creatives/
├── SYBB Batch 3/
│   ├── briefing.md
│   ├── hook1-statement.jpg
│   ├── hook2-question.mp4
│   └── hook3-carousel-1.jpg, hook3-carousel-2.jpg, ...
├── Silk Lancering/
│   ├── briefing.md
│   ├── visual-hero.jpg
│   └── video-demo.mp4
└── ...
```

### briefing.md format

Het bestand `briefing.md` in elke submap bevat de campagne-instructies:

```markdown
# Campagne: [naam]
## Doel
[CONVERSIONS / TRAFFIC / AWARENESS] (default: CONVERSIONS)

## Budget
[€X/dag per ad set] (max €100/dag tenzij anders aangegeven)

## Targeting
- Leeftijd: [bv. 25-45]
- Geslacht: [Vrouwen / Mannen / Alle]
- Locaties: [bv. EU, of specifieke landen]
- Interesses: [bv. ballonnen, event decoratie, party supplies]
- Uitsluitingen: [optioneel]

## Ads
### Ad 1
- Bestand: [bestandsnaam.jpg of .mp4]
- Hook type: [Statement / Question / Command / Label / Conditional / Story / List]
- Hook: "[hook tekst]"
- Body: "[body tekst]"
- CTA: "[CTA tekst]"
- CTA button: [LEARN_MORE / SHOP_NOW / SIGN_UP / etc.]
- Link: [URL]

### Ad 2
...
```

Als er geen briefing.md aanwezig is in een submap, sla die map over en meld dit.

## Veiligheidsregels (STRIKT)
- **NOOIT** automatisch op ACTIVE zetten zonder expliciete goedkeuring van Robin
- **NOOIT** meer dan €100/dag per ad set tenzij briefing.md een hoger bedrag specificeert
- **ALTIJD** eerst een volledig overzicht tonen van ALLE campagnes die worden aangemaakt
- **ALTIJD** bevestiging vragen voordat er iets wordt aangemaakt
- **ALTIJD** na het aanmaken vragen of Robin wil activeren
- Bij ontbrekende of onduidelijke informatie: STOP en vraag Robin
- **NOOIT** meer dan 50 ads in één batch aanmaken zonder tussentijdse bevestiging

## Naming convention
Volgt hetzelfde patroon als /ads-deploy:
```
[DATUM]_[CAMPAGNE]_[AUDIENCE]_[HOOK-TYPE]
```

## Stappen

### 1. Zoek de "Ad Creatives" map in Google Drive
Gebruik `mcp__google__drive_files_search` met query: `name = 'Ad Creatives' and mimeType = 'application/vnd.google-apps.folder'`

Als de map niet bestaat, meld dit en stop:
> "Ik kan de map 'Ad Creatives' niet vinden in Google Drive. Maak deze map aan en voeg submappen toe per campagne met een briefing.md en je assets."

### 2. Lijst alle submappen op
Gebruik `mcp__google__drive_files_list` met de folder ID uit stap 1 om submappen te vinden.

Als de gebruiker een specifieke submap heeft opgegeven (bv. "/ads-batch-upload SYBB Batch 3"), verwerk alleen die map. Anders verwerk alle submappen.

### 3. Per submap: lees briefing.md
Gebruik `mcp__google__drive_files_search` om `briefing.md` te vinden in de submap.
Download het bestand met `mcp__google__drive_file_download` en lees de inhoud.

Als briefing.md ontbreekt:
> "⚠️ Map '[mapnaam]' heeft geen briefing.md — overgeslagen."

### 4. Per submap: inventariseer assets
Gebruik `mcp__google__drive_files_list` om alle bestanden in de submap op te lijsten.
Categoriseer:
- **Afbeeldingen**: .jpg, .jpeg, .png, .webp
- **Video's**: .mp4, .mov, .avi
- **Documenten**: .md, .txt (briefing)
- **Overig**: meld en sla over

Match elk asset-bestand met de bijbehorende ad in briefing.md (op bestandsnaam).
Meld als er assets zijn die niet in de briefing staan of vice versa.

### 5. Bouw targeting op
Per campagne uit briefing.md:
- `mcp__claude_ai_Pipeboard_Meta_Ads__search_interests` — zoek interesses
- `mcp__claude_ai_Pipeboard_Meta_Ads__search_geo_locations` — zoek locaties
- `mcp__claude_ai_Pipeboard_Meta_Ads__estimate_audience_size` — valideer audience grootte

### 6. Toon het volledige batch plan
Toon één overzicht van ALLE campagnes die worden aangemaakt:

```
## Batch Upload Plan — [datum]

### Bron: Google Drive / Ad Creatives

---

### Campagne 1: [mapnaam]

**Campagne:** [naam volgens naming convention]
**Doel:** [objective]
**Account:** act_567892422940728 (Sempertex Ad Account)

**Ad Set:**
| Naam | Budget/dag | Audience | Geschatte grootte |
|------|-----------|----------|-------------------|
| [naam] | €X | [targeting] | X.XM |

**Ads:**
| # | Naam | Asset | Type | Hook | CTA |
|---|------|-------|------|------|-----|
| 1 | [naam] | hook1.jpg | Image | "[hook]" | "[CTA]" |
| 2 | [naam] | hook2.mp4 | Video | "[hook]" | "[CTA]" |

**Assets:** X afbeeldingen, X video's

---

### Campagne 2: [mapnaam]
[zelfde structuur]

---

### Batch samenvatting
- **Totaal campagnes:** X
- **Totaal ad sets:** X
- **Totaal ads:** X
- **Totaal assets te uploaden:** X afbeeldingen, X video's
- **Totaal dagbudget:** €X
- **Geschat maandbudget:** €X

⚠️ Problemen gevonden:
- [mapnaam]: asset "foto.jpg" staat niet in briefing.md
- [mapnaam]: ad 3 verwijst naar "video.mp4" maar bestand niet gevonden
```

Vraag dan: **"Zal ik deze batch aanmaken op PAUSED? (X campagnes, X ads, €X/dag totaal)"**

### 7. Upload assets naar Meta (na bevestiging)
Per campagne, per ad:

**Afbeeldingen:**
- Download van Drive: `mcp__google__drive_file_download`
- Upload naar Meta: `mcp__claude_ai_Pipeboard_Meta_Ads__upload_ad_image`

**Video's:**
- Download van Drive: `mcp__google__drive_file_download`
- Upload naar Meta: `mcp__claude_ai_Pipeboard_Meta_Ads__upload_ad_video`

Log elk upload-resultaat (hash/ID) voor gebruik in ad creatives.

### 8. Maak campagnes aan
Per campagne uit het plan, gebruik account `act_567892422940728`:

**8a — Campagne:**
`mcp__claude_ai_Pipeboard_Meta_Ads__create_campaign`
- `status`: "PAUSED"
- `objective`: uit briefing.md

**8b — Ad Set:**
`mcp__claude_ai_Pipeboard_Meta_Ads__create_adset`
- `status`: "PAUSED"
- `daily_budget`: in centen
- `targeting`: opgebouwd in stap 5

**8c — Ad Creative:**
`mcp__claude_ai_Pipeboard_Meta_Ads__create_ad_creative`
- Met de geüploade asset (image hash of video ID)
- `body`: uit briefing.md
- `title`: hook uit briefing.md
- `call_to_action`: uit briefing.md
- `link`: uit briefing.md

**8d — Ad:**
`mcp__claude_ai_Pipeboard_Meta_Ads__create_ad`
- `status`: "PAUSED"
- `creative`: ID uit stap 8c

### 9. Toon het resultaat

```
## Batch Upload Compleet — [datum]

### Campagne 1: [naam]
- ✅ Campagne: [naam] (ID: [id])
- ✅ Ad Set: [naam] (ID: [id]) — €X/dag
- ✅ Assets geüpload: X afbeeldingen, X video's
- ✅ Ads aangemaakt:
  - [naam] (ID: [id]) — "[hook preview]"
  - [naam] (ID: [id]) — "[hook preview]"

### Campagne 2: [naam]
[zelfde structuur]

### Totaal aangemaakt
- Campagnes: X
- Ad Sets: X
- Ads: X
- Assets geüpload: X

### Status: ALLES OP PAUSED
Wil je dat ik een of meer campagnes activeer? Geef aan welke:
1. [campagne naam 1]
2. [campagne naam 2]
Of: "activeer alles"
```

### 10. Activeer (alleen na goedkeuring)
Na Robin's bevestiging (specifieke campagnes of "alles"):

Per goedgekeurde campagne:
- `mcp__claude_ai_Pipeboard_Meta_Ads__update_campaign` → status "ACTIVE"
- `mcp__claude_ai_Pipeboard_Meta_Ads__update_adset` per ad set → status "ACTIVE"

Bevestig per campagne:
> "✅ [campagne naam] is nu ACTIVE — €X/dag budget"

## Regels
- Schrijf in het Nederlands
- Naming convention is VERPLICHT
- Bedragen in EUR met twee decimalen
- Verwerk submappen alfabetisch
- Als een asset upload faalt: sla die ad over, meld de fout, ga door met de rest
- Als een campagne-aanmaak faalt: stop die campagne, meld de fout, ga door met de volgende
- Nooit concurrenten bij naam noemen in ad copy
- Gebruik de Sempertex tone of voice
- Refereer aan het Sempertex Ad Account (act_567892422940728) tenzij Robin anders aangeeft
- Bij meer dan 50 ads: toon het plan in batches van 20 en vraag tussentijds bevestiging
- Log alle aangemaakte ID's en asset hashes voor traceerbaarheid
