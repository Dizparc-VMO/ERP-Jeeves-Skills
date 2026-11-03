# Skill: Jeeves Change Impact Analyzer

## Purpose
Estimate impact when changing a program, table, or term.

## Use When
- User asks "vad paverkas om vi andrar X".
- User asks for dependency or regression checklist.

## Inputs
- One entity: program code, table code, or term code

## Procedure
1. Identify entity type and primary source file.
2. Build direct links:
   - Program -> main table(s)
   - Table -> program(s)
   - Term -> table(s)
3. Build indirect links by one extra hop where possible.
4. Produce risk list:
   - Data model risk
   - Report/print risk
   - Workflow/permissions risk
   - Client compatibility risk (if DocAreas applies)
5. Return a test checklist.

## Output Template
- Andring: <entity>
- Direkt paverkan: <bullets>
- Indirekt paverkan: <bullets>
- Riskniva: Lag/Medel/Hog + motiv
- Testchecklista: <numbered list>
