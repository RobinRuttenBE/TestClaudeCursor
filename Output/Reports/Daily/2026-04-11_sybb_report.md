# SYBB Daily Report - 11 april 2026

## 1. Samenvatting

Uitzonderlijk hoge spend dag (€137.76, 3x het 7-daags gemiddelde) met sterke traffic naar de LP (242 pageviews, 176 unieke bezoekers). De bounce rate blijft echter kritiek hoog op 84.7%, consistent met het weekgemiddelde. Positief: 2 purchases gerealiseerd en 25 /booking bezoeken. Grootste zorg: H15 trekt veel clicks (hoogste CTR 2.41%) maar heeft een bounce rate van 97%, wat een ernstige ad-pagina mismatch aantoont.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €137.76 | €46.42 | ↑ |
| Impressions | 14,466 | 5,462 | ↑ |
| Clicks | 284 | 112 | ↑ |
| Link Clicks | 157 | 60 | ↑ |
| CTR | 1.96% | 2.06% | → |
| CPC | €0.49 | €0.41 | ↑ |
| LP Views | 123 | 44 | ↑ |
| Frequency | 1.63 | 1.75 | → |
| Purchases | 2 | 0.3 | ↑ |

**Opmerking spend:** De spend van €137.76 is fors boven het dagelijkse 7d gemiddelde van €46.42. Dit wijst op ofwel budget-wijzigingen, ofwel Facebook's algoritme dat een "goede dag" detecteerde en meer budget alloceerde via campaign budget optimization.

### Ad Variant Performance

| Ad (utm_content) | Link Clicks | CTR | CPC | LP Bounce | LP Sessions |
|-------------------|-------------|-----|-----|-----------|-------------|
| h12_b3_cta5 | 55 | 2.04% | €0.38 | 84.6% | 52 |
| h13_b3_cta5 | 40 | 1.77% | €0.64 | 78.4% | 37 |
| h11_b3_cta5 | 26 | 2.01% | €0.54 | 83.8% | 37 |
| h15_b3_cta5 | 26 | 2.41% | €0.40 | 97.0% | 33 |
| h14_b3_cta5 | 10 | 1.38% | €0.65 | 72.7% | 11 |

**Beste variant:** H13 (h13_b3_cta5). Combineert acceptabele bounce (78.4%), 2 purchases, en de meeste conversieacties (add to cart, checkout, purchase). Ondanks een hogere CPC (€0.64) levert deze ad het beste eindresultaat.

**Slechtste variant:** H15 (h15_b3_cta5). Heeft de hoogste CTR (2.41%) maar een vernietigende bounce rate van 97%. Slechts 1 van de 33 sessies ging verder dan de landingspagina. Klassieke ad-pagina mismatch: de hook trekt de verkeerde mensen, of belooft iets dat de LP niet levert.

**Runner-up concern:** H14 (h14_b3_cta5). Facebook geeft deze ad minimale delivery (€11.67 spend, laagste CTR 1.38%). Ironisch genoeg heeft H14 de laagste bounce rate (72.7%), wat suggereert dat de mensen die WEL klikken meer gekwalificeerd zijn.

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | 84.7% | 84.8% | <55% | 🔴 |
| Avg Session Duration (engaged) | 140.5s | 140.4s | >90s | 🟢 |
| Median Session Duration | 13.5s | - | >90s | 🔴 |
| Scroll Depth | n.v.t. | n.v.t. | >60% | ⚪ |
| CTA Click Rate (→ /booking) | 13.2% | 11.5% | >4% | 🟢 |
| /booking Visits | 25 | 9.6 | meten | ↑ |

**Kanttekening sessieduur:** De 140.5s geldt alleen voor de 15% bezoekers die NIET bouncen. De mediane sessieduur van 13.5s is representatiever voor het totaal. Dit bevestigt dat de meeste bezoekers binnen enkele seconden afhaken.

**Scroll depth:** Geen scroll tracking geinstalleerd. Dit is een blinde vlek in de analyse. Aanbeveling: implementeer scroll depth events (25/50/75/100%) in PostHog.

## 4. Funnel Drop-off

```
LP Sessies (190) ─── 100%
    │
    ├── BOUNCE (161) ──── 84.7% verliest hier
    │
    ▼
Engaged (29) ──────── 15.3%
    │
    ▼
/booking (25) ─────── 13.2%
    │
    ▼
Checkout (18) ─────── 9.5%
    │
    ▼
Purchase (2) ──────── 1.1%
```

**Grootste lek:** De eerste seconden op de LP. 84.7% van alle bezoekers bounced direct. De above-the-fold content (hero sectie) faalt om bezoekers vast te houden. Wie WEL voorbij de bounce komt, converteert opvallend goed: 25/29 engaged sessies gaan naar /booking (86%).

