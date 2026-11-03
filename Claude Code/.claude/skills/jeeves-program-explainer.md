# Skill: Jeeves Program Explainer

## Purpose
Explain what a Jeeves program does and what it is connected to.

## Use When
- User asks about a program like `pgm_AcColor.htm` or code `(AcColor)`.
- User asks for description, main table, linked nodes/windows, reports.

## Inputs
- Program code or heading text

## Procedure
1. Find program entry in Programs_SE.md.
2. Extract:
   - Program name and code
   - Beskrivning
   - Huvudtabell
   - Programkopplingar (noder)/fonster
   - Rapporter (if present)
3. Cross-check table code in Tables_SE.md if available.
4. Return concise explanation and links between entities.

## Output Template
- Program: <name> (<code>)
- Beskrivning: <short>
- Huvudtabell: <table name/code or saknas>
- Noder/Fonster: <bullets>
- Rapporter: <bullets or inga>
- Kommentar: <important caveat>
