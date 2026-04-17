# Meta Ads Rapport — 2026-04-17

**Periode:** last_30d (2026-03-18 → 2026-04-16)
**Account:** Sempertex Ad Account (act_567892422940728)
**Databron:** Pipeboard Meta Ads MCP

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (Purchase) | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|------------------|-------|
| 2026: SYBB | Active | €834,24 | 76.611 | 1.582 | 2,1% | €0,53 | €10,89 | 6 | 53,04x |

\*ROAS op basis van Meta pixel `purchase_value = €44.247`. Dit cijfer wijkt sterk af van de realistische workshop ticket waarde. Zeer waarschijnlijk overtelling in Meta-attributie (ook `complete_registration_value = €86.100` is onrealistisch hoog). Zie sectie *Data caveat*.

**Funnel absolute cijfers (campagne):**
- Link clicks: 832
- Landing page views: 643 (LPV/Click = 77,3%)
- Add to Cart: 38
- Initiate Checkout: 24
- Add Payment Info: 4
- Purchase: 6 (CPA €139,04)

## Overzicht per ad (gesorteerd op spend)

| Ad naam | Adset | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | LPV | ATC | Purch. |
|---------|-------|--------|-------|-------|--------|-----|-----|-----|-------|-----|-----|--------|
| H11,B3,CTA5 | Kopie 1 | **Active** | €370,45 | 28.507 | 569 | 2,0% | €0,65 🚩 | €13,00 | 1,76 | 232 | 20 | 4 |
| H13,B3,CTA5 | Kopie 3 | **Active** | €158,28 | 13.334 | 258 | 1,9% | €0,61 🚩 | €11,87 | 1,52 | 131 | 8 | 2 |
| H14,B3,CTA5 | BATCH 2 | Paused | €122,96 | 16.551 | 297 | 1,8% | €0,41 | €7,43 | 1,34 | 108 | 0 | 0 |
| H12,B3,CTA5 | Kopie 2 | **Active** | €116,02 | 12.266 | 291 | 2,4% | €0,40 | €9,46 | 1,82 | 115 | 7 | 0 |
| H15,B3,CTA5 | Kopie 4 | Paused | €49,83 | 4.737 | 107 | 2,3% | €0,47 | €10,52 | 1,45 | 36 | 1 | 0 |
| H12,B3,CTA5 | BATCH 2 | Paused | €14,37 | 1.058 | 50 | 4,7% | €0,29 | €13,58 | 1,94 | 18 | 2 | 0 |
| H15,B3,CTA5 | BATCH 2 | Paused | €2,32 | 157 | 10 | 6,4% | €0,23 | €14,78 | 1,34 | 3 | 0 | 0 |
| H13,B3,CTA5 | BATCH 2 | Paused | €0,01 | 1 | 0 | 0,0% | n/a | €10,00 | 1,00 | 0 | 0 | 0 |

🚩 = flag op drempelwaarde

## Underperformers

- **H11,B3,CTA5 (Kopie 1, ACTIVE)** — CPC €0,65 ligt 30% boven de drempel van €0,50. Grootste spend van de campagne (€370,45, 44% van totaal). CTR van 2,0% is gezond, dus dure clicks komen niet door weak hook maar door auction pricing / audience overlap. Aanbeveling: bid cap toevoegen of audience verfijnen; niet uitschakelen, want levert wel 4 purchases op (beste converter).
- **H13,B3,CTA5 (Kopie 3, ACTIVE)** — CPC €0,61 boven drempel. 2 purchases, CPA €79,14 (helft van campagne gemiddelde). Marginaal maar converteert. Aanbeveling: hou 1 week langer aan, monitor CPC trend.
- **Campagne totaal** — CPC €0,53 zit net boven drempel €0,50. Gedreven door H11 en H13. Alle overige metrics (CTR 2,1%, CPM €10,89, Freq 2,06) ruim binnen targets.
- **Geen frequency issues.** Hoogste frequency op actieve ads = 1,82 (H12, Kopie 2). Ruim onder de 3,5 drempel → nog geen creative fatigue.

