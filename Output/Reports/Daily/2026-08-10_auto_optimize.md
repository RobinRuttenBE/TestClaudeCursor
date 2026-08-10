Het command kon niet draaien. De kern ervan hangt volledig op de Meta Ads MCP, en die is dicht.

**Wat er aan de hand is**

De Pipeboard connector is in deze sessie niet geautoriseerd. Vierde dag op rij, hetzelfde als in het ads rapport van vanochtend. Zonder ad-level insights zijn er geen impressions, link clicks of spend, dus:

- De kill-regels zijn niet geëvalueerd, niet "gehaald". Er zijn nul ads gepauzeerd omdat er niets te meten viel.
- 70-20-10 classificatie en alle budget-, variatie- en audience-voorstellen vervallen, die zijn puur afgeleid van performance data.

Autoriseren kan alleen jij, via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Deze sessie is non-interactief.

**Wat PostHog wel liet zien**

Nul betaald verkeer over de laatste zeven dagen. Geen enkele `meta` bron, geen enkele `cpc` medium in de UTM verdeling. De enige getagde bronnen zijn e-mail (mailjet, klaviyo), organic (youtube, pinterest) en één partner referral. Laatste betaalde klik blijft 1 juli.

Dat maakt de blokkade urgenter dan een gemist rapport. Er zijn twee scenario's en je kunt ze nu niet uit elkaar houden: óf de campagnes staan uit, en dan valt er niets te optimaliseren, óf ze draaien wel en de tracking is stuk, en dan verbrand je budget dat je niet ziet. Twee minuten in Meta Ads Manager beantwoordt dat, ook zonder Pipeboard.

Let ook op de 32.973 pageviews zonder bron over 5.908 personen. Gecombineerd met de crawler-bevinding van vanochtend is dat cijfer vervuild, dus zet bot filtering aan voordat je die cross-references weer gaat gebruiken.

Alleen de Meta Ads MCP en PostHog MCP zijn benaderd, geen Google MCPs, niets naar de tracker Sheet. Rapport staat in `Output/Reports/Daily/2026-08-10_auto_optimize.md`, gecommit en gepusht.
