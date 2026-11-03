---
description: Sok och beskriv ett Jeeves-databasobjekt (tabell, kolumn, term) pa svenska. Visa beskrivning och var objektet anvands.
argument-hint: "tabellnamn, kolumnnamn eller fritext, t.ex. ArtNr, kund, FaktDat, tbd_ar"
---

Anvand skillen i .claude/skills/jeeves-describe.md.

Anvandarens input: $ARGUMENTS

Uppgift:
1. Identifiera om input ar en tabell (tbd_*), term/kolumn (ted_*) eller fritext.
2. Sok i Tables_SE.md och/eller Terms_SE.md.
3. Returnera:
   - Beskrivning pa svenska av objektet
   - Vilka tabeller objektet finns i
   - Relaterade program
   - Teknisk info (datatyp, SQL-typ)
4. Om ingen exakt traff: foreslaa 3 narmaste alternativ.
5. Inkludera alltid "Hittad i: <filnamn>".
6. Svara alltid pa svenska.
