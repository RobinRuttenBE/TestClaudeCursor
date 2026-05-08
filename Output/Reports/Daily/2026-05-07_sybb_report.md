# SYBB Daily Report, 2026-05-07

## 1. Samenvatting
Campagne "2026: SYBB" stond gisteren (en het hele 7-daagse vergelijkingsvenster) op PAUSED, dus geen Meta Ads spend, impressies of clicks. De landing page kreeg 1 pageview in 1 sessie van 11 seconden, een bounce. Traffic is vrijwel volledig afhankelijk van organische Instagram en Facebook bio links, niet van betaalde acquisitie.

## 2. Meta Ads Performance

**Status: campagne PAUSED.** Campaign ID `120239435987290239`, account `act_567892422940728` (Sempertex Ad Account). Geen actieve ad sets of ads. Pipeboard `get_insights` retourneert lege dataset voor zowel 2026-05-07 als 2026-04-30 t/m 2026-05-06.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0 | €0 | flat |
| Impressions | 0 | 0 | flat |
| Clicks | 0 | 0 | flat |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

### Ad Variant Performance
Geen Meta Ads variant data beschikbaar (campaign paused). PostHog detecteerde wel 2 pageviews op 2026-05-05 met `utm_source=meta` en `utm_content=h13_b3_cta5`, vermoedelijk afkomstig van eerder geklikte ad-links of cached referrals. Verder geen paid clicks in het venster.

**Beste variant:** n/a
**Slechtste variant:** n/a

## 3. Landing Page Health

Bron: PostHog HogQL queries op `properties.$host = 'www.startyourballoonbusiness.com'`. Note: in de SKILL stond het host zonder www, maar in PostHog is alle traffic getagd met `www.startyourballoonbusiness.com`. Aangepast in deze run.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 1 | 3,4/dag | n/a | rood |
| Sessions | 1 | 2,7/dag | n/a | rood |
| Bounce Rate | 100% | 84,2% | <55% | rood |
| Avg Session Duration | 11s | 113s | >90s | rood |
| Scroll 25% | n/a | n/a | >80% | niet getrackt |
| Scroll 50% | n/a | n/a | >60% | niet getrackt |
| Scroll 75% | n/a | n/a | >40% | niet getrackt |
| Scroll 100% | n/a | n/a | >20% | niet getrackt |
| CTA Click Rate | n/a | n/a | >4% | niet getrackt |

**Belangrijk:** in de PostHog events tabel bestaan alleen `$pageview`, `$pageleave`, `$autocapture` en `$web_vitals` voor dit domein. Er zijn geen scroll-depth events of expliciet getagde CTA click events. De PostHog instrumentatie op startyourballoonbusiness.com mist de scroll-tracking en CTA-tracking die de SKILL veronderstelt. Dit is zelf een rode vlag, zie sectie 5.

## 4. Funnel Drop-off

Pageview home (1) → Scroll 50% (n/a) → CTA Click (n/a) → /checkout (0)

Yesterday geen /checkout en geen /booking pageviews. In het 7d venster zijn er wel 3 /checkout pageviews en 1 /review, maar zonder funnel events kan ik geen gekoppelde conversion rate berekenen.

**Grootste lek:** met 1 sessie van 11 seconden en geen scroll-instrumentatie is het lek niet meetbaar. Op basis van de data lijkt het lek tussen "land op homepage" en "blijven lezen", maar dit is een vermoeden, niet bewijs.

## 5. Rode Vlaggen

1. **Campagne paused, geen acquisitie pipeline.** Het hele 7d window kreeg de campagne nul spend. Organische Instagram bio link draagt 11 van de 24 pageviews (45%), Facebook bio link 5 (21%). Zonder ads geen testdata, geen optimalisatie loop.
2. **PostHog scroll en CTA tracking niet ingericht.** De daily-sybb-report SKILL veronderstelt scroll-depth events (25/50/75/100) en CTA click events. Geen van beide bestaat in de events tabel voor dit domein. Hierdoor kan de report 6 van de 7 LP health KPIs niet vullen.
3. **Bounce rate 100% gisteren, 84,2% in 7d window.** Ruim boven de target van <55%. 16 van 19 sessies in het 7d window zijn single-pageview.
4. **Avg session duration gisteren 11 seconden.** 88% onder 7d gemiddelde van 113s. Steekproef van 1, dus statistisch zwak, maar wel onder de target van 90s.
5. **Host mismatch in SKILL configuratie.** SKILL noemt `startyourballoonbusiness.com`, PostHog tagt alles als `www.startyourballoonbusiness.com`. Een eerdere run zonder de www prefix zou nul resultaten geven en het beeld vertekenen.

## 6. Top 3 Acties voor Vandaag

1. **Beslissen of "2026: SYBB" weer aan moet, en zo ja met welk budget en welke creatives.** Waarom: zonder paid traffic geen funnel test, geen learnings, geen pipeline. Hoe: open Meta Ads Manager, check waarom gepauzeerd is (budget, performance, freeze), zet één ad set in 5 hooks (h11 t/m h15) opnieuw aan met €10/dag of besluit dat SYBB on hold blijft. Verwachte impact: traffic terug van 1 naar 50+ sessies/dag bij €10/dag CPC <€0,50. Escalatie level: oranje (Robin beslissing).
2. **PostHog scroll-depth en CTA click events instrumenteren op startyourballoonbusiness.com.** Waarom: 6 van 7 KPIs in dit rapport zijn nu n/a. Zonder instrumentatie kunnen we niet detecteren waar bezoekers afhaken, dus elke landingspagina-iteratie is gokwerk. Hoe: in Wix Editor een PostHog snippet toevoegen die `$scroll` events stuurt op 25/50/75/100% en een `cta_click` event op de "Book Now" en "Apply" knoppen. Verwachte impact: vanaf morgen wel een meetbare scroll- en CTA-funnel. Escalatie level: oranje (Wix Editor).
3. **SKILL configuratie en host fixen.** Waarom: deze run en alle vorige runs van de daily-sybb-report op `startyourballoonbusiness.com` zonder www gaven nul resultaten waar wel data is. Hoe: in `skills/daily-sybb-report/SKILL.md` documenteren dat queries `properties.$host = 'www.startyourballoonbusiness.com'` moeten gebruiken (of beide hosts via OR). Verwachte impact: toekomstige reports laden correct, ook als CDN of redirect ooit verandert. Escalatie level: groen (auto, edit in skill file).

---

**Cross-reference notitie:** met campagne paused vervalt de cross-reference logica tussen Meta Ads CTR en LP bounce. De enige interessante observatie: 2 paid clicks (h13_b3_cta5) op 2026-05-05 leidden tot 1 sessie. Te klein voor conclusies, maar h13 was tijdens de actieve periode in januari/april al de enige variant die nog incidenteel verkeer triggert via cached links. Bij heractivatie zou ik h13 als baseline gebruiken en daarnaast een tweede hook (bv. h12 of h15) testen.

**Data sources:** Meta Ads MCP (Pipeboard), PostHog MCP. Geen Google MCPs gebruikt zoals afgesproken voor deze run.
