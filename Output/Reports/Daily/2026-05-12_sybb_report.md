# SYBB Daily Report: 12 May 2026

## 1. Samenvatting

Twee dingen tegelijk op 12 mei. Eén, de Pipeboard Meta Ads MCP geeft voor de tweede dag op rij "Facebook connection required" en levert geen ad-data; de campagne `2026: SYBB` is presumed nog steeds PAUSED (23e dag sinds 19 april). Twee, PostHog ziet een vreemde piek: 14 pageviews, 10 sessies, 8 unieke bezoekers — bijna 4x het 7-daags gemiddelde, waarvan 13 op de `/review` route (gisteren 2, eergisteren 0). Twaalf van die 13 `/review` sessies zijn Belgische mobiele bezoekers, dertien zijn `$direct`, en vier sessies vallen binnen 8 seconden van elkaar (14:13 UTC). Eén Belgische desktop sessie van 311s op `/review` is de enige met serieuze engagement; de rest bouncet binnen 7s. Dit lijkt op een gedeelde link in een Belgische chat of een interne testronde, niet op een organische trafficstroom.

## 2. Meta Ads Performance

| Metric | Gisteren (12 mei) | 7d Gemiddelde (5-11 mei) | Trend |
|--------|-------------------|---------------------------|-------|
| Spend | n/a (MCP error) | €0,00 (paused) | n/a |
| Impressions | n/a (MCP error) | 0 | n/a |
| Clicks | n/a (MCP error) | 0 | n/a |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

**MCP status:** Pipeboard Meta Ads MCP gaf vandaag (zoals gisteren) op alle calls `Facebook connection required. Connect your account at https://pipeboard.co/connections`. Gepoogd: `get_ad_accounts`, `get_campaigns(act_567892422940728)`, `get_campaign_details(120239435987290239)`, `get_insights(120239435987290239, 2026-05-12)`. Allemaal dezelfde auth-fout. Tweede dag storing. Pipeboard reconnect blijft een blokker voor alle Meta Ads gedreven rapportages.

**Context uit PostHog (cross-check):** nul `utm_medium=cpc` pageviews op 12 mei. Op 5 mei kwamen er nog 2 stale `meta/cpc/sybb` clicks binnen (`utm_content=h13_b3_cta5`, beide naar `/`), maar die zijn waarschijnlijk uitgesteld door cached link clicks of een fbclid retry. Sindsdien geen enkele cpc-getagde pageview. Dit bevestigt dat de campagne in elk geval geen levering meer heeft.

### Ad Variant Performance

Niet meetbaar. Campagne presumed 23 dagen PAUSED. Meta Ads MCP voor de 2e dag dood. PostHog ziet nul cpc-sessies op 12 mei.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (12 mei) | 7d Gemiddelde (5-11 mei) | Target | Status |
|--------|-------------------|---------------------------|--------|--------|
| Pageviews | 14 | 3,1/dag (22 totaal) | n/a | informatief |
| Unique visitors | 8 | 2,9/dag | n/a | informatief |
| Sessions | 10 | 2,9/dag (20 totaal) | n/a | informatief |
| Bounce Rate | 70,0% (7/10) | 88,7% (15/20)* | <55% | 🔴 |
| Avg Session Duration | 32,1s | ~17s (gewogen) | >90s | 🔴 |
| Scroll 25%+ | n/m | n/m | >80% | n/m (geen scroll-events) |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| Scroll 75%+ | n/m | n/m | >40% | n/m |
| Scroll 100% | n/m | n/m | >20% | n/m |
| CTA Click Rate | n/m | n/m | >4% | n/m (geen CTA events) |

*Gewogen 7d gemiddelde: 4 sessies op 5 mei en 2 op 6 mei waren niet-bounces (bounce 66,7% / 0%); 7-11 mei zat steeds op 100% bounce.

