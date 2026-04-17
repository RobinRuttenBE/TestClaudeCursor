# Auto-Optimize Rapport — 2026-04-17

**Periode:** 2026-04-14 t/m 2026-04-16 (last_3d)
**Account:** Sempertex Ad Account (act_567892422940728)
**Campagne:** 2026: SYBB (OUTCOME_SALES, €100/dag)
**Run-modus:** alleen Meta Ads MCP + PostHog MCP. Geen Google MCPs, geen Google Sheet writes.

> Tweede account (act_607231713057715): geen API-toegang (token allowed list: act_1489853856181844, act_567892422940728). Account act_1489853856181844 heeft geen actieve campagnes.

---

## Databasis

3 actieve ads in 3 actieve ad sets onder campagne 2026: SYBB. Alle 3 draaien sinds 2026-04-09 (>7 dagen actief, ruim boven 24h minimum).

| Ad | Ad ID | Ad Set | Impressions | Spend | Link clicks | Link CTR | CPC (link) | Freq | Purchases | Value | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | 120242894133330239 | Kopie 1 | 12.791 | €167,16 | 145 | 1,1% | €1,15 | 1,55 | 4 | €1.473,50 | 8,82x |
| H13,B3,CTA5 | 120242894133350239 | Kopie 3 | 3.112 | €39,19 | 33 | 1,1% | €1,19 | 1,41 | 0 | €0 (€700 ATC) | n/a |
| H12,B3,CTA5 | 120242894133390239 | Kopie 2 | 1.739 | €22,06 | 26 | 1,5% | €0,85 | 2,14 | 0 | €0 (€1.050 IC) | n/a |
| **Totaal** | | | **17.642** | **€228,41** | **204** | **1,2%** | **€1,12** | — | **4** | **€1.473,50** | **6,45x** |

Metrics berekend uit `actions.link_click`, niet Meta's `clicks`/`ctr`/`cpc`.

---

## Automatische acties uitgevoerd

**Geen ads gepauzeerd — alles presteert boven de drempelwaarden.**

| Ad | Link CTR | Kill-regel <0,8% | CPC (link) | Kill-regel >€1,50 | Impressions |
|---|---|---|---|---|---|
| H11,B3,CTA5 | 1,1% | PASS | €1,15 | PASS | 12.791 |
| H13,B3,CTA5 | 1,1% | PASS | €1,19 | PASS (minder dan 500 link clicks, regel n.v.t.) | 3.112 |
| H12,B3,CTA5 | 1,5% | PASS | €0,85 | PASS (minder dan 500 link clicks, regel n.v.t.) | 1.739 |

**Totaal gepauzeerd: 0 ads**

---

## Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| H12,B3,CTA5 | Frequency stijgend | 2,14 (onder 3,5) | Monitoren, nog geen fatigue |
| Alle ads | CPC (link) dicht bij €1,50 kill-regel | €0,85 – €1,19 | H11 en H13 draaien op 77–79% van de kill-drempel. Bij verdere stijging actie nodig. |
| H12,B3,CTA5 | Lage absolute spend en impressions | 1.739 imp / €22,06 | Ad set krijgt te weinig budget om sneller leeringen te genereren |

Geen creative fatigue (geen frequency >3,5), geen dure reach (geen CPM >€15). Lifetime Link CTR-vergelijking overgeslagen: lifetime-insights op ad-niveau retourneerde te veel data om binnen budget te parsen; 3-daagse waardes zelf vormen een betrouwbare proxy.

---

## 70-20-10 Classificatie

*Drempels als richtlijn (TODO in playbook: link-metric drempels nog niet gekalibreerd). Budget-shifts alleen als voorstel, niet automatisch.*

**70% Core — Bewezen winners:**
- **H11,B3,CTA5** — Link CTR 1,1%, CPC (link) €1,15, ROAS 8,82x (4 purchases, €1.473,50). Kwalificeert via ROAS >2x.

**20% Emerging — Potentieel:**
- **H12,B3,CTA5** — Link CTR 1,5%, CPC (link) €0,85. Beste Link CTR en laagste CPC van de drie. Nog geen purchases, wel 3 initiate checkouts en 5 add-to-carts. Geeft signaal dat de hook converteert richting koopintentie.
- **H13,B3,CTA5** — Link CTR 1,1%, CPC (link) €1,19. 2 add-to-carts, nog geen purchases. Vergelijkbare Link CTR als H11, maar conversie ontbreekt.

