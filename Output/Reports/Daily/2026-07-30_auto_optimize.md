# Auto-Optimize Rapport, 30 July 2026

**Account:** Sempertex Ad Account (`act_567892422940728`)
**Periode geanalyseerd:** last_3d (27 t/m 30 July 2026)
**Databronnen:** Meta Ads MCP (Pipeboard). Geen Google MCPs gebruikt, niet naar de tracker Sheet geschreven.

---

## Samenvatting

**Er zijn geen actieve campagnes, ad sets of ads. Het account staat volledig stil.**

Nul impressions, nul spend en nul link clicks in de afgelopen 3 dagen. Ook over de afgelopen 90 dagen (1 May t/m 30 July) is er geen enkele delivery geweest. De laatste maand met spend was April 2026.

Daarmee zijn alle kill-regels, waarschuwingsregels en de 70-20-10 classificatie niet van toepassing. Er is niets om te pauzeren en niets om budget tussen te herverdelen.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Er zijn nul actieve ads, dus geen enkele kill-regel kon triggeren.**

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| (geen) | (geen actieve ads) | | | |

**Totaal gepauzeerd: 0 ads**

---

## Campagne status (alle campagnes in het account)

| Campagne | ID | Status | Daily budget | Laatst gewijzigd |
|---|---|---|---|---|
| 2026: SYBB | 120239435987290239 | PAUSED | €100.00 | 19 April 2026 |
| 2026: SYBB, Kopie | 120243293329420239 | PAUSED | geen | 20 April 2026 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | geen | 21 September 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70.00 | 15 September 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30.00 | 15 September 2025 |

Het account draait dus al ruim 3 maanden niet meer, sinds ongeveer 20 April 2026.

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| Account volledig inactief | 0 impressions over 90 dagen | Besluit nemen: heropstarten of bewust gepauzeerd laten |
| Ad account `act_607231713057715` niet bereikbaar | API token heeft geen toegang | Zie sectie Toegangsprobleem hieronder |
| Purchase-waardes in Meta lijken verkeerd geschaald | Zie sectie Data-kwaliteit | Pixel value configuratie controleren voor je ROAS als stuurmetric gebruikt |

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn nul actieve ads om te classificeren en nul actief budget om te verdelen.

**Budget mismatch:** Niet van toepassing, totaal actief budget is €0.00 per dag.

---

## Historische context: hoe stond SYBB erbij toen het werd gepauzeerd

Campagne `2026: SYBB`, alle cijfers berekend op **link clicks**, niet op all-clicks.

| Maand | Impressions | Link clicks | Link CTR | CPC (link) | Spend | CPM | Frequency |
|---|---|---|---|---|---|---|---|
| Jan 2026 | 16.268 | 112 | 0.7% | €0.91 | €101.74 | €6.25 | 1.81 |
| Mrt 2026 | 189.067 | 9.703 | 5.1% | €0.14 | €1.323,83 | €7.00 | 2.07 |
| Apr 2026 | 91.839 | 1.036 | 1.1% | €1.02 | €1.059,47 | €11.54 | 2.19 |
| **Lifetime** | **297.174** | **10.851** | **3.7%** | **€0.23** | **€2.485,04** | **€8.36** | **2.09** |

Ter vergelijking, dezelfde maanden op Meta's misleidende all-clicks velden: Maart 5.3% en €0.13, April 2.1% en €0.55. In April is het verschil tussen all-clicks en link het grootst, wat betekent dat een groot deel van de "clicks" passieve engagement was en geen echte doorklik.

**Wat dit laat zien:**

1. **Maart was de sterke maand.** 5.1% Link CTR tegen €0.14 CPC (link) is ruim binnen de Core-definitie van de 70-20-10 regel. 6.174 landing page views uit 9.703 link clicks, een doorloop van 63.6%.

2. **April zakte hard weg.** Link CTR viel van 5.1% naar 1.1%, CPC (link) steeg van €0.14 naar €1.02, een factor 7.3 duurder. CPM steeg tegelijk van €7.00 naar €11.54. Dat patroon, dalende CTR plus stijgende CPM bij oplopende frequency, is het klassieke beeld van creative fatigue en audience saturation.

3. **April Link CTR zat op 30.9% van het lifetime gemiddelde**, ruim onder de waarschuwingsdrempel van 70%. De campagne was op het moment van pauzeren dus duidelijk uitgeput, niet toevallig even zwak.

4. **April had wel de eerste echte conversies:** 6 purchases, 44 add to carts, 33 initiate checkouts, 6 complete registrations. Maart had 15 leads maar nul purchases. De April-creatives trokken minder maar warmer verkeer.

---

## Data-kwaliteit: purchase-waardes kloppen niet

In April rapporteert Meta 6 purchases met `action_values.purchase` = 44247. Tegelijk rapporteert `web_app_in_store_purchase` een waarde van 4.42 voor diezelfde 6 purchases. Die twee kunnen niet allebei kloppen.

