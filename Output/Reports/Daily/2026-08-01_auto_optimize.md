Rapport staat in `Output/Reports/Daily/2026-08-01_auto_optimize.md`, gecommit en gepusht.

## Auto-Optimize, 1 augustus 2026

**Nul automatische acties.** Alle 5 campagnes in `act_567892422940728` staan PAUSED. Insights over `last_3d`, `last_30d` en `last_90d` geven allemaal een lege dataset. Laatste spend was 20 april, 103 dagen geleden. Er is geen ad om te pauzeren en geen data om tegen de drempels te toetsen.

**Twee dingen die je moet weten:**

**1. Het tweede account is niet bereikbaar.** De command noemt `act_607231713057715`, maar de Pipeboard token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844` (dat laatste is leeg). Als dat account echt mee moet, moet de token-scope uitgebreid worden.

**2. De link-metrics herberekening levert wél iets op.** Ik heb de laatst bekende periode opnieuw doorgerekend op link clicks in plaats van all-clicks, per adset. Dat verandert het beeld:

| Ad set | Link CTR | CPC (link) | Spend |
|--------|---------:|-----------:|------:|
| BATCH 2: Expertise & POC (origineel) | 4,8% | €0,15 | €1.463,49 |
| 4x Kopie | 1,1 tot 1,3% | €0,81 tot €1,22 | €919,81 |
| SYBB test set STATISCH | 0,7% | €0,91 | €101,74 |

Identieke creatives, 4x betere Link CTR en 8x lagere CPC in het origineel. De duplicatie kostte grofweg 5.800 link clicks aan gemiste volume.

De STATISCH adset (Link CTR 0,7%) zou de nieuwe kill-regel hebben getriggerd. Op all-clicks CTR (1,03%) was hij er doorheen geglipt. De drempelherziening van 13 april doet dus wat hij moet doen.

**Gat in de regelset:** Kopie 1 verbrandde €521,56 op een CPC (link) van €1,22 zonder ooit gepauzeerd te worden, omdat hij de 500 link clicks nooit haalde. Ik stel een tweede regel voor: CPC (link) > €0,80 na 150 link clicks. Dat had €340 bespaard op die ene adset.

**Zes voorstellen staan in het rapport, wachtend op goedkeuring.** Nummer 1 blokkeert de rest: de corrupte pixelwaarde (€21.386 per aankoop in Kopie 3) moet gefixt voordat er budget in gaat. Ik heb bewust geen nieuwe creative-varianten uitgeschreven, want die test je nu tegen een funnel die 12.262 clicks omzette in 6 aankopen. Zeg het als je ze toch wilt.

Alleen Meta Ads MCP gebruikt. Geen Google MCPs, niet naar de Tracker Sheet geschreven. PostHog heb ik niet bevraagd omdat er geen ad-data was om tegen te cross-referencen, maar dat is wel de meest waardevolle vervolgstap gezien die 0,05% click-to-purchase.
