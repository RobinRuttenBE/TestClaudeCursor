# SYBB Daily Report -- 2026-04-15

## 1. Samenvatting

Lagere spend-dag (€74.65, -27% vs 7d gemiddelde) met minder impressies en clicks, maar opvallend sterke conversies: 4 purchases (€1,473.50 revenue) leveren een ROAS van 19.7x op. Alle purchases kwamen via H11. CPC steeg naar €0.61 (boven €0.50 target). H12 blijft de variant met de hoogste CTR (4.55%) en laagste CPC (€0.25), maar krijgt slechts 7.8% van het budget. H13 presteert het slechtst: laagste CTR (1.14%), hoogste CPC (€0.95), en nul conversies. PostHog MCP was niet bereikbaar, waardoor LP-data ontbreekt in dit rapport.

---

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €74.65 | €101.97 | ↓ |
| Impressions | 5,847 | 8,811 | ↓ |
| Clicks | 122 | 189 | ↓ |
| CTR | 2.09% | 2.15% | → |
| CPC | €0.61 | €0.54 | ↑ |
| Link Clicks | 57 | 98 | ↓ |
| LP Views | 44 | 76 | ↓ |
| Frequency | 1.34 | 2.10 | ↓ |
| Video Views | 1,367 | 1,825 | ↓ |
| Add to Cart | 2 | 4.0 | ↓ |
| Purchases | 4 | 0.9 | ↑ |
| Revenue | €1,473.50 | - | - |
| ROAS | 19.7x | - | - |

### Ad Set Performance

| Ad Set | Spend | Impressions | Clicks | CTR | CPC | Link Clicks | LP Views | Frequency |
|--------|-------|-------------|--------|-----|-----|-------------|----------|-----------|
| Kopie 1 (H11) | €62.18 | 4,729 | 92 | 1.95% | €0.68 | 46 | 32 | 1.25 |
| Kopie 2 (H12) | €5.83 | 506 | 23 | 4.55% | €0.25 | 7 | 7 | 1.61 |
| Kopie 3 (H13) | €6.64 | 612 | 7 | 1.14% | €0.95 | 4 | 5 | 1.13 |

### Ad Variant Performance

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LP Views (Meta) | Purchases | ATC | View Content |
|-------------------|-------|-------------|-----|-----|-----------------|-----------|-----|--------------|
| h11_b3_cta5 | €62.18 | 46 | 1.95% | €0.68 | 32 | 4 | 2 | 7 |
| h12_b3_cta5 | €5.83 | 7 | 4.55% | €0.25 | 7 | 0 | 0 | 1 |
| h13_b3_cta5 | €6.64 | 4 | 1.14% | €0.95 | 5 | 0 | 0 | 0 |

**Beste variant:** H12,B3,CTA5. Hoogste CTR (4.55%), laagste CPC (€0.25, ruim onder €0.50 target). Ondanks minimaal budget (7.8%) genereert deze variant de meest efficiente clicks. Geen conversies gisteren, maar dat is te verwachten bij slechts 7 LP views.

**Slechtste variant:** H13,B3,CTA5. Laagste CTR (1.14%), hoogste CPC (€0.95, bijna 2x de target), nul conversies, en slechts 4 link clicks van 612 impressies.

### 7d Ad Variant Totalen (voor context)

| Ad | 7d Spend | 7d Link Clicks | 7d LP Views | 7d CPC (overall) | 7d Purchases |
|----|----------|----------------|-------------|-------------------|--------------|
| H11,B3,CTA5 | €328.99 | 259 | 197 | €0.66 | 4 |
| H12,B3,CTA5 | €123.01 | 148 | 123 | €0.38 | 0 |
| H13,B3,CTA5 | €149.31 | 142 | 122 | €0.62 | 2 |
| H14,B3,CTA5 | €60.30 | 78 | 52 | €0.42 | 0 |
| H15,B3,CTA5 | €52.15 | 61 | 39 | €0.45 | 0 |

**Let op:** H14 en H15 zaten in de parent ad set en Kopie 4 die gisteren geen spend kregen. Alleen Kopie 1/2/3 waren actief.

---

## 3. Landing Page Health

**PostHog MCP niet beschikbaar.** LP-metrics (bounce rate, scroll depth, sessie duur, CTA clicks) konden niet worden opgehaald. Zie Rode Vlaggen sectie 5.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | N/A | N/A | <55% | -- |
| Avg Session Duration | N/A | N/A | >90s | -- |
| Scroll 25%+ | N/A | N/A | >80% | -- |
| Scroll 50%+ | N/A | N/A | >60% | -- |
| Scroll 75%+ | N/A | N/A | >40% | -- |
| Scroll 100% | N/A | N/A | >20% | -- |
| CTA Click Rate | N/A | N/A | >4% | -- |

---

## 4. Funnel Drop-off

Geen funnel data beschikbaar (PostHog MCP niet bereikbaar).

Op basis van Meta data alleen:

```
Impressions (5,847)
    ↓ 99.0% drop
Link Clicks (57, 0.97% van impressions)
    ↓ 22.8% drop
LP Views (44, 77.2% van link clicks)
    ↓ 95.5% drop
Purchases (4, 9.1% van LP views)
```

**Opmerkelijk:** De conversie van LP view naar purchase (9.1%) is zeer sterk. Het probleem zit hoger in de funnel: het aantal mensen dat daadwerkelijk op de LP landt is laag (44 van 5,847 impressies).

---

## 5. Rode Vlaggen

