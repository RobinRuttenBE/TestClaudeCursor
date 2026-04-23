# Auto-Optimize Rapport, 2026-04-23

Run tijd: 2026-04-23 (dagelijkse auto-optimize, 3-daagse window)
Data-window: 2026-04-20 t/m 2026-04-22 (last_3d)
Bron: Meta Ads MCP (Pipeboard). PostHog niet geraadpleegd (geen actieve ads, landing page performance niet relevant voor deze run). Google MCPs expliciet uitgesloten.

## Account-status

| Account | Status | Actieve campagnes |
|---|---|---|
| act_567892422940728 (Sempertex Ad Account) | Toegankelijk | 0 actief, 5 PAUSED |
| act_1489853856181844 | Toegankelijk | 0 actief |
| act_607231713057715 | Geen token-toegang | n.v.t. |

Conclusie: er zijn geen live ads om te optimaliseren op dit moment.

## Automatische acties uitgevoerd (Niveau 1)

**Geen ads gepauzeerd.** Alle campagnes in act_567892422940728 staan al op PAUSED. De meest recente activiteit ("2026: SYBB - Kopie", campaign_id 120243293329420239) is handmatig gepauzeerd op 2026-04-20 en draait sindsdien niet meer.

Kill-regel check op de tail-data (informatief, niet uitvoerend):

| Ad | Impressions | Link clicks | Link CTR | CPC (link) | Kill-regel? |
|---|---|---|---|---|---|
| H11, B3, CTA5 | 1.972 | 33 | 1,7% | €0,85 | Nee (Link CTR > 0,8%, clicks < 500) |
| H13, B3, CTA5 | 1.517 | 25 | 1,6% | €1,26 | Nee (Link CTR > 0,8%, clicks < 500) |
| H12, B3, CTA5 | 798 | 17 | 2,1% | €1,07 | Nee (< 1.000 imp, geen kill-regel toepasbaar) |

Geen ad triggert een automatische pauze. De CPC (link) bij H13 en H12 is boven €1,50... correctie: is respectievelijk €1,26 en €1,07, dus onder de drempel van €1,50. Bovendien onvoldoende link clicks (< 500) om de CPC-kill-regel toe te passen.

## Waarschuwingen

| Ad | Signaal | Waarde | Drempel | Actie aanbevolen |
|---|---|---|---|---|
| H13, B3, CTA5 | Dure reach | CPM €20,80 | > €15 | Audience verbreden of vervangen |
| H12, B3, CTA5 | Dure reach | CPM €22,74 | > €15 | Audience verbreden of vervangen |

Geen creative fatigue (alle frequencies onder 1,30). Lifetime-CTR vergelijking niet uitgevoerd in deze run (3-daagse tail tegen een verder PAUSED account heeft geen baseline).

## 70-20-10 Classificatie

Niet van toepassing: er zijn 0 actieve ads en 0 live budget om te herverdelen.

Ter referentie, als "2026: SYBB - Kopie" wordt heropend, zouden de drie laatste ads bij de link-metrics als volgt classificeren (richtlijn, conform TODO in het command over kalibratie van link-drempels):

| Ad | Link CTR | CPC (link) | Checkouts | Proxy-ROAS (initiate_checkout) | Richtlijn-klasse |
|---|---|---|---|---|---|
| H11, B3, CTA5 | 1,7% | €0,85 | 1 (€350) | 12,4x | Core/Emerging grens |
| H12, B3, CTA5 | 2,1% | €1,07 | 1 (€350) | 19,3x | Emerging (< 1.000 imp, data dun) |
| H13, B3, CTA5 | 1,6% | €1,26 | 0 | 0x | Emerging (geen conversie, dure CPM) |

Opmerking: "purchase" is niet geregistreerd in deze window, `initiate_checkout` is als proxy gebruikt. Echte ROAS ligt lager zodra de checkout drop-off wordt meegenomen.

## Voorstellen (Niveau 2, wacht op goedkeuring)

