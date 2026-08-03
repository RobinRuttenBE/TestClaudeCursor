# Morning Report — 2026-08-03

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 3 augustus 2026

**Het account ligt stil.** Nul spend in de laatste 30 dagen, en ook nul over de laatste 90 dagen. De laatste actieve dag was in april 2026, dus ruim 3 maanden geleden. Alle 5 campagnes staan op PAUSED.

Het tweede account uit het command (`act_607231713057715`) bestaat niet onder deze connectie. Wel gecheckt: **AmbitionAvenue** (`act_1489853856181844`), geen campagnes, geen spend.

### Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | Paused | € 2.485,04 | 297.174 | 12.067 | 4,1% | € 0,21 | € 8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | € 853,19 | 129.558 | 3.291 | 2,5% | € 0,26 | € 6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | € 800,78 | 109.869 | 2.786 | 2,5% | € 0,29 | € 7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | € 604,03 | 369.136 | 3.638 | 1,0% | € 0,17 | € 1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | € 124,42 | 7.615 | 195 | 2,6% | € 0,64 | € 16,34 | 0 | n.v.t. |

\* Die 17,8x klopt niet. De pixel meldt 6 purchases met € 44.247,00 totaalwaarde, dus € 7.374,50 per SYBB-ticket, plus € 86.100,00 op complete_registration. Tracking-fix nodig.

### Underperformers
- **2026: SYBB - Kopie**, CPC € 0,64 en CPM € 16,34, beide boven drempel. Duurste campagne van het account, nul purchases.
- **Ad H13,B3,CTA5 (Kopie 3)**, CPC € 0,93. Dezelfde hook draaide in BATCH 2 op € 0,07. De hook is niet het probleem, de gedupliceerde ad set wel.
- **Ad H11, B3, CTA5 (Kopie 1)**, CPC € 0,67 over € 521,56, de grootste spender van 2026. Origineel in BATCH 2: € 0,25.
- **Ad SYBB w/ Semp (BLACK)**, CTR 1,0% en CPC € 0,61. Enige statische creative, zwakste van het account.
- **April als maand**, CPC € 0,55 en CPM € 11,54 tegen € 0,13 en € 7,00 in maart.

Frequency zit nergens boven 3,5 (max 2,89), dus de kostenstijging komt niet van herhaling maar van het dupliceren van ad sets.

### Top performers
- **Beste CTR:** H13,B3,CTA5 in BATCH 2, 9,8%
- **Laagste CPC:** dezelfde ad, € 0,07
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1, 8,3x
- **Beste ad set:** BATCH 2: Expertise & POC, € 1.463,49 spend, 10.322 clicks, gemiddeld € 0,14 CPC

### Aanbeveling
1. Fix eerst de pixel-waardes. Zonder betrouwbare purchase value is elke ROAS-beslissing giswerk.
2. Herstart de **originele** 2026: SYBB met de bestaande BATCH 2 ad set, archiveer de kopie definitief.
3. 70% bewezen (H13, H15, H12 uit BATCH 2: samen 8.615 clicks op € 0,12), 20% nieuwe hooks op dezelfde B3 body en CTA5, 10% één nieuwe angle (pricing of quality proof). Geen statische creatives meer.
4. Elke week extra stilstand maakt de herstart duurder: pixel-signalen verouderen en de learning phase moet opnieuw.

Rapport opgeslagen in `output/reports/daily/2026-08-03_ads_report.md`, gecommit en gepusht. Google Sheet-stap overgeslagen, geen enkele Google MCP aangeroepen.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Let wel: met nul ad traffic sinds april zal die funnel data alleen organisch verkeer laten zien.

---

Rapport staat in `Output/Reports/Daily/2026-08-02_sybb_report.md`, gecommit en gepusht.

**Wat de data zegt**

Beide bronnen zijn leeg voor 2 augustus. Campagne `2026: SYBB` (id `120239435987290239`) staat op PAUSED met nul spend, impressies en clicks, op elke dag van 27 juli t/m 2 augustus. Laatste echte delivery was april 2026. PostHog registreerde nul pageviews op `www.startyourballoonbusiness.com` op 2 augustus, en 3 pageviews van 3 bezoekers over het hele 7-daagse venster, allemaal direct verkeer.

**De eigenlijke vondst**

Tijdens het ophalen van de PostHog data bleek de meetopstelling die de skill veronderstelt grotendeels niet te bestaan:

