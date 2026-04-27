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

Ik kan het rapport niet draaien zonder Meta Ads data, en de Pipeboard MCP staat momenteel op niet-geauthenticeerd. De enige beschikbare tools zijn `authenticate` en `complete_authentication` — de daadwerkelijke `get_ad_accounts`, `get_campaigns`, `get_insights` en `get_ads` calls verschijnen pas na een succesvolle OAuth flow.

**Twee opties:**

1. **Authenticeren nu** — ik start de OAuth flow, jij klikt door in de browser, plakt de callback URL terug, en ik draai meteen het volledige rapport voor `act_567892422940728` (Sempertex) en `act_607231713057715` (Robin Rutten) over de laatste 30 dagen, met output naar `Output/Reports/Daily/2026-04-25_ads_report.md`.

2. **Overslaan** — als je nu geen tijd hebt voor de auth flow, sla ik het rapport over en pakken we het op zodra Pipeboard weer geauth'd is. Geen sense in een leeg of gefantaseerd rapport schrijven.

Welke wil je? Als je voor optie 1 gaat, zeg "ga", dan start ik de auth.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-24_sybb_report.md`.

**Kernpunten:**
- Vierde dag op rij nul spend op SYBB. Beide campagnes nog PAUSED (Kopie sinds 04-20 17:09, origineel sinds 04-19 14:29).
- Meta Ads MCP gaf data (zero-spend bevestigd via `get_insights` met `time_breakdown=day` over 04-17 t/m 04-24).
- PostHog MCP zesde dag op rij niet in de tool list, dus landing page health sectie blijft "geen data".
- Geen Google MCPs aangeraakt; alleen lokale markdown geschreven.
- Top actie: vandaag definitief beslissen tussen heractiveren, killen of rebuilden.

---

De Meta Ads MCP (Pipeboard) is niet meer geauthenticeerd, dus ik kan de campagne-data niet ophalen voor de auto-optimize run.

**Actie vereist van jou:**

1. Open deze URL in je browser om Pipeboard te autoriseren:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=3aee829ace93cf41d245bfad54c83a8e&code_challenge=JCztfSsMq6p73Y6GrvwGqM7hhvJmBgUWj6DOxRWHGPg&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A57813%2Fcallback&state=MZTDMWLeQ5ZfDXQQvI8K4BIWI5yOabU6WtMCjL7LWt4&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

2. Als de redirect pagina een fout toont (connection refused op localhost:57813), kopieer dan de volledige URL uit de adresbalk en plak die hier — dan rond ik de auth af en draai ik direct daarna de hele auto-optimize flow (3-daagse data ophalen → kill-regels toepassen → 70-20-10 classificeren → rapport opslaan in `Output/Reports/Daily/2026-04-25_auto_optimize.md`).

Geen Google MCPs worden aangeroepen, conform de strikte regel voor deze run.

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