Lees je 44247 als euro's, dan is de ROAS 41.8x op €1.059,47 spend, oftewel €7.374,50 per aankoop. Dat is niet realistisch voor SYBB. Lees je het als centen, dan is het €442.47 en een ROAS van 0.42x.

Ook de andere waardes ogen als vaste placeholders: elke view_content is 350 waard, elke add_to_cart 350, elke complete_registration 14.350. Dat lijkt op een hardgecodeerde waarde in de pixel in plaats van echte orderwaardes.

**Aanbeveling: controleer de value-parameter in de Meta Pixel op startyourballoonbusiness.com voordat je ROAS als beslissingsmetric gebruikt.** Tot dat is opgelost is ROAS in dit account niet bruikbaar voor de 70-20-10 classificatie en moet je op Link CTR en CPC (link) sturen.

---

## Toegangsprobleem: tweede ad account

Het command verwijst naar `act_607231713057715` als tweede te checken account. Het API token heeft daar geen toegang toe:

> This API token does not have access to account act_607231713057715. Allowed accounts: act_1489853856181844, act_567892422940728

Het token heeft wel toegang tot `act_1489853856181844`, een account dat niet in het command staat. Dat account bevat nul campagnes, actief noch gepauzeerd.

**Twee dingen om op te lossen:**
1. Klopt `act_607231713057715` nog als account ID? Zo ja, moet de Pipeboard connectie toegang krijgen.
2. Zo nee, pas het command aan naar het juiste ID, of haal de verwijzing weg.

---

## 💡 Voorstellen (wacht op goedkeuring)

Omdat er niets draait, gaan de voorstellen niet over budget-shifts maar over de vraag of en hoe je weer aanzet.

**1. Beslis over de status van het account**

Het account ligt sinds 20 April stil, ruim 3 maanden. Zolang dat zo blijft heeft het dagelijks draaien van dit command geen functie, er valt niets te optimaliseren. Drie opties:

- **Heropstarten van SYBB** met nieuwe creatives, zie voorstel 2.
- **Bewust gepauzeerd laten** en dit command tijdelijk uit de dagelijkse scheduled run halen, scheelt ruis in je morning report.
- **Op een lage waakvlam zetten**, bijvoorbeeld €10 tot €20 per dag op de bewezen Maart-hooks, puur om het pixel-signaal en de audience warm te houden.

**2. Bij heropstarten: nieuwe creatives, niet de April-set**

De April-creatives waren op het moment van pauzeren aantoonbaar op. Ze zetten opnieuw aan levert waarschijnlijk direct weer 1.1% Link CTR op. Bovendien is er inmiddels 3 maanden verstreken, dus zelfs de Maart-creatives zijn voor de audience niet meer vers.

Concreet startpunt volgens de 70-20-10 regel:
- **70% Core:** de Maart-hooks die 5.1% Link CTR haalden, opnieuw gefilmd of opnieuw gemonteerd in een nieuw format. De boodschap werkte, de uitvoering is verbruikt.
- **20% Emerging:** 2 tot 3 variaties op die winnende hooks, andere opening, andere CTA.
- **10% Experimental:** 1 tot 2 nieuwe hooks uit een ongebruikt Hormozi hook type.

Voor de invulling van de hooks: lees `Bronnen/Alex Hormozi/100m-hooks-playbook.md` en `Bronnen/Sempertex Europe/sybb-8-pillars.md`. Ik kan de concrete hook-teksten uitschrijven zodra je zegt dat je wilt heropstarten.

**3. Los eerst de pixel-waardes op**

Zet de campagne niet aan voordat de purchase values kloppen. Draait de campagne op OUTCOME_SALES met foute waardes, dan optimaliseert Meta's algoritme op een verkeerd signaal en verbrand je budget aan de verkeerde mensen. Dit is een blokkerende stap, geen nice to have.

**4. Herstel de account-toegang**

Zie de sectie Toegangsprobleem. Zonder dit blijft elke run van dit command met dezelfde fout eindigen op het tweede account.

---

## Wat er nu is gebeurd

| Tijdstip | Actie | Resultaat |
|---|---|---|
| 30 July 2026 | Campagnes opgehaald, beide accounts | 5 campagnes gevonden, allemaal PAUSED |
| 30 July 2026 | Insights opgehaald, last_3d, account niveau | Lege dataset, geen delivery |
| 30 July 2026 | Insights opgehaald, last_90d, campagne niveau | Lege dataset, geen delivery sinds 1 May |
| 30 July 2026 | Kill-regels toegepast | Niet van toepassing, nul actieve ads |
| 30 July 2026 | Ads gepauzeerd | 0 |

Er zijn geen wijzigingen doorgevoerd in het ad account.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
