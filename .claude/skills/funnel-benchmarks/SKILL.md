---
name: Funnel Benchmarks
description: Standaard funnel benchmarks voor alle Sempertex Europe marketing commands. Bevat drempelwaarden per funnel stap met diagnose-richtlijnen.
---

# Funnel Benchmarks — Sempertex Europe

Deze benchmarks worden gebruikt door alle commands die funnel performance analyseren (o.a. /funnel-diagnose, /ads-optimize, /ads-report).

---

## 1. Ad → Click (CTR — Click-Through Rate)

**Berekening:** clicks / impressions × 100

| Rating    | Drempel | Kleur  |
|-----------|---------|--------|
| Slecht    | < 1%    | Rood   |
| Goed      | 1–3%   | Oranje |
| Excellent | > 3%    | Groen  |

**Diagnose bij slecht:**
Bottleneck is de ad creative. De hook pakt niet.
- Test nieuwe hooks (zie `100m-hooks-playbook.md`)
- 70-20-10 regel: 70% bewezen hooks, 20% variaties, 10% experimenten
- Check of de thumbnail/visual aandacht trekt in de feed
- Vergelijk met best performers uit dezelfde campagne

---

## 2. Click → Landing Page (Drop-off Rate)

**Berekening:** LP visitors / clicks × 100

| Rating           | Drempel | Kleur  |
|------------------|---------|--------|
| Technisch probleem | < 85%   | Rood   |
| Normaal          | ≥ 85%  | Groen  |

**Diagnose bij slecht:**
Mensen klikken maar komen niet aan op de landing page.
- Check pagina laadsnelheid (vooral mobiel)
- Controleer redirect/URL issues
- Test mobile compatibility
- Controleer of de link in de ad correct is
- Check of cookie consent de pagina blokkeert

---

## 3. Landing Page → Booking/Opt-in (LP Conversion Rate)

**Berekening:** booking clicks / LP visitors × 100

| Rating    | Drempel | Kleur  |
|-----------|---------|--------|
| Slecht    | < 3%    | Rood   |
| Goed      | 3–8%   | Oranje |
| Excellent | > 8%    | Groen  |

**Diagnose bij slecht:**
Mensen komen op de pagina maar klikken niet door. Bottleneck = landing page.
- Headline matcht niet met ad (message match)
- Geen social proof (testimonials, reviews, data)
- Geen urgentie (limited spots, deadline)
- Onduidelijke CTA (te veel opties, te vaag)
- Prijsshock (prijs te vroeg of onverwacht zichtbaar)
- Te weinig info over wat ze krijgen
- Risk reversal ontbreekt (money back guarantee, clear expectations)

---

## 4. Booking → Add to Cart (Intent Rate)

**Berekening:** add to cart / booking clicks × 100

| Rating    | Drempel | Kleur  |
|-----------|---------|--------|
| Slecht    | < 30%   | Rood   |
| Goed      | 30–60% | Oranje |
| Excellent | > 60%   | Groen  |

**Diagnose bij slecht:**
Mensen bekijken het aanbod maar haken af.
- Onverwachte kosten (shipping, BTW, fees)
- Te veel stappen in het proces
- Geen trust signals (logo, reviews, SSL, bekende betaalmethodes)
- Prijs-waarde verhouding onduidelijk
- Geen urgentie na de click

---

## 5. Add to Cart → Purchase (Checkout Conversion)

**Berekening:** purchases / add to cart × 100

| Rating    | Drempel | Kleur  |
|-----------|---------|--------|
| Slecht    | < 40%   | Rood   |
| Goed      | 40–70% | Oranje |
| Excellent | > 70%   | Groen  |

**Diagnose bij slecht:**
Mensen willen kopen maar voltooien het niet.
- Te weinig betaalopties
- Onverwachte shipping kosten
- Technische errors in checkout
- Te veel formuliervelden
- Geen guest checkout optie
- Pagina voelt niet veilig

---

## 6. Overall ROAS (Return on Ad Spend)

**Berekening:** (purchases × gemiddelde orderwaarde) / ad spend

| Rating          | Drempel | Kleur  |
|-----------------|---------|--------|
| Niet winstgevend | < 2×   | Rood   |
| Goed            | 2–4×   | Oranje |
| Excellent       | > 4×    | Groen  |

**Context:**
- Nozzle Up ads: 3.2× ROAS in testfase (benchmark voor STX EU)
- ROAS alleen is niet genoeg — kijk ook naar absolute winst en lifetime value
- Zie `100m-lifetime-value-playbook.md` voor LTV perspectief

---

## SYBB Historische Referentiedata (Dag 1-3 learnings)

Uit de eerste live test van SYBB Ad Set 1, Batch 2:

- **Dag 1:** Veel page views, bijna niemand gaat door na opt-in. Funnel niet ideaal — te weinig info over het event. Landing page aangepast met booking sectie en meer info.
- **Dag 2:** CTR op ad fenomenaal, CPC goed. Van LP bezoekers gaat ~1% naar booking page. ~40% klikt op een product. Bijna niemand gaat door checkout. Vermoedelijk prijsshock. LP miste: proof, urgentie, risk reversing, ad-match.
- **Dag 3:** Veel minder page views (zondag). Ads presteren goed maar LP converteert niet. Ads gepauzeerd. Frankrijk uit targeting. Herstart met nieuwe LP.

**Key takeaway:** Bij SYBB zat de bottleneck bij LP → Booking (< 1% conversie). De ad creatives werkten, de landing page niet.
