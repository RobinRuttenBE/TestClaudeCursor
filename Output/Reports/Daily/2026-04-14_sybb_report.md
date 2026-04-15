# SYBB Daily Report — 2026-04-14

## 1. Samenvatting
Rustiger dag: spend daalde met 32% naar €95,91 (vs €140,48 gisteren) terwijl CPC op €0,63 bleef hangen, nog steeds boven target van €0,50. Slechts 3 ads actief (H15 niet meer live). H11 blijft dominant met 66% van spend en hoogste CPC. H12 is opnieuw de efficiëntste variant (beste CTR 2,85%, laagste CPC €0,52) en genereert als enige add-to-carts (2). Geen purchases gisteren, net als 13 april.

**PostHog data niet beschikbaar:** PostHog MCP is niet verbonden in deze sessie. Landing page health, scroll depth, bounce rate en funnel data ontbreken. Aanbevolen: herstart sessie met actieve PostHog MCP voor compleet rapport.

## 2. Meta Ads Performance

### Campaign Totals
| Metric | Gisteren (14/04) | 7d Daily Avg | Trend |
|---|---|---|---|
| Spend | €95,91 | €100,25 | → stabiel (-4%) |
| Impressions | 7.288 | 9.465 | ↓ -23% |
| Clicks (all) | 152 | 193 | ↓ -21% |
| Link clicks | 83 | 102 | ↓ -18% |
| CTR | 2,09% | 2,04% | → stabiel |
| CPC (all) | €0,63 | €0,52 | ↑ +21% 🚩 |
| Frequency | 1,53 | 1,92 (7d agg) | ↓ lager (goed) |
| Landing page views | 63 | 78 | ↓ -19% |
| Add to cart | 2 | 3,7 | ↓ |
| Initiate checkout | 0 | 2,1 | ↓ |
| Purchases | 0 | 0,3 (2 in 7d) | → |
| Video views | 1.565 | 1.865 | ↓ -16% |

### Ad Variant Performance (gisteren)
| Ad (utm_content) | Impr | Link Clicks | CTR | CPC | Spend | LP Views | ATC | View Content |
|---|---|---|---|---|---|---|---|---|
| h11_b3_cta5 | 4.900 | 55 | 2,02% | €0,64 | €63,49 (66%) | 40 | 0 | 4 |
| h13_b3_cta5 | 1.791 | 19 | 2,01% | €0,65 | €23,57 (25%) | 14 | 0 | 2 |
| h12_b3_cta5 | 597 | 9 | 2,85% | €0,52 | €8,85 (9%) | 9 | 2 | 1 |

**Beste variant:** H12 (CTR 2,85%, laagste CPC €0,52, enige met add-to-carts). Krijgt slechts 9% van het budget.
**Slechtste variant:** H11 (laagste CTR 2,02%, hoogste CPC €0,64, 66% van spend, 0 add-to-carts).
**Opvallend:** H15 is niet meer actief (was wel live op 13/04 met 100% bounce). Mogelijk gepauzeerd na gisteren.

### Ad Set Performance (gisteren)
| Ad Set | Spend | Impr | CTR | CPC | Freq | LP Views |
|---|---|---|---|---|---|---|
| BATCH 2: Expertise & POC - Kopie 1 (H11) | €63,49 | 4.900 | 2,02% | €0,64 | 1,34 | 40 |
| BATCH 2: Expertise & POC - Kopie 3 (H13) | €23,57 | 1.791 | 2,01% | €0,65 | 1,27 | 14 |
| BATCH 2: Expertise & POC - Kopie 2 (H12) | €8,85 | 597 | 2,85% | €0,52 | 1,64 | 9 |

## 3. Landing Page Health (startyourballoonbusiness.com)

⚠️ **PostHog MCP niet verbonden in deze sessie.** Onderstaande metrics zijn niet beschikbaar:
- Pageviews, unique visitors, sessions
- Bounce rate (overall en per UTM)
- Scroll depth distribution (25/50/75/100%)
- Average session duration
- CTA click rate
- Path distribution (/booking, /checkout visits)
- Session recordings

**Referentie gisteren (13/04):** Bounce rate was 73,4% (7d avg 81,9%), avg scroll 60,1%. Target bounce rate is <55%.

## 4. Funnel Drop-off

Partiële funnel op basis van Meta Ads data:
```
Meta link clicks (83) → LP views (63) → Add to cart (2) → Initiate checkout (0) → Purchase (0)
     100%                  75,9%           2,4%               0%                      0%
```

**Link click → LP view drop:** 24% verlies (83 → 63). Normaal range 20-30%, dit is acceptabel.
**LP view → ATC:** slechts 3,2% (2 van 63). Laag, maar alle ATC komt van H12 variant.
**ATC → Checkout:** 0% conversie gisteren. Beide add-to-carts kwamen niet door naar checkout.

