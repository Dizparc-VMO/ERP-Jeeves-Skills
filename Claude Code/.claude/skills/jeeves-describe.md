---
name: jeeves-describe
description: >
  Sok och beskriv Jeeves-databasobjekt pa svenska. Anvand nar anvandaren vill veta vad en tabell,
  kolumn, falt eller term betyder, vad den gor och var den anvands. Trigga pa fragor som
  "beskriv kolumnen X", "vad ar Y?", "forklara tabellen Z", "vad betyder faltet W?",
  "var anvands X?", "sok efter...", "hitta information om...", "vilka tabeller innehaller...".
  Aven nar anvandaren bara skriver ett databasnamn eller en kod och forvantar sig en forklaring.
---

# Jeeves Databasbeskrivning

Sok efter och beskriv Jeeves-databasobjekt (tabeller, kolumner, termer) pa svenska.
Returnera alltid en tydlig beskrivning och var objektet anvands.

## Arbetsflode

### 1. Identifiera vad anvandaren soker

Tolka sokordet och avgora typ:

| Sokord-monster | Typ | Primar kalla |
|----------------|-----|--------------|
| `tbd_*` eller tabellnamn (t.ex. `ar`, `ors`, `kund`) | Tabell | Tables_SE.md |
| `ted_*` eller faltnamn (t.ex. `ArtNr`, `FaktDat`) | Term/Kolumn | Terms_SE.md |
| Fritext (t.ex. "fakturanummer", "artikelbeskrivning") | Okand | Sok i bade Terms_SE.md och Tables_SE.md |

### 2. Sok i kallorna

**For tabeller** — sok i Tables_SE.md:
1. Hitta tabellrubriken (`# tbd_<namn>.htm`)
2. Las beskrivningstexten direkt under rubriken
3. Hamta kolumnlistan (Ledtext, Datanamn, SQL datatyp)
4. Hamta "Tabellen ar huvudtabell i foljande program"

**For kolumner/termer** — sok i Terms_SE.md:
1. Hitta termrubriken (`# ted_<namn>.htm`)
2. Las definitionstexten
3. Hamta "Faltet ingar i foljande tabeller" — detta visar var objektet anvands

**For fritext** — sok i bada filerna:
1. Sok pa Ledtext (prompt) i Tables_SE.md kolumntabeller
2. Sok pa termnamn i Terms_SE.md
3. Returnera basta traffen

### 3. Svarsformat

Svara ALLTID med denna struktur:

```
## <Objektnamn> (<kod>)

**Typ:** Tabell | Kolumn/Term
**Beskrivning:** <Forklaring pa svenska — vad objektet ar och vad det anvands till>

### Finns i tabeller
- <tabellnamn1> (<tabellkod1>) — <kort beskrivning av tabellen>
- <tabellnamn2> (<tabellkod2>) — <kort beskrivning av tabellen>

### Relaterade program
- <programkod> — <programnamn>

### Teknisk info
| Egenskap | Varde |
|----------|-------|
| Datanamn | <namn> |
| Jeeves-typ | <typ> |
| SQL-typ | <typ> |
| Antal tecken | <N> |

**Hittad i:** <filnamn>
```

## Regler

- Svara ALLTID pa svenska
- Om sokordet inte hittas exakt: foreslaa de 3 narmaste matchningarna
- Om flera traffar: lista alla och lat anvandaren valja
- Inkludera alltid "Hittad i:" med kallfilens namn
- For tabeller: visa max 15 viktigaste kolumner (inte alla), namnda att det finns fler
- For kolumner: visa alltid ALLA tabeller dar den ingar
- Om oklart: skriv "Oklart i kallorna" och forklara vad som saknas