**Belangrijk:** PostHog tracking blijft beperkt tot `$pageview` en `$web_vitals`. Scroll milestones en CTA-clicks worden nog steeds niet gevuurd. Engagement-KPI's uit de skill-target tabel zijn niet meetbaar tot scroll- en CTA-tracking opnieuw worden gewired. Onveranderde meet-gap voor de 4e dag op rij. Volume is plotseling 4x hoger maar zonder scroll-events kunnen we niet zien of de Belgische mobiele bezoekers iets *deden* op `/review`.

### Pageviews per dag (5-12 mei)

| Datum | Pageviews | Sessions | Unieke bezoekers | Bounces | Bounce % | Avg duur |
|-------|-----------|----------|------------------|---------|----------|----------|
| 5 mei | 8 | 6 | 6 | 4 | 66,7% | 113,2s |
| 6 mei | 4 | 2 | 2 | 0 | 0,0% | 75,0s |
| 7 mei | 1 | 1 | 1 | 1 | 100,0% | 0s |
| 8 mei | 2 | 2 | 2 | 2 | 100,0% | 0s |
| 9 mei | 2 | 2 | 2 | 2 | 100,0% | 0s |
| 10 mei | 3 | 3 | 3 | 3 | 100,0% | 0s |
| 11 mei | 4 | 4 | 4 | 4 | 100,0% | 0s |
| **12 mei** | **14** | **10** | **8** | **7** | **70,0%** | **32,1s** |

12 mei breekt de 5-dagen-100%-bounce streak. Een enkele 311s sessie trekt de gemiddelde duur omhoog; mediaan zit alsnog op 0s.

### Trafficbron breakdown (12 mei)

| Bron | Pageviews | Sessions |
|------|-----------|----------|
| direct / no UTM | 13 | 9 |
| instagram / organic / sybb / bio_link | 1 | 1 |
| **Totaal** | **14** | **10** |

Eén organische Instagram sessie via Manychat bio link (`t-sml.mtrbio.com`) landde op `/`. Alle andere 13 pageviews kwamen via `$direct` (geen referrer doorgegeven). Nul betaalde traffic.

### Pagina breakdown (12 mei)

| Pad | Pageviews | Sessies |
|-----|-----------|---------|
| `/review` | 13 | 9 (alle direct) |
| `/` (landing page) | 1 | 1 (Instagram bio link) |
| `/booking` | 0 | 0 |
| `/checkout` | 0 | 0 |

### `/review` route trend (5-12 mei)

| Datum | `/review` pageviews | `/` pageviews | `/checkout` pageviews |
|-------|----------------------|----------------|-------------------------|
| 5 mei | 1 | 6 | 1 |
| 6 mei | 0 | 3 | 1 |
| 7 mei | 0 | 1 | 0 |
| 8 mei | 0 | 2 | 0 |
| 9 mei | 0 | 2 | 0 |
| 10 mei | 0 | 3 | 0 |
| 11 mei | 2 | 2 | 0 |
| **12 mei** | **13** | **1** | **0** |

`/review` is in 8 dagen geëxplodeerd van 1 view (5 mei) → 0 (6-10 mei) → 2 (11 mei) → 13 (12 mei). Tegelijk daalde de homepage van 6 views op 5 mei naar 1 view op 12 mei. De `/review` route absorbeert nu effectief alle directe traffic.

### Sessie clustering (12 mei)

| Tijd (UTC) | Sessions | Land/device | Duur | Pageviews | Pad |
|------------|----------|-------------|------|-----------|-----|
| 13:37 | 1 | BE / Desktop | 311s | 3 | /review (3x) |
| 14:00 | 1 | BE / Mobile | 0s | 1 | /review |
| 14:13:32-40 | 4 | 3x BE Mobile + 1x NL Mobile | 0-7s | 1-2 | /review |
| 16:24 | 1 | US / Mobile | 0s | 1 | / (Instagram bio link) |
| 16:46 | 1 | BE / Mobile | 0s | 1 | /review |
| 17:33 | 1 | BE / Mobile | 0s | 1 | /review |
| 19:02 | 1 | BE / Mobile | 3s | 2 | /review (2x) |

