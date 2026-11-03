param(
    [string]$CopilotHome = (Join-Path $env:USERPROFILE '.copilot'),
    [string]$PromptsDirectory = (Join-Path $env:APPDATA 'Code\User\prompts')
)

$ErrorActionPreference = 'Stop'
$skillSource = Join-Path $PSScriptRoot '.github\skills'
$promptSource = Join-Path $PSScriptRoot '.github\prompts'
$skillsDirectory = Join-Path $CopilotHome 'skills'
$resourcesDirectory = Join-Path $CopilotHome 'jeeves-docs'
$documents = @('DocAreas_SE.md', 'Jeeves_SE.md', 'Programs_SE.md', 'Tables_SE.md', 'Terms_SE.md')
$skillFiles = @(Get-ChildItem -LiteralPath $skillSource -Recurse -Filter 'SKILL.md')
$promptFiles = @(Get-ChildItem -LiteralPath $promptSource -Filter '*.prompt.md')
$utf8 = New-Object System.Text.UTF8Encoding($false)

if ($skillFiles.Count -ne 8 -or $promptFiles.Count -ne 8) {
    throw 'Expected eight source skills and eight source prompts.'
}

$destinations = @($resourcesDirectory)
foreach ($file in $skillFiles) {
    $destinations += Join-Path $skillsDirectory $file.Directory.Name
}
foreach ($file in $promptFiles) {
    $destinations += Join-Path $PromptsDirectory $file.Name
}
foreach ($destination in $destinations) {
    if (Test-Path -LiteralPath $destination) {
        throw "Installation stopped to protect existing files: $destination"
    }
}
foreach ($document in $documents) {
    if (-not (Test-Path -LiteralPath (Join-Path $PSScriptRoot $document) -PathType Leaf)) {
        throw "Source documentation missing: $document"
    }
}

$installedFiles = @()
$null = New-Item -ItemType Directory -Path $resourcesDirectory -Force
$null = New-Item -ItemType Directory -Path $PromptsDirectory -Force
foreach ($document in $documents) {
    $source = Join-Path $PSScriptRoot $document
    $destination = Join-Path $resourcesDirectory $document
    Copy-Item -LiteralPath $source -Destination $destination
    if ((Get-FileHash -LiteralPath $source).Hash -ne (Get-FileHash -LiteralPath $destination).Hash) {
        throw "Documentation hash mismatch: $document"
    }
}

$rules = Get-Content -LiteralPath (Join-Path $PSScriptRoot '.github\copilot-instructions.md') -Raw -Encoding UTF8
foreach ($document in $documents) {
    $rules = $rules.Replace("(../$document)", "(./$document)")
}
$rulesFile = Join-Path $resourcesDirectory 'jeeves-rules.md'
[System.IO.File]::WriteAllText($rulesFile, $rules, $utf8)
$installedFiles += $rulesFile

foreach ($file in $skillFiles) {
    $directory = Join-Path $skillsDirectory $file.Directory.Name
    $null = New-Item -ItemType Directory -Path $directory -Force
    $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    $text = $text.Replace('user-invocable: false', 'user-invocable: true')
    $text = $text.Replace('(../../copilot-instructions.md)', '(../../jeeves-docs/jeeves-rules.md)')
    foreach ($document in $documents) {
        $text = $text.Replace("(../../../$document)", "(../../jeeves-docs/$document)")
    }
    $text = $text.Replace('Folj [projektinstruktionerna]', 'Las och folj [Jeeves-instruktionerna]')
    $text += "`nDokumentationen ligger utanfor det aktuella projektet. Sok och las kallfilerna via deras lankade filsystemssokvagar, inte enbart via sokning i aktuell workspace. Om atkomst nekas, ange detta och be om tillatelse; hitta inte pa ett svar.`n"
    $destination = Join-Path $directory 'SKILL.md'
    [System.IO.File]::WriteAllText($destination, $text, $utf8)
    $installedFiles += $destination
}

$promptBaseUri = [System.Uri]::new($PromptsDirectory.TrimEnd('\') + '\')
foreach ($file in $promptFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    foreach ($skillFile in $skillFiles) {
        $skillName = $skillFile.Directory.Name
        $skillPath = Join-Path (Join-Path $skillsDirectory $skillName) 'SKILL.md'
        $skillUri = [System.Uri]::new($skillPath)
        $relativePath = $promptBaseUri.MakeRelativeUri($skillUri).ToString()
        $text = $text.Replace("(../skills/$skillName/SKILL.md)", "($relativePath)")
    }
    $destination = Join-Path $PromptsDirectory $file.Name
    [System.IO.File]::WriteAllText($destination, $text, $utf8)
    $installedFiles += $destination
}

$linkCount = 0
foreach ($installedFile in $installedFiles) {
    $text = Get-Content -LiteralPath $installedFile -Raw -Encoding UTF8
    foreach ($link in [regex]::Matches($text, '\[[^\]]+\]\((?<path>[^)]+)\)')) {
        $relativePath = [System.Uri]::UnescapeDataString($link.Groups['path'].Value)
        $resolved = Join-Path (Split-Path -Parent $installedFile) $relativePath
        if (-not (Test-Path -LiteralPath $resolved -PathType Leaf)) {
            throw "Broken installed link in ${installedFile}: $relativePath"
        }
        $linkCount++
    }
}
foreach ($file in $skillFiles) {
    $destination = Join-Path (Join-Path $skillsDirectory $file.Directory.Name) 'SKILL.md'
    $text = Get-Content -LiteralPath $destination -Raw -Encoding UTF8
    if ($text -notmatch '(?m)^user-invocable: true\r?$' -or $text.Contains('../../../Tables_SE.md')) {
        throw "Skill not converted for personal installation: $destination"
    }
}

Write-Output "PASS: 8 personal skills, 8 personal prompts, 5 identical documentation copies, $linkCount valid links."
Write-Output "Skills: $skillsDirectory"
Write-Output "Prompts: $PromptsDirectory"
Write-Output "Documentation: $resourcesDirectory"