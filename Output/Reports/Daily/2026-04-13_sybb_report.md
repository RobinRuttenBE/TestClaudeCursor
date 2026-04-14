## 📊 SYBB Rapport — 2026-04-13 (data over 2026-04-12)

### ⚡ Samenvatting
Spend gisteren €139,80 (ruim 2× het 7d gemiddelde van €66,44), maar Link CTR zakte naar 0,92% en CPC (link) sprong naar €1,41 — beide ruim onder/boven target. 2 InitiateCheckouts (€700 waarde, ✅ sanity check op €350/ticket). Bounce rate op LP 57,8% (boven target), gem. sessieduur 54,6s (onder target). H13 is de schoonste variant; H15 verdient pauze.

### 🚩 Rode Vlaggen
- 🚩 **PIXEL DATAFOUT (7d Purchase waarde):** Meta meldt 2 purchases met totale waarde €42.773,50 = €21.386,75 per purchase. Past in geen enkele ticket-veelvoud (€350 ex / €423,50 incl). **Verifieer met Wix orders** voordat dit als omzet wordt gerapporteerd. Toon purchase-aantal als `? (verifieer Wix)` tot bevestiging. (Bron: Meta Ads MCP)
- 🚩 **CPC (link) ruim boven target:** €1,41 gisteren vs target <€0,50, ook 7d gem €0,90 zit ver boven target. (Bron: Meta Ads MCP, berekend €139,80 / 99 link clicks)
- 🚩 **Link CTR onder target:** 0,92% gisteren vs target >1%. 7d gem 1,06% zit nipt boven target. (Bron: Meta Ads MCP, berekend 99 / 10.781)
- 🚩 **Bounce rate boven target:** 57,8% gisteren vs target <55%. 7d gem 55,3% zit ook nipt boven. (Bron: PostHog MCP, n=135 sessies)
- 🚩 **Avg sessieduur onder target:** 54,6s gisteren vs target >90s. (Bron: PostHog MCP, n=135 sessies)
- 🚩 **Actieve ad zonder delivery:** ad `H14,B3,CTA5` in adset BATCH 1 (`120241274560730239`) staat op ACTIVE maar kreeg 0 impressies/spend gisteren. Onderzoek waarom deze niet uitlevert (audience overlap met BATCH 2, learning limited, of bid issue). (Bron: Meta Ads MCP)
- 🚩 **DATA MISMATCH Meta LP views ↔ PostHog meta sessies:** Meta 90 LP views, PostHog 129 meta-getagde sessies (+43%). Mogelijke oorzaken: pixel blocking (PostHog vangt meer), session cutoff verschil, of bot/preload sessies in PostHog. (Bron: Meta Ads MCP, PostHog MCP)
- 🚩 **H15 zwakke variant:** Link CTR 0,59%, CPC link €2,31, bounce 70%, gem. sessieduur 7,7s — slechtste op alle dimensies. Overweeg pauzeren. (Bron: gecombineerd)

### 📈 Meta Ads Performance (campagne "2026: SYBB")
| Metric | Gisteren | 7d Gem. | Trend | Target | Status |
|--------|----------|---------|-------|--------|--------|
| Spend | €139,80 | €66,44 (over 7 actieve dagen, totaal €465,10) | ↑↑ | — | — |
| Impressions | 10.781 | 7.009 | ↑ | — | — |
| Reach | 7.132 | 3.908 | ↑ | — | — |
| Frequency | 1,51 | 1,79 | ↓ | <3,5 | 🟢 |
| Link Clicks | 99 | 74 | ↑ | — | — |
| All Clicks | 207 | 142 | ↑ | — | — |
| Link CTR | 0,92% | 1,06% | ↓ | >1% | 🔴 |
| All Clicks CTR | 1,92% | 2,03% | → | — | — |
| CPC (link) | €1,41 | €0,90 | ↑↑ | <€0,50 | 🔴 |
| CPC (all) | €0,68 | €0,47 | ↑ | — | — |
| CPM | €12,97 | €9,48 | ↑ | — | — |
| LP Views | 90 | 56,6 | ↑ | — | — |
| Click → LP drop-off | 9,1% (99→90) | 23,7% (519→396) | — | <20% | 🟢 (dag) / 🔴 (7d) |

> Bron: Meta Ads MCP. Berekeningen: Link CTR = link_clicks/impressions; CPC (link) = spend/link_clicks; LP drop-off = (link_clicks − LP views)/link_clicks.

