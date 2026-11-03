---
name: jeeves-table-mapper
description: 'Anvand for Jeeves-tabellschema, tbd_-koder, faltlistor, kolumner, Jeeves-datatyper, SQL-datatyper och kopplingar fran tabeller till program och termer.'
user-invocable: false
---

# Jeeves Table Mapper

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Hitta tabellens exakta rubrik i [Tables_SE.md](../../../Tables_SE.md).
2. Las syfte och valt falturval med Ledtext, Datanamn, Jeeves datatyp, antal tecken, antal decimaler och SQL datatyp.
3. Hamta program fran "Tabellen ar huvudtabell i foljande program" och verifiera vid behov i [Programs_SE.md](../../../Programs_SE.md).
4. For efterfragade falt: las motsvarande termdefinition i [Terms_SE.md](../../../Terms_SE.md).
5. Visa normalt upp till tio relevanta falt. Om hela schemat efterfragas, visa samtliga. Kalla dem inte primarnyckelfalt om nyckeln inte ar dokumenterad.
6. Om match saknas: visa upp till tre hittade alternativ. Ange "oklart i kallet" for saknade nycklar, index eller relationer.

## Svarsformat
- Tabell: namn och kod.
- Syfte: 1-2 meningar.
- Falt: tabell med exakt Datanamn, Ledtext, Jeeves-typ, SQL-typ, langd och decimaler.
- Relaterade program: kod och namn.
- Relaterade termer: definitioner for efterfragade falt.
- Hittad i: kallfil och radnummer nar mojligt.