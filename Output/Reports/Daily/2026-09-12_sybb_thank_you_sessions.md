# SYBB thank-you sessies (PostHog HogQL extract)

Datum run: 12 September 2026
Venster: 13 August 2026 00:00 tot 12 September 2026 00:00 (UTC)
Bron: PostHog (claude.ai connector `execute-sql` + directe REST route), project STX EU (149694)

## Resultaat

```json
{"thank_you_sessions": []}
```

## Notities

- Er bestaat geen PostHog project met de naam "Default project" in de organisatie Sempertex Europe. Beschikbare projecten: STX EU (149694) en Ambition Avenue (240270). De pixel van startyourballoonbusiness.com zit in STX EU; de query is daar uitgevoerd en ter controle ook op 240270 (eveneens 0 rijen).
- Query (exact zoals opgegeven, met LIMIT 500) gaf 0 rijen via beide routes. Tweede query per sessie (utm_content van de eerste pageview) is daardoor niet van toepassing.
- Sanity check: startyourballoonbusiness.com had in het venster slechts 4 pageviews in totaal (2 op 23 augustus, 2 op 28 augustus), geen daarvan op een /thank-you pagina.
- Paden met "thank" in het project zijn uitsluitend webshop productpagina's op sempertexeurope.com (folie ballonnen "Thank You Dad" e.d.), geen conversiepagina.
- De geconfigureerde `posthog` MCP server (mcp.posthog.com/sse) faalde met HTTP 405; de claude.ai PostHog connector werkte wel. Geen Google MCPs gebruikt, geen Google Sheet bijgewerkt.
