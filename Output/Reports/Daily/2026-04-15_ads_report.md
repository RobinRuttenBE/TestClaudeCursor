# Meta Ads Rapport -- 15 april 2026

**Periode:** 16 maart 2026 t/m 14 april 2026 (last 30 days)
**Account:** Sempertex Ad Account (act_567892422940728)

---

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Reach | Freq. | LP Views | Purchases | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|-------|----------|-----------|------|
| 2026: SYBB | Active | EUR 701,76 | 66.261 | 1.356 | 2,0% | EUR 0,52 | EUR 10,59 | 34.460 | 1,92 | 545 | 2 | 60,9x |

**Overige accounts:** act_607231713057715 (Robin Rutten) is niet toegankelijk via de huidige API token.

---

## Ad-level performance (gesorteerd op spend)

| Ad | Adset | Status | Spend | Impr. | CTR | CPC | CPM | Link Clicks | LP Views | ATC | IC | Purch. |
|----|-------|--------|-------|-------|-----|-----|-----|-------------|----------|-----|----|--------|
| H11,B3,CTA5 | Kopie 1 | ACTIVE | EUR 266,80 | 20.619 | 2,0% | EUR 0,66 | EUR 12,94 | 213 | 165 | 13 | 13 | 0 |
| H13,B3,CTA5 | Kopie 3 | ACTIVE | EUR 142,66 | 12.014 | 1,9% | EUR 0,61 | EUR 11,87 | 138 | 117 | 6 | 2 | 2 |
| H14,B3,CTA5 | Origineel | PAUSED | EUR 122,96 | 16.551 | 1,8% | EUR 0,41 | EUR 7,43 | 158 | 108 | 0 | 0 | 0 |
| H12,B3,CTA5 | Kopie 2 | ACTIVE | EUR 102,81 | 11.124 | 2,3% | EUR 0,40 | EUR 9,24 | 121 | 98 | 4 | 0 | 0 |
| H15,B3,CTA5 | Kopie 4 | PAUSED | EUR 49,83 | 4.737 | 2,3% | EUR 0,47 | EUR 10,52 | 57 | 36 | 1 | 0 | 0 |
| H12,B3,CTA5 | Origineel | PAUSED | EUR 14,37 | 1.058 | 4,7% | EUR 0,29 | EUR 13,58 | 20 | 18 | 2 | 0 | 0 |
| H15,B3,CTA5 | Origineel | PAUSED | EUR 2,32 | 157 | 6,4% | EUR 0,23 | EUR 14,78 | 4 | 3 | 0 | 0 | 0 |
| H13,B3,CTA5 | Origineel | PAUSED | EUR 0,01 | 1 | 0,0% | -- | EUR 10,00 | 0 | 0 | 0 | 0 | 0 |

---

## Underperformers

- **H11,B3,CTA5 (Kopie 1)** -- CPC EUR 0,66 (drempel: EUR 0,50). Hoogste spend van alle ads (EUR 266,80) maar duurste klik. 13 ATC en 13 IC maar 0 purchases: checkout drop-off is kritiek. Aanbeveling: onderzoek checkout flow, overweeg budget te herverdelen naar H12 (Kopie 2).
- **H13,B3,CTA5 (Kopie 3)** -- CPC EUR 0,61 (drempel: EUR 0,50). Wel de enige ad met 2 purchases (EUR 42.773,50 waarde). Aanbeveling: voorlopig laten draaien vanwege conversies, monitor of purchases doorzetten.
- **Campagne-gemiddelde CPC** -- EUR 0,52 ligt net boven de target van EUR 0,50. Wordt omhoog getrokken door H11 en H13.

---

## Top performers

- **Beste CTR**: H15,B3,CTA5 (Origineel) -- 6,4% (klein volume: 157 impressions)
- **Laagste CPC**: H15,B3,CTA5 (Origineel) -- EUR 0,23 per klik
- **Beste CPC bij volume**: H12,B3,CTA5 (Kopie 2) -- EUR 0,40 bij 11.124 impressions
- **Laagste CPM**: H14,B3,CTA5 (Origineel) -- EUR 7,43
- **Beste ROAS**: H13,B3,CTA5 (Kopie 3) -- 2 purchases, EUR 42.773,50 omzet op EUR 142,66 spend = ~300x ROAS
- **Beste engagement**: H12,B3,CTA5 (Origineel) -- 4,7% CTR

