# Meta Ads Rapport -- 15 april 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode:** Last 30 days (16 maart - 14 april 2026)
**Gegenereerd:** 15 april 2026

---

## Campagne Overzicht

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Reach | Freq. | LP Views | Purchases | Purchase Value |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|-------|----------|-----------|----------------|
| 2026: SYBB | Active | EUR 701,76 | 66.261 | 1.356 | 2,0% | EUR 0,52 | EUR 10,59 | 34.460 | 1,92 | 545 | 2 | EUR 42.773,50 |

**ROAS campagne:** 60,9x (EUR 42.773,50 / EUR 701,76)
**Daily budget:** EUR 100,00
**Bid strategy:** Lowest Cost

---

## Ad-Level Performance (Actieve Ads)

| Ad | Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | LP Views | ATC | Checkouts | Purchases |
|----|-------|-------|-------|--------|-----|-----|-----|----------|-----|-----------|-----------|
| H12,B3,CTA5 | Kopie 2 | EUR 102,81 | 11.124 | 255 | 2,3% | EUR 0,40 | EUR 9,24 | 98 | 4 | 0 | 0 |
| H13,B3,CTA5 | Kopie 3 | EUR 142,66 | 12.014 | 234 | 1,9% | EUR 0,61 | EUR 11,87 | 117 | 6 | 2 | 2 |
| H11,B3,CTA5 | Kopie 1 | EUR 266,80 | 20.619 | 403 | 2,0% | EUR 0,66 | EUR 12,94 | 165 | 13 | 13 | 0 |

### Gepauzeerde Batch (Batch 4, adset origineel)

| Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | LP Views | ATC |
|-------|-------|-------|--------|-----|-----|-----|----------|-----|
| BATCH 2: Expertise & POC | EUR 139,66 | 17.767 | 357 | 2,0% | EUR 0,39 | EUR 7,86 | 129 | 2 |

*Gepauzeerd op 9 april, vervangen door Batch 5 ad sets (Kopie 1/2/3)*

---

## Underperformers

- **H11,B3,CTA5** -- CPC EUR 0,66 (drempel: EUR 0,50). Hoogste spend (EUR 266,80) maar geen purchases. CPM EUR 12,94 richting bovenkant. Aanbeveling: overweeg pauzeren of budget verschuiven naar H12/H13.
- **H13,B3,CTA5** -- CPC EUR 0,61 (drempel: EUR 0,50). Wel 2 purchases en hoogste conversiewaarde. CPC te hoog maar ROI compenseert dit. Aanbeveling: hook variatie testen om CPC te drukken.
- **Campagne gemiddeld CPC EUR 0,52** -- Net boven de EUR 0,50 target, getrokken door H11.

---

## Top Performers

- **Beste CTR:** H12,B3,CTA5 -- 2,3% (ruim boven 1% drempel)
- **Laagste CPC:** H12,B3,CTA5 -- EUR 0,40 (onder EUR 0,50 target)
- **Laagste CPM:** H12,B3,CTA5 -- EUR 9,24
- **Meeste conversies:** H13,B3,CTA5 -- 2 purchases (EUR 42.773,50 waarde)
- **Beste engagement:** H11,B3,CTA5 -- 13 add to cart, 13 initiate checkout (maar geen purchases)
- **Video views:** 13.059 totaal (H11: 4.264, H13: 2.550, H12: 1.857)

---

## PostHog Landing Page Cross-Reference

| Metric | Waarde | Target 30d | Status |
|--------|--------|------------|--------|
| Pageviews | 1.353 | -- | -- |
| Unique Sessions | 996 | -- | -- |
| Bounce Rate | 81,9% | <55% | KRITIEK |
| CTA Clicks | 633 | -- | -- |
| CTA Click Rate | 63,6% (633/996) | >4% | OK |

### UTM Bronnen (PostHog)

