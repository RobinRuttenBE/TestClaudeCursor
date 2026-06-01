# SYBB Daily Report — 31 May 2026

> Gegenereerd op 1 June 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP — conform de strikte bron-restrictie voor deze run (geen Google-bronnen gebruikt).

## 1. Samenvatting
Er is **niets te rapporteren over advertentieprestaties** voor 31 May 2026: de campagne **`2026: SYBB`** stond op **PAUSED** en heeft die dag (en de hele afgelopen 7 dagen) **geen delivery** gehad. Op accountniveau was er gisteren **€0 spend** in het hele Sempertex-advertentieaccount. Daarnaast kon de **PostHog data niet worden opgehaald**: de PostHog MCP is in deze sessie niet verbonden, dus landing page health (bounce, scroll, CTA) ontbreekt. Belangrijkste actie: campagne weer activeren én PostHog-koppeling herstellen voordat dit rapport waarde levert.

## 2. Meta Ads Performance
**Campagne:** `2026: SYBB` (ID `120239435987290239`) — status **PAUSED**, daily budget €100, objective OUTCOME_SALES.

| Metric | Gisteren (31 May) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0 | €0 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Meta Insights gaf voor 31 May en voor de periode 25–31 May een lege dataset terug, zowel op campagne- als op accountniveau. De campagne levert dus niet uit.

### Ad Variant Performance
Geen data beschikbaar — de campagne stond gepauzeerd, dus er zijn geen impressies of clicks per `utm_content`-variant (h11_b3_cta5 t/m h15_b3_cta5). Zodra de campagne weer loopt, vult deze tabel zich.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health
**Niet beschikbaar.** De PostHog MCP is in deze sessie niet verbonden (geen `mcp__posthog__*` tools beschikbaar). Conform de strikte bron-restrictie is er **niet** uitgeweken naar een Google-bron of GA4 als vervanging.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

## 4. Funnel Drop-off
Niet te berekenen. Funnel-analyse vereist zowel Meta-traffic (stap: ad click) als PostHog-events (pageview → scroll 50% → CTA click → /booking). Beide ontbreken voor 31 May (geen ad-delivery + geen PostHog-verbinding).

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** niet vast te stellen zonder data.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne `2026: SYBB` staat op PAUSED** — geen enkele euro spend op 31 May, en geen delivery in de afgelopen 7 dagen. Dit is de hoofdoorzaak van het ontbreken van Meta-data.
- 🚩 **PostHog MCP niet verbonden** — landing page health, scroll depth, CTA-clicks en session recordings konden niet worden opgehaald. Het rapport mist daardoor de helft van zijn waarde (de cross-referencing tussen ad-gedrag en pagina-gedrag).
- ⚠️ Zolang beide bovenstaande punten openstaan, kan dit dagrapport geen betekenisvolle optimalisatie-signalen geven.

## 6. Top 3 Acties voor Vandaag
1. **Beslis of `2026: SYBB` weer aan moet** — de campagne staat sinds 19 April op PAUSED. Als SYBB actief gemonitord moet worden, activeer de campagne in Meta Ads Manager (of bevestig dat hij bewust uit staat, zodat dit dagrapport gepauzeerd kan worden). *Waarom:* €0 delivery 7 dagen op rij. *Impact:* zonder dit blijft elk dagrapport leeg.
2. **Herstel de PostHog MCP-verbinding** — controleer of de PostHog MCP-server correct is gekoppeld in deze omgeving (de tools `mcp__posthog__*` waren niet beschikbaar). *Waarom:* landing page health is de kern van het SYBB-rapport. *Impact:* maakt bounce/scroll/CTA-tracking en funnel drop-off weer mogelijk.
3. **Verifieer dat de PostHog landing page (`startyourballoonbusiness.com`) nog correct tracking heeft** zodra de MCP weer werkt — pageviews, scroll-events (25/50/75/100%) en CTA-clicks met de juiste `utm_content`. *Waarom:* bij heractivatie van de campagne moet de tracking meteen kloppen. *Impact:* voorkomt dat de eerste dagen na heractivatie alsnog datagaten opleveren.

---

### Databron-status (deze run)
- ✅ **Meta Ads MCP (Pipeboard):** verbonden en bevraagd. Account `act_567892422940728` (Sempertex Ad Account). Campagne `2026: SYBB` = PAUSED, 0 delivery op 31 May en 25–31 May.
- ❌ **PostHog MCP:** niet beschikbaar in deze sessie (geen tools gevonden).
- 🚫 **Niet gebruikt (conform strikte regel):** Gmail, Google Calendar, Google Drive, Google Sheets, Google Docs, Google Slides, GA4. Er is ook niet naar de Meta Ads Tracker Google Sheet geschreven.
