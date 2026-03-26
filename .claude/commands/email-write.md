# /email-write — Individuele Email Copy Generator

Schrijf een individuele email klaar om in Mailjet te plakken, in Sempertex Europe tone of voice.

## Input

De gebruiker beschrijft welke email ze willen, bijvoorbeeld:
- "welkom email na SYBB inschrijving"
- "abandoned cart reminder dag 3"
- "post-purchase bedankt email"
- "review vraag email dag 10"
- "re-engagement email 1"
- "nieuwsbrief maart — nieuwe kleuren launch"

## Stappen

### 1. Bepaal context
Lees de email-automation SKILL (`.claude/skills/email-automation/SKILL.md`) om te bepalen:
- In welke flow past deze email?
- Welk segment ontvangt dit?
- Wat is de timing?
- Wat is het doel?

### 2. Laad referentiemateriaal
- `Kennis/Brand/tone-of-voice.md` — schrijfstijl
- `Kennis/Klantprofielen/klantprofielen.md` — doelgroep
- `Bronnen/Alex Hormozi/100m-hooks-playbook.md` — hook types voor subject line

Optioneel (afhankelijk van de email):
- `Kennis/Products/producten-overzicht.md` — bij product-gerelateerde emails
- `Kennis/Voorgaande campagnes/campagne-historie.md` — bij SYBB emails
- `Bronnen/Alex Hormozi/100m-lead-nurture-playbook.md` — bij nurture emails

### 3. Schrijf de email

Lever het volgende op:

```
## [Email Titel]

**Flow:** [flow naam]
**Segment:** [segment]
**Timing:** [wanneer in de flow]
**Doel:** [wat deze email moet bereiken]

---

**Subject Line A:** [primary]
**Subject Line B:** [A/B variant]
**Preview Text:** [inbox preview tekst]

---

Hi {{first_name}},

[Volledige email body]

[CTA sectie]

[Signoff]

---

**CTA Button:** [button tekst]
**CTA Link:** [URL of placeholder]
```

### 4. Schrijfregels voor de body

**Opening (1-2 zinnen):**
- Start met een hook die relevant is voor de ontvanger
- Maak het persoonlijk — spreek ze aan, erken hun situatie
- Geen "We hope this email finds you well" of andere clichés

**Body (3-6 zinnen):**
- Lever de kernwaarde van deze email
- Wees specifiek: "This technique saves you 20 minutes per installation" > "This is useful"
- Gebruik bullet points voor lijsten of stappen
- Eén kernboodschap per email — niet alles tegelijk

**CTA (1-2 zinnen):**
- Duidelijke, specifieke uitnodiging
- Vertel wat ze krijgen als ze klikken
- Gebruik actietaal: "Explore", "Discover", "Get your copy", "Join us"
- Nooit "Click here" of "Buy now" als standalone CTA

**Signoff:**
- Warm en persoonlijk
- Consistent per flow (gebruik dezelfde signoff binnen een flow)
- Sofie ondertekent de mails: "Sofie — Sempertex Europe", "Sofie & the STX EU Team", "Sofie from Sempertex Europe"

## Subject Line Regels

- **Max 50 karakters** (ideaal 30-40 voor mobile)
- **Specifiek** — de lezer moet weten wat de email biedt
- **Nieuwsgierigheid** — geef genoeg om te willen openen, niet alles
- **Geen clickbait** — lever wat de subject line belooft
- **Geen ALL CAPS** of overmatige leestekens
- **Emoji's:** maximaal 1, en alleen als het past bij de content
- **Personalisatie:** gebruik {{first_name}} waar het natuurlijk voelt

**A/B strategie:**
- Variant A en B moeten een ander hook type gebruiken
- Test: vraag vs. statement, kort vs. lang, met/zonder emoji, met/zonder naam

## Output

Na het schrijven, toon de email en vraag:

> **Wil je aanpassingen? Of zal ik de volgende email in deze flow schrijven?**

## Regels

- Schrijf in het **Engels** (Europees publiek) tenzij anders aangegeven
- Sempertex tone of voice: professioneel maar warm, als een ervaren collega
- Nooit concurrenten noemen
- Geen "goedkoop" of "budget" — we zijn premium
- Elke email moet standalone waarde bieden
- Hormozi: geef WHAT en WHY gratis, bewaar HOW voor betaald
- Social proof: Sempertex is "the world's #1 balloon brand" — use ratings, testimonials, artist results
- Gebruik {{first_name}}, {{company_name}} en andere Mailjet merge tags waar relevant
- Preview text moet de subject line aanvullen, niet herhalen
- Max 200 woorden per email body (kort en krachtig)
