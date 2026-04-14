## /ads-auto-optimize Rapport — 2026-04-13 (last 3d window: 2026-04-10 → 2026-04-12)

> **MODUS: ALLEEN-RAPPORTEREN.** Geen ads, ad sets of campagnes zijn gewijzigd in deze run. Niveau 1 acties (auto-pauze) zijn geanalyseerd maar **niet uitgevoerd**, op uitdrukkelijk verzoek van Robin. Geen `update_ad`, `update_adset` of `update_campaign` calls gemaakt.

### 1. Niveau 1: Kill-regels (auto-pauze drempels)

Geanalyseerd op 5 actieve ads in campagne `2026: SYBB`:

| Regel | Drempel | Min. data | Resultaat |
|---|---|---|---|
| Lage CTR | CTR (all clicks) < 0,5% | ≥ 1.000 impressies | **0 ads triggeren** |
| Hoge CPC | CPC (all clicks) > €1,00 | ≥ 500 clicks | **0 ads triggeren** (geen ad heeft 500+ all clicks in 3d) |

**Per ad — kill rule check:**
| Ad | Imp (3d) | All Clicks | All-Clicks CTR | All-Clicks CPC | CTR-rule | CPC-rule | Auto-pauze? |
|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | 10.372 | 198 | 1,91% | €0,63 | 🟢 boven 0,5% | 🟢 onder min clicks | nee |
| H12,B3,CTA5 | 9.627 | 212 | 2,20% | €0,37 | 🟢 boven 0,5% | 🟢 onder min clicks | nee |
| H13,B3,CTA5 | 7.284 | 137 | 1,88% | €0,59 | 🟢 boven 0,5% | 🟢 onder min clicks | nee |
| H15,B3,CTA5 | 4.014 | 90 | 2,24% | €0,45 | 🟢 boven 0,5% | 🟢 onder min clicks | nee |
| H14,B3,CTA5 | 2.470 | 42 | 1,70% | €0,50 | 🟢 boven 0,5% | 🟢 onder min clicks | nee |

**Conclusie kill-regels:** geen enkele ad triggert de auto-pauze drempels op de standaard Meta `ctr` (all-clicks) en `cpc` (all-clicks) velden. Dit is opvallend gegeven dat **alle 5 ads ruim boven de Link CPC target van €0,50 zitten** als je rekent met `actions.link_click`. Het auto-optimize command werkt momenteel met all-clicks metrics — ik adviseer dit te updaten naar Link CTR/CPC zoals het morning-report command voorschrijft.

> **Actie als kill-regels zouden draaien op LINK metrics (CPC link > €1, ≥500 link clicks):** ook dan zou geen ad triggeren (max 106 link clicks in 3d). De campagne heeft simpelweg te weinig volume voor de huidige drempels.

### 2. Niveau 1 (alternatief, geen update_ad uitgevoerd)
Als ik de drempels zou versoepelen naar **Link CTR < 1,0% met ≥1.000 impressies**, dan zouden deze ads gepauzeerd worden:

| Ad | Imp | Link Clicks | Link CTR | Zou-pauzeren? |
|---|---|---|---|---|
| H15,B3,CTA5 | 4.014 | 49 | 1,22% | nee |
| H14,B3,CTA5 | 2.470 | 20 | 0,81% | **ja** (als drempel <1%) |
| H11,B3,CTA5 | 10.372 | 106 | 1,02% | nee |

**Aanbeveling:** stel met Robin een nieuwe drempel-set in voor de auto-pauze, gebaseerd op Link CTR/CPC en realistische volumes voor SYBB scope (~€100/dag). Voorstel:
- Lage Link CTR: < 0,8% met ≥ 2.000 impressies
- Hoge CPC link: > €2,00 met ≥ 30 link clicks
- Met deze drempels zou H14 (Link CTR 0,81%, 2.470 imp) net buiten vallen en H15 op 30d (Link CTR 0,59%, 1.016 imp) wel triggeren zodra de impressie-drempel zakt naar 1.000.

### 3. Waarschuwingsregels (alleen rapporteren)

| Regel | Drempel | Resultaat |
|---|---|---|
| Creative fatigue (Frequency > 3,5) | — | 🟢 alle ads onder 1,7 frequency. Geen fatigue. |
| Dure reach (CPM > €15) | — | 🟢 alle ads onder €13 CPM. Audience is gezond breed. |
| Dalende CTR (3d < 70% van lifetime) | — | n.v.t. — campagne draait pas 6 dagen, geen lifetime baseline om tegen te vergelijken |

### 4. Niveau 2: Voorstellen (vereisen Robin's goedkeuring)

