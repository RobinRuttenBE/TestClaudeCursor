Ik kan het rapport nu niet genereren met live data. Hier is wat er aan de hand is:

**Blokkers:**
- **Meta Ads MCP (Pipeboard)** — niet geauthenticeerd. Tools zoals `get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads` zijn niet beschikbaar tot je de OAuth flow afrondt.
- **PostHog MCP** — niet geladen in deze sessie. Geen tools voor pageviews, bounce rate, CTA clicks etc.

De strikte regel voor deze run sluit Google MCPs (Sheets/Drive/GA4) en alle andere bronnen uit, dus ik heb geen alternatieve databron.

**Actie nodig van jou:**

1. Open deze URL in je browser om Pipeboard Meta Ads te autoriseren:

   https://pipeboard.co/oauth/authorize?response_type=code&client_id=f02ce0c1ed6d5c6e8b6b52ebb1c2c101&code_challenge=1UUuwNVTZBbkIn44iJuZbhiqPkF26_LbIdzxrO7uVNk&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A55426%2Fcallback&state=bP87qLjhruG5uLJ2rG8hpGpq-aLc0Tbi27CJFlD6QWU&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

2. Als de redirect-pagina een connection error toont, plak de volledige URL uit je adresbalk hier — dan rond ik de auth af.

3. Voor PostHog: laat weten of de MCP geconfigureerd moet worden, of dat ik dit rapport mag draaien zonder PostHog cross-reference (alleen Meta Ads data).

Zodra Pipeboard geautoriseerd is, draai ik het rapport en sla op naar `Output/Reports/Daily/2026-04-26_ads_report.md`.
