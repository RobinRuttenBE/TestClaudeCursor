# Auto-Optimize Rapport — 2026-05-08

**Run modus:** lokaal, alleen Meta Ads MCP (Pipeboard) + PostHog MCP gebruikt. Geen Google MCPs aangeroepen. Geen schrijfacties naar Google Sheets tracker.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd — er zijn geen actieve ads om tegen kill-regels te toetsen.**

### Reden

Beide toegankelijke ad accounts (`act_567892422940728` Sempertex Europe en `act_1489853856181844`) bevatten momenteel **0 actieve campagnes**. Alle 5 campagnes in `act_567892422940728` staan op status `PAUSED`:

| Campagne ID | Naam | Status | Laatst geüpdatet |
|---|---|---|---|
| 120243293329420239 | 2026: SYBB - Kopie | PAUSED | 2026-04-20 |
| 120239435987290239 | 2026: SYBB | PAUSED | 2026-04-19 |
| 120233295855990239 | Last push Nozzle Up | PAUSED | 2025-09-21 |
| 120232324822740239 | Nozzle Up END OF AUGUST | PAUSED | 2025-09-15 |
| 120230372047970239 | Campagne Nozzle Up 2025 1 | PAUSED | 2025-09-15 |

Account `act_607231713057715` is niet toegankelijk via deze API token (alleen `act_567892422940728` en `act_1489853856181844` zijn toegestaan).

Insights call op `2026: SYBB` over `last_3d`: leeg (geen spend, geen impressions). Idem account-level `last_7d`.

**Totaal gepauzeerd: 0 ads** — alles staat al uit.

---

## ⚠️ Waarschuwingen

| Signaal | Detail | Actie |
|---|---|---|
| Geen actieve advertentie-uitgaven | 0 active campagnes, 0 impressions in last_3d en last_7d | Lancering nieuwe SYBB-batch nodig om weer data te genereren |
| Account toegang | `act_607231713057715` returnt 401 op deze token | Verifieer of dit account nog relevant is, of token-permissies herzien |

---

## 📊 70-20-10 Classificatie

**Niet van toepassing.** Classificatie vereist actieve ads met minimaal 24 uur runtime en meetbare Link CTR / CPC (link). Met 0 actieve ads is er niets te classificeren.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatie-voorstellen op basis van performance data, omdat er geen performance data is. Wel een paar systeem-niveau actiepunten:

**1. Lanceer een nieuwe SYBB-batch**
- De `2026: SYBB` campagne staat sinds 2026-04-19 op pause
- Zonder actieve campagne genereert het Auto-Optimize command geen waarde, en het Morning Report mist Meta Ads data
- Aanbevolen: nieuwe batch ads lanceren op basis van eerdere winnende hooks (zie laatste `/ads-report` voor referentie)

**2. Verifieer token-permissies voor `act_607231713057715`**
- Reden: huidige token weigert dit account; als het nog gebruikt wordt is dat een blinde vlek
- Actie: of token-permissies uitbreiden, of het account uit de auto-optimize scope verwijderen

**3. Overweeg drempel-kalibratie voor 70-20-10 op link metrics**
- Het command is recent overgestapt van all-clicks naar link metrics (Link CTR < 0.8%, CPC link > €1.50)
- De 70-20-10 grenzen (>1.5% Link CTR, < €0.50 CPC link voor Core) zijn nog niet formeel gekalibreerd
- Bij eerstvolgende live-batch: verzamel 7 dagen data en stel definitieve drempels vast

---

**Wil je een of meer van deze voorstellen oppakken? Geef aan welke nummers.**

---

## Run metadata

- **Datum:** 2026-05-08
- **Periode:** last_3d (Meta Ads insights)
- **Accounts gecheckt:** `act_567892422940728` (toegankelijk, 0 actief), `act_607231713057715` (geen toegang), `act_1489853856181844` (toegankelijk, 0 actief)
- **MCPs gebruikt:** Pipeboard Meta Ads MCP. PostHog MCP niet aangeroepen — zonder ad spend was er geen meaningful cross-reference mogelijk.
- **Output locatie:** `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-08_auto_optimize.md`
