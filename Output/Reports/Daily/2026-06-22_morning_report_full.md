# Morning Report — 2026-06-22

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Connection closed mid-response. The response above may be incomplete.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-06-21_sybb_report.md` en is gecommit + gepusht.

## Wat het rapport laat zien

**De kern: er was gisteren geen SYBB activiteit.**

- **Meta Ads (`2026: SYBB`, ID `120239435987290239`):** campagne staat op **PAUSED**. Nul impressies, clicks en spend op 21 juni, en hetzelfde voor het hele 7daagse venster (15 t/m 21 juni). Laatste actieve maand was april 2026, laatst aangepast 19 april.
- **PostHog:** de PostHog MCP was in deze sessie **niet verbonden**. Ik kon dus geen landing page data (bounce, scroll depth, CTA clicks, session recordings) ophalen. Conform je strikte regel heb ik géén Google/GA4 bron als vervanging gebruikt, alleen Meta Ads MCP en (poging tot) PostHog MCP.

Omdat beide databronnen leeg/onbeschikbaar waren voor gisteren, heb ik de volledige skill-structuur aangehouden maar eerlijk ingevuld met "geen data / n.v.t." waar dat klopt, plus een korte **historische referentie** (jan/mrt/apr 2026) ter context.

## Top 3 acties uit het rapport
1. 🟡 Beslis over de campagnestatus, bewust gepauzeerd of weer activeren.
2. 🟡 Herstel de PostHog MCP koppeling zodat de landing page kant weer gevuld kan worden.
3. 🟢 Bij relaunch: verifieer UTM tagging en verse creatives vooraf.

Twee dingen die je waarschijnlijk wil weten: wil je dat ik de campagne weer activeer (dat is 🟡, vergt jouw goedkeuring), en is de PostHog MCP bewust uit of moet die opnieuw verbonden worden? Zodra PostHog terug is kan ik een volwaardig rapport met funnel en cross-referencing draaien.

---

Klaar. Rapport opgeslagen, gecommit en gepusht.

## Auto-Optimize Rapport — 22 juni 2026

**Conclusie: geen actieve ads om te optimaliseren.** Alle campagnes op beide toegankelijke accounts staan op PAUSED, geen delivery in de laatste 3 dagen (0 impressions, €0,00 spend).

### ⚡ Automatische acties
**0 ads gepauzeerd** — er zijn geen actieve ads. Geen kill-regels getriggerd (kan ook niet bij 0 delivery).

### Wat ik heb gecontroleerd
- **`act_567892422940728`** (primair): 5 campagnes, allemaal PAUSED — waaronder **2026: SYBB** (€100/dag budget, gepauzeerd sinds 19 april). Insights last_3d voor SYBB: leeg.
- **`act_607231713057715`**: token heeft geen toegang. Meta meldt toegestane accounts: `act_1489853856181844` + `act_567892422940728`.
- **`act_1489853856181844`**: 0 actieve campagnes.

### 💡 Enig aandachtspunt
De hoofdcampagne **2026: SYBB** staat al sinds april op PAUSED. Zolang dat zo blijft leveren zowel `/ads-report` als `/ads-auto-optimize` lege rapporten op. **Wil je SYBB weer activeren, of blijft die bewust gepauzeerd?** Pas met live delivery heeft auto-optimalisatie weer nut.

Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven — alleen Meta Ads MCP en lokale markdown, zoals gevraagd.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
