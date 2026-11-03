---
description: Oversatt naturligt sprak till SQL mot Jeeves-databasen. Skriv vad du vill hamta pa svenska sa bygger jag fragan.
argument-hint: "beskriv pa svenska, t.ex. 'skapa en vy som visar alla kundorder med belopp' eller 'hamta fakturor fran 2024'"
---

Anvand skillen i .claude/skills/jeeves-sql-builder.md.

Anvandarens input: $ARGUMENTS

Uppgift:
1. Forsta vad anvandaren vill hamta/skapa baserat pa naturligt sprak.
2. Mappa svenska ord till ratt Jeeves-tabeller och kolumner via Tables_SE.md.
3. Bygg korrekt SQL (SELECT, VIEW, aggregering) med ratt datatyper och kolumnnamn.
4. Forklara pa svenska vilka tabeller och kolumner som anvands och varfor.
5. Inkludera WITH (NOLOCK), meningsfulla alias, och ForetagKod-filter.
6. Om nagon del ar oklar: stall motfraga eller skriv "Oklart i kallorna".
7. Svara alltid pa svenska.