- geen scroll depth event in het project, dus Scroll 25/50/75/100% zijn structureel niet meetbaar
- geen CTA click event op de SYBB pagina, dus CTA Click Rate is niet berekenbaar
- geen enkele UTM property op `$pageview`, dus de `utm_content=hXX_bX_ctaX` conventie komt nergens in de analytics terecht en de cross-reference tussen ad variant en paginagedrag is onmogelijk, ook bij volle campagne

De pagina is wel correct aangesloten op PostHog, er komt alleen vrijwel niemand. Ter vergelijking deed de webshop op dezelfde dag 3.256 pageviews in hetzelfde project.

Uit de laatst bekende ads-data haalde ik nog twee dingen die los staan van de stilstand: in maart 9.703 link clicks tegen 6.174 landing page views, 36% verlies tussen klik en geladen pagina, en de pixel purchase values kloppen niet (€ 7.374,50 per SYBB-ticket, € 86.100,00 op complete_registration).

Ik heb alleen de Meta Ads MCP en PostHog MCP gebruikt, geen Google MCP aangeroepen en niet naar de Google Sheet tracker geschreven.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-08-03_auto_optimize.md` en gepusht.

## Uitkomst: geen acties uitgevoerd

Er viel niets te optimaliseren. Het account ligt volledig stil.

- **0 actieve campagnes.** Alle 5 campagnes staan op PAUSED.
- **0 impressies, 0 spend** over last_3d én last_30d.
- Laatste delivery van `2026: SYBB` ligt vóór 5 mei 2026, instellingen laatst aangeraakt 19/20 april 2026. Dat bevestigt het "account dark" signaal uit het ads-report van vanochtend.
- Kill-regels konden dus niet triggeren. Ik heb **niets** gewijzigd in Meta, dit was volledig read-only.

## Wat ik wel heb gedaan

Omdat een leeg rapport weinig waarde heeft, heb ik de lifetime data van `2026: SYBB` uitgerekend op link metrics als basis voor een herstart. Drie dingen sprongen eruit:

**1. Er zijn duidelijke winners om mee te herstarten.** H15, H14 en H11 (allemaal in ad set BATCH 2: Expertise & POC) halen 2.2% tot 4.1% Link CTR bij €0.16 tot €0.31 CPC (link). Schoon genoeg om direct op verder te bouwen.

**2. Eén ad zou de kill-regel triggeren.** `SYBB w/ Semp (BLACK)`: 0.7% Link CTR over 16,268 impressies. Staat al gepauzeerd, dus geen actie, maar niet heractiveren.

**3. Twee datakwaliteitsproblemen die je moet uitzoeken vóór herstart.** De H13 hoofdvariant claimt 10.6% Link CTR bij €0.07 CPC, 5 tot 10x hoger dan identieke ads met dezelfde body en CTA. En één ad rapporteert €42,773.50 purchase value uit 2 aankopen, oftewel €21,386.75 per stuk. Dat is geen workshopprijs. Zolang dat niet verklaard is, is de ROAS-regel in de 70-20-10 classificatie onbetrouwbaar voor dit account. Exclusief die H13 outlier is het echte campagnebeeld 1.9% Link CTR bij €0.46 CPC (link), wat prima is.

Ik heb hierop bewust geen budget-shifts voorgesteld als harde actie, conform de openstaande TODO in het command dat de 70-20-10 drempels nog niet gekalibreerd zijn voor link metrics.

## Twee dingen voor jou

**Het tweede account kon ik niet controleren.** De API-token heeft geen toegang tot `act_607231713057715`. Hij geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`. Dat laatste heb ik wel gecheckt: 0 campagnes. Als `act_607231713057715` echt gecontroleerd moet worden, moet de token-toegang uitgebreid worden of het account-ID in het command gecorrigeerd.

**Belangrijkste beslissing:** het account ligt ruim 105 dagen stil. Dit dagelijkse rapport levert nu geen waarde en zal morgen exact hetzelfde opleveren. Wil je herstarten (ik heb een concreet voorstel klaar: €30 per dag, alleen de 3 winners, duplicaat-ad sets uit), of zet ik de dagelijkse auto-optimize tijdelijk uit tot er weer een campagne live staat?

Ter info: de claude.ai-gehoste Pipeboard connector vraagt om herautorisatie, maar de lokale Pipeboard MCP werkte prima, dus dat heeft deze run niet geblokkeerd. Geen Google MCPs aangeroepen en niets naar de Tracker Sheet geschreven, zoals gevraagd.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
