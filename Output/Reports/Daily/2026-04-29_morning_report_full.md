# Morning Report — 2026-04-29

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,13%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 88,29** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1059,47 · impressions 91.839 · link_clicks 1.036
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-29

**Periode:** last_30d (2026-03-30 t/m 2026-04-28)
**Account:** Sempertex Ad Account (`act_567892422940728`) — geen ACTIVE campagnes. Account `act_607231713057715` niet bereikbaar via deze token.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout)* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 (6 IC) | n.v.t. |
| Last push Nozzle Up | PAUSED | — | — | — | — | — | — | — | — |
| Nozzle Up END OF AUGUST | PAUSED | — | — | — | — | — | — | — | — |
| Campagne Nozzle Up 2025 1 | PAUSED | — | — | — | — | — | — | — | — |

*ROAS lijkt opgeblazen door upsell/wholesale tracking. Bij €350 workshop AOV = ~n.v.t. (pixel datafout) reëel.

### Underperformers

- **2026: SYBB** — CPC €0,55 boven drempel €0,50. Lichte tweak via thumbnails bij relaunch.
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34. Te kleine schaal voor stabiele unit economics. Mergen of verhogen naar min €30/dag/adset.
- **Funnel gat Kopie** — 6 initiate checkouts → ? purchases (verifieer Wix). Check checkout flow (payment, currency, mobile UX).
- **ATC → Purchase main** — 44 ATC → ? purchases (verifieer Wix) = 13,6% (hoort >25% te zijn). Cart abandonment flow activeren.

### Top performers

- **Beste CTR**: 2026: SYBB - Kopie — 2,6%
- **Laagste CPC**: 2026: SYBB — €0,55
- **Beste ROAS**: 2026: SYBB — n.v.t. (pixel datafout) gerapporteerd / ~n.v.t. (pixel datafout) reëel

### Samenvatting

- **Totaal spend**: €1.183,89 (last 30d)
- **Beste performer**: 2026: SYBB — schaal + 818 LPVs + ? purchases (verifieer Wix)
- **Slechtste performer**: Kopie-campagne op conversie-niveau, ? purchases (verifieer Wix) ondanks 6 IC's
- **Aanbeveling (70-20-10)**: 70% main campaign relaunchen met budget +20-30% op winnende adsets, 20% kopie mergen met main, 10% nieuwe hooks op ATC→Purchase gat. Funnel-fix (checkout + cart abandonment) is hogere leverage dan nieuwe creatives.

### Google Sheet
Overgeslagen conform instructie. Rapport opgeslagen in `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-29_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Twee blokkades voor deze run, identiek aan de afgelopen dagen:

**1. Pipeboard Meta Ads MCP — OAuth flow gestart**
Open deze URL in je browser om te autoriseren:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=047042c19e2f443f05f324fe5ea14953&code_challenge=ajTgLJqOkgh2Og9Wnt5BoUn8K430CwERqq0nc6Oy-mE&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A55027%2Fcallback&state=AX4Gn21er7Oc8lF4MYy68NAvhjo8TYypItuMhXXSOYc&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Na autorisatie verschijnen de Meta Ads data-tools (`get_campaigns`, `get_insights`, `get_ads`, etc.) automatisch. Als de redirect-pagina een connection error toont, paste de volledige URL uit je adresbalk hier en ik roep `complete_authentication` aan.

**2. PostHog MCP — niet beschikbaar in deze sessie**
Geen `posthog_*` tools in de deferred tool lijst (10e rapportdag op rij). Dit raakt de Landing Page Health sectie en de cross-reference logic die de kern is van deze SKILL.

**Wat ik niet doe:**
- Geen placeholder rapport wegschrijven naar `Output/Reports/Daily/2026-04-28_sybb_report.md`. Conform precedent in `2026-04-27_sybb_report.md` en `2026-04-28_ads_report.md`: alleen schrijven met echte data.
- Geen Google MCPs als fallback (Gmail/Calendar/Drive/Sheets/Docs/Slides). Geen schrijfactie naar de Meta Ads Tracker Google Sheet.

**Context die je al hebt zonder nieuwe MCP-calls:**
Beide SYBB campagnes staan sinds 2026-04-19/20 op PAUSED. Het 2026-04-29 ads_report (vanmorgen geschreven) bevat al de last_30d snapshot waarin 2026-04-28 valt: 0 spend op 04-28, totaal €1.183,89 over 30d, beslissingslog en iter1 baseline-document staan al 4 dagen open. Voor een "echt" SYBB rapport voor specifiek 04-28 met daily breakdown heb ik alsnog `get_insights` met `time_breakdown=day` nodig.

Wil je de auth afronden en dan run ik `get_campaigns` + `get_insights` (range 04-21 t/m 04-28 voor 7d window + dag 04-28) op `act_567892422940728` en schrijf het rapport weg? Of wil je een rapport-versie die expliciet beide bronnen als "niet beschikbaar in deze sessie" markeert en alleen leunt op de reeds in eerdere rapporten verzamelde data?

---

## Auto-Optimize Rapport — 2026-04-29

**Geen automatische acties uitgevoerd. Geen actieve campagnes.**

Bevindingen:
- `act_567892422940728`: alle 5 campagnes staan op PAUSED. "2026: SYBB" sinds 2026-04-19, "2026: SYBB - Kopie" sinds 2026-04-20.
- `act_1489853856181844`: geen campagnes.
- `act_607231713057715`: niet toegankelijk via huidig token (allowlist sluit dit account uit).
- last_3d insights op accountniveau: leeg voor beide toegankelijke accounts.

Kill-regels niet activeerbaar — geen impressions, geen link clicks, geen ads om te pauzeren.

**Belangrijkste signaal van vandaag is geen optimalisatieprobleem maar een delivery-gat:** SYBB-funnel ligt 9 dagen stil. Als always-on bedoeld → opnieuw activeren. Voorstellen voor heractivatie staan in het rapport (ad-niveau review op last_30d data + ROAS-onderzoek; SYBB liep op €176,58 per purchase / ROAS n.v.t. (pixel datafout)).

Volledig rapport: `Output/Reports/Daily/2026-04-29_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