### 🎬 Ad Variant Performance — gisteren (2026-04-12)
| Ad (utm_content) | Spend | Link Clicks | Link CTR | CPC (link) | LP Views (Meta) | Sessions (PH) | LP Bounce (PH) | Avg Dur (PH) | ATC | IC | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 (`h11_b3_cta5`) | €78,85 | 51 | 0,86% | €1,55 | 44 | 73 | 63,0% | 32,4s | 1 | 2 | 🔴 hoogste spend, lage CTR, hoge bounce |
| H13,B3,CTA5 (`h13_b3_cta5`) | €27,85 | 24 | 1,06% | €1,16 | 24 | 30 | 53,3% | 64,8s | 2 | 0 | 🟢 beste LP-engagement |
| H12,B3,CTA5 (`h12_b3_cta5`) | €19,27 | 18 | 1,13% | €1,07 | 14 | 16 | 56,2% | 24,6s | 0 | 0 | 🟡 beste CTR, middelmatige LP |
| H15,B3,CTA5 (`h15_b3_cta5`) | €13,83 | 6 | 0,59% | €2,31 | 8 | 10 | 70,0% | 7,7s | 1 | 0 | 🔴 slechtste op alle dimensies |
| **Totaal actieve delivery** | **€139,80** | **99** | **0,92%** | **€1,41** | **90** | **129 (meta)** | — | — | **4** | **2** | — |

**Beste variant:** **H13,B3,CTA5** — laagste bounce (53,3%), hoogste avg dur op LP (64,8s), 2 ATCs, beste CPC link (€1,16) onder de delivery-ads. Beslissingsgrond: combinatie van Meta delivery én PostHog kwaliteit.

**Slechtste variant:** **H15,B3,CTA5** — Link CTR 0,59% (geen serieuze hook), CPC link €2,31, bounce 70%, sessieduur 7,7s. Pauzeren.

**Delivery check:** 4 van de 5 ACTIVE ads kregen gisteren delivery. `H14,B3,CTA5` (BATCH 1, ad ID `120241275621450239`) staat ACTIVE maar kreeg 0 impressies → onderzoeken (zie rode vlag).

#### Gepauzeerde ads (restspend)
Geen gepauzeerde ads met restspend in deze periode. Alle 22 PAUSED ads in de campagne hadden 0 spend gisteren. (Bron: Meta Ads MCP)

### 📡 Pixel Events — gisteren
| Event | Aantal | Cost per Event | Trend (vs 7d gem) |
|---|---|---|---|
| ViewContent | 10 | €13,98 | → |
| AddToCart | 4 | €34,95 | ↑ (7d: €29,07) |
| InitiateCheckout | 2 | €69,90 | ↑ (7d: €46,51) |
| Purchase | 0 | — | — (gisteren niets) |

**InitiateCheckout sanity check ✅** — €700 totaalwaarde / 2 events = €350 per event = exact 1 ticket ex BTW. Past in de reeks. Géén datafout op IC.

**Purchase sanity check (7d window):** Meta meldt 2 purchases over de afgelopen 7 dagen met waarde €42.773,50 → €21.386,75 per purchase. Dit is **niet** een veelvoud van €350 of €423,50 (15% marge). **PIXEL DATAFOUT, purchase waarde onrealistisch, verifieer met Wix orders.** Het 7d purchase aantal wordt hieronder als `? (verifieer Wix)` weergegeven.

| Event (7d window) | Aantal | Cost per Event | Waarde (Meta) |
|---|---|---|---|
| ViewContent | 31 | €15,00 | — |
| AddToCart | 16 | €29,07 | — |
| InitiateCheckout | 10 | €46,51 | €3.500 (✅ €350/event) |
| Purchase | ? (verifieer Wix) | — | €42.773,50 (🚨 datafout) |

### 🌐 Landing Page Health (PostHog, www.startyourballoonbusiness.com)
| Metric | Dag (2026-04-12) | 7d Gem. | Target | Status |
|---|---|---|---|---|
| Sessies | 135 | 113,9 (totaal 797) | — | — |
| Pageviews | 189 | 132,3 (totaal 926) | — | — |
| Unieke bezoekers | 124 | 96,4 (totaal 675) | — | — |
| Bounce Rate | Dag: 57,8% · 7d gem: 55,3% | — | <55% | 🔴 / 🔴 |
| Avg Sessieduur | Dag: 54,6s · 7d gem: 79,4s | — | >90s | 🔴 / 🔴 |
| Pageviews/sessie | 1,4 | — | — | — |
| Scroll 25% / 50% / 75% / 100% | Niet geconfigureerd | — | — | — |
| CTA Click Rate | Niet geconfigureerd | — | >4% | — |

