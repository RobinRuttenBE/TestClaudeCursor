Klaar. Hier is de uitkomst van `/ads-auto-optimize` voor 18 May 2026:

## Geen actieve campagnes — geen optimalisatie mogelijk

De flow kon niet draaien zoals bedoeld, want **er staat geen enkele Meta Ads campagne live**:

| Account | Resultaat |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED** |
| `act_1489853856181844` | Geen campagnes |
| `act_607231713057715` | Token heeft geen toegang |

De hoofdcampagne **`2026: SYBB`** (dagbudget €100,00, ID 120239435987290239) staat sinds 2026-04-19 op pauze. Alle Nozzle Up campagnes zijn al sinds september 2025 inactief.

**Niveau 1 (automatisch):** geen ads gepauzeerd, er zijn geen actieve ads om tegen de kill-regels te toetsen.
**Niveau 2 (voorstellen):** geen, zonder live data is elke classificatie of budget-aanbeveling speculatief.

PostHog is niet bevraagd: zonder ad-traffic is er niets te cross-referencen. Geen Google MCPs gebruikt, geen Google Sheet beschreven, conform de strikte regel.

Rapport opgeslagen in `Output/Reports/Daily/2026-05-18_auto_optimize.md` en gecommit + gepusht naar `main`.

## Beslissing nodig

Wil je dat ik de campagne **`2026: SYBB`** weer activeer? Dat is een Niveau 2 actie, dus ik voer het niet zonder jouw expliciete akkoord uit. Pas met minstens één actieve campagne heeft deze dagelijkse auto-optimalisatie zin.
