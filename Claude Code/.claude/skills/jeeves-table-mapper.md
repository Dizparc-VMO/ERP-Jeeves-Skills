# Skill: Jeeves Table Mapper

## Purpose
Map table metadata and connect tables to programs and terms.

## Use When
- User asks for fields/columns in a table.
- User asks which program uses a table.
- User asks for datatypes and SQL mapping.

## Inputs
- Table code/name, optional field filter

## Procedure
1. Locate table in Tables_SE.md.
2. Extract selected fields with:
   - Ledtext
   - Datanamn
   - Jeeves datatyp
   - SQL datatyp
3. Find related programs from "Tabellen ar huvudtabell i foljande program".
4. For a requested field, resolve term in Terms_SE.md if available.

## Output Template
- Tabell: <name> (<code>)
- Syfte: <1-2 meningar>
- Nyckelfalt: <up to 10 rows>
- Relaterade program: <bullets>
- Relaterade termer: <bullets>
