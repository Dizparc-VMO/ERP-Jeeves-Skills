---
description: Snabb generell lookup i Jeeves-dokumentationen over alla huvudfiler.
argument-hint: "sokfras eller kod, t.ex. AccelDepr, tbd_AcColor, menu code Delete"
---

Primar skill: .claude/skills/jeeves-doc-navigator.md

Anvandarens input: $ARGUMENTS

Uppgift:
1. Sok i foljande filer: Jeeves_SE.md, DocAreas_SE.md, Programs_SE.md, Tables_SE.md, Terms_SE.md.
2. Prioritera exakta kodtraffar (pgm_*, tbd_*, ted_*), sedan namntraffar.
3. Returnera upp till 5 bast matchande traffar.
4. For varje traff, visa:
- Traff
- Kod (om finns)
- Kort svar (1-2 meningar)
- Hittad i (filnamn)
5. Om ingen exakt traff: visa 5 narliggande forslag och foresla battre sokfras.

Svara alltid pa svenska.
