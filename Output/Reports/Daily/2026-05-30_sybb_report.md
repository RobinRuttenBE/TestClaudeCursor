# SYBB Daily Report — 30 May 2026

## 1. Samenvatting
De campagne `2026: SYBB` draait stabiel: €47,13 spend, 142 clicks, CTR 1,69% en CPC €0,33 (ruim onder de €0,50 target), met 3 purchases en een ROAS van 4,12x. Alle kerncijfers liggen binnen 10% van het 7d gemiddelde, dus geen schokken. Belangrijke kanttekening: de PostHog landing page data kon vandaag niet opgehaald worden (query engine gaf op alle analytische calls een error), dus de Landing Page Health en scroll/CTA cijfers ontbreken. De funnel hieronder is daarom opgebouwd uit Meta's eigen signalen.

## 2. Meta Ads Performance
Campagne: `2026: SYBB` (ID 120214244887790182, ACTIVE, objective OUTCOME_SALES). 7d gemiddelde = daggemiddelde over 23 t/m 29 mei.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €47,13 | €45,12 | → |
| Impressions | 8.421 | 8.301 | → |
| Clicks | 142 | 146 | → |
| CTR | 1,69% | 1,76% | → |
| CPC | €0,33 | €0,31 | → |
| Frequency | 1,22 | 1,39 (7d cumulatief) | → |
| Purchases | 3 | 3,4 | → |
| ROAS | 4,12x | 4,55x | → |

Frequency van 1,22 op dagniveau is gezond en ver onder de fatigue grens van 3,0.

### Ad Variant Performance
LP Bounce en LP Scroll kolommen zijn leeg: PostHog data was niet beschikbaar (zie sectie 3). Purchases per variant toegevoegd als vervangend conversiesignaal.

| Ad (utm_content) | Clicks | CTR | CPC | LPV | Purchases | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----|-----------|-----------|----------------|
| h11_b3_cta5 | 31 | 1,83% | €0,30 | 27 | 1 | n/b | n/b |
| h12_b3_cta5 | 33 | 2,06% | €0,30 | 29 | 1 | n/b | n/b |
| h13_b3_cta5 | 26 | 1,50% | €0,37 | 22 | 0 | n/b | n/b |
| h14_b3_cta5 | 19 | 1,05% | €0,49 | 15 | 0 | n/b | n/b |
| h15_b3_cta5 | 33 | 1,85% | €0,28 | 28 | 0 | n/b | n/b |

n/b = niet beschikbaar (PostHog query error)

**Beste variant:** h12_b3_cta5. Hoogste CTR (2,06%), lage CPC (€0,30), 29 landing page views en een purchase. h15_b3_cta5 is de kostenefficiëntste (laagste CPC €0,28, 33 clicks) en verdient meer budget.

**Slechtste variant:** h14_b3_cta5. Laagste CTR (1,05%, bijna de helft van h12) en hoogste CPC (€0,49), dicht tegen de €0,50 ceiling. Slechts 15 LPV en geen conversies. Kandidaat om te pauzeren of de hook te vervangen.

## 3. Landing Page Health
> **PostHog data niet beschikbaar.** Op 30 mei gaven alle analytische PostHog calls (query-trends, execute-sql en property values) consistent de fout "Failed to query insight: An unexpected error occurred." Alleen de statische event-schema lijst kwam door. Dit wijst op een tijdelijke storing aan PostHog's query backend, niet op een tracking-fout aan onze kant. De onderstaande tabel kon daardoor niet gevuld worden.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n/b | n/b | <55% | ⚪ geen data |
| Avg Session Duration | n/b | n/b | >90s | ⚪ geen data |
| Scroll 25% | n/b | n/b | >80% | ⚪ geen data |
| Scroll 50% | n/b | n/b | >60% | ⚪ geen data |
| Scroll 75% | n/b | n/b | >40% | ⚪ geen data |
| Scroll 100% | n/b | n/b | >20% | ⚪ geen data |
| CTA Click Rate | n/b | n/b | >4% | ⚪ geen data |

**Actie:** morgen opnieuw ophalen. Als PostHog dan nog steeds geen data geeft, controleren of het Meta verkeer (utm_source=meta) überhaupt binnenkomt in project "Default project". Meta meldt 118 landing page views voor gisteren, dus het verkeer landt wel; het probleem zit bij PostHog's rapportage.

## 4. Funnel Drop-off
Opgebouwd uit Meta signalen (PostHog scroll/CTA stappen ontbreken).

Link clicks (129) → Landing page views (118, 91%) → Initiated checkout (8, 6,2%) → Purchase (3, 2,3%)

- Click → LPV: 91% (slechts 9% verlies, gezond. Pagina laadt en houdt mensen vast)
- LPV → Initiated checkout: 6,8% (118 naar 8)
- Checkout → Purchase: 37,5% (8 naar 3, sterke afsluiting)

**Grootste lek:** LPV → Initiated checkout. Van de 118 mensen die de pagina bereiken starten er maar 8 een checkout. Dit is precies de stap waar PostHog's scroll depth en CTA click data het "waarom" zouden verklaren (lezen ze tot de prijs? klikken ze de CTA?). Die data missen we vandaag, dus dit is morgen prioriteit nummer 1 om te onderzoeken.

## 5. Rode Vlaggen 🚩
- **h14_b3_cta5: CPC €0,49 en CTR 1,05%.** Bijna de €0,50 ceiling, laagste CTR van alle varianten, geen conversies. De hook trekt niet.
- **PostHog data gat.** Geen landing page health voor 30 mei. Beslissingen over LP optimalisatie staan on hold tot de data terug is.
- Geen frequency, bounce of CPC-spike alarmen verder: campagne draait binnen alle Meta targets.

## 6. Top 3 Acties voor Vandaag
1. **PostHog data herstellen en LPV → checkout lek onderzoeken.** Wat: morgen het rapport opnieuw draaien en, zodra PostHog werkt, scroll depth en CTA click rate per utm_content checken. Waarom: de funnel verliest 93% tussen landing en checkout (118 naar 8) en we zien nu niet of dat aan scroll, CTA of prijs ligt. Verwachte impact: dit is de grootste hefboom op conversie. Escalatie: Geel (Robin, want mogelijk LP aanpassing nodig).
2. **h14_b3_cta5 pauzeren of hook vervangen.** Wat: variant uitzetten en budget herverdelen naar h12 en h15. Waarom: CPC €0,49 bij CTR 1,05% en 0 conversies, terwijl h15 op €0,28 zit. Verwachte impact: lagere gemiddelde CPC en meer clicks voor hetzelfde budget. Escalatie: Geel (Meta Ads Manager).
3. **Budget verschuiven naar h12 en h15.** Wat: meer spend naar de twee best presterende varianten (hoogste CTR en laagste CPC). Waarom: 70-20-10 regel, dubbel inzetten op bewezen winnaars. Verwachte impact: hogere campagne-CTR en meer landing page views per euro. Escalatie: Geel (Meta Ads Manager).

---
*Databronnen: Meta Ads MCP (Pipeboard), campagne `2026: SYBB`. PostHog MCP (project "Default project") gaf op 30 mei een query engine error; landing page data ontbreekt in dit rapport.*
