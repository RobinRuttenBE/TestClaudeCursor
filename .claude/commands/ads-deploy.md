# /ads-deploy — Meta Ads Campagne Deployer

Deploy een volledige Meta Ads campagne (campagne + ad sets + ads) vanuit een briefing en goedgekeurde ad combinaties. Alles wordt PAUSED aangemaakt — pas na expliciete goedkeuring van Robin wordt de campagne live gezet.

## Input
De gebruiker geeft een campagne briefing met:
- **Campagne naam/onderwerp** (bv. "SYBB workshop", "Silk lancering")
- **Dagbudget** (bv. "€50/dag") — max €100/dag tenzij expliciet anders aangegeven
- **Targeting** (bv. "vrouwen 25-40, interesse in ballonnen en event decoratie, EU")
- **Doel** (bv. conversies, traffic, awareness) — default: CONVERSIONS

Als onderdelen ontbreken, vraag ernaar voordat je begint.

## Veiligheidsregels (STRIKT)
- **NOOIT** een campagne automatisch op ACTIVE zetten zonder expliciete goedkeuring van Robin
- **NOOIT** meer dan €100/dag per campagne tenzij Robin een hoger bedrag specifiek noemt
- **ALTIJD** eerst een volledig overzicht tonen van wat er wordt aangemaakt, VOORDAT je het aanmaakt
- **ALTIJD** bevestiging vragen na het overzicht: "Zal ik dit aanmaken op PAUSED?"
- **ALTIJD** na het aanmaken vragen: "Alles staat klaar op PAUSED. Wil je dat ik de campagne activeer?"
- Bij twijfel: STOP en vraag Robin

## Naming convention
Alle namen volgen dit patroon:
```
[DATUM]_[CAMPAGNE]_[AUDIENCE]_[HOOK-TYPE]
```
Voorbeelden:
- Campagne: `2025-03-14_SYBB_EU-Women-25-40`
- Ad Set: `2025-03-14_SYBB_EU-Women-25-40_Interest-Balloons`
- Ad: `2025-03-14_SYBB_EU-Women-25-40_Statement-Hook1`

## Stappen

### 1. Lees de ad combinaties
Zoek goedgekeurde ad combinaties op twee plekken:

**Optie A — /ad-combinator output:**
Als de gebruiker verwijst naar eerder gegenereerde combinaties in deze sessie, gebruik die.

**Optie B — Google Drive:**
Zoek via `mcp__google__drive_files_search` naar een map of bestand met goedgekeurde ads:
- Zoekterm: `name contains '[campagne-naam]' and name contains 'ads'`
- Of vraag Robin naar de locatie

Als er geen combinaties beschikbaar zijn, bied aan om eerst `/ad-combinator` te draaien.

### 2. Lees de kennisbank en tracking standards
- `Kennis/Brand/tone-of-voice.md` — voor ad copy check
- `Kennis/Klantprofielen/klantprofielen.md` — voor targeting validatie
- `Kennis/Voorgaande campagnes/campagne-historie.md` — voor referentie
- `.claude/skills/tracking-standards/SKILL.md` — VERPLICHT voor UTM conventies en pixel requirements

### 3. Bouw het targeting profiel
Gebruik de Meta Ads MCP tools om targeting op te bouwen:
- `mcp__claude_ai_Pipeboard_Meta_Ads__search_interests` — zoek relevante interesses
- `mcp__claude_ai_Pipeboard_Meta_Ads__search_geo_locations` — zoek locaties
- `mcp__claude_ai_Pipeboard_Meta_Ads__search_demographics` — zoek demographics
- `mcp__claude_ai_Pipeboard_Meta_Ads__estimate_audience_size` — schat audience grootte

Valideer dat de audience niet te breed (>50M) of te smal (<100K) is.

### 4. Genereer UTMs voor elke ad

**VERPLICHT: Geen enkele ad mag live gaan zonder UTMs.**

Genereer voor elke ad een unieke URL met UTM parameters volgens de tracking-standards skill:

```
[landing-page-url]?utm_source=meta&utm_medium=paid-social&utm_campaign=[campagne-slug]&utm_content=[ad-naam-slug]&utm_term=[audience-slug]
```

**Regels:**
- utm_campaign = campagne slug (bv. `sybb-workshop`)
- utm_content = ad naam slug (bv. `statement-hook13-b3-cta5`)
- utm_term = audience/ad set slug (bv. `eu-women-25-40-interest-balloons`)
- Alles lowercase, streepjes, geen spaties
- Elke ad krijgt een UNIEKE utm_content waarde

Sla alle gegenereerde UTMs op in de Google Sheet "UTM & Tracking Reference" via `mcp__google__drive_files_search` en `mcp__google__sheets_values_update`.

### 5. Toon het deployment plan
Toon een compleet overzicht VOORDAT je iets aanmaakt:

```
## Deployment Plan — [campagne naam]

### Campagne
- Naam: [naam volgens naming convention]
- Doel: [CONVERSIONS / TRAFFIC / AWARENESS]
- Status: PAUSED
- Account: act_567892422940728 (Sempertex Ad Account)

### Ad Sets
| # | Naam | Budget/dag | Audience | Geschatte grootte |
|---|------|-----------|----------|-------------------|
| 1 | [naam] | €X | [targeting details] | X.XM |

### Ads (met UTMs)
| # | Ad Set | Naam | Hook type | Hook | CTA | UTM Content |
|---|--------|------|-----------|------|-----|-------------|
| 1 | [ad set naam] | [naam] | Statement | "[hook tekst]" | "[CTA]" | [utm_content slug] |
| 2 | ... | ... | ... | ... | ... | ... |

### UTM URLs
| Ad | Volledige URL |
|---|---------------|
| [ad naam] | [landing-page]?utm_source=meta&utm_medium=paid-social&utm_campaign=[slug]&utm_content=[slug] |

### Budget samenvatting
- Dagbudget totaal: €X
- Geschat weekbudget: €X
- Geschat maandbudget: €X
```

Vraag dan: **"Zal ik dit aanmaken op PAUSED?"**

### 6. Maak de campagne aan (na bevestiging)
Gebruik het Sempertex Ad Account `act_567892422940728`.

**Stap 6a — Campagne:**
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__create_campaign` met:
- `account_id`: "act_567892422940728"
- `name`: volgens naming convention
- `objective`: zoals opgegeven (default: OUTCOME_SALES)
- `status`: "PAUSED"
- `special_ad_categories`: [] (tenzij anders nodig)

**Stap 6b — Ad Sets:**
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__create_adset` per ad set met:
- `campaign_id`: ID uit stap 5a
- `name`: volgens naming convention
- `daily_budget`: in centen (€50 = 5000)
- `billing_event`: "IMPRESSIONS"
- `optimization_goal`: passend bij campagne doel
- `targeting`: opgebouwd in stap 3
- `status`: "PAUSED"

**Stap 6c — Ads (met UTM URLs):**
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__create_ad` per ad met:
- `adset_id`: ID uit stap 6b
- `name`: volgens naming convention
- `creative`: de ad creative (hook + body + CTA)
- `status`: "PAUSED"

Als er afbeeldingen/video's nodig zijn, gebruik:
- `mcp__claude_ai_Pipeboard_Meta_Ads__upload_ad_image` voor afbeeldingen
- `mcp__claude_ai_Pipeboard_Meta_Ads__upload_ad_video` voor video's
- Of vraag Robin om de assets te uploaden

De website URL in elke ad MOET de UTM-getagde URL uit stap 4 bevatten. Gebruik de volledige URL inclusief alle UTM parameters als de destination URL van de ad.

### 7. Toon het resultaat
Na het aanmaken, toon een overzicht:

```
## Deployment Compleet — [campagne naam]

### Aangemaakt
- ✅ Campagne: [naam] (ID: [id])
- ✅ Ad Sets: [aantal] aangemaakt
  - [naam] (ID: [id]) — €X/dag
- ✅ Ads: [aantal] aangemaakt
  - [naam] (ID: [id]) — "[hook preview]"

### Status: PAUSED
Alles staat klaar op PAUSED. Wil je dat ik de campagne activeer?
```

### 8. Activeer (alleen na expliciete goedkeuring)
Pas na Robin's bevestiging ("ja", "activeer", "live zetten", etc.):

Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__update_campaign` om status naar "ACTIVE" te zetten.
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__update_adset` per ad set om status naar "ACTIVE" te zetten.

Bevestig daarna:
```
### ✅ Campagne LIVE
- [campagne naam] is nu actief
- Budget: €X/dag
- Eerste resultaten verwacht binnen 24-48 uur
- Tip: draai morgen /ads-report om de eerste data te bekijken
```

## Regels
- Schrijf in het Nederlands
- Naming convention is VERPLICHT — geen afwijkingen
- UTMs zijn VERPLICHT — geen enkele ad mag live gaan zonder correcte UTM parameters
- Lees ALTIJD de tracking-standards skill voor UTM conventies
- Budget in EUR, altijd met twee decimalen
- Bij elke stap: valideer dat de data klopt voordat je doorgaat
- Als een API call faalt: stop, meld de fout, en probeer niet automatisch opnieuw
- Log alle aangemaakte ID's zodat Robin ze later kan terugvinden
- Nooit concurrenten bij naam noemen in ad copy
- Gebruik de Sempertex tone of voice in alle ad teksten
- Refereer aan het Sempertex Ad Account (act_567892422940728) tenzij Robin anders aangeeft
