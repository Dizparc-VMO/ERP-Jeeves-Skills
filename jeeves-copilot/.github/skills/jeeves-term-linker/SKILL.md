---
name: jeeves-term-linker
description: 'Anvand for Jeeves-termdefinitioner, ted_-koder, vad betyder termen eller faltet och var en kolumn anvands i tabeller och verksamhetsfloden.'
user-invocable: false
---

# Jeeves Term Linker

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Hitta termens kod eller namn i [Terms_SE.md](../../../Terms_SE.md).
2. Las definition, villkor, undantag och eventuella standardvarden fram till nasta `# ted_`-rubrik.
3. Hamta hela listan under "Faltet ingar i foljande tabeller".
4. Verifiera efterfragade tabellanvandningar och datatyper i [Tables_SE.md](../../../Tables_SE.md).
5. Ge en praktisk tolkning endast nar den stodjs av definitionen. Termens tabelllista bevisar inte relationer mellan tabeller.
6. Vid utebliven exakt match: visa upp till tre hittade alternativ. Vid saknad definition: "oklart i kallet" och vad som saknas.

## Svarsformat
- Term: ledtext och exakt Datanamn/kod.
- Definition: kort forklaring med relevanta undantag.
- Ingar i tabeller: samtliga dokumenterade namn och koder.
- Praktisk tolkning: kallbackad anvandning.
- Hittad i: kallor och radnummer nar mojligt.