Het rapport staat in `Output/Reports/Daily/2026-09-26_auto_optimize.md`, gecommit en gepusht (e430fc9a). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt live nul betaalde sessies in het kill-venster van 23 t/m 25 september en ook vandaag tot 12:30. Er zijn geen `update_ad` calls gedaan. Drieëntwintigste dag zonder levering.

**Meta-weeklimiet zit nog vol.** De enige call kreeg `weekly_limit_exceeded` (30 van 30, reset maandag 28 september 00:00 UTC). De run draait daarom op de campagnestatus uit het ads-rapport van gisteren plus de per-ad link-tabel uit het live extract van 24 september. Dat is veilig zolang er geen levering is.

**Twee dingen om te weten:**

- **Archiefprobleem blijft.** De bestanden van 25 september bevatten op schijf alleen de chatsamenvatting. De volledige tabel stond wel in de commit, en daar heb ik hem vandaan gehaald. Het bestand van vandaag is met grep gecontroleerd en bevat de tabel.
- **30d-venster verschuift morgen.** Vanaf 27 september valt de eerste leveringsdag (27 augustus) uit het venster, dus de LIT-cijfers gaan dalen zonder dat er iets gebeurde. Maandag trek ik een extract met vast datumbereik 27 augustus t/m 4 september.

**Funnel /become-a-distributor:** geen inzending sinds Malta op 20 september. Eén formulierstart op 25 september zonder inzending. Organisch 2 tot 6 sessies per dag op de pagina.

**Zeven voorstellen wachten op je goedkeuring**, ongewijzigd sinds 22 september:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met bedragen per ad en beide SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout (15,5%) en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten. Dit blijft urgent: de limiet zat vrijdag al vol en houdt zaterdag en zondag alle Meta-data tegen.
7. Nieuwe 70-20-10 drempels op link-metrics.

Geef aan welke nummers ik mag uitvoeren.
