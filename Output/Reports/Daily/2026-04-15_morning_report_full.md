# Morning Report — 2026-04-15

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 21386.75** bij 2 purchases (totaal EUR 42773.50).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (15% marge): EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), EUR 892-1465 (3 tickets), etc.
> Purchase aantal en ROAS in onderstaand rapport zijn overschreven met `? (verifieer Wix)` en `n.v.t. (pixel datafout)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport opgeslagen. Hier is de samenvatting:

## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (ACTIVE)
| Spend | Impressions | Clicks | CTR | CPC | Purchases | Revenue | ROAS |
|-------|------------|--------|-----|-----|-----------|---------|------|
| EUR 701,76 | 66.259 | 1.356 | 2,0% | EUR 0,52 | 2 | EUR 42.773,50 | n.v.t. (pixel datafout) |

### Top ads (op spend)
| Ad | Spend | CTR | CPC | Purch. | Flag |
|----|-------|-----|-----|--------|------|
| H11 (Kopie 1) | EUR 266,80 | 2,0% | **EUR 0,66** | 0 | CPC boven drempel |
| H13 (Kopie 3) | EUR 142,66 | 1,9% | EUR 0,61 | **2** | ROAS n.v.t. (pixel datafout) |
| H14 (BATCH 2) | EUR 122,96 | 1,8% | EUR 0,41 | 0 | Gepauzeerd |
| H12 (Kopie 2) | EUR 102,81 | 2,3% | EUR 0,40 | 0 | Beste CTR+CPC |
| H15 (Kopie 4) | EUR 49,83 | 2,3% | EUR 0,47 | 0 | Gepauzeerd |

### PostHog Cross-Reference
Alle bounce rates boven 55% target (59,8% tot 67,5%). Sessieduur is goed (1m42s tot 3m34s, allemaal boven 90s target). Grootste funnel lek: LP View naar View Content (91% drop-off).

### Top 5 Aanbevelingen
1. **70% budget naar H13** (enige converter,ROAS n.v.t. (pixel datafout))
2. **Pauzeer of halveer H11** (EUR 266,80 spend, ? purchases (verifieer Wix))
3. **Fix landing page bounce rate** (alle varianten boven 55% target)
4. **H12 als 20% variatie** (beste CPC EUR 0,40 + CTR 2,3%)
5. **Debug checkout funnel** (87% drop-off van IC naar purchase)

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_ads_report.md`

> **Wil je funnel data toevoegen?** Ik kan een `/funnel-diagnose` draaien met de Meta + PostHog data die ik al heb. Of geef aanvullende Wix/GA4 metrics voor een complete analyse.

---

Rapport opgeslagen en gepusht. Hier de samenvatting:

**SYBB Daily Report 14 april 2026 -- Kernpunten:**

**Meta Ads:** Spend €95.93, CPC €0.62 (24% boven target), CTR 2.11%. Impressies -23% vs 7d gem. 3 ads actief: H11 (66% budget, matig), H13 (70.4% bounce, slecht), H12 (beste op alle metrics maar slechts 9% budget).

**Landing Page (PostHog):** 134 pageviews, 100 unieke bezoekers. Bounce rate 60% (boven 55% target). Scroll depth zorgwekkend: slechts 44.8% scrollt voorbij 25%. CTA click rate ~15% (boven target). 10 unieke /booking bezoekers.

**Rode vlaggen:** CPC boven target, H13 bounce 70.4% (ad-pagina mismatch), scroll depth ≥25% slechts 44.8%, bounce rate boven target.

**Top 3 acties:**
1. Herverdeel budget van H11 naar H12 (beste performer op alle metrics)
2. Overweeg H13 te pauzeren (70.4% bounce = weggegooid geld)
3. Optimaliseer hero sectie LP (55% scrollt niet voorbij 25%)

Rapport: `Output/Reports/Daily/2026-04-14_sybb_report.md`

---

Rapport opgeslagen, gecommit en gepusht.

**Samenvatting:**

- **0 ads gepauzeerd** - alle 3 actieve ads presteren boven de kill-drempels
- **Vlakke performance** - nagenoeg identiek aan gisteren op alle metrics
- **Grootste risico:** H11 CPC (link) €1,40 blijft op €0,10 van de kill-grens, terwijl het 62,4% van budget opslokt
- **Opvallend:** H11 is de enige ad die checkouts/registraties genereert. H12 heeft na 124 lifetime link clicks nog steeds nul checkouts.
- **PostHog:** CTA click tracking is kapot (0 events). LP engagement is goed (1,9 pagina's per meta-sessie).

**5 voorstellen wachten op goedkeuring:** verscherpte CPC-monitoring (1), budget herverdeling (2A/2B), H12 funnel-diagnose (3), PostHog CTA tracking fix (4), H13 ROAS verificatie (5). Welke wil je uitvoeren?

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
