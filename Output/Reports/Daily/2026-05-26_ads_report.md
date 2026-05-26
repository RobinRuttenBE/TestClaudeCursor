# Meta Ads Rapport, 26 May 2026

**Account:** Sempertex Ad Account (`act_567892422940728`)
**Periode primair:** last_30d (geen spend) + lifetime context voor gepauzeerde campagnes
**Status:** Geen ACTIVE campagnes. Alle campagnes staan op PAUSED. Lifetime data van de 3 grootste gepauzeerde campagnes hieronder.

> Het tweede account (`act_1489853856181844`, AmbitionAvenue) heeft €0 spend en is niet meegenomen.

---

## Overzicht per campagne (lifetime)

| Campagne | Status | Periode | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Conv. (purchase) | ROAS |
|----------|--------|---------|-------|-------------|--------|-----|-----|-----|-------|------------------|------|
| 2026: SYBB | PAUSED | 2026-01-13 → 2026-05-26 | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 2,24 | 6 (€442,47) | 0,18x |
| Last push Nozzle Up | PAUSED | 2025-09-15 → 2026-05-26 | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 2,39 | 3 (€6,23) | 0,01x |
| 2026: SYBB - Kopie | PAUSED | 2026-04-19 → 2026-05-26 | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,42 | 0 (IC: 6 × €350) | n.v.t. |

**Andere gepauzeerde campagnes (geen lifetime insights opgevraagd):** "Nozzle Up END OF AUGUST", "Campagne Nozzle Up 2025 1".

---

## Ad-level breakdown 2026: SYBB (gesorteerd op spend)

| # | Ad name | Ad set | Spend | Impressions | Clicks | CTR | CPC | Flag |
|---|---------|--------|-------|-------------|--------|-----|-----|------|
| 1 | H11, B3, CTA5 | BATCH 2 Kopie 1 | €521,56 | 38.614 | 784 | 2,0% | €0,67 | CPC hoog |
| 2 | H13, B3, CTA5 | BATCH 2 | €421,29 | 60.074 | 5.902 | 9,8% | €0,07 | CTR uitschieter, mogelijk video plays misgeteld |
| 3 | H12, B3, CTA5 | BATCH 2 | €388,40 | 48.166 | 1.248 | 2,6% | €0,31 | OK |
| 4 | H14, B3, CTA5 | BATCH 2 | €232,36 | 33.235 | 911 | 2,7% | €0,26 | OK |
| 5 | H15, B3, CTA5 | BATCH 2 | €218,96 | 34.299 | 1.465 | 4,3% | €0,15 | Beste echte performer |
| 6 | H13, B3, CTA5 | BATCH 2 Kopie 3 | €206,99 | 16.766 | 331 | 2,0% | €0,63 | CPC hoog |
| 7 | H11, B3, CTA5 | BATCH 2 | €202,48 | 31.060 | 796 | 2,6% | €0,25 | OK |
| 8 | H12, B3, CTA5 | BATCH 2 Kopie 2 | €141,43 | 13.955 | 356 | 2,6% | €0,40 | Net onder drempel |
| 9 | SYBB w/ Semp (BLACK) | STATISCH testset | €101,74 | 16.268 | 167 | 1,0% | €0,61 | CTR laag + CPC hoog |
| 10 | H15, B3, CTA5 | BATCH 2 Kopie 4 | €49,83 | 4.737 | 107 | 2,3% | €0,47 | OK |

---

## Underperformers

- **2026: SYBB - Kopie (campagne)** CPM €16,34 (drempel €15), CPC €0,64. Aanbeveling: niet heractiveren in huidige vorm, batch eerst opnieuw bouwen met de bewezen hook H15.
- **Ad H11, B3, CTA5 (BATCH 2 Kopie 1)** CPC €0,67 op €521 spend. Aanbeveling: pauzeer permanent, dupliceer alleen de originele BATCH 2-versie.
- **Ad H13, B3, CTA5 (BATCH 2 Kopie 3)** CPC €0,63, CTR 2,0%. Aanbeveling: archiveer kopie, focus op originele.
- **Ad SYBB w/ Semp (BLACK)** CTR 1,0% (drempel 1%), CPC €0,61. Aanbeveling: statische BLACK creatief loslaten, video-hooks halen veel meer engagement.
- **Frequency 2026: SYBB** 2,24 over lifetime. Aanbeveling: bij heropstart targeting verbreden of fresh creative om saturation te vermijden.