---

## PostHog Cross-referentie (www.startyourballoonbusiness.com)

| Metric | Waarde | Target 30d |
|--------|--------|------------|
| Totaal pageviews | 1.172 | -- |
| Totaal sessions | 853 | -- |
| Meta sessions ("meta" + "META") | 751 (88%) | -- |
| Organic/Direct sessions | 117 (14%) | -- |
| Bounce Rate | Niet meetbaar (tracking ontbreekt) | <55% |

### Traffic bronnen (PostHog)

| UTM Source | Sessions | Pageviews |
|------------|----------|-----------|
| meta | 564 | 716 |
| META | 187 | 235 |
| (direct/organic) | 117 | 191 |
| instagram | 10 | 18 |
| facebook | 6 | 9 |
| youtube | 2 | 3 |

### Cross-referentie Meta vs PostHog

- Meta rapporteert **545 landing page views**, PostHog toont **751 Meta-gerelateerde sessions**
- Verschil (206 sessions) kan komen door: UTM case mismatch, bot traffic, of verschil in attributie venster
- **UTM case inconsistentie gedetecteerd:** "META" (187 sessions) vs "meta" (564 sessions). Per tracking standaard moet dit altijd lowercase "meta" zijn. Fix nodig in ad set configuratie.

---

## Funnel samenvatting (Meta Ads data)

| Stap | Volume | Conversie naar volgende |
|------|--------|------------------------|
| Impressions | 66.261 | -- |
| Clicks | 1.356 | 2,0% CTR |
| Link Clicks | 711 | 52,4% van clicks |
| LP Views | 545 | 76,7% van link clicks |
| View Content | 49 | 9,0% van LP views |
| Add to Cart | 26 | 53,1% van view content |
| Initiate Checkout | 15 | 57,7% van ATC |
| Purchase | 2 | 13,3% van IC |

**Bottleneck:** LP View naar View Content (9,0%). 91% van de bezoekers verlaat de pagina zonder een product te bekijken. Dit wijst op een landing page engagement probleem: de content boven de fold sluit mogelijk niet aan bij de ad belofte.

---

## Samenvatting

- **Totaal spend**: EUR 701,76 (periode: last 30 days)
- **Beste performer**: H12,B3,CTA5 (Kopie 2). Combinatie van gezonde CTR (2,3%), lage CPC (EUR 0,40), laag CPM (EUR 9,24) en 4 add-to-carts. Beste balans tussen kost en engagement.
- **Slechtste performer**: H11,B3,CTA5 (Kopie 1). Verreweg de hoogste spend (EUR 266,80) maar duurste CPC (EUR 0,66) en geen purchases. Eet 38% van het budget op zonder conversies.
- **Purchase champion**: H13,B3,CTA5 (Kopie 3). Enige ad met purchases (2x, EUR 42.773,50 totale waarde). Hoge CPC (EUR 0,61) maar positief rendement.

### Aanbevelingen (Hormozi 70-20-10)

1. **70% budget naar bewezen winnaars:** Verschuif budget van H11 (Kopie 1) naar H12 (Kopie 2) en H13 (Kopie 3). H12 heeft de beste CPC bij volume, H13 levert daadwerkelijk purchases.
2. **20% variaties testen:** Reactiveer H14,B3,CTA5 (Origineel, gepauzeerd) als variatie-test. Had EUR 7,43 CPM en EUR 0,41 CPC. Test met aangepaste CTA of landing page variant.
3. **10% experiment:** H15-hooks lieten in klein volume sterke CTR zien (2,3-6,4%). Overweeg een nieuwe adset met H15 creative in een breder publiek om te valideren.
4. **UTM fix (urgent):** Corrigeer de "META" naar "meta" in alle actieve ad sets. Dit verstoort tracking en maakt segmentatie in PostHog onbetrouwbaar.
5. **PostHog bounce tracking:** Bounce rate tracking werkt niet. Check of het PostHog JS snippet correct geconfigureerd is met `capture_pageleave: true`.
6. **LP engagement:** Slechts 9% van LP bezoekers bekijkt een product. Optimaliseer de above-the-fold content voor directe engagement.

### Google Sheet

Status: OVERGESLAGEN per instructie. Rapport opgeslagen als lokaal markdown bestand.

---

*Rapport gegenereerd op 15 april 2026 door Claude Code*
