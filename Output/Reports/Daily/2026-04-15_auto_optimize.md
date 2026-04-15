## Auto-Optimize Rapport, 15 april 2026

**Campagne:** 2026: SYBB (act_567892422940728)
**Periode:** last 3d (12-14 april 2026)
**Dagbudget:** €100,00 | **3d spend:** €376,46 (gem. €125,49/dag)
**Account act_607231713057715:** geen toegang (niet beschikbaar voor dit API token)

---

### Automatische acties uitgevoerd

Geen ads gepauzeerd. Alle 3 actieve ads presteren boven de drempelwaarden.

---

### Campagne-niveau (3d totaal)

| Metric | Waarde |
|--------|--------|
| Spend | €376,46 |
| Impressions | 27.976 |
| Reach | 14.925 |
| Frequency | 1,87 |
| Link clicks | 291 |
| **Link CTR** | **1,04%** |
| **CPC (link)** | **€1,29** |
| CPM | €13,46 |
| Landing page views | 239 |
| View content | 28 |
| Add to cart | 14 |
| Initiate checkout | 7 |
| Complete registration | 1 |

---

### Ad-niveau performance (3d)

| Ad | Ad Set | Impressions | Link clicks | Link CTR | CPC (link) | Spend | Spend % | CPM | Freq |
|----|--------|-------------|-------------|----------|-----------|-------|---------|-----|------|
| H11, B3, CTA5 | Kopie 1 | 16.148 | 158 | 0,98% | €1,40 | €220,60 | 62,4% | €13,66 | 1,59 |
| H12, B3, CTA5 | Kopie 2 | 3.096 | 37 | 1,20% | €1,16 | €42,96 | 12,2% | €13,88 | 1,77 |
| H13, B3, CTA5 | Kopie 3 | 6.993 | 82 | 1,17% | €1,10 | €90,03 | 25,5% | €12,87 | 1,39 |

**Kill-regel check:**

| Ad | Link CTR vs 0,8% | Impressions vs 1.000 | CPC (link) vs €1,50 | Link clicks vs 500 | Resultaat |
|----|-------------------|----------------------|----------------------|---------------------|-----------|
| H11 | 0,98% PASS | 16.148 PASS | €1,40 PASS | 158 (n.v.t.) | GEEN KILL |
| H12 | 1,20% PASS | 3.096 PASS | €1,16 PASS | 37 (n.v.t.) | GEEN KILL |
| H13 | 1,17% PASS | 6.993 PASS | €1,10 PASS | 82 (n.v.t.) | GEEN KILL |

---

### Funnel per ad (3d)

| Stap | H11 | H12 | H13 | Totaal |
|------|-----|-----|-----|--------|
| Link clicks | 158 | 37 | 82 | 277 |
| Landing page views | 121 | 30 | 72 | 223 |
| View content | 16 | 3 | 8 | 27 |
| Add to cart | 7 | 2 | 4 | 13 |
| Initiate checkout | 7 | 0 | 0 | 7 |
| Add payment info | 1 | 0 | 0 | 1 |
| Complete registration | 1 | 0 | 0 | 1 |

**Opvallend:** H11 genereert ALLE checkout- en registratie-events. H12 (37 link clicks) en H13 (82 link clicks) leveren nul checkouts op in de afgelopen 3 dagen.

---

### Waarschuwingen

| Ad | Signaal | Waarde | Drempel | Urgentie |
|----|---------|--------|---------|----------|
| H11 | CPC (link) nadert kill-grens | €1,40 | €1,50 | HOOG |
| H11 | Budget dominantie | 62,4% van spend | ideaal ~33% | MIDDEL |
| H12 | Nul checkouts op 124 lifetime link clicks | 0 checkouts | verwacht >0 | HOOG |
| H13 | Nul checkouts in 3d (wel 2 lifetime purchases) | 0 in 3d | n.v.t. | MIDDEL |
| LP | CTA click tracking ontbreekt in PostHog | 0 events | >0 verwacht | HOOG |

**Geen waarschuwingen voor:**
- Creative fatigue: alle frequency < 2,0 (drempel 3,5)
- Dure reach: alle CPM < €14 (drempel €15)
- Dalende Link CTR: alle 3d CTR > 97% van lifetime CTR

---

### Trend vs gisteren (dag-over-dag)

| Ad | Link CTR gisteren | Link CTR vandaag | CPC (link) gisteren | CPC (link) vandaag | Trend |
|----|-------------------|------------------|---------------------|--------------------|-------|
| H11 | 0,98% | 0,98% | €1,40 | €1,40 | Stabiel |
| H12 | 1,19% | 1,20% | €1,16 | €1,16 | Stabiel |
| H13 | 1,17% | 1,17% | €1,10 | €1,10 | Stabiel |

Alle metrics vlak. Geen verslechtering, maar ook geen verbetering.

---

### Lifetime performance (9-15 april)