---

## Top performers

- **Beste CTR (echt):** H15, B3, CTA5 (BATCH 2) — 4,3% CTR bij €0,15 CPC. Dit is de winnende hook.
- **Laagste CPC:** H13, B3, CTA5 (BATCH 2) — €0,07. Let op: CTR 9,8% is een uitschieter die waarschijnlijk een video-play actie als klik registreert. Behandel als bewezen hook, maar valideer in PostHog of er werkelijke landing page views uitkomen.
- **Beste ROAS op campagne-niveau:** geen enkele campagne haalt 1,0x. Purchase tracking lijkt ondergerapporteerd (6 purchases over €2.485 spend op SYBB, 3 purchases met €6,23 totaalwaarde op Nozzle Up wijst op tracking issue).

---

## Samenvatting

- **Totaal spend (3 grootste paused campagnes, lifetime):** €3.410,24
- **Totaal impressions:** 414.658
- **Totaal clicks:** 15.048
- **Totaal LP views (volgens Meta Pixel):** ±9.012
- **Spend last_30d:** €0,00 (alle campagnes paused)
- **Beste performer:** 2026: SYBB — €0,21 gemiddelde CPC, 4,1% CTR. Hook H15 + ad set BATCH 2 is de combinatie om mee verder te gaan.
- **Slechtste performer:** 2026: SYBB - Kopie — duplicaten van BATCH 2 met substantieel hogere CPC (€0,64 vs €0,21 origineel). De Kopie-strategie heeft Meta dwingen herleren en CPM laten oplopen.
- **Hormozi 70-20-10 aanbeveling bij heropstart:**
  - 70% budget op de bewezen winnaar: H15, B3, CTA5 (BATCH 2) — €0,15 CPC, 4,3% CTR
  - 20% op variaties van H15 (zelfde body/CTA, ander visueel, andere openingsregel)
  - 10% op één nieuwe hook-test (bijvoorbeeld een POC of testimonial-format)
- **Tracking actie:** purchase value €442 op €2.485 spend voor SYBB en €6 op €800 spend voor Nozzle Up wijst op gebroken e-commerce conversion tracking. Voor heropstart eerst Meta Pixel + Wix conversie events valideren, anders blijft ROAS-meting onbruikbaar.

---

## PostHog cross-reference (last 30 days, startyourballoonbusiness.com)

- **Totale pageviews:** 110
- **Sessies:** 90
- **Unieke visitors:** 81
- **Top URLs:**
  - `/` (homepage): 40 pv (organisch)
  - `/?utm_source=instagram&utm_medium=organic` (bio link): 29 pv
  - `/review`: 21 pv
  - `/?utm_source=facebook&utm_medium=organic`: 10 pv
  - `/?utm_source=meta&utm_medium=cpc&utm_content=h13_b3_cta5` (resterende Meta traffic): 2 pv
  - `/booking` met Meta UTM `h11_b3_cta5`: 1 pv
  - `/checkout`: 3 sessies
  - `/thank-you-page`: 1
- **Cross-reference inzicht:** alle bezoekers van de afgelopen 30 dagen komen via organische social posts (Instagram bio, Facebook bio) of direct. De campagnes zijn al >30 dagen niet meer actief, dus er is geen paid-to-LP funnel data om te benchmarken. Wel zichtbaar: organisch verkeer blijft minimaal (90 sessies/30d) en mist conversies — heropstart van paid is nodig om de funnel te voeden.

---

## Google Sheet

[Stap overgeslagen volgens instructie. Rapport uitsluitend opgeslagen als `Output/Reports/Daily/2026-05-26_ads_report.md`.]

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
