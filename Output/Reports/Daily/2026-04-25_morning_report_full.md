# Morning Report — 2026-04-25

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
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 207,00 | 16.767 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 155,80 | 15.013 | 194 | 1,29% | EUR 0,80 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 52,15 | 4.894 | 61 | 1,25% | EUR 0,85 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H13 · ROAS 2.05x · 1 order(s) · EUR 423,50 revenue.


Ik kan het rapport niet draaien zonder Meta Ads data. De Pipeboard Meta Ads MCP is niet geauthenticeerd in deze sessie.

**Actie vereist van Robin:**

1. Open deze URL in je browser om Pipeboard te autoriseren:

```
https://pipeboard.co/oauth/authorize?response_type=code&client_id=bbf49e8178e1e0bcbf36968f22198fe1&code_challenge=KqPxdXlmYVH8iUtTNyohdEDBMID28xJuglAo-N5GKsU&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A61314%2Fcallback&state=pEMWYzX6HGcZvixBbxsR2xaCtpHHQBTAPeKvWxFs0mA&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
```

2. Na autorisatie zou je naar `http://localhost:61314/callback?code=...&state=...` worden geredirect. Als die pagina niet laadt: kopieer de volledige URL uit de adresbalk en plak hem hier, dan rond ik de auth af en draai het rapport meteen.

**Status van de strikte regels:** ik blijf binnen Meta Ads MCP + PostHog MCP, geen Google MCPs aangeroepen, en het rapport zal worden opgeslagen naar `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-25_ads_report.md` zodra de data binnen is.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-04-24_sybb_report.md`.

**Kernbevindingen:**
- Campagne **"2026: SYBB" staat PAUSED sinds 19/4** — geen spend, 0 impressions/klikken gisteren. Op de LP slechts 2 pageviews/2 sessies (organisch).
- 7d snapshot (alleen 18-19/4 actief): €138.45 spend, CTR 2.32%, CPC €0.65, 9 initiate checkouts.
- **Winnende variant: H12_B3_CTA5** — CTR 3.63%, CPC €0.45, beste IC-ratio (8.1%).
- LP health is rood: bounce 84.5%, avg scroll 33.5%, avg session 37s, slechts 4.4% klikt door naar product-pagina.

**Top 3 acties:** (1) beslissen of campagne herstart wordt of de "Kopie"-variant lanceert, (2) hero-sectie en CTA-positie van LP herzien vóór budget terug aan staat, (3) bij herstart alleen H12 actief zetten met €30/dag.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-25_auto_optimize.md`.

**Samenvatting:**
- Geen actieve Meta Ads campagnes in de toegankelijke accounts (`act_567892422940728` en `act_1489853856181844`).
- Alle 5 campagnes op het primaire STX EU account staan op PAUSED — inclusief `2026: SYBB` (gepauzeerd op 2026-04-19) en de duplicaat `2026: SYBB - Kopie` (2026-04-20).
- Geen spend/impressies in `last_3d` op accountniveau, dus geen kill-acties uit te voeren en geen 70-20-10 classificatie mogelijk.
- `act_607231713057715` is niet toegankelijk met de huidige Pipeboard-token (alleen `act_1489853856181844` en `act_567892422940728` zijn allowed).
- Twee operationele vragen voor jou opgenomen: is de SYBB-pauze bewust, en moet de token-scope voor `act_607231713057715` worden uitgebreid?

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.05x | EUR 207,00 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-18, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

**Ranking op Verified ROAS:**

| Rank | Ad | Verified ROAS | Wix Orders | Revenue | Spend | Advies |
|---|---|---|---|---|---|---|
| 🥇 | H13,B3,CTA5 | 2.05x | 1 | EUR 423,50 | EUR 207,00 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| 🥈 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | 20% budget — tweede verified winner · houd actief |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H13** (verified ROAS 2.05x, 1 Wix order(s), EUR 423,50 revenue).
- H13 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
