# Morning Report — 2026-08-02

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

I'll pull the Meta Ads data. Let me load the Pipeboard MCP tools first.
API Error: Connection closed mid-response. The response above may be incomplete.

---

Meta MCP leeft weer. Ik zoek het account ID.
API Error: Connection closed mid-response. The response above may be incomplete.

---

Rapport staat in `Output/Reports/Daily/2026-08-02_auto_optimize.md`, gecommit en gepusht.

## Kernpunt: er viel niets te optimaliseren

Alle vijf campagnes in act_567892422940728 staan op PAUSED. Nul impressions en EUR 0,00 spend in de laatste 3 dagen, en ook in de laatste 30 dagen. De kill-regels hebben geen enkele ad om op te vuren, dus **0 ads gepauzeerd**. Laatste levering was April 2026, het account staat ruim drie maanden donker.

## Wat de historie wel laat zien

Campagne 2026: SYBB, EUR 2.485,04 over 297.174 impressions. Lifetime Link CTR 3,7% bij CPC (link) EUR 0,23.

Het interessante zit in het maandverloop:

| Maand | Spend | Link CTR | CPC (link) | CPM |
|---|---|---|---|---|
| March | EUR 1.323,83 | 5,1% | EUR 0,14 | EUR 7,00 |
| April | EUR 1.059,47 | 1,1% | EUR 1,02 | EUR 11,54 |

April brak weg, maar dat was CPM-gedreven, niet creative-gedreven. Dezelfde hooks (H11, H12, H13, H15) draaiden in de "Kopie" ad set op een CPM van EUR 10,13 tot EUR 13,51 tegen EUR 6,38 tot EUR 8,06 in de originele set. Zelfde creative, dubbele kostprijs. Dat is verzadiging van de audience, niet vermoeidheid van de creatives (frequency bleef overal onder 2,0).

## Drie dingen die aandacht vragen

1. **act_607231713057715 is niet bereikbaar.** Het Pipeboard-token meldt dat alleen act_1489853856181844 en act_567892422940728 zijn toegestaan. Dit account staat wel in het command. Checken op pipeboard.co/connections.

2. **De pixel-waarden kloppen niet.** 6 purchases met een waarde van 44.247, dus EUR 7.374 per aankoop. Er staat daarnaast een tweede purchase-waarde van 4,42 in dezelfde data. Zolang dit niet klopt is elke ROAS-beslissing waardeloos, inclusief de Core-regel op ROAS > 2x.

3. **H13 is een uitschieter die verificatie verdient.** 10,6% Link CTR bij EUR 0,07 CPC, ruim 2,6 keer boven de op een na beste ad. Maar slechts 64,1% van die link clicks werd een landing page view, dus circa 2.279 klikken kwamen nooit aan. Verifiëren voor je hierop opschaalt.

Mijn advies bij heropstart: originele BATCH 2 ad set terug met de vier Core ads, nieuwe of verbrede audience, en starten op EUR 30,00 per dag in plaats van de EUR 100,00 die nu klaarstaat. Nieuwe creatives op een verzadigde audience lossen het April-probleem niet op.

Voorstellen staan genummerd in het rapport, niets uitgevoerd zonder jouw akkoord. Het eerdere `/ads-report` van vandaag was overigens halverwege afgebroken op een API-fout, dus dit is de eerste run met echte data.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
