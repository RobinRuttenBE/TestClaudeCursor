Klaar. Het rapport staat opgeslagen in `Output/Reports/Daily/2026-06-26_auto_optimize.md` en is gecommit + gepusht.

## Uitkomst van deze run

**Er is niets te optimaliseren: alle campagnes staan op PAUSED.**

Wat ik vond bij het ophalen van de data (alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Sheet geschreven):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | **0** — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | 0 |
| `act_607231713057715` | ❌ geen toegang | n.v.t. |

Twee dingen die ik wil aanstippen:

1. **Het in het command genoemde alternatieve account `act_607231713057715` is niet toegankelijk** met de huidige token. De token geeft toegang tot `act_567892422940728` en `act_1489853856181844`. Ik heb dat tweede toegankelijke account meegenomen, ook leeg.

2. **De hoofdcampagne 2026: SYBB (dagbudget €100,00) staat sinds 19 april op PAUSED.** Dit sluit aan op het SYBB dagrapport van gisteren.

Omdat er geen live delivery is, zijn de kill-regels (Link CTR < 0,8%, CPC (link) > €1,50) niet getriggerd, is er geen 70-20-10 classificatie mogelijk en zijn er geen data-gedreven voorstellen.

**Wil je de SYBB campagne opnieuw activeren?** Zo ja, dan draait deze auto-optimize flow bij de volgende run op echte data. Zolang alles gepauzeerd blijft, kan de dagelijkse run worden overgeslagen.
