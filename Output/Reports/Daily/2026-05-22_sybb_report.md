# SYBB Daily Report — 22 May 2026

## 1. Samenvatting
Tweede dag op rij met radiostilte. Meta-campagne **`2026: SYBB`** staat sinds 19 April op **PAUSED**, dus 0 spend / 0 clicks. Het landingspagina-verkeer bestaat uit **2 organische bio-link bezoekers** (1× Instagram Mobile US, 1× Facebook Mobile België), beide gebounced op de homepage. De funnel produceert geen exploiteerbaar signaal zolang er geen paid traffic loopt én scroll-/CTA-instrumentatie ontbreekt.

## 2. Meta Ads Performance

Campagne **`2026: SYBB`** (ID `120239435987290239`, account `act_567892422940728` — Sempertex Ad Account, EUR) staat sinds **2026-04-19** op `PAUSED`. `daily_budget` = €100, `budget_remaining` = €100 (volledig ongebruikt). Insights endpoint geeft een lege dataset voor 22 mei én voor het 7d-window 15–21 mei (campagne, adset en ad niveau).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads. De spend pijplijn (`h11_b3_cta5` t/m `h15_b3_cta5`) staat volledig uit. Er was in de afgelopen 8 dagen ook **0 paid-attributed pageviews** op `www.startyourballoonbusiness.com` (alle UTM-getagde sessies zijn `utm_medium=organic` vanuit Instagram of Facebook bio-links).

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

Host: `www.startyourballoonbusiness.com`. PostHog project "Default project" (id 149694).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 2 | 4,6 / dag | n.v.t. | ⚪ |
| Unique Visitors | 2 | 3,7 / dag | n.v.t. | ⚪ |
| Sessions | 2 | 3,9 / dag | n.v.t. | ⚪ |
| Bounce Rate | 100% (2/2) | 85% (23/27) | <55% | 🔴 |
| Avg Session Duration | 0s | 64s | >90s | 🔴 |
| Scroll 25% / 50% / 75% / 100% | niet gemeten | niet gemeten | >80 / >60 / >40 / >20% | ⚪ |
| CTA Click Rate (autocapture clicks ÷ pageviews) | 0% (0 clicks / 2 pv) | n.b. | >4% | 🔴 |

### Wat we wél kunnen lezen uit de 2 sessies van gisteren
- Sessie 1: `instagram / organic / sybb / bio_link`, referrer `t-sml.mtrbio.com`, Mobile, **United States**, landing `/`, 1 pv, 0s, 0 clicks → bounce.
- Sessie 2: `facebook / organic / sybb / bio_link`, referrer `t-sml.mtrbio.com`, Mobile, **België**, landing `/`, 1 pv, 0s, 0 clicks → bounce.
- 0 rageclicks, 0 dead clicks.

Geen van beide bezoekers bewoog buiten de hero. Zonder scroll-events kunnen we niet zien of de hero gelezen werd of dat ze direct wegklikten.

## 4. Funnel Drop-off

Gisteren (2 sessies):
```
Pageview /         — 2   (100%)
  → Scroll 50%     — niet gemeten
  → CTA Click      — 0 ($autocapture clicks)
  → /booking       — 0
  → /checkout      — 0
```

7d-window (2026-05-15 t/m 2026-05-21, 27 sessies):
```
Pageview /        — 23 sessies (~85%)
  → /product-page                              — 1
  → /booking                                   — 1
  → /checkout                                  — 1
```

**Grootste lek:** stap `/` → `/booking`. 29 pageviews op de homepage in 8 dagen leveren 1 boeking-pageview op (~3,4% door-klik). De /checkout-pageview kwam zelfs van een sessie zonder /booking-pageview ervoor, wat suggereert dat de funnel via Wix mogelijk een booking-bevestiging direct routeert naar /checkout zonder /booking-page-event. Validatie nodig.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat 33 dagen op PAUSED.** `budget_remaining = daily_budget = €100`. Vorig rapport (21 mei) markeerde dit al als #1 blocker — geen verandering.
- 🚩 **100% bounce rate gisteren (N=2).** Klein steekproefje, maar in lijn met de 85% bounce over het 7d-window. Bio-link verkeer landt en vertrekt zonder zichtbare interactie.
- 🚩 **0% CTA click rate gisteren.** Beide bezoekers genereerden geen enkele `$autocapture` click. Of de hero faalt, of de scroll start niet, of de page laadde traag — onderscheidbaar maken vereist scroll-instrumentatie.
- 🚩 **Scroll & cta_click tracking ontbreken nog steeds.** Zelfde action item als gisteren, niet aangepakt.
- ⚠️ **Mismatch tussen booking en checkout sessies in 7d.** 1× `/booking` (organic IG bio) en 1× `/checkout` zitten in verschillende sessies — vermoedelijk Wix routing of een direct checkout-link. Funnel-attributie onbetrouwbaar tot Wix flow geverifieerd is.

## 6. Top 3 Acties voor Vandaag

1. **Beslis vandaag: SYBB-campagne reactiveren of officieel parkeren tot Q3.**
   - **Wat:** Open Meta Ads Manager → campagne `120239435987290239` (`2026: SYBB`). Kies tussen (a) heractiveer winning ad `120242894133350239` standalone op €30–50/dag conform gisteren's ads-rapport aanbeveling, of (b) zet de campagne formeel op "tot Q3" en parkeer dit rapport.
   - **Waarom:** 33 dagen radiostilte. De `/morning-report` en `/sybb-report` lopen 5 weken zonder data om op te draaien; budget van €100/dag staat te wachten.
   - **Hoe:** Ads Manager → set Ad `120242894133350239` op ACTIVE → set adset budget naar €30 → laat overige paused → monitor 48u CTR + UTM-flow naar PostHog.
   - **Verwachte impact:** binnen 48u eerste variant-data; baseline om de andere 4 ads tegen te benchmarken in 70-20-10 setup.
   - **Escalatie:** 🟡 Robin-beslissing (strategisch + budget).

2. **Instrumenteer scroll-depth + `cta_click` event in PostHog op `www.startyourballoonbusiness.com`.**
   - **Wat:** `posthog.capture('scroll_depth', { percent: 25/50/75/100 })` via een scroll-listener én een expliciete `cta_click` event op alle "Book Now" / "Get Started" / "Reserve Your Seat" buttons (data-attribute zodat het Wix-design-onafhankelijk blijft).
   - **Waarom:** Vandaag al twee dagen op rij vullen sectie 3 (rows scroll 25/50/75/100% en CTA click rate) zonder data. Het skill-rapport-template eist deze events; zonder instrumentatie kunnen we ad-CTR vs LP-scroll cross-references niet draaien zodra ads weer live gaan.
   - **Hoe:** Wix Editor → Custom Code → embed snippet (zie `Kennis/tools/posthog-integratie.md` als die er nog niet is — anders maken). Test in PostHog Live Events tab vóór deploy.
   - **Verwachte impact:** vanaf morgen volledige tabel sectie 3, en bij paid heractivatie meteen variant-vergelijking mogelijk.
   - **Escalatie:** 🟠 Wix Editor + dev-tijd (~1u).

3. **Audit de homepage hero met de ogen van een mobiele bio-link bezoeker (US + EU).**
   - **Wat:** Open `https://t-sml.mtrbio.com/` op mobiel → klik door naar `www.startyourballoonbusiness.com/`. Noteer eerste 3 frictiepunten boven de fold: laadtijd, headline match met bio-link copy, CTA zichtbaarheid, valuta/taal (US ziet €? UK spelling?).
   - **Waarom:** Beide bezoekers gisteren waren Mobile bio-link en bounced binnen 0s. Bio-link verkeer is warm, gratis en je enige bron zolang ads uit staan — elke %-punt conversie is pure marge.
   - **Hoe:** Visuele audit (10 min) + Lighthouse mobile score. Eventueel A/B-test hero-headline via Wix als de bio-link copy en pagina-H1 niet matchen.
   - **Verwachte impact:** verdubbeling bio-link → /booking conversie = ~2 boekingen/week extra, nul mediakosten.
   - **Escalatie:** 🟢 zelfstandig.

---

## Bijlage: Data Sources

- **Meta Ads:** Pipeboard MCP — account `act_567892422940728` (Sempertex Ad Account, EUR). Campagne `120239435987290239` ("2026: SYBB"), status `PAUSED` sinds 2026-04-19. Daily budget €100. Insights leeg voor 2026-05-22 (campaign/adset/ad niveau) en 2026-05-15…2026-05-21.
- **PostHog:** project "Default project" (id 149694) in org "Sempertex Europe". Host `www.startyourballoonbusiness.com`. Person-on-events mode actief. Project tz: UTC. Geen `$scroll` / `cta_click` events ingericht — alleen `$pageview`, `$pageleave`, `$autocapture`, `$rageclick`, `$dead_click`, `$web_vitals`.
- **Periode:** 2026-05-22 (gisteren), vergelijking 2026-05-15 t/m 2026-05-21 (7d).
- **Niet geraadpleegd (conform run-instructies):** Gmail, Google Calendar, Google Drive, Google Sheets, Google Docs, Google Slides. Niet geschreven naar Meta Ads Tracker Google Sheet.
