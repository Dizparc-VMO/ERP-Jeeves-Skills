---
name: jeeves-sql-builder
description: 'Anvand for att oversatta svenska affarsfragor till SQL-forslag mot Jeeves ERP: skriv SQL, SELECT, skapa en vy, fakturor, kundorder, lager, budget och aggregerade rapporter.'
user-invocable: false
---

# Jeeves SQL Builder

Folj [projektinstruktionerna](../../copilot-instructions.md).
Skriv SQL-forslag; anslut inte till en databas och kor inte fragor som en del av detta arbetsflode.

## Arbetsflode
1. Identifiera data, urval, tidsperiod, foretag och resultatets detaljniva. Fraga om oklarheter som paverkar korrektheten.
2. Sok affarsbegreppen i [Tables_SE.md](../../../Tables_SE.md). Anvand inte en schablonordlista som bevis for tabellnamn.
3. Verifiera varje tabell och varje kolumn mot aktuell tabellspecifikation. SQL-namn kommer fran tabellkod och Datanamn, inte fran ledtext eller HTML-prefix.
4. Kontrollera betydelse, datum, status och flaggvarden i [Terms_SE.md](../../../Terms_SE.md). Anvand [Programs_SE.md](../../../Programs_SE.md) och [DocAreas_SE.md](../../../DocAreas_SE.md) nar affarslogik behover klarlaggas.
5. Identifiera JOIN-kandidater och kontrollera foretagsavgransning, radnummer, restnummer och andra dokumenterade kopplingsfalt. Samma kolumnnamn ar inte bevis for en foreign key eller unikhet.
6. Om fullstandiga JOIN-nycklar inte kan styrkas: skriv "oklart i kallet", lista saknade uppgifter och markera tydligt att SQL-forslaget bygger pa antaganden. Presentera inte ett osakert forslag som verifierad SQL.
7. Bygg SELECT, aggregering eller efterfragad CREATE VIEW med tydliga alias och dokumenterade datatyper. Anvand `ForetagKod`-filter och foretagsvillkor i JOIN nar faltet finns och ar relevant. Hitta inte pa ett foretagsnummer.
8. Behall den tidigare command-konventionen `WITH (NOLOCK)` nar anvandaren vill folja den, men behandla den inte som ett belagt Jeeves-krav. Om lasningsisolering inte ar angiven, utelamna tabellhinten och ange att val av isolering inte framgar av kallorna.
9. Kontrollera att alla identifierare finns i dokumentationen och att aggregeringen inte bygger pa obevisad kardinalitet. Detta ar dokumentationskontroll, inte verifiering mot en levande databas.

## Svarsformat
- SQL: syfte och kort forklaring.
- Anvanda tabeller: kod, namn och roll.
- SQL: fenced `sql`-block med forslaget.
- Kolumnforklaringar: Datanamn, alias och betydelse.
- Forutsattningar: parametrar, foretag, datum, antagna relationer och ej verifierat schema.
- Hittad i: kallfiler och relevanta avsnitt.

Ge inte generella pastanden om Y/N, 1/0, decimalprecision eller index utan falt- och tabellspecifikt underlag. Om anvandaren efterfragar en vy, skilj foreslagen vydefinition fran befintliga dokumenterade objekt.