---
name: jeeves-change-impact
description: 'Anvand for konsekvensanalys av andringar i Jeeves-program, tabeller, kolumner eller termer: vad paverkas, beroenden, risker och regressionstestchecklista.'
user-invocable: false
---

# Jeeves Change Impact Analyzer

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Identifiera entitet och vad som ska andras. Be om precisering om andringens innebord saknas.
2. Hitta program i [Programs_SE.md](../../../Programs_SE.md), tabell i [Tables_SE.md](../../../Tables_SE.md) eller term i [Terms_SE.md](../../../Terms_SE.md).
3. Bygg direkta dokumenterade kopplingar: program till huvudtabell, tabell till program och term till tabeller.
4. Folj ett extra hopp for indirekta kopplingar, exempelvis term till tabell till program. Ange kedjan och kalla.
5. Kontrollera [DocAreas_SE.md](../../../DocAreas_SE.md) for berorda arbetsfloden, rapporter, behorigheter och klientstod nar relevant.
6. Bedom datamodell-, rapport-, arbetsflodes-, behorighets- och klientrisker utifran belagda kopplingar. Skilj mojlig risk fran konstaterad paverkan.
7. Skapa en fokuserad testchecklista for andringen. Dokumentationen ger inte en fullstandig kodberoendeanalys; ange nar procedurer, triggers, integrationer eller anpassningar behover granskas separat.

## Svarsformat
- Andring: entitet och andringens innebord.
- Direkt paverkan: kopplingar med kallor.
- Indirekt paverkan: kopplingskedjor med kallor.
- Riskniva: lag, medel eller hog med motiv; om underlag inte racker, "oklart i kallet".
- Testchecklista: numrerade steg.
- Hittad i: kallor samt vad som saknas for en fullstandig analys.