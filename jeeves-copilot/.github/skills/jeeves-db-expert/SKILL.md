---
name: jeeves-db-expert
description: 'Anvand for Jeeves ERP-databasfragor om tabeller, kolumner, datatyper, relationer, joins, index, SQL och programkopplingar. Exempel: vilka kolumner har ac, hur joinar jag tabeller, vad betyder faltet ArtNr?'
user-invocable: false
---

# Jeeves Database Expert

Hjalp utvecklare och dataanalytiker med kallbackade databasbeskrivningar.
Folj [projektinstruktionerna](../../copilot-instructions.md).

## Kallor
- [Tabeller](../../../Tables_SE.md): kolumner, ledtext, Jeeves-typ, SQL-typ, langd, decimaler och huvudtabellkopplingar.
- [Termer](../../../Terms_SE.md): betydelse, tillatna varden och tabellanvandning.
- [Program](../../../Programs_SE.md): beskrivningar, huvudtabeller, noder och rapporter.
- [Dokumentationsomraden](../../../DocAreas_SE.md): funktioner och arbetsfloden.

## Arbetsflode
1. Klassificera fragan som tabell, kolumn, relation, SQL eller programkoppling.
2. Sok efter `# tbd_<kod>.htm`, `# ted_<kod>.htm` eller `# pgm_<kod>.htm` i relevant kalla. Las fram till nasta objektrubrik.
3. For tabeller: hamta beskrivning och efterfragade kolumner. For kolumner: hamta termdefinition och verifiera datatyp i den aktuella tabellen.
4. For relationer: jamfor datanamn, termreferenser och programkopplingar. Markera kandidatrelationer som antaganden; kolumnnamn ensamt bevisar inte relation eller kardinalitet.
5. For SQL: folj [SQL-skillen](../jeeves-sql-builder/SKILL.md). Kontrollera `ForetagKod` i varje relevant tabell.
6. For index och nycklar: redovisa endast dokumenterade uppgifter. Om DDL eller indexmetadata saknas, ange det.
7. Vid utebliven exakt traff: ge upp till tre faktiskt hittade alternativ. Fraga vilket som avses om valet paverkar svaret.

## Svarsformat
- Tabell: namn, kod, syfte och efterfragade kolumner i en tabell med Datanamn, Ledtext, SQL-typ och beskrivning.
- Kolumn: Datanamn, ledtext, Jeeves-typ, SQL-typ, definition och tabeller dar faltet forekommer.
- Relation: dokumenterad koppling eller kandidatrelation, underlag och saknade nyckeluppgifter.
- Programkopplingar: exakta programkoder och namn. Anta inte las-/skrivbeteende fran en huvudtabellkoppling.
- Avsluta med "Hittad i" och eventuella punkter markerade "oklart i kallet".