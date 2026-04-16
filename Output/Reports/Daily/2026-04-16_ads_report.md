# Meta Ads Rapport, 16 april 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode:** 17 maart - 15 april 2026 (last 30 days)
**Rapport type:** /ads-report

> NB: Account act_607231713057715 (Robin Rutten) is niet toegankelijk via de huidige API token.

---

## Campagne Overzicht

| Campagne | Status | Spend | Impressions | Reach | Clicks | CTR | CPC | CPM | Freq. | Purchases | Purchase Value | ROAS |
|----------|--------|-------|-------------|-------|--------|-----|-----|-----|-------|-----------|----------------|------|
| 2026: SYBB | Active | €776,42 | 72.110 | 36.185 | 1.478 | 2,0% | €0,53 | €10,77 | 1,99 | 6 | €44.247,00 | 57,0x |

### Funnel Breakdown (campagne totaal)

| Stap | Aantal | Cost per |
|------|--------|----------|
| Impressions | 72.110 | €10,77 CPM |
| Link Clicks | 768 | €1,01 |
| Landing Page Views | 589 | €1,32 |
| View Content | 57 | €13,62 |
| Add to Cart | 28 | €27,73 |
| Initiate Checkout | 19 | €40,86 |
| Add Payment Info | 4 | €194,11 |
| Complete Registration | 5 | €155,28 |
| Purchase | 6 | €129,40 |

---

## Ad Set Performance (gesorteerd op spend)

| Ad Set | Status | Spend | Imp. | CTR | CPC | CPM | Link Clicks | LPV | Purch. | Value | ROAS |
|--------|--------|-------|------|-----|-----|-----|-------------|-----|--------|-------|------|
| Kopie 1 (H11) | Active | €328,99 | 25.350 | 2,0% | €0,66 | €12,98 | 259 | 197 | 4 | €1.473,50 | 4,5x |
| Kopie 3 (H13) | Active | €149,30 | 12.626 | 1,9% | €0,62 | €11,82 | 142 | 122 | 2 | €42.773,50 | 286,5x |
| Original (H14) | Paused | €139,66 | 17.767 | 2,0% | €0,39 | €7,86 | 182 | 129 | 0 | €0 | 0x |
| Kopie 2 (H12) | Active | €108,64 | 11.630 | 2,4% | €0,39 | €9,34 | 128 | 105 | 0 | €0 | 0x |
| Kopie 4 (H15) | Paused | €49,83 | 4.737 | 2,3% | €0,47 | €10,52 | 57 | 36 | 0 | €0 | 0x |

### Targeting (alle ad sets)
- Leeftijd: 18-65 (Advantage Audience aan)
- Landen: NL, BE, LU, DE
- Optimalisatie: Offsite Conversions
- Bidding: Lowest Cost Without Cap

---

## Ad Level Performance (gesorteerd op spend)

| Ad | Ad Set | Status | Spend | Imp. | CTR | CPC | LPV | Purch. | Flag |
|----|--------|--------|-------|------|-----|-----|-----|--------|------|
| H11, B3, CTA5 | Kopie 1 | Active | €328,99 | 25.350 | 2,0% | €0,66 | 197 | 4 | CPC |
| H13, B3, CTA5 | Kopie 3 | Active | €149,30 | 12.626 | 1,9% | €0,62 | 122 | 2 | CPC |
| H14, B3, CTA5 | Original | Paused | €122,96 | 16.551 | 1,8% | €0,41 | 108 | 0 | - |
| H12, B3, CTA5 | Kopie 2 | Active | €108,64 | 11.630 | 2,4% | €0,39 | 105 | 0 | - |
| H15, B3, CTA5 | Kopie 4 | Paused | €49,83 | 4.737 | 2,3% | €0,47 | 36 | 0 | - |
| H12, B3, CTA5 | Original | Paused | €14,37 | 1.058 | 4,7% | €0,29 | 18 | 0 | - |
| H15, B3, CTA5 | Original | Paused | €2,32 | 157 | 6,4% | €0,23 | 3 | 0 | klein sample |

---

## Underperformers

- **H11, B3, CTA5 (Kopie 1)**: CPC €0,66 (drempel: €0,50). Hoogste spend (€328,99 = 42% van budget) met duurst verkeer. Levert wel 4 van de 6 purchases. Aanbeveling: CPC monitoren maar niet uitschakelen vanwege conversievolume. Test nieuwe hook variaties om CPC te drukken.