**Signaal:** 4 sessies tussen 14:13:32 en 14:13:40 UTC (8 seconden interval), bijna allemaal BE Mobile, alle 4 direct, alle 4 op `/review`. Dit is gedragsmatig consistent met een gedeelde link in een Belgische groepschat (WhatsApp/Messenger met link preview die meerdere apparaten triggert) of een interne test/demo door meerdere collega's. Geen organisch patroon.

De 13:37 sessie (BE Desktop, 311s, 3 pageviews op `/review`) is de enige sessie met echte engagement. Mogelijk Robin of een teamlid die de pagina kwaliteitschecked. Daarna komen de mobiele sessies pas.

## 4. Funnel Drop-off

```
/review pageviews          13   (100% van /review traffic)
   └─ langere dan 7s             1   (7,7%) — alleen de 311s desktop sessie
   └─ CTA clicks               n/m  (geen tracking)
   └─ /booking views            0   (0%)
   └─ /checkout views           0   (0%)

/ (homepage) pageviews       1   (100% van homepage traffic)
   └─ /booking views            0   (0%)
   └─ /checkout views           0   (0%)
```

**Grootste lek:** twee verschillende lekken, allebei volledig.
1. Op `/review` blijven 8 van 9 sessies onder 7s. Onbekend of dit door de paginainhoud komt (te traag, niet matchend, geen duidelijke CTA) of door de aard van de bezoekers (notificatie/preview clicks zonder intentie).
2. De ene `/` sessie via Instagram bio link bouncet ook direct (0s). Geen progressie naar `/booking` of `/checkout` op 12 mei, geen progressie in de hele 8-daagse window (`/checkout` 1 view op 5 mei, 1 op 6 mei, dan nul; `/booking` nul over de hele periode).

## 5. Rode Vlaggen 🚩

- 🚩 **Pipeboard Meta Ads MCP voor de 2e dag dood.** Zelfde "Facebook connection required" error op alle endpoints. Reconnect bij https://pipeboard.co/connections is overdue. Dit blokkeert `/morning-report`, `/ads-report`, `/ads-optimize` en `/ads-auto-optimize` voor de tweede dag.
- 🚩 **Onverklaarbare `/review` piek (+550% in 24u).** 13 sessies op één pagina, 12 daarvan Belgisch mobiel, 13 van 14 pageviews direct (geen UTM, geen referrer). Het 14:13 cluster (4 sessies binnen 8s) wijst op een gedeelde link, niet op organisch zoekverkeer. Bron onbekend. Onderzoek nodig: was er een link gedeeld in een WhatsApp/Messenger groep, een Manychat broadcast, of een interne test? Tot we de bron kennen kunnen we niet beoordelen of dit goed nieuws (warme leads in Belgie) of ruis (preview-bots, teamtest) is.
- 🚩 **`/review` route blijft ongedocumenteerd.** Tweede dag op rij dat deze pagina traffic vangt zonder dat we weten wat erop staat, hoe hij in de funnel past, of welke tracking erop is gedefinieerd. 13 pageviews zonder funnel-context is 13 verloren leerkansen.
- 🚩 **Campagne 23 dagen paused.** 5e achtereenvolgende dag zonder enige ad-spend op SYBB. Pixel-warmte voor retargeting is praktisch nul; relaunch betekent een nieuwe learning fase van 2-4 dagen.
- 🚩 **Geen scroll- of CTA-tracking events binnen.** Onveranderd sinds 9 mei. Bij relaunch is dit een blokkerende meet-gap.
- 🚩 **Zero `/booking` events voor de 9e dag op rij.** Workshop-funnel volledig stil — dit ondanks 14 pageviews op 12 mei.
- 🚩 **70% bounce rate, 32,1s avg duur op 12 mei.** Volume nu hoog genoeg voor een eerste signaal: de pagina (`/review` vooral) houdt 7 van 10 sessies geen 7 seconden vast.

## 6. Top 3 Acties voor Vandaag

