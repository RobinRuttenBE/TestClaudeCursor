# SYBB Daily Report — 22 juli 2026

## 1. Samenvatting
De SYBB funnel stond gisteren volledig stil. De Meta campagne `2026: SYBB` is PAUSED (al sinds 19 april 2026), dus er was nul spend, nul impressies en nul clicks. De landing page (www.startyourballoonbusiness.com) kreeg gisteren 0 pageviews; de laatste bezoeker was op 21 juli. Er is dus geen betaald verkeer en nagenoeg geen organisch verkeer naar de funnel. Dit is geen performance-probleem maar een aan/uit-probleem: de campagne draait niet.

> Databronnen: Meta Ads (Pipeboard MCP, account `act_567892422940728` — Sempertex Ad Account) en PostHog (project "Default project", EU). Beide bevestigen onafhankelijk dat de funnel inactief was op 22-07-2026.

## 2. Meta Ads Performance
Campagne `2026: SYBB` (ID `120239435987290239`) — **status: PAUSED**, dagbudget €100,00 (niet actief).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Insights API gaf een lege dataset terug voor zowel 22-07-2026 als het venster 16-07 t/m 22-07. De campagne levert niets uit omdat hij op pauze staat.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen actieve ads) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t. — geen delivery.
**Slechtste variant:** n.v.t. — geen delivery.

## 3. Landing Page Health
Host: `www.startyourballoonbusiness.com`. Gisteren 0 pageviews, dus geen sessie-metrics te berekenen. Ter context het trailing 7-daags patroon (allemaal organisch/direct, geen Meta UTM's):

| Dag | Pageviews | Unieke bezoekers |
|-----|-----------|------------------|
| 15 jul | 1 | 1 |
| 16 jul | 2 | 2 |
| 17 jul | 3 | 3 |
| 18 jul | 3 | 3 |
| 19 jul | 2 | 2 |
| 20 jul | 6 | 6 |
| 21 jul | 1 | 1 |
| **22 jul** | **0** | **0** |

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | ~2,3/dag | meten | 🔴 |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ geen data |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ geen data |
| Scroll 25/50/75/100% | n.v.t. | n.v.t. | >80/60/40/20% | ⚪ geen data |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | ⚪ geen data |

Er is te weinig volume (piek van 6 views op één dag) om bounce rate, scroll depth of CTA-clicks betrouwbaar te meten. Dit verkeer is bovendien niet afkomstig van de SYBB advertenties, want er stond gisteren geen enkele `utm_source=meta` / `utm_campaign=sybb` hit in PostHog.

## 4. Funnel Drop-off
Pageview (0) → Scroll 50% (0) → CTA Click (0) → /booking (0)

**Grootste lek:** de funnel begint niet. Er is geen instroom bovenaan omdat de betaalde campagne uit staat. Zonder verkeer is er geen drop-off te analyseren.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSE.** `2026: SYBB` levert al sinds 19-04-2026 niets uit. Als de bedoeling was dat SYBB draait, dan lekt hier budget-tijd, geen budget-geld: elke dag zonder delivery is een dag zonder leads.
- 🚩 **Nul LP-verkeer op een dag (0 bezoekers).** De landing page kreeg gisteren geen enkele bezoeker. Het weinige verkeer van de afgelopen week (1 tot 6/dag) is organisch/direct, niet vanuit ads.
- 🚩 **Geen SYBB UTM-verkeer.** Geen enkele hit met `utm_source=meta` of `utm_campaign=sybb`, wat bevestigt dat er geen advertentie-instroom is.
- ℹ️ Ter info: het PostHog-project meet vooral `www.sempertexeurope.com` (5.086 pageviews gisteren). Dat is de corporate B2B-site, niet de SYBB-funnel. De SYBB landing page is een aparte, momenteel vrijwel slapende, host.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of SYBB weer aan moet.** Als de campagne hoort te draaien: activeer `2026: SYBB` in Meta Ads Manager (of de nieuwere `2026: SYBB - Kopie`, ID `120243293329420239`, ook PAUSED). Zo niet: bevestig dat SYBB bewust uit staat, zodat dit dagelijkse rapport geen valse alarmen blijft geven. *(Escalatie: Rood — strategiebeslissing, vereist jouw goedkeuring.)*
2. **Controleer de tracking op de landing page.** Verifieer dat `www.startyourballoonbusiness.com` correct de PostHog pixel en de UTM-parameters doorgeeft, zodat er bij heractivatie meteen schone data binnenkomt (bounce rate, scroll depth, CTA clicks). Nu ontbreken die events volledig. *(Escalatie: Geel — check + eventueel technische fix.)*
3. **Bevestig de databron-scope.** De SYBB landing page zit in hetzelfde PostHog-project als de corporate site. Leg vast dat rapportage op host `www.startyourballoonbusiness.com` filtert (niet op projecttotalen), zodat toekomstige rapporten SYBB-cijfers niet vermengen met sempertexeurope.com. *(Escalatie: Groen — administratief.)*

---
*Rapport gegenereerd 23-07-2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP. Geen Google-diensten geraadpleegd, geen schrijfacties naar externe trackers.*
