# Morning Report — 2026-05-13

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

De Meta Ads MCP-verbinding is verlopen. Ik kan zonder Facebook-authenticatie geen campagne data, insights of ads ophalen — dat blokkeert het volledige rapport.

**Actie nodig van Robin:**

Open deze URL in je browser om opnieuw te koppelen met Pipeboard / Meta:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=0f75a6ea066c0dac726a6daf7389139a&code_challenge=WkB_HlNsyxGgERMXtrI767ndgsve5dxK8FmiMGz1RhU&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A57469%2Fcallback&state=V64GY_3bhQpY8vOu8_tVhYP38MJMSkGb8mit9AhQYnY&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Wat je doet:
1. Klik de URL, log in en autoriseer
2. De browser krijgt een "kan niet bereiken" foutpagina op `localhost:57469/callback?...` — dat is normaal
3. Kopieer de **volledige URL uit de adresbalk** van die foutpagina en plak hem hier

Zodra ik die callback URL heb, voltooi ik de authenticatie en draai het rapport meteen door. Output komt in `Output/Reports/Daily/2026-05-13_ads_report.md` (geen Google Sheet write, zoals afgesproken).

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-12_sybb_report.md`.

**Belangrijkste bevindingen 12 mei:**
- **Meta Ads MCP voor de 2e dag dood** — `Facebook connection required` op alle Pipeboard calls. Geen ad-data ophaalbaar. Reconnect via https://pipeboard.co/connections is overdue.
- **PostHog ziet een vreemde piek**: 14 pageviews (+350% vs 7d gem.), 10 sessies, 8 unieke bezoekers. 13 van de 14 pageviews op `/review`, alle direct, 12 daarvan Belgisch mobiel.
- **Cluster van 4 sessies binnen 8 seconden** op 14:13 UTC wijst sterk op een gedeelde link (WhatsApp/Messenger preview-fetches) of interne test — niet organisch.
- **70% bounce, 32,1s avg duur**: één Belgische desktop sessie van 311s trekt het gemiddelde op; mediane sessie zit op 0-7s.
- **Nul cpc-traffic** bevestigt dat campagne `2026: SYBB` daadwerkelijk geen levering meer heeft. 23e dag paused. Zero `/booking` views voor 9e dag op rij.
- **Onveranderde meet-gap**: alleen `$pageview` en `$web_vitals`. Geen scroll/CTA tracking, dus de `/review` engagement is een black box.

**Top 3 acties:** (1) Pipeboard MCP reconnect — 2e dag overdue. (2) Onderzoek herkomst van de `/review` piek voordat het signaal afkoelt (Manychat/sociale kanalen/teamtest). (3) `/review` route documenteren én tracking deployen, parallel met relaunch-of-stop beslissing.

Geen Google MCPs aangeroepen.

---

Run geblokkeerd: Pipeboard Meta Ads MCP heeft re-authenticatie nodig (`Facebook connection required` op alle calls voor beide accounts). Voorlopig rapport opgeslagen in `Output/Reports/Daily/2026-05-13_auto_optimize.md` met de status en wat er geprobeerd is.

Open de OAuth-URL hierboven, plak daarna de callback-URL terug in chat, dan draai ik /ads-auto-optimize opnieuw met live data.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
