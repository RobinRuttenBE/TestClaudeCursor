# Auto-Optimize Rapport, 6 juli 2026

**Run tijd:** 2026-07-06
**Databron:** Meta Ads MCP (Pipeboard). Periode: last_3d.
**Accounts gecontroleerd:** act_567892422940728 (primair), act_1489853856181844
**Niet toegankelijk:** act_607231713057715 (token heeft geen toegang, zie notities)

## Samenvatting

Er zijn **geen actieve Meta Ads campagnes** op de toegankelijke accounts. Er is dus geen performance data over de afgelopen 3 dagen, geen ad die een kill-regel kan triggeren en geen budget om te herverdelen. Dit rapport is een status-check, geen optimalisatie.

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn geen actieve ads om te evalueren.

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen. Zonder actieve ads is er geen creative fatigue, dure reach of dalende Link CTR te meten.

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven budget-, variatie- of audience-voorstellen mogelijk zonder lopende campagnes.

Wel twee operationele aandachtspunten:

**1. SYBB campagne staat op PAUSED**
- Campagne `2026: SYBB` (id 120239435987290239, dagbudget €100,00) is gepauzeerd, laatst gewijzigd 19 april 2026.
- Ook `2026: SYBB - Kopie` (id 120243293329420239) en alle Nozzle Up campagnes staan op PAUSED.
- Actie voor Robin: zolang SYBB gepauzeerd blijft, levert dit dagelijkse auto-optimize rapport geen signaal op. Zet de campagne weer actief om de kill-regels en 70-20-10 logica te laten werken, of pauzeer de dagelijkse run tot de volgende campagne live gaat.

**2. Secundair account niet toegankelijk**
- Het command verwijst naar `act_607231713057715`, maar het huidige API token heeft daar geen toegang toe.
- Toegestane accounts volgens het token: `act_1489853856181844` en `act_567892422940728`.
- Actie voor Robin: controleer of `act_607231713057715` het juiste account-id is, of werk het command bij naar een toegankelijk account. Als er campagnes op dat account draaien, worden die nu gemist.

## Databron notities

- Meta Ads MCP (Pipeboard): bereikbaar, token actief. Eerste twee campagne-calls gaven een socket timeout, daarna succesvol na retry.
- Alleen Meta Ads MCP gebruikt, conform de strikte regel voor deze run. Geen Google MCPs aangeroepen, niet naar de Google Sheet tracker geschreven.
- PostHog niet geraadpleegd: zonder actieve ads is er geen ad-naar-pagina cross-reference te maken.

---

**Conclusie:** geen actie vereist vanuit auto-optimize. De pijplijn staat stil omdat er geen actieve campagnes zijn. Wil je dat ik de SYBB campagne weer activeer, of het command bijwerk naar een toegankelijk secundair account?
