---
description: Check of een pagina correct tracking heeft (GA4, UTMs, Meta Pixel)
user_invocable: true
---

# /tracking-check — Tracking Verificatie

Check of een URL correct tracking heeft: GA4 data, UTM parameters, en Meta Pixel events.

## Stap 1: Input

De gebruiker geeft een URL. Voorbeeld:
```
/tracking-check https://startyourballoonbusiness.com/workshops
```

Als geen URL gegeven: vraag ernaar.

## Stap 2: Lees tracking standards

Lees ALTIJD `.claude/skills/tracking-standards/SKILL.md` voor de vereiste tracking setup.

## Stap 3: Checks uitvoeren

### Check 1: GA4 Data — Ontvangt deze pagina data?

Gebruik `mcp__ga4__run_report` op property **528249861**:
```
dimensions: ["pagePath"]
metrics: ["screenPageViews", "sessions", "activeUsers"]
dimension_filter: filter op het pad uit de URL
date_ranges: last 7 days
```

- Als data gevonden: 🟢 GA4 ontvangt data van deze pagina
- Als geen data: 🔴 GA4 ontvangt GEEN data — tag ontbreekt of pagina heeft geen traffic

### Check 2: UTM Parameters — Worden UTMs correct opgepikt?

Gebruik `mcp__ga4__run_report`:
```
dimensions: ["sessionSource", "sessionMedium", "sessionCampaignName"]
metrics: ["sessions"]
dimension_filter: filter op pagePath
date_ranges: last 30 days
```

- Als UTM data gevonden (source/medium/campaign): 🟢 UTMs worden correct opgepikt
- Als alleen "(direct) / (none)": 🟠 Geen UTM data — links hebben waarschijnlijk geen UTMs
- Als geen data: 🔴 Geen sessions op deze pagina

### Check 3: Conversie Events — Vuren er events op deze pagina?

Gebruik `mcp__ga4__run_report`:
```
dimensions: ["eventName", "pagePath"]
metrics: ["eventCount"]
dimension_filter: filter op pagePath
date_ranges: last 30 days
```

Check of de volgende events aanwezig zijn:
- `page_view` — basis (moet er zijn)
- `scroll` — engagement
- `click` — outbound clicks
- `view_content` — product/workshop views
- `generate_lead` — formulier invullen
- `add_to_cart` — winkelwagen
- `begin_checkout` — checkout
- `purchase` — aankoop

### Check 4: Meta Pixel — Wordt het pad getrackt door de pixel?

Cross-reference met Meta Ads data:
- Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` op account niveau
- Controleer of er `landing_page_view` actions zijn voor dit domein
- Als de URL een bekende landing page is van een campagne: check of view_content, add_to_cart, purchase events via de pixel binnenkomen

### Check 5: Realtime verificatie

Als de pagina net is opgezet of gewijzigd, draai een realtime check:
```
mcp__ga4__run_realtime_report
dimensions: ["pagePath"]
metrics: ["activeUsers"]
```
Vraag de gebruiker om de pagina te bezoeken en check dan of ze verschijnen.

## Stap 4: Output

```
## Tracking Check — [URL]

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 1 | GA4 Tag | 🟢/🔴 | [X pageviews afgelopen 7 dagen / geen data] |
| 2 | UTM Tracking | 🟢/🟠/🔴 | [X sessions met UTM data / alleen direct traffic / geen data] |
| 3 | Conversie Events | 🟢/🟠/🔴 | [welke events vuren / welke missen] |
| 4 | Meta Pixel | 🟢/🟠/🔴 | [LP views getrackt / geen pixel data] |
| 5 | Realtime | 🟢/🔴 | [X actieve users / geen activiteit] |

### Ontbrekende tracking
- [Lijst van wat er mist en hoe het te fixen]

### Aanbevolen acties
1. [Actie 1]
2. [Actie 2]
3. [Actie 3]
```

## Regels
- GA4 property voor SYBB: **528249861**
- Meta Ads account: **act_567892422940728**
- Als GA4 net is gekoppeld (weinig data): vermeld dit en focus op realtime check
- Geef altijd concrete fix-instructies, niet alleen "dit mist"
- Bij UTM issues: genereer direct de correcte UTM met /utm-generate

$ARGUMENTS
