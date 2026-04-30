Ik kan het Meta Ads rapport niet draaien zonder werkende MCP-verbindingen. Twee blockers:

**1. Pipeboard Meta Ads MCP — niet geauthenticeerd**
Open deze URL om te autoriseren:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=e6ceaa3dff6a1aef3cda5a01a597fd86&code_challenge=Bu59qrq2d62Cn15gfgOVJfFAqlF7gZfXXAdWCssGEgQ&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A51099%2Fcallback&state=JEeO5xBBdgK1x-KBxHkzfdt0pQIOYg7pDPsy2wAusjM&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Als de browser een connection error toont op de redirect, kopieer de volledige URL uit de adresbalk en stuur die terug, dan complete ik de auth flow.

**2. PostHog MCP — niet beschikbaar in deze sessie**
Ik vind geen `mcp__posthog__*` tools tussen de geladen MCPs. Mogelijk moet die server opnieuw gestart of toegevoegd worden in MCP-config.

De Google MCPs (Drive/Sheets) wil je niet gebruiken voor deze run, dus ik kan ook geen oude rapporten cross-checken via Drive. Laat me weten zodra Pipeboard geautoriseerd is, dan trek ik de Meta Ads data en schrijf het rapport naar `Output/Reports/Daily/2026-04-30_ads_report.md` (zonder PostHog cross-reference, of we wachten tot PostHog ook online is).
