# /ads-report — Meta Ads Performance Rapport

Genereer een volledig performance rapport van alle actieve Meta Ads campagnes voor Sempertex Europe. Schrijf de resultaten ook naar de Google Sheet "Meta Ads Tracker".

## Stappen

### 1. Haal ad accounts op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_ad_accounts` om alle beschikbare accounts op te halen. Gebruik het **Sempertex Ad Account** (`act_567892422940728`) als primaire bron. Check ook `act_607231713057715` (Robin Rutten) voor eventuele actieve campagnes.

### 2. Haal actieve campagnes op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_campaigns` per account met `status_filter: "ACTIVE"`. Als er geen actieve campagnes zijn, haal ook `PAUSED` op en vermeld dit.

### 3. Haal performance data op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` per campagne met de volgende metrics:
- `spend`
- `impressions`
- `clicks`
- `ctr`
- `cpc`
- `cpm`
- `conversions` (of `actions` als conversions niet beschikbaar is)
- `purchase_roas` (of `action_values` voor ROAS berekening)

Gebruik date_preset "last_30d" tenzij de gebruiker een andere periode opgeeft.

### 4. Haal ad-level data op
Gebruik `mcp__claude_ai_Pipeboard_Meta_Ads__get_ads` per campagne om individuele ad performance te zien. Haal ook `mcp__claude_ai_Pipeboard_Meta_Ads__get_insights` op ad-niveau op voor gedetailleerde metrics.

### 5. Markeer underperformers
Analyseer elke campagne en ad op deze drempelwaarden:
- **CPC boven €0,50** → markeer als te duur
- **CTR onder 1%** → markeer als lage engagement
- **Frequency boven 3,5** → markeer als creative fatigue risico
- **CPM boven €15** → markeer als dure reach

### 6. Schrijf naar Google Sheet
Zoek de Google Sheet "Meta Ads Tracker" via `mcp__google__drive_files_search` met query `name = 'Meta Ads Tracker'`.
- Als de sheet bestaat: update met `mcp__google__sheets_values_update`
- Als de sheet niet bestaat: maak aan met `mcp__google__docs_document_create` of meld dit aan Robin

Schrijf de data in het "Weekly Report" tabblad met kolommen:
`Datum | Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conversies | ROAS | Flag`

## Output format

```
## Meta Ads Rapport — [datum]

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| [naam]   | Active | €X    | X           | X      | X%  | €X  | €X  | X     | Xx   |

### Underperformers

- **[campagne/ad naam]** — CPC €X (drempel: €0,50) → Aanbeveling: [actie]
- **[campagne/ad naam]** — CTR X% (drempel: 1%) → Aanbeveling: [actie]

### Top performers

- **Beste CTR**: [naam] — X%
- **Laagste CPC**: [naam] — €X
- **Beste ROAS**: [naam] — Xx

### Samenvatting

- **Totaal spend**: €X (periode: last 30 days)
- **Beste performer**: [naam] — waarom
- **Slechtste performer**: [naam] — waarom
- **Aanbeveling**: [concrete actie op basis van data]

### Google Sheet
[Status: geschreven naar "Meta Ads Tracker" / sheet niet gevonden]
```

Na het tonen van het rapport, vraag:

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Als de gebruiker funnel data aanlevert:
1. Combineer de Meta Ads data (impressions, clicks, spend) met de gegeven landing page metrics
2. Draai automatisch een `/funnel-diagnose` analyse met alle beschikbare data
3. Voeg de volledige funnel diagnose toe aan de output (tabel, #1 bottleneck, 3 actiepunten, SYBB vergelijking)
4. Als de data naar een dagelijkse email gaat: neem de funnel diagnose mee als extra sectie onder "Funnel Analyse" in de email body

## Regels
- Schrijf in het Nederlands
- Bedragen in EUR met twee decimalen
- Percentages met één decimaal
- Sorteer campagnes op spend (hoogste eerst)
- Als er geen actieve campagnes zijn: vermeld dit en toon de meest recente gepauzeerde campagnes met hun laatste performance data
- Gebruik de Hormozi 70-20-10 regel bij aanbevelingen: focus op bewezen winnaars
