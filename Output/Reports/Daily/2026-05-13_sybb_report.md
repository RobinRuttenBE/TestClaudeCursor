# SYBB Daily Report: 13 May 2026

## 1. Samenvatting

Drie dingen tegelijk op 13 mei. Eén, de Pipeboard Meta Ads MCP geeft voor de 3e dag op rij "Facebook connection required" en blokkeert alle Meta Ads endpoints; campagne `2026: SYBB` is presumed nog steeds PAUSED (24e dag sinds 19 april). Twee, de `/review` piek van 12 mei (13 pageviews, Belgisch mobiel cluster) is op 13 mei volledig verdampt: nul pageviews op `/review`, nul `$direct` sessies, en geen sporen van het 14:13 UTC cluster. Dat bevestigt achteraf dat de 12 mei spike een eenmalige link share of test was, geen organische trend. Drie, het enige signaal op 13 mei is dezelfde, dagelijks terugkerende Instagram bio link sessie: 1 pageview, 1 sessie, 1 unieke bezoeker, US mobiel, 0 seconden duur, bounce. Volume is daarmee teruggevallen onder zelfs het ruisniveau van de afgelopen week.

## 2. Meta Ads Performance

| Metric | Gisteren (13 mei) | 7d Gemiddelde (6-12 mei) | Trend |
|--------|--------------------|---------------------------|-------|
| Spend | n/a (MCP error) | €0,00 (paused) | n/a |
| Impressions | n/a (MCP error) | 0 | n/a |
| Clicks | n/a (MCP error) | 0 | n/a |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

**MCP status:** Pipeboard Meta Ads MCP gaf vandaag (3e dag op rij) op alle calls `Facebook connection required. Connect your account at https://pipeboard.co/connections`. Gepoogd: `get_ad_accounts`, `get_campaigns`. Beide auth-fout. Een nieuwe OAuth challenge URL is gegenereerd voor reconnect (zie actie 1). Tot reconnect zijn `get_insights`, `get_ad_details`, `get_campaign_details` en alle ad-data calls onbruikbaar.

**Context uit PostHog (cross-check):** nul `utm_medium=cpc` pageviews op 13 mei. Het enige UTM-getagde verkeer is `instagram/organic/sybb/bio_link`. Bevestigt dat de campagne geen levering heeft. Verklaart ook waarom de utm_content varianten (h11-h15) nul data tonen.

### Ad Variant Performance

Niet meetbaar. Campagne presumed 24 dagen PAUSED, Meta Ads MCP voor 3e dag geblokkeerd, PostHog ziet nul cpc-sessies op 13 mei.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (13 mei) | 7d Gemiddelde (6-12 mei) | Target | Status |
|--------|--------------------|---------------------------|--------|--------|
| Pageviews | 1 | 4,3/dag (30 totaal) | n/a | informatief |
| Unique visitors | 1 | 3,1/dag | n/a | informatief |
| Sessions | 1 | 3,4/dag (24 totaal) | n/a | informatief |
| Bounce Rate | 100% (1/1) | 85,8% (gewogen) | <55% | 🔴 |
| Avg Session Duration | 0s | ~10s (gewogen) | >90s | 🔴 |
| Scroll 25%+ | n/m | n/m | >80% | n/m (geen scroll-events) |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| Scroll 75%+ | n/m | n/m | >40% | n/m |
| Scroll 100% | n/m | n/m | >20% | n/m |
| CTA Click Rate | n/m | n/m | >4% | n/m (geen CTA events) |

**Belangrijk:** PostHog tracking blijft beperkt tot `$pageview` en `$web_vitals`. Op 13 mei waren er in totaal 2 events op de site (1 pageview, 1 web_vitals). Geen autocapture, geen dead clicks, geen rage clicks. Scroll milestones en CTA-clicks worden voor de 5e dag op rij niet gevuurd. Engagement-KPI's uit de skill-target tabel zijn niet meetbaar tot scroll- en CTA-tracking opnieuw worden gewired.

### Pageviews per dag (6-13 mei)

| Datum | Pageviews | Sessions | Unieke bezoekers | Bounces | Bounce % | Avg duur |
|-------|-----------|----------|-------------------|---------|----------|----------|
| 6 mei | 4 | 2 | 2 | 0 | 0,0% | 75,0s |
| 7 mei | 1 | 1 | 1 | 1 | 100,0% | 0s |
| 8 mei | 2 | 2 | 2 | 2 | 100,0% | 0s |
| 9 mei | 2 | 2 | 2 | 2 | 100,0% | 0s |
| 10 mei | 3 | 3 | 3 | 3 | 100,0% | 0s |
| 11 mei | 4 | 4 | 4 | 4 | 100,0% | 0s |
| 12 mei | 14 | 10 | 8 | 7 | 70,0% | 32,1s |
| **13 mei** | **1** | **1** | **1** | **1** | **100,0%** | **0s** |

