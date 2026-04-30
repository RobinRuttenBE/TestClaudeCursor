# Morning Report — 2026-04-30

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

Ik kan het Meta Ads rapport niet draaien zonder werkende MCP-verbindingen. Twee blockers:

**1. Pipeboard Meta Ads MCP — niet geauthenticeerd**
Open deze URL om te autoriseren:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=e6ceaa3dff6a1aef3cda5a01a597fd86&code_challenge=Bu59qrq2d62Cn15gfgOVJfFAqlF7gZfXXAdWCssGEgQ&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A51099%2Fcallback&state=JEeO5xBBdgK1x-KBxHkzfdt0pQIOYg7pDPsy2wAusjM&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Als de browser een connection error toont op de redirect, kopieer de volledige URL uit de adresbalk en stuur die terug, dan complete ik de auth flow.

**2. PostHog MCP — niet beschikbaar in deze sessie**
Ik vind geen `mcp__posthog__*` tools tussen de geladen MCPs. Mogelijk moet die server opnieuw gestart of toegevoegd worden in MCP-config.

De Google MCPs (Drive/Sheets) wil je niet gebruiken voor deze run, dus ik kan ook geen oude rapporten cross-checken via Drive. Laat me weten zodra Pipeboard geautoriseerd is, dan trek ik de Meta Ads data en schrijf het rapport naar `Output/Reports/Daily/2026-04-30_ads_report.md` (zonder PostHog cross-reference, of we wachten tot PostHog ook online is).

---

Rapport opgeslagen en gepusht naar GitHub: `Output/Reports/Daily/2026-04-29_sybb_report.md`.

**Headline:** Campagne `2026: SYBB` staat sinds 2026-04-19 op PAUSED — nul activiteit op 2026-04-29 (geen spend, clicks, impressies). De top-actie is een reactiveer-of-archiveer beslissing, niet een ad-tweak.

**Beperkingen van deze run:**
- PostHog MCP niet beschikbaar in deze sessie → secties 3 (Landing Page Health) en 4 (Funnel Drop-off) zonder data, geen cross-referencing mogelijk.
- Duplicaat-campagne `2026: SYBB - Kopie` (aangemaakt 2026-04-19, ook PAUSED) gevlagd voor opruimen.
- Geen Google MCPs gebruikt zoals gevraagd.

Wil je dat ik een `/schedule` zet om de PostHog MCP-status over een paar dagen opnieuw te checken, of pak je MCP-config zelf op?

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-30_auto_optimize.md`.

**Korte samenvatting:**
- **0 ads gepauzeerd** — er zijn geen actieve campagnes op `act_567892422940728` (alle 5 staan op PAUSED, geen spend last_3d).
- Account `act_1489853856181844` ook leeg, `act_607231713057715` niet toegankelijk met huidige token.
- Geen voorstellen op basis van performance, wel één observatie: de SYBB campagne (`120239435987290239`) staat al sinds 2026-04-19 op PAUSED. Wil je 'm weer aanzetten of bewust uit laten?
- Alleen Meta Ads MCP gebruikt; geen Google MCPs, geen schrijfacties naar Google Sheet.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| (geen ad match) | - | - | - | 2 (EUR 773,50) | EUR 773,50 | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **0** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
