# SYBB Daily Report — 2026-04-24

## 1. Samenvatting
De campagne "2026: SYBB" stond gisteren PAUSED (sinds 2026-04-19, 16u42). Geen spend, geen impressions, geen klikken. Op de landing page kwamen via overige bronnen 2 pageviews binnen (2 unieke bezoekers, 2 sessies). De 7-daagse cijfers in dit rapport reflecteren grotendeels de Apr 18-19 burst voor de pauze.

**Kern actie:** beslissen of campagne herstart wordt, en met welke variant(en). H12_B3_CTA5 had de beste CTR (3.63%) en goedkoopste CPC (€0.45) tijdens de actieve periode.

---

## 2. Meta Ads Performance

### Campagne (2026: SYBB) — status: PAUSED
| Metric | Gisteren (24/4) | 7d totaal (18-24/4) | 7d gemiddelde / dag actief* | Trend |
|--------|----------------|----------------------|------------------------------|-------|
| Spend | €0.00 | €138.45 | €69.23 | n.v.t. (paused) |
| Impressions | 0 | 9.210 | 4.605 | n.v.t. |
| Clicks (link) | 0 | 126 | 63 | n.v.t. |
| Total Clicks | 0 | 214 | 107 | n.v.t. |
| CTR | — | 2.32% | 2.32% | n.v.t. |
| CPC | — | €0.65 | €0.65 | n.v.t. |
| Frequency | — | 1.35 | 1.35 | n.v.t. |
| Initiate Checkout | 0 | 9 | 4.5 | n.v.t. |
| Cost per IC | — | €15.38 | €15.38 | n.v.t. |

*Alleen Apr 18 (€94.64, 6.454 imp) en Apr 19 (€43.81, 2.756 imp) hadden spend. Daarna is de campagne gepauzeerd.

### Ad Variant Performance (laatste 7d, alleen Apr 18-19 actief)
| Ad (utm_content) | Impressions | Clicks | CTR | CPC | Spend | IC | LP Sessions* |
|-------------------|-------------|--------|-----|-----|-------|-----|--------------|
| h11_b3_cta5 | 5.715 | 124 | 2.17% | €0.69 | €85.09 | 4 | 144 |
| h13_b3_cta5 | 2.475 | 53 | 2.14% | €0.70 | €36.85 | 2 | 95 |
| h12_b3_cta5 | 1.020 | 37 | **3.63%** | **€0.45** | €16.51 | 3 | 41 |

*LP Sessions = unieke sessies op www.startyourballoonbusiness.com gematcht via utm_content (PostHog).

**Beste variant:** **H12_B3_CTA5** — hoogste CTR (3.63% = +57% vs H11), laagste CPC (€0.45 = -35% vs H11), en best initiate-checkout-ratio (3 IC op 37 klikken = 8.1% IC/click). Krijg meer budget toegewezen.
**Slechtste variant:** **H13_B3_CTA5** — vergelijkbare CTR/CPC als H11 maar duidelijk lagere checkout-conversie (2 IC op 53 klikken = 3.8%). Overwegen te pauzeren bij herstart.

---

## 3. Landing Page Health (www.startyourballoonbusiness.com)

### Gisteren (2026-04-24) vs 7d gemiddelde
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 2 | 53 | — | 🔴 (campagne paused) |
| Sessions | 2 | 43 | — | 🔴 |
| Bounce Rate | n.v.t. (te weinig data) | 84.5% | <55% | 🔴 |
| Avg Session Duration | n.v.t. | 37s | >90s | 🔴 |
| Avg Scroll Depth | n.v.t. | 33.5% | >60% | 🔴 |
| Scroll 25% reached | n.v.t. | 32.5% | >80% | 🔴 |
| Scroll 50% reached | n.v.t. | 30.1% | >60% | 🔴 |
| Scroll 75% reached | n.v.t. | 27.7% | >40% | 🔴 |
| Scroll 100% reached | n.v.t. | 19.3% | >20% | 🟡 |
| /booking visits | 0 | 5 (7d totaal) | — | 🔴 |

### Pageviews per pad (7d)
| Pathname | Pageviews | Sessions |
|----------|-----------|----------|
| / | 328 | 296 |
| /checkout | 24 | 21 |
| /product-page/start-your-balloon-business-professional | 15 | 13 |
| /booking | 5 | 5 |
| /thank-you-page | 1 | 1 |

### Daily traffic trend (7d)
| Datum | Pageviews | Unique | Sessions |
|-------|-----------|--------|----------|
| 2026-04-24 | 2 | 2 | 2 |
| 2026-04-23 | 4 | 3 | 3 |
| 2026-04-22 | 4 | 3 | 3 |
| 2026-04-20 | 88 | 72 | 75 |
| 2026-04-19 | 140 | 115 | 119 |
| 2026-04-18 | 135 | 100 | 102 |

