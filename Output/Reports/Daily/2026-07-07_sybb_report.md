# SYBB Daily Report — 7 juli 2026

> Gegenereerd op 8 juli 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP.
> Rapportperiode: gisteren, **7 juli 2026**.

## 1. Samenvatting

Er valt vandaag weinig te rapporteren: de campagne **"2026: SYBB" staat op PAUSED** en heeft op 7 juli 2026 **geen spend, impressies of clicks** gedraaid. Ook de volledige week 1–7 juli 2026 laat nul activiteit zien. Zonder betaald verkeer is er geen ad-performance en geen ad-gedreven landing page-data om te analyseren. Daarnaast was de **PostHog MCP deze run niet beschikbaar** (server verbond niet), dus landing page-metrics konden niet worden opgehaald.

**Belangrijkste trend:** campagne ligt stil sinds medio april 2026 (laatste wijziging 19 april). Zolang de campagne PAUSED blijft, blijft dit rapport leeg.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID 120239435987290239) — status **PAUSED**, daily budget €100,00, objective OUTCOME_SALES.

| Metric | Gisteren (7 jul) | 7d Gemiddelde (1–7 jul) | Trend |
|--------|------------------|--------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> Meta Insights gaf voor 7 juli een lege dataset terug, en voor elke dag in 1–7 juli eveneens nul. Dit is consistent met de PAUSED-status.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t. — geen ads actief.
**Slechtste variant:** n.v.t. — geen ads actief.

## 3. Landing Page Health

**Status: data niet beschikbaar.** De PostHog MCP was tijdens deze run niet verbonden, waardoor pageviews, bounce rate, session duration, scroll depth en CTA clicks voor startyourballoonbusiness.com niet opgehaald konden worden.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | — | — | <55% | ⚪ geen data |
| Avg Session Duration | — | — | >90s | ⚪ geen data |
| Scroll 25% | — | — | >80% | ⚪ geen data |
| Scroll 50% | — | — | >60% | ⚪ geen data |
| Scroll 75% | — | — | >40% | ⚪ geen data |
| Scroll 100% | — | — | >20% | ⚪ geen data |
| CTA Click Rate | — | — | >4% | ⚪ geen data |

> Let op: ook als PostHog wél beschikbaar was geweest, zou ad-gedreven verkeer nul zijn (campagne PAUSED). Eventueel organisch/direct verkeer kan er wel zijn, maar dat kon nu niet gemeten worden.

## 4. Funnel Drop-off

Niet te berekenen. Er is geen betaald verkeer (Meta Ads = 0) en geen PostHog-data om de funnel Pageview → Scroll 50% → CTA Click → /booking op te bouwen.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne PAUSED** — "2026: SYBB" draait niet en heeft de hele week 1–7 juli nul spend. Als deze campagne actief hoort te zijn, is dit de meest urgente bevinding.
- 🚩 **PostHog MCP niet beschikbaar** — landing page-monitoring ontbreekt in deze run. Zonder deze bron is cross-referencing (ad ↔ pagina) onmogelijk.

## 6. Top 3 Acties voor Vandaag

1. **Beslis of "2026: SYBB" weer aan moet.** *Wat:* controleer in Meta Ads Manager of de pauze bewust is. *Waarom:* nul spend sinds ~19 april; geen enkele lead-flow via deze campagne. *Escalatie:* Rood (strategie/Robin) — pas budget/activatie niet automatisch aan.
2. **Herstel de PostHog MCP-verbinding.** *Wat:* verbind de PostHog MCP opnieuw (via /mcp in een interactieve sessie of connector-instellingen) zodat landing page-data weer meegenomen wordt. *Waarom:* zonder PostHog mist het rapport de helft van zijn waarde (LP health + cross-reference). *Escalatie:* Geel.
3. **Verifieer de rapport-trigger.** *Wat:* bevestig dat dit dagelijkse rapport op een campagne draait die daadwerkelijk live is; overweeg de trigger te pauzeren zolang "2026: SYBB" PAUSED staat. *Waarom:* voorkomt dagelijkse lege rapporten. *Escalatie:* Groen.

---

### Databron-notitie
- **Meta Ads (Pipeboard MCP):** succesvol bevraagd. Account `act_567892422940728` (Sempertex Ad Account). Campagne `2026: SYBB` — PAUSED, 0 activiteit 1–7 juli 2026.
- **PostHog MCP:** niet beschikbaar in deze sessie (server verbond niet; geen tools blootgesteld). Landing page-secties konden niet gevuld worden.
- Conform de striktregel voor deze run zijn uitsluitend Meta Ads MCP en (poging tot) PostHog MCP gebruikt. Geen Google-services aangeroepen; niet naar de Google Sheet-tracker geschreven.
