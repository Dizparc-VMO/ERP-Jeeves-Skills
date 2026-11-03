# Skill: Jeeves Doc Navigator

## Purpose
Find the right section quickly across the five Jeeves markdown files.

## Use When
- User asks "var finns", "hitta", "visa avsnitt", "vilken fil".
- User asks for quick lookup by code (for example pgm_*, tbd_*, ted_*).

## Inputs
- Search query or code
- Optional file scope

## Procedure
1. Detect likely code type:
   - `pgm_` -> Programs_SE.md
   - `tbd_` -> Tables_SE.md
   - `ted_` -> Terms_SE.md
   - menu/client/macro support -> DocAreas_SE.md
2. Locate nearest matching heading and capture a short excerpt.
3. Return source file and heading.
4. If no match: propose closest 3 alternatives.

## Output Template
- Traff: <heading>
- Kod: <code or N/A>
- Kort svar: <1-3 meningar>
- Hittad i: <filename>
- Narliggande alternativ: <list or none>