**Zonder PostHog data:** scrolldiepte, CTA clicks en on-page funnel niet beschikbaar.

## 5. Rode Vlaggen 🚩

- 🚩 **CPC +21% vs 7d avg:** €0,63 vs €0,52. Boven target €0,50 (30d). Tweede dag op rij boven €0,60.
- 🚩 **H11 domineert budget inefficiënt:** 66% van spend (€63,49), laagste CTR (2,02%), 0 add-to-carts, 0 purchases. Eerdere aanbeveling om budget te herverdelen nog niet uitgevoerd.
- 🚩 **0 purchases, 2e dag op rij:** Samen met 0 initiated checkouts duidt dit op een dieper checkout-probleem, niet alleen een volume-issue.
- 🚩 **H12 krijgt slechts 9% budget:** Beste performer (CTR 2,85%, CPC €0,52, enige met ATC) wordt structureel onderbedeeld door Meta's learning algorithm.
- 🚩 **Impressions -23%:** Significante daling in bereik. Mogelijk budget cap bereikt of audience verzadiging in H11's ad set.
- ⚠️ **PostHog MCP niet beschikbaar:** Geen LP health data, geen bounce rate monitoring, geen scroll depth. Cross-referencing onmogelijk.

## 6. Top 3 Acties voor Vandaag

### 1. Budget herverdelen: H11 ↓, H12 ↑ (Escalatie: Geel, Robin goedkeuring)
**Wat:** Verlaag budget op adset Kopie 1 (H11) met 50%. Verhoog adset Kopie 2 (H12) budget met het vrijgekomen bedrag.
**Waarom:** H12 is 2 dagen op rij de beste performer (CTR 2,85%, CPC €0,52, enige met ATC). H11 verbrandt 66% van het budget met de slechtste metrics en 0 down-funnel conversies. Dit patroon is consistent met 13/04 waar dezelfde aanbeveling al stond.
**Hoe:** Meta Ads Manager > Campaign 2026: SYBB > Ad Set budgets handmatig aanpassen.
**Verwachte impact:** CPC daling richting €0,55, meer budget naar bewezen converter.

### 2. Checkout flow end-to-end testen (Escalatie: Rood, Strategie)
**Wat:** Handmatig test de volledige booking flow op desktop en mobiel: LP → /booking → /checkout → purchase.
**Waarom:** 2 dagen op rij 0 purchases, 0 initiated checkouts gisteren terwijl er wel 2 ATC events zijn. Op 13/04 waren er zelfs 4 /checkout visits met 0 conversies. Er is mogelijk een technische blokkade in de checkout flow of een Meta Pixel issue.
**Hoe:** 1) Test zelf via startyourballoonbusiness.com met een test-aankoop. 2) Check Wix Bookings dashboard voor eventuele errors. 3) Verifieer Meta Pixel events op /checkout page via browser developer tools.
**Verwachte impact:** Als checkout blokkade gevonden en gefixt: directe conversie-unlock bij elke ATC.

### 3. PostHog MCP herstellen voor volledige monitoring (Escalatie: Groen, auto)
**Wat:** Herstart Claude Code sessie en verifieer dat PostHog MCP server correct draait.
**Waarom:** Zonder PostHog ontbreekt 50% van de rapportdata: bounce rate, scroll depth, CTA clicks, session recordings, UTM-level LP behavior. Cross-referencing (ad CTR vs LP bounce) is onmogelijk, waardoor ad-page mismatches niet gedetecteerd worden.
**Hoe:** 1) Check of PostHog MCP server draait (settings.local.json toont configuratie). 2) Herstart Claude Code. 3) Test met `mcp__posthog__query-run`.
**Verwachte impact:** Volledige rapportcapabiliteit hersteld, cross-referencing weer mogelijk.

---

## Bijlage: Data Notes

- **Data bronnen:** Meta Ads MCP (Pipeboard), campagne ID `120239435987290239` (`2026: SYBB`), account `act_567892422940728`.
- **PostHog:** NIET BESCHIKBAAR in deze sessie. MCP server geconfigureerd maar niet verbonden. Alle LP metrics ontbreken.
- **7d window:** 2026-04-08 t/m 2026-04-14 inclusief (Meta Ads aggregated 7d data).
- **7d daily avg berekening:** 7d totalen gedeeld door 7 (€701,74 spend / 7 = €100,25/dag).
- **Actieve ads:** 3 van 21 totaal. H15 (Kopie 4) was actief op 13/04 maar niet meer op 14/04.
- **Ad naming convention:** H = hook variant, B = body variant, CTA = call-to-action variant. Format: hXX_bX_ctaX.
- **7d purchases:** 2 totaal (beide via H13 op eerdere dagen, ROAS 60,95x op 7d campagne-niveau).
