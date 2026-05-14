De Meta Ads MCP (Pipeboard) heeft een verlopen Facebook connectie en kan op dit moment geen data ophalen. Ik kan zonder die data geen rapport genereren.

**Wat je moet doen:**

Open deze URL in je browser om de Pipeboard Meta Ads connectie te herstellen:

```
https://pipeboard.co/oauth/authorize?response_type=code&client_id=3600e7cd3a17d279dde0e741c5c191f9&code_challenge=_EblJapPNOgVttoTvT3hIddIoifN4s-Qojm7tP-g5zU&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A56927%2Fcallback&state=xAMquyQBOKt4YdIQ7L_-WTtscF_s7l2YsSgihK_h2jA&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
```

Na het voltooien van de autorisatie kun je `/ads-report` opnieuw draaien. Als de browser een connection error toont op de redirect pagina, plak dan de volledige URL uit de adresbalk hier zodat ik `complete_authentication` kan aanroepen.

**Status rapport:** niet gegenereerd. Geen lokaal bestand geschreven naar `Output/Reports/Daily/2026-05-14_ads_report.md` omdat er geen brondata beschikbaar is.
