# Morning Report — 2026-05-16

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,36%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,06** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 70,75** over 4 actieve dagen (niet totaal/30)
> - Bron: spend EUR 283,02 · impressions 19.726 · link_clicks 268
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H11, B3, CTA5 | EUR 192,54 | 13.261 | 169 | 1,27% | EUR 1,14 |
> | H13,B3,CTA5 | EUR 57,69 | 4.140 | 53 | 1,28% | EUR 1,09 |
> | H12,B3,CTA5 | EUR 32,79 | 2.325 | 46 | 1,98% | EUR 0,71 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-16_ads_report.md` (gecommit en gepusht).

## Meta Ads Rapport — 16 May 2026

> **Geen actieve campagnes.** Account `act_607231713057715` uit de skill bestaat niet meer; beschikbaar zijn `act_567892422940728` (Sempertex) en `act_1489853856181844` (AmbitionAvenue, €0). Hieronder de 5 meest recente gepauzeerde campagnes met laatste/lifetime data. De som van de spend (€4.867,46) = volledige accounthistorie.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Purch. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|--------|-------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 2,2 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 2,9 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 2,4 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 2,2 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,4 | 0 | n.v.t. |

\* ROAS = purchase value ÷ spend. **Caveat:** lage conversie-aantallen (0–6) + deels toegekende Meta-waarden → richtinggevend, geen hard cijfer.

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) → te vroeg om te oordelen (€124 spend); mergen in hoofd-SYBB i.p.v. los heropstarten
- **2026: SYBB - Kopie** — CPM €16,34 (>€15) → dure reach door kleine audience; bredere targeting bij heropstart
- **Nozzle Up END OF AUGUST** — CTR 1,0% (≈drempel) → laagste engagement; niet als hook-referentie hergebruiken
- **Frequency:** geen enkele campagne >3,5 — geen creative fatigue risico

### Top performers

- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — 17,8x (richtinggevend); meest betrouwbaar op volume: Nozzle Up 2025 1 — 8,3x

### Samenvatting

- **Totaal spend**: €4.867,46 (volledige historie, geen actieve campagnes)
- **Beste performer**: **2026: SYBB** — sterkste op schaal (4,1% CTR, €0,21 CPC over ~300k impressies). De bewezen winnaar.
- **Slechtste performer**: **2026: SYBB - Kopie** — duurste CPC én CPM, nul purchases. Onafgewerkte duplicaat.
- **Aanbeveling (70-20-10)**: **70%** heropstart "2026: SYBB" met verhoogd budget · **20%** test creative-variaties bínnen die structuur (niet de losse Kopie) · **10%** hergebruik de Nozzle Up 2025 1 hook (8,3x) richting SYBB-publiek · **opruimen:** archiveer SYBB-Kopie, Last push Nozzle Up (0,8x) en Nozzle Up END OF AUGUST (CTR <1%).

### Google Sheet
Overgeslagen op verzoek (strikte run-regel: geen Google MCPs). Lokaal opgeslagen.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Klaar. Rapport gegenereerd, opgeslagen en gepusht.

## Belangrijkste bevinding

De Meta campagne **"2026: SYBB" staat op PAUSED en levert niets uit**. De Meta Ads MCP gaf voor 15 May én voor de volledige periode 9 t/m 15 May een lege dataset terug: nul spend, impressies en clicks. Dit is de enige echt relevante anomalie.

## Wat het rapport bevat

- **Meta Ads:** campagne gevonden (id `120239435987290239`, account `act_567892422940728`), status PAUSED, daily budget €100. Geen delivery dus geen variant/CPC/CTR data.
- **PostHog (`www.startyourballoonbusiness.com`):** gisteren 3 sessies / 4 pageviews / 3 unieke bezoekers, 0% bounce, ~245s sessieduur. Alles organisch via `bio_link` en direct, geen betaalde UTM. 7-daags baseline meegenomen per dag.
- **Datagaten gemeld:** PostHog vangt alleen `$pageview` plus systeemevents. **Geen scroll-depth en geen CTA-click tracking** ingericht, dus die KPI's en de funnel konden niet gerapporteerd worden.

## Top 3 acties
1. Bevestig of de pauze van "2026: SYBB" bewust is, heractiveer indien niet.
2. Richt scroll-depth en CTA-click tracking in op de landingspagina.
3. Geen optimalisatie op ad/pagina-niveau: 3 sessies is statistische ruis.

Conform de run-instructie zijn alleen de Meta Ads MCP en PostHog MCP gebruikt, geen Google MCPs en niet naar de tracker Sheet geschreven. Output staat in `Output/Reports/Daily/2026-05-15_sybb_report.md`.

Eén kanttekening die geen onderdeel van de taak was: je git committer-identiteit is niet expliciet ingesteld (`Robin Rutten <robinrutten@Mac-mini.local>`, automatisch afgeleid). De push slaagde. Laat het weten als je dit wilt corrigeren.

---

Gecommit en gepusht naar GitHub (`main 11beac2`). Klaar.

Korte conclusie: er viel niets te optimaliseren omdat geen enkele campagne actief is. Het rapport documenteert dit volledig, inclusief de twee aandachtspunten (gepauzeerde SYBB-campagne en het ontoegankelijke account `act_607231713057715`).

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 192,54 | 169 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 32,79 | 46 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 57,69 | 53 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 283,02** | **268** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
> - Sessie op 2026-04-18, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
