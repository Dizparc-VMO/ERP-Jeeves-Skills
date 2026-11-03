---
description: Jeeves Database Expert — fraga om tabeller, kolumner, relationer, SQL och programkopplingar.
argument-hint: "fraga om databas, t.ex. 'vilka kolumner har tabellen ac?' eller 'skriv SQL for kundorder'"
---

Anvand skillen i .claude/skills/jeeves-db-expert.md.

Anvandarens input: $ARGUMENTS

Uppgift:
1. Analysera fragan och klassificera den (tabell, kolumn, relation, SQL, program).
2. Sok i relevanta filer: Tables_SE.md, Terms_SE.md, Programs_SE.md.
3. For SQL-fragor: identifiera ratt tabeller och kolumner, bygg korrekt SQL med ratta datatyper.
4. For relationer: hitta gemensamma falt mellan tabeller via kolumnnamn och termer.
5. Svara pa svenska med strukturerad output enligt skillens mallar.
6. Inkludera alltid "Hittad i: <filnamn>" for sparbarhet.
7. Om osakerhet: skriv "Oklart i kallorna" och ge 3 narmaste alternativ.
