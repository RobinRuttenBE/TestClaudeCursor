# Auto-Optimize Rapport, 3 augustus 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode kill-regels:** last_3d (31 juli t/m 3 augustus 2026)
**Databronnen:** Meta Ads MCP (Pipeboard). Geen Google MCPs gebruikt, geen schrijfactie naar de Tracker Sheet.

---

## Samenvatting

Er is niets te optimaliseren. Het advertentieaccount ligt volledig stil: **0 actieve campagnes, 0 impressies, 0 spend** over de afgelopen 3 dagen. Alle 5 campagnes in het account staan op PAUSED. Geen enkele kill-regel kan triggeren, want er is geen delivery.

Dit is de tweede dag op rij dat dit wordt vastgesteld (zie `2026-08-03_ads_report.md`: "account dark, last active April 2026"). De data bevestigt dat: de laatste levering van campagne `2026: SYBB` ligt vóór 5 mei 2026, en de campagne-instellingen zijn voor het laatst aangeraakt op 19 en 20 april 2026.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd. Er zijn geen actieve ads.**

De kill-regels (Link CTR < 0.8% na ≥ 1.000 impressies, CPC (link) > €1.50 na ≥ 500 link clicks) zijn niet toegepast omdat er over last_3d geen enkele ad delivery had. Er is geen enkele status gewijzigd in Meta.

---

## Account- en campagnestatus

| Campagne | ID | Status | Dagbudget | Laatst gewijzigd |
|---|---|---|---|---|
| 2026: SYBB | 120239435987290239 | PAUSED | €100.00 | 19 april 2026 |
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | geen (CBO uit) | 20 april 2026 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | geen | 21 september 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70.00 | 15 september 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30.00 | 15 september 2025 |

**Accountgezondheid:** account_status = 1 (actief, niet geblokkeerd). Valuta EUR, tijdzone Europe/Brussels. Lifetime spend €4,867.46. Saldo €0.00.

Het account is dus gezond en klaar om te draaien. De stilstand is een keuze of een vergeten herstart, geen technische blokkade.