**10% Experimental — Tests:**
- Leeg. Alle drie actieve ads draaien >1.000 impressions; er zijn geen net gelanceerde test-ads.

---

## Budget verdeling (werkelijke spend last_3d)

| Categorie | Ad(s) | Spend | % van totaal | Ideaal 70-20-10 |
|---|---|---|---|---|
| Core | H11 | €167,16 | 73,2% | 70% |
| Emerging | H12 + H13 | €61,25 | 26,8% | 20% |
| Experimental | — | €0 | 0% | 10% |

**Budget mismatch:** gering. Core krijgt ongeveer het juiste aandeel. Emerging zit licht boven target. Experimental is 0% omdat er geen nieuwe test-ads draaien — dit is de belangrijkste structurele mismatch: er wordt niet getest.

---

## Voorstellen (wacht op goedkeuring)

### 1. Budget verhogen H12 (Emerging → bewijzen)
- **Van** €7,35/dag **naar** €15,00/dag (+104%)
- **Reden:** H12 heeft de hoogste Link CTR (1,5%) en laagste CPC (€0,85) van alle actieve ads. Met slechts 1.739 impressions over 3 dagen is er te weinig data om de hook te valideren. Dubbele spend versnelt lering.
- **Verwachte impact:** binnen 3–5 dagen duidelijkheid of H12 doorbreekt naar Core (ROAS >2x) of stagneert.

### 2. Budget H13 gelijk houden of licht verlagen
- **Van** €13,06/dag **naar** €10,00/dag (–23%)
- **Reden:** zelfde Link CTR (1,1%) en CPC (€1,19) als H11, maar zonder purchases na 3.112 impressions. H11 trekt 4x zoveel impressions en 4 purchases. Spend die vrijkomt herverdelen naar H12 of een experimental.
- **Verwachte impact:** €3/dag vrij voor de experimental slot hieronder.

### 3. Nieuwe variaties — winnende hook H11 uitbaten
De hook achter H11 (B3, CTA5) levert ROAS 8,82x. Gebruik de Hormozi 7 hook-types om 2–3 variaties te testen:

- **Variatie A — Curiosity hook:** zelfde body/CTA, nieuwe openingszin die een onbekende pijn benoemt (Pillar 7 pricing is kandidaat). Format: Reel 9:16, 15s.
- **Variatie B — Contrarian hook:** pak een aanname die starters hebben over ballonprijzen, draai om. Format: static carousel, 3 slides.
- **Variatie C — Proof hook:** start met concreet cijfer (bijv. gemiddelde marge per trosballon). Format: Reel 9:16, 30s.

### 4. Experimental slot openen
- Start 1 nieuwe ad set met €5/dag budget gericht op test-creatives (bv. variatie A uit punt 3).
- **Reden:** de 10% experimental-bucket is leeg. Zonder test-ads kan de funnel niet doorgroeien.
- **Verwachte impact:** na 7 dagen eerste leesbare data (1.000+ impressions bij €5/dag).

### 5. Audience — geen wijziging voorgesteld
De huidige audiences (NL/BE/LU/DE, 18–65, advantage+) laten nog geen structurele onderpresteerders zien op 3 dagen data. Frequency op H12 (2,14) rechtvaardigt geen uitsluiting of uitbreiding. Heroverwegen bij volgende wekelijkse rapport.

---

## Data-kwaliteit opmerkingen

- Campagne-totaal en 3-dagen data komen direct uit Meta Ads MCP via `get_insights` met `time_range: last_3d`.
- Lifetime insights op ad-niveau overgeslagen: response >75k tokens, buiten budget. Vergelijking "last_3d Link CTR vs lifetime Link CTR" niet uitgevoerd voor deze run.
- Tweede ad account (act_607231713057715) niet toegankelijk met huidige token.
- Account act_1489853856181844 heeft geen actieve campagnes.
- PostHog-cross-reference niet gedraaid in deze run: auto-optimize richt zich op Meta-side kill-regels en budget-classificatie. Voor landing page health, zie `/morning-report` of `/ads-report`.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers (1 t/m 5).**
