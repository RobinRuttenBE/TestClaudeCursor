# SYBB Daily Report — 14 July 2026

> Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP. Rapport gegenereerd op 15 July 2026.

## ⚠️ Data-status (lees eerst)

| Bron | Status | Toelichting |
|------|--------|-------------|
| Meta Ads (Pipeboard) | ✅ Verbonden, **geen delivery** | Campagne `2026: SYBB` staat op **PAUSED**. Nul impressies/spend voor 8–14 juli. |
| PostHog | 🔴 **Niet beschikbaar** | Geen PostHog MCP verbonden in deze sessie. Landing page data kon niet worden opgehaald. |

Beide databronnen leverden dus geen bruikbare data voor gisteren. Onderstaande secties zijn ingevuld voor zover mogelijk; ontbrekende data is expliciet gemarkeerd.

---

## 1. Samenvatting

Er is **geen performance-data voor 14 juli**. De Meta-campagne `2026: SYBB` staat gepauzeerd en heeft de hele week (8–14 juli) niets uitgeleverd: nul impressies, nul spend, nul clicks. De PostHog-koppeling is in deze sessie niet beschikbaar, dus landing page gedrag (bounce, scroll, CTA) kon niet worden gemeten. Kortom: de funnel staat stil. Belangrijkste trend van de week is dus simpelweg dat er niets loopt.

Ter context (levensduur van de campagne, 13 jan – 14 jul): €2.485 spend, 297.174 impressies, 12.067 clicks, CTR 4,06%, CPC €0,21, 15 leads en 6 purchases. De campagne hééft dus goed gepresteerd toen ze live stond — ze is nu alleen uitgezet.

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID 120239435987290239) · Status: **PAUSED** · Daily budget: €100,00

| Metric | Gisteren (14 jul) | 7d Gemiddelde (8–14 jul) | Trend |
|--------|-------------------|--------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | — | — | → |
| CPC | — | — | → |
| Frequency | — | — | → |

*Geen delivery in de volledige periode. Alle dag-segmenten (8 t/m 14 juli) kwamen leeg terug uit de Meta API — consistent met de PAUSED-status.*

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| — | — | — | — | — | — |

Geen actieve ads → geen variant-data. Zodra de campagne weer live gaat, wordt hier per `utm_content` (h11_b3_cta5, h12_b3_cta5, …) gerapporteerd.

**Beste variant:** n.v.t. (geen delivery)
**Slechtste variant:** n.v.t. (geen delivery)

## 3. Landing Page Health

🔴 **Geen data** — de PostHog MCP is niet verbonden in deze sessie, dus voor startyourballoonbusiness.com kon geen bounce rate, session duration, scroll depth of CTA click rate worden opgehaald.

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

Niet te berekenen. Zowel de Meta-instroom (paused) als de PostHog-metingen (niet verbonden) ontbreken.

Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)

**Grootste lek:** n.v.t. — funnel staat volledig stil.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat op PAUSED** — er komt geen enkele nieuwe lead of purchase binnen zolang dit zo blijft. Dit is de belangrijkste vlag.
- 🚩 **PostHog MCP niet verbonden** — landing page monitoring ligt stil; ad-pagina mismatches en scroll/CTA-problemen kunnen op dit moment niet gedetecteerd worden.
- ℹ️ Geen CPC-/bounce-/frequency-anomalieën te melden, simpelweg omdat er geen verkeer is.

## 6. Top 3 Acties voor Vandaag

1. **Beslis of `2026: SYBB` weer aan moet.** De campagne presteerde historisch prima (CTR 4,06%, CPC €0,21). Is pauzeren bewust (budget, seizoen, creative refresh) of per ongeluk? → Als ze moet lopen: heractiveren in Meta Ads Manager. Als bewust gepauzeerd: leg de reden en de geplande herstartdatum vast zodat dit dagrapport niet elke ochtend loos alarm slaat. *(Escalatie: Geel — Robin goedkeuring)*
2. **PostHog MCP (her)verbinden.** Zonder PostHog kan dit rapport de kern-cross-reference (ad CTR × landing page gedrag) niet maken. Autoriseer/koppel de PostHog MCP in een interactieve sessie (`/mcp` of `claude mcp`) zodat landing page health morgen weer meeloopt. *(Escalatie: Geel — setup)*
3. **Controleer de duplicaat `2026: SYBB - Kopie`.** Er staat een tweede, ook gepauzeerde kopie (ID 120243293329420239, aangemaakt 19 apr). Ruim op of documenteer waarvoor die dient, om verwarring bij heractivatie en rapportage te voorkomen. *(Escalatie: Groen — opruimen)*

---

### Technische noot
- Meta-account: `act_567892422940728` (Sempertex Ad Account). Campagne-ID `120239435987290239`.
- Dag-breakdown 8–14 juli via Meta Insights API: 7 lege segmenten (geen delivery).
- PostHog: geen `mcp__posthog__*` tools beschikbaar in deze sessie; conform de run-instructie zijn géén Google-bronnen als vervanging gebruikt.
