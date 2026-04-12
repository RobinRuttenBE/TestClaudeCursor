# 📊 SYBB Rapport, 2026-04-12 (data van gisteren 2026-04-11)

**Campagne:** `2026: SYBB` (ID `120239435987290239`)
**Ad account:** Sempertex Ad Account (`act_567892422940728`)
**Databronnen:** Meta Ads MCP (Pipeboard), PostHog MCP (project 149694)

---

## ⚡ Samenvatting

Spend is gisteren verdubbeld t.o.v. de voorgaande dagen (€138.06 vs ~€62/dag avg). Link CTR en CPC (link) blijven onder target met respectievelijk 1.09% en €0.87. De pixel rapporteert een totaal onrealistische purchase waarde van €42.773,50, dat is een van de grootste rode vlaggen van vandaag. PostHog toont 47% meer meta-sessies dan Meta LP views rapporteert, wat wijst op pixel blocking of missing fires.

---

## 🚩 Rode Vlaggen

1. **🔴 PIXEL DATAFOUT, purchase waarde onrealistisch.** Meta rapporteert `€42,773.50` purchase value voor 2 purchases, dat is `€21,386.75` per purchase. SYBB workshop kost €350 ex BTW (€423,50 incl). Correcte waarde: **2 × €423,50 = €847,00**. Vermoedelijk Wix product variant fout ingesteld in Meta Pixel event, of custom parameter met verkeerde conversie. **Verifieer het aantal purchases met Wix orders** en fix het pixel event waarde schema.
2. **🔴 DATA MISMATCH, Meta LP views vs PostHog sessions wijken 47% af.** Meta rapporteert 123 landing_page_views, PostHog ziet 181 sessies met `utm_source=meta` op dezelfde dag. Boven de 30% drempel. Vermoedelijke oorzaken: iOS Safari ITP pixel blocking (93% van verkeer is mobile), PostHog session cutoff van 30 min dat één klik in meerdere sessies knipt, of meta pixel dat later fire't dan PostHog snippet.
3. **🔴 CPC (link) €0.87, ruim boven target €0.50.** Gisteren was het piek, vandaag lijkt het door te stijgen (€1.40 op 2026-04-12 partial).
4. **🔴 Bounce rate 82.7%, ver boven 70% trigger.** Consistent met 7d gemiddelde. Landingspagina `/` heeft 83% bounce.
5. **🟡 Link CTR 1.09%, nipt boven target 1%.** Net niet gealarmeerd maar geen marge.
6. **🟡 Frequency 1.63.** OK, onder drempel 3.

---

## 📈 Meta Ads Performance, campagne niveau

Periode: 2026-04-11 (gisteren). 7d gem berekend over **5 actieve dagen** (2026-04-08 t/m 2026-04-12), geen gepauzeerde dagen in deze range, spend >€0 op alle 5 dagen.

| Metric | Gisteren 2026-04-11 | 7d Gem (5 actieve dagen) | Trend | Target | Status |
|---|---|---|---|---|---|
| Spend | €138.06 | €91.12/dag | ↑ 51% | , | , |
| Impressions | 14,509 | 9,670.6/dag | ↑ 50% | , | , |
| Link clicks (`actions.link_click`) | 158 | 102.6/dag | ↑ 54% | , | , |
| All clicks (`clicks`) | 285 | 196.6/dag | ↑ 45% | , | , |
| **Link CTR** (`link_clicks/impressions`) | **1.09%** | 1.06% | ↑ 3% | >1% | 🟡 |
| All Clicks CTR (ter referentie) | 1.96% | 2.03% | → | , | , |
| **CPC (link)** (`spend/link_clicks`) | **€0.874** | €0.888 | ↓ 2% | <€0.50 | 🔴 |
| CPC (all) (ter referentie) | €0.484 | €0.464 | ↑ 4% | , | , |
| CPM | €9.52 | €9.42 | → | , | , |
| Reach | 8,916 | 6,591/dag | ↑ 35% | , | , |
| Frequency | 1.63 | 1.47 | ↑ | <3.0 | 🟢 |
| Landing page views | 123 | 78.4/dag | ↑ 57% | , | , |

