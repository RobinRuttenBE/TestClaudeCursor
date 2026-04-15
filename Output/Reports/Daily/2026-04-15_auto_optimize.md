## Auto-Optimize Rapport — 2026-04-15

**Campagne:** 2026: SYBB | **Account:** act_567892422940728 | **Periode:** last 3d (12-14 apr)

---

### Automatische acties uitgevoerd

**Geen ads gepauzeerd. Alle 3 actieve ads presteren boven de kill-drempels.**

| Ad | Link CTR | Drempel | Impressions | CPC (link) | Drempel | Link Clicks | Resultaat |
|----|----------|---------|-------------|------------|---------|-------------|-----------|
| H11, B3, CTA5 | 0,98% | > 0,80% | 16.151 | €1,40 | < €1,50 | 158 (< 500) | PASS |
| H12, B3, CTA5 | 1,19% | > 0,80% | 3.096 | €1,16 | < €1,50 | 37 (< 500) | PASS |
| H13, B3, CTA5 | 1,17% | > 0,80% | 6.994 | €1,10 | < €1,50 | 82 (< 500) | PASS |

> CPC (link) kill-regel (> €1,50) niet toepasbaar: geen enkele ad heeft 500+ link clicks in de 3d-periode.

---

### Waarschuwingen

| Signaal | Drempel | H11 | H12 | H13 | Status |
|---------|---------|-----|-----|-----|--------|
| Creative fatigue (frequency) | > 3,5 | 1,59 | 1,77 | 1,39 | Geen risico |
| Dure reach (CPM) | > €15 | €13,66 | €13,88 | €12,87 | Geen risico |
| Dalende Link CTR (3d vs lifetime) | < 70% | 98,6% | 108,7% | 102,5% | Stabiel |

**Geen waarschuwingen.** Alle ads draaien binnen gezonde ranges. Frequencies zijn laag, CPM's onder de drempel, en Link CTR is stabiel tot verbeterend.

---

### Campagne Totalen (3d)

| Metric | Waarde |
|--------|--------|
| Spend | €376,47 |
| Impressions | 27.980 |
| Reach | 14.925 |
| Link Clicks | 291 |
| Link CTR | 1,04% |
| CPC (link) | €1,29 |
| All Clicks CTR | 2,03% |
| CPC (all) | €0,66 |
| CPM | €13,45 |
| Frequency | 1,87 |
| Landing Page Views | 239 |
| Add to Cart | 14 |
| Initiate Checkout | 7 |
| Complete Registration | 1 |
| Purchases (3d) | 0 |

---

### 70-20-10 Classificatie

> **Let op:** drempels zijn RICHTLIJNEN, niet hard. Oorspronkelijk gekalibreerd op all-clicks, nu toegepast op link metrics. Link CTR is structureel ~50-60% van all-clicks CTR.

**70% Core (ROAS > 2x of Link CTR > 1,5% + CPC link < €0,50):**
- **H13, B3, CTA5** (Kopie 3) — lifetime 2 purchases, €42.773,50 omzet, ROAS 290,6x
  - Link CTR 1,17% | CPC (link) €1,10 | Spend €90,03/3d | €147,19 lifetime
  - Kwalificeert op ROAS. De anomaal hoge ROAS (2 grote B2B orders) maakt dit metric onbetrouwbaar als bewijs van consistente performance. Toch de enige ad met echte revenue.

**20% Emerging (Link CTR 0,8-1,5%):**
- **H12, B3, CTA5** (Kopie 2) — Link CTR 1,19%, CPC (link) €1,16
  - Beste Link CTR van alle ads. Laagste CPC (link). 0 purchases, 0 initiate checkout.
  - Potentieel sterk, maar geen funnel conversies. Mogelijk LP-mismatch.
- **H11, B3, CTA5** (Kopie 1) — Link CTR 0,98%, CPC (link) €1,40
  - Laagste Link CTR, hoogste CPC (link). Maar: 13 initiate_checkout lifetime, 1 add_payment_info, 0 purchases.
  - Sterk mid-funnel signaal, maar checkout flow is kapot.

**10% Experimental:**
- Geen ads in deze categorie (alle > 3.000 impressions).

---

### Budget Verdeling (3d)

| Ad | Ad Set | Spend 3d | % van totaal | Classificatie |
|----|--------|----------|-------------|---------------|
| H11, B3, CTA5 | Kopie 1 | €220,61 | 62,4% | Emerging |
| H13, B3, CTA5 | Kopie 3 | €90,03 | 25,5% | Core |
| H12, B3, CTA5 | Kopie 2 | €42,96 | 12,2% | Emerging |
| Overig (gepauzeerde ads) | — | €22,87 | — | — |

**Budget mismatch: JA, en het wordt erger.**