## 5. Cross-Reference Analyse

### Ad CTR vs LP Bounce (mismatch indicator)

| Variant | Meta CTR | LP Bounce | Mismatch Score |
|---------|----------|-----------|----------------|
| H15 | 2.41% (hoogste) | 97.0% (hoogste) | KRITIEK |
| H12 | 2.04% | 84.6% | Hoog |
| H11 | 2.01% | 83.8% | Hoog |
| H13 | 1.77% | 78.4% | Gemiddeld |
| H14 | 1.38% (laagste) | 72.7% (laagste) | Laag |

**Patroon:** Er is een duidelijke negatieve correlatie. Hoe hoger de CTR, hoe hoger de bounce. Dit wijst op hooks die curiosity opwekken maar niet matchen met wat de LP biedt. De ads "overpromisen" of trekken een breed maar ongekwalificeerd publiek.

### Frequentie vs Bounce
Frequency (1.63) is nog gezond en niet gecorreleerd met bounce stijging. Ad fatigue is nog geen probleem.

### CPC vs Conversie
H12 heeft de laagste CPC (€0.38) en levert volume, maar geen directe purchases. H13 heeft een hogere CPC (€0.64) maar is de enige variant met purchases gisteren. Duurdere clicks ≠ slechtere ROI.

## 6. Rode Vlaggen 🚩

1. **Bounce rate 84.7% (target: <55%)** - Al 7+ dagen consistent boven 80%. Dit is het #1 probleem in de gehele funnel. Elke dag verliezen we 85% van betaald verkeer in de eerste seconden.

2. **H15 bounce rate 97%** - Slechts 1 op 33 sessies gaat verder. Bij €19.19 spend is dit €19.19 verspild aan verkeer dat instant afhaakt.

3. **CPC ↑19% vs 7d gemiddelde** - CPC gestegen van €0.41 naar €0.49. Nog net onder de €0.50 target, maar trending verkeerd.

4. **Spend spike 3x normaal** - €137.76 vs €46.42 gemiddeld. Als dit niet bewust is (budget verhoging), check of CBO correct is ingesteld.

5. **Geen scroll depth tracking** - Zonder deze data is het onmogelijk te bepalen waar op de pagina bezoekers afhaken.

## 7. Top 3 Acties voor Vandaag

### 1. Pauzeer of herwerk H15 (h15_b3_cta5)
- **Wat:** Pauzeer ad variant H15 of pas de hook aan om beter te matchen met LP content
- **Waarom:** 97% bounce rate = de hook creert verwachtingen die de LP niet waarmaakt
- **Hoe:** Meta Ads Manager → Ad level → H15 pauzeren. Of: analyseer wat H15 belooft vs wat de LP biedt en align de messaging
- **Verwachte impact:** Bespaart ~€19/dag aan verspild verkeer, verbetert overall bounce rate met ~2-3 procentpunt
- **Escalatie:** Geel (Robin goedkeuring)

### 2. Onderzoek LP hero sectie (above the fold)
- **Wat:** Analyseer de eerste 3 seconden van de LP ervaring. Wat zien bezoekers? Matcht het met de ad hooks?
- **Waarom:** 84.7% bounced = de hero faalt om aandacht vast te houden. Maar 86% van engaged bezoekers gaat naar /booking, dus de rest van de pagina werkt WEL
- **Hoe:** Check session recordings in PostHog. Vergelijk hero headline met de top-performing ad hooks. Test een hero die direct de waardepropositie toont
- **Verwachte impact:** Als bounce daalt naar 70% → +28 extra engaged sessies/dag → ~+20 booking bezoeken/dag
- **Escalatie:** Oranje (Wix Editor)

### 3. Implementeer scroll depth tracking
- **Wat:** Voeg scroll depth events toe (25%, 50%, 75%, 100%) aan PostHog tracking
- **Waarom:** Zonder scroll data is het gissen waar precies op de pagina bezoekers afhaken. Dit blokkeert gerichte LP optimalisatie
- **Hoe:** Voeg een JavaScript snippet toe aan de Wix site die scroll percentages trackt en naar PostHog stuurt als custom events
- **Verwachte impact:** Geen directe conversie impact, maar maakt data-gedreven LP optimalisatie mogelijk
- **Escalatie:** Groen (auto-implementeerbaar)

---

## Data Bronnen
- **Meta Ads:** Pipeboard MCP, campaign "2026: SYBB" (ID: 120239435987290239), account act_567892422940728
- **PostHog:** Project 149694, host www.startyourballoonbusiness.com
- **Periode:** 11 april 2026 (gisteren), 7d referentie: 5-11 april 2026
- **Rapport gegenereerd:** 12 april 2026
