Het rapport staat in `Output/Reports/Daily/2026-09-21_auto_optimize.md`, gecommit en gepusht (3938a57c). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. De ad-level call over de laatste 3 dagen gaf nul rijen, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan. Achttiende dag zonder levering.

**Meta was live bereikbaar.** De weeklimiet is vannacht gereset. Ik heb de kans gebruikt om de per-ad Link CTR en CPC (link) over 30 dagen vers op te halen en als markdown-tabel op te slaan, zoals gisteren afgesproken. Verbruik vandaag over de drie rapporten: 6 van 30 calls.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies van 14 tot en met 21 september. Op de distributeurspagina alleen organisch verkeer: 2 inzendingen (Letland 18 september, Malta 20 september) en opnieuw een formulierfout op 20 september.

**Wat de echte link-metrics laten zien.** Link CTR ligt gemiddeld op 55% van de all-clicks CTR en CPC (link) is 1,8 keer hoger dan CPC (all). Op link-metrics haalt alleen Statisch 2 (SWE) de Core-drempel (Link CTR 2,2%, CPC link €0,45). Statisch 1 (LIT) zou met 0,6% Link CTR mechanisch gepauzeerd worden, terwijl het op kosten per inzending (€36,06) een van de drie beste ads is. Beide SWE-video's vallen op link-metrics én conversie af.

**Waarschuwingen** gelden bij herstart: frequency 3,97 op LIT, CPM boven €15,00 op beide SWE-video's, en Statisch 2 (LIT) met goedkope clicks maar €63,63 per inzending.

**Zeven voorstellen wachten op je goedkeuring.** De eerste zes zijn bekend, nu opnieuw uitgewerkt op link-metrics. Nummer 7 is nieuw:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met concrete bedragen per ad en de drie zwakste ads naar €0,00.
2. Drie hook-varianten (Statement, Label, Vraag) op de Statisch 2 (SWE) visual, Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, Statisch 1 (LIT) naar 25-65 zonder desktop, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Funnel en pixel fix vóór herstart.
6. Eén gedeeld Meta-extract per dag.
7. Nieuwe 70-20-10 drempels gekalibreerd op de echte link-cijfers, zodat de indeling overeenkomt met de conversie-ranking. Dit sluit de TODO in het command.

Geef aan welke nummers ik mag uitvoeren. Als ik morgen de huidige ad-copy mag ophalen voor voorstel 2, kost dat één extra Meta-call.
