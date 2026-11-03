# Claude Project Instructions

This workspace contains exported Jeeves documentation in Swedish.

## Source Files
- DocAreas_SE.md
- Jeeves_SE.md
- Programs_SE.md
- Tables_SE.md
- Terms_SE.md

## Working Style
- Answer in Swedish unless the user asks for English.
- Base answers only on content found in workspace files.
- If a mapping is uncertain, say "oklart i kallet" and list what is missing.
- Prefer short, structured output with clear headings.

## Skill Routing
- Use `.claude/skills/jeeves-describe.md` for searching and describing database objects (tables, columns, terms) — returns Swedish description and where the object is used.
- Use `.claude/skills/jeeves-db-expert.md` for database questions: tables, columns, relations, SQL, indexes, datatyper, programkopplingar. This is the primary skill for developers and data analysts.
- Use `.claude/skills/jeeves-doc-navigator.md` for lookup and navigation tasks.
- Use `.claude/skills/jeeves-program-explainer.md` when a user asks about a specific program (pgm_*).
- Use `.claude/skills/jeeves-table-mapper.md` for table schema and program-table relationships.
- Use `.claude/skills/jeeves-term-linker.md` for term definition and usage mapping.
- Use `.claude/skills/jeeves-change-impact.md` when asked about impact or dependencies.

## Slash Commands
- `/desc <query>` -> sok och beskriv databasobjekt (tabell, kolumn, term) pa svenska
- `/db <query>` -> database expert: tabeller, kolumner, relationer, SQL, programkopplingar
- `/sql <query>` -> oversatt naturligt sprak till SQL mot Jeeves-databasen
- `/program <query>` -> program explanation flow
- `/table <query>` -> table mapping flow
- `/term <query>` -> term definition and usage flow
- `/impact <query>` -> change impact analysis flow
- `/find <query>` -> general lookup across all documentation files

Command files are located in `.claude/commands/`.

## Output Defaults
- Include exact program/table/term codes when available.
- When possible, include "Hittad i" with source filename.