**1. Besluit over "2026: SYBB - Kopie" (campaign_id 120243293329420239)**
De campagne staat PAUSED sinds 2026-04-20. In de 3 dagen daarvoor: €77,85 spend, 75 link clicks, 2 initiate checkouts (€700 waarde), Link CTR 1,7%, CPC (link) €1,04.
Voorstel: bepaal of deze campagne heropend wordt. Zo ja, doe dit selectief (zie voorstel 2), niet als geheel.

**2. Selectieve ad-heractivering**
Bij heropening, alleen de twee ads met bewezen conversie activeren:
- H11, B3, CTA5 (ad_id 120243293329410239), CPM €14,27 (onder drempel), 1 checkout
- H12, B3, CTA5 (ad_id 120243293329700239), CPM €22,74 (boven drempel, monitoren), 1 checkout

H13, B3, CTA5 (ad_id 120243293329660239) blijft PAUSED: 0 checkouts op 1.517 imp, CPM €20,80, geen duidelijk signaal dat deze combinatie werkt.

**3. CPM verlagen voordat Batch 2 opnieuw opengaat**
Account-CPM over last_3d: €18,16 (boven €15 drempel). Ad-set "BATCH 2: Expertise & POC - Kopie" is mogelijk te smal. Voorstel: audience verbreden (lookalike van checkouts of bredere interest-stack) voordat je Batch 2 weer opendraait, anders betaal je premium voor dezelfde 1.600-reach buckets.

**4. Status van de originele "2026: SYBB" campagne (120239435987290239)**
De originele SYBB campagne (dagbudget €100) is 2026-04-19 gepauzeerd, vlak voordat de "Kopie" 2026-04-19 startte en op 2026-04-20 werd gepauzeerd. Voorstel: bepaal welke van de twee de basis wordt voor de volgende push, zodat je niet twee parallelle sporen houdt.

**5. Batch 1 vs Batch 2**
De last_3d data toont alleen Batch 2 ads (H11/H12/H13). Controleer in /ads-report of Batch 1 (H1-H10) klaar staat en of die als eerste heractiveert, gezien de hogere CPC (link) van Batch 2.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

## Appendix: bron-data

Ad-insights over 2026-04-20 t/m 2026-04-22, level=ad, account act_567892422940728:

| Ad | Adset | Imp | Link clicks | Link CTR | Spend | CPC (link) | CPM | Freq | Checkouts | Checkout-waarde | All Clicks CTR | CPC (all) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | Kopie 1 | 1.972 | 33 | 1,7% | €28,14 | €0,85 | €14,27 | 1,19 | 1 | €350 | 2,8% | €0,51 |
| H13, B3, CTA5 | Kopie 3 | 1.517 | 25 | 1,6% | €31,56 | €1,26 | €20,80 | 1,17 | 0 | €0 | 2,0% | €1,02 |
| H12, B3, CTA5 | Kopie 2 | 798 | 17 | 2,1% | €18,15 | €1,07 | €22,74 | 1,26 | 1 | €350 | 4,1% | €0,55 |
| **Totaal** |  | **4.287** | **75** | **1,7%** | **€77,85** | **€1,04** | **€18,16** | **1,34** | **2** | **€700** | **2,8%** | **€0,65** |

Methodologie:
- Link CTR = actions.link_click / impressions × 100 (NIET Meta's `ctr` veld)
- CPC (link) = spend / actions.link_click (NIET Meta's `cpc` veld)
- CPM en Frequency komen direct uit de Meta API
- All Clicks CTR en CPC (all) ter referentie opgenomen, worden NIET gebruikt voor kill-regels

Tool-notities:
- get_insights op campaign-level voor campaign_id 120239435987290239 gaf lege data (campagne PAUSED sinds 2026-04-19, geen spend in last_3d). Verwacht.
- get_insights op campaign-level voor campaign_id 120243293329420239 gaf een MCP proxy-fout ("Anthropic Proxy: Invalid content from server"). Workaround: account-level insights met level=ad gebruikt, die data is compleet.
- get_insights op account-level voor act_567892422940728 gaf totalen consistent met de som van de 3 ads (4.287 imp, 75 link clicks, €77,85 spend), bevestigt dat er geen verborgen ads zijn.
