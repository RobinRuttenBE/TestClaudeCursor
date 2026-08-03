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
