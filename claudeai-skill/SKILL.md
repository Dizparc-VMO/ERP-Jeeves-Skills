---
name: jeeves-erp-db
description: >
  Slå upp och förklara Jeeves ERP-databasobjekt (tabeller, kolumner/termer, program),
  bygg SQL mot Jeeves-databasen, och gör konsekvensanalys av ändringar. Använd när
  användaren frågar om en Jeeves-tabell (tbd_*), en term/kolumn (ted_*), ett program
  (pgm_*), vill veta "vad betyder fältet X", "var används Y", "vilka program påverkas
  om jag ändrar Z", "skriv SQL för...", eller vill navigera Jeeves-dokumentationen.
  Svara alltid på svenska om inte användaren ber om engelska.
---

# Jeeves ERP – databasexpert

Den här skillen ger dig en fullständig, sökbar databas över Jeeves ERP:
**2 650 tabeller, 76 596 kolumner, 12 039 termer, 3 566 program** och
**931 dokumentationskapitel** — byggd från Jeeves officiella exporterade
dokumentation (samma källa som fanns i markdown-form tidigare).

Datat ligger i en bifogad SQLite-fil, `jeeves.db`, i samma mapp som denna
SKILL.md. Använd kod-exekvering (Python, modulen `sqlite3`) för att fråga den
— gissa aldrig fram tabellnamn, kolumnnamn eller programkoder ur minnet.

## Steg 0 – Hitta databasfilen (gör detta först, en gång per konversation)

```python
import os, sqlite3

db_path = None
for root, dirs, files in os.walk('/mnt'):
    if 'jeeves.db' in files:
        db_path = os.path.join(root, 'jeeves.db')
        break
if not db_path:
    # fallback: sök i hela filsystemet fran en rimlig startpunkt
    for root, dirs, files in os.walk('/'):
        if 'jeeves.db' in files:
            db_path = os.path.join(root, 'jeeves.db')
            break

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
```

Om sökningen är långsam eller misslyckas: leta specifikt i skill-paketets
egen mapp (samma katalog som denna SKILL.md-fil ligger i) — `jeeves.db`
ligger alltid direkt bredvid den.

## Schema

```
tables(code PK, name_sv, description)
columns(table_code, prompt_sv, data_name, jeeves_type, chars, decimals, sql_type)
terms(code PK, name_en, description)          -- name_en = termens korta kod-namn, ej alltid engelska
term_tables(term_code, table_code)             -- var en term/kolumn används
programs(code PK, name_sv, description)
program_tables(program_code, table_code)       -- programmets huvudtabell(er)
program_nodes(program_code, node_code, node_name)  -- noder/fönster i programmet
docareas(code, title, body)                    -- dokumentationskapitel (fri text)
```

Index finns på `columns.table_code`, `columns.data_name`, `term_tables.term_code`,
`term_tables.table_code`, `program_tables.program_code`, `program_tables.table_code`,
samt på `name_sv`/`name_en` för tables/terms/programs.

**Ingen FTS5 i denna databas** (togs bort för att hålla filen under Claude.ai:s
storleksgräns). Fritextsökning görs istället med vanlig `LIKE`, case-okänsligt:

```sql
SELECT code, name_sv FROM tables
 WHERE code LIKE '%' || :q || '%' COLLATE NOCASE
    OR name_sv LIKE '%' || :q || '%' COLLATE NOCASE
    OR description LIKE '%' || :q || '%' COLLATE NOCASE;
```
Samma mönster mot `terms` (name_en/description), `programs` (name_sv/description)
och `docareas` (title/body). Radantalen (max ~76 000) gör att en full scan är
snabb nog för en enstaka interaktiv fråga.

**Viktigt om täckning:** ~83 % av `columns.data_name` matchar en `terms.code`
rakt av (`JOIN terms t ON t.code = columns.data_name`) — använd det för att
hämta fältets fulla beskrivning. Vill du fritextsöka på fältbetydelse (inte
bara exakt kod), sök i `terms.description` med `LIKE` — det täcker de allra
flesta kolumner via denna koppling.

## Arbetsflöden

### 1. Beskriv ett objekt (tabell / kolumn / term / program)

Avgör typ från söktermen:

