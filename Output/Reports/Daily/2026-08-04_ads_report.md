Rapport staat in `Output/Reports/Daily/2026-08-04_ads_report.md` en is gecommit en gepusht.

## Meta Ads Rapport, 4 augustus 2026

**Er draait niets.** Nul euro spend in de laatste 30 én 90 dagen. Alle 5 campagnes staan op PAUSED, laatste uitgave was april 2026. Het account ligt ~3,5 maand stil.

Twee dingen vooraf over de data:
- `act_607231713057715` (Robin Rutten) is **niet toegankelijk** met de huidige Pipeboard token. Als daar iets draait, zie ik het niet.
- Stap 6 (Google Sheet) is overgeslagen zoals gevraagd. Geen Google MCP calls gedaan.

### Laatste bekende performance per campagne

| Campagne | Spend | CTR | CPC | CPM | Aankopen | ROAS |
|----------|-------|-----|-----|-----|----------|------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,81x ⚠️ |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,30x |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,37x |
| 2026: SYBB, Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Drie dingen die eruit springen

**1. De ROAS van SYBB klopt niet.** Van de €44.247 conversiewaarde komt €42.773,50 uit 2 aankopen op één ad. Dat is €21.386 per aankoop vanaf een starter landingspagina. Vrijwel zeker een pixel fout (waarde in centen, of verkeerd ordertotaal). Realistische ROAS zonder die twee: **0,59x**.

**2. De ads werkten, de pagina niet.** Winnende ad H13 leverde 4.063 landing page views voor €421,29 (€0,10 per bezoeker, uitstekend) en daaruit kwamen **nul** checkouts. Campagnebreed: SYBB converteert 0,5% van bezoeker naar checkout, Nozzle Up deed 19,0% met dezelfde pixel. Dat is 38x slechter. Target is >5%.

**3. Kopieën presteren structureel slechter.** Elke "Kopie" adset heeft een hogere CPC dan het origineel: €0,67 vs €0,25, €0,63 vs €0,07, €0,40 vs €0,31. Dezelfde creative, 9x duurder, puur door opnieuw te moeten leren.

### Aanbevelingen

1. **Fix eerst de tracking.** Op deze ROAS kun je niet sturen, en Meta optimaliseert zelf ook op ruis.
2. **Fix de landingspagina voor je budget aanzet.** 99,5% van elke euro verdampt na de klik. Nozzle Up bewees dat 19% haalbaar is.
3. **Herstart 70-20-10:** 70% op H13 (9,8% CTR, €0,07 CPC) en H11 (enige hook met aankopen), 20% varianten op H15, 10% nieuw. Statisch is al getest en werkt niet, blijf bij video.
4. **Archiveer de Kopie campagne.** Werk verder in bestaande adsets.
5. **Zoek uit wat er in april misging.** CPC ging van €0,13 (maart) naar €0,56 (april) binnen één maand.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Ik kan die ook uit PostHog halen als je wilt, dat mag binnen de regels van deze run. Zeg het maar.
