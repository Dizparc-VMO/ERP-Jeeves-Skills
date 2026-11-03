# Jeeves ERP - Copilot

## Kallor och sprak
- Svara pa svenska om anvandaren inte ber om ett annat sprak.
- Basera Jeeves-specifika svar endast pa projektets dokumentation: [Tables_SE.md](../Tables_SE.md), [Terms_SE.md](../Terms_SE.md), [Programs_SE.md](../Programs_SE.md), [DocAreas_SE.md](../DocAreas_SE.md) och [Jeeves_SE.md](../Jeeves_SE.md).
- Sok efter exakt kod eller rubrik och las det relevanta avsnittet. Las inte hela de stora dokumentationsfilerna som standard.
- Inkludera exakta program-, tabell- och termkoder samt "Hittad i" med klickbar kallfil och radnummer nar mojligt.
- Om information saknas eller en mappning ar osaker: skriv "oklart i kallet" och lista vad som saknas. Skilj dokumenterade fakta fran forslag och antaganden.
- Kalltexten kan sakna svenska tecken. Sok aven pa exporterade stavningar och exakta datanamn.
- Gemensamma kolumnnamn bevisar inte foreign keys, unika nycklar eller fullstandiga JOIN-villkor. Hitta inte pa index eller relationer.
- Verifiera flaggvarden i det aktuella faltets dokumentation; anta inte att alla char/boolean-falt anvander samma varden.
- Dokumentationen beskriver JAS 15.0.12. Bekrafta inte att en annan installation har samma schema utan underlag.
- Andra inte kallfilerna och kor inte SQL mot en databas utan uttrycklig begaran.

## Skills och kommandon
Anvand relevant skill for fragan. De korta slash-kommandona finns i `.github/prompts/` och lankar till arbetsflodet.

| Kommando | Skill | Uppgift |
| --- | --- | --- |
| /jvsdb | jeeves-db-expert | Databasfragor, kolumner, relationer och programkopplingar |
| /jvsDesc | jeeves-describe | Beskriv tabell, kolumn eller term |
| /jvsfind | jeeves-doc-navigator | Sok i alla fem dokumentationsfiler |
| /jvsimpact | jeeves-change-impact | Konsekvensanalys och testchecklista |
| /jvsprogram | jeeves-program-explainer | Program, huvudtabell, noder och rapporter |
| /jvssql | jeeves-sql-builder | SQL-forslag fran naturligt sprak |
| /jvstable | jeeves-table-mapper | Tabellschema och datatyper |
| /jvsterm | jeeves-term-linker | Termdefinition och anvandning |