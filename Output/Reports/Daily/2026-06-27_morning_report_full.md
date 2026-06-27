# Morning Report — 2026-06-27

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Connection closed mid-response. The response above may be incomplete.

---

Klaar. Het rapport staat opgeslagen op `Output/Reports/Daily/2026-06-26_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevindingen

**Meta Ads — campagne ligt stil** 🔴
De campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED** en had **nul delivery op 26 juni**. Ik heb dit breder gecheckt: een dag-breakdown (20–26 jun) én een week-breakdown (28 mei–26 jun) gaven op élke periode een lege dataset. De campagne is dus al **minimaal 30 dagen dark**, ondanks een ingesteld dagbudget van €100. Er bestaat ook een duplicaat `2026: SYBB - Kopie` (ook paused).

**PostHog — data niet beschikbaar** ⚠️
De PostHog MCP-server was wel verbonden maar registreerde deze run **geen aanroepbare tools**. Ik heb het meerdere keren geprobeerd (verschillende zoektermen + directe selectie) — zonder resultaat. Landing page health, scroll depth, bounce rate en funnel-analyse konden daardoor niet worden opgehaald.

Conform je strikte instructie heb ik **geen enkele Google MCP** aangeroepen en alles uitsluitend lokaal opgeslagen.

## Top 3 acties uit het rapport
1. **Beslis over heractivatie** van `2026: SYBB` — 30 dagen nul delivery = nul betaalde SYBB-leads (🟡 jouw budgetbeslissing).
2. **Herstel de PostHog MCP-koppeling** — zonder PostHog is de helft van dit rapport blind (🟡 technische check).
3. **Ruim het campagne-duplicaat op** om rapportage-/deploy-verwarring te voorkomen (🟢 snel).

Wil je dat ik de PostHog-koppeling nu help debuggen, of eerst de campagnestatus met je doorneem?

---

Klaar. Het rapport staat opgeslagen in `Output/Reports/Daily/2026-06-27_auto_optimize.md` en is gecommit + gepusht.

## Uitkomst: geen optimalisatie mogelijk, campagne staat dark

Ik heb alleen de Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs en geen schrijfacties naar de Tracker Sheet.

**Wat ik vond:**
- **act_567892422940728** (primair): 0 actieve campagnes. Alle 5 campagnes staan PAUSED, inclusief "2026: SYBB" (dagbudget €100,00, paused sinds 19 apr) en "2026: SYBB - Kopie".
- **act_1489853856181844**: 0 actieve campagnes.
- **act_607231713057715**: de huidige API token heeft geen toegang tot dit account (alleen de twee bovenstaande zijn toegestaan), dus dat kon ik niet checken.

**Acties:**
- ⚡ Niveau 1: **0 ads gepauzeerd.** Geen actieve ads, dus de kill-regels (Link CTR < 0,8%, CPC link > €1,50) zijn niet van toepassing.
- ⚠️ Geen waarschuwingen, geen 70-20-10 classificatie, geen budget-mismatch. Er draait niets.
- 💡 Het enige zinvolle actiepunt is strategisch: beslis of de SYBB campagne weer aan moet, of pauzeer het dagelijkse rapport-ritme tot de campagne live gaat. Een auto-optimize loop op een dark campagne is leeg werk.

Wil je dat ik de SYBB campagne weer activeer, of laat je hem voorlopig dark?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
