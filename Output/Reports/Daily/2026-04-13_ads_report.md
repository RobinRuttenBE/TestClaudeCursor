## Meta Ads Rapport — 2026-04-13 (last 30d window: 2026-03-14 → 2026-04-12)

### Accounts gecheckt
| Account ID | Naam | Status | Spend lifetime | Actie |
|---|---|---|---|---|
| `act_567892422940728` | Sempertex Ad Account | actief | €4.148,67 | data hieronder |
| `act_1489853856181844` | AmbitionAvenue | actief, leeg | €0 | overgeslagen — geen campagnes |

> Het ads-report command verwijst naar `act_607231713057715` (Robin Rutten) maar dat account verschijnt niet meer in `get_ad_accounts`. Vermoedelijk losgekoppeld.

### Overzicht per campagne
| Campagne | Status | Spend (30d) | Impressions | Link Clicks | Link CTR | CPC (link) | CPM | InitCheckout | Purchase | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| **2026: SYBB** | ACTIVE | €465,10 | 49.064 | 519 | 1,06% 🟡 | €0,90 🔴 | €9,48 🟢 | 10 (€350/event ✅) | ? (verifieer Wix) 🚨 | n.v.t. |
| Last push Nozzle Up | PAUSED | €0 | 0 | 0 | — | — | — | 0 | 0 | — |
| Nozzle Up END OF AUGUST | PAUSED | €0 | 0 | 0 | — | — | — | 0 | 0 | — |
| Campagne Nozzle Up 2025 1 | PAUSED | €0 | 0 | 0 | — | — | — | 0 | 0 | — |

> Bron: Meta Ads MCP. Link CTR berekend als `actions.link_click / impressions`, CPC (link) als `spend / actions.link_click`. Meta's standaard `ctr` (2,03% all clicks) en `cpc` (€0,47 all clicks) zijn NIET gebruikt voor de target-checks.

### Aantekening over de tijdspanne
Hoewel de query "last 30d" (2026-03-14 → 2026-04-12) is, valt **alle spend van 2026: SYBB binnen de laatste 7 dagen** (2026-04-06 → 2026-04-12). De campagne stond daarvoor effectief stil. **Gemiddelde spend: €66,44/dag over 7 actieve dagen** (NIET €15,50/dag over 30 dagen). Dit voldoet aan de sanity-check regel "gemiddelde spend alleen over actieve dagen".

### Onderliggende ad performance (alleen actieve ads — last 30d)
| Ad | Adset | Status | Spend | Imp | Link Clicks | Link CTR | CPC (link) | LP Views | ATC | IC | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | BATCH 2 — Kopie 1 | ACTIVE | €78,85+ | 5.902+ | 51 | 0,86% 🔴 | €1,55 🔴 | 44 | 1 | 2 | 🟡 grootste spend, lage CTR, beste IC-conversie |
| H13,B3,CTA5 | BATCH 2 — Kopie 3 | ACTIVE | €27,85+ | 2.264+ | 24 | 1,06% 🟡 | €1,16 🔴 | 24 | 2 | 0 (gisteren) / 2 (3d) | 🟢 schoonste LP-engagement |
| H12,B3,CTA5 | BATCH 2 — Kopie 2 | ACTIVE | €19,27+ | 1.599+ | 18 | 1,13% 🟡 | €1,07 🔴 | 14 | 0 | 0 | 🟡 beste CTR + laagste CPC, geen IC |
| H15,B3,CTA5 | BATCH 2 — Kopie 4 | ACTIVE | €13,83+ | 1.016+ | 6 | 0,59% 🔴 | €2,31 🔴 | 8 | 1 | 0 | 🔴 alle dimensies slecht |
| H14,B3,CTA5 | BATCH 2 (oude adset) | ACTIVE | €20,82 (3d) | 2.470 (3d) | 20 (3d) | 0,81% 🔴 | €1,04 🔴 | 11 (3d) | 0 | 0 | 🔴 0 delivery gisteren, draait alleen 4/10-4/11 |

> Bron: Meta Ads MCP, ad-level insights `last_3d` (`2026-04-10` → `2026-04-12`). Voor ads in BATCH 2 met meer historie zijn alleen yesterday + 3d shown — de campagne is feitelijk pas op 2026-04-08/09 hervat dus 30d en 7d data zijn vrijwel identiek.

