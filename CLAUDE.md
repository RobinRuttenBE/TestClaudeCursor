# CLAUDE.md — Sempertex Europe Marketing Automation

## Wie zijn wij
Sempertex Europe (STX EU) is de officiële Europese distributeur van Sempertex latex ballonnen. B2B only. #1 merk voor professionele ballonartiest en decorateurs. "From balloon artists, for balloon artists."

## Wie is Robin
Head of Marketing. Bouwt dit volledige marketing automation systeem. Niet-technisch. Spreekt Nederlands intern, Engels met Claude.

## Taal
- Interne communicatie & content: Nederlands (tenzij anders aangegeven)
- Klantcommunicatie: Engels (Europees publiek)
- Nooit concurrenten bij naam noemen in publieke content

---

## Kennisbank (lees per taak wat relevant is)

### Kennis/Brand/
Merkidentiteit, kleurcodes, fonts, tone of voice. **Lees altijd bij elke content- of designtaak.**
- `merkidentiteit.md` — wie we zijn, 7 brand pillars, positionering
- `kleurcodes.md` — primary/secondary/neutral/tertiary HEX codes
- `fonts.md` — Rethink Sans (titels/CTA) + Lato (body). Nooit andere fonts.
- `tone-of-voice.md` — professioneel maar warm, per-kanaal richtlijnen, 7 content pillars

### Kennis/Products/
- `producten-overzicht.md` — 9 latex lijnen, folie, specialty (Link-O-Loon!), accessoires, finish hiërarchie

### Kennis/Klantprofielen/
- `klantprofielen.md` — wholesalers (~60%) vs. professionals (~40%), 3 sub-segmenten, demografie

### Kennis/Voorgaande campagnes/
- `campagne-historie.md` — Nozzle Up, Black Friday, SYBB (volledig met 19 hooks/ads/funnels), podcast strategie, geplande campagnes 2025

### Kennis/Email Marketing/
Email strategie, Hormozi-frameworks voor email, en segment-specifieke waarde. **Lees bij elke email-taak.**
- `email-marketing-hormozi.md` — Hormozi email strategie: 10 tactieken, Reward Framework, cadence, opt-in, funnel follow-ups
- `email-marketing-waarde.md` — waarde per segment: 7 segmenten met problemen, oplossingen, CTA-richtingen
- `mozi-minute-email-structures.md` — Hormozi Mozi Minute emails als STRUCTURELE referentie: 3 templates (Problem→Script→Story, Belief-Bust→Reframe→Framework, Hidden Insight→Research→Data), tone translation guide. **Gebruik de structuur, niet de toon.**

### Kennis/Concurrentie/
- `concurrenten.md` — Kalisan, Gemar, Tuftex. Sterkte/zwakte. **Nooit publiek benoemen.**

---

## Bronnen (frameworks & referentiemateriaal)

### Bronnen/Alex Hormozi/
Marketing frameworks van Alex Hormozi. **Lees bij content-, ads- en strategietaken.**
- `100m-branding-playbook.md` — branding = associatie, bouquet metafoor, 4-stappen proces
- `100m-hooks-playbook.md` — 7 hook types, 70-20-10 regel, hook testing, checklist
- `100m-lead-nurture-playbook.md` — lead nurture frameworks en strategieën
- `100m-lifetime-value-playbook.md` — lifetime value optimalisatie
- `100m-price-raise-playbook.md` — prijsverhogingsstrategieën
- `goated-ads-playbook-summary.md` — ad frameworks en best practices
- `marketing-machine-playbook-summary.md` — marketing machine systeem

### Bronnen/Sempertex Europe/
- `sybb-8-pillars.md` — 8 kernproblemen van startende ballonartiesten + oplossingsrichtingen per pilaar. **Lees ALTIJD bij starter-gerichte content.** Zie Starter Audience Content regels hieronder.

### Bronnen/Balloon industry/
- `sempertex-industrie-kennis.md` — industrie kennis, trends, marktdata

---

## Content (scripts, transcripts, referenties)

### Content/Scripts/
- `filming-plan-referentie-denise-maart2025.md` — template voor filming sessies, 9 content types, hook/CTA patronen

### Content/Scripts/Balloon Content/
Ballontechnieken & productkennis. **Raadpleeg bij elke content-taak die technieken, producttoepassingen of tutorials raakt.**
- Alle bestanden bevatten: techniek uitleg, business applications, content angles, en key vocabulary
- Bruikbaar voor: email content, video scripts, social media posts, blog content, workshop materiaal, klantcommunicatie
- Merknaam is altijd Sempertex — geen andere merken noemen
- Zie `Content/Scripts/Balloon Content/INDEX.md` voor volledige index per bestand met techniek, moeilijkheid, categorie en segmenten

### Content/Transcripts/
- `no1-video-leverage-focus-better.md` — werk = output, leverage > uren, focus, better is boring
- `no2-video-blueprint-millionaire.md` — equity, niet diversifiëren, 5 fases, compounding, goodwill
- `no3-video-brutal-business-truths.md` — premium eerst, prioriteiten, talent, 100 golden BBs, brand, deep work
- `social-media-strategy-spcl.md` — SPCL framework (Status, Power, Credibility, Likeness), views vs invloed

---

## Tools & Integraties