13 mei is een complete terugval naar het pre-12mei baseline patroon: 1 pageview, 1 sessie, 100% bounce, 0s duur. Identiek aan 7 mei. De 12 mei spike was een puntje, geen plateau.

### Trafficbron breakdown (13 mei)

| Bron | Pageviews | Sessions |
|------|-----------|----------|
| instagram / organic / sybb / bio_link | 1 | 1 |
| **Totaal** | **1** | **1** |

Eén Instagram bio link sessie via Manychat (`t-sml.mtrbio.com`) landde op `/`, US mobiel, om 16:11 UTC, 0s duur, bounce. Dit is exact hetzelfde patroon als de enige niet-`/review` sessie op 12 mei (Instagram bio link, US mobiel, 0s). Mogelijke conclusie: er is een dagelijks terugkerend, automatisch klikbron (Manychat campaign of trigger). Waarde voor SYBB: nul.

### Pagina breakdown (13 mei)

| Pad | Pageviews | Sessies |
|-----|-----------|---------|
| `/` (landing page) | 1 | 1 (Instagram bio link) |
| `/review` | 0 | 0 |
| `/booking` | 0 | 0 |
| `/checkout` | 0 | 0 |

### `/review` route trend (6-13 mei)

| Datum | `/review` pageviews | `/` pageviews | `/checkout` pageviews |
|-------|----------------------|----------------|-------------------------|
| 6 mei | 0 | 3 | 1 |
| 7 mei | 0 | 1 | 0 |
| 8 mei | 0 | 2 | 0 |
| 9 mei | 0 | 2 | 0 |
| 10 mei | 0 | 3 | 0 |
| 11 mei | 2 | 2 | 0 |
| 12 mei | 13 | 1 | 0 |
| **13 mei** | **0** | **1** | **0** |

`/review` is dood na de 12 mei spike. Drie scenario's: (a) de gedeelde link is uitgewerkt qua preview-fetches, (b) de Belgische groep waarin de link circuleerde is leeg gelopen, (c) een interne test is afgelopen. Volgende ankerpunt: als `/review` 14-15 mei nul blijft, was 12 mei vrijwel zeker een one-off share/test. Als er weer een spike komt, hebben we een patroon.

## 4. Funnel Drop-off

```
Homepage `/` pageviews        1   (100% van traffic)
   └─ langer dan 7s            0   (0%)
   └─ CTA clicks              n/m  (geen tracking)
   └─ /booking views           0   (0%)
   └─ /checkout views          0   (0%)
```

**Grootste lek:** dezelfde als alle dagen voor 12 mei. De enige sessie bouncet binnen 0 seconden. Er is geen funnel progressie naar `/booking` of `/checkout` in de volledige 8-daagse window (6-13 mei): `/booking` nul views over 8 dagen, `/checkout` 1 view op 6 mei daarna nul. De funnel produceert geen workshop-leads, ongeacht of het volume 1 of 14 is.

## 5. Rode Vlaggen 🚩

- 🚩 **Pipeboard Meta Ads MCP voor de 3e dag dood.** Zelfde "Facebook connection required" error op `get_ad_accounts` en `get_campaigns`. Reconnect bij https://pipeboard.co/connections is 3 dagen overdue. Een nieuwe OAuth URL is gegenereerd in deze run en is klaar voor gebruik. Blokkeert `/morning-report`, `/ads-report`, `/ads-optimize` en `/ads-auto-optimize` voor de derde dag.
- 🚩 **`/review` spike van 12 mei is single-day puntmeting.** Van 13 pv naar 0 pv in 24 uur, geen vervolg. De hypothese "Belgische gedeelde link of interne test" wordt sterker. Onderzoeksactie van 12 mei (Manychat / WhatsApp / interne kanalen check) is nog steeds open. Zonder bron-identificatie blijft 12 mei een ongeplaceerde puntmeting in de geschiedenis.
- 🚩 **Dagelijks terugkerende Instagram bio link sessie levert nul waarde.** Op 12 mei en 13 mei zien we exact hetzelfde patroon: 1 US mobiel sessie via `t-sml.mtrbio.com`, 0s duur, bounce. Dit lijkt op een dagelijks automatisch klikbron (mogelijk Manychat trigger, preview crawler, of een bot). Onderzoek of deze sessie überhaupt menselijk is.
- 🚩 **Campagne 24 dagen paused.** 6e achtereenvolgende dag zonder enige ad-spend op SYBB. Pixel-warmte voor retargeting is praktisch nul; relaunch betekent een nieuwe learning fase van 2-4 dagen.
- 🚩 **Geen scroll- of CTA-tracking events binnen.** Onveranderd sinds 9 mei (5e dag). Bij relaunch is dit een blokkerende meet-gap.
- 🚩 **Zero `/booking` events voor de 10e dag op rij.** Workshop-funnel volledig stil. Sinds 6 mei nul `/checkout` views; sinds nog langer nul `/booking` views.
- 🚩 **Volume baseline zonder spike: 2,3 pv/dag (7-11 + 13 mei).** Onder dit volume is statistisch geen enkele beslissing over funnel-prestatie verdedigbaar. Iedere KPI in `output/reports/daily/` is signal-loos zolang de campagne paused blijft.