*Bron: Meta Ads MCP. `clicks` en standaard `ctr`/`cpc` uit Meta API zijn ALL clicks metrics, niet doorkliks. De Link CTR en CPC (link) zijn berekend uit `actions.link_click`.*

---

## 🎬 Ad Variant Performance, 2026-04-11

| Ad naam | Spend | Link clicks | Link CTR | CPC (link) | LP views | IC | ATC | Purch | Flag |
|---|---|---|---|---|---|---|---|---|---|
| H12,B3,CTA5 (Kopie 2) | €39.36 | 56 | 1.10% | €0.703 | 45 | 0 | 0 | 0 | 🟢 beste CPC |
| H13,B3,CTA5 (Kopie 3) | €37.84 | 40 | 1.20% | €0.946 | 34 | 2 | 2 | 2* | 🟡 alle conv |
| H11,B3,CTA5 (Kopie 1) | €29.99 | 26 | 0.93% | €1.154 | 22 | 4 | 4 | 0 | 🔴 Link CTR + CPC |
| H15,B3,CTA5 (Kopie 4) | €19.19 | 26 | 1.30% | €0.738 | 16 | 0 | 0 | 0 | 🟢 CTR OK |
| H14,B3,CTA5 | €11.68 | 10 | 0.77% | €1.168 | 6 | 0 | 0 | 0 | 🔴 slechtste |

\* Purchase aantal = 2 staat op de H13 Kopie 3 ad. **Verifieer het aantal purchases met Wix orders** voor 2026-04-11. De pixel purchase value is onbruikbaar (zie rode vlag 1).

**Beste variant:** H12,B3,CTA5 Kopie 2. Laagste CPC (link) van alle ads (€0.70), grootste volume link clicks (56), solide Link CTR 1.10%, goede LP view ratio (80% LP view / link click).

**Slechtste variant:** H14,B3,CTA5. Link CTR 0.77% en CPC (link) €1.17 beide het slechtst. Slechts 6 LP views op 10 link clicks, geen conversies.

**Delivery check:** 5 van de 5 getoonde ads kregen delivery gisteren. De 3 ads die in het 7d data ook actief waren (H12 origineel, H13 origineel, H15 origineel) hebben gisteren geen delivery gehad, vermoedelijk door lage bid scores of budget rotatie naar Kopie varianten.

---

## 📡 Pixel Events, 2026-04-11

| Event | Aantal | Cost per Event | Waarde per event | Status |
|---|---|---|---|---|
| ViewContent | 8 | €17.26 | €350.00 | 🟡 (350 = 1 workshop ex BTW, plausibel) |
| AddToCart | 6 | €23.01 | €350.00 | 🟡 (idem) |
| InitiateCheckout | 6 | €23.01 | €350.00 | 🟡 (idem) |
| Purchase | 2 | €69.03 | **€21,386.75** | 🔴 PIXEL DATAFOUT |

De Meta campagne is geoptimaliseerd op `InitiateCheckout` (zie "Results" in Ads Manager). Dat is **NIET** een lead, het is een IC event. CAC op IC = €23.01 gisteren. Op Purchase (indien je de 2 echt-telt als orders): €69.03, met correcte revenue €847 → ROAS = 6.1x op de 2 purchases van deze campagne.

**⚠️ Verifieer het aantal purchases met Wix orders.** Zonder Wix cross-check is zelfs het aantal onbetrouwbaar.

---

## 🌐 Landing Page Health, PostHog

Periode: 2026-04-11 00:00 CEST tot 2026-04-12 00:00 CEST (UTC 04-10 22:00 tot 04-11 22:00).

| Metric | Gisteren | Target | Status |
|---|---|---|---|
| Sessies | 197 | , | , |
| Pageviews | 256 | , | , |
| **Bounce rate** | **82.7%** | <55% | 🔴 |
| Avg Session Duration | 46.5 sec | >90s | 🔴 |
| PV per session | 1.30 | , | , |

Scroll depth en CTA click rate: **Niet geconfigureerd** (geen PostHog custom events op scroll/click). Adviseer de PostHog autocapture uit te breiden met `$autocapture` of handmatige events op de primary CTA's (`/product-page/...` en `/booking` links).

**Device breakdown:**
| Device | Sessions | % |
|---|---|---|
| Mobile | 183 | 92.9% |
| Desktop | 10 | 5.1% |
| Tablet | 4 | 2.0% |