## Top performers

- **Beste CTR (significant volume):** H12,B3,CTA5 (Kopie 2, ACTIVE) — 2,4% bij 12.266 impressies
- **Laagste CPC (significant volume):** H12,B3,CTA5 (Kopie 2, ACTIVE) — €0,40
- **Meeste purchases:** H11,B3,CTA5 (Kopie 1, ACTIVE) — 4 purchases, CPA €92,61
- **Beste funnel doorstroom (LPV/Click):** H11 Kopie 1 = 76,5%, H13 Kopie 3 = 86,2% — sterke page relevance
- **Hoogste CTR absoluut:** H15,B3,CTA5 (BATCH 2, PAUSED) — 6,4% maar slechts 10 clicks, niet significant

## Samenvatting

- **Totaal spend:** €834,24 (last 30d, 4 ACTIVE ads + legacy volume van nu gepauzeerde BATCH 2 ads)
- **Beste performer:** H12 Kopie 2 — laagste CPC (€0,40), hoogste CTR (2,4%) op significant volume, frequency nog laag (1,82). Hook H12 wint op engagement efficiency. Enige minpunt: 0 purchases in 30d ondanks 115 LPV en 7 ATC → funnel stokt na Add to Cart.
- **Slechtste performer onder ACTIVE:** H13 Kopie 3 — CPC €0,61, slechts 2 purchases, lage ATC ratio (8 op 131 LPV = 6,1%).
- **Belangrijkste observatie:** De 70-20-10 regel staat onder druk. 3 actieve ads, allen met hook batch B3/CTA5. Geen variatie in bewezen winners. H11 doet het werk qua purchases (4 van 6), maar 1 ad kan geen campagne dragen.
- **Aanbeveling (Hormozi 70-20-10):**
  1. **70% bewezen:** Verhoog budget op H11 Kopie 1 met 30%, ondanks de hoge CPC. Het is je enige bewezen converter.
  2. **20% variaties:** Maak 2 nieuwe varianten op H11 hook met andere CTA (CTA6, CTA7). H11 hook werkt, test of een scherpere CTA de CPC drukt.
  3. **10% experiment:** Test een nieuwe hook batch (B4) met de sterkste CTA uit H11 om verdere creative fatigue op H11 voor te zijn.
  4. **Funnel fix:** H12 Kopie 2 en H13 Kopie 3 hebben Add to Cart maar geen Purchase. Checkout flow en cart abandonment email moeten gecheckt worden (Pillar 7 van SYBB — pricing pagina friction?).

## Data caveat

De `purchase_value` van €44.247 bij slechts 6 purchases (gemiddeld €7.374 per transactie) is niet consistent met de startyourballoonbusiness.com workshop ticketprijs. Ook `complete_registration_value = €86.100` voor 6 registraties is onmogelijk. Mogelijke oorzaken:
- Meta pixel fires purchase event met verkeerde value parameter (bijv. lifetime value of conversion value placeholder).
- Dubbeltelling tussen onsite_web_purchase en omni_purchase.
- Pixel mapping naar shopifystore met verkeerde product SKU.

**Actie:** check Meta Events Manager → Data Source → SYBB pixel (ID 888973173636482) → `purchase` event quality. Tot die check klopt, ROAS getal is niet bruikbaar voor beslissingen. Stuur op CPA (€139,04) en absolute purchase count (6 in 30d).

## Google Sheet

**Niet geschreven.** Stap 6 overgeslagen conform instructie — enkel Meta Ads MCP en PostHog MCP mogen gebruikt worden. Rapport opgeslagen in:
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-17_ads_report.md`

## Accounts check

- `act_567892422940728` (Sempertex) — 1 actieve campagne (2026: SYBB).
- `act_1489853856181844` — 0 actieve campagnes.
- `act_607231713057715` (Robin Rutten) — geen API toegang met huidige token. Niet gecheckt.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