| Ad | Impressions | Link clicks | Link CTR | CPC (link) | Spend | Purchases | Purchase value |
|----|-------------|-------------|----------|-----------|-------|-----------|----------------|
| H11 | 23.227 | 232 | 1,00% | €1,31 | €303,56 | 0 | €0 |
| H12 | 11.279 | 124 | 1,10% | €0,85 | €104,87 | 0 | €0 |
| H13 | 12.296 | 141 | 1,15% | €1,04 | €146,02 | 2 | €42.773,50 |

**ROAS-anomalie H13:** 2 purchases met waarde €42.773,50 (lifetime). Dit is waarschijnlijk 1 grote B2B wholesale order. ROAS = €42.773,50 / €146,02 = 293x. Dit getal is niet representatief voor structurele performance en mag niet als basis dienen voor budget-opschaling zonder verificatie.

---

### PostHog cross-referentie (12-15 april)

| Metric | Waarde |
|--------|--------|
| Totaal pageviews LP | 538 |
| Unique visitors LP | 344 |
| Meta-attributed pageviews | 465 (86,4% van totaal) |
| Pagina's per meta-sessie | ~1,9 (465 PV / 239 LP views) |
| CTA clicks getrackt | 0 |

**Cross-referentie analyse:**
- Meta meldt 239 landing page views, PostHog telt 465 meta pageviews. Dit is consistent: bezoekers bekijken gemiddeld ~1,9 pagina's per sessie. Goed engagement-signaal.
- CTA click events = 0 in PostHog. Dit is een tracking-probleem. Het `cta_click` event wordt niet getriggerd of het event heet anders. Hierdoor missen we een kritieke funnel-metric.

---

### 70-20-10 Classificatie

> NB: Link metrics drempels zijn nog niet gekalibreerd. Classificatie is indicatief.

**70% Core (Link CTR > 1,5% EN CPC link < €0,50):**
- Geen ads kwalificeren. Alle CPC (link) waarden liggen boven €0,50.

**20% Emerging (Link CTR 0,8-1,5%):**
- H11, B3, CTA5: Link CTR 0,98%, CPC (link) €1,40 (laagste efficiency)
- H12, B3, CTA5: Link CTR 1,20%, CPC (link) €1,16 (laagste CPC, maar nul conversies)
- H13, B3, CTA5: Link CTR 1,17%, CPC (link) €1,10 (beste overall balance + enige ad met lifetime purchases)

**10% Experimental:**
- Geen ads in deze categorie (alle > 3.000 impressions)

**Budget mismatch: JA**
H11 krijgt 62,4% van het budget maar is de minst efficiente ad op zowel Link CTR als CPC (link). De enige reden om H11 niet direct te beperken is dat het de enige ad is die checkout/registratie-events genereert in de afgelopen 3 dagen.

---

### Voorstellen (wacht op goedkeuring)

**1. CPC-monitoring H11 verscherpen**
- H11 CPC (link) is al 2 dagen op €1,40 gestabiliseerd, maar €0,10 onder de kill-grens. Bij een slechte dag overschrijdt het de drempel.
- Voorstel: dagelijkse check. Als CPC (link) > €1,45 op enig moment, direct pauzeren.

**2. Budget herverdeling via ad set spend limits**
- **2A:** Stel een minimum dagelijks spend in voor Kopie 2 (H12 ad set) van €20/dag. Momenteel krijgt deze ad set maar €14,32/dag gemiddeld.
- **2B:** Stel een maximum dagelijks spend in voor Kopie 1 (H11 ad set) van €50/dag. Momenteel slokt deze €73,53/dag op.
- Reden: H12 en H13 hebben betere efficiency metrics. Meer budget geeft ze de kans om ook checkout-events te genereren.

**3. H12 funnel-diagnose**
- H12 heeft 124 lifetime link clicks en 0 checkouts. Dat is statistisch onwaarschijnlijk als de LP goed werkt voor dit verkeer.
- Mogelijke oorzaken: audience mismatch, LP variatie die niet converteert, of tracking-issue op checkout-pagina voor H12-verkeer.
- Voorstel: review de UTM-parameters van H12 vs. H11 en check of hetzelfde checkout-pad wordt gevolgd.

**4. PostHog CTA tracking fixen**
- 0 CTA click events in PostHog over 4 dagen op een pagina met 538 pageviews. Dit is een tracking-defect.
- Voorstel: verify dat het `cta_click` event correct is geimplementeerd op de LP. Zonder deze metric missen we bounce rate context en CTA effectiviteit.

**5. ROAS-anomalie H13 verifieren**
- 2 purchases met waarde €42.773,50 (lifetime). Waarschijnlijk een grote B2B order.
- Voorstel: check in WooCommerce/backend of dit een echte order is en of de pixel-attributie klopt. Als deze order legitiem is via H13, is dat sterke validatie van die hook.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers (1/2A/2B/3/4/5).**
