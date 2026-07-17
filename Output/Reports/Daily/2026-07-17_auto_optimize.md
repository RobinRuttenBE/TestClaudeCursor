Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-17_auto_optimize.md` en gepusht.

## Kort samengevat

**Er is niets geoptimaliseerd en niets gepauzeerd, want er zijn geen actieve ads.**

- **Primair account** (`act_567892422940728`): alle campagnes staan op **PAUSED**, inclusief de hoofdcampagne `2026: SYBB`. Last_3d insights op campagne- en accountniveau zijn leeg (0 spend, 0 impressions).
- **Tweede account** (`act_1489853856181844`): geen actieve campagnes.
- **`act_607231713057715`**: dit token heeft **geen toegang** tot dit account (toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`). Overgeslagen. Als dit account nog relevant is, moeten de token-permissies hersteld worden.

De kill-regels (Link CTR / CPC link) en de 70-20-10 classificatie zijn niet toegepast: er is geen live performance data. PostHog was niet nodig omdat er geen ad-traffic is om tegen af te zetten.

**De enige echte actie voor jou:** de `2026: SYBB` campagne staat sinds 19 april op PAUSED. Zolang die uit staat levert deze dagelijkse run niks op. Wil je SYBB heractiveren zodat de optimalisatie weer kan draaien? Zo niet, dan kunnen we de auto-optimize run tijdelijk stilzetten tot er weer een campagne live is.

Alleen de Meta Ads MCP is gebruikt, geen Google MCPs, en er is niet naar de Google Sheet tracker geschreven.
