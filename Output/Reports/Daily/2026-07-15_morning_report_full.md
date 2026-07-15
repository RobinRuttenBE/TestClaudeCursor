# Morning Report — 2026-07-15

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en lokaal opgeslagen. Alleen Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs, geen Sheet-write.

## Meta Ads Rapport — 15 juli 2026

**Belangrijkste bevinding: er draaien nu geen actieve campagnes** in beide accounts (Sempertex Ad Account + AmbitionAvenue, die laatste heeft €0 spend ooit). Ik heb daarom de twee meest recente **gepauzeerde** campagnes gerapporteerd met hun lifetime data.

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**Underperformers:** de kortlopende testkopie "SYBB - Kopie" — CPC €0,64 (>€0,50) én CPM €16,34 (>€15), 0 verkopen. Kwam nooit uit de leerfase.

**Winnaar:** "2026: SYBB" — lage CPC (€0,21), sterke CTR (4,1%), 17,8x ROAS. De enige campagne met echte verkopen én leads.

**Aanbeveling (70-20-10):** budget terug naar de bewezen winnaar heractiveren, stoppen met losse kopie-campagnes met versnipperd budget. Funnel-signaal: grote gap tussen landing page views (6.992) en add-to-cart (53) — bottleneck zit vroeg, sluit aan bij je SYBB bounce/scroll KPI's.

Opgeslagen in: `Output/Reports/Daily/2026-07-15_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` erbovenop.

---

Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-14_sybb_report.md` en gepusht naar GitHub.

## Wat ik vond

**Meta Ads (Pipeboard) — verbonden, maar geen data:**
- Campagne `2026: SYBB` bestaat (ID `120239435987290239`, account `act_567892422940728`) maar staat op **PAUSED**.
- Nul delivery voor de hele week 8–14 juli: 0 impressies, 0 spend, 0 clicks. Dus geen data voor gisteren.
- Ter context, lifetime (13 jan–14 jul): €2.485 spend, 297k impressies, CTR 4,06%, CPC €0,21, 15 leads, 6 purchases. De campagne liép goed — ze is alleen uitgezet.
- Er staat ook een gepauzeerde duplicaat `2026: SYBB - Kopie`.

**PostHog — niet beschikbaar:**
- Er is **geen PostHog MCP verbonden** in deze sessie (wel Pipeboard, Google, Instagram, Canva, Wix, ga4). Landing page data (bounce, scroll, CTA) kon dus niet worden opgehaald.
- Conform je strikte regel heb ik **geen** Google-bron (Sheets/Drive/etc.) als vervanging gebruikt, en niets naar de Tracker-Sheet geschreven.

Het rapport volgt de volledige structuur uit `SKILL.md`, met alle ontbrekende data expliciet gemarkeerd in plaats van verzonnen.

## Belangrijkste acties (staan ook in het rapport)
1. **Beslis of `2026: SYBB` weer aan moet** — heractiveren of de pauze-reden/herstartdatum vastleggen (anders slaat dit dagrapport elke ochtend loos alarm).
2. **PostHog MCP (her)verbinden** via een interactieve sessie (`/mcp` of `claude mcp`) zodat landing page health morgen weer meeloopt.
3. **Duplicaat-campagne opruimen** om verwarring te voorkomen.

Wil je dat ik de PostHog-koppeling nu voor je nakijk, of de campagne-status verder onderzoek?

---

Klaar. Rapport opgeslagen en gepusht.

## Auto-Optimize Rapport — 15 juli 2026

**Geen automatische acties uitgevoerd, geen optimalisaties mogelijk.** Alle campagnes op beide toegankelijke ad accounts staan op PAUSED — er zijn geen actieve ads om te toetsen.

**Data-check (Meta Ads MCP, `last_3d`):**

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | 0 (SYBB + 4 Nozzle Up campagnes allemaal PAUSED) |
| `act_1489853856181844` | ✅ | 0 |
| `act_607231713057715` (secundair uit command) | ❌ geen toegang | n.v.t. |

**Twee aandachtspunten voor jou:**

1. **Account-toegang**: het secundaire account in het command (`act_607231713057715`) is niet bereikbaar met dit token. Het token wijst naar `act_1489853856181844`. Wil je het command-ID corrigeren, of de token-toegang laten uitbreiden?

2. **SYBB staat gepauzeerd** (net als in het rapport van 14 juli). Zolang de campagne uit staat, heeft deze run niets te optimaliseren. Zodra "2026: SYBB" weer live gaat, pikt de volgende auto-optimize run automatisch de kill-regels (Link CTR / CPC link) en 70-20-10-classificatie op.

Rapport: `Output/Reports/Daily/2026-07-15_auto_optimize.md` — uitsluitend lokaal opgeslagen, geen Google MCPs aangeroepen, niet naar de tracker Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
