---
name: jeeves-doc-navigator
description: 'Anvand for sokning och navigation i Jeeves-dokumentationen: hitta, var finns, visa avsnitt, vilken fil, pgm_, tbd_, ted_, menykoder, klientstod och makrofunktioner.'
user-invocable: false
---

# Jeeves Doc Navigator

Folj [projektinstruktionerna](../../copilot-instructions.md).

## Arbetsflode
1. Identifiera sokfras, exakt kod och eventuell avgransning till en fil.
2. Prioritera `pgm_*` i [Programs_SE.md](../../../Programs_SE.md), `tbd_*` i [Tables_SE.md](../../../Tables_SE.md) och `ted_*` i [Terms_SE.md](../../../Terms_SE.md).
3. Sok funktioner, arbetsfloden, menykoder, klientstod och makron i [DocAreas_SE.md](../../../DocAreas_SE.md). Anvand [Jeeves_SE.md](../../../Jeeves_SE.md) for allman dokumentationsinformation.
4. Sok forst exakt kod, sedan objektnamn och slutligen fritext. Anvand stavningen i exporten nar svenska tecken saknas.
5. Las den matchande rubrikens avsnitt och returnera upp till fem basta traffar med kort utdrag eller sammanfattning.
6. Om ingen exakt traff finns: visa upp till fem narliggande, faktiskt hittade alternativ och foresla en mer precis sokfras.

## Svarsformat per traff
- Traff: rubrik.
- Kod: exakt objektkod om tillganglig.
- Kort svar: 1-3 meningar.
- Hittad i: klickbar kallfil och radnummer nar mojligt.

Vid saknat underlag: "oklart i kallet" och vad som saknas.