### Morning Report (`/morning-report`)
- Command: `.claude/commands/MORNING_REPORT_COMMAND_v2 (1).md`
- Script: `scripts/morning-report.sh` (draait via launchd om 08:00, email delivery via `scripts/send-gmail.py`)
- **Secties:** Meta Ads SYBB performance, PostHog Landing Page health, cross-reference analyse, top acties
- **Data bronnen:** Meta Ads MCP (Pipeboard) en PostHog MCP. GEEN Google Calendar, Gmail, Drive of Sheets als databron.
- **PostHog metrics:** pageviews, bounce rate, scroll depth (25/50/75/100%), sessie duur, CTA clicks, session recordings
- **Cross-referencing:** combineert Meta Ads + PostHog data om ad-pagina mismatches te detecteren
- **Output:** rapport in console + opslaan in `output/reports/daily/YYYY-MM-DD_sybb_report.md`

### Fireflies.ai (meeting transcripts)
- Documentatie: `Kennis/tools/fireflies-integratie.md`
- Script: `scripts/fireflies_fetch.py`
- Slash command: `/fetch-meetings`
- Transcripts: `Kennis/content/transcripts/`
- Meeting summaries: `Kennis/content/meeting-summaries/`

### SYBB Daily Report Skill
- Locatie: `skills/daily-sybb-report/SKILL.md`
- Trigger: automatisch bij laptop wake (daily report flow) of handmatig via "SYBB rapport", "hoe doet SYBB het?", "landing page performance"
- **Data bronnen:**
  - Meta Ads MCP (Pipeboard): campagne `2026: SYBB`
  - PostHog MCP: project "Default project", site startyourballoonbusiness.com
- **UTM conventie:** lowercase, format `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X`
- **KPI Targets:**

| KPI | Target 30d | Target 90d |
|-----|-----------|-----------|
| LP Bounce Rate | <55% | <40% |
| LP Conversie Rate | >5% | >8% |
| Avg Scroll Depth | >60% | >75% |
| CTA Click Rate | >4% | >6% |
| Meta CPC | <€0.50 | <€0.40 |
| Time on Page | meten | >90s |

- **Output:**
  - Dagelijks: `output/reports/daily/YYYY-MM-DD_sybb_report.md`
  - Wekelijks: `output/reports/weekly/YYYY-WXX_sybb_summary.md`

### Meta Ads Tracker Excel Formatting Skill
- Locatie: `skills/meta-ads-tracker-excel/SKILL.md`
- Trigger: bij genereren/updaten van `Meta_Ads_Tracker_Sempertex.xlsx` of schrijven naar Google Sheet tracker
- **Bestanden:**
  - Excel: `Meta_Ads_Tracker_Sempertex.xlsx`
  - Google Sheet: `1kMtMXBYxFYStVxop_yjkWaB5mfh7Y2tgmpYcjf2ytHs`
- **5 sheets:** Dashboard, Weekly Report, Ad Master List, Campaign Overview, UTM & Pixel Reference
- **Formatting:** Arial 10, zebra striping, conditional formatting (CPC >€0.50, CTR <1%, ROAS <1x), currency €#,##0.00
- **PostHog kolommen (Y-AC):** Bounce Rate, Scroll Depth, Session Duration, CTA Click Rate, /booking Visits. Match via `utm_content`.
- **Implementatie:** altijd openpyxl, nooit pandas voor formatting. Run `scripts/recalc.py` na save.

---

## Assets
- `assets/templates/` — *Nog te vullen — Remotion templates, Canva template specs*
- `assets/notities/` — *Nog te vullen — losse notities en ideeën*

---

## .claude/ (commands, skills, rules)
Wordt opgebouwd in Fase 2-5 van het implementatieplan.
- `.claude/commands/` — slash commands als .md bestanden
- `.claude/skills/` — SKILL.md per vaardigheid
- `.claude/rules/` — gedragsregels

---

## Kernprincipes
1. **Hormozi-regel:** Geef WHAT en WHY gratis, bewaar HOW voor betaald
2. **Hook first:** 80% van je advertentiebudget zit in de eerste zin
3. **70-20-10:** 70% bewezen hooks, 20% variaties, 10% experimenten
4. **Focus:** Eén campagne tegelijk perfect maken, niet 5 half
5. **Better is leverage:** Saai werk (split tests, CRM, follow-up) levert het meeste geld op
6. **Brand = goodwill:** Compound effect van educatie, community, gratis waarde
7. **Nooit concurrenten noemen in publieke content**

---

## Starter Audience Content
Bij het schrijven van content, emails, of ad copy gericht op startende ballonartiesten:
1. Lees `Bronnen/Sempertex Europe/sybb-8-pillars.md` eerst
2. Identificeer welke pilaar/pilaren de content adresseert
3. Gebruik de PROBLEMS sectie voor hooks en audience identificatie
4. Gebruik de SOLUTIONS sectie voor waarde — maar alleen het "what," nooit het volledige "how"
5. Het "how" is gereserveerd voor de SYBB workshop — eindig altijd met een SYBB CTA
6. Gebruik de content hooks per pilaar als startpunt
7. Cross-refereer `Content/Scripts/Balloon Content/pricing-balloons-strategy.md` wanneer Pillar 7 (Pricing) relevant is
8. CTA-structuur: erken waarde → creëer gap → positioneer workshop → directe actie → future-pace