#### Voorstel A — Pauzeer H15,B3,CTA5
**Waarom:** Op 30d/7d niveau:
- Link CTR 0,59% (slechtste van alle 5)
- CPC link €2,31 (slechtste van alle 5)
- LP bounce 70%, gemiddelde sessieduur 7,7s (LP onkend door bezoeker)
- 1 ATC, 0 IC ondanks 8 LP views

Op 3d niveau (waar de drempels naar kijken) levert H15 wel betere getallen op (Link CTR 1,22%, CPC link €0,83) — vermoedelijk omdat de ad recent meer impressies krijgt. Dit maakt de beslissing minder zwart-wit. **Aanbeveling:** wacht 2 dagen extra delivery voor je pauzeert, OF pauzeer nu en dump de spend in H13.

**Verwachte impact:** −€14/dag wasted spend, +1-2% campagne Link CTR.

#### Voorstel B — Pauzeer H14,B3,CTA5 (oude BATCH 1 adset)
**Waarom:**
- 0 delivery op 2026-04-12 ondanks ACTIVE status
- Lage Link CTR (0,81% over 3d)
- Zit in een aparte adset (`120241274560730239`) die mogelijk concurrentie veroorzaakt met BATCH 2 (audience overlap)
- Geen IC of ATC over 3d

**Aanbeveling:** Pauzeer de hele oude adset BATCH 1 (`120241274560730239`) — niet alleen deze ad. Dit elimineert audience overlap met de nieuwere BATCH 2 adsets en concentreert learning op één set creatives.

**Verwachte impact:** schonere learning fase, geen verborgen ACTIVE status flags, betere delivery distributie binnen BATCH 2.

#### Voorstel C — Budget shift naar H13 + H12
**Waarom:** H13 heeft de laagste LP bounce (53,3%), langste avg sessieduur (64,8s), 4 ATCs en (volgens Meta) 2 purchases over 3d. H12 heeft de hoogste Link CTR (1,06%) en laagste CPC link (€0,78). Beide krijgen samen 22,4% van het budget terwijl H11 alleen 56,4% krijgt met slechtere LP-engagement.

**Aanbeveling:** bij CBO/Advantage+ campaign budget zou ik niet handmatig herverdelen — Meta's algoritme moet dit doen. Als de budgetten op adset-niveau zitten: shift €15-20/dag van Kopie 1 (H11) naar Kopie 2 (H12) en Kopie 3 (H13).

**Verwachte impact:** meer link clicks voor zelfde spend, meer ATCs/ICs op de schoonste funnels. Risico: H11 geeft op dit moment de meeste IC's — niet zomaar wegschuiven zonder B/C testen.

#### Voorstel D — Nieuwe ad variaties op H13's hook
**Waarom:** H13 is de schoonste funnel-presteerder maar is slechts 1 creative. Maak 2-3 variaties op de winning hook (B3 en CTA5 vasthouden, intro 3-5s aanpassen). Volgens de Hormozi 70-20-10 regel: 70% bewezen winnaars, 20% variaties, 10% experimenten.

**Verwachte impact:** verspreid winning creative over meer audience-segments zonder fatigue.

#### Voorstel E — Onderzoek pixel datafout
**Waarom:** H13 toont 2 purchases met waarde €42.773,50 (€21.386,75 per purchase). Dit is onmogelijk gegeven de SYBB ticket prijs (€350 ex / €423,50 incl). Zie de SYBB rapport sanity check sectie.

**Aanbeveling:** check Wix orders voor 2026-04-06 → 2026-04-12 met een filter op SYBB tickets. Vergelijk het werkelijke aantal en de werkelijke waarde met wat Meta meldt. Mogelijke oorzaken:
1. Conversion API stuurt foute waardes (test events, factor 100x of dergelijke)
2. Een test order met onrealistische waarde
3. Pixel mapping issue tussen `purchase` en `web_in_store_purchase`

**Verwachte impact:** betrouwbare ROAS-rapportage, voorkomt foute beslissingen op basis van fake omzet.

### 5. Samenvatting auto-optimize
- **Auto-pauzes uitgevoerd:** 0 (modus alleen-rapporteren)
- **Voorstellen ter goedkeuring:** 5 (Voorstel A t/m E)
- **Eerstvolgende manual actie:** Voorstel E (Wix order check) — blokkeert betrouwbare beslissingen op alle andere voorstellen tot purchase data klopt
- **Tweede manual actie:** Voorstel B (BATCH 1 adset pauze) — quick win, geen risico
- **Derde manual actie:** Voorstel A (H15 pauze) — wacht 2 dagen extra data voor harde beslissing

### Niet-acties
- Geen `update_ad` calls gemaakt
- Geen `update_adset` calls gemaakt
- Geen `update_campaign` calls gemaakt
- Geen Google Sheet writes
- Geen test events of pixel calls
