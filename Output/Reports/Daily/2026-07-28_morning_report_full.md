# Morning Report — 2026-07-28

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Meta data is complete. Let me add a quick PostHog landing page check for context.
API Error: Connection closed mid-response. The response above may be incomplete.

---

Two important findings emerging. Let me verify both.
API Error: Connection closed mid-response. The response above may be incomplete.

---

Rapport staat in `Output/Reports/Daily/2026-07-28_auto_optimize.md`, gecommit en gepusht.

## Wat ik vond

**Er is niets te optimaliseren: alle campagnes staan gepauzeerd.** Alle 5 campagnes in `act_567892422940728` zijn PAUSED, spend over de laatste 3 dagen is €0,00, en er is zelfs over de afgelopen 90 dagen geen enkele impressie geregistreerd. Laatste activiteit in het account was 20 april 2026. Er zijn dus 0 ads gepauzeerd, en de 70-20-10 classificatie is niet toepasbaar.

Drie dingen die wel opvielen:

1. **De scheduled run is stuk.** De rapporten van 26 en 27 juli bevatten alleen `Not logged in · Please run /login`. De automatisering draait dus al twee dagen zonder geldige sessie, en had ook niets kunnen pauzeren als er wél actieve ads waren geweest. Dit lijkt me de belangrijkste fix.

2. **`act_607231713057715` is niet bereikbaar.** De Pipeboard token geeft alleen toegang tot `act_567892422940728` (Sempertex) en `act_1489853856181844` (AmbitionAvenue, leeg). Het account uit het command staat niet in de token-scope. Ik kon dat account dus niet checken.

3. **De purchase values in de SYBB campagne kloppen niet.** €44.247 op 6 purchases, en €86.100 op 6 registraties. Als de campagne herstart op value optimisation, stuurt Meta op ruis. Ik heb de ROAS van 17,8x in het rapport als onbetrouwbaar gemarkeerd.

Ter voorbereiding op een herstart heb ik de lifetime performance per campagne op link-basis uitgerekend (`actions.link_click`, niet Meta's all-clicks velden). SYBB is de duidelijke winnaar: 3,7% Link CTR bij €0,23 CPC (link) over 297k impressies. Ik heb daarnaast een voorstel opgenomen voor link-gebaseerde 70-20-10 drempels, want de huidige waarden zouden de helft van de historische campagnes als Core classificeren.

Twee kanttekeningen bij het committen: git had geen identity geconfigureerd, dus ik heb per-commit de auteur van de vorige auto-sync commits gebruikt (`Robin Rutten <robinrutten@Robins-MacBook-Air.local>`) in plaats van global config aan te passen. En omdat er al veel bestanden gestaged stonden van een onafgemaakte auto-sync, zijn die meegegaan in dezelfde commit (26 bestanden, vooral logs en de rapporten van 26 en 27 juli).

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
