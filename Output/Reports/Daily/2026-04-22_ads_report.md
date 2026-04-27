De Pipeboard Meta Ads MCP server is niet geauthenticeerd, ik zie alleen `mcp__pipeboard-meta-ads__authenticate` en `mcp__pipeboard-meta-ads__complete_authentication`. De data tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn pas beschikbaar nadat de OAuth flow is doorlopen.

Volgens jouw strikte regel mag ik geen Google MCPs gebruiken en geen andere data bronnen aanroepen. Zonder Meta Ads authenticatie kan ik geen echte campagne data ophalen.

Twee opties:

1. **Authenticeer Pipeboard nu** — ik start de OAuth flow, jij autoriseert in de browser, en ik haal dan live data op voor het rapport.
2. **Skip Meta Ads voor nu** — ik genereer een leeg/placeholder rapport met alleen het format en sla het op naar het opgegeven pad. Niet bruikbaar voor beslissingen.

Wil je dat ik de Pipeboard OAuth flow start (optie 1)?
