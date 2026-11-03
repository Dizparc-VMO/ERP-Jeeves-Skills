---
name: jeeves-program-explainer
description: 'Anvand nar anvandaren fragar om ett Jeeves-program, pgm_-kod eller programnamn och vill ha beskrivning, huvudtabell, programkopplingar, noder, fonster eller rapporter.'
user-invocable: false
---

# Jeeves Program Explainer

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Hitta programkod eller namn i [Programs_SE.md](../../../Programs_SE.md).
2. Las hela programavsnittet fram till nasta `# pgm_`-rubrik.
3. Hamta programnamn, exakt kod, beskrivning, huvudtabell, noder/fonster och rapporter om de finns.
4. Korsverifiera huvudtabellen i [Tables_SE.md](../../../Tables_SE.md).
5. Folj relevanta kapitelreferenser i [DocAreas_SE.md](../../../DocAreas_SE.md) endast nar fragan kraver arbetsflode eller forutsattningar.
6. Om exakt match saknas: ge upp till tre narliggande hittade program. Anta inte att en nods ledtext ar en tabellkod.

## Svarsformat
- Program: namn och kod.
- Beskrivning: kort sammanfattning.
- Huvudtabell: namn och kod, eller "oklart i kallet".
- Noder/Fonster: dokumenterade nodkoder och namn.
- Rapporter: dokumenterade rapporter, eller "inte angivet i avsnittet".
- Kommentar: viktiga begransningar eller forutsattningar.
- Hittad i: kallfil och radnummer nar mojligt.