- H11 (Emerging, 0 purchases) krijgt **62,4%** van het budget (was 45% op 14 apr)
- H13 (Core, enige ad met purchases) krijgt slechts **25,5%**
- H12 (Emerging, beste Link CTR) krijgt maar **12,2%**
- Meta's CBO stuurt budget naar H11 vanwege mid-funnel signalen (13 IC) maar de checkout converteert niet

---

### Funnel Analyse per Ad (Lifetime)

| Stap | H11 | H12 | H13 |
|------|-----|-----|-----|
| Impressions | 23.890 | 11.372 | 12.408 |
| Link Clicks | 237 | 125 | 142 |
| Landing Page Views | 181 | 102 | 122 |
| View Content | 23 | 9 | 13 |
| Add to Cart | 13 | 4 | 6 |
| Initiate Checkout | 13 | 0 | 2 |
| Add Payment Info | 1 | 0 | 1 |
| Complete Registration | 1 | 0 | 1 |
| **Purchase** | **0** | **0** | **2 (€42.773,50)** |
| **Spend** | **€313,04** | **€106,01** | **€147,19** |

**Opvallend bij H11:** 13 initiate_checkout maar 0 purchases. Er zit een blokkade tussen checkout starten en afronden. Dit is een conversie-lek dat direct onderzocht moet worden (payment gateway, form errors, redirect issues).

**Opvallend bij H12:** Beste CTR en laagste CPC, maar 0 initiate_checkout bij 4 add_to_cart. Verkeer is geinteresseerd maar converteert niet. Mogelijke LP-mismatch of audience die browst maar niet koopt.

---

### Voorstellen (wacht op goedkeuring)

**1. Pauzeer Ad Set Kopie 1 (H11) om budget te forceren naar H13/H12**
- H11 heeft €313 lifetime uitgegeven met 0 purchases
- De 13 initiate_checkout misleiden Meta's CBO om steeds meer budget naar H11 te sturen
- Door Kopie 1 te pauzeren gaat het budget automatisch naar Kopie 2 (H12) en Kopie 3 (H13)
- Verwachte impact: H13 (enige ad met revenue) krijgt 2-3x meer budget

**2. Checkout flow diagnose uitvoeren**
- H11: 13 initiate_checkout, 1 add_payment_info, 0 purchases. Iets blokkeert de afronding.
- Check in Wix: zijn er payment gateway errors? Form validatie problemen? Redirect loops?
- Check PostHog session recordings van users die IC triggeren maar niet afronden
- Dit is potentieel €313+ aan verloren conversies

**3. Nieuwe hook variaties op H13 (de winnaar)**
- H13 is de enige ad met purchases. Op basis van Hormozi 70-20-10: maak variaties op de winnende hook.
- Variatie A: Zelfde H13 hook, ander videoformat (testimonial ipv educatief)
- Variatie B: Zelfde H13 hook, andere CTA (urgentie ipv value)
- Variatie C: H13 hook + H12 body combo (beste CTR hook + bewezen conversiepath)

**4. ROAS verificatie (herhaling van gisteren)**
- H13's 2 purchases (€42.773,50) zijn waarschijnlijk 1-2 grote B2B wholesale orders
- Verifieer in Wix order dashboard of dit echte, afgeronde orders zijn
- Als bevestigd: dit is het bewijs dat H13's audience het dichtst bij koopintentie zit

**5. Audience optimalisatie**
- Geen directe actie nodig: frequency < 2,0 op alle ads, geen audience saturatie
- Bij budget shift naar H13/H12 zal frequency mogelijk stijgen. Monitor dagelijks.

---

### Trend vs Gisteren (14 apr)

| Metric | 14 apr | 15 apr | Trend |
|--------|--------|--------|-------|
| Actieve ads | 4 (H11-H14) | 3 (H11-H13) | H14 gepauzeerd |
| H11 budget share | 45% | 62,4% | Stijgend (probleem) |
| H13 budget share | ~25% | 25,5% | Stabiel (te laag) |
| Campagne Link CTR | 1,0% | 1,04% | Stabiel |
| Campagne CPC (link) | €1,14 | €1,29 | Stijgend |

**CPC (link) stijgt** van €1,14 naar €1,29. Dit komt doordat H11 (duurste ad) nu een groter deel van het budget pakt na het wegvallen van H14.

---

### Aanbevolen prioriteit

1. **NU:** Pauzeer Ad Set Kopie 1 (H11) om budget mismatch te corrigeren
2. **VANDAAG:** Checkout flow diagnose (het conversie-lek bij H11 kost mogelijk ook H13/H12)
3. **DEZE WEEK:** Nieuwe H13 variaties lanceren
4. **MONITOR:** CPC (link) trend. Als het boven €1,50 campagne-gemiddeld komt, is er een structureel probleem.

---

*Rapport gegenereerd: 2026-04-15 | Data: Meta Ads MCP (Pipeboard) | Alleen LINK metrics gebruikt voor kill-rules*

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
