# Skill: Jeeves Term Linker

## Purpose
Explain a term and show where it is used.

## Use When
- User asks "vad betyder termen" or gives `ted_*` code.
- User asks where a field is used.

## Inputs
- Term code or term name

## Procedure
1. Find term block in Terms_SE.md.
2. Extract definition text.
3. Extract "Faltet ingar i foljande tabeller" list.
4. For each listed table, optionally verify in Tables_SE.md.
5. Return practical interpretation plus usage map.

## Output Template
- Term: <name> (<code>)
- Definition: <short>
- Ingaar i tabeller: <bullets>
- Praktisk tolkning: <short>
- Kallor: Terms_SE.md (+ optional Tables_SE.md)
