Zelfde situatie als gisteren. Twee blokkades:

1. **Pipeboard Meta Ads MCP** is geïnstalleerd maar vereist OAuth authenticatie. De data-tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn niet beschikbaar tot je inlogt.
2. **PostHog MCP** is niet aangesloten in deze sessie (geen tools gevonden in search).

Conform jouw instructie mag ik geen Google MCPs gebruiken als fallback, dus ik kan zonder Pipeboard geen campagnedata ophalen.

Wil je dat ik de Pipeboard auth flow start? Dan krijg je een autorisatie-URL — na login kan ik `act_567892422940728` (Sempertex) en `act_607231713057715` (Robin Rutten) trekken over last_30d en het rapport opslaan in `Output/Reports/Daily/2026-04-28_ads_report.md`. Ik schrijf het bestand pas weg zodra er echte data is — geen placeholder rapporten.
