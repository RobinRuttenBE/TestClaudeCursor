# SYBB Daily Report — 26 June 2026

> Gegenereerd op 27 June 2026. Databronnen: Meta Ads MCP (Pipeboard) + PostHog MCP.
> Rapportperiode: gisteren = **26 June 2026**.

## 1. Samenvatting

Er valt voor gisteren **geen performance te rapporteren**: de campagne `2026: SYBB` stond op **PAUSED** en had nul delivery (geen spend, impressions of clicks) op 26 June 2026 — en in feite gedurende de **volledige laatste 30 dagen**. Daarnaast kon de **PostHog data niet worden opgehaald**: de PostHog MCP leverde deze run geen aanroepbare tools op, dus de landing page health en funnel-analyse ontbreken. Conclusie: de SYBB funnel ligt momenteel stil. De belangrijkste actie is een beslissing over heractivatie, niet optimalisatie.

---

## 2. Meta Ads Performance

**Campagne:** `2026: SYBB` (ID `120239435987290239`)
**Status:** 🔴 PAUSED — daily budget €100,00 ingesteld, maar geen actieve delivery
**Account:** Sempertex Ad Account (`act_567892422940728`)

| Metric | Gisteren (26 Jun) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> De Meta Ads API gaf voor 26 June 2026 een lege dataset terug (`data: []`). Een dag-breakdown over 20–26 June 2026 en een week-breakdown over 28 May–26 June 2026 leverden **op elke dag/week nul delivery** op. De campagne is dus al minimaal een maand niet actief.

### Ad Variant Performance

Geen ad-level data beschikbaar — bij nul delivery zijn er geen impressions of clicks per `utm_content` variant om te rapporteren.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| _geen data_ | — | — | — | — | — |

**Beste variant:** n.v.t. (campagne staat uit)
**Slechtste variant:** n.v.t. (campagne staat uit)

---

## 3. Landing Page Health

⚠️ **PostHog data niet beschikbaar.** De PostHog MCP-server was deze run wel verbonden, maar registreerde geen aanroepbare tools (meerdere tool-lookups gaven geen resultaat). Hierdoor konden pageviews, bounce rate, sessieduur, scroll depth en CTA clicks voor `startyourballoonbusiness.com` **niet** worden opgehaald.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Bounce Rate | geen data | geen data | <55% | ⚪ |
| Avg Session Duration | geen data | geen data | >90s | ⚪ |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | ⚪ |

> Opmerking: zelfs als PostHog beschikbaar was, zou organisch verkeer minimaal zijn omdat er geen betaald verkeer vanuit Meta naar de landing page loopt.

---

## 4. Funnel Drop-off

Niet te berekenen. Stap 1 (betaald verkeer vanuit Meta) is nul, en de PostHog-zijde van de funnel (scroll, CTA click, /booking) is deze run niet op te halen.

```
Pageview (—) → Scroll 50% (—) → CTA Click (—) → /booking (—)
```

**Grootste lek:** De funnel staat aan de bron dicht — er komt geen verkeer in. Dit overschaduwt elk on-page lek.

---

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne volledig dark.** `2026: SYBB` is PAUSED en heeft 0 delivery over de laatste 30 dagen, ondanks een ingesteld dagbudget van €100. Geen leads vanuit de hoofd-acquisitiecampagne.
- 🚩 **PostHog data-integratie faalt.** De PostHog MCP gaf geen tools deze run. Landing page monitoring is hierdoor blind. Dit moet hersteld worden voordat het dagelijkse rapport weer betekenisvol is.
- ℹ️ Er bestaat een duplicaat `2026: SYBB - Kopie` (ID `120243293329420239`, ook PAUSED). Controleer of dit opgeruimd moet worden om verwarring te voorkomen.

---

## 6. Top 3 Acties voor Vandaag

1. **Beslis over heractivatie van `2026: SYBB`.**
   - **Wat:** Bepaal of de campagne weer aangezet wordt (en met welk budget/creatives), of bewust uit blijft.
   - **Waarom:** 30 dagen nul delivery = nul SYBB-leads uit betaald. Zonder besluit blijft de funnel leeg.
   - **Hoe:** Meta Ads Manager → campagne `2026: SYBB` → status + budget controleren, creatives/ad fatigue checken voordat live.
   - **Escalatie:** 🟡 Geel — Robin's goedkeuring nodig (budgetbeslissing).

2. **Herstel de PostHog MCP-koppeling.**
   - **Wat:** Controleer waarom de PostHog MCP geen tools registreert (auth/token, project-config, server-status).
   - **Waarom:** Zonder PostHog is de helft van dit rapport blind; landing page health en funnel zijn niet meetbaar.
   - **Hoe:** MCP-config/credentials voor PostHog nakijken; daarna een testquery op `startyourballoonbusiness.com` draaien.
   - **Escalatie:** 🟡 Geel — technische check vereist.

3. **Ruim het campagne-duplicaat op.**
   - **Wat:** Beoordeel `2026: SYBB - Kopie` en archiveer indien overbodig.
   - **Waarom:** Voorkomt rapportage- en deploy-verwarring tussen twee bijna-identieke campagnes.
   - **Hoe:** Meta Ads Manager → archiveer of hernoem het duplicaat.
   - **Escalatie:** 🟢 Groen — lage impact, snel uit te voeren.

---

*Databron-status: Meta Ads MCP ✅ (campagne dark, 0 delivery) · PostHog MCP ⚠️ niet beschikbaar deze run. Geen Google-bronnen gebruikt, conform run-instructie.*
