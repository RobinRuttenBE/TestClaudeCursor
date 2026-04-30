# SYBB Daily Report — 2026-04-29

> Gegenereerd op 2026-04-30. Databronnen: Meta Ads (Pipeboard MCP). PostHog MCP was niet beschikbaar in deze sessie, dus landing page sectie en cross-referencing zijn beperkt — zie sectie 7.

## 1. Samenvatting
Campagne `2026: SYBB` staat sinds 2026-04-19 op PAUSED. Op 2026-04-29 was er nul activiteit: geen spend, geen impressies, geen clicks. Het rapport heeft vandaag dus geen performance om te analyseren — de hoofdactie is een beslissing over reactivatie of vervanging van de campagne.

## 2. Meta Ads Performance

| Metric | Gisteren (2026-04-29) | 7d Gemiddelde | Trend |
|--------|----------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Status:** Campagne `2026: SYBB` (id `120239435987290239`) is PAUSED. Daily budget staat ingesteld op €100,00, objective `OUTCOME_SALES`, bid strategy `LOWEST_COST_WITHOUT_CAP`. Laatste update op de campagne: 2026-04-19.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h12_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h13_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h14_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h15_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |

26 ads in totaal binnen de campagne (5 hooks × batch B3 × CTA5 plus varianten + 1 legacy "SYBB w/ Semp (BLACK)" ad), allemaal PAUSED sinds 2026-04-19.

**Beste variant:** Niet bepaalbaar (geen activiteit).
**Slechtste variant:** Niet bepaalbaar (geen activiteit).

### Extra observatie
Er bestaat een duplicaat-campagne `2026: SYBB - Kopie` (id `120243293329420239`) aangemaakt op 2026-04-19, eveneens PAUSED. Onduidelijk of dit een staging-duplicaat is of een accidentele kopie. Opruimen of bewust labelen voorkomt verwarring bij volgende launches.

## 3. Landing Page Health

PostHog MCP niet beschikbaar in deze sessie — geen verse data voor 2026-04-29.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

> Met een gepauzeerde campagne is verkeer op startyourballoonbusiness.com sowieso minimaal (alleen organic / direct), dus PostHog-data zou voor deze dag waarschijnlijk weinig signaal opleveren over ad-pagina mismatch.

## 4. Funnel Drop-off

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

Geen funnel-data: campagne paused, geen PostHog-toegang in deze sessie.

**Grootste lek:** Niet bepaalbaar — vandaag is het lek de uitgeschakelde campagne zelf, niet de pagina of de funnel.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne `2026: SYBB` staat sinds 2026-04-19 op PAUSED.** Inmiddels 10 aaneengesloten dagen zonder spend; budget van €100/dag wordt niet benut. Pijplijn voor de SYBB workshop is leeg vanuit Meta Ads.
- 🚩 **Duplicaat campagne `2026: SYBB - Kopie`** aangemaakt op dezelfde dag als de pauze, ook PAUSED. Mogelijk werd gewerkt aan een nieuwe variant die nooit live ging — opvolgen.
- 🚩 **Geen PostHog-zicht in deze run.** Cross-referencing tussen ads en landing page niet mogelijk; de SKILL-flow werkt alleen volledig met beide bronnen tegelijk.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: reactiveren of definitief stoppen.** De campagne staat 10 dagen stil. Concrete keuze nodig:
   - **Reactiveren** met huidige H11–H15 / B3 / CTA5 set → daarna 3-7 dagen later via daily report opnieuw evalueren.
   - **Vervangen** door `2026: SYBB - Kopie` als die een nieuwe creative-batch bevat → live zetten en oude campagne archiveren.
   - **Definitief stoppen** als SYBB workshop op pauze gaat → archiveren beide campagnes en daily report tijdelijk uitschakelen.
   *Waarom:* €100/dag budget × 10 dagen = €1.000 niet besteed; geen leadflow voor SYBB workshop.
   *Hoe:* Meta Ads Manager → campaign status → Active. Of archive de duplicaat.
   *Verwachte impact:* Pas na reactivatie kan rapportage weer waarde leveren.
   *Escalatie:* 🟡 Robin goedkeuring vereist (strategische keuze, niet auto).

2. **Opruimen `2026: SYBB - Kopie`.** Onduidelijk waarom dit duplicaat bestaat. Of mergen met main campagne, of archiveren.
   *Waarom:* Voorkomt verwarring in toekomstige rapporten en MCP-uitvoer.
   *Hoe:* Bevestig met Robin → archiveren in Meta Ads Manager.
   *Verwachte impact:* Schoner rapport, minder ruis in queries.
   *Escalatie:* 🟢 Auto na Robin's bevestiging.

3. **PostHog MCP-verbinding herstellen.** De skill `daily-sybb-report` werkt alleen volledig met PostHog naast Meta Ads. Vandaag was die niet bereikbaar in de sessie.
   *Waarom:* Zonder PostHog kan ad-pagina mismatch (high CTR + high bounce, scroll cliffs, CTA-click rate) niet gedetecteerd worden. Dat is precies de cross-referencing waarde die de skill omschrijft.
   *Hoe:* Check MCP-config (`.mcp.json` of harness settings), herstart PostHog server, verifieer met een testcall.
   *Verwachte impact:* Volgende daily report kan weer landing page health en funnel drop-off bevatten.
   *Escalatie:* 🟡 Robin moet MCP-config controleren (niet auto-fixable vanuit Claude).

## 7. Notities over deze run

- **Meta Ads (Pipeboard):** geauthenticeerd, alle calls geslaagd. Account `act_567892422940728` (Sempertex Ad Account, EUR, lifetime spend €4.867,46).
- **PostHog:** geen `mcp__posthog__*` tools beschikbaar in deze sessie. Sectie 3 en 4 daardoor zonder data.
- **Strikte regel actief:** Geen Google MCPs aangeroepen (Gmail, Calendar, Drive, Sheets, Docs, Slides). Geen schrijfacties naar Meta Ads Tracker Google Sheet. Output uitsluitend lokaal in `Output/Reports/Daily/`.
- **Vergelijkingsperiode (laatste sybb_report met data):** 2026-04-27 — daarna twee dagen geen daily sybb_report en sinds 2026-04-19 geen ad-activiteit.
