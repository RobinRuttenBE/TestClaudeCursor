The Meta Ads MCP server needs to be authenticated before I can pull any campaign data. The `/ads-auto-optimize` command depends entirely on live Pipeboard data — without it I cannot fetch insights, evaluate kill-rules, or pause underperformers.

**Actie vereist — kies één van beide:**

1. **Aanbevolen:** Voer `/mcp` uit en selecteer **"claude.ai Pipeboard Meta Ads"** om te authenticeren.
2. **Alternatief:** Open deze URL in je browser om de `pipeboard-meta-ads` server te autoriseren:

   ```
   https://pipeboard.co/oauth/authorize?response_type=code&client_id=ec4e5e3b755cfce2ed7b7543e97cf0be&code_challenge=oDJ6v6yysxW2N_MQL3dvR_GPFf9bjKQyK4Q7GqS4Q6I&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A61387%2Fcallback&state=dO-C50Cdy90cwwmz7KfO2-3fZq3n8_QRDtc149Xq7wA&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
   ```

   Als de redirect-pagina een verbindingsfout toont, plak de volledige URL uit de adresbalk hier zodat ik `complete_authentication` kan aanroepen.

Zodra de authenticatie rond is, hervat ik automatisch:
- 3 dagen performance data ophalen voor `act_567892422940728` en `act_607231713057715`
- Kill-regels toepassen (Link CTR < 0.8%, CPC link > €1.50) en underperformers pauzeren
- 70-20-10 classificatie + budget/variatie/audience voorstellen
- Rapport opslaan naar `Output/Reports/Daily/2026-05-17_auto_optimize.md`

Ik houd me strikt aan de regel: **alleen Meta Ads MCP en PostHog MCP, geen Google MCPs, niet naar de Google Sheet schrijven.**

Laat me weten zodra je geauthenticeerd bent, of plak de callback-URL.
