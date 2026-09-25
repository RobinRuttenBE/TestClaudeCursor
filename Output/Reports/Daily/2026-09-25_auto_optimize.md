Het rapport staat in `Output/Reports/Daily/2026-09-25_auto_optimize.md`, gecommit en gepusht (1e59cf9d). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt live nul betaalde sessies van 18 t/m 25 september. Er zijn geen `update_ad` calls gedaan. Tweeëntwintigste dag zonder levering.

**Meta-weeklimiet zit vol.** De enige call kreeg `weekly_limit_exceeded` (30 van 30, reset maandag 28 september). Het ads-rapport van 08:17 vanochtend kon nog 3 calls doen, dus tussen woensdag en vrijdag ging het verbruik van circa 6 naar 30. De run draait daarom op de campagnestatus uit dat ads-rapport plus de per-ad link-tabel uit het live extract van 24 september. Dat is veilig: zonder levering veranderen de per-ad cijfers niet, en PostHog bevestigt dat.

**Archiefprobleem blijft.** Het bestand van 24 september bevat op schijf opnieuw alleen de chatsamenvatting. De volledige tabel stond wel in de commit, en daar heb ik hem vandaan gehaald. Het bestand van vandaag is met grep gecontroleerd en bevat de tabel.

**Funnel /become-a-distributor:** vijfde dag op rij zonder formulierstart. Geen inzending sinds Malta op 20 september. Organisch 3 tot 6 sessies per dag op de pagina.

**Zeven voorstellen wachten op je goedkeuring**, ongewijzigd sinds 22 september:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met bedragen per ad en beide SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout (15,6%) en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten. Dit is nu urgent: de limiet zat vrijdag al vol.
7. Nieuwe 70-20-10 drempels op link-metrics.

Geef aan welke nummers ik mag uitvoeren.
