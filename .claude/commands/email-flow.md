# /email-flow — Email Flow Generator

Genereer een volledige email flow met alle copy, timing en A/B test varianten voor Sempertex Europe.

## Input

De gebruiker geeft een flow naam, bijvoorbeeld:
- "SYBB pre-workshop"
- "SYBB lead nurture"
- "SYBB post-workshop"
- "abandoned cart"
- "post-purchase"
- "welcome"
- "re-engagement"
- "newsletter welcome"

## Stappen

### 1. Laad de email-automation SKILL
Lees `.claude/skills/email-automation/SKILL.md` om de flow definitie, segment, triggers en timing op te halen.

### 2. Laad referentiemateriaal
Lees de volgende bestanden voor context:
- `Kennis/Voorgaande campagnes/campagne-historie.md` — bestaande SYBB flows als basis
- `Bronnen/Alex Hormozi/100m-lead-nurture-playbook.md` — nurture structuur
- `Bronnen/Alex Hormozi/100m-hooks-playbook.md` — hook types voor subject lines
- `Kennis/Brand/tone-of-voice.md` — schrijfstijl
- `Kennis/Klantprofielen/klantprofielen.md` — doelgroep context
- `Kennis/Products/producten-overzicht.md` — productkennis

### 3. Check of de flow al uitgeschreven is
Zoek in `Content/Email Flows/` of er al een uitgeschreven versie bestaat van deze flow. Als die bestaat, lees die en bied aan om te updaten in plaats van opnieuw te schrijven.

### 4. Genereer de volledige flow

Per email in de flow, schrijf:

#### Flow Header
```
## [Flow Naam]
**Segment:** [segment naam]
**Trigger:** [wat de flow start]
**Totaal emails:** [aantal]
**Tijdlijn:** [dag 1 t/m dag X]
**Doel:** [primaire KPI]
```

#### Per Email
```
---

### Email [nummer]: [titel]
**Timing:** [dag X / X uur na trigger]
**Doel:** [wat deze email moet bereiken]

**Subject Line A:** [subject line]
**Subject Line B:** [A/B variant]
**Preview Text:** [eerste regel die in inbox preview verschijnt]

---

[Volledige email body — klaar om in Mailjet te plakken]

---

**CTA Button:** [button tekst]
**CTA Link:** [URL of placeholder]
```

### 5. Schrijf de volledige email copy

Per email, schrijf de complete body tekst:
- **Opening:** Hook die aansluit op het doel van de email
- **Body:** Waarde, inzicht, of social proof — afhankelijk van positie in de flow
- **CTA:** Duidelijk, specifiek, uitnodigend — nooit pushy
- **Signoff:** Sofie ondertekent de mails. Varieer: "Sofie — Sempertex Europe", "Sofie & the STX EU Team", "Sofie from Sempertex Europe". Consistent binnen een flow.

Volg de Hormozi waarde-eerst structuur:
- Emails 1–3: Geef waarde (educatie, tips, social proof)
- Emails 4–5: Bouw vertrouwen (case studies, resultaten)
- Emails 6+: Zachte CTA (uitnodiging, niet druk)

### 6. Subject Line A/B Varianten

Genereer 2 subject lines per email, gebaseerd op verschillende hook types:
- Variant A: Primaire hook (statement of vraag)
- Variant B: Alternatieve hook (ander type — label, conditioneel, lijst, etc.)

Gebruik de 7 hook types uit het Hormozi hooks playbook:
1. Labels — "Balloon artists, ..."
2. Vragen — "Did you know...?"
3. Conditionelen — "If you're starting out..."
4. Commando's — "Don't miss this"
5. Statements — "The #1 mistake new decorators make"
6. Lijsten — "3 things every starter needs"
7. Verhalen — "When I started my balloon business..."

## Output Format

Toon de volledige flow in markdown format, klaar om:
1. Te kopiëren naar Mailjet
2. Op te slaan als referentie in `Content/Email Flows/`

Na het genereren, vraag:

> **Wil je deze flow opslaan naar `Content/Email Flows/[flow-naam].md`?**

Als ja, sla het bestand op.

## Regels

- Schrijf alle email copy in het **Engels** (Europees publiek) tenzij de gebruiker anders aangeeft
- Gebruik Sempertex tone of voice: professioneel maar warm, als een ervaren collega
- Elke email moet standalone waarde bieden — ook zonder click
- Nooit concurrenten noemen
- Subject lines: max 50 karakters, specifiek, nieuwsgierigheid opwekkend
- Preview text: max 90 karakters, complementeert de subject line
- CTA buttons: max 4 woorden, actiegericht
- Geen overdreven urgentie die niet echt is
- Geen "goedkoop" of "budget" taal — we zijn premium
- Social proof: gebruik echte referenties waar mogelijk (Sempertex reviews, artiest verhalen)
- Hormozi-regel: geef WHAT en WHY gratis, bewaar HOW voor betaald
- 70-20-10: 70% bewezen hooks, 20% variaties, 10% experimenten
