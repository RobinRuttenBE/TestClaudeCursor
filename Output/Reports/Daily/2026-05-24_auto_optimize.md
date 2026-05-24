# Auto-Optimize Rapport, 2026-05-24

**Status:** Geen acties uitgevoerd. Er staan momenteel geen actieve campagnes, ad sets of ads in de toegankelijke Sempertex ad accounts. Kill-regels en 70-20-10 classificatie zijn niet van toepassing.

## Wat is gecheckt

| Account | Toegang | Actieve campagnes | Opmerking |
|---------|---------|-------------------|-----------|
| act_567892422940728 (Sempertex Europe, primair) | Ja | 0 | 5 campagnes aanwezig, allemaal PAUSED |
| act_1489853856181844 | Ja | 0 | Geen campagnes |
| act_607231713057715 | Nee | n.v.t. | Token heeft geen toegang tot dit account |

Status check tegen `status_filter: "ACTIVE"` leverde een lege dataset op beide toegankelijke accounts. Geen insights opgehaald omdat er geen actieve objecten zijn om te meten.

## Automatische acties uitgevoerd

Geen. Er waren geen actieve ads, dus geen kill-regels op Link CTR (<0,8%) of CPC link (>€1,50) konden triggeren.

## Waarschuwingen

Geen. Frequency, CPM en Link CTR-drift kunnen niet worden gemeten zonder actieve impressions.

## 70-20-10 Classificatie

Niet uitgevoerd. Vereist actieve ads met minimaal 24 uur live data.

## Voorstellen (wacht op goedkeuring)

Geen ads om te optimaliseren. In plaats daarvan strategische voorstellen voor de relaunch, gebaseerd op de bevindingen uit `2026-05-24_ads_report.md`:

**1. Fix pixel value tracking voor SYBB voor relaunch**
- Probleem: 2026: SYBB rapporteerde €7.374 per purchase (€44.247 totaal voor 6 purchases). De purchase value uit de Meta Pixel is misgeconfigureerd.
- Reden: Zonder correcte purchase values is ROAS onbetrouwbaar en kan een toekomstige auto-optimize geen budget-beslissingen op ROAS baseren.
- Verwachte impact: betrouwbare ROAS-data, kill-regels en 70-20-10 classificatie kunnen daarna draaien op echte omzet.

**2. Relaunch template: Campagne Nozzle Up 2025 1**
- Hoogste betrouwbare ROAS van alle gepauzeerde campagnes: 8,3x op €853 spend.
- AOV €1.180 wijst op een schone funnel-flow tot aan checkout.
- Reden: bewezen converter, geen pixel-vraagtekens zoals SYBB.
- Verwachte impact: nieuwe campagne start met hoogste kans op rendabele eerste 3 dagen.

**3. Combineer SYBB hooks met Nozzle Up funnel**
- SYBB had de hoogste CTR (4,2%) van alle gepauzeerde campagnes, ondanks ROAS-vraagtekens.
- Nozzle Up template (zie voorstel 2) had de schoonste funnel.
- Reden: hook-kwaliteit kun je los van funnel testen. SYBB hook + Nozzle Up landingspagina geeft de hoogste verwachte combinatie van klik en conversie.

**4. Pauzeer Last push Nozzle Up als learning, niet als template**
- 0,8x ROAS, verlies op deze laatste push. Funnel knelde aan checkout.
- Niet gebruiken als blauwdruk voor de relaunch, wel als case study voor wat NIET werkte.

## Vereisten voor volgende auto-optimize run

- Minstens één campagne moet status ACTIVE hebben in act_567892422940728
- Ads moeten minimaal 24 uur live zijn voordat kill-regels worden toegepast
- Voor betrouwbare ROAS-beslissingen: pixel value tracking eerst fixen op SYBB-campagnes
- Voor act_607231713057715: API token moet uitgebreid worden met toegang tot dit account, anders blijft het buiten scope

## Definities die gehanteerd zouden zijn

- **Link CTR** = `actions.link_click / impressions × 100` (niet het `ctr` veld uit Meta)
- **CPC (link)** = `spend / actions.link_click` (niet het `cpc` veld uit Meta)
- Kill drempels: Link CTR < 0,8% bij ≥1.000 impressions, CPC (link) > €1,50 bij ≥500 link clicks

## Output

- Rapport: `Output/Reports/Daily/2026-05-24_auto_optimize.md`
- Geen Meta API mutaties uitgevoerd
- Geen Google MCP calls (Gmail, Calendar, Drive, Sheets, Docs, Slides) per command-argument
- Geen schrijfacties naar Meta Ads Tracker Google Sheet
