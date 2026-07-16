#Requires -Version 7.0
<#
.SYNOPSIS
    CI helper: copy compiled PDFs to _site/ for GitHub Pages deployment
#>

$ErrorActionPreference = 'Continue'
$base = $PSScriptRoot + '/..'
$out  = "$base/_site"

if (-not (Test-Path -LiteralPath $out)) {
    New-Item -ItemType Directory -Path $out | Out-Null
}

$projects = @(
    @{ dir = 'algorithm';                       job = 'algorithm' }
    @{ dir = 'configure';                       job = 'configure' }
    @{ dir = 'Contains View Range';             job = 'containers_views_ranges' }
    @{ dir = 'CoreBook';                        job = 'cpp_core_guidelines_textbook' }
    @{ dir = 'CTPR and PImpl';                  job = 'ctpr_and_pimpl' }
    @{ dir = 'Design Pattern';                  job = 'design_patterns' }
    @{ dir = 'extern C use in other language';  job = 'externC' }
    @{ dir = 'IO';                              job = 'io' }
    @{ dir = 'memory leak';                     job = 'memory_leak' }
    @{ dir = 'Operator Overloading';            job = 'operator_overloading' }
    @{ dir = 'PackageManager';                  job = 'cpp_package_managers' }
    @{ dir = 'Reflect';                         job = 'reflection' }
    @{ dir = 'Script';                          job = 'scripting' }
    @{ dir = 'Serialization';                   job = 'serialization' }
    @{ dir = 'SFINAE and Concept';              job = 'sfinae_and_concepts' }
    @{ dir = 'Thread and Coroutine';            job = 'thread_coroutine' }
    @{ dir = 'NewDelete';                       job = 'new_delete' }
)

$copied = 0
$failed = 0

foreach ($p in $projects) {
    $pdfPath = "$base/$($p.dir)/$($p.job).pdf"
    if (Test-Path -LiteralPath $pdfPath) {
        Copy-Item -LiteralPath $pdfPath -Destination "$out/$($p.job).pdf" -Force
        $copied++
        Write-Host "[OK] $($p.job).pdf"
    } else {
        $failed++
        Write-Host "[MISS] $($p.job).pdf not found"
    }
}

Write-Host "`nCopied: $copied / $($projects.Count) | Missing: $failed"

if ($failed -gt 0) {
    exit 1
}
