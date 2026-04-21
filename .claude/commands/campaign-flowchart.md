# Campaign Flowchart Generator

Genereer een Mermaid flowchart die een volledige STX EU marketingcampagne visualiseert.

## Input
De gebruiker beschrijft een campagne. Bijvoorbeeld: "SYBB workshop funnel", "Silk collectie lancering", "Nozzle Up 2027 ticket campagne".

Als er een argument is meegegeven, gebruik dat als campagne: $ARGUMENTS

## Voorbereiding

Lees voor je begint:
1. `Kennis/Voorgaande campagnes/campagne-historie.md` — referentie voor campagnestructuur
2. `.claude/skills/campaign-design/SKILL.md` — funnel structuur en campagne template

Indien relevant voor het onderwerp, lees ook:
- `Kennis/Products/producten-overzicht.md`
- `Kennis/Klantprofielen/klantprofielen.md`
- `Kennis/Balloon Knowledge/INDEX.md` — bij techniek-, product- of pricing-campagnes: kies het centrale Balloon Knowledge bestand dat de campagne-spil vormt (bv. `diamond-weave-technique.md` voor een Diamond Weave masterclass campagne, `pricing-balloons-strategy.md` voor pricing workshop, `latex-balloons-explained.md` voor Sempertex range awareness). Gebruik dit voor inhoudelijke onderbouwing van content touchpoints en lead magnet keuze.

## Flowchart structuur

De Mermaid flowchart moet de volgende lagen bevatten:

### Laag 1: Entry Points (bovenkant)
Waar komt de doelgroep binnen?
- Meta Ads (FB + IG)
- YouTube Ads / organisch
- TikTok organisch
- Instagram organisch
- Email lijst
- Warm outreach
- Event / workshop

### Laag 2: Funnel Stappen (4 fasen)
Gebruik subgraphs per fase:
- **AWARENESS** — eerste touchpoints, hooks, scroll-stoppers
- **CONSIDERATION** — verdieping, free value, lead magnets, retargeting
- **PURCHASE** — conversie, booking, checkout
- **SATISFACTION** — post-purchase, retention, upsell

### Laag 3: Content Touchpoints (binnen elke fase)
Per fase de specifieke content types:
- Ads (statisch + video)
- Organische posts
- Landing pages
- Email flows
- Retargeting loops

### Laag 4: Email Flows (rechter zijkant of onderaan)
Parallelle email sequences:
- Pre-event / pre-purchase flow
- Reminder flow
- Post-event / post-purchase flow
- Long-term nurture

### Laag 5: Retargeting Loops
Pijlen die teruglopen van consideration/purchase naar awareness:
- Website bezoekers retargeting
- Video viewers retargeting
- Email openers retargeting
- Abandoned cart/booking retargeting

## Mermaid Syntax Regels

- Gebruik `graph TD` (top-down) als standaard richting
- Gebruik `subgraph` voor funnel fasen
- Gebruik verschillende node vormen:
  - `[Rechthoek]` voor kanalen en content
  - `{Ruit}` voor beslissingsmomenten
  - `([Stadium])` voor entry/exit points
  - `((Cirkel))` voor KPI meetpunten
- Gebruik `-->` voor standaard flow
- Gebruik `-.->` voor retargeting/teruglopende flows
- Gebruik `==>` voor de hoofdroute (happy path)
- Voeg labels toe aan pijlen waar nodig: `-->|label|`
- Gebruik `style` of `classDef` voor kleuren:
  - Awareness: lichtpaars (#f1d9ff)
  - Consideration: paars (#6b3fb9) met witte tekst
  - Purchase: magenta (#cd0b5c) met witte tekst
  - Satisfaction: goud (#ffdb5a)
  - Retargeting: stippellijn

## Output Format

```markdown
## 🗺️ Campaign Flowchart: [Campagnenaam]

### Campagne samenvatting
- **Doel:** [...]
- **Doelgroep:** [...]
- **Kanalen:** [...]
- **Looptijd:** [...]

### Flowchart

```mermaid
[volledige mermaid code]
```

### Leeswijzer
- [Uitleg van de flow voor Robin — wat zijn de belangrijkste routes, waar zitten de beslismomenten, waar zijn de retargeting loops]

### KPI's per fase
| Fase | Metric | Target |
|------|--------|--------|
| Awareness | [metric] | [target] |
| Consideration | [metric] | [target] |
| Purchase | [metric] | [target] |
| Satisfaction | [metric] | [target] |
```

## Complexiteitsniveau

Gebruik de SYBB campagne als referentie voor het gewenste complexiteitsniveau:
- SYBB had: 19 hooks × 4 bodies × 6 CTAs, 5 landing pages, 3 email flows, retargeting
- De flowchart hoeft niet elke individuele ad te tonen, maar wel de structuur en routes
- Toon de KEUZEMOMENTEN (waar splits de funnel?) en de TERUGKOPPELING (retargeting loops)
- Houd het leesbaar — max 30-40 nodes per flowchart

## Regels
- Altijd Mermaid syntax (geen ASCII art of andere formats)
- Altijd top-down layout
- Altijd de 4 funnel fasen als subgraphs
- Altijd minstens 1 retargeting loop tonen
- Altijd email flows als parallelle stroom tonen
- Kleuren uit de STX EU brand guide gebruiken in de styling
- Nederlands voor labels en beschrijving, Engels voor de campagne-elementen waar passend
