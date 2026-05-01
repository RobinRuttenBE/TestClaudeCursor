# SYBB Daily Report — 2026-04-30

> Gegenereerd op 2026-05-01. Databronnen: Meta Ads (Pipeboard MCP). PostHog MCP was niet beschikbaar in deze sessie, dus landing page sectie en cross-referencing zijn beperkt — zie sectie 7.

## 1. Samenvatting
Campagne `2026: SYBB` staat sinds 2026-04-19 op PAUSED. Op 2026-04-30 was er geen spend, geen impressies, geen clicks. Inmiddels 11 aaneengesloten dagen zonder activiteit, terwijl het daily budget van €100 ongebruikt blijft. Het rapport heeft vandaag opnieuw geen performance om te analyseren — de hoofdactie blijft een beslissing over reactivatie of vervanging van de campagne.

## 2. Meta Ads Performance

| Metric | Gisteren (2026-04-30) | 7d Gemiddelde | Trend |
|--------|----------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Status:** Campagne `2026: SYBB` (id `120239435987290239`) is PAUSED. Daily budget staat ingesteld op €100,00, objective `OUTCOME_SALES`, bid strategy `LOWEST_COST_WITHOUT_CAP`. Laatste update op de campagne: 2026-04-19. Budget remaining: €100,00. Configured status én effective status zijn beide PAUSED.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h12_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h13_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h14_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h15_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |

Alle ads in de campagne zijn PAUSED sinds 2026-04-19; geen impressies te attribueren per utm_content.

**Beste variant:** Niet bepaalbaar (geen activiteit).
**Slechtste variant:** Niet bepaalbaar (geen activiteit).

### Extra observatie
`2026: SYBB - Kopie` (id `120243293329420239`, aangemaakt 2026-04-19) staat eveneens PAUSED. Geen impressies of spend in de afgelopen 7 dagen. Geen andere ACTIVE campagnes in account `act_567892422940728` — er is op dit moment dus geen enkele ad-activiteit in het hele account.

## 3. Landing Page Health

PostHog MCP niet beschikbaar in deze sessie — geen verse data voor 2026-04-30.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

> Met een gepauzeerde campagne en geen andere ACTIVE campagnes is het verkeer op startyourballoonbusiness.com sowieso minimaal (alleen organic / direct). PostHog-data zou voor deze dag waarschijnlijk weinig signaal opleveren over ad-pagina mismatch.

## 4. Funnel Drop-off

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

Geen funnel-data: campagne paused, geen PostHog-toegang in deze sessie.

**Grootste lek:** Niet bepaalbaar — vandaag is het lek nog steeds de uitgeschakelde campagne zelf, niet de pagina of de funnel.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne `2026: SYBB` staat sinds 2026-04-19 op PAUSED — dag 11.** Cumulatief €1.100 niet-besteed budget (€100/dag × 11 dagen). Pijplijn voor de SYBB workshop blijft leeg vanuit Meta Ads.
- 🚩 **Geen ACTIVE campagnes in account `act_567892422940728`.** Filter op status ACTIVE geeft een lege lijst terug; er is geen enkele draaiende ad-campagne, niet alleen voor SYBB.
- 🚩 **Duplicaat `2026: SYBB - Kopie` blijft staan.** Sinds 2026-04-19 PAUSED, geen activiteit. Of inzetten of opruimen — sleept nu al 11 dagen mee.
- 🚩 **PostHog MCP nog steeds niet beschikbaar.** Zelfde issue als gisteren: cross-referencing tussen ads en landing page niet mogelijk. Skill werkt alleen volledig met beide bronnen.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag: reactiveren of definitief stoppen.** De campagne staat 11 dagen stil. Concrete keuze is overdue:
   - **Reactiveren** met huidige H11–H15 / B3 / CTA5 set → daarna 3-7 dagen later via daily report opnieuw evalueren.
   - **Vervangen** door `2026: SYBB - Kopie` als die een nieuwe creative-batch bevat → live zetten en oude campagne archiveren.
   - **Definitief stoppen** als SYBB workshop op pauze gaat → archiveren beide campagnes en daily report tijdelijk uitschakelen om ruis te voorkomen.
   *Waarom:* €100/dag × 11 dagen = €1.100 niet besteed; geen leadflow voor SYBB workshop; daily report draait leeg.
   *Hoe:* Meta Ads Manager → campaign status → Active. Of archive de duplicaat.
   *Verwachte impact:* Pas na reactivatie kan rapportage weer waarde leveren.
   *Escalatie:* 🟡 Robin goedkeuring vereist (strategische keuze, niet auto).

2. **Opruimen `2026: SYBB - Kopie`.** Onduidelijk waarom dit duplicaat bestaat. Of mergen met main campagne, of archiveren.
   *Waarom:* Voorkomt verwarring in toekomstige rapporten en MCP-uitvoer; sleept nu 11 dagen mee zonder doel.
   *Hoe:* Bevestig met Robin → archiveren in Meta Ads Manager.
   *Verwachte impact:* Schoner rapport, minder ruis in queries.
   *Escalatie:* 🟢 Auto na Robin's bevestiging.

3. **PostHog MCP-verbinding herstellen.** De skill `daily-sybb-report` werkt alleen volledig met PostHog naast Meta Ads. Tweede dag op rij niet bereikbaar.
   *Waarom:* Zonder PostHog kan ad-pagina mismatch (high CTR + high bounce, scroll cliffs, CTA-click rate) niet gedetecteerd worden. Dat is precies de cross-referencing waarde die de skill omschrijft. Bovendien: zelfs met paused campagne is organic / direct verkeer op startyourballoonbusiness.com nuttig om in beeld te hebben.
   *Hoe:* Check MCP-config (`.mcp.json` of harness settings), herstart PostHog server, verifieer met een testcall.
   *Verwachte impact:* Volgende daily report kan weer landing page health en funnel drop-off bevatten zodra er weer ad-traffic is.
   *Escalatie:* 🟡 Robin moet MCP-config controleren (niet auto-fixable vanuit Claude).

## 7. Notities over deze run

- **Meta Ads (Pipeboard):** geauthenticeerd, alle calls geslaagd. Account `act_567892422940728` (Sempertex Ad Account, EUR). Insights voor zowel `2026: SYBB` als `2026: SYBB - Kopie` voor 2026-04-30 én 2026-04-23..29 retourneren een lege `data`-array — bevestigt geen activiteit.
- **PostHog:** geen `mcp__posthog__*` tools beschikbaar in deze sessie. Sectie 3 en 4 daardoor zonder data.
- **Strikte regel actief:** Geen Google MCPs aangeroepen (Gmail, Calendar, Drive, Sheets, Docs, Slides). Geen schrijfacties naar Meta Ads Tracker Google Sheet. Output uitsluitend lokaal in `Output/Reports/Daily/`.
- **Vergelijkingsperiode:** Laatste sybb_report met data is 2026-04-18 (laatste dag voor pauze). Sinds 2026-04-19 elf dagen op rij geen ad-activiteit; rapport blijft daardoor structureel leeg tot reactivatie.
