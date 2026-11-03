---
description: Gor konsekvensanalys for andring av program, tabell eller term.
argument-hint: "entitet att analysera, t.ex. AcColor, tbd_AcColor eller ted_AcColorType"
---

Anvand skillen i .claude/skills/jeeves-change-impact.md.

Anvandarens input: $ARGUMENTS

Uppgift:
1. Identifiera om input ar program, tabell eller term.
2. Bygg direkt paverkan:
- Program -> huvudtabell(er)
- Tabell -> program
- Term -> tabeller
3. Bygg indirekt paverkan med ett extra hopp nar mojligt.
4. Bedom riskniva (Lag/Medel/Hog) med kort motiv.
5. Skapa testchecklista.
6. Svara pa svenska i strukturen:
- Andring
- Direkt paverkan
- Indirekt paverkan
- Riskniva
- Testchecklista
- Hittad i

Om underlag saknas, skriv "oklart i kallet" och specificera vad som saknas.
