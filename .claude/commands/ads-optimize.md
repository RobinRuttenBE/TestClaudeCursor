# /ads-optimize — Meta Ads Optimalisatie Analyse

Analyseer alle actieve Meta Ads campagnes en geef concrete optimalisatie-aanbevelingen op basis van performance data en de Hormozi 70-20-10 regel.

## Stappen

### 1. Haal campagne data op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_campaigns` voor account `act_567892422940728` (Sempertex Ad Account) met `status_filter: "ACTIVE"`. Check ook `act_607231713057715`.

### 2. Haal gedetailleerde insights op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` per campagne met:
- date_preset: "last_7d" en "last_30d" (voor trendvergelijking)
- Breakdowns waar mogelijk: `age`, `gender`, `placement`
- Metrics: `spend`, `impressions`, `clicks`, `ctr`, `cpc`, `cpm`, `frequency`, `reach`, `conversions`, `purchase_roas`, `cost_per_action_type`

### 3. Haal ad set data op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_adsets` per campagne om audience targeting en budget verdeling te analyseren.

### 4. Haal ad-level data op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_ads` en `mcp__claude_ai_Pipeboard_Meta_Ads__get_ad_creatives` per ad set om individuele creative performance te beoordelen.

### 5. Analyseer op drie assen

#### A. Creative Fatigue detectie
- **Frequency > 3,5** + **CTR dalend** (vergelijk last_7d vs last_30d) = creative fatigue
- **Frequency > 5** = zware fatigue, ongeacht CTR trend
- Vergelijk CTR trends: als CTR last_7d < 80% van CTR last_30d → dalende trend

#### B. Underperforming audiences
- Vergelijk ad sets op CPC, CTR en conversie-kosten
- Identificeer ad sets die >30% slechter presteren dan het gemiddelde
- Check of bepaalde demographics of placements disproportioneel budget verbruiken zonder resultaten

#### C. Budget verdeling
- Bereken spend per ad set als percentage van totaal
- Vergelijk dit met performance (conversies, ROAS) per ad set
- Identificeer mismatches: hoog budget + lage performance = budget verkeerd verdeeld
- Identificeer kansen: laag budget + hoge performance = schaalbaar

### 6. Pas de 70-20-10 regel toe
Lees `Bronnen/Alex Hormozi/100m-hooks-playbook.md` voor context.

- **70% Core**: Welke ads/hooks presteren bewezen goed? Aanbevelen om deze te schalen.
- **20% Emerging**: Welke ads tonen potentieel maar zijn nog niet bewezen? Aanbevelen om variaties te testen.
- **10% Experimental**: Zijn er genoeg nieuwe hooks/formats in de mix? Suggereer experimenten.

Categoriseer elke actieve ad in een van deze drie buckets op basis van performance data.

## Output format

```
## Meta Ads Optimalisatie — [datum]

### Creative Fatigue Alert

| Ad naam | Frequency | CTR (7d) | CTR (30d) | Trend | Actie |
|---------|-----------|----------|-----------|-------|-------|
| [naam]  | X.X       | X%       | X%        | ↓     | Pauzeer / Vervang creative |

### Underperforming Audiences

| Ad Set | Audience | CPC | CTR | Conv. | vs. Gemiddeld | Actie |
|--------|----------|-----|-----|-------|---------------|-------|
| [naam] | [targeting] | €X | X% | X | -X% | Pauzeer / Herdefinieer |

### Budget Verdeling

| Ad Set | Budget (%) | Spend | Conversies | CPA | Efficiëntie | Actie |
|--------|-----------|-------|------------|-----|-------------|-------|
| [naam] | X%        | €X    | X          | €X  | Hoog/Laag   | Schaal op / Reduceer |

### 70-20-10 Classificatie

**70% Core (schaal deze):**
- [ad naam] — CTR X%, CPC €X — bewezen performer

**20% Emerging (test variaties):**
- [ad naam] — toont potentieel, suggestie: [variatie]

**10% Experimental (nieuwe tests nodig):**
- Suggestie: test [nieuw hook type / format / audience]
- Gebaseerd op: [referentie uit hooks playbook]

### Concrete Aanbevelingen (prioriteit)

1. **NU doen**: [actie] — verwachte impact: [X]
2. **Deze week**: [actie] — verwachte impact: [X]
3. **Volgende sprint**: [actie] — verwachte impact: [X]
```

## Regels
- Schrijf in het Nederlands
- Wees concreet: geen "overweeg om..." maar "pauzeer ad X en vervang met variatie van hook Y"
- Refereer aan specifieke hooks uit `Kennis/Voorgaande campagnes/campagne-historie.md` waar relevant
- Gebruik de SYBB campagne als referentiekader (19 hooks, 4 body types, 6 CTAs)
- Bij twijfel: aanbevelen om te testen, niet om te stoppen
- Budget aanbevelingen altijd in verhouding tot totale spend