1. **Repareer Pipeboard Meta Ads MCP — 2e dag overdue.**
   - **Wat:** ga naar https://pipeboard.co/connections, reconnect het Meta/Facebook account met toegang tot `act_567892422940728`, en valideer met een `get_ad_accounts` call.
   - **Waarom:** zonder werkende Meta Ads MCP is er voor de 2e dag geen ad-data, geen kill-rules, geen CPC/frequency monitoring. Als de relaunch-of-stop beslissing (zie actie #3) naar relaunch neigt, gaat dat niet zonder live tracking.
   - **Verwachte impact:** herstel van alle Meta Ads gedreven rapportages binnen 1 dag.
   - **Escalatie:** 🟡 Robin handmatig reconnect.

2. **Onderzoek waar de 13 `/review` pageviews vandaan komen — voordat de spike afkoelt.**
   - **Wat:** identificeer de bron van de Belgische mobiele direct traffic op 12 mei rond 14:00-19:00 UTC. Check (a) Manychat campagne-broadcasts vandaag/gisteren, (b) gedeelde links in eigen WhatsApp/Messenger groepen, (c) eventuele Instagram/Facebook posts met `/review` link op 11-12 mei, (d) interne test/demo door teamleden.
   - **Waarom:** 13 sessies in één dag op een nauwelijks bestaande route is zeldzame traffic; als het organisch is wil je het versterken, als het ruis is wil je het filteren. Zonder bronkennis blijft het cijfer onbruikbaar. Het cluster van 4 sessies binnen 8s (14:13 UTC) wijst sterk op een gedeelde link met preview-fetches.
   - **Hoe:** Manychat dashboard → broadcasts vandaag/gisteren, filter op `/review` link. Sociale kanalen → zoek op `/review` URL in eigen posts/stories laatste 7 dagen. WhatsApp/Telegram → vraag teamleden of zij de link hebben gedeeld.
   - **Verwachte impact:** maakt 14 pageviews bruikbaar als signaal in plaats van noise; voorkomt dat een eenmalige test als trend wordt geïnterpreteerd.
   - **Escalatie:** 🟡 Robin checkt eigen kanalen + team.

3. **`/review` route documenteren en taggen — én relaunch-of-stop forceren.**
   - **Wat:** twee parallelle subacties.
     - (a) Bekijk `/review` in Wix Editor: wat staat erop, welke CTA's, welke link-to. Voeg PostHog tracking toe: `posthog.capture('scroll_milestone', {pct: 25/50/75/100})` via een scroll listener en `posthog.capture('cta_click', {cta_id: ...})` op elke knop. Documenteer de route in `CLAUDE.md` of de SYBB-funnel-definitie.
     - (b) Beslis vandaag SYBB campagne relaunch (13-14 mei, batch_4 met 2-3 nieuwe creatives) of full stop (verwijder uit dagelijks rapport). 23 dagen stilstand is dure besluiteloosheid.
   - **Waarom:** `/review` is nu de #1 trafficvanger en we hebben er nul tracking op. Als deze route blijft groeien, verliezen we onze meest informatieve dataset. Op campagnegebied: iedere stilstandsdag = ~€40-50 derving + dieper pixel-koud worden.
   - **Hoe:** Wix Editor → Pages → `/review` → custom code panel → PostHog `init` is al geladen op site, voeg scroll listener + click listener toe in `<script>` blok. Verifieer events in PostHog Activity feed binnen 1 uur. Voor relaunch: nieuwe ads UTM `utm_source=meta utm_medium=cpc utm_campaign=sybb utm_content=hXX_bX_ctaX utm_term=batch_4`, budget ≥€70/dag, 14d evaluatievenster, coördineer met actie #1.
   - **Verwachte impact:** vanaf morgen meetbare engagement-data op `/review`; bij relaunch betekenisvolle CTA/scroll data vanaf dag 1; einde aan de lege rapport-cyclus.
   - **Escalatie:** 🟠 Robin (Wix code-edit, strategie, budget, tracking-deploy).

---

**Data sources:** Meta Ads MCP (Pipeboard) — **niet beschikbaar 12 mei** (Facebook connection required, 2e dag op rij). Account `act_567892422940728`, campaign `120239435987290239` ("2026: SYBB") referenties uit voorgaand rapport (10 mei) bevroren. PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets, Drive, Gmail, Calendar, Docs of Slides aangeroepen voor dit rapport.**