| Mönster | Typ | Fråga |
|---|---|---|
| `tbd_*` eller känd tabellkod (`ac`, `ors`, `kund`) | Tabell | `SELECT * FROM tables WHERE code=?` |
| `ted_*` eller fältnamn (`ArtNr`, `FaktDat`) | Term/kolumn | `SELECT * FROM terms WHERE code=?` |
| `pgm_*` eller programkod (`aco`, `faco`) | Program | `SELECT * FROM programs WHERE code=?` |
| Fritext ("fakturanummer") | Okänd | `LIKE`-sök i `terms`, `tables`, `programs` (se ovan) |

Exakt kod hittas inte → sök `LIKE '%ord%'` i `code`/`name_sv`/`name_en` och
föreslå de 3 närmaste träffarna.

Hämta fullständig bild av en tabell:
```sql
SELECT * FROM tables WHERE code = ?;
SELECT prompt_sv, data_name, jeeves_type, chars, decimals, sql_type
  FROM columns WHERE table_code = ? ORDER BY prompt_sv;
SELECT program_code FROM program_tables WHERE table_code = ?;
```

Hämta fullständig bild av en term/kolumn:
```sql
SELECT * FROM terms WHERE code = ?;
SELECT table_code FROM term_tables WHERE term_code = ?;
```

**Svarsformat:**
```
## <Namn> (<kod>)
**Typ:** Tabell | Kolumn/Term | Program
**Beskrivning:** <text från description>

### Finns i tabeller / Huvudtabell
- <kod> — <name_sv>

### Relaterade program
- <kod> — <name_sv>

### Teknisk info (för kolumner)
| Datanamn | Jeeves-typ | SQL-typ | Tecken |
|---|---|---|---|

**Hittad i:** jeeves.db (tables/terms/programs)
```
Visa max 15 kolumner för en stor tabell, notera att fler finns.
Om inget hittas: skriv **"oklart i källorna"** och lista vad som söktes.

### 2. Bygg SQL mot Jeeves-databasen

Slå upp exakta kolumnnamn (`data_name`) och `sql_type` via `columns`-tabellen
innan du skriver frågan — gissa aldrig kolumnnamn. Presentera den färdiga
SQL-frågan i ett kodblock, och nämn vilka tabeller/kolumner den bygger på.

### 3. Förklara ett program (pgm_*)

```sql
SELECT * FROM programs WHERE code = ?;
SELECT table_code FROM program_tables WHERE program_code = ?;
SELECT node_code, node_name FROM program_nodes WHERE program_code = ?;
```
Svara med: beskrivning, huvudtabell(er), och noder/fönster i programmet.

### 4. Konsekvensanalys (change impact)

Vid fråga om vad som påverkas av en ändring i en tabell, kolumn eller term:

```sql
-- Program som har tabellen som huvudtabell
SELECT program_code FROM program_tables WHERE table_code = ?;
-- Tabeller där en given term/kolumn ingår
SELECT table_code FROM term_tables WHERE term_code = ?;
-- Kombinera: vilka program berörs indirekt via de tabellerna
SELECT DISTINCT pt.program_code
  FROM term_tables tt JOIN program_tables pt ON pt.table_code = tt.table_code
 WHERE tt.term_code = ?;
```
Redovisa kedjan: **term/kolumn → tabeller → program**, så användaren ser
hela påverkanskedjan, inte bara slutresultatet.

### 5. Dokumentnavigering

`LIKE`-sök i `docareas` (title/body) för att hitta rätt kapitel; visa `title`
och en kort utdrag ur `body`, samt `code` som referens.

## Regler (gäller alla arbetsflöden)

- Svara alltid på svenska om inte annat begärs.
- Basera svar enbart på vad SQL-frågorna faktiskt returnerar — hitta inte på
  fält, tabeller eller kopplingar.
- Är kopplingen osäker eller saknas data: skriv **"oklart i källorna"** och
  ange precis vad som saknas.
- Håll svaren korta och strukturerade med tydliga rubriker.
- Ange alltid exakta koder (tbd_/ted_/pgm_-kod) när de finns.
- Avsluta svar med **"Hittad i:"** som pekar på jeeves.db.
