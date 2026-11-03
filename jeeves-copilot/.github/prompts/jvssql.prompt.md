---
name: jvssql
description: 'Oversatt en svensk affarsfraga till ett kallbackat SQL-forslag for Jeeves.'
argument-hint: 'Beskriv urvalet, t.ex. hamta fakturor fran 2024 for ett foretag'
agent: agent
---

Las och folj [jeeves-sql-builder](../skills/jeeves-sql-builder/SKILL.md).
Anvand texten efter slash-kommandot som uppgift. Om uppgiften saknas, be om den.
Verifiera tabeller, Datanamn, datatyper, flaggvarden och foretagsavgransning i dokumentationen. Forklara SQL-forslaget pa svenska med "Hittad i" och tydliga antaganden. Kor inte SQL. Anvand inte NOLOCK som ett obestyrkt standardkrav.