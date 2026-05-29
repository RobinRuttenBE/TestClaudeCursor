## Meta Ads Rapport — 29 May 2026

⚠️ **Geen actieve campagnes** op beide toegankelijke accounts. Het rapport toont daarom de laatste bekende (lifetime) performance van de recentste gepauzeerde campagnes op het Sempertex account. Het account `act_607231713057715` uit de command is niet bereikbaar via deze connectie; ik zag wel AmbitionAvenue (`act_1489853856181844`, €0 spend, 0 campagnes).

**Overzicht (gepauzeerd, gesorteerd op spend):**

| Campagne | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| 2026: SYBB - Kopie | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

**Top performers:** ad **H13,B3,CTA5** is de absolute winnaar — 9,8% CTR en €0,07 CPC. De hoofdcampagne SYBB zit op elke drempel ruim goed.

**Underperformers:** de Kopie-campagne (CPC €0,64 + CPM €16,34, 0 purchases), ad **H11,B3,CTA5** (€521 spend, CPC €0,67 — grootste budgetlek), en **SYBB w/ Semp (BLACK)** (CTR 1,0%, CPC €0,61).

**⚠️ ROAS niet betrouwbaar:** €44.247 op 6 purchases = €7.374 per order. Dat is onrealistisch voor de SYBB-funnel en wijst op een verkeerd geconfigureerde pixel-waarde. Fix de pixel value-tracking vóór je ROAS-beslissingen neemt — de volume-metrics (clicks, CTR, CPC, 53 add-to-cart, 36 checkouts, 15 leads) zijn wél betrouwbaar.

**Aanbeveling (70-20-10):** bouw bij heractivatie op de bewezen winnaar H13 (70%), H15 als variatie (20%), schrap de dure low-CTR ads.

Volledig rapport opgeslagen in `Output/Reports/Daily/2026-05-29_ads_report.md` (gecommit + gepusht). Google Sheet-stap overgeslagen conform run-instructie.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
