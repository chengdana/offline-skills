param(
  [string]$Target = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

New-Item -ItemType Directory -Force -Path $Target | Out-Null

foreach ($dir in @("skills", "superpowers", "system-skills")) {
  $srcRoot = Join-Path $Root $dir
  if (-not (Test-Path $srcRoot)) {
    continue
  }

  Get-ChildItem -Path $srcRoot -Directory | ForEach-Object {
    $destination = Join-Path $Target $_.Name
    if (Test-Path $destination) {
      Remove-Item -LiteralPath $destination -Recurse -Force
    }
    Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse
    Write-Host "Installed $($_.Name) -> $destination"
  }
}

Write-Host "Done. Target: $Target"
