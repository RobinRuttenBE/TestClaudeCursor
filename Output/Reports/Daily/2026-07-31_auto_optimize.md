# Auto-Optimize Rapport, 31 juli 2026

**Run:** 2026-07-31, bronnen Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google MCPs gebruikt, niet naar de Tracker Sheet geschreven.
**Uitkomst in één zin:** het ad account ligt nog steeds volledig stil, er is niets gewijzigd, en de SYBB landingspagina blijkt helemaal niet gemeten te worden in PostHog.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Er zijn 0 ads gepauzeerd en er is niets gewijzigd in het ad account.**

Reden: er zijn nul actieve campagnes, nul actieve ads, nul impressions en nul spend over de afgelopen 3 dagen. Kill-regels kunnen zonder delivery niet triggeren.

| Account | Status | Campagnes | Spend laatste 3d |
|---|---|---|---|
| `act_567892422940728` (Sempertex Ad Account) | Actief, saldo €0.00 | 5, allemaal PAUSED | €0.00 |
| `act_1489853856181844` | Bereikbaar | 0 | €0.00 |
| `act_607231713057715` | **Geen toegang** | n.v.t. | n.v.t. |

Laatste delivery in het account: **april 2026**. De campagne `2026: SYBB` is rond 19 en 20 april gepauzeerd. Dat is inmiddels ruim drie maanden geleden. Ook over `last_90d` retourneert Meta nul rijen.

---

## ⚠️ Waarschuwingen

Geen live waarschuwingen, er draait niets. De onderstaande punten komen uit de laatste actieve periode (april 2026) en uit de tracking-check van vandaag.

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| SYBB landingspagina niet gemeten in PostHog | 0 events van `startyourballoonbusiness.com` | Blokkerend, pixel plaatsen voor heropstart |
| Purchase-waardes in Meta inconsistent | 6 purchases, waarde 44247 versus 4.42 | Blokkerend, ROAS is nu onbruikbaar |
| Creative fatigue bij stopzetten | Link CTR 5.1% (mrt) naar 1.1% (apr) | Niet dezelfde creatives heropstarten |
| Tweede ad account uit het command onbereikbaar | Toegangsfout op `act_607231713057715` | Command-bestand corrigeren |

### Nieuw vandaag: de SYBB landingspagina staat niet in PostHog

De `daily-sybb-report` skill en de KPI-tabel in `CLAUDE.md` gaan ervan uit dat `startyourballoonbusiness.com` gemeten wordt in PostHog project "Default project". Dat is niet zo.

De enige hostnames die events sturen naar dit project zijn `www.sempertexeurope.com` en `rezolvbv-sh-sempertex.odoo.com`. De organisatie Sempertex Europe heeft bovendien maar één project (id 149694), dus de data staat ook niet elders. In de top 15 entry pages over 30 dagen komt SYBB niet voor.

Concreet gevolg: de KPI targets voor SYBB (LP bounce rate <55%, scroll depth >60%, CTA click rate >4%, time on page) zijn op dit moment **niet meetbaar**. Ook de cross-reference tussen Meta Ads en PostHog uit het morning report kan niet werken zolang dit niet is opgelost.

Ter referentie, wat er wel gemeten wordt (sempertexeurope.com, laatste 30 dagen):

| Metric | Waarde |
|---|---|
| Bezoekers | 9.159 |
| Pageviews | 63.168 |
| Sessies | 11.222 |
| Gem. sessieduur | 5m 10s |
| Bounce rate | 58.6% |

---

## 📊 70-20-10 Classificatie

**Niet van toepassing.** Er zijn geen actieve ads om te classificeren, en geen budget om te verdelen. Huidig dagbudget in delivery: €0.00.

**Budget mismatch:** n.v.t.

### Baseline voor heropstart (april 2026, laatste actieve venster)

Alle 8 ads zaten in één ad set, `BATCH 2: Expertise & POC`. Totaal: €1.059,47 spend, 91.839 impressions, 1.036 link clicks.

| Ad | Impressies | Spend | Link clicks | Link CTR | CPC (link) | All Clicks CTR | CPC (all) | Freq | CPM | LPV |
|---|---|---|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | 38.614 | €521,56 | 428 | 1,1% | €1,22 | 2,0% | €0,67 | 1,85 | €13,51 | 343 |
| H13,B3,CTA5 | 16.766 | €206,99 | 195 | 1,2% | €1,06 | 2,0% | €0,63 | 1,64 | €12,35 | 171 |
| H12,B3,CTA5 | 13.955 | €141,43 | 174 | 1,2% | €0,81 | 2,6% | €0,40 | 1,95 | €10,13 | 139 |
| H14,B3,CTA5 | 16.551 | €122,96 | 158 | 1,0% | €0,78 | 1,8% | €0,41 | 1,34 | €7,43 | 108 |
| H15,B3,CTA5 | 4.737 | €49,83 | 57 | 1,2% | €0,87 | 2,3% | €0,47 | 1,45 | €10,52 | 36 |
| H12,B3,CTA5 (dupl.) | 1.058 | €14,37 | 20 | 1,9% | €0,72 | 4,7% | €0,29 | 1,94 | €13,58 | 18 |
| H15,B3,CTA5 (dupl.) | 157 | €2,32 | 4 | 2,6% | €0,58 | 6,4% | €0,23 | 1,34 | €14,78 | 3 |
| H13,B3,CTA5 (dupl.) | 1 | €0,01 | 0 | 0,0% | n.v.t. | 0,0% | €0,00 | 1,00 | €10,00 | 0 |
| **Blended** | **91.839** | **€1.059,47** | **1.036** | **1,1%** | **€1,02** | **2,1%** | **€0,55** | 2,19 | €11,54 | 818 |

