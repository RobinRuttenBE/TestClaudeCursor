## Ochtendrapport -- 31 maart 2026

### Agenda vandaag
Geen afspraken vandaag. Focus dag!

### Laatste 5 emails
- **robin.rutten2@gmail.com** -- "Morning Report FAILED -- 31-03-2026" > Het automatische morning report is mislukt. Check logs: `logs/morning-report-2026-03-31.log`
- **Social Deal Hasselt** -- "Gehele dag entree voor de sauna bij La Nostra Vita" > Deals aanbieding (niet relevant)
- **Ochtend - Nieuwsblad** -- "FOD Financien wil werknemers met fitness lokken" > Nieuwsbrief (niet relevant)
- **Social Deal Kempen** -- "3-gangendiner a la carte bij Brasserie La Perla" > Deals aanbieding (niet relevant)
- **Bloomberg** -- "How high could oil prices get?" > Market news over olieprijzen (niet relevant)

### Recente Drive activiteit
- **Meta ads tracker (niet clean)** -- laatst gewijzigd 30-03-2026 13:41
- **Mailjet Campaign Statistics** -- laatst gewijzigd 30-03-2026 13:24
- **STX EU Email Batch March/April 2026 (14 emails)** -- laatst gewijzigd 30-03-2026 12:14
- **Social media tracker** -- laatst gewijzigd 14-03-2026
- **Email flows master** (spreadsheet) -- laatst gewijzigd 14-03-2026
- **Email Flows Master -- Sempertex Europe** (document) -- laatst gewijzigd 14-03-2026
- **UTM & Tracking Reference** -- laatst gewijzigd 14-03-2026
- **Content Kalender Q2 2025** (map) -- laatst gewijzigd 12-03-2026
- **Top Content Analyse** (map) -- laatst gewijzigd 12-03-2026
- **Campagne Templates** (map) -- laatst gewijzigd 12-03-2026

### Meta Ads Performance -- SYBB

**Campagne PAUSED sinds 08-03-2026. Geen actieve spend.**

Lifetime performance (13 jan - 8 mrt 2026):

| Metric | Lifetime | Gemiddelde |
|--------|----------|------------|
| Spend | EUR 1.323,83 (last 30d) | ~EUR 24/dag (actieve periode) |
| Impressions | 189.067 | |
| Link Clicks | 9.703 | |
| CTR | 5,27% | |
| CPC | EUR 0,13 | |
| Landing Page Views | 6.174 | |
| Leads (pixel) | 15 | |
| Cost per Lead | EUR 88,26 | |
| Video Views | 47.643 | |

**Ad-level ranking (lifetime):**

| Ad | Spend | CTR | CPC | LP Views | Leads | CPL |
|----|-------|-----|-----|----------|-------|-----|
| H13,B3,CTA5 | EUR 421 | 9,82% | EUR 0,07 | 4.063 | 3 | EUR 140 |
| H15,B3,CTA5 | EUR 217 | 4,26% | EUR 0,15 | 842 | 0 | - |
| H14,B3,CTA5 | EUR 109 | 3,68% | EUR 0,18 | 357 | 1 | EUR 109 |
| H12,B3,CTA5 | EUR 374 | 2,54% | EUR 0,31 | 467 | 5 | EUR 75 |
| H11,B3,CTA5 | EUR 202 | 2,56% | EUR 0,25 | 445 | 6 | EUR 34 |
| SYBB w/ Semp (BLACK) | EUR 102 | 1,03% | EUR 0,61 | 0 | 0 | - |

**Beste ad (traffic):** H13,B3,CTA5 -- CTR 9,82%, CPC EUR 0,07, verantwoordelijk voor 65% van alle LP views. Duidelijke winnaar qua klikvolume.

**Beste ad (conversie):** H11,B3,CTA5 -- Laagste cost per lead (EUR 33,75) met 6 leads. Beste ROI ondanks lagere CTR.

**Slechtste ad:** SYBB w/ Semp (BLACK) -- CTR 1,03%, CPC EUR 0,61, geen enkele landing page view of lead. Statische ad die duidelijk niet werkt.

### Landing Page Health -- PostHog

**PostHog token is verlopen. Kan geen data ophalen.**

Actie vereist: Re-autoriseer PostHog MCP server om landing page analytics te herstellen.

| Metric | Gisteren | Target | Status |
|--------|----------|--------|--------|
| Bezoekers | ? | - | - |
| Bounce Rate | ? | <55% | ? |
| Scroll 50%+ | ? | >60% | ? |
| Scroll 100% | ? | >20% | ? |
| CTA Click Rate | ? | >4% | ? |
| Sessie duur | ? | >90s | ? |

**Session recordings:** Niet beschikbaar (token verlopen)

### Rode Vlaggen
- !! **PostHog MCP token verlopen** -- Geen landing page analytics beschikbaar. Moet opnieuw geautoriseerd worden.
- !! **Morning report automatisering faalt** -- Het automatische morning report (launchd) is mislukt. Check `logs/morning-report-2026-03-31.log`.
- **SYBB campagne staat PAUSED** sinds 08-03-2026 (23 dagen geleden). Geen actieve lead generatie.

### Funnel Diagnose
Geen actieve campagnes. Geen funnel data beschikbaar.

Laatste bekende funnel data (voor pauze op 8 maart):
- 189K impressies > 9.703 link clicks (5,1% CTR) > 6.174 LP views (63,6% van clicks) > 15 leads (0,24% LP conversie)
- **Bottleneck:** LP conversie (0,24%) is ver onder target van 5%. De landing page converteert slecht ondanks goed ad traffic volume.

### Top 3 Acties voor Vandaag
1. **Re-autoriseer PostHog MCP** -- Zonder analytics ben je blind op LP performance. Fix dit eerst zodat je weer data hebt wanneer de campagne herstart.
2. **Fix morning report automatisering** -- Check de log file en herstel het launchd script zodat het rapport weer automatisch draait.
3. **Evalueer SYBB herstart** -- De campagne staat al 23 dagen op pauze. Plan wanneer je herstart, met focus op de twee winnende ads: H13 (volume) en H11 (conversie). Overweeg de statische BLACK ad te verwijderen.

Prioriteit gebaseerd op: impact x snelheid van implementatie
