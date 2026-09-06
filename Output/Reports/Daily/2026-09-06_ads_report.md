# Meta Ads Rapport, 6 september 2026

**Bronnen deze run:** Meta Ads via Pipeboard (geprobeerd, geblokkeerd) en PostHog (directe REST call op project STX EU, de claude.ai connector sloot de verbinding). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

## Datastatus: Meta Ads vandaag niet bereikbaar

Geen enkele route naar de Meta Ads data werkte vandaag:

| Route | Resultaat |
|---|---|
| Pipeboard MCP (`claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads`) | "requires authentication", niet te herstellen in een non-interactieve sessie |
| Pipeboard directe JSON-RPC (token pk_0c38…) | "You have reached the weekly limit for AI tool executions on your Free plan" |
| Facebook token uit de Instagram MCP config | Verlopen (code 190, "user logged out"), zoals sinds 24 augustus bekend |

De Meta-cijfers hieronder zijn daarom de **laatst bekende stand van 4 september** (uit het rapport van 5 september, periode 27 augustus t/m 4 september). PostHog is wel live en bevestigt dat er sinds de pauze vrijwel geen betaald verkeer meer binnenkomt.

## Wat PostHog vandaag laat zien (live data)

Betaalde sessies op `/en_GB/become-a-distributor` (entry utm_source=facebook) en formulier-inzendingen per dag:

| Dag | Betaalde sessies | Alle sessies | Inzendingen |
|---|---|---|---|
| 28 aug | 254 | 255 | 6 |
| 29 aug | 216 | 218 | 4 |
| 30 aug | 124 | 125 | 6 |
| 31 aug | 160 | 162 | 5 |
| 1 sep | 205 | 210 | 1 |
| 2 sep | 156 | 161 | 3 |
| 3 sep | 210 | 212 | 1 |
| 4 sep | 58 | 63 | 1 |
| 5 sep | 0 | 2 | 0 |
| 6 sep (tot 08:00 UTC) | 2 | 4 | 0 |

Totaal 27 augustus t/m 4 september: 1.406 betaalde sessies en 33 inzendingen (2,3% sessie-naar-inzending). Sinds 5 september: 0 inzendingen.

**Let op:** de 2 betaalde sessies van vandaag (04:53 en 06:31 UTC) hebben beide `utm_campaign=wholesaler_se`, `utm_content=video_01`. Dat is de ad die op 4 september gepauzeerd is en die volgens het rapport van gisteren niet meer geactiveerd zou worden. Twee dagen na een pauze is nalevering door Meta ongebruikelijk. Check in Ads Manager of Video 1 (SWE) per ongeluk weer aanstaat. Met Meta-toegang had ik dit direct kunnen verifiëren.

SYBB: 0 sessies met utm_source=meta of utm_campaign=sybb in de laatste 30 dagen, consistent met de campagne `2026: SYBB` die sinds 19 april gepauzeerd is.

## Overzicht per campagne (laatst bekende Meta-stand, 27 aug t/m 4 sep)

| Campagne | Status (4 sep) | Spend | Impressions | Link clicks | Link CTR | Link CPC | CPM | Freq. | Leads Meta | Inzendingen PostHog | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,13 | 90.887 | ~880 | 1,0% | €0,64 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | ~695 | 1,8% | €0,73 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 0 | 0 | n.v.t. |
| **Totaal** | | **€1.069,37** | **130.154** | **~1.575** | **1,2%** | **€0,68** | **€8,22** | **3,73** | **19** | **33** | **€32,41** |

Er is vandaag geen nieuwe spend om aan deze tabel toe te voegen: PostHog laat zien dat het verkeer op 5 september volledig is gestopt. Als Video 1 (SWE) toch weer draait, klopt dat vanaf vandaag niet meer. Het account `act_607231713057715` uit het command bestaat niet; het tweede account is AmbitionAvenue zonder campagnes.

## Underperformers (stand 4 sep, drempels CPC €0,50 / CTR 1% / freq. 3,5 / CPM €15)

- **Video 1 (SWE)**: €126,75 spend, 0 inzendingen, CPM €15,27 (boven €15). Aanbeveling: niet opnieuw activeren. Vandaag toch 2 sessies via deze ad, dus eerst checken of hij uitstaat.
- **Video 2 (SWE)**: CPM €17,07, link CPC €1,11, €63,50 per inzending. Aanbeveling: niet terugzetten bij herstart.
- **Statisch 1 (LIT)**: Link CTR 0,6% (onder 1%), maar beste sessie-naar-inzending ratio binnen LIT (3,2%). Aanbeveling: alleen terug met een nieuwe eerste zin, in de 10% experimentbucket.
- **Wholesaler (LIT) campagne**: frequency 3,97 (boven 3,5) door vier ad sets op dezelfde audience. Aanbeveling: ad sets samenvoegen naar 2 voor de herstart.
- **Beide campagnes**: link CPC boven €0,50 (€0,64 en €0,73). Voor een B2B lead-campagne acceptabel zolang de kosten per inzending onder €35 blijven, wat in de laatste drie draaidagen niet meer lukte (€67).

## Top performers (stand 4 sep)

- **Beste CTR**: Statisch 2 (SWE), 2,2% link CTR.
- **Laagste CPC**: Statisch 2 (LIT), €0,43 link CPC.
- **Beste ROAS**: niet meetbaar, lead-campagne zonder purchase value. Goedkoopste inzendingen: Video 2 (LIT) €28,75 en Video 1 (LIT) €29,38.
- **Meeste betaalde sessies per ad (PostHog)**: Statisch 2 (LIT) 290, Statisch 2 (SWE) 255, Video 1 (LIT) 248.

## Samenvatting

- **Totaal spend**: €1.069,37 over 27 augustus t/m 4 september (laatst bekende stand). Geen spend op 5 september, vandaag onbevestigd.
- **Beste performer**: Statisch 2 (SWE en LIT), hoogste CTR, laagste CPC en meeste sessies.
- **Slechtste performer**: Video 1 (SWE), duurste reach en nul inzendingen.
- **Aanbeveling (70-20-10, ongewijzigd, wacht op goedkeuring)**:
  1. Eerst tracking fixen: Meta zag 19 leads, PostHog 33. Meta optimaliseert nu op de helft van het signaal.
  2. 70% budget op Statisch 2 (SWE), Video 1 (LIT) en Statisch 2 (LIT). Richtbudget €140/dag.
  3. 20% op hetzelfde Statisch 2 visual met drie nieuwe hooks per land. Alle 8 ads gebruikten dezelfde tekst.
  4. 10% op Statisch 1 (LIT) met nieuwe eerste zin.
  5. LIT ad sets samenvoegen zodat de frequency onder 3,5 blijft.

## Google Sheet

Overgeslagen op verzoek. Geen write naar "Meta Ads Tracker".

## Acties om de Meta-data morgen weer te krijgen

1. **Pipeboard**: de directe route zit op de weeklimiet van het gratis plan. Upgrade naar Pro (pipeboard.co/pricing) of wacht tot de weekteller reset. Dit raakt ook het morning report en auto-optimize.
2. **Pipeboard MCP**: in een interactieve sessie `/mcp` draaien en `claude.ai Pipeboard Meta Ads` opnieuw autoriseren, dan gebruikt het rapport de MCP in plaats van de directe call en telt het mogelijk niet mee voor dezelfde limiet.
3. **Fallback**: een nieuw Meta System User token met `ads_read` in de config zetten, dan kan het rapport rechtstreeks naar de Marketing API als Pipeboard uitvalt.

## Funnel data

Funnel data na de inzending (gesprek gepland, distributeur actief, eerste order) zit niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.
