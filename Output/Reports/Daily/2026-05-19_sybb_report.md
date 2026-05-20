# SYBB Daily Report — 19 May 2026

## 1. Samenvatting
Campagne "2026: SYBB" staat al ruim een maand op PAUSED (sinds 19 april), dus er was gisteren geen betaalde traffic en geen Meta Ads spend. De landing page kreeg 6 sessies (allemaal van 6 unieke bezoekers), waarvan 1 via Instagram bio_link en 5 zonder UTM (direct/referral). Alle sessies bleven op de homepage staan, geen enkele bezoeker klikte door naar /booking — feitelijk 100% bounce en 0 conversies.

## 2. Meta Ads Performance

Campagne "2026: SYBB" (ID 120239435987290239) status: **PAUSED** sinds 19 april 2026. Daily budget configuratie staat nog op €100, maar er is geen actieve delivery.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen data — campagne staat gepauzeerd. Wel zichtbaar in PostHog: over de laatste 8 dagen kwam er 1 sessie binnen met `utm_content=h11_b3_cta5` (`utm_medium=cpc`, `utm_source=meta`), waarschijnlijk een vertraagde click of cache hit van vóór de pauze. Geen overige Meta CPC traffic.

**Beste variant:** n.v.t.
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

Bron: PostHog project "Default project", host `startyourballoonbusiness.com`.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 6 | 5,4 | meten | 🟡 |
| Unique visitors | 6 | 3,7 | meten | 🟢 |
| Sessions | 6 | 4,3 | meten | 🟢 |
| Bounce Rate (single-pv) | 100% | ~93% | <55% | 🔴 |
| Avg Session Duration | ~389s (mediaan 166s) | n.v.t. (geen $session_duration) | >90s | 🟢 |
| Scroll 25% | n.v.t. | n.v.t. | >80% | ⚪ |
| Scroll 50% | n.v.t. | n.v.t. | >60% | ⚪ |
| Scroll 75% | n.v.t. | n.v.t. | >40% | ⚪ |
| Scroll 100% | n.v.t. | n.v.t. | >20% | ⚪ |
| CTA Click Rate | 0% | 0% | >4% | 🔴 |
| /booking visits | 0 | 0 | meten | 🔴 |

**Toelichting:**
- Bounce rate hier is gedefinieerd als sessies met exact 1 pageview / totaal sessies. Alle 6 sessies van gisteren hadden 1 pageview.
- Scroll depth komt niet door als event property (`$prev_pageview_max_scroll_percentage` was steeds None). De scroll heatmap config in PostHog moet gecheckt worden — anders blijft deze KPI doodloop.
- 7 autocapture clicks op pad "/" gedetecteerd, maar geen ervan leidde tot een pageview op /booking. Geen rageclicks of dead clicks.

### Sessie detail (6 sessies)
| Sessie start (UTC) | Bron | Duur | Pages |
|--------------------|------|------|-------|
| 05:31 | instagram organic / bio_link | 152s | 1 |
| 14:06 | direct | 8s | 1 |
| 14:06 | direct | 10s | 1 |
| 15:44 | direct | 578s | 1 |
| 17:55 | direct | 1409s* | 1 |
| 17:55 | direct | 179s | 1 |

*1409s lijkt een open tab op de achtergrond, niet actieve sessie.

## 4. Funnel Drop-off

```
Pageview homepage  (6 sessies, 100%)
        ↓  -100%
Scroll 50%         (n.v.t. — niet getrackt)
        ↓
CTA Click          (0 — homepage CTA werd niet aantoonbaar geklikt richting /booking)
        ↓
/booking visit     (0, 0%)
```

**Grootste lek:** 100% drop-off tussen homepage en /booking. Geen enkele bezoeker bereikte de boekingspagina. Combineer met het feit dat de paid campagne uit staat: dit is volledig "warme" organische traffic die niet getriggerd wordt door de homepage.

## 5. Rode Vlaggen 🚩

