Ik kan het rapport niet draaien zonder de data. Twee blokkades:

1. **Pipeboard Meta Ads MCP** is geïnstalleerd maar vereist OAuth authenticatie. De echte tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn niet beschikbaar tot je inlogt.
2. **PostHog MCP** lijkt niet aangesloten in deze sessie. Hij komt niet terug in de tool search.

Wil je dat ik de Pipeboard auth flow start? Dan krijg je een autorisatie-URL die je in de browser opent, en daarna kan ik direct de data ophalen voor `act_567892422940728` en `act_607231713057715` over de afgelopen 30 dagen.

Voor PostHog: check even of die MCP actief is in je config, anders kan ik wel het Meta Ads gedeelte draaien zonder de PostHog cross-reference.
