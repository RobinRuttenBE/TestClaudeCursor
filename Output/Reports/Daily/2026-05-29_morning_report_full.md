# Morning Report — 2026-05-29

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 29 May 2026

⚠️ **Geen actieve campagnes** op beide toegankelijke accounts. Het rapport toont daarom de laatste bekende (lifetime) performance van de recentste gepauzeerde campagnes op het Sempertex account. Het account `act_607231713057715` uit de command is niet bereikbaar via deze connectie; ik zag wel AmbitionAvenue (`act_1489853856181844`, €0 spend, 0 campagnes).

**Overzicht (gepauzeerd, gesorteerd op spend):**

| Campagne | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| 2026: SYBB - Kopie | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

**Top performers:** ad **H13,B3,CTA5** is de absolute winnaar — 9,8% CTR en €0,07 CPC. De hoofdcampagne SYBB zit op elke drempel ruim goed.

**Underperformers:** de Kopie-campagne (CPC €0,64 + CPM €16,34, 0 purchases), ad **H11,B3,CTA5** (€521 spend, CPC €0,67 — grootste budgetlek), en **SYBB w/ Semp (BLACK)** (CTR 1,0%, CPC €0,61).

**⚠️ ROAS niet betrouwbaar:** €44.247 op 6 purchases = €7.374 per order. Dat is onrealistisch voor de SYBB-funnel en wijst op een verkeerd geconfigureerde pixel-waarde. Fix de pixel value-tracking vóór je ROAS-beslissingen neemt — de volume-metrics (clicks, CTR, CPC, 53 add-to-cart, 36 checkouts, 15 leads) zijn wél betrouwbaar.

**Aanbeveling (70-20-10):** bouw bij heractivatie op de bewezen winnaar H13 (70%), H15 als variatie (20%), schrap de dure low-CTR ads.

Volledig rapport opgeslagen in `Output/Reports/Daily/2026-05-29_ads_report.md` (gecommit + gepusht). Google Sheet-stap overgeslagen conform run-instructie.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-05-28_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevinding: er is bijna niets te rapporteren — en dat is het verhaal

**Meta Ads — geen data:** De campagne `2026: SYBB` (`120239435987290239`, account "Sempertex Ad Account") staat op **PAUSED** sinds ~19 april. Nul spend, nul impressies, nul klikken — zowel voor gisteren als voor heel mei. De `- Kopie` variant staat ook op paused. Er is dus geen ad-performance om te meten.

**PostHog — organische druppel:** De landingspagina kreeg gisteren **3 pageviews van 2 unieke bezoekers**, tegenover ~1 pageview/dag de week ervoor. Bronnen: een link-in-bio domein (`t-sml.mtrbio.com`) en direct verkeer. **Geen** `utm_medium=cpc` verkeer — bevestigt dat alles organisch is.

**Twee meet-beperkingen die ik moet melden:**
1. Dit PostHog project heeft **geen scroll-depth, CTA-click of `$pageleave` events** geconfigureerd. Bounce rate, scroll depth en CTA click rate uit de skill-structuur zijn dus simpelweg niet meetbaar — ik heb die cellen op "niet gemeten" gezet in plaats van getallen te verzinnen.
2. Bij 3 pageviews zou geen enkele ratio toch statistisch betekenisvol zijn.

**Top 3 acties** (in het rapport): (1) beslissen of de campagne weer aan moet — dit is de hoofdoorzaak van alle nullen, (2) on-page tracking live zetten vóór reactivering zodat het rapport niet blind blijft, (3) UTM-tagging verifiëren vóór de campagne aangaat.

Eén ding om te bevestigen: wil je dat ik je help de campagne te reactiveren (doel/budget/periode), of staat hij bewust uit?

---

Klaar. Rapport opgeslagen en gecommit.

## Auto-Optimize Rapport — 29 May 2026

**Geen optimalisaties uitgevoerd: er zijn geen actieve campagnes.**

Wat ik vond (alleen via Meta Ads MCP, geen Google MCPs):

| Account | Resultaat |
|---------|-----------|
| `act_567892422940728` (primair) | 0 actieve campagnes — alles PAUSED |
| `act_1489853856181844` | 0 actieve campagnes |
| `act_607231713057715` | **Niet toegankelijk** met huidige token |

Alle campagnes op het primaire account staan op PAUSED, inclusief **2026: SYBB** (dagbudget €100,00). Daardoor:

- ⚡ **0 ads gepauzeerd** (geen actieve ads om tegen de kill-regels Link CTR < 0,8% / CPC link > €1,50 te toetsen)
- ⚠️ Geen fatigue/CPM-waarschuwingen
- 📊 70-20-10 classificatie niet van toepassing
- 💡 Geen budgetvoorstellen mogelijk zonder live data

**Twee aandachtspunten:**

1. **2026: SYBB staat op PAUSED.** Als die campagne actief hoort te zijn, moet hij eerst worden geactiveerd voordat dit command iets kan optimaliseren. Wil je dat ik de campagne (na jouw goedkeuring) weer activeer? Dan draai ik het rapport opnieuw met echte data.
2. **Account `act_607231713057715`** uit het command is niet bereikbaar met de huidige Pipeboard-token (toegestaan: `act_1489853856181844`, `act_567892422940728`). Als dat account meegenomen moet worden, is een re-auth met de juiste toegang nodig.

Rapport: `Output/Reports/Daily/2026-05-29_auto_optimize.md` (gecommit en gepusht).

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
