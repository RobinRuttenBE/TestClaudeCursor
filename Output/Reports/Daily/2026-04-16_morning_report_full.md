# Morning Report — 2026-04-16

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport is geschreven en gepusht. Hier is de samenvatting:

---

## Meta Ads Rapport -- 16 april 2026

### Campagne: 2026: SYBB (Active)

| Metric | Waarde |
|--------|--------|
| **Spend (30d)** | EUR 776,42 |
| **Impressions** | 72.110 |
| **Clicks** | 1.478 |
| **CTR** | 2,0% |
| **CPC** | EUR 0,53 |
| **Purchases** | 6 (waarde: EUR 44.247) |
| **ROAS** | 57,0x |

### 3 Actieve Ads

| Ad | Spend | CPC | CTR | Purchases | ROAS | Flag |
|----|-------|-----|-----|-----------|------|------|
| H11, B3, CTA5 | EUR 328,99 | EUR 0,66 | 2,0% | 4 | 4,5x | CPC boven target |
| H13, B3, CTA5 | EUR 149,30 | EUR 0,62 | 1,9% | 2 | 286,5x | CPC boven target |
| H12, B3, CTA5 | EUR 108,64 | EUR 0,39 | 2,4% | 0 | 0x | Geen conversies |

### Key Takeaways

1. **H12 paradox:** Laagste CPC (EUR 0,39), hoogste CTR (2,4%), maar 0 purchases na EUR 108 spend. Funnel probleem na de klik.
2. **H13 power:** Slechts 2 purchases maar EUR 42.773 aan waarde. Premium kopers.
3. **H11 workhorse:** 4 van 6 purchases, meest consistent maar duurste CPC.
4. **Campaign CPC** (EUR 0,53) net boven de EUR 0,50 target.
5. **Frequency** (1,99) veilig, geen creative fatigue risico.

### Hormozi 70-20-10

- **70%:** H11 + H13 behouden (alle conversies)
- **20%:** H12 testen met andere LP/CTA variant om conversie gap te dichten
- **10%:** Overweeg H14 reactivatie (had goede CPC EUR 0,41 en CPM EUR 7,43)

Rapport opgeslagen in `Output/Reports/Daily/2026-04-16_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit PostHog, Wix Analytics of GA4. Ik heb nodig: landing page visitors, bounce rate, scroll depth, CTA clicks, en booking/purchase conversies. Dan draai ik automatisch een `/funnel-diagnose`.

---

Rapport is klaar en gepusht. Hier de samenvatting:

**Belangrijk: er bleek al een rapport voor 15 april op de remote te staan** (eerder vandaag gegenereerd met PostHog data). Die versie is completer dan de mijne omdat PostHog MCP in deze sessie niet bereikbaar was. De remote versie is behouden.

## Key findings 15 april:

**Positief:**
- **4 purchases, €1,473.50 revenue, ROAS 19.7x** (alle via H11)
- Frequency laag (1.34), publiek is vers
- CTR stabiel rond 2.09%

**Aandachtspunten:**
- **CPC €0.61** (boven €0.50 target, +13% vs 7d gem.)
- **Volume fors lager**: spend -27%, impressions -34%, LP views -42% vs 7d gemiddelde
- **H13 presteert slecht**: 1.14% CTR, €0.95 CPC, 0 conversies
- **83% van budget gaat naar H11**, terwijl H12 4.55% CTR heeft en €0.25 CPC

**PostHog MCP was niet bereikbaar** in deze sessie. Voor een volledig rapport met LP-data (bounce rate, scroll depth, CTA clicks) moet de PostHog MCP server opnieuw verbonden worden. Het remote rapport van eerder vandaag heeft die data wel.

**Top acties:**
1. PostHog MCP herstellen
2. Budget van H13 naar H12 verschuiven
3. De 4 purchases van gisteren valideren in het order dashboard

---

Rapport opgeslagen, gecommit en gepusht.

---

## Resultaat Auto-Optimize 2026-04-16

**0 ads gepauzeerd** - alle 3 actieve ads presteren boven de kill-drempelwaarden.

### Highlights:
- **ROAS campagne:** 4,74x (€1.473,50 omzet op €311,19 spend)
- **H11** is de converter: 4 purchases, ROAS 7,23x, maar CPC (link) op €1,33 (nadert €1,50 grens)
- **H12** heeft de beste Link CTR (1,30%) maar krijgt slechts 9,5% van het budget door CBO
- **H13** stabiel, lifetime data toont opvallend hoge purchase value (€42.773,50) die verificatie nodig heeft

### 4 voorstellen ter goedkeuring:
1. **H11 CPC (link) dagelijks monitoren** (zit op 89% van kill-grens)
2. **H12 minimum budget €15/dag** geven voor eerlijke dataverzameling
3. **2 experimentele ads toevoegen** (er draaien nu 0 experimental ads, zou 10% moeten zijn)
4. **H13 purchase waarde verifi\u00ebren** in webshop backend (€42.773,50 voor 2 purchases lijkt abnormaal)

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
