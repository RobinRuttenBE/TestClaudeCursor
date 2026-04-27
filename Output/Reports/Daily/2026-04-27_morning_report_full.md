# Morning Report — 2026-04-27

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,13%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 88,29** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1059,47 · impressions 91.839 · link_clicks 1.036
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H13 · ROAS 2.05x · 1 order(s) · EUR 423,50 revenue.


Ik kan het rapport niet draaien zonder live data. De Pipeboard Meta Ads MCP vereist eerst OAuth, en de PostHog MCP-tools zijn niet beschikbaar in deze sessie.

**Wat is nodig om door te gaan:**

1. Open deze URL in je browser om de Meta Ads MCP te autoriseren:

   https://pipeboard.co/oauth/authorize?response_type=code&client_id=0ec17ee6fb82e56ac95edf588a15adcf&code_challenge=WPGZ2zDfnOT7EDoOkGdJ7c2vjLL5DBd4O_8nyLTxfTo&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A50726%2Fcallback&state=jtSABpZZkg82p71ichKC-I1tBdBFuGw1G55OObj2hoc&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

2. Als de redirect-pagina niet laadt, plak de volledige `localhost:50726/callback?code=...&state=...` URL hier zodat ik `complete_authentication` kan callen.

3. Voor PostHog cross-referencing: de PostHog MCP staat niet in de deferred tools-lijst van deze sessie. Wil je dat ik het rapport draai op alleen Meta Ads data (zonder PostHog), of moet de PostHog MCP eerst opnieuw geconnect worden?

**Context (gisteren 2026-04-26):** Geen ACTIVE campagnes — alle 5 campagnes op `act_567892422940728` stonden PAUSED, met `2026: SYBB` als grootste spender (€1.059 over 30d, CPC €0,55, ? purchases (verifieer Wix)). Ik kan dat snapshot niet hergebruiken voor vandaag, dus zonder live auth kan ik geen vers rapport schrijven.

Wat wil je dat ik doe — wachten op OAuth, of het laatste snapshot van 26-04 als referentie kopiëren naar de vandaag-bestandsnaam?

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-26_sybb_report.md`.

**Hoofdbevinding:** campagne "2026: SYBB" stond gisteren op PAUSED. Geen Meta Ads delivery (€0 spend, 0 clicks). PostHog landing page zag alleen 5 pageviews uit 4 organische sessies, geen UTM tagged traffic. Sinds ~21-04 ligt de paid funnel volledig stil. De 7d voorgaande periode (19-25 april) liet €43,81 spend zien met CPC €0,72 (44% boven het <€0,50 target).

**Top actie:** beslissen of de campagne weer geactiveerd wordt, en zo ja eerst de hoge CPC en UTM tagging onderzoeken.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-04-27_auto_optimize.md`.

**Kernbevinding:** Er zijn 0 actieve campagnes en €0,00 spend over de afgelopen 3 dagen op beide toegankelijke accounts (`act_567892422940728` en `act_1489853856181844`). Het derde account `act_607231713057715` is niet meer beschikbaar via de huidige API token. Alle 5 campagnes in het Sempertex account staan op PAUSED, inclusief `2026: SYBB` (laatst geüpdatet 2026-04-19).

**Niveau 1 (automatisch):** geen acties uitgevoerd. Geen ads om te pauzeren.

**Niveau 2 voorstellen (wachten op jouw goedkeuring):**
1. Relaunch-beslissing voor `2026: SYBB` (3 opties A/B/C)
2. Archiveer de drie oude Nozzle Up campagnes om ruis te verminderen
3. Kalibreer 70-20-10 drempels op link-metrics (open TODO in het command)
4. Pre-launch checklist (creatives, UTM, landing page health)

Geef aan welke voorstellen je wilt uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.05x | EUR 207,00 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires
> 
> Wix orders laatst bijgewerkt: 2026-04-18 (8 dagen geleden). Mogelijk niet actueel.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
> - Sessie op 2026-04-18, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

**Ranking op Verified ROAS:**

| Rank | Ad | Verified ROAS | Wix Orders | Revenue | Spend | Advies |
|---|---|---|---|---|---|---|
| 🥇 | H13,B3,CTA5 | 2.05x | 1 | EUR 423,50 | EUR 207,00 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| 🥈 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | 20% budget — tweede verified winner · houd actief |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H13** (verified ROAS 2.05x, 1 Wix order(s), EUR 423,50 revenue).
- H13 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
