# SYBB Daily Report -- 10 april 2026

## 1. Samenvatting

Sterke dag voor SYBB. Spend steeg fors naar EUR 68,21 door de lancering van 4 nieuwe ad sets (Kopie 1-4) met varianten H11, H12, H13, H15. CTR en CPC bleven stabiel ondanks de schaalvergroting. H11 is de duidelijke winnaar: hoogste CTR (2,69%), meeste link clicks (29) en als enige ad 2 add-to-carts en 2 initiated checkouts. PostHog data niet beschikbaar (authenticatie vereist).

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | EUR 68,21 | EUR 26,72 | ↑ (+155%) |
| Impressions | 8.452 | 3.393 | ↑ (+149%) |
| Clicks (all) | 187 | 71,7 | ↑ (+161%) |
| Link Clicks | 100 | 37,4 | ↑ (+167%) |
| CTR | 2,21% | 2,11% | -> (stabiel) |
| CPC | EUR 0,36 | EUR 0,37 | -> (stabiel) |
| Frequency | 1,58 | 1,54 | -> (stabiel) |
| Landing Page Views | 65 | 26,1 | ↑ (+149%) |
| Video Views | 1.657 | 626 | ↑ (+165%) |

**Opmerking:** De forse stijging in spend/impressions komt door 4 nieuwe ad sets die op 10 april gelanceerd zijn. CTR en CPC zijn stabiel gebleven, wat aangeeft dat de schaalvergroting zonder kwaliteitsverlies verloopt.

### Conversies
| Conversie | Gisteren | 7d Totaal |
|-----------|----------|-----------|
| View Content | 9 | 13 |
| Add to Cart | 4 | 6 |
| Initiate Checkout | 2 | 2 |
| Cost per Checkout | EUR 34,11 | EUR 93,53 |

### Ad Variant Performance

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | Cost/LP View | LP Views | Conversies |
|-------------------|-------|-------------|-----|-----|--------------|----------|------------|
| H11, B3, CTA5 | EUR 16,16 | 29 | 2,69% | EUR 0,36 | EUR 0,73 | 22 | 2 ATC + 2 IC |
| H12, B3, CTA5 | EUR 20,44 | 28 | 2,07% | EUR 0,34 | EUR 0,89 | 23 | 2 ATC |
| H13, B3, CTA5 | EUR 14,74 | 16 | 1,98% | EUR 0,45 | EUR 1,34 | 11 | 2 VC |
| H14, B3, CTA5 | EUR 9,10 | 10 | 2,07% | EUR 0,38 | EUR 1,82 | 5 | -- |
| H15, B3, CTA5 | EUR 7,77 | 17 | 2,39% | EUR 0,32 | EUR 1,94 | 4 | -- |

*ATC = Add to Cart, IC = Initiate Checkout, VC = View Content*

**Beste variant:** H11, B3, CTA5. Hoogste CTR (2,69%), laagste cost per landing page view (EUR 0,73), en als enige variant zowel add-to-carts (2) als initiated checkouts (2). Dit is de sterkste performer over de hele funnel.

**Tweede plaats:** H12, B3, CTA5. Meeste landing page views (23), laagste CPC (EUR 0,34), 2 add-to-carts. Goede volume driver.

**Slechtste variant:** H14, B3, CTA5. Slechts 10 link clicks en 5 landing page views bij EUR 9,10 spend. Hoogste cost per LP view (EUR 1,82), nul conversies. Dit is dezelfde ad die in het originele ad set de afgelopen week EUR 111,24 heeft gespend met beperkte conversies.

### Ad Set Structuur

| Ad Set | Status | Ad | Spend gisteren |
|--------|--------|-----|----------------|
| BATCH 2: Expertise & POC (origineel) | Actief | H14, B3, CTA5 | EUR 9,10 |
| Kopie 1 | NIEUW | H11, B3, CTA5 | EUR 16,16 |
| Kopie 2 | NIEUW | H12, B3, CTA5 | EUR 20,44 |
| Kopie 3 | NIEUW | H13, B3, CTA5 | EUR 14,74 |
| Kopie 4 | NIEUW | H15, B3, CTA5 | EUR 7,77 |

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | -- | -- | <55% | PostHog auth vereist |
| Avg Session Duration | -- | -- | >90s | PostHog auth vereist |
| Scroll 25% | -- | -- | >80% | PostHog auth vereist |
| Scroll 50% | -- | -- | >60% | PostHog auth vereist |
| Scroll 75% | -- | -- | >40% | PostHog auth vereist |
| Scroll 100% | -- | -- | >20% | PostHog auth vereist |
| CTA Click Rate | -- | -- | >4% | PostHog auth vereist |

