# Meta Ads Rapport -- 15 april 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode:** Last 30 days (16 maart - 14 april 2026)
**Gegenereerd:** 15 april 2026

---

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Reach | Freq. | LP Views | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|-------|----------|-------|------|
| 2026: SYBB | Active | EUR 701,77 | 66.263 | 1.356 | 2,0% | EUR 0,52 | EUR 10,59 | 34.460 | 1,92 | 545 | 2 | 60,9x |

**Budget:** EUR 100/dag | **Objective:** OUTCOME_SALES | **Bid Strategy:** Lowest Cost

---

## Ad-level Performance (actieve ads)

| Ad | Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | Link Clicks | LP Views | ATC | IC | Purch. | ROAS |
|----|-------|-------|-------|--------|-----|-----|-----|-------------|----------|-----|-----|--------|------|
| H11,B3,CTA5 | Batch 2 Kopie 1 | EUR 266,81 | 20.621 | 403 | 2,0% | EUR 0,66 | EUR 12,94 | 213 | 165 | 13 | 13 | 0 | 0x |
| H13,B3,CTA5 | Batch 2 Kopie 3 | EUR 142,66 | 12.014 | 234 | 1,9% | EUR 0,61 | EUR 11,87 | 138 | 117 | 6 | 2 | 2 | 299,8x |
| H12,B3,CTA5 | Batch 2 Kopie 2 | EUR 102,81 | 11.124 | 255 | 2,3% | EUR 0,40 | EUR 9,24 | 121 | 98 | 4 | 0 | 0 | 0x |

**Overige spend (gepauzeerde batch 4 ads):** EUR 189,49

---

## Funnel Breakdown (campagne totaal)

| Stap | Aantal | Conversie |
|------|--------|-----------|
| Impressions | 66.263 | -- |
| Clicks | 1.356 | 2,0% van impressions |
| Link Clicks | 711 | 52,4% van clicks |
| Landing Page Views | 545 | 76,7% van link clicks |
| View Content (pixel) | 49 | 9,0% van LP views |
| Add to Cart | 26 | 53,1% van view content |
| Initiate Checkout | 15 | 57,7% van ATC |
| Purchase | 2 | 13,3% van IC |

**Purchase waarde:** EUR 42.773,50 (2 purchases)
**Cost per Purchase:** EUR 350,89

---

## PostHog Cross-referentie (Landing Page)

| Metric | Waarde |
|--------|--------|
| Totaal SYBB pageviews (30d) | 1.354 |
| Unieke bezoekers (30d) | 909 |
| Meta traffic pageviews (utm_source=meta) | 882 |
| Meta traffic % van totaal | 65,1% |
| Meta LP views (Ads Manager) | 545 |
| PostHog meta pageviews | 882 |
| Verschil (tracking gap) | +337 (+61,8%) |

**Analyse:** PostHog registreert 882 pageviews van meta traffic, terwijl Meta Ads Manager 545 landing page views rapporteert. Dit verschil (337 sessies) is normaal: Meta telt alleen views waar de pagina volledig laadt, PostHog tracked elke pageview inclusief herbezoeken en snelle bounces.

---

## Underperformers

- **H11,B3,CTA5** -- CPC EUR 0,66 (drempel: EUR 0,50). Hoogste spend (EUR 266,81) maar 0 purchases. Wel 13 add-to-carts en 13 initiate checkouts, wat betekent dat de funnel ergens na checkout blokkeert. Aanbeveling: Analyseer waarom checkout niet converteert. Mogelijk checkout flow issue, niet de ad zelf.

- **H13,B3,CTA5** -- CPC EUR 0,61 (drempel: EUR 0,50). Maar dit is de enige ad met purchases (2x, waarde EUR 42.773,50). De hoge CPC wordt ruimschoots gecompenseerd door ROAS van 299,8x. Aanbeveling: CPC monitoren maar NIET pauzeren, dit is de winnaar.

- **Campagne CPC overall** -- EUR 0,52 (marginaal boven EUR 0,50 drempel). Geen reden tot alarm, maar optimalisatie ruimte aanwezig.

---

## Top Performers

- **Beste CTR:** H12,B3,CTA5 -- 2,3% (ruim boven 1% drempel)
- **Laagste CPC:** H12,B3,CTA5 -- EUR 0,40 (enige ad onder EUR 0,50 drempel)
- **Beste ROAS:** H13,B3,CTA5 -- 299,8x (2 purchases, EUR 42.773,50 waarde)
- **Meeste engagement:** H11,B3,CTA5 -- 4.545 post engagements, 4.264 video views
- **Beste LP conversion:** H12,B3,CTA5 -- 81,0% link click-to-LP view rate

---

## Engagement Metrics (campagne totaal)

| Metric | Waarde |
|--------|--------|
| Video Views | 13.059 |
| Cost per Video View | EUR 0,05 |
| Post Reactions | 161 |
| Post Saves (netto) | 23 |
| Comments | 1 |
| Likes | 4 |

---

## Samenvatting

- **Totaal spend:** EUR 701,77 (periode: last 30 days)
- **Totaal revenue:** EUR 42.773,50 (2 workshop purchases)
- **Campaign ROAS:** 60,9x
- **Beste performer:** H13,B3,CTA5. Enige ad met daadwerkelijke purchases. ROAS 299,8x. Ondanks hogere CPC levert deze ad het geld op.
- **Efficientiester:** H12,B3,CTA5. Laagste CPC (EUR 0,40), hoogste CTR (2,3%), beste LP conversion rate. Maar nog geen purchases. Potentieel nodig: meer budget/tijd of landing page optimalisatie.
- **Bottleneck:** De funnel lekt het meest tussen LP View en View Content (pixel fire rate 9,0%). Dit wijst op een hoge bounce rate op de landing page, of een tracking gap waar de pixel niet altijd afvuurt.
- **Frequency:** 1,92 (ruim onder 3,5 fatigue drempel). Geen creative fatigue risico.

---

## Aanbevelingen (Hormozi 70-20-10)

### 70% - Bewezen winnaars verdubbelen
1. **H13 is de winner.** Overweeg meer budget naar het adset van H13 te alloceren. Dit is de enige ad die daadwerkelijk purchases genereert.
2. **H12 testen met meer budget.** Beste efficiency metrics (CPC, CTR) maar nog geen conversies. Geef deze ad meer impressies om te zien of conversies volgen.

### 20% - Variaties op winnaars
3. **H13 variaties maken.** Nieuwe body copy of CTA variaties op de H13 hook, in een nieuw adset, om te testen of de winnende hook nog beter kan converteren.

### 10% - Experimenteren
4. **Landing page bounce onderzoeken.** Met 545 LP views maar slechts 49 view content events (9%) verdwijnt 91% van het verkeer zonder meaningful engagement. Dit is het #1 verbeterpunt. Overweeg: snellere laadtijd, sterkere boven-de-vouw content, betere aansluiting tussen ad copy en LP.

---

## Google Sheet
Status: Overgeslagen (conform /ads-report instructie, alleen lokale opslag)

---

*Rapport opgeslagen in: Output/Reports/Daily/2026-04-15_ads_report.md*
