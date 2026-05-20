# Auto-Optimize Rapport — 2026-05-20

**Run:** /ads-auto-optimize
**Datum:** 2026-05-20
**Periode geanalyseerd:** last_3d (2026-05-17 t/m 2026-05-19)
**Bronnen gebruikt:** Pipeboard Meta Ads MCP (alleen). PostHog MCP niet aangeroepen omdat er geen actieve ads zijn om tegen te kruisen.
**Strikte regel actief:** Geen Google MCPs aangeroepen. Niets geschreven naar Google Sheet tracker.

---

## ⚡ Automatische acties uitgevoerd

**Totaal gepauzeerd: 0 ads**

Geen automatische pauzeer-acties uitgevoerd. Reden: er zijn geen ACTIVE campagnes in het Sempertex Ad Account.

---

## 🔍 Status van de geanalyseerde accounts

| Account | Status | Aantal ACTIVE campagnes | Opmerking |
|---|---|---|---|
| `act_567892422940728` (Sempertex Ad Account, primair) | Toegankelijk | 0 | Alle 5 campagnes staan PAUSED |
| `act_1489853856181844` (extra toegankelijk via token) | Toegankelijk | 0 | Geen ACTIVE campagnes |
| `act_607231713057715` (genoemd in command) | **Niet toegankelijk** | n.v.t. | Token heeft geen access — alleen `act_567892422940728` en `act_1489853856181844` zijn toegestaan |

### Detail — campagnes op `act_567892422940728` (alle PAUSED)

| Campagne | ID | Status | Daily budget | Laatst geüpdatet |
|---|---|---|---|---|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | n.v.t. | 2026-04-20 |
| 2026: SYBB | 120239435987290239 | PAUSED | €100,00 | 2026-04-19 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | n.v.t. | 2025-09-21 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30,00 | 2025-09-15 |

---

## ⚠️ Waarschuwingen

| Signaal | Beschrijving | Actie aanbevolen |
|---|---|---|
| Geen actief verkeer | 0 ACTIVE campagnes in primair account; SYBB-campagne staat sinds 2026-04-19 op PAUSED | Bevestigen of dit een bewuste pauze is (na de drempelwijziging op 2026-04-13) of dat de campagne onbedoeld uit staat |
| Account-toegang | `act_607231713057715` uit het command/CLAUDE.md is niet toegankelijk via huidige Pipeboard token | Token-permissies controleren of account-ID corrigeren in command-definitie |

---

## 📊 70-20-10 Classificatie

Niet uitgevoerd. Er zijn geen ACTIVE ads om te classificeren in Core / Emerging / Experimental.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen budget-, variatie- of audience-voorstellen omdat er geen lopende performance-data is.

**Wel besluit-vragen aan Robin:**

1. **SYBB campagne (`120239435987290239`) opnieuw activeren?**
   - Stond op PAUSED sinds 2026-04-19, ongeveer een maand geleden.
   - Reden: de Link CTR / CPC (link) drempels zijn op 2026-04-13 herzien — werd de campagne daarna opzettelijk uitgezet om eerst nieuwe creatives te bouwen, of is dit een drift?
   - Beslis: opnieuw aan, of definitief afsluiten en als archief markeren.

2. **Account-mismatch oplossen:**
   - Het command refereert aan `act_607231713057715` als secundair account, maar de Pipeboard token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`.
   - Beslis: token uitbreiden (Pipeboard re-auth met andere business), of de command-definitie en `CLAUDE.md` updaten naar `act_1489853856181844`.

3. **Wat moet de Auto-Optimize doen als er niets draait?**
   - Optie A: stilletjes "geen acties" loggen (huidige gedrag).
   - Optie B: in deze toestand een alert sturen ("ads staan uit, geen budget loopt"), zodat het niet onopgemerkt blijft.

---

**Wil je een of meer van deze besluit-vragen oppakken? Geef aan welke nummers.**

---

## Log

- 2026-05-20 — Run uitgevoerd zonder Google MCPs en zonder Google Sheet writes.
- Geen `update_ad` calls naar Pipeboard (geen ads om te pauzeren).
- Geen PostHog queries (niet relevant zonder ad-verkeer om te kruisen).
- Rapport opgeslagen: `Output/Reports/Daily/2026-05-20_auto_optimize.md`.