*PostHog authenticatie is vereist om deze data op te halen. Autoriseer via de link hierboven.*

## 4. Funnel Drop-off

```
Impressions (8.452) -> Link Clicks (100, 1,18%) -> LP Views (65, 65%) -> View Content (9, 13,8%) -> ATC (4, 44,4%) -> Checkout (2, 50%)
```

**Grootste lek:** Impressions naar Link Click (1,18% click-to-LP rate). Van de 187 clicks zijn er slechts 100 link clicks, wat gebruikelijk is bij video ads. De link click naar LP view conversie (65%) is acceptabel.

**Positief:** de bottom-funnel conversie is sterk. 44% van view content gaat naar add-to-cart, en 50% daarvan naar checkout. De kwaliteit van het verkeer dat doorkomt is hoog.

## 5. Rode Vlaggen

- **H14 performance vs budget:** H14 heeft over de afgelopen 7 dagen EUR 111,24 gespend (59% van totale campagne spend) maar genereert geen conversies (0 ATC, 0 IC). Dit is veruit de duurste ad met de slechtste ROI. De nieuwe ad sets met H11, H12, H13 en H15 trekken nu budget weg, wat een verbetering is.
- **H13 CPC boven gemiddelde:** EUR 0,45 CPC is het hoogste van alle varianten. Nog onder de EUR 0,50 target, maar houd in de gaten.
- **PostHog data ontbreekt:** Zonder landing page engagement data (bounce rate, scroll depth, CTA clicks) kunnen we geen ad-pagina mismatch detecteren. Dit is een blind punt.

## 6. Cross-referencing Insights

Zonder PostHog data beperkt tot Meta-only inzichten:

1. **H11 high CTR + high conversions:** Dit suggereert dat zowel de ad hook als de landing page alignment goed werken voor deze variant. Valideer met PostHog scroll depth data.
2. **H14 moderate CTR + zero conversions:** Mogelijk ad-pagina mismatch. De hook trekt wel clicks maar het verkeer converteert niet. PostHog bounce rate per utm_content zou dit bevestigen.
3. **H12 laagste CPC + hoge LP views:** Efficiënte volume driver. Check of de on-page engagement ook proportioneel is.

## 7. Top 3 Acties voor Vandaag

### 1. PostHog authenticatie herstellen
- **Wat:** PostHog MCP opnieuw autoriseren zodat landing page data beschikbaar is
- **Waarom:** Zonder bounce rate, scroll depth en CTA click data per utm_content missen we cruciale cross-referencing inzichten
- **Hoe:** Klik op de autorisatielink en voltooi de OAuth flow
- **Verwachte impact:** Volledig rapport met actionable LP optimalisatie inzichten
- **Escalatie:** Groen (zelf te doen)

### 2. H14 budget evalueren
- **Wat:** Overweeg om H14 te pauzeren of het budget te verlagen in het originele ad set
- **Waarom:** EUR 111,24 spend over 7 dagen met 0 conversies. De nieuwe ad sets met H11, H12 presteren significant beter
- **Hoe:** In Meta Ads Manager het originele ad set "BATCH 2: Expertise & POC" pauzeren of budget verlagen
- **Verwachte impact:** Budget verschuift naar beter presterende varianten, hogere ROAS
- **Escalatie:** Geel (Robin goedkeuring nodig)

### 3. H11 en H12 schalen
- **Wat:** Meer budget toewijzen aan de ad sets met H11 en H12
- **Waarom:** H11 is de enige variant met checkout conversies, H12 is de meest efficiente volume driver (laagste CPC, meeste LP views)
- **Hoe:** Budget van Kopie 1 (H11) en Kopie 2 (H12) verhogen, eventueel via CBO aanpassing
- **Verwachte impact:** Meer conversies bij lagere kosten per conversie
- **Escalatie:** Geel (Robin goedkeuring, wacht eerst 3-5 dagen data af van nieuwe ad sets)

---

*Rapport gegenereerd op 11 april 2026. Meta Ads data: Pipeboard MCP. PostHog data: niet beschikbaar (authenticatie vereist).*
