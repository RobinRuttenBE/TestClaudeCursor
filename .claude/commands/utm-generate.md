---
description: Genereer UTM-getagde URLs volgens Sempertex tracking standards
user_invocable: true
---

# /utm-generate — UTM URL Generator

Genereer volledige URLs met UTM parameters volgens de Sempertex Europe tracking standards.

## Stap 1: Input parsen

De gebruiker geeft minimaal:
- **Kanaal** (verplicht): meta-ads, email, instagram, facebook, youtube, linkedin, tiktok, google-ads
- **Campagne** (verplicht): campagnenaam of slug
- **Content** (verplicht): beschrijving van de ad/content

Optioneel:
- **URL** (de bestemmings-URL — default: https://startyourballoonbusiness.com)
- **Term** (audience/keyword)

Als onderdelen ontbreken, vraag ernaar.

## Stap 2: Lees de tracking standards

Lees ALTIJD `.claude/skills/tracking-standards/SKILL.md` voor de juiste UTM conventies per kanaal.

## Stap 3: Genereer de UTM URL

### Kanaal mapping

| Input | utm_source | utm_medium |
|-------|-----------|------------|
| meta-ads | meta | paid-social |
| google-ads | google | cpc |
| email | email | email |
| instagram | instagram | organic-social |
| facebook | facebook | organic-social |
| youtube | youtube | organic-video |
| linkedin | linkedin | organic-social |
| tiktok | tiktok | organic-social |

### Slug generatie regels
- Alles lowercase
- Spaties → streepjes
- Verwijder speciale tekens
- Kort maar beschrijvend
- Voorbeeld: "SYBB Workshop Hook Pricing Video" → `sybb-workshop-hook-pricing-video`

## Stap 4: Output

Toon de gegenereerde URL in dit format:

```
## UTM URL — [beschrijving]

**Volledige URL:**
[base-url]?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]&utm_term=[term]

**Parameters:**
| Parameter | Waarde |
|-----------|--------|
| utm_source | [source] |
| utm_medium | [medium] |
| utm_campaign | [campaign] |
| utm_content | [content] |
| utm_term | [term of "—"] |

**Kopieer-klare URL:**
`[volledige url]`
```

## Stap 5: Opslaan in Google Sheet

Zoek de Google Sheet "UTM & Tracking Reference" via `mcp__google__drive_files_search`.

- Als de sheet bestaat: voeg een nieuwe rij toe met `mcp__google__sheets_values_update`:
  `Datum | Kanaal | Campagne | Content | Volledige URL | Aangemaakt door`

- Als de sheet niet bestaat: maak hem aan via `mcp__google__drive_file_upload` of meld aan Robin dat deze nog aangemaakt moet worden. Stel voor om de sheet aan te maken met de header:
  `Datum | Kanaal | utm_source | utm_medium | utm_campaign | utm_content | utm_term | Volledige URL`

## Stap 6: Batch modus

Als de gebruiker meerdere UTMs tegelijk nodig heeft (bv. "genereer UTMs voor alle 5 SYBB ads"), genereer ze allemaal in één tabel en sla ze allemaal op.

```
## Batch UTM URLs — [campagne]

| # | Content | Volledige URL |
|---|---------|---------------|
| 1 | [content-1] | [url-1] |
| 2 | [content-2] | [url-2] |
| ... | ... | ... |

Alle [X] URLs opgeslagen in "UTM & Tracking Reference" sheet.
```

## Regels
- Volg STRIKT de naming conventions uit tracking-standards skill
- Alles lowercase, streepjes, geen spaties
- Valideer dat de base URL correct is (geen typos)
- Elke gegenereerde UTM wordt opgeslagen — geen uitzonderingen
- Als de gebruiker een URL geeft die al UTMs bevat: waarschuw en vervang met correcte UTMs

$ARGUMENTS
