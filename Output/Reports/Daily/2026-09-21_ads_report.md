## Meta Ads Rapport, 21 september 2026

**Meta was vandaag weer live bereikbaar.** De weeklimiet van Pipeboard is vannacht gereset; de directe JSON-RPC route gaf op de eerste call direct data. Drie Meta-calls gedaan (campaign-level 30d, ad-level 30d, campagnelijst) en vier PostHog-queries. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Achttiende dag zonder levering. PostHog bevestigt: laatste betaalde sessies op 9 september (2 nalopers), nul sinds.

**Overzicht per campagne (last 30d, 22 aug t/m 20 sep, live)**

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 events in 32 sessies (23 via ad, 9 zonder UTM) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd (Meta pixel telt structureel te weinig). SWE staat vandaag op 7 inzendingen via ad in plaats van 8: de sessie-join telt unieke sessies, het eerdere getal telde submit-events. Het all-in totaal (35 events) is ongewijzigd.

De overige 5 campagnes (2026: SYBB, 2026: SYBB - Kopie, drie Nozzle Up campagnes uit 2025) staan al maanden op PAUSED en hebben nul spend in het venster.

**Per ad (last 30d, live Meta plus PostHog sessies)**

| Ad | Spend | Impr. | CTR | CPC | CPM | Freq. | Link clicks | CPC (link) | Meta leads | PostHog sessies | Inzendingen | Conv. | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 2,4% | €0,32 | €7,72 | 1,90 | 242 | €0,61 | 3 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | €143,74 | 17.267 | 1,4% | €0,58 | €8,32 | 2,52 | 179 | €0,80 | 4 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | €144,24 | 28.434 | 1,0% | €0,49 | €5,07 | 2,91 | 163 | €0,88 | 3 | 134 | 4 | 3,0% | €36,06 | |
| Statisch 2 (LIT) | €127,25 | 26.146 | 2,4% | €0,20 | €4,87 | 2,37 | 297 | €0,43 | 1 | 292 | 2 | 0,7% | €63,63 | |
| Video 1 (SWE) | €126,75 | 8.299 | 2,9% | €0,53 | €15,27 | 2,05 | 139 | €0,91 | 0 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM |
| Video 2 (SWE) | €127,00 | 7.441 | 2,5% | €0,69 | €17,07 | 2,02 | 114 | €1,11 | 1 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | €125,36 | 10.262 | 2,7% | €0,45 | €12,22 | 2,15 | 157 | €0,80 | 2 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | €128,13 | 13.265 | 4,0% | €0,24 | €9,66 | 1,97 | 286 | €0,45 | 5 | 256 | 3 | 1,2% | €42,71 | |

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15). Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27 boven drempel, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Campagne LIT**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives voor herstart.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%) en laagste kosten per inzending. Aanbeveling: behouden, niet mechanisch pauzeren op CPC.
- **Statisch 2 (LIT)**: geen drempel geraakt, maar 0,7% conversie en €63,63 per inzending bij de goedkoopste clicks. Aanbeveling: nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06
- Beste ROAS: n.v.t. (lead-campagnes)

**Funnel /become-a-distributor (30d, live PostHog):** 1.699 pageviews, 141 formulierstarts, 22 formulierfouten, 35 inzendingen. Van start naar inzending komt 24,8% door. Sinds de pauze kwamen 2 organische inzendingen binnen (Letland 18 september, Malta 20 september), beide zonder UTM. Op 20 september ook 1 formulierfout: het formulier blijft dus haperen, ook zonder betaald verkeer.

**Samenvatting**

- Totaal spend: €1.069,38 (periode: last 30 days, 22 augustus t/m 20 september)
- Beste performer: Video 2 (LIT), 3,5% sessie-naar-inzending en €28,75 per inzending ondanks een CPC boven drempel
- Slechtste performer: Video 1 (SWE), duurste reach van alle ads en nul inzendingen
- Aanbeveling (70-20-10) bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten toevoegen. Eerst het formulierlek (75% valt af tussen start en inzending) dichten vóór er weer budget op gaat.

**Wijzigingen t.o.v. gisteren:** Meta-cijfers zijn vandaag live geverifieerd en identiek aan het extract van 16 september. Per-ad tabel nu als markdown opgeslagen zodat latere runs erop kunnen terugvallen. Verder geen nieuwe inzendingen of betaald verkeer.

**Google Sheet:** overgeslagen op verzoek. Rapport alleen lokaal opgeslagen.

---
Databronnen: Pipeboard Meta Ads (directe JSON-RPC route, 3 calls, account act_567892422940728), PostHog STX EU project 149694 (directe REST-route, 4 HogQL queries). Gegenereerd 21 september 2026.