- **H13, B3, CTA5 (Kopie 3)**: CPC €0,62 (drempel: €0,50). Tweede duurste verkeer. Levert 2 purchases met extreem hoge conversiewaarde (€42.773,50). Aanbeveling: actief houden vanwege hoge ROAS, maar hook optimaliseren voor goedkopere clicks.

- **Campaign gemiddelde CPC**: €0,53 (drempel: €0,50). Net boven target. De actieve ad sets met purchases (Kopie 1 en 3) trekken het gemiddelde omhoog. De goedkopere ad sets (Kopie 2 met €0,39 CPC) converteren niet.

---

## Top Performers

- **Beste CTR**: H12, B3, CTA5 (Kopie 2), 2,4%. Goedkoop verkeer (€0,39 CPC) maar geen conversies.
- **Laagste CPC**: H12, B3, CTA5 (Kopie 2), €0,39. Efficiëntste verkeer van de actieve ads.
- **Beste ROAS**: H13, B3, CTA5 (Kopie 3), 286,5x. Twee high-value purchases voor €149,30 spend.
- **Meeste conversies**: H11, B3, CTA5 (Kopie 1), 4 purchases. Meest consistente performer.

---

## PostHog Landing Page Cross-Reference (30d)

| Metric | Waarde |
|--------|--------|
| LP Pageviews (PostHog) | 1.416 |
| LP Unique Visitors (PostHog) | 947 |
| LP Views (Meta pixel) | 589 |
| Delta PostHog vs Meta | +827 pageviews (58% van traffic is niet-Meta) |

**Analyse:** Van de 1.416 pageviews op startyourballoonbusiness.com komt 42% (589) via Meta Ads. De overige 58% is organisch, direct of via andere kanalen. Dit suggereert dat de SYBB pagina ook buiten advertenties om bezocht wordt.

---

## Gepauzeerde Campagnes (historisch)

| Campagne | Status | Periode |
|----------|--------|---------|
| Last push Nozzle Up | Paused | sep 2025 |
| Nozzle Up END OF AUGUST | Paused | aug-sep 2025 |
| Campagne Nozzle Up 2025 1 | Paused | jul-sep 2025 |

---

## Samenvatting

- **Totaal spend**: €776,42 (30 dagen)
- **Dagelijks budget**: €100,00 (ingesteld) / €25,88 (werkelijk gemiddeld)
- **Beste performer**: H13, B3, CTA5 (Kopie 3). Twee high-value conversies en extreme ROAS. Daarnaast H11, B3, CTA5 (Kopie 1) met de meeste conversies (4x).
- **Aandachtspunt**: H12, B3, CTA5 (Kopie 2) trekt goedkoop verkeer maar converteert niet. Na 7 dagen en €108,64 geen enkele purchase.
- **Frequency**: Campagne gemiddeld 1,99. Veilig. Geen creative fatigue risico.

### Aanbevelingen (Hormozi 70-20-10)

**70% bewezen winnaars:**
1. Schaal H13, B3, CTA5 (Kopie 3) op. Heeft de hoogste ROAS en nog lage frequency (1,50). Meer budget toekennen.
2. H11, B3, CTA5 (Kopie 1) blijft de meest consistente performer. CPC is hoog maar het levert.

**20% variaties:**
3. Maak variaties op H13 en H11 hooks met lagere CPC als doel. Behoud de body (B3) en CTA (CTA5), test nieuwe hooks.

**10% experimenten:**
4. Overweeg H12 (Kopie 2) te pauzeren als er na nog 3 dagen geen conversie komt. Het verkeer is goedkoop maar converteert niet, wat kan duiden op een audience-hook mismatch.

### KPI Check vs Targets

| KPI | Huidig | Target 30d | Status |
|-----|--------|-----------|--------|
| CPC | €0,53 | <€0,50 | Net boven target |
| LP Bounce Rate | Niet gemeten | <55% | Onbekend |
| LP Conversie Rate | 1,0% (6 purch / 589 LPV) | >5% | Onder target |
| CTA Click Rate | Niet gemeten | >4% | Onbekend |

---

## Google Sheet

**Status:** Stap overgeslagen conform instructie. Data is opgeslagen in dit lokale rapport.

---

*Rapport gegenereerd op 16 april 2026 via /ads-report*