**Session recordings:** 87 nieuwe opnames gisteren. (Bron: PostHog MCP, `raw_session_replay_events`)

> Scroll depth en CTA click events zijn (nog) niet geconfigureerd in PostHog — alleen `$pageview`, `$autocapture`, `$pageleave`, `$web_vitals` zijn aanwezig. Om deze metrics te kunnen rapporteren moet er een PostHog scroll-tracker en custom CTA click event op de LP komen.

### 🔁 Cross-Reference (Meta ↔ PostHog)
- **Click → LP View drop-off (dag):** 9,1% (99 link clicks → 90 LP views volgens Meta). 🟢 Onder de 20% drempel.
- **Meta LP views vs PostHog meta sessies:** Meta 90, PostHog 129 → **+43% mismatch**. PostHog vangt meer dan Meta. Mogelijke oorzaken: pixel blocking, attribution window verschil, of PostHog telt sessies van users die Meta's pixel blocked. Verdere analyse nodig.
- **CTR vs Bounce per variant:**
  - H11: lage Link CTR (0,86%) + hoge bounce (63%) = ad-pagina mismatch of zwakke hook. Krijgt wel het meeste budget — herzien.
  - H13: gemiddelde Link CTR (1,06%) + laagste bounce (53,3%) + langste sessieduur = beste ad-LP combinatie.
  - H15: laagste Link CTR + hoogste bounce + kortste sessie = consistente verliezer.
- **Spend allocatie mismatch:** H11 krijgt 56,4% van het budget maar levert 51,5% van de link clicks en heeft de slechtste LP-bounce van de top 3. H13 krijgt 19,9% van het budget maar heeft de schoonste funnel.

### 🎯 Top 3 Acties
1. **H15,B3,CTA5 pauzeren** — Link CTR 0,59%, CPC link €2,31, bounce 70%, gem. sessieduur 7,7s. Geen enkele dimensie werkt. Pauze geeft ~10% budget-relief en duwt delivery naar betere varianten. **Verwachte impact:** −€14/dag wasted spend, hogere campagne-CTR. (Bron: alle metrics gecombineerd)
2. **H14 BATCH 1 onderzoeken/pauzeren** — staat ACTIVE in de oude adset (`BATCH 1`) maar krijgt 0 delivery, terwijl BATCH 2 wel uitlevert. Check of de adset ook PAUSED moet of dat de audience overlapt met BATCH 2. Als overlap → pauze BATCH 1 volledig om budget en learning te concentreren. **Verwachte impact:** schonere learning fase, geen verborgen status-flags.
3. **Wix order check + LP fix** — verifieer **vandaag** of er over 2026-04-06 t/m 2026-04-12 daadwerkelijk 2 orders zijn (en welke waarde). Tot Wix bevestigt blijft de Meta purchase waarde onbruikbaar voor ROAS. Parallel: kijk in de 87 session recordings van gisteren waarom bounce 57,8% is en sessieduur 54s — eerste hypothese is dat H11 (grootste bron, 73 sessies, 32s gem) een mismatch creëert met de LP boodschap. **Verwachte impact:** betrouwbare omzet-rapportage + concrete LP-verbetering binnen 1 sprint.

---

### Bronnen
- **Meta Ads MCP (Pipeboard):** campaign `120239435987290239` (2026: SYBB) op account `act_567892422940728`, `time_range=yesterday` en `last_7d`, `level=campaign` en `level=ad`. Link clicks via `actions.link_click`, niet `clicks`.
- **PostHog MCP:** project 149694 ("Default project"), HogQL queries op `events` en `sessions` tabellen, host filter `www.startyourballoonbusiness.com`, datum window `2026-04-12 00:00:00` t/m `2026-04-13 00:00:00` voor dag, `2026-04-06` t/m `2026-04-13` voor 7d.
- **Sanity checks toegepast:** purchase value veelvoud-check (rule 1) → IC ✅, Purchase 🚨; alle CTR/CPC met `Link`-label; geen ramingen.