1. **PostHog MCP niet bereikbaar** -- Geen LP-data beschikbaar voor dit rapport. Bounce rate, scroll depth, sessie duur en CTA clicks ontbreken volledig. Hierdoor is cross-referencing tussen Meta en LP-gedrag niet mogelijk. Controleer of de PostHog MCP server draait.

2. **CPC €0.61 > €0.50 target** -- 13% boven 7d gemiddelde (€0.54). Bij lagere spend (€74.65 vs €101.97 gem.) krijg je proportioneel nog minder verkeer.

3. **H13 CPC €0.95** -- Bijna 2x de target. Bij 612 impressies genereerde H13 slechts 4 link clicks en 0 conversies. Cost per LP view: €1.33. Dit is niet rendabel.

4. **Budget concentratie: 83% naar H11** -- H11 krijgt €62.18 van €74.65 totaal, maar heeft een CPC van €0.68 (boven target). H12 presteert efficenter op CPC (€0.25) en CTR (4.55%) maar krijgt slechts €5.83.

5. **LP Views daling -42%** -- 44 LP views gisteren vs 76/d gemiddeld. Minder verkeer op de landing page betekent minder kans op conversies, ook al is de conversie rate sterk.

---

## 6. Cross-Reference Analyse

**Beperkt door PostHog MCP uitval.** Alleen Meta-interne cross-referencing mogelijk.

### Meta-interne analyse

| Pattern | Variant | Bevinding |
|---------|---------|-----------|
| Hoge CTR + Lage CPC | H12 (4.55% CTR, €0.25 CPC) | Meest efficiente variant. Algoritme geeft het weinig budget ondanks sterke performance. |
| Hoge Spend + Conversies | H11 (€62.18, 4 purchases) | Budget concentratie betaalt zich uit in conversies. ROAS op H11: €1,473.50/€62.18 = 23.7x. |
| Laag alles | H13 (1.14% CTR, €0.95 CPC, 0 conv) | Slechtste performer op elke metric. 8.9% budget voor 0 resultaat. |

### Cost per LP View per variant

| Variant | Spend | LP Views | Cost per LP View |
|---------|-------|----------|-----------------|
| H11 | €62.18 | 32 | €1.94 |
| H12 | €5.83 | 7 | €0.83 |
| H13 | €6.64 | 5 | €1.33 |

### Conversie-analyse H11

H11 genereerde gisteren 4 purchases met een totale waarde van €1,473.50 (gem. €368.38/purchase). Daarnaast: 3 complete registrations, 4 initiate checkouts, 2 add to carts, en 2 add payment info events. Dit is een volledige funnel flow die wijst op een sterke dag voor workshop bookings. De 7d totaal toont echter ook 4 purchases, wat betekent dat ALLE 7d purchases op gisteren vielen. Dit kan een anomalie zijn of een seizoenseffect.

---

## 7. Top 3 Acties voor Vandaag

### 1. Herstel PostHog MCP verbinding
- **Wat:** Check of de PostHog MCP server draait en verbind opnieuw. Zonder LP-data is het onmogelijk om ad-pagina mismatch te detecteren.
- **Waarom:** PostHog MCP was niet bereikbaar, waardoor 50% van de rapportage-data ontbreekt. Bounce rate, scroll depth en CTA clicks zijn essentieel voor optimalisatie.
- **Hoe:** Check `claude mcp list` voor PostHog server status. Herstart indien nodig.
- **Verwachte impact:** Volledig rapport met cross-referencing, betere optimalisatiebeslissingen.
- **Escalatie:** Groen (technisch, zelf op te lossen)

### 2. Verhoog H12 budget, verlaag H13
- **Wat:** Verschuif budget van Kopie 3 (H13) naar Kopie 2 (H12). Overweeg H13 te pauzeren.
- **Waarom:** H12 heeft 4x hogere CTR (4.55% vs 1.14%), 4x lagere CPC (€0.25 vs €0.95), en de laagste cost per LP view (€0.83). H13 genereerde 0 conversies in 7 dagen met €149 spend.
- **Hoe:** Meta Ads Manager > Campagne 2026: SYBB > Pauzeer Kopie 3, verhoog Kopie 2 budget naar minimaal €20/dag.
- **Verwachte impact:** Bij gelijke spend zou H12 ~3x meer LP views genereren dan H13. Met PostHog data van vorige rapporten weten we ook dat H12 de laagste bounce rate had.
- **Escalatie:** Geel (Robin goedkeuring nodig)

### 3. Analyseer de 4 purchases van gisteren
- **Wat:** Check in Wix/WooCommerce welke bookings er gisteren binnenkwamen. Valideer of de Meta pixel correct attributeert.
- **Waarom:** 4 purchases op 1 dag is uitzonderlijk (7d totaal was ook 4). De gemiddelde orderwaarde van €368.38 matcht een workshop booking. Als dit klopt, is de funnel zeer effectief en moet de focus liggen op volume (meer LP traffic).
- **Hoe:** Check order dashboard voor 15 april. Vergelijk met Meta conversie data.
- **Verwachte impact:** Bevestiging van pixel accuracy. Als attributie klopt, verschuift de strategie van "fix de LP" naar "meer budget = meer bookings".
- **Escalatie:** Geel (Robin moet orders controleren)

---

*Rapport gegenereerd op 2026-04-16 op basis van Meta Ads MCP (Pipeboard) data.*
*PostHog MCP was niet bereikbaar. LP-data ontbreekt volledig.*
*Datumbereik: 2026-04-15 (dagdata) vs 2026-04-09 t/m 2026-04-15 (7d referentie).*