Dit venster laat precies zien waarom de drempels op 13 april naar link metrics zijn gezet. Op all-clicks oogt april als 2,1% CTR bij €0,55 CPC, wat acceptabel lijkt. Op link metrics is het 1,1% bij €1,02, bijna twee keer zo slecht. Het verschil is passieve engagement, niet doorklikken.

Als de kill-regels destijds hadden gedraaid: **geen enkele ad zou zijn gepauzeerd**. De laagste Link CTR was 1,0% (H14), boven de 0,8% drempel. Geen enkele ad haalde de 500 link clicks die de CPC-regel vereist, de hoogste was 428.

### Verloop over de campagne-levensduur

| Maand | Impressies | Spend | Link clicks | Link CTR | CPC (link) | CPM | Checkouts | Purchases |
|---|---|---|---|---|---|---|---|---|
| Jan 2026 | 16.268 | €101,74 | 112 | 0,7% | €0,91 | €6,25 | 0 | 0 |
| Mrt 2026 | 189.067 | €1.323,83 | 9.703 | 5,1% | €0,14 | €7,00 | 3 | 0 |
| Apr 2026 | 91.839 | €1.059,47 | 1.036 | 1,1% | €1,02 | €11,54 | 33 | 6 |
| **Lifetime** | **297.174** | **€2.485,04** | **10.851** | **3,7%** | **€0,23** | **€8,36** | **36** | **6** |

Twee dingen die opvallen:

**Januari zou nu gepauzeerd zijn.** Met 0,7% Link CTR over 16.268 impressions triggert januari de kill-regel wel. Dat is een nuttige sanity check dat de drempel op 0,8% niet te streng staat.

**Maart was volume, april was kwaliteit.** Maart kocht 9.703 link clicks voor €0,14 per stuk, maar leverde 3 checkouts en 0 purchases op. April kocht 1.036 link clicks tegen €1,02 en leverde 33 checkouts en 6 purchases. Duurder verkeer dat wél converteerde. Van de 9.703 maart-clicks kwamen er maar 6.174 aan als landing page view, een verlies van 36%. Bij heropstart is de maart-configuratie dus niet het voorbeeld om naar terug te keren, ook al zien de CTR-cijfers er beter uit.

**ROAS:** niet betrouwbaar vast te stellen. Meta rapporteert voor dezelfde 6 purchases een waarde van 44247 onder `purchase` en 4.42 onder `web_app_in_store_purchase`. Als 44247 centen zijn (€442,47) komt april uit op circa 0,4x ROAS en lifetime op circa 0,2x. De overige waardes ogen als vaste placeholders, elke view_content precies 350 en elke registratie 14.350. Zolang dit niet klopt optimaliseert een OUTCOME_SALES campagne op een verkeerd signaal.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen budget- of biedvoorstellen, er is geen delivery om op te sturen. Dit zijn randvoorwaarden voor heropstart.

**1. Plaats PostHog tracking op startyourballoonbusiness.com**
Zonder dit is er geen landingspagina-data, geen bounce rate, geen scroll depth en geen cross-reference met Meta. Het morning report en de SYBB skill draaien nu op een aanname die niet klopt.
Verwachte impact: maakt de volledige KPI-set uit `CLAUDE.md` meetbaar en de dagelijkse rapportage weer zinvol.

**2. Repareer de pixel value tracking voordat je heropstart**
De purchase-waardes zijn intern tegenstrijdig en de overige eventwaardes ogen als placeholders. Zolang dit niet klopt is ROAS onbruikbaar als stuurmetric en optimaliseert Meta op ruis.
Verwachte impact: ROAS wordt bruikbaar als classificatiecriterium in de 70-20-10 regel, nu valt dat criterium weg.

**3. Start met nieuwe creatives, niet met de april-set**
De april-ads waren aantoonbaar uitgeput: Link CTR op 30,9% van het lifetime gemiddelde, ruim onder de 70% waarschuwingsdrempel, bij stijgende CPM. Hergebruik van dezelfde hooks start op een fatigued audience.
Concreet: houd H11 en H13 als structuur-referentie (zij droegen 60% van de link clicks), maar bouw nieuwe hooks. De hook-nummering H11 tot en met H15 met vaste B3 en CTA5 betekent dat body en CTA nooit getest zijn, alleen de hook. Dat is een open testrichting.

**4. Corrigeer het command-bestand**
Twee fouten in `.claude/commands/ads-auto-optimize`: `act_607231713057715` is niet toegankelijk met dit token (wel `act_1489853856181844`, dat leeg is), en de MCP heet `pipeboard-meta-ads`, niet `claude_ai_Pipeboard_Meta_Ads`.

**5. Beslis over de dagelijkse run**
Dit is de tweede dag op rij met een identieke nul-uitkomst. Zolang het account stilligt levert een dagelijkse run van dit command geen informatie op.
Voorstel: uit de scheduled morning report halen tot de heropstart, of omzetten naar een wekelijkse check.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef de nummers aan.**

---

### Log

| Tijd | Actie | Resultaat |
|---|---|---|
| 2026-07-31 | Campagnes opgehaald, beide accounts | 5 PAUSED, 0 ACTIVE, 1 account onbereikbaar |
| 2026-07-31 | Insights last_3d, last_7d, last_90d | Nul rijen, geen delivery |
| 2026-07-31 | Ad-level insights april 2026 | 8 ads, link metrics berekend, baseline vastgelegd |
| 2026-07-31 | PostHog host-check | SYBB domein stuurt geen events, 1 project in org |
| 2026-07-31 | Kill-regels toegepast | 0 ads gepauzeerd, geen mutaties in het ad account |