Traffic is na 20/4 ineengezakt (campagne paused 19/4 's avonds), wat de organische restjes laat zien (~3 visits/dag).

---

## 4. Funnel Drop-off (laatste 7d, alle bronnen)

```
LP / pageview (296 sessions, 100%)
    ↓ -91.9%
/product-page visits (13 sessions, 4.4%)
    ↓ -38.5%
/checkout sessions (21 sessions, 7.1% — let op: kan ook direct van LP)
    ↓ -76.2%
/booking visits (5 sessions, 1.7%)
    ↓ -80.0%
/thank-you-page (1 session, 0.34%)
```

**Grootste lek:** **LP → product-page** (-91.9%). Slechts 4.4% van LP-bezoekers klikt door naar de product-pagina. Dit matched met de zwakke scroll depth (avg 33.5%) — bezoekers haken af voordat ze de CTA bereiken.

**Tweede lek:** **/checkout → /booking** (-76.2%). Veel mensen starten een checkout maar voltooien niet. Hier is meta-pixel ondersteuning (9 IC events) consistent met de 5 /booking visits.

---

## 5. Rode Vlaggen 🚩

1. 🚩 **Campagne PAUSED sinds 19/4** — geen acquisitie, geen data om op te optimaliseren. Hoogste prioriteit beslissing.
2. 🚩 **Bounce rate 84.5%** vs target <55% — ad-pagina mismatch of zwakke hero. Ver boven drempel.
3. 🚩 **Avg scroll depth 33.5%** vs target >60% — minder dan een derde van de bezoekers ziet de helft van de pagina.
4. 🚩 **CPC €0.65** in 7d — boven target van €0.50 (+30%). H11 (€0.69) en H13 (€0.70) trekken dit gemiddelde omhoog; H12 (€0.45) is wel binnen target.
5. 🚩 **Avg session duration 37s** vs target >90s — bevestiging dat de pagina niet boeit.
6. 🚩 **0 /booking visits gisteren** — direct gevolg van paused campagne; geen pipeline.
7. 🚩 **Cost per IC €15.38** — relatief duur voor een initiate checkout in B2B starter-segment.

---

## 6. Cross-References (Meta Ads × PostHog)

- **H12 punches above its weight:** 1.020 impressions → 37 clicks → 41 LP sessions (matchratio 1.1) → 3 IC. Zowel ad als landing-page ervaring werken hier samen.
- **H11 leakage:** 5.715 impressions → 124 clicks → 144 LP sessions (matched), maar slechts 4 IC (3.2%). De ad krijgt traffic maar de pagina converteert niet voor deze hook-audience.
- **H13 dropoff:** 2.475 impressions → 53 clicks → 95 LP sessions, maar 2 IC. Hoogste sessions/click ratio van de drie (1.79), wat duidt op mogelijke dubbel-klikkers/refresh, maar zwakke conversie.
- **Bounce 84.5% × ad CTR 2.32%:** mensen klikken (2.32% CTR is acceptabel) maar de pagina sluit ze direct uit. Klassiek ad-pagina mismatch signaal.

---

## 7. Top 3 Acties voor Vandaag

### 1. 🔴 Beslissen: campagne SYBB herstarten of strategisch wijzigen
- **Wat:** kies vandaag of campagne 120239435987290239 ("2026: SYBB") wordt hervat, gepauzeerd blijft, of dat de "Kopie"-variant (120243293329420239) wordt gelanceerd.
- **Waarom:** 0 spend = 0 leads. Geen iteratie mogelijk zonder traffic. De Kopie-versie is op 19/4 gemaakt — vermoedelijk staat er een herziene aanpak klaar.
- **Hoe:** Meta Ads Manager → besluit: resume met alleen H12 op verhoogd budget (€50/dag) OR launch "2026: SYBB - Kopie" met nieuwe creatives.
- **Verwachte impact:** terug naar 50-150 LP sessions per dag, 2-4 IC events.
- **Escalatie:** Geel (Robin goedkeuring vereist).

### 2. 🟠 Landing page conversie-upgrade vóór herstart
- **Wat:** de hero-sectie en CTA-positie van de homepage herzien voordat budget terug aan staat.
- **Waarom:** bounce rate 84.5%, avg scroll 33.5%, en slechts 4.4% klikt door naar de product-pagina. Geld in de huidige funnel pompen verspilt budget. Hero faalt om de scroll te triggeren.
- **Hoe:** Wix Editor — (a) hook eerste sectie visueel match maken met H12 ad copy (winnaar), (b) primaire CTA hoger plaatsen (boven de fold), (c) social proof boven scroll-line.
- **Verwachte impact:** bounce naar <70%, scroll 50% reach naar >50%, IC verdubbelen.
- **Escalatie:** Oranje (Wix Editor).

### 3. 🟡 H12-only test bij herstart, H11/H13 pauzeren
- **Wat:** als de campagne hervat wordt, alleen ad-set met H12_B3_CTA5 actief zetten met €30/dag budget gedurende 5 dagen.
- **Waarom:** H12 had de enige CTR boven 3% (3.63%) én CPC binnen target (€0.45). H11 en H13 zaten beide rond €0.69-0.70 CPC met zwakkere checkout-conversie.
- **Hoe:** Meta Ads Manager → ad-set "BATCH 2: Expertise & POC - Kopie 2" actief, Kopie 1 en Kopie 3 paused. Budget verschuiven.
- **Verwachte impact:** lagere blended CPC (€0.50 → €0.45), hogere CTR (2.32% → 3%+), 1-2 extra IC per €30.
- **Escalatie:** Geel (Robin goedkeuring).

---

## 8. Notes & Context

- **Datacontext:** PostHog `properties.$host` is `www.startyourballoonbusiness.com` (niet zonder `www.`). Skill-documentatie kan geüpdatet worden om dit standaard te gebruiken.
- **UTM verkeer afwijkingen:** 14 sessies via `bio_link` (niet uit Meta), 27 sessies zonder utm_content (mogelijk direct of organisch), 2 sessies met `test123` (testverkeer — opschonen of negeren).
- **Conversie tracking:** /thank-you-page slechts 1x bezocht in 7d, terwijl Meta 9 IC registreerde — pixel-attribution werkt grotendeels via Meta-side, niet via on-site /thank-you tracking. Aandachtspunt voor funnel-betrouwbaarheid.

---

*Rapport gegenereerd op 2026-04-25 voor data 2026-04-24. Bronnen: Meta Ads MCP (Pipeboard) en PostHog MCP. Account act_567892422940728 (Sempertex Ad Account), PostHog project Default project (149694).*
