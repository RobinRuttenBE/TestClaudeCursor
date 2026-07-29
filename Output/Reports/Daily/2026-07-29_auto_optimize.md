Committed and pushed. Report saved to `Output/Reports/Daily/2026-07-29_auto_optimize.md`.

## Wat ik vond

**Er draait niets.** Alle 5 campagnes in `act_567892422940728` staan op PAUSED. Laatste spend was **April 2026**, 91 dagen geleden. Nul impressies en nul spend in de laatste 30 dagen. Geen ads gepauzeerd, want er is niets om te pauzeren.

Ik heb het rapport daarom omgebouwd tot een relaunch-briefing op basis van de laatste actieve periode (March/April, 9 ads, €2.383,30).

## De belangrijkste bevinding

De 70-20-10 drempels uit het command wijzen op deze data **exact de verkeerde kant op**:

| | "Core" volgens drempels | "Emerging" volgens drempels |
|---|---|---|
| Link clicks | 9.185 | 1.550 |
| Spend | €1.075,09 | €1.308,21 |
| **Aankopen** | **0** | **alle 6** |

De traffic-geoptimaliseerde ad set haalde 4,8% Link CTR voor €0,15 per click en leverde **nul omzet**. De conversie-ad set haalde 1,2% Link CTR voor €1,08 per click en leverde **alle 6 aankopen**. Het verschil zit in klikkwaliteit: 80 tot 88% van die clicks laadde de pagina echt, tegenover 60 tot 70% bij het goedkope verkeer.

Scherpste voorbeeld: dezelfde hook H13 deed 6.342 clicks à €0,07 met nul aankopen in de ene ad set, en 195 clicks à €1,06 met twee aankopen in de andere.

De TODO in het command over het herijken van die drempels is dus niet cosmetisch. Budget verschuiven naar Link CTR zou hier de omzet naar nul brengen. Ook goed om te weten: geen enkele ad zou door de huidige kill-regels geraakt zijn, maar H11 Kopie zat met €1,22 CPC (link) dicht bij de €1,50-grens en had 4 van de 6 aankopen.

## Twee dingen die je aandacht nodig hebben

1. **Pixel purchase values zijn corrupt.** 2 aankopen gerapporteerd als €42.773,50, 4 aankopen als €1.473,50. Ik heb daarom bewust geen ROAS berekend, dat zou verzonnen zijn. Dit is blokkerend voor elke omzetgestuurde beslissing.

2. **`act_607231713057715` is niet toegankelijk** met dit token (alleen `act_567892422940728` en `act_1489853856181844` zijn toegestaan). Als daar iets draait, is dat niet meegenomen. Het command noemt dat account wel als bron, dus dat gat blijft anders stilzwijgend bestaan.

PostHog bevestigt het beeld: de SYBB landing page doet ~2 bezoekers per dag. Wel merk ik op dat PostHog de webshop pas sinds 15 July 2026 volgt, dus cross-referencing met de Meta-historie is beperkt.

De 5 voorstellen in het rapport wachten op je goedkeuring, ik heb niets aan de campagnes gewijzigd.
