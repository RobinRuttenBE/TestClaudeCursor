De Meta Ads MCP-verbinding is verlopen. Ik kan zonder Facebook-authenticatie geen campagne data, insights of ads ophalen — dat blokkeert het volledige rapport.

**Actie nodig van Robin:**

Open deze URL in je browser om opnieuw te koppelen met Pipeboard / Meta:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=0f75a6ea066c0dac726a6daf7389139a&code_challenge=WkB_HlNsyxGgERMXtrI767ndgsve5dxK8FmiMGz1RhU&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A57469%2Fcallback&state=V64GY_3bhQpY8vOu8_tVhYP38MJMSkGb8mit9AhQYnY&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Wat je doet:
1. Klik de URL, log in en autoriseer
2. De browser krijgt een "kan niet bereiken" foutpagina op `localhost:57469/callback?...` — dat is normaal
3. Kopieer de **volledige URL uit de adresbalk** van die foutpagina en plak hem hier

Zodra ik die callback URL heb, voltooi ik de authenticatie en draai het rapport meteen door. Output komt in `Output/Reports/Daily/2026-05-13_ads_report.md` (geen Google Sheet write, zoals afgesproken).