## 6. Top 3 Acties voor Vandaag

1. **Repareer Pipeboard Meta Ads MCP, derde dag overdue.**
   - **Wat:** open de nieuw gegenereerde OAuth URL `https://pipeboard.co/oauth/authorize?response_type=code&client_id=f06cfc45f4461f52b0a206afdd97a82d&code_challenge=FD5Cd643CFGNjqb85SVgl1tnMElFxldBzv-ZydM1eYk&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A58213%2Fcallback&state=HoWbEDtOhhKPQCDoD90LH5gSW_BcujLzc8LqZ0NTHU8&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F`, autoriseer Meta/Facebook met toegang tot `act_567892422940728`, kopieer de callback URL uit de adresbalk (de "kan niet bereiken" foutpagina is verwacht), plak hem in `mcp__pipeboard-meta-ads__complete_authentication`, en valideer met `get_ad_accounts`.
   - **Waarom:** zonder werkende Meta Ads MCP is er voor de 3e dag geen ad-data, geen kill-rules, geen CPC/frequency monitoring, geen relaunch-validatie. De volledige `/ads-*` familie blijft offline tot dit gefixt is.
   - **Verwachte impact:** herstel van alle Meta Ads gedreven rapportages binnen 1 dag.
   - **Escalatie:** 🟡 Robin handmatig reconnect (Pipeboard kan dit niet via MCP zelf voltooien).

2. **Beslis vandaag: SYBB campagne relaunch of full stop.**
   - **Wat:** maak een binaire keuze. Optie A: relaunch 14-15 mei met batch_4 (2-3 nieuwe creatives), budget ≥€70/dag, 14d evaluatievenster, UTM `utm_source=meta utm_medium=cpc utm_campaign=sybb utm_content=hXX_bX_ctaX utm_term=batch_4`. Optie B: full stop, verwijder SYBB uit dagelijks rapport en herrouteer het `/morning-report` script naar enkel PostHog generieke metrics tot er een nieuwe campagne staat.
   - **Waarom:** 24 dagen stilstand is dure besluiteloosheid. Iedere dag rapport zonder ad-data is rapport-overhead zonder leerwinst. PostHog-only metrics op 1-4 pv/dag leveren geen actionable signal. Een relaunch herstart de leerlus; een stop ontlast het dagelijkse rapport en maakt ruimte voor andere prioriteiten.
   - **Hoe:** coördineer met actie 1 (MCP eerst werkend). Bij relaunch: nieuwe ads in Meta Ads Manager met batch_4 UTM's; bij stop: archiveer `/morning-report` SYBB sectie tot nader order.
   - **Verwachte impact:** einde aan de lege rapport-cyclus; bij relaunch betekenisvolle data vanaf dag 1-3; bij stop teruggewonnen attention voor andere campagnes.
   - **Escalatie:** 🔴 Robin strategische beslissing.

3. **Onderzoek de dagelijks terugkerende Instagram bio link sessie.**
   - **Wat:** controleer in Manychat of er een actieve flow/trigger/campagne is die dagelijks rond 16:00 UTC een klik op de `t-sml.mtrbio.com` bio link genereert. Cross-check: identieke US mobiel sessies op 12 mei (16:24 UTC) en 13 mei (16:11 UTC), beide met UTM `instagram/organic/sybb/bio_link`, beide 0s duur, beide bounce. Dit ruikt naar een bot, een Instagram preview crawler, of een Manychat self-test.
   - **Waarom:** als deze sessie geen mens is, vervuilt hij de baseline en suggereert hij valselijk dat er nog organisch verkeer is. Filteren of stoppen levert een schoner dashboard. Als hij wél een mens is, is hij een geïsoleerde, niet-converterende fan.
   - **Hoe:** Manychat dashboard, automation tab, filter op SYBB en bio_link triggers. Vergelijk timestamp-patroon met PostHog: zoek of er meer dergelijke sessies in de afgelopen 14 dagen zitten.
   - **Verwachte impact:** schoner volume-signaal in toekomstige rapporten; mogelijk een te stoppen automation; in elk geval duidelijkheid over of we 1 dagelijkse "echte" bezoeker hebben of niet.
   - **Escalatie:** 🟡 Robin checkt Manychat.

---

**Data sources:** Meta Ads MCP (Pipeboard), **niet beschikbaar 13 mei** (Facebook connection required, 3e dag op rij). Account `act_567892422940728` en campaign `120239435987290239` ("2026: SYBB") referenties uit voorgaand rapport (10 mei) bevroren. PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets, Drive, Gmail, Calendar, Docs of Slides aangeroepen voor dit rapport.**
