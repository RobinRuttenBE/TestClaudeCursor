# SYBB Daily Report - 13 april 2026

## 1. Samenvatting

Flinke spendstijging gisteren: €140,38 tegenover een 7-daags gemiddelde van €66,45/dag (+111%). Meta heeft de delivery sterk opgeschaald. De CPC (link click) is met €1,29 ruim boven de €0,50 target, maar de funnel laat sterke signalen zien: 5 initiate checkouts en 1 complete registration. H11 domineert het budget (55,6%) en trekt alle bottom-funnel conversies. H14, vorige week de volumeleider, draait niet meer.

**PostHog data niet beschikbaar** - PostHog MCP is niet verbonden in deze sessie. Landing page metrics (bounce rate, scroll depth, session duration, CTA clicks) ontbreken.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €140,38 | €66,45 | ↑ +111% |
| Impressions | 9.890 | 7.010 | ↑ +41% |
| Link Clicks | 109 | 74 | ↑ +47% |
| CTR (all clicks) | 2,10% | 2,03% | → |
| CPC (link click) | €1,29 | €0,90 | ↑ +43% |
| CPC (all clicks) | €0,67 | €0,47 | ↑ +43% |
| Frequency | 1,47 | 1,79 | ↓ -18% |
| Reach | 6.715 | 3.908 | ↑ +72% |
| Landing Page Views | 86 | 57 | ↑ +52% |

### Conversies Gisteren

| Event | Aantal |
|-------|--------|
| View Content | 11 |
| Add to Cart | 8 |
| Initiate Checkout | 5 |
| Add Payment Info | 1 |
| Complete Registration | 1 |
| Purchase | 0 |

7d vergelijking: 2 purchases (€42.773,50 attributed value), 10 IC, 16 ATC, 1 registration.

### Ad Variant Performance (gisteren)

| Ad (utm_content) | Link Clicks | CTR | CPC (link) | Spend | LP Views | LP View Rate | Conversies |
|-------------------|-------------|-----|------------|-------|----------|--------------|------------|
| h11_b3_cta5 | 52 | 1,97% | €1,50 | €78,04 | 37 | 71,2% | 5 IC, 6 ATC, 1 reg |
| h13_b3_cta5 | 39 | 2,08% | €0,99 | €38,53 | 34 | 87,2% | 2 ATC |
| h12_b3_cta5 | 10 | 2,79% | €1,48 | €14,77 | 7 | 70,0% | 0 |
| h15_b3_cta5 | 8 | 2,35% | €1,13 | €9,04 | 8 | 100% | 0 |

**Beste variant:** H13 (h13_b3_cta5). Laagste CPC (€0,99), hoogste LP view rate (87,2%), en goede click-through. Efficiëntste advertentie van de dag.

**Slechtste variant:** H12 (h12_b3_cta5). Slechts 10 link clicks, geen enkele conversie, en een CPC van €1,48. Krijgt weinig delivery van Meta, wat aangeeft dat het algoritme hier ook minder vertrouwen in heeft.

**Opvallend:** H11 eet 55,6% van het dagbudget maar is verantwoordelijk voor ALLE downstream conversies (5 initiate checkouts, 1 complete registration). De hoge CPC (€1,50) wordt gecompenseerd door een veel hogere conversieratio op de landing page.

### Ad Set Performance (gisteren)

| Ad Set | Spend | Link Clicks | CPC (link) | Frequency |
|--------|-------|-------------|------------|-----------|
| Kopie 1 (H11) | €78,04 | 52 | €1,50 | 1,32 |
| Kopie 3 (H13) | €38,53 | 39 | €0,99 | 1,25 |
| Kopie 2 (H12) | €14,77 | 10 | €1,48 | 1,50 |
| Kopie 4 (H15) | €9,04 | 8 | €1,13 | 1,15 |

## 3. Landing Page Health

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | n/a | n/a | <55% | ⚪ |
| Avg Session Duration | n/a | n/a | >90s | ⚪ |
| Scroll 25% | n/a | n/a | >80% | ⚪ |
| Scroll 50% | n/a | n/a | >60% | ⚪ |
| Scroll 75% | n/a | n/a | >40% | ⚪ |
| Scroll 100% | n/a | n/a | >20% | ⚪ |
| CTA Click Rate | n/a | n/a | >4% | ⚪ |

> PostHog MCP niet beschikbaar. Verbind PostHog om deze sectie te vullen.

## 4. Funnel Drop-off (Meta Ads only)

```
Impressions (9.890) → Link Clicks (109 / 1,1%) → LP Views (86 / 78,9%) → View Content (11 / 12,8%) → ATC (8 / 9,3%) → IC (5 / 5,8%) → Registration (1 / 1,2%)
```

