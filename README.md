# Sempertex Europe — Marketing Automation Project

## Wat is dit?
Dit is de kennisbank en projectstructuur voor het Claude Code marketing automation systeem van Sempertex Europe. Claude Code leest deze bestanden om taken uit te voeren met volledige context over het merk, de producten, de klanten en de marketingstrategie.

## Hoe werkt het?
- **CLAUDE.md** is het hoofdbestand dat Claude Code bij elke sessie leest. Het bevat een kort overzicht en verwijzingen naar alle submappen.
- **Kennisbestanden** (.md) bevatten de inhoudelijke kennis per onderwerp.
- **Claude Code leest niet alles tegelijk** — het leest per taak alleen de relevante bestanden. CLAUDE.md vertelt welk bestand bij welke taak hoort.

## Mappenstructuur

```
sempertex-marketing/
├── CLAUDE.md                          ← Hoofdindex (max 200 regels)
├── README.md                          ← Dit bestand
│
├── kennis/                            ← Bedrijfskennis
│   ├── brand/                         ← Merkidentiteit, kleuren, fonts, tone of voice
│   ├── products/                      ← Productlijnen en specificaties
│   ├── klantprofielen/                ← Doelgroepen en segmenten
│   ├── campagne-historie/             ← Voorgaande campagnes en resultaten
│   └── concurrenten/                  ← Concurrentieanalyse (nooit publiek delen)
│
├── bronnen/                           ← Externe frameworks en referentiemateriaal
│   ├── hormozi/                       ← Alex Hormozi playbooks en video samenvattingen
│   ├── sempertex/                     ← Interne Sempertex documenten (nog te vullen)
│   └── balloon-industry/              ← Industrie-informatie (nog te vullen)
│
├── content/                           ← Content productie
│   ├── scripts/                       ← Filming plannen en scriptvoorbeelden
│   ├── transcripts/                   ← Video transcripts (Descript exports)
│   └── top-content/                   ← Best performing content voor analyse
│
├── assets/                            ← Templates en notities
│   ├── templates/                     ← Remotion/Canva template specificaties
│   └── notities/                      ← Losse ideeën en notities
│
└── .claude/                           ← Claude Code configuratie
    ├── commands/                      ← Slash commands (.md bestanden)
    ├── skills/                        ← Skills per vaardigheid (SKILL.md)
    └── rules/                         ← Gedragsregels
```

## Status

| Map | Status | Bestanden |
|---|---|---|
| kennis/brand/ | ✅ Compleet | 4 bestanden |
| kennis/products/ | ✅ Compleet | 1 bestand |
| kennis/klantprofielen/ | ✅ Compleet | 1 bestand |
| kennis/campagne-historie/ | ✅ Compleet | 1 bestand |
| kennis/concurrenten/ | ✅ Compleet | 1 bestand |
| bronnen/hormozi/ | ✅ 6 bestanden, meer volgen | 6 bestanden |
| bronnen/sempertex/ | ⏳ Nog te vullen | — |
| bronnen/balloon-industry/ | ⏳ Nog te vullen | — |
| content/scripts/ | ✅ 1 referentie | 1 bestand |
| content/transcripts/ | ⏳ Nog te vullen | — |
| content/top-content/ | ⏳ Nog te vullen | — |
| assets/ | ⏳ Nog te vullen | — |
| .claude/ | ⏳ Fase 2-5 | — |

## Eigenaar
Robin — Head of Marketing, Sempertex Europe
