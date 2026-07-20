# Meta Ads Rapport — 20 juli 2026

> **Let op:** Er zijn momenteel **geen actieve campagnes** op de toegankelijke ad accounts. Onderstaand rapport toont de meest recente **gepauzeerde** campagnes met hun laatste (lifetime) performance data. Cijfers zijn lifetime per campagne (niet last 30 days), omdat alle campagnes gepauzeerd zijn en er in de afgelopen 30 dagen geen spend was.

**Accounts gecheckt:**
- `act_567892422940728` (Sempertex Ad Account) — 5 gepauzeerde campagnes, geen actieve
- `act_1489853856181844` (AmbitionAvenue) — geen campagnes
- `act_607231713057715` (Robin Rutten) — **geen toegang** met huidige API token (toegestaan: act_1489853856181844, act_567892422940728)

---

## Overzicht per campagne (gepauzeerd, gesorteerd op spend)

| Campagne | Status | Periode | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|---------|-------|-------------|--------|-----|-----|-----|----------|------|
| 2026: SYBB | Paused | 13 jan–20 jul 2026 | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | 23 jul 2025 | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | 15 sep 2025 | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | 26 aug 2025 | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | 19 apr 2026 | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

*ROAS berekend uit `purchase` action_values / spend. Aankoopvolume is laag (3–6 per campagne), dus ROAS-cijfers zijn indicatief, niet statistisch robuust.*

---

## Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel: €0,50) → Aanbeveling: te duur bij laag volume (195 clicks, 0 aankopen). Deze kopie-test niet heractiveren zonder nieuwe hook; budget naar de bewezen hoofdcampagne.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel: €15) → Aanbeveling: dure reach, smalle/verzadigde targeting. Breder publiek of nieuwe creative testen voordat je opnieuw spendt.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel: 1%) → Aanbeveling: op de grens. Zeer lage CPM (€1,64) en CPC (€0,17) compenseren, maar de hook trekt relatief weinig door. Bij heractivatie: sterkere hook op de eerste frame.
- **Last push Nozzle Up** — ROAS 0,8x (spend €800,78 → €623 omzet) → Aanbeveling: verliesgevend. Dit was een end-of-campaign push met verzadigd publiek (frequency 2,39). Niet herhalen als los format.

*Geen enkele campagne overschreed de frequency-drempel (>3,5). Hoogste frequency: Campagne Nozzle Up 2025 1 met 2,89.*

---

## Top performers

- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — 17,8x (€2.485 → €44.247), gevolgd door Campagne Nozzle Up 2025 1 — 8,3x
- **Laagste CPM**: Nozzle Up END OF AUGUST — €1,64

---

## Samenvatting

- **Totaal spend**: €4.867,46 (lifetime, 5 gepauzeerde campagnes — komt exact overeen met de account lifetime spend)
- **Beste performer**: **2026: SYBB** — beste CTR (4,1%), lage CPC (€0,21) én hoogste ROAS (17,8x). Dit is de bewezen winnaar van het account.
- **Slechtste performer**: **2026: SYBB - Kopie** — hoogste CPC (€0,64) en CPM (€16,34), 0 aankopen op €124 spend. De kopie-test presteerde structureel slechter dan het origineel.
- **Aanbeveling (Hormozi 70-20-10)**: Zet het budget op de bewezen winnaar. **2026: SYBB** is je 70%-fundament: heractiveer deze als hoofdcampagne (daily budget stond op €100). Gebruik 20% voor variaties op de SYBB-hooks die de 4,1% CTR opleverden, en reserveer 10% voor experimenten. Stop met losstaande "kopie"- en "last push"-campagnes zonder nieuwe hoek. Nozzle Up-format is uitgewerkt (verzadigd publiek, dalende ROAS in de laatste push).

---

## Google Sheet
Overgeslagen conform run-instructie (stap 6 niet uitgevoerd). Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-07-20_ads_report.md`. Geen schrijfactie naar de Meta Ads Tracker Google Sheet.
