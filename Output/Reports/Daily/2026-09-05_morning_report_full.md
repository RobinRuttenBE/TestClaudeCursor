# Morning Report — 2026-09-05

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-05_ads_report.md`, gecommit en gepusht (f1c9e871). Alleen Meta Ads (Pipeboard via directe JSON-RPC, de MCP meldt "requires authentication") en PostHog (claude.ai connector) gebruikt. Geen Google MCPs, niets naar de Sheet.

## Meta Ads Rapport, 5 september 2026

**Er draait niets meer.** Beide Wholesaler campagnes en alle 8 ads zijn op 4 september tussen 11:50 en 11:52 handmatig gepauzeerd, 25 minuten nadat auto-optimize alleen Statisch 1 (LIT) had stilgezet. Sindsdien geen spend en geen verkeer. Dit rapport is de eindafrekening over 27 augustus t/m 4 september.

| Campagne | Spend | Impr. | Link CTR | Link CPC | CPM | Freq. | Leads Meta | Inzendingen PostHog | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,13 | 90.887 | 1,0% | €0,64 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 1,8% | €0,73 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| Totaal | €1.069,37 | 130.154 | 1,2% | €0,68 | €8,22 | 3,73 | 19 | 33 | €32,41 |

**Belangrijkste bevinding.** De eerste vijf dagen leverden 27 inzendingen op, de laatste vier dagen nog 6, bij stabiel verkeer van rond 200 sessies per dag. De kostprijs per inzending ging van ongeveer €25 naar €67 in de laatste drie draaidagen. De creative fatigue van gisteren is bevestigd, dus de pauze was verdedigbaar.

**Underperformers**
- **Video 1 (SWE)**: €126,75, 0 inzendingen, CPM €15,27. Niet opnieuw activeren.
- **Video 2 (SWE)**: CPM €17,07, duurste link click (€1,11), €63,50 per inzending.
- **Statisch 1 (LIT)**: Link CTR 0,6%, maar wel de beste sessie-naar-inzending ratio van LIT (3,2%).
- **LIT campagne**: frequency 3,97 door vier ad sets op dezelfde audience.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 2,2% link.
- Laagste CPC: Statisch 2 (LIT), €0,43 link.
- Goedkoopste inzendingen: Video 2 (LIT) €28,75 en Video 1 (LIT) €29,38.

**Aanbeveling voor de herstart (70-20-10)**
1. Eerst tracking fixen. Meta ziet 19 leads, PostHog 33, en 9 inzendingen hebben geen UTM. Meta optimaliseert nu op de helft van het signaal.
2. 70% op Video 1 (LIT), Video 2 (LIT) en Statisch 2 (SWE). Richtbudget LIT €60/dag, SWE €40/dag.
3. 20% op dezelfde visuals met nieuwe hooks. Alle 8 ads gebruikten tot nu toe exact dezelfde tekst.
4. 10% op Statisch 1 (LIT) met een nieuwe eerste zin.
5. LIT ad sets samenvoegen zodat de frequency onder 3,5 blijft.

**Opmerkingen**
- Het account `act_607231713057715` uit het command bestaat niet. Het tweede account is AmbitionAvenue, zonder spend.
- Funnel data na de inzending (gesprek gepland, distributeur actief, eerste order) zit niet in Meta of PostHog. Als je die cijfers aanlevert, draai ik de volledige funnel-diagnose.

---

Het rapport staat op `Output/Reports/Daily/2026-09-04_sybb_report.md` en is gecommit en gepusht (commit 53773f3c). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.

**Toegang tot de databronnen.** De Pipeboard MCP meldde "requires authentication" en de PostHog MCP server gaf een 405. Meta data heb ik daarom via de directe Pipeboard JSON-RPC call opgehaald, PostHog data via de claude.ai PostHog connector op project STX EU. Beide leverden volledige data.

**Wat het rapport laat zien voor 4 september:**

- **Meta Ads:** beide SYBB campagnes staan op PAUSED, nul spend en nul impressies over de hele week. De wholesaler campagnes zijn gisteren om 11:50 ook gepauzeerd, dus het account draait nu helemaal niets meer.
- **Landing page startyourballoonbusiness.com:** 0 bezoekers gisteren. De enige 2 pageviews in het 7-daags venster zijn interne tests van 28 augustus.
- **Event registratiepagina's op sempertexeurope.com:** 4 bezoekers in 4 sessies, tegen een 7-daags gemiddelde van 4,9. Drie sessies waren directe hits van 0 seconden op Engelstalige registratie-URL's zonder UTM's, allemaal bounces. Alleen een Duitse bezoeker vergeleek echt twee edities via de event listing.
- **Conversie:** nog steeds niet meetbaar. Geen registratie-voltooid event, en in de SYBB sessies van gisteren geen account-registratie of bestelling.

**Rode vlaggen die nieuw zijn ten opzichte van het rapport van 3 september:**

- Session replay heeft van 28 augustus tot en met 4 september nul opnames vastgelegd, terwijl het product aan staat en de site duizenden bezoekers had. Dat wijst op een uitgeschakelde of geblokkeerde replay-configuratie.
- De drie onherleidbare directe links op de Engelse registratiepagina's lekken attributie, of het zijn link-preview bots.
- Rage clicks concentreren zich op de Odoo accountregistratie, wat de SYBB inschrijving indirect kan raken.

**Top 3 acties in het rapport:** replay-instellingen in PostHog controleren, de bron van de directe Engelse registratie-links achterhalen en vervangen door UTM-versies, en een registratie-voltooid event laten bouwen op de event flow.

Ik heb daarnaast het PostHog geheugen aangevuld met de juiste kolomnamen van de sessions tabel, omdat twee queries daarop stukliepen.

---

Rapport staat in `Output/Reports/Daily/2026-09-05_auto_optimize.md`, gecommit en gepusht (bdc087e3). Alleen Meta Ads (Pipeboard via directe JSON-RPC, de MCP meldt "requires authentication") en PostHog (claude.ai connector) gebruikt. Geen Google MCPs, niets naar de Sheet.

**Geen automatische acties.** Beide Wholesaler campagnes, alle 8 ad sets en alle 8 ads staan sinds 4 september 11:50 op PAUSED. Er is dus niets waarop de kill-regels kunnen draaien. PostHog bevestigt dat het verkeer is gestopt: 1 wholesaler pageview op 5 september. Het tweede account AmbitionAvenue heeft geen campagnes.

**Slotcijfers 2 t/m 4 september**
- Spend €335,49, 47.824 impressions, 473 link clicks, Link CTR 1,0%, CPC (link) €0,71.
- 5 inzendingen in PostHog tegenover 3 leads bij Meta. Dat is €67,10 per inzending, tegen ongeveer €25 in de eerste vijf dagen. De pauze was terecht.
- Video 2 (LIT) en Statisch 1 (LIT) zaten onder de 0,8% Link CTR. Beste ads: Statisch 2 (SWE) met 1,8% Link CTR en Statisch 2 (LIT) met €0,43 CPC (link).

**Voorstellen die op goedkeuring wachten**
1. Tracking fixen voor de herstart. Meta ziet 19 leads, PostHog 33.
2. Budget herverdeling bij herstart, €140/dag: Statisch 2 (SWE) naar €40, Video 1 (LIT) en Statisch 2 (LIT) naar €30, beide SWE video's niet terugzetten.
3. Drie hook-varianten per land op het winnende Statisch 2 visual, plus CTA-test SEE_DETAILS versus APPLY_NOW. Alle 8 ads gebruikten tot nu toe dezelfde tekst.
4. Beslissing over Video 2 (LIT): conversie-guard op de kill-regel (mijn advies) of strikt pauzeren.
5. LIT ad sets samenvoegen naar 2 met Advantage+ budget, SWE audience verbreden naar 21+ en alleen feeds.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