| Bron | Sessies | Pageviews |
|------|---------|-----------|
| meta / sybb (lowercase) | 697 | 881 |
| META / SYBB (uppercase) | 187 | 235 |
| Direct / organic | 121 | 197 |
| instagram / sybb | 15 | 23 |
| facebook / sybb | 9 | 14 |
| youtube / sybb | 2 | 3 |

**Totaal Meta Ads sessies:** 884 (88,8% van alle sessies)

### Cross-Reference Analyse

- Meta rapporteert 545 landing page views, PostHog meet 884 Meta-getagde sessies
- **Gap van 339 sessies** (62% meer in PostHog): Meta telt alleen volledig geladen pagina's als "landing page view"
- UTM inconsistentie: uppercase "META/SYBB" (187 sessies) naast lowercase "meta/sybb" (697 sessies). Fix de UTM parameters naar consistent lowercase.
- Bounce rate van 81,9% is alarmerend. Van de 996 sessies verlaten 816 de pagina zonder tweede interactie.
- 11 rageclicks gedetecteerd: mogelijk frustratie met niet-klikbare elementen

---

## Funnel Analyse (Meta Ads naar Conversie)

| Stap | Volume | Drop-off |
|------|--------|----------|
| Impressions | 66.261 | -- |
| Clicks | 1.356 | 97,9% drop |
| Link Clicks | 711 | 47,6% drop |
| Landing Page Views | 545 | 23,3% drop |
| View Content | 49 | 91,0% drop |
| Add to Cart | 26 | 46,9% drop |
| Initiate Checkout | 15 | 42,3% drop |
| Purchase | 2 | 86,7% drop |

**Grootste bottleneck:** Landing Page View naar View Content (91,0% drop). Van 545 LP views gaan slechts 49 door naar content bekijken. Dit correleert met de 81,9% bounce rate.

---

## Samenvatting

- **Totaal spend:** EUR 701,76 (30 dagen)
- **Gem. dagspend:** EUR 23,39 (ver onder EUR 100 daily budget, delivery lijkt gelimiteerd)
- **Beste performer:** H12,B3,CTA5. Laagste CPC (EUR 0,40), hoogste CTR (2,3%), meest efficiente reach. Geen purchases nog, maar funnel metrics zijn het sterkst.
- **Conversiekampioen:** H13,B3,CTA5. Enige ad met purchases (2x, EUR 42.773,50 waarde). ROAS op ad-niveau: 299,8x.
- **Slechtste performer:** H11,B3,CTA5. Hoogste spend (EUR 266,80) maar duurste CPC (EUR 0,66), geen purchases. Meta geeft deze ad de meeste impressions maar conversie blijft uit.

---

## Aanbevelingen (Hormozi 70-20-10)

### 70% Focus: Bewezen winnaars opschalen
1. **Verschuif budget van H11 naar H12 en H13.** H12 heeft de beste efficiency, H13 de enige purchases. Overweeg H11 te pauzeren.
2. **Fix de bounce rate.** 81,9% is onacceptabel. De landing page verliest 9 van de 10 bezoekers. Prioriteit: above-the-fold waardepropositie versterken, laadtijd checken, mobiele ervaring testen.

### 20% Variaties
3. **Test hook variaties op H12 body.** De hook/body combo van H12 trekt het best, maar de body (B3) en CTA (CTA5) zijn bij alle ads identiek. Test nieuwe body variaties bij H12's hook.
4. **Fix UTM inconsistentie.** Uppercase UTMs vervuilen de data. Zet alle UTMs naar lowercase format.

### 10% Experimenten
5. **Test een nieuwe hook (H16+).** Alle huidige ads draaien op H11-H15. Tijd voor verse hooks om creative fatigue voor te zijn (frequency nu 1,92, richting 2+).

---

## Google Sheet

**Status:** Overgeslagen (per instructie). Rapport opgeslagen als lokaal markdown bestand.

---

*Rapport gegenereerd op 15 april 2026 via /ads-report*
