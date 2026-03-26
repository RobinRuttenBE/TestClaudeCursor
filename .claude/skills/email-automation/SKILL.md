---
name: Email Automation
description: Volledige email strategie van Sempertex Europe. Definieert alle triggers, segmenten, flows en timing. Wordt gebruikt door /email-flow en /email-write commands.
---

# Email Automation — Sempertex Europe

## Platform & Architectuur

- **Email platform:** Mailjet (versturen, templates, segmenten)
- **Connectie:** Zapier (Wix → Mailjet triggers)
- **Copy & strategie:** Claude Code (dit systeem)
- **Tracking:** UTM-tags op alle links (zie tracking-standards SKILL)

Claude Code schrijft alle email copy en strategie. Mailjet en Zapier handelen het versturen en de triggers af.

---

## Triggers & Segmenten

### 1. Free Value Download (SYBB Lead Magnet)

| Veld | Waarde |
|------|--------|
| **Trigger** | Opt-in via SYBB landing page (free value download) |
| **Segment** | `SYBB Lead` |
| **Flow** | SYBB Lead Nurture |
| **Emails** | 7 |
| **Timing** | Dag 1–7, daarna reguliere lijst |
| **Doel** | Conversie naar workshop inschrijving |

**Flow overzicht:**
1. Dag 1: Bevestiging + free value levering
2. Dag 2: Artiest spotlight (social proof)
3. Dag 3: Wat vond je ervan? + workshop CTA
4. Dag 4: Quick win — kwaliteit kiezen
5. Dag 5: Reviews & social proof
6. Dag 6: Industry insights (free value)
7. Dag 7: Event kalender — SYBB gericht

Na dag 7 → verplaats naar segment `Newsletter` voor reguliere educatieve mails.

---

### 2. Workshop Inschrijving (SYBB Registered)

| Veld | Waarde |
|------|--------|
| **Trigger** | Workshop ticket gekocht via Wix |
| **Segment** | `SYBB Registered` |
| **Flow** | SYBB Pre-Workshop |
| **Emails** | 9 |
| **Timing** | Dag 1–7 + reminder op D-3 en D-1 |
| **Doel** | Maximale show rate, excitement opbouwen, website traffic |

**Flow overzicht:**
1. Dag 1: Bevestigingsmail inschrijving
2. Dag 1 (+4u): Succesvolle artiest in de spotlight
3. Dag 2: Quick win — kwaliteit kiezen met Sempertex
4. Dag 3: Social proof — reviews van de wereld
5. Dag 4: Free value — industry insights
6. Dag 5: Event kalender — wat er nog meer komt
7. Dag 7: Website verkennen + starter producten
8. D-3: Workshop reminder + wat te verwachten + free value
9. D-1: Laatste reminder — we kijken ernaar uit!

**Belangrijk:** Zodra iemand zich inschrijft voor de workshop, stopt de SYBB Lead Nurture flow. Ze krijgen ALLEEN de Pre-Workshop flow, geen dubbele content.

Na workshop → segment verplaatst naar `SYBB Alumni`.

---

### 3. Workshop Voltooid (SYBB Alumni)

| Veld | Waarde |
|------|--------|
| **Trigger** | Workshop datum verstreken (handmatig of via Zapier) |
| **Segment** | `SYBB Alumni` |
| **Flow** | SYBB Post-Workshop |
| **Emails** | 5 |
| **Timing** | Dag 1, 2, 7, 14, 30 |
| **Doel** | Review, social sharing, upsell naar Pro workshop, reguliere lijst |

**Flow overzicht:**
1. Dag 1: Bedankt + SYBB boekje + starter ideas
2. Dag 2: Deel je ervaring op Instagram + educatie kanalen (IG & YT)
3. Dag 7: Feedback vraag + volgende stap met je business
4. Dag 14: Upsell — Pro workshop of advanced educatie
5. Dag 30: Welkom in de community + educatie resources

Na dag 30 → segment verplaatst naar `Customer` + `Newsletter` voor reguliere mails met educatie en business insights.

---

### 4. Product Gekocht (Customer)

| Veld | Waarde |
|------|--------|
| **Trigger** | Aankoop voltooid via Wix webshop |
| **Segment** | `Customer` |
| **Flow** | Post-Purchase |
| **Emails** | 5 |
| **Timing** | Dag 1, 5, 10, 20, 30 |
| **Doel** | Review, educatie, upsell, community building, herhaalaankoop |

**Flow overzicht:**
1. Dag 1: Bedankt + order tips
2. Dag 5: Tips & tricks voor gekochte producten
3. Dag 10: Review vraag
4. Dag 20: Cross-sell — gerelateerde producten + educatie
5. Dag 30: Community welkom + volgende stap

---

### 5. Winkelwagen Verlaten (Abandoned Cart)

| Veld | Waarde |
|------|--------|
| **Trigger** | Cart verlaten zonder checkout (Wix → Zapier) |
| **Segment** | `Abandoned Cart` |
| **Flow** | Cart Recovery |
| **Emails** | 3 |
| **Timing** | 1 uur, dag 3, dag 7 |
| **Doel** | Heractiveren en conversie |

**Flow overzicht:**
1. 1 uur: Gentle reminder — je hebt iets achtergelaten
2. Dag 3: Social proof + waarde benadrukken
3. Dag 7: Laatste herinnering + urgentie

**Belangrijk:** Stop de flow zodra de aankoop alsnog voltooid wordt.

---

### 6. Account Aangemaakt (New Account)