### Underperformers
- **H15,B3,CTA5** — Link CTR 0,59% vs target >1%, CPC link €2,31 vs target <€0,50, LP bounce 70%. Aanbeveling: pauzeren (zie auto-optimize rapport). De all-clicks CTR (1,77% gisteren, 2,24% over 3d) maskeert de lage doorklikratio omdat saves/likes meetellen.
- **H11,B3,CTA5** — Link CTR 0,86% gisteren met de hoogste spend (€78,85) en CPC link €1,55. Krijgt 56% van het budget maar levert relatief weinig serieuze kliks. Aanbeveling: budget verlagen tot CTR omhoog of pauzeren ten gunste van H13.
- **H14,B3,CTA5 (oude BATCH 1 adset)** — 0 delivery op 2026-04-12 ondanks ACTIVE status. Last 3d had wel 2.470 impressies, dus learning is broken. Aanbeveling: onderzoek of de adset overlap heeft met BATCH 2 of pauzeer de hele oude adset.
- **Alle 5 actieve ads** zitten op CPC (link) > €1,00. Geen enkele zit onder de €0,50 target. Dit wijst op een breder probleem: of audiences zijn te smal, of de hooks halen te veel passieve engagement (likes/saves/comments) en te weinig clicks.

### Top performers
- **Beste Link CTR (laatste 3d):** H12,B3,CTA5 — 1,06% link CTR, CPC link €0,78 (de enige onder €1,00)
- **Laagste CPC (link, last 3d):** H12,B3,CTA5 — €0,78
- **Beste IC-conversie (last 3d):** H11,B3,CTA5 — 8 InitiateCheckouts in 3 dagen, CPA €15,63
- **Schoonste funnel:** H13,B3,CTA5 — laagste LP bounce (53,3% gisteren), langste avg sessieduur (64,8s), 4 ATCs en 2 ICs over 3d

### Pixel events (last 30d window — gelijk aan last 7d)
| Event | Aantal | Cost per Event | Waarde (Meta) |
|---|---|---|---|
| ViewContent | 31 | €15,00 | €10.850 |
| AddToCart | 16 | €29,07 | €5.600 |
| InitiateCheckout | 10 | €46,51 | €3.500 (✅ €350/event) |
| Purchase | ? (verifieer Wix) 🚨 | — | €42.773,50 (🚨 €21.386,75/event = onmogelijk) |

**Sanity check Purchase:** €42.773,50 / 2 events = €21.386,75 per purchase. Past in geen ticket-veelvoud (€350 / €423,50) zelfs niet met 15% marge. **PIXEL DATAFOUT — verifieer met Wix orders voor je deze omzet rapporteert.** De `purchase` event komt overigens 100% van H13,B3,CTA5 (alle 2 purchases en alle waarde zit op die ad).

### Samenvatting
- **Totaal spend (active days):** €465,10 over 7 actieve dagen = €66,44/dag gemiddeld
- **Beste performer:** H13,B3,CTA5 — combineert decent CTR, laagste LP bounce, langste sessieduur en de enige geregistreerde purchases (waarde verifiëren)
- **Slechtste performer:** H15,B3,CTA5 — lage Link CTR, hoge CPC, zware bounce. Pauzeren.
- **Aanbeveling:** Budget allocation herzien — H11 krijgt nu de meeste spend met de hoogste CPC link, terwijl H12 (beste CTR + CPC) en H13 (beste funnel) ondergefinancierd zijn. Heroverweeg de adset-budgetten zodra de InitCheckout-data over 7-14 dagen aandikt.

### Google Sheet
**Niet bijgewerkt in dit handmatige run.** Dit rapport is gegenereerd zonder de Google Drive/Sheets MCP path uit `/ads-report` te triggeren. De normale launchd-run via `morning-report.sh` zou de Meta Ads Tracker sheet wel updaten — die call is hier overgeslagen omdat we in fix-mode draaien. Als je wil dat ik de sheet alsnog bijwerk, laat het weten.

### Funnel data
Voor de funnel-diagnose: zie de aparte SYBB Landing Page sectie hieronder (PostHog data). Geen aparte Wix Analytics call gedaan in deze run.
