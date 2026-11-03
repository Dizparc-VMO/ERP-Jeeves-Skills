# Jeeves ERP – Agent Skill för Claude.ai

Detta paket gör Jeeves-dokumentationen sökbar i **Claude.ai** (webb/desktop),
utanför Claude Code/CMD. Datat i `Tables_SE.md`, `Terms_SE.md`, `Programs_SE.md`
och `DocAreas_SE.md` (~38 MB rå markdown) är ombyggt till en enda SQLite-databas
(`jeeves.db`, ~20 MB uppackad / ~5,8 MB zippad) som Claude frågar via
kod-exekvering istället för att textsöka i markdown.

> Första versionen (33 MB) avvisades av Claude.ai:s 30 MB-gräns för uppackad
> storlek. FTS5-fritextindexen togs bort (sökning görs nu med `LIKE` istället,
> fullt tillräckligt snabbt på dessa radantal) och två databuggar fixades
> samtidigt: markdown-escape (`\_`) som läckte in i kodfält, och
> skiftläges-skillnader mellan källfilerna (`ak` vs `Ak`) som gjorde att vissa
> program↔tabell-kopplingar missades. Databasen har nu ~20 MB marginal kvar
> till gränsen.

## Innehåll

- `SKILL.md` – instruktioner till Claude (schema, arbetsflöden, svarsformat)
- `jeeves.db` – SQLite-databas: 2 650 tabeller, 76 596 kolumner, 12 039 termer,
  3 566 program, 931 dokumentationskapitel + fritextsökning (FTS5)
- `build_db.py` – parsern som byggde `jeeves.db` från markdown-filerna
- `jeeves-erp-db.zip` – **det här är filen du laddar upp**

## Ladda upp i Claude.ai

1. Kräver Claude Pro, Max, Team eller Enterprise (Agent Skills-stöd).
2. I Claude.ai: Inställningar → Capabilities/Skills → **Ladda upp skill**.
3. Välj `jeeves-erp-db.zip`.
4. Testa i en ny chatt, t.ex. "Beskriv tabellen tbd_ac" eller "Vilka program
   påverkas om jag ändrar fältet AcDrawn?".

Om uppladdningen nekas pga filstorlek: hör av dig, då delar jag databasen i
en mindre kärna (tables/terms/programs) + en separat docareas-fil, eller
byter FTS mot ett lättare index.

## Bygga om databasen (t.ex. efter ny Jeeves-export)

```bash
python build_db.py --src "E:\Jeeves Hjälp\AI Skills" --out jeeves.db
```

`--src` ska peka på mappen med de fyra `*_SE.md`-filerna. Skriv sedan om
`jeeves-erp-db.zip` (SKILL.md + nya jeeves.db) och ladda upp på nytt — samma
skill-namn skriver över den gamla versionen i Claude.ai.

## Om ChatGPT

ChatGPT har inget filsystem att köra SQL mot inne i en Custom GPT, så samma
paket går inte att återanvända rakt av där. Två vägar om det blir aktuellt:

- **Custom GPT + Knowledge**: ladda upp `Tables_SE.md` m.fl. som knowledge-filer.
  Fungerar för ungefärliga frågor, men sökningen är vektorbaserad (inte exakt
  kod-uppslag) och opålitlig på 38 MB text.
- **Custom GPT + Action (API)**: hosta `jeeves.db` bakom ett litet eget API
  (t.ex. en Flask-endpoint) som GPT:n anropar. Ger samma precision som i
  Claude, men kräver en server att drifta. Kan byggas på samma `jeeves.db`.