| Veld | Waarde |
|------|--------|
| **Trigger** | Nieuw account aangemaakt op Wix webshop |
| **Segment** | `New Account` |
| **Flow** | Welcome |
| **Emails** | 4 |
| **Timing** | Direct, dag 3, dag 7, dag 14 |
| **Doel** | Eerste aankoop stimuleren, merk leren kennen |

**Flow overzicht:**
1. Direct: Welkom bij Sempertex Europe + wie we zijn
2. Dag 3: Bestsellers + waar te beginnen
3. Dag 7: Educatie — gratis content + workshops
4. Dag 14: Community + social proof

Na dag 14 → verplaats naar `Newsletter`.

---

### 7. Nieuwsbrief Signup (Newsletter)

| Veld | Waarde |
|------|--------|
| **Trigger** | Newsletter opt-in via website footer of pop-up |
| **Segment** | `Newsletter` |
| **Flow** | Newsletter Welcome + reguliere cadans |
| **Emails** | 3 welkom + doorlopend |
| **Timing** | Direct, dag 3, dag 7, daarna 2x per maand |
| **Doel** | Waarde bieden, brand loyalty, traffic naar shop |

**Welcome flow:**
1. Direct: Welkom + wat ze kunnen verwachten
2. Dag 3: Beste content van afgelopen maand
3. Dag 7: Introductie community + events

**Reguliere cadans:** 2x per maand nieuwsbrief met educatie, inspiratie, product launches, events.

---

### 8. Inactief (Re-engagement)

| Veld | Waarde |
|------|--------|
| **Trigger** | Geen email opens of clicks in 90 dagen |
| **Segment** | `Inactive` |
| **Flow** | Re-engagement |
| **Emails** | 3 |
| **Timing** | Dag 1, dag 7, dag 14 |
| **Doel** | Heractiveren of opschonen |

**Flow overzicht:**
1. Dag 1: We missen je — update + beste content
2. Dag 7: Exclusieve waarde (tip, download, of preview)
3. Dag 14: Laatste kans — wil je nog van ons horen?

Na dag 14 zonder interactie → verwijder uit actieve lijst (list hygiene).

---

## Segment Hiërarchie & Conflictregels

Een contact kan in meerdere segmenten zitten, maar ontvangt nooit dubbele emails:

1. **Actieve flow > reguliere nieuwsbrief.** Als iemand in een actieve flow zit, ontvangt die geen nieuwsbrief tot de flow afgelopen is.
2. **Workshop inschrijving > lead nurture.** Zodra iemand zich inschrijft, stopt de SYBB Lead Nurture flow.
3. **Aankoop > abandoned cart.** Zodra een cart geconverteerd is, stopt de recovery flow.
4. **Re-engagement > alles.** Als iemand in re-engagement zit, stopt alle andere communicatie.

---

## Email Principes (Hormozi + STX EU)

### Waarde-eerst structuur
1. **Email 1–3:** Geef waarde. Educatie, tips, social proof. Geen harde verkoop.
2. **Email 4–5:** Bouw vertrouwen. Case studies, resultaten, community.
3. **Email 6+:** Zachte CTA. Uitnodiging, niet druk. Urgentie alleen als die echt is.

### Hormozi-regels voor email
- Geef WHAT en WHY gratis, bewaar HOW voor betaald (workshop/product)
- Hook first: de subject line is 80% van je email
- Social proof > claims: toon resultaten van echte artiesten
- Elke email moet standalone waarde bieden — zelfs als ze niet klikken
- Reciprociteit: geef eerst, vraag later

### Tone of Voice in email
- Persoonlijk, warm, niet spammy
- Schrijf alsof je een collega-artiest mailt, niet een klant
- Elke email moet waarde bieden — een tip, een inzicht, een inspiratie
- CTA's zijn uitnodigingen, geen bevelen
- Subject lines: specifiek, nieuwsgierigheid opwekkend, nooit clickbait
- Taal: Engels (Europees publiek), tenzij specifiek NL segment

### A/B Testing
- Elke email krijgt 2 subject line varianten
- Test op open rate (subject line) en click rate (content/CTA)
- Winnaar na 24u → verstuur naar rest
- Documenteer winnaars in de Google Sheet

---

## KPI's per Flow

| Flow | Primaire KPI | Target |
|------|-------------|--------|
| SYBB Lead Nurture | Workshop inschrijving | 15% conversie |
| SYBB Pre-Workshop | Show rate | 85% show rate |
| SYBB Post-Workshop | Review + social share | 30% response |
| Post-Purchase | Review + herhaalaankoop | 20% review, 25% repeat in 90 dagen |
| Abandoned Cart | Cart recovery | 10% recovery |
| Welcome | Eerste aankoop | 20% conversie in 30 dagen |
| Newsletter | Open rate + click rate | 35% open, 5% click |
| Re-engagement | Heractivatie | 15% heractivatie |

---

## Referentiebestanden

- `Kennis/Voorgaande campagnes/campagne-historie.md` — SYBB email flows, learnings
- `Bronnen/Alex Hormozi/100m-lead-nurture-playbook.md` — nurture frameworks
- `Bronnen/Alex Hormozi/100m-hooks-playbook.md` — hook types voor subject lines
- `Kennis/Brand/tone-of-voice.md` — schrijfstijl
- `Kennis/Klantprofielen/klantprofielen.md` — doelgroep segmenten
- `Kennis/Products/producten-overzicht.md` — productkennis voor content
