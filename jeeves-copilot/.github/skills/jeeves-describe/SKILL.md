---
name: jeeves-describe
description: 'Anvand nar anvandaren vill beskriva eller forklara ett Jeeves-databasobjekt, tabell, kolumn, falt eller term pa svenska och se var det anvands. Exempel: beskriv ArtNr, vad betyder FaktDat, vilka tabeller innehaller faltet?'
user-invocable: false
---

# Jeeves Databasbeskrivning

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Tolka input: `tbd_*` eller tabellkod betyder tabell; `ted_*` eller datanamn betyder term/kolumn. Vid fritext, sok i bada kallorna.
2. For tabell: hitta objektrubriken i [Tables_SE.md](../../../Tables_SE.md), las syfte, faltlista och huvudtabellens programkopplingar.
3. For term/kolumn: hitta rubriken i [Terms_SE.md](../../../Terms_SE.md), las definition och hela listan over tabeller dar faltet ingar.
4. Verifiera teknisk information i respektive tabell. Samma term kan forekomma i flera tabeller; ange vilken tabell en datatyp avser.
5. Kontrollera relaterade program i [Programs_SE.md](../../../Programs_SE.md) nar det behovs.
6. Vid flera rimliga matchningar: lista dem och be anvandaren precisera. Vid ingen exakt traff: foresla upp till tre hittade alternativ.

## Svarsformat
- Objektnamn och exakt kod.
- Typ: tabell eller kolumn/term.
- Beskrivning: vad objektet betyder och anvands till.
- Finns i tabeller: samtliga dokumenterade tabellanvandningar for en term.
- Relaterade program: koder och namn.
- Teknisk info: Datanamn, Jeeves-typ, SQL-typ och antal tecken nar dokumenterat.
- Hittad i: kallfil och relevant rubrik/rad.

Visa normalt hogst 15 relevanta kolumner for en tabell och ange om fler finns. Visa alla om anvandaren efterfragar hela schemat. Vid osakerhet: "oklart i kallet" och vad som saknas.