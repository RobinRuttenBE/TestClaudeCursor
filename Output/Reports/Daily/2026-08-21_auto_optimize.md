Rapport staat in `Output/Reports/Daily/2026-08-21_auto_optimize.md`, gecommit en gepusht (`113f8d8d`).

## Kort

**Nul automatische acties, en dat klopt.** Alle vijf campagnes staan op PAUSED, `last_3d` en `last_7d` geven een lege dataset terug. Geen enkele ad haalt de minimumdrempel van 1.000 impressions of 500 link clicks, dus geen kill-regel kan vuren. Alleen Meta Ads (Pipeboard) en PostHog gebruikt, geen Google MCP, niets naar de tracker Sheet.

De MCP connector stond op "requires authentication", maar de geconfigureerde token werkt wel via directe JSON-RPC calls. Dat heb ik als memory vastgelegd.

## Wat de analyse op lifetime link metrics wél opleverde

**Het is de adset, niet de hook.** De openstaande vraag uit je ads rapport van vanochtend is beantwoord: H13 kreeg €0,07 per klik in de originele adset `BATCH 2: Expertise & POC`, en €1,06 in `Kopie 3`. Dat patroon geldt voor alle vier de hooks die in beide draaiden, telkens in het voordeel van het origineel: H13 15,1x, H15 5,4x, H11 4,1x, H12 1,4x.

**Maar de dure adset is de enige die verkoopt.** De vier verifieerbare SYBB aankopen komen uit H11 in Kopie 1, tegen €1,22 per klik. De goedkope adset leverde 5.808 link clicks en nul aankopen. H13 alleen: 6.342 link clicks, 4.063 landing page views, nul aankopen. Sturen op CPC (link) zou je precies de verkeerde adset laten kiezen.

**Je account-ROAS is 2,7x, niet 11,5x.** Eén ad (H13 in Kopie 3) rapporteert €21.386,75 per order. Haal je die eruit, dan blijft €13.026,75 op €4.867,46 over. De andere vier converterende ads zijn wel plausibel (€1.180 tot €208 per order).

## Twee dingen die aandacht vragen

**Drie ads staan op ACTIVE onder de paused campagne "2026: SYBB - Kopie".** Zet je die campagne aan, dan starten H13, H12 en H11 meteen, en dat zijn precies de drie duurste ads van het account. Pauzeer ze eerst.

**Je kill-regel zou je op één na beste ad slopen.** "Ad 1 - Eind Aug" heeft een Link CTR van 0,7% en zou automatisch gepauzeerd worden. Diezelfde ad draait op €0,23 per link click met 6 aankopen en 6,4x ROAS. Ik stel voor de regel voorwaardelijk te maken: Link CTR < 0,8% **én** CPC (link) > €0,50 **én** nul aankopen. Dan overleeft Eind Aug en sneuvelen "SYBB w/ Semp (BLACK)" en "Ad 1 - nieuwe doelgroep" alsnog.

Vijf voorstellen staan in het rapport, geen daarvan uitgevoerd. Geef door welke nummers je wil.