**Tweede account:** `act_607231713057715` kon niet gecontroleerd worden. De API-token heeft er geen toegang toe. De token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`. Dat tweede toegankelijke account (`act_1489853856181844`) is gecontroleerd en bevat 0 campagnes.

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| Account inactief | ~105 dagen zonder delivery (sinds ca. 20 april 2026) | Beslis: herstarten of formeel afsluiten |
| Learning phase verloren | > 3 maanden stil | Bij herstart begint elke ad set opnieuw in learning. Reken op 5 tot 7 dagen ruis voordat data betrouwbaar is |
| Datakwaliteit purchase value | 2 purchases met €42,773.50 totale waarde op één ad | Verifieer de pixel value voordat je op ROAS stuurt. Zie hieronder |

Creative fatigue en CPM-waarschuwingen zijn niet van toepassing: geen delivery betekent geen frequency-opbouw. Lifetime frequency lag bij alle ads tussen 1.45 en 1.95, dus ruim onder de drempel van 3.5. De creatives zijn niet opgebrand, ze zijn simpelweg gestopt.

---

## 📊 70-20-10 classificatie (historische data, geen live oordeel)

Omdat er geen live data is, is hieronder de **lifetime** performance van campagne `2026: SYBB` geclassificeerd. Dit is bedoeld als startpunt voor een herstart, niet als actueel oordeel. Conform de openstaande TODO in het command zijn de 70-20-10 drempels nog niet gekalibreerd voor link metrics, dus dit is een richtlijn. **Er zijn op basis hiervan geen budget-shifts uitgevoerd.**

Alle metrics zijn berekend uit `actions.link_click`, niet uit Meta's `clicks`/`ctr`/`cpc` velden.

### 70% Core, bewezen winners

| Ad | Ad set | Impressies | Link clicks | Link CTR | CPC (link) | Spend | ROAS |
|---|---|---|---|---|---|---|---|
| H15,B3,CTA5 | BATCH 2: Expertise & POC | 34,299 | 1,403 | 4.1% | €0.16 | €218.96 | 0.00x |
| H14,B3,CTA5 | BATCH 2: Expertise & POC | 33,235 | 760 | 2.3% | €0.31 | €232.36 | 0.00x |
| H11, B3, CTA5 | BATCH 2: Expertise & POC | 31,060 | 684 | 2.2% | €0.30 | €202.48 | 0.00x |
| H11, B3, CTA5 | BATCH 2: Expertise & POC - Kopie 1 | 38,614 | 428 | 1.1% | €1.22 | €521.56 | 2.83x |

H15 en H14 zijn de schoonste winners: hoge Link CTR én lage CPC (link). H11 in Kopie 1 kwalificeert alleen via de ROAS-regel (2.83x, 4 purchases, €1,473.50), niet via link metrics. De link-performance van die ad is juist zwak (€1.22 CPC), wat betekent dat er weinig maar zeer koopkrachtig verkeer doorheen kwam.

### 20% Emerging, potentieel

| Ad | Ad set | Impressies | Link clicks | Link CTR | CPC (link) | Spend |
|---|---|---|---|---|---|---|
| H12,B3,CTA5 | BATCH 2: Expertise & POC | 48,166 | 696 | 1.4% | €0.56 | €388.40 |
| H15,B3,CTA5 | BATCH 2: Expertise & POC - Kopie 4 | 4,737 | 57 | 1.2% | €0.87 | €49.83 |
| H12,B3,CTA5 | BATCH 2: Expertise & POC - Kopie 2 | 13,955 | 174 | 1.2% | €0.81 | €141.43 |
| H13,B3,CTA5 | BATCH 2: Expertise & POC - Kopie 3 | 16,766 | 195 | 1.2% | €1.06 | €206.99 |

### Buiten classificatie, zou de kill-regel triggeren

| Ad | Ad set | Impressies | Link clicks | Link CTR | CPC (link) | Spend |
|---|---|---|---|---|---|---|
| SYBB w/ Semp (BLACK) | Ad Set SYBB test set STATISCH | 16,268 | 112 | 0.7% | €0.91 | €101.74 |

Deze ad haalt 0.7% Link CTR over 16,268 impressies en zou bij live delivery direct gepauzeerd worden door de kill-regel. Hij staat al op PAUSED via de campagne, dus geen actie nodig. **Niet heractiveren bij herstart.**

### Apart gezet: datakwaliteit

| Ad | Ad set | Impressies | Link clicks | Link CTR | CPC (link) | Purchases | Waarde |
|---|---|---|---|---|---|---|---|
| H13,B3,CTA5 | BATCH 2: Expertise & POC | 60,074 | 6,342 | 10.6% | €0.07 | 0 | €0.00 |
| H13,B3,CTA5 | BATCH 2: Expertise & POC - Kopie 3 | 16,766 | 195 | 1.2% | €1.06 | 2 | €42,773.50 |

Twee signalen die geverifieerd moeten worden vóór je hierop stuurt:

1. **10.6% Link CTR op de H13 hoofdvariant.** Dat is 5 tot 10x hoger dan elke andere ad in dezelfde campagne, met exact dezelfde body en CTA. Voor een B2B-workshopfunnel is dat onwaarschijnlijk hoog. Vergelijk deze 6,342 link clicks met het werkelijke aantal sessies in PostHog over dezelfde periode. Wijkt dat sterk af, dan telt Meta hier clicks die de landingspagina nooit bereiken.
2. **€42,773.50 aan purchase value uit 2 purchases** (€21,386.75 per aankoop) op de Kopie 3 variant. Dat is geen SYBB-workshopprijs. Waarschijnlijk lekt hier een groothandelsorder of een verkeerde pixel-waarde in. Zolang dit niet is uitgezocht is de ROAS-regel in de 70-20-10 classificatie onbetrouwbaar voor dit account.

### Totalen campagne `2026: SYBB` (lifetime)

| Metric | Inclusief H13 hoofdvariant | Exclusief H13 hoofdvariant |
|---|---|---|
| Spend | €2,485.04 | €2,063.75 |
| Impressies | 297,174 | 237,100 |
| Link clicks | 10,851 | 4,509 |
| Link CTR | 3.7% | 1.9% |
| CPC (link) | €0.23 | €0.46 |

De rechterkolom is het realistische beeld. Een Link CTR van 1.9% en CPC (link) van €0.46 is een gezonde basis om op verder te bouwen.

**Budget mismatch:** niet van toepassing. Er loopt geen budget.

---

## 💡 Voorstellen (wacht op goedkeuring)

Alle voorstellen hieronder gaan over een eventuele **herstart**. Er is niets uitgevoerd.

### 1. Beslis eerst: herstarten of afsluiten

Het account ligt ruim drie maanden stil. Dit dagelijkse auto-optimize rapport levert nu geen waarde, want er is niets te optimaliseren.

- **Optie A, herstarten.** Zie voorstel 2 en 3.
- **Optie B, pauzeren van de rapportage.** Zet de dagelijkse `/ads-auto-optimize` uit tot er weer een campagne live staat. Scheelt ruis in je inbox.

Zonder deze beslissing produceert dit rapport morgen exact hetzelfde resultaat.

### 2. Herstart-configuratie (als optie A)

Start niet de oude campagne opnieuw met alle 10 ads. Voorstel:

- Heractiveer campagne `2026: SYBB` (120239435987290239) met dagbudget €30.00 in plaats van €100.00. Reden: na 3 maanden stilstand is elke ad set terug in learning phase. Klein beginnen beperkt de kosten van de leerperiode.
- Activeer alleen 3 ads: **H15 (Batch 2)**, **H14 (Batch 2)** en **H11 (Batch 2)**. Dit zijn de drie schoonste performers op link metrics (Link CTR 2.2% tot 4.1%, CPC €0.16 tot €0.31).
- Laat **SYBB w/ Semp (BLACK)** uit. Die faalt de kill-regel op lifetime data.
- Laat de duplicaat-ad sets (Kopie 1 t/m 4) uit. Ze verdelen budget over dezelfde creatives en verzwakken daarmee de learning phase van elke ad set afzonderlijk.
- Verwachte impact: bij een Link CTR van circa 2% en CPC (link) van circa €0.30 levert €30.00 per dag ongeveer 100 link clicks per dag op tegen een schone leercurve.

### 3. Verifieer tracking vóór herstart

Doe dit voordat er weer budget doorheen gaat, anders bouw je optimalisatie op onbetrouwbare cijfers:

- Controleer de purchase value in de pixel. De €21,386.75 per aankoop moet verklaard of gecorrigeerd worden.
- Controleer of de UTM-parameters nog volgens de conventie staan: `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X`, alles lowercase.
- Vergelijk Meta link clicks met PostHog sessies op startyourballoonbusiness.com om de H13 anomalie te verklaren.

### 4. Nieuwe variaties op de winnende hooks

Gebaseerd op de top 3 hooks op Link CTR (H15 met 4.1%, H14 met 2.3%, H11 met 2.2%). Deze hooks hebben bewezen te werken op de starter-doelgroep. Voorstel: per hook 2 variaties bouwen volgens de 70-20-10 regel, waarbij de bestaande 3 het 70% deel vormen en de variaties het 20% deel.

Dit voorstel is bewust nog niet uitgewerkt tot concrete copy. De hookteksten zelf staan niet in de Meta-data, alleen de codes. Geef aan of je wilt dat ik de hookteksten ophaal uit de campagne-historie en dan concrete varianten schrijf.

---

## Uitgevoerde acties in Meta

**Geen.** Dit rapport is volledig read-only. Er is geen enkele campagne, ad set of ad gewijzigd.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

De meest urgente is voorstel 1: beslissen of het account herstart of dat de dagelijkse rapportage tijdelijk uit gaat.
