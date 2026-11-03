---
name: jeeves-sql-builder
description: >
  Oversatt naturligt sprak (svenska) till SQL-fragor och vyer mot Jeeves-databasen. Anvand nar
  anvandaren beskriver vad de vill hamta, skapa eller se i databasen med vanliga ord — t.ex.
  "hamta alla fakturor fran januari", "skapa en vy som visar kundorder med belopp",
  "vilka artiklar har lagersaldo under 10", "visa budgetposter per konto".
  Trigga aven pa "skriv SQL", "skapa en vy", "SELECT", "rapport fran databasen",
  "jag behover en fraga som...", "kan du gora en query...", eller nar anvandaren
  beskriver affarsdata de vill se utan att namna specifika tabeller.
---

# Jeeves SQL Builder

Oversatt naturliga sprakfragor pa svenska till korrekta SQL-fragor och vyer mot Jeeves ERP-databasen.

## Arbetsflode

### Steg 1: Forsta avsikten

Las anvandarens fraga och identifiera:

1. **Vad vill de se?** (vilken data — fakturor, artiklar, kunder, ordrar, budget, lager...)
2. **Vilka villkor?** (tidsperiod, status, belopp, foretag...)
3. **Vilken typ av resultat?** (SELECT-fraga, VIEW, sammanstallning/aggregering)

### Steg 2: Mappa till Jeeves-tabeller

Anvand denna ordlista for att hitta ratt tabeller:

| Anvandaren sager | Jeeves-tabell(er) | Tabellkod |
|---|---|---|
| faktura, fakturor | Fakturahuvud / Fakturarader | fh / fr |
| kund, kunder | Kunder | kund |
| artikel, artiklar, produkt | Artiklar | ar |
| order, kundorder | Orderhuvud / Orderrader | oh / ors |
| inkopsorder, bestallning | Inkopsorderhuvud / rader | bh / br |
| lager, lagersaldo | Artiklar per lagerstalle | ars |
| leverantor | Leverantorer | lev |
| projekt, uppdrag | Projekt | prj |
| budget | Budgetposter | (sok i Tables_SE.md) |
| konto, kontoplan | Konton | (sok i Tables_SE.md) |
| verifikat, bokforing | Verifikat / transaktioner | (sok i Tables_SE.md) |
| personal, anstallda | Personal | (sok i Tables_SE.md) |
| a conto | A conto, uppdrag | ac |
| struktur, stycklista | Struktur | sr |
| operation, tillverkning | Operationer | op |
| batch, parti | Batch | bat |
| statistik | Artikelstatistik | sars |

**Om tabellen inte finns i listan:** Sok i Tables_SE.md efter relevanta nyckelord.

### Steg 3: Hitta ratt kolumner

1. Sok i Tables_SE.md for att hitta exakta kolumnnamn (Datanamn) och SQL-datatyper
2. Om kolumnbeskrivning behovs — kolla Terms_SE.md for termens definition
3. Anvand alltid **Datanamn** (inte Ledtext) i SQL:en

### Steg 4: Bygg SQL

Folj dessa regler:

**Grundregler:**
- Tabellnamn utan prefix: `tbd_ar.htm` → tabellen heter `ar`
- Kolumnnamn = Datanamn fran tabellspecifikationen
- Boolean-falt: `= 'Y'` eller `= 'N'` (INTE 1/0)
- Inkludera alltid `ForetagKod` i WHERE om relevant (multi-company)
- Datumaformat: `datetime` — anvand `CONVERT` eller `CAST` vid behov

**For SELECT:**
```sql
SELECT <kolumner med tydliga alias>
FROM <tabell> WITH (NOLOCK)
WHERE <villkor>
ORDER BY <sortering>
```

**For VIEW:**
```sql
CREATE VIEW dbo.v_<beskrivande_namn>
AS
SELECT <kolumner med tydliga alias>
FROM <tabell> WITH (NOLOCK)
LEFT JOIN <relaterad tabell> WITH (NOLOCK) ON <koppling>
WHERE <villkor>
```

**For aggregering:**
```sql
SELECT <gruppering>, 
       SUM(<belopp>) AS <alias>,
       COUNT(*) AS Antal
FROM <tabell> WITH (NOLOCK)
WHERE <villkor>
GROUP BY <gruppering>
```

### Steg 5: Svarsformat

Svara ALLTID med:

```
## SQL: <kort beskrivning av vad fragan gor>

### Forklaring
<1-3 meningar om vad fragan hamtar och varfor tabellerna valdes>

### Anvanda tabeller
| Tabell | Beskrivning | Roll i fragan |
|--------|-------------|---------------|
| <kod>  | <namn>      | <varfor>      |

### SQL

```sql
<den fardiga SQL-koden>
```

### Kolumnforklaringar
| Kolumn | Alias | Betydelse |
|--------|-------|-----------|
| <Datanamn> | <alias> | <kort forklaring> |

### OBS
- <eventuella forutsattningar, t.ex. "filtrera pa ForetagKod for ratt foretag">
- <tips om prestanda eller index>

**Hittad i:** <vilka filer som anvandes>
```

## Exempel pa tolkningar

| Anvandaren skriver | Tolkning |
|---|---|
| "hamta alla fakturor fran januari" | SELECT fran fh/fr WHERE FaktDat BETWEEN jan-start och jan-slut |
| "vilka kunder har obetalda fakturor" | JOIN kund + fh WHERE betalstatus = obetald |
| "skapa en vy med artiklar och lagersaldo" | CREATE VIEW med ar JOIN ars |
| "visa budgetposter per konto" | Hitta budgettabell, GROUP BY konto |
| "hur manga ordrar per manad i ar" | COUNT fran oh GROUP BY manad WHERE ar = YEAR(GETDATE()) |

## Regler

- Svara ALLTID pa svenska (kommentarer, alias, forklaringar)
- Anvand WITH (NOLOCK) pa alla tabeller (Jeeves-standard for lasning)
- Ge meningsfulla svenska alias: `ArtBeskr AS Artikelnamn`
- Om tabellen ar osaker: skriv "Oklart i kallorna" och foreslaa alternativ
- Om fragan ar tvetydig: stall en motfraga innan du skriver SQL
- Inkludera alltid "Hittad i:" med kallfiler
