Ik kan het rapport niet draaien. De vereiste MCPs zijn niet beschikbaar in deze sessie:

- **Meta Ads MCP (Pipeboard)** — geïnstalleerd, maar **niet geauthenticeerd**. Alleen `authenticate` en `complete_authentication` zijn beschikbaar. De data-tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn pas bereikbaar na OAuth.
- **PostHog MCP** — **niet aangesloten** in deze sessie. Geen enkele `mcp__posthog__*` tool beschikbaar.

Je instructie verbiedt expliciet alle Google MCPs als alternatieve bron, dus ik heb geen fallback om Meta Ads- of landing page-data op te halen. Zonder deze data kan ik geen inhoudelijk rapport schrijven — ik zou moeten gokken op cijfers, en dat doe ik niet in een performance rapport.

**Wat ik nodig heb om door te gaan — kies één:**

1. **Authenticeer Meta Ads (Pipeboard)** — ik start de OAuth flow, jij autoriseert in de browser, daarna kan ik Meta Ads data ophalen. PostHog blijft dan ongebruikt (sectie "Landing page health" vervalt) tenzij je die MCP alsnog aansluit.
2. **Sluit PostHog MCP aan** — en authenticeer Meta Ads. Dan kan ik het volledige rapport draaien.
3. **Lever de data handmatig aan** — plak campagne-data (spend, impressions, clicks, CTR, CPC, CPM, conversions) en ik verwerk het naar het rapport-format zoals gespecificeerd in de skill, en schrijf het weg naar `Output/Reports/Daily/2026-04-24_ads_report.md`.

Welke wil je?
