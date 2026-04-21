# /ad-combinator — Ad Combinatie Generator

Genereer 10 nieuwe ad combinaties (hook + body + CTA) voor een opgegeven campagne-onderwerp. Gebaseerd op de bewezen SYBB structuur en Hormozi hook types.

## Input
De gebruiker geeft een campagne-onderwerp, bijvoorbeeld:
- "SYBB workshop"
- "Silk lancering"
- "Link-O-Loon campagne"
- "Nozzle Up 2027"
- "Black Friday actie"

Als er geen onderwerp is opgegeven, vraag ernaar: "Welk campagne-onderwerp wil je combinaties voor genereren?"

## Stappen

### 1. Lees de kennisbank
Lees de volgende bestanden:
- `Kennis/Voorgaande campagnes/campagne-historie.md` — bewezen hooks, bodies en CTAs
- `Bronnen/Alex Hormozi/100m-hooks-playbook.md` — 7 hook types en 70-20-10 regel
- `Kennis/Brand/tone-of-voice.md` — tone of voice richtlijnen
- `Kennis/Products/producten-overzicht.md` — productkennis (indien relevant voor het onderwerp)
- `Kennis/Klantprofielen/klantprofielen.md` — doelgroepkennis
- `Kennis/Balloon Knowledge/INDEX.md` — kies bij techniek-, product-, of pricing-campagnes het meest relevante bestand voor inhoudelijke hooks (specifieke vocab, demo-momenten, problem statements). Heavy hitters: `latex-balloons-explained.md`, `pricing-balloons-strategy.md`, `interview-sofie-ceo-stx-eu.md`, `sempertex-company-heritage-and-vision.md`. Hormozi-regel: WHAT en WHY in de hook, HOW achter de CTA.

### 2. Analyseer de bestaande ad database
Uit de campagne-historie, extraheer:

**Bewezen hooks (SYBB):**
1-19: de 19 video hooks uit de SYBB campagne

**Bewezen bodies (SYBB):**
1. Free Value focus
2. Pricing/Business focus
3. Expertise & POC focus
4. Education/Community focus

**Bewezen CTAs (SYBB):**
1-6: de 6 CTAs uit de SYBB campagne

### 3. Genereer 10 combinaties
Verdeel de 10 combinaties volgens de 70-20-10 regel:

**7 combinaties (70% Core):**
- Gebruik bewezen hook-structuren uit de SYBB campagne
- Pas ze aan voor het nieuwe onderwerp
- Varieer over minimaal 4 van de 7 Hormozi hook types

**2 combinaties (20% Emerging):**
- Modelleer succesvolle hooks uit aangrenzende niches (event planning, creative business, craft industry)
- Of maak variaties op de best presterende SYBB hooks met een twist

**1 combinatie (10% Experimental):**
- Compleet nieuw format of hook type
- Provocerend, onverwacht, of een nieuw visueel concept
- POV, timelapse, behind-the-scenes reveal, of ander experimenteel format

### 4. Varieer over de 7 Hormozi hook types
Zorg dat de 10 combinaties minimaal 5 van deze types bevatten:
- **Statements**: krachtige uitspraken (meest bewezen, ~48% van top hooks)
- **Commands**: directe instructies (~22%)
- **Questions**: ja-vragen of open vragen (~10%)
- **Labels**: woorden waarmee de doelgroep zich identificeert
- **Conditionals**: scenario's die naar een resultaat leiden
- **Stories**: anekdotes of ervaringsverhalen
- **Lists**: stappen of opsommingen

### 5. Wijs platform en format toe
Per combinatie:
- **Platform**: Facebook, Instagram, of beide
- **Format**: Video (kort/lang), Static image, Carousel
- Baseer op het type hook en body (stories → video, statements → static of video, lists → carousel)

## Output format

```
## Ad Combinator — [onderwerp] — [datum]

### Verdeling
- 70% Core: 7 combinaties (bewezen structuren)
- 20% Emerging: 2 combinaties (veelbelovende variaties)
- 10% Experimental: 1 combinatie (nieuw concept)

---

### Combinatie 1 — [Hook type] — 70% Core
**Hook**: "[volledige hook tekst]"
**Body focus**: [Free Value / Pricing / Expertise / Community / Anders]
**Body sketch**: [2-3 zinnen die de richting van de body aangeven]
**CTA**: "[volledige CTA tekst]"
**Platform**: FB / IG / Beide
**Format**: Video (30s) / Static / Carousel
**Setting suggestie**: [visuele setting beschrijving]

---

[... combinaties 2-10 ...]

---

### Samenvatting hook types gebruikt
- Statements: X combinaties
- Commands: X combinaties
- Questions: X combinaties
- Labels: X combinaties
- Conditionals: X combinaties
- Stories: X combinaties
- Lists: X combinaties

### Volgende stap
[Aanbeveling: welke combinaties eerst testen, hoe te splitten in ad sets]
```

## Regels
- Hooks in het **Engels** (Europees publiek), tenzij de gebruiker Nederlands aangeeft
- Test suggestie: een aantal hooks ook in het Nederlands testen voor Benelux markt
- Body sketches zijn richtinggevend, niet volledig uitgeschreven
- Nooit concurrenten bij naam noemen
- Gebruik de Sempertex tone of voice: professioneel maar warm, "from balloon artists, for balloon artists"
- Refereer aan concrete producten/features waar relevant (Silk, Link-O-Loon, etc.)
- CTAs moeten duidelijk en actiegericht zijn
- Combinaties moeten onderling divers zijn — niet 10 variaties van dezelfde hook
