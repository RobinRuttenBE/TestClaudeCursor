# /ads-auto-optimize — Automatische Meta Ads Optimalisatie

Analyseer de performance van alle actieve Meta Ads campagnes over de afgelopen 3 dagen en voer automatische optimalisaties uit. Ontworpen om dagelijks na /ads-report te draaien (handmatig of via scheduled task).

## Twee actie-niveaus

### Niveau 1: Automatische acties (GEEN bevestiging nodig)
Deze acties worden direct uitgevoerd omdat ze duidelijke underperformers stoppen:

- **Pauzeer ads met CTR < 0.5%** na minimaal 1.000 impressions
- **Pauzeer ads met CPC > €1.00** na minimaal 500 clicks

### Niveau 2: Voorstellen (WEL bevestiging nodig)
Deze acties worden ALLEEN voorgesteld — Robin moet goedkeuren:

- Budget verhogen op top performers
- Nieuwe ad variaties maken gebaseerd op winnende hooks
- Audiences aanpassen of uitsluiten
- Budget herverdelen tussen ad sets

**NOOIT** niveau 2 acties uitvoeren zonder expliciete goedkeuring van Robin.

## Stappen

### 1. Haal performance data op (3 dagen)
Gebruik het Sempertex Ad Account `act_567892422940728`. Check ook `act_607231713057715`.

**Per account:**
- `mcp__claude_ai_Pipeboard_Meta_Ads__get_campaigns` met `status_filter: "ACTIVE"`
- `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` per campagne met `date_preset: "last_3d"`
  - Metrics: `spend`, `impressions`, `clicks`, `ctr`, `cpc`, `cpm`, `frequency`, `reach`, `conversions`, `purchase_roas`, `cost_per_action_type`
- `mcp__claude_ai_Pipeboard_Meta_Ads__get_adsets` per campagne
- `mcp__claude_ai_Pipeboard_Meta_Ads__get_ads` per ad set
- `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` op ad-niveau met `date_preset: "last_3d"`

### 2. Analyseer elke ad tegen de drempelwaarden

**Kill-regels (automatisch pauzeren):**

| Regel | Drempel | Minimum data | Actie |
|-------|---------|-------------|-------|
| Lage CTR | CTR < 0.5% | ≥ 1.000 impressions | Pauzeer ad |
| Hoge CPC | CPC > €1.00 | ≥ 500 clicks | Pauzeer ad |

**Waarschuwingsregels (alleen rapporteren):**

| Regel | Drempel | Signaal |
|-------|---------|---------|
| Creative fatigue | Frequency > 3.5 | Creative vervangen |
| Dure reach | CPM > €15 | Audience te smal of saturated |
| Dalende CTR | CTR last_3d < 70% van lifetime CTR | Vermoeidheid begint |

### 3. Voer automatische acties uit (Niveau 1)

Voor elke ad die een kill-regel triggert:

1. Log de huidige performance (voor het rapport)
2. Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__update_ad` om status naar "PAUSED" te zetten
3. Registreer de actie in het rapport

### 4. Classificeer ads volgens 70-20-10

Lees `Bronnen/Alex Hormozi/100m-hooks-playbook.md` voor context.

Classificeer alle ACTIEVE ads (na pauzeren van underperformers):

**70% Core — Bewezen winners:**
- Ads met CTR > 1.5% EN CPC < €0.50
- Of ads met ROAS > 2x
- Deze moeten het meeste budget krijgen

**20% Emerging — Potentieel:**
- Ads met CTR 0.8-1.5% of CPC €0.50-€0.80
- Nog niet genoeg data voor definitief oordeel
- Verdienen meer tijd/budget om zich te bewijzen

**10% Experimental — Tests:**
- Nieuw gelanceerde ads (< 500 impressions)
- Ads met ongebruikelijke hooks of formats
- Bewust klein budget om te leren

### 5. Bereken optimale budget verdeling

Op basis van de 70-20-10 classificatie:
- Bereken het huidige budget per categorie (% van totaal)
- Bereken het ideale budget per categorie
- Identificeer mismatches

### 6. Genereer voorstellen (Niveau 2)

**Budget voorstellen:**
- Als een Core ad < 70% van budget krijgt → stel budgetverhoging voor
- Als een Experimental ad > 15% van budget krijgt → stel verlaging voor
- Geef concrete bedragen (van €X naar €X)

**Variatie voorstellen:**
- Identificeer de top 3 hooks (hoogste CTR)
- Stel 2-3 variaties voor per winnende hook (ander format, andere CTA, andere body)
- Gebruik de 7 Hormozi hook types als inspiratie

**Audience voorstellen:**
- Als bepaalde demographics of placements structureel slechter presteren → stel uitsluiting voor
- Als een audience saturated is (frequency > 4) → stel uitbreiding of vervanging voor

## Output format

```
## Auto-Optimize Rapport — [datum]

### ⚡ Automatische acties uitgevoerd

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| [naam] | CTR 0.3% (< 0.5%) | ACTIVE | PAUSED | 2.100 imp, 6 clicks |
| [naam] | CPC €1.23 (> €1.00) | ACTIVE | PAUSED | 520 clicks, €639 spend |

**Totaal gepauzeerd: [X] ads**
(of: "Geen ads gepauzeerd — alles presteert boven de drempelwaarden ✅")

### ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|----|---------|--------|-----------------|
| [naam] | Creative fatigue | Freq 4.2 | Creative vervangen |

### 📊 70-20-10 Classificatie

**70% Core (budget: €X/dag — huidig X% van totaal):**
- [ad naam] — CTR X%, CPC €X, ROAS Xx

**20% Emerging (budget: €X/dag — huidig X% van totaal):**
- [ad naam] — CTR X%, CPC €X — potentieel

**10% Experimental (budget: €X/dag — huidig X% van totaal):**
- [ad naam] — [X] impressions — te vroeg voor oordeel

**Budget mismatch:** [Ja/Nee — beschrijving als ja]

### 💡 Voorstellen (wacht op goedkeuring)

**1. Budget herverdeling**
- [ad/adset naam]: van €X/dag naar €X/dag (+X%)
- Reden: [waarom]
- Verwachte impact: [wat]

**2. Nieuwe variaties**
- Gebaseerd op winnende hook "[hook tekst]" (CTR X%):
  - Variatie A: "[nieuwe hook]" — [format]
  - Variatie B: "[nieuwe hook]" — [format]

**3. Audience aanpassingen**
- [voorstel met concrete targeting wijziging]
- Reden: [data die dit ondersteunt]

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
```

## Integratie met morning report

Wanneer dit command wordt aangeroepen vanuit het scheduled morning report script:
- Voer alleen Niveau 1 acties uit (automatisch pauzeren)
- Log alle Niveau 2 voorstellen in de email
- Robin kan de voorstellen later in een interactieve sessie goedkeuren

## Regels
- Schrijf in het Nederlands
- Bedragen in EUR met twee decimalen
- Percentages met één decimaal
- Wees concreet: geen "overweeg om..." maar "pauzeer ad X" of "verhoog budget van €X naar €X"
- Bij twijfel over data-kwaliteit (te weinig impressions, te korte periode): meld dit en sla de ad over
- Minimale data vereist: een ad moet minimaal 24 uur actief zijn geweest voordat kill-regels van toepassing zijn
- Nooit meer dan 50% van alle actieve ads in één keer pauzeren — als dit dreigt te gebeuren, stop en meld dit aan Robin
- Log elke automatische actie met timestamp en reden
- Refereer aan het Sempertex Ad Account (act_567892422940728) als primaire bron
- Volg de Hormozi 70-20-10 regel strikt bij budget aanbevelingen
