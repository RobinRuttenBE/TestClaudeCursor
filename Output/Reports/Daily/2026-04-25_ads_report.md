Ik kan het rapport niet draaien zonder Meta Ads data, en de Pipeboard MCP staat momenteel op niet-geauthenticeerd. De enige beschikbare tools zijn `authenticate` en `complete_authentication` — de daadwerkelijke `get_ad_accounts`, `get_campaigns`, `get_insights` en `get_ads` calls verschijnen pas na een succesvolle OAuth flow.

**Twee opties:**

1. **Authenticeren nu** — ik start de OAuth flow, jij klikt door in de browser, plakt de callback URL terug, en ik draai meteen het volledige rapport voor `act_567892422940728` (Sempertex) en `act_607231713057715` (Robin Rutten) over de laatste 30 dagen, met output naar `Output/Reports/Daily/2026-04-25_ads_report.md`.

2. **Overslaan** — als je nu geen tijd hebt voor de auth flow, sla ik het rapport over en pakken we het op zodra Pipeboard weer geauth'd is. Geen sense in een leeg of gefantaseerd rapport schrijven.

Welke wil je? Als je voor optie 1 gaat, zeg "ga", dan start ik de auth.
