# Meta Ads Rapport — 18 juli 2026

> **Let op: er zijn momenteel GEEN actieve campagnes.** Alle campagnes in het Sempertex Ad Account (`act_567892422940728`) staan op PAUSED. Het tweede account uit het command (`act_607231713057715`, Robin Rutten) is niet toegankelijk met deze API-token. Het extra toegankelijke account (`act_1489853856181844`) heeft geen actieve campagnes.
>
> Onderstaande cijfers zijn de **laatst bekende lifetime-performance** van de vier meest recente gepauzeerde campagnes (elk over hun eigen looptijd, niet één gemeenschappelijke periode). Ze zijn dus niet 1-op-1 met elkaar te vergelijken.

## Overzicht per campagne (gepauzeerd, lifetime data)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purchase) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x ⚠️ |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

⚠️ **ROAS-caveat 2026: SYBB:** de gerapporteerde purchase-waarde (€44.247 op 6 aankopen = €7.374 per aankoop) wijst op een verkeerd geconfigureerde pixel-waarde, niet op echte omzet. Behandel de 17,8x als onbetrouwbaar. Ook de `complete_registration`-waarde (€86.100) is verdacht hoog. Aanbeveling: controleer de pixel-waardeconfiguratie voordat je op ROAS stuurt.

## Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel: €0,50) → Aanbeveling: test-kopie met te weinig data (slechts €124 spend, 195 clicks). Niet heropstarten in deze vorm; vouw leerpunten terug in de hoofdcampagne 2026: SYBB.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel: €15) → Aanbeveling: dure reach door kleine, smalle doelgroep. Bij heropstart doelgroep verbreden of bewezen creatives uit hoofdcampagne gebruiken.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (net op de drempel van 1%) → Aanbeveling: lage engagement ondanks zeer goedkope reach (CPM €1,64). Hook eerste zin herzien volgens 70-20-10 voordat je dit format opnieuw inzet.

Geen enkele campagne overschrijdt de frequency-drempel (3,5); hoogste frequency is 2,39 (Last push Nozzle Up).

## Top performers

- **Beste CTR**: 2026: SYBB — 4,1% (sterk boven de 1%-drempel; bewezen hook-materiaal)
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: Nozzle Up END OF AUGUST — 6,4x (betrouwbaarste ROAS; SYBB's 17,8x is pixel-vertekend)

## Samenvatting

- **Totaal spend** (4 campagnes, lifetime, niet-overlappend): €4.014,27
- **Beste performer**: **2026: SYBB** — laagste CPC-tier (€0,21), veruit de hoogste CTR (4,1%) en het grootste bereik onder de recente campagnes. Dit is het sterkste hook-fundament om op door te bouwen (70-20-10: dit zijn de bewezen winnaars).
- **Slechtste performer**: **2026: SYBB - Kopie** — dure CPC (€0,64) én dure CPM (€16,34), 0 aankopen op €124 spend. Klassieke te-vroeg-gestopte testcampagne zonder statistische massa.
- **Aanbeveling**:
  1. **Fix eerst de tracking.** De SYBB purchase- en registration-waarden zijn onrealistisch hoog. Zolang de pixel-waarde niet klopt, kun je niet op ROAS optimaliseren. Verifieer via `/tracking-check` op de landing page.
  2. **Bouw voort op 2026: SYBB (70-20-10).** Dit is de bewezen winnaar qua CTR en CPC. Bij een nieuwe actieve run: 70% budget op de best presterende SYBB-hooks, 20% variaties, 10% experiment.
  3. **Herstart de Kopie niet los.** Vouw eventuele leerpunten terug in de hoofdcampagne in plaats van een aparte, te dunne test.

## Google Sheet

Overgeslagen conform instructie voor deze run (stap 6). Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-07-18_ads_report.md`. Er is niet naar de Meta Ads Tracker Google Sheet geschreven.

## Databronnen

- Meta Ads MCP (Pipeboard) — account `act_567892422940728` (Sempertex Ad Account)
- Geen Google MCPs gebruikt. PostHog niet nodig (geen actieve campagne om te cross-referencen).
