# Auto-Optimize Rapport — 2026-05-25

## Samenvatting

**Geen actieve ads om te optimaliseren.** Alle campagnes op het Sempertex Ad Account staan op PAUSED. Er zijn geen ad-impressies in de laatste 3 dagen. Niveau 1 (auto-pauzeren) en Niveau 2 (voorstellen) zijn niet van toepassing tot er weer een campagne live gaat.

---

## Account scan

| Account | Toegang | Actieve campagnes | Totaal campagnes |
|---|---|---|---|
| act_567892422940728 (Sempertex Europe) | ✅ | 0 | 5 (allen PAUSED) |
| act_1489853856181844 | ✅ | 0 | 0 |
| act_607231713057715 | ❌ (token mist permissies) | n.v.t. | n.v.t. |

### Status per campagne (act_567892422940728)

| Campagne | Status | Laatste update | Objective | Daily budget |
|---|---|---|---|---|
| 2026: SYBB - Kopie | PAUSED | 2026-04-20 | OUTCOME_SALES | — |
| 2026: SYBB | PAUSED | 2026-04-19 | OUTCOME_SALES | €100,00 |
| Last push Nozzle Up | PAUSED | 2025-09-21 | OUTCOME_SALES | — |
| Nozzle Up END OF AUGUST | PAUSED | 2025-09-15 | OUTCOME_SALES | €70,00 |
| Campagne Nozzle Up 2025 1 | PAUSED | 2025-09-15 | OUTCOME_SALES | €30,00 |

De meest recente activiteit dateert van rond **19-20 april 2026**, toen de SYBB campagne (en de kopie) op PAUSED zijn gezet. Sindsdien geen ad delivery.

---

## ⚡ Automatische acties uitgevoerd

Geen. Er zijn geen ACTIVE ads om tegen de kill-regels (Link CTR < 0.8% bij ≥1.000 imp, CPC link > €1.50 bij ≥500 link clicks) te toetsen.

## ⚠️ Waarschuwingen

Geen ad-niveau waarschuwingen mogelijk zonder delivery data.

**Operationele waarschuwing:** SYBB campagne staat ~5 weken stil. Funnel-tests, audience-leerdata en pixel-signaal degraderen elke week dat er geen verkeer komt. Als de campagne weer aangaat is een nieuwe learning phase waarschijnlijk.

## 📊 70-20-10 Classificatie

Niet uitvoerbaar — geen ACTIVE ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatie-voorstellen op ad-niveau. Wel een handvol strategische beslispunten die Robin kan oppakken voordat de volgende run zinvol is:

**1. SYBB campagne reactiveren of definitief afsluiten**
- Huidige situatie: 2 SYBB campagnes staan PAUSED ("2026: SYBB" en "2026: SYBB - Kopie"). Beide bevatten historische learning data die hergebruikt kan worden.
- Beslispunt: campagne weer ACTIVE zetten (en dan rolt /ads-auto-optimize vanaf morgen weer normaal), of de PAUSED campagnes archiveren en met een schone campagne starten.
- Verwachte impact: zonder live campagne is /ads-auto-optimize een no-op.

**2. Token uitbreiden voor act_607231713057715**
- Pipeboard token heeft momenteel alleen permissies voor act_1489853856181844 en act_567892422940728.
- Als act_607231713057715 nog relevante data bevat, regenereer dan een token met access tot dat account.
- Anders verwijder de referentie naar dat account uit `.claude/commands/ads-auto-optimize.md` om foutmeldingen in toekomstige runs te voorkomen.

**3. Kalibreren van 70-20-10 drempels op link metrics**
- TODO in de command staat nog open: 70-20-10 thresholds zijn gekalibreerd op all-clicks, niet op link metrics.
- Aanbevolen: bij re-launch van SYBB de eerste 7-10 dagen alleen rapporteren (geen budget-shifts) tot er voldoende link-metric data is om nieuwe drempels te zetten.

---

## Conclusie

Tot er weer een campagne live gaat, levert /ads-auto-optimize niets op. De minimale data-vereiste (24 uur live, ≥1.000 impressies of ≥500 link clicks per ad) wordt niet gehaald omdat er nul delivery is.

Volgende run heeft alleen zin nadat een campagne minstens 24 uur ACTIVE is geweest.
