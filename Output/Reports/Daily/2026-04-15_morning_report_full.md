# Morning Report — 2026-04-15

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 21386,75** bij 2 purchases (totaal EUR 42773,50).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (15% marge): EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), EUR 892-1465 (3 tickets), etc.
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,07%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 0,99** (spend ÷ link_clicks)
> - Bron: spend EUR 701,76 · impressions 66.261 · link_clicks 711
> Dit zijn de ENIGE betrouwbare CTR/CPC cijfers in dit rapport. Kale `CTR`/`CPC` in campagne-summary tabellen zijn overschreven met de link-based waarden. Per-ad tabellen bevatten mogelijk nog all-clicks cijfers — controleer dubbel.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport klaar. Hier de kernpunten:

## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | EUR 701,76 |
| Impressions | 66.261 |
| Link CTR | 1,07% |
| CPC (link) | EUR 0,99 |
| Purchases | ? (verifieer Wix) |
|ROAS n.v.t. (pixel datafout) |

### 3 actieve ads

| Ad | Spend | CPC | Purch. | Flag |
|----|-------|-----|--------|------|
| H11, B3, CTA5 | EUR 266,80 | EUR 0,66 | 0 | CPC te hoog, 0 conversies |
| H13, B3, CTA5 | EUR 142,66 | EUR 0,61 | 2 | CPC hoog maar ENIGE met purchases |
| H12, B3, CTA5 | EUR 102,81 | EUR 0,40 | 0 | Beste CPC/CTR ratio |

### Kritieke bevindingen

1. **H11 eet 38% van het budget** maar converteert niet, ondanks 13 add-to-carts en 13 initiate checkouts. Er zit een blokkade in de checkout flow.
2. **Bounce rate 81,9%** (target: <55%). Van 996 sessies verlaten 816 de pagina direct. Dit is het #1 probleem.
3. **UTM inconsistentie:** 187 sessies met uppercase "META/SYBB" naast 697 met lowercase. Fix naar consistent lowercase.
4. **Gem. dagspend EUR 23,39** van EUR 100 budget. Delivery is gelimiteerd.

### Top 3 acties
1. **Verschuif budget van H11 naar H13** (enige converterende ad, ROAS n.v.t. (pixel datafout))
2. **Fix de landing page bounce rate** (81,9% is de grootste bottleneck in de funnel)
3. **Geef H12 meer ruimte** als secondary winner (laagste CPC EUR 0,40)

Rapport: `Output/Reports/Daily/2026-04-15_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen en gepusht. Hier de kernpunten:

**Meta Ads 14 april:** €95.93 spend, CPC €0.62 (boven target), 83 link clicks, 63 LP views. H12 is de sterkste variant (3.02% CTR, €0.98/link click, 2 ATCs) maar krijgt slechts 9% van het budget.

**Landing Page:** 82.7% bounce rate (target <55%), 46.7s sessieduur (target >90s), gemiddelde scroll depth 49%. 10 unieke bezoekers bereikten /booking. CTA click rate (~11%) is sterk, het probleem zit in de eerste seconden.

**Cross-reference:** H11 krijgt 66% van het budget maar 0% van de ATCs. H12 krijgt 9% budget maar 100% van de ATCs. Budget is omgekeerd aan prestatie.

**Prioriteiten:**
1. Budget van H11 naar H12 verschuiven (directe CPC/ATC impact)
2. Hero sectie herschrijven (bounce rate aanpakken)
3. Rageclicks analyseren in PostHog (11 stuks in 7 dagen)

---

Auto-optimize rapport klaar. Hier de samenvatting:

## Resultaat 2026-04-15

**0 ads gepauzeerd** -- alle 3 actieve ads (H11, H12, H13) presteren boven de kill-drempels.

### Key metrics (3d)
| Ad | Link CTR | CPC (link) | Spend | Purchases |
|----|----------|------------|-------|-----------|
| H11 | 0,98% | €1,40 | €220,60 | 0 |
| H12 | 1,19% | €1,16 | €42,96 | 0 |
| H13 | 1,17% | €1,10 | €90,03 | 0 |

### Grootste probleem: budget mismatch wordt erger
- H11 (? purchases (verifieer Wix) lifetime, €311 spend) krijgt nu **62,4%** van budget (was 45% gisteren)
- H13 (enige ad met purchases,ROAS n.v.t. (pixel datafout)) krijgt slechts **25,5%**
- Na pauzering van H14 gisteren stuurt Meta nog meer budget naar H11

### 5 voorstellen wachten op goedkeuring:
1. **Pauzeer ad set Kopie 1 (H11)** om budget naar H13/H12 te forceren
2. **Checkout flow diagnose** -- H11 heeft 13 IC maar ? purchases (verifieer Wix), er zit een blokkade
3. **Hook variaties** op H12 (beste CTR) en H13 (enige met purchases)
4. **ROAS verificatie** -- zijn H13's ? purchases (verifieer Wix) (€42.773) echte orders?
5. **Audience** -- geen actie nodig, frequency <2.0

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_auto_optimize.md`. Welke voorstellen wil je uitvoeren?

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