**Traffic bronnen (via utm_source, case-insensitive):**
| utm_source | Sessions |
|---|---|
| `meta` | 181 |
| `none` (direct/ongetagd) | 20 |
| `instagram` | 1 |

*Bron: PostHog MCP, HogQL query op `events` tabel gefilterd op `properties.$host = 'www.startyourballoonbusiness.com'`.*

**Entry pages (per sessie):**
| Entry page | Sessies | Bounce |
|---|---|---|
| `/` | 193 | 83.0% |
| `/booking` | 4 | 75.0% |

Minimum datadrempel: 197 sessies >= 50, bounce/duration cijfers zijn valide. `/booking` als entry page heeft slechts 4 sessies dus bounce rate is niet statistisch betrouwbaar.

---

## 🔄 Cross-Reference, Meta Ads ↔ PostHog

| Bron | Aantal |
|---|---|
| Meta link clicks | 158 |
| Meta landing page views | 123 |
| PostHog sessies totaal | 197 |
| PostHog sessies met `utm_source ~= meta` | 181 |
| PostHog sessies `none` (direct/ongetagd) | 20 |

**Meta LP views vs PostHog meta-sessies:** `(181 , 123) / 123 = +47.2%` → boven 30% drempel → **DATA MISMATCH, Meta LP views vs PostHog sessions wijken 47% af.**

**Meta link clicks vs PostHog meta-sessies:** 158 vs 181 = PostHog +14.6% hoger dan Meta link clicks. Dat kan niet kloppen als de funnel is click → LP view → session, tenzij:
1. PostHog telt refreshes of tabs-opnieuw-openen als nieuwe sessie (30 min cutoff)
2. Mensen komen terug op de meta-tagged URL (bookmark of browser history) en de utm_source plakt
3. Sommige directe bezoekers hadden eerder een meta sessie, PostHog attribueert op basis van `$initial_utm_source` van de persoon

**Meta link clicks vs Meta LP views:** 158 → 123 = **78% LP view rate**, dat betekent 22% drop tussen klik en laad. Acceptabel, maar net aan de hoge kant (trigger >20% drop).

**Conclusie:** Pixel is waarschijnlijk onderrapportage. Met 93% mobile verkeer (iOS ITP) verliest Meta Pixel een groot deel van de LP view fires. Vertrouw PostHog meer voor volume metrics, Meta voor relatieve CTR/CPC-vergelijking tussen ads.

---

## 🎯 Top 3 Acties

1. **Pauzeer of herwerk H14,B3,CTA5.** Link CTR 0.77% en CPC (link) €1.17 zijn de slechtste in de set. €11.68 spend gisteren leverde 6 LP views en 0 conversies op. Herwerk de hook of vervang door H16 variant. Verwachte impact: €8 tot €12 spend/dag herverdeeld naar betere ads, 5 tot 8 extra LP views/dag.
2. **Fix de pixel purchase value.** Meta rapporteert €42.773,50 voor 2 purchases. Check in Wix Analytics → Pixels → Meta Pixel event schema of het `value` veld correct uit de product variant price wordt gepakt. Verwachte impact: ROAS wordt betrouwbaar, optimization naar Purchase event wordt mogelijk (nu zit campagne op IC).
3. **Verifieer handmatig het aantal purchases op 2026-04-11 in Wix orders.** Meta telt 2 purchase events. Als Wix er 2 heeft, is het aantal juist en alleen de waarde fout. Als Wix er 0 of 3 heeft, is er ook een fire-consistency probleem. Verwachte impact: helderheid over welke correctie nodig is.

---

## Data Integriteit notes

- Alle metrics uit Meta Ads MCP (Pipeboard). Link CTR en CPC (link) zijn berekend, niet overgenomen uit Meta's standaard `ctr`/`cpc` velden (dat zijn ALL clicks metrics).
- Alle landing page metrics uit PostHog MCP, HogQL queries op `events` tabel.
- Gemiddelden over **5 actieve dagen** (2026-04-08 t/m 2026-04-12), geen gepauzeerde dagen in deze window.
- Geen verzonnen of geschatte metrics. Scroll depth en CTA click rate zijn niet gerapporteerd want niet geconfigureerd in PostHog.
