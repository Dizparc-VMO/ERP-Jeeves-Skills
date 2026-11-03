# Jeeves ERP med GitHub Copilot

Copilot-version av de atta skills och atta commands som finns i det ursprungliga projektets `.claude`-mapp. Originalen lamnas oforandrade.

## Personlig installation - alla projektmappar
Den personliga installationen anvander:
- `%USERPROFILE%\.copilot\skills\jeeves-*\SKILL.md` for atta skills, anropbara som exempelvis `/jeeves-db-expert`.
- `%APPDATA%\Code\User\prompts\jvs*.prompt.md` for de atta korta kommandona, exempelvis `/jvsdb` och `/jvssql`.
- `%USERPROFILE%\.copilot\jeeves-docs\` for dokumentkopior och Jeeves-regler som skills laser vid anvandning.

Efter installation: kor **Developer: Reload Window**, starta en ny Copilot-chatt i valfri projektmapp och skriv `/jvsdb` eller `/jeeves-db-expert`. Ingen Jeeves-projektmapp behover oppnas. Detta galler Copilot i VS Code pa den har datorn och profilen, inte automatiskt GitHub-webbplatsen eller andra datorer. Copilot kan be om tillatelse att lasa dokumentationen utanfor aktuell projektmapp.

Installationen kan goras med [install-personal.ps1](./install-personal.ps1):
```powershell
& '.\install-personal.ps1'
```
Installeraren skyddar befintliga filer och avbryter om Jeeves-installationen redan finns. Den verifierar dokumentkopiornas hash och alla lokala lankar. Den personliga versionen har `user-invocable: true`; projektversionen nedan behaller `false` for att undvika dubbla kommandon.

## Alternativ: starta projektversionen
1. Oppna **denna mapp, jeeves-copilot**, som projektmapp i VS Code via File > Open Folder. En `.github`-mapp inuti ett underprojekt hittas inte nodvandigtvis fran den overordnade projektmappen.
2. Anvand GitHub Copilot Chat i Agent-lage och starta en ny chatt.
3. Skriv `/` och valj ett av kommandona nedan. Skriv din fraga efter kommandot.
4. Om kommandona inte visas, kor Developer: Reload Window och kontrollera organisationens policy for Copilot-anpassningar.

## Kommandon
| Kommando | Exempel |
| --- | --- |
| `/jvsdb` | `/jvsdb vilka kolumner har tabellen ac?` |
| `/jvsDesc` | `/jvsDesc ArtNr` |
| `/jvsfind` | `/jvsfind menu code Delete` |
| `/jvsimpact` | `/jvsimpact vad paverkas om vi andrar AcColorType?` |
| `/jvsprogram` | `/jvsprogram AcColor` |
| `/jvssql` | `/jvssql hamta fakturor fran 2024 for ett foretag` |
| `/jvstable` | `/jvstable ac` |
| `/jvsterm` | `/jvsterm AcColorType` |

## Struktur
```text
jeeves-copilot/
  .github/
    copilot-instructions.md
    prompts/                    # Atta *.prompt.md slash-kommandon
    skills/<skillnamn>/SKILL.md  # Atta arbetsfloden
  DocAreas_SE.md
  Jeeves_SE.md
  Programs_SE.md
  Tables_SE.md
  Terms_SE.md
  README.md
```

Projektinstruktionerna laddas som gemensamma regler. Skills kan valjas automatiskt utifran beskrivningarna; `user-invocable: false` undviker dubbla langa slash-kommandon. Prompt-filerna ger de korta kommandona och lankar till respektive skill.

Claude-specifika `$ARGUMENTS` har ersatts med instruktionen att anvanda texten efter slash-kommandot. Claude-installationens `settings.local.json` kopieras inte: den ar inte Copilot-konfiguration.

## Kallor och begransningar
De fem dokumentationsfilerna ar kopior av originalen och beskriver JAS 15.0.12. Skills soker relevanta avsnitt i stallet for att lasa allt. Svaren ges pa svenska med kallhanvisningar.

Konverteringen behaller arbetsflodena men tar bort obestyrkta tabellordlistor och generella antaganden om flaggor, nycklar och datatyper. `NOLOCK` ar inte ett automatiskt krav. SQL ar forslag som kontrolleras mot dokumentationen, inte mot en levande databas. Saknat underlag markeras med "oklart i kallet".

Vid nya dokumentationsversioner: ersatt de fem kopiorna med uppdaterade kallfiler och kontrollera angiven JAS-version.