1. **Campagne staat gepauzeerd sinds 19 april** — al 30 dagen geen paid acquisition voor SYBB. Funnel staat stil.
2. **0% conversie van homepage naar /booking** — 6 sessies, 0 die naar /booking gaan. Homepage CTA werkt niet als conversie-driver, ook niet voor organische bezoekers.
3. **Scroll depth tracking lijkt niet actief** — `$prev_pageview_max_scroll_percentage` blijft None. Daardoor kunnen we engagement diepte niet meten en de SKILL-targets voor scroll 25/50/75/100 niet vullen.
4. **100% single-pageview bounce** — elke bezoeker zag alleen "/" en niets anders. Voor 1 sessie van 23 minuten is dat opvallend: lang op één pagina maar geen vervolgactie.
5. **Geen $session_duration event property** — PostHog session-properties uitbreiding nog niet ingericht; we rekenen nu met start/eind van events per session_id als proxy.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: SYBB campagne aanzetten of bewust opnieuw plannen.**
   - **Wat:** Campagne `2026: SYBB` is 30 dagen uit. Of activeer hem (met dezelfde of nieuwe creatives), of vervang door `2026: SYBB - Kopie` (PAUSED, aangemaakt 19 april — bedoeld als nieuwe iteratie?).
   - **Waarom:** Funnel staat stil. Organisch krijg je 4-5 sessies per dag op de LP, paid duwde dat voorheen veel hoger. Geen paid = geen schaal.
   - **Hoe:** Meta Ads Manager → kies één van beide campagnes → check budgets, creatives en doelgroep → activeer. Of plan een launch datum.
   - **Verwachte impact:** terug naar betaalde traffic, zonder dat is dit rapport een leeg formulier.
   - **Escalatie:** Geel (Robin goedkeuring nodig).

2. **Fix het conversie-pad homepage → /booking.**
   - **Wat:** Alle 6 sessies bleven op "/" hangen. CTA-positie of -copy op de homepage werkt niet (ook niet voor warme Instagram bio_link traffic die intent had).
   - **Waarom:** 0 /booking pageviews over 6 sessies én 7 autocapture clicks elders op de pagina. Mensen klikken, maar niet op de CTA naar booking.
   - **Hoe:** Wix Editor → above-the-fold CTA testen (kleur primary geel/oranje, copy meer urgent, "Reserve your spot" → directe doorklik naar /booking). Zet PostHog session recording aan voor 1-2 dagen om te zien waar mensen wél klikken.
   - **Verwachte impact:** zelfs zonder paid traffic moeten 1-2 van de 6 dagelijkse organische bezoekers /booking bereiken.
   - **Escalatie:** Oranje (Wix Editor wijziging).

3. **Activeer scroll depth tracking in PostHog.**
   - **Wat:** Scroll % wordt niet capturet — eigenschap `$prev_pageview_max_scroll_percentage` is leeg op alle pageviews.
   - **Waarom:** Zonder scroll data kunnen we niet diagnosticeren of de hero faalt, of dat mensen wel scrollen maar de CTA missen. Half van het rapport blijft "n.v.t."
   - **Hoe:** Check PostHog autocapture instellingen → zorg dat scroll capture enabled is. Of voeg manueel een scroll listener toe via Wix custom code die `posthog.capture('scroll_depth', {depth: 25/50/75/100})` stuurt op breakpoints.
   - **Verwachte impact:** vanaf morgen scroll distribution in het rapport, dus we kunnen ad-pagina mismatches zien zodra paid weer aan staat.
   - **Escalatie:** Geel (technisch werk, geen merknaam wijziging).

---

**Data sources:** Pipeboard Meta Ads MCP (campagne `2026: SYBB`, account `act_567892422940728`) + PostHog MCP (project "Default project", host `startyourballoonbusiness.com`). Tijdrange: 19 mei 2026 00:00–23:59 UTC, baseline 12–18 mei 2026.