**Grootste lek:** Link Click → Landing Page View (21,1% drop-off). 23 van de 109 klikkers laden de pagina niet volledig. Dit kan wijzen op trage laadtijd of gebruikers die direct terugnavigeren. Zonder PostHog data is het moeilijk om te bepalen of dit een technisch of content probleem is.

**Positief:** Van LP View naar Initiate Checkout is het conversiepercentage 5,8%, wat boven het 5% target voor LP Conversie Rate ligt.

## 5. Rode Vlaggen

1. **CPC (link click) €1,29 - 158% boven target** (target: <€0,50). Alle individuele ads zitten boven target. Zelfs H13 met de beste CPC zit op €0,99. Dit is een structureel probleem, niet een incident.

2. **Spend spike +111%** vs 7d gemiddelde. Meta heeft de delivery agressief opgeschaald naar €140,38 (dagbudget: €100). Dit kan positief zijn (Meta vindt goede audiences), maar de stijgende CPC suggereert dat het meer kost om deze mensen te bereiken.

3. **H14 is verdwenen.** Vorige week was H14 de absolute volumeleider (€122,96/7d, 158 link clicks, laagste CPC €0,78). Gisteren: nul impressies. Als dit onbedoeld is, loop je je efficiëntste ad mis.

4. **H11 budgetconcentratie.** 55,6% van het spend in een enkele ad variant. Als H11 underperformt op een dag, heeft dat oversized impact op het totale resultaat. Wel de enige ad met downstream conversies.

## 6. Top 3 Acties voor Vandaag

### 1. Check status H14 in Meta Ads Manager
**Wat:** Controleer of H14,B3,CTA5 bewust gepauzeerd is of per ongeluk uit staat.
**Waarom:** H14 was vorige week de volumeleider met de laagste CPC (€0,78/link click) en 108 LP views in 7 dagen. Gisteren nul activiteit.
**Hoe:** Open Meta Ads Manager → Campagne "2026: SYBB" → Check status van het originele "BATCH 2: Expertise & POC" ad set en alle H14 ads.
**Verwachte impact:** Als H14 opnieuw geactiveerd wordt, kan dit de gemiddelde CPC verlagen en volume verhogen.
**Escalatie:** Geel (Robin goedkeuring nodig voor wijziging)

### 2. Monitor H11 conversieratio vandaag
**Wat:** Volg of de hoge conversieratio van H11 (5 IC van 37 LP views = 13,5%) aanhoudt of een daguitbijter was.
**Waarom:** H11 eet meer dan helft van het budget tegen de hoogste CPC (€1,50), maar is de enige ad die daadwerkelijk converteert. Als de conversieratio vandaag terugvalt, is de ROAS niet meer te rechtvaardigen.
**Hoe:** Check vanavond de dagresultaten. Als H11 vandaag 0 IC heeft bij vergelijkbaar spend, overweeg budget herverdeling.
**Verwachte impact:** Datagedreven beslissing over budget allocatie.
**Escalatie:** Groen (alleen observeren)

### 3. Verbind PostHog MCP voor complete analyse
**Wat:** Zorg dat PostHog MCP beschikbaar is voor de volgende rapport-run.
**Waarom:** Zonder landing page data missen we cruciale cross-referenties: H13 heeft de laagste CPC maar converteer die goedkope clicks ook op de LP? H11 is duur maar converteert, komt dat door de ad-kwaliteit of de LP-ervaring? Die vragen zijn onbeantwoordbaar zonder PostHog.
**Hoe:** Check PostHog MCP configuratie in Claude Code settings.
**Verwachte impact:** Volledige cross-referentie analyse mogelijk, betere optimalisatie beslissingen.
**Escalatie:** Groen (technische setup)

---

## Cross-Referentie Analyse (beperkt zonder PostHog)

Wat we WEL kunnen zien uit Meta data:

| Pattern | Observatie | Interpretatie |
|---------|------------|---------------|
| H11: Laag CTR + Hoog IC | 1,97% CTR maar 13,5% IC rate | Ad pre-kwalificeert hard. Minder klikkers, maar de juiste mensen. |
| H13: Hoog efficiency + Laag IC | €0,99 CPC, 87% LP view rate, maar 0 IC | Trekt geïnteresseerden aan die niet converteren. Mogelijk te breed publiek. |
| H12: Hoog CTR + 0 conversies | 2,79% CTR maar nul downstream | Misleidende ad of verkeerde audience match. |
| Spend spike + CPC stijging | +111% spend, +43% CPC | Meta schaalt op maar tegen hogere kosten. Audience wordt duurder. |

**Zonder PostHog ontbreken de LP-gedrag patronen.** We kunnen niet bepalen of H13's lage conversie komt door de LP (bounce, scroll) of door audience mismatch.

---

*Rapport gegenereerd op 14 april 2026 om 08:00*
*Databronnen: Meta Ads MCP (Pipeboard) | PostHog: niet beschikbaar*
*Campagne: 2026: SYBB | Account: Sempertex Ad Account (act_567892422940728)*
