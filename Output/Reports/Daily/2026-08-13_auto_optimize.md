## Auto-Optimize 13 augustus 2026: niet uitgevoerd

**Meta Ads MCP (Pipeboard) is niet geautoriseerd.** Zonder impressions, `actions.link_click` en spend hebben de kill-regels geen invoer, en `update_ad` is niet beschikbaar. Dus zelfs een terechte pauze had ik niet kunnen doorvoeren.

**0 ads geëvalueerd, 0 gepauzeerd.** Belangrijk: dat is niet hetzelfde als "alles presteert goed". Er is geen enkele ad beoordeeld.

### Wat PostHog wél laat zien (laatste 3 dagen, 1.299 sessies)

Geen betaald verkeer, punt. Nul Paid Social, nul Paid Search, nul `meta / cpc / sybb` sessies. De 5 Facebook-verwijzingen zijn organisch. Consistent met de laatste betaalde klik op 14 juli.

Kanalen: Direct 59,0%, Referral 19,5%, Organic Search 17,5%, AI 2,7%, Email 0,7%, Organic Social 0,7%.

Het self-referral probleem uit het ochtendrapport staat er nog: `www.sempertexeurope.com` levert 236 sessies (18,2%). Daarnaast zie ik Mollie, Odoo en het shipping-portal als verwijzer terugkomen.

### Wat blind blijft

Of er nog ACTIVE ads in Meta staan die budget verbranden zonder clicks te leveren, kan ik niet zien. Dat is precies het scenario waarvoor dit command bestaat.

### Voorstellen

1. **Autoriseer Pipeboard** (claude.ai connector instellingen of `/mcp`). Ik kan dit niet zelf.
2. **Referral exclusions in PostHog**: `sempertexeurope.com`, `mollie.com`, de Odoo en shipping-portal domeinen. Doe je dit niet vóór de herstart, dan reken je Meta af op verzonnen cijfers.
3. **Conversie events op de SYBB pagina** vóór herstart, anders blijft ROAS leeg en werkt de 70% Core regel ook ná autorisatie niet.
4. **70-20-10 drempels herzien voor link metrics.** Die TODO staat nog open in het command, ze zijn nog gekalibreerd op all-clicks.

Punt 2, 3 en 4 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-13_auto_optimize.md`, gecommit en gepusht. Geen Google MCPs aangeroepen, niet naar de Sheet tracker geschreven.
