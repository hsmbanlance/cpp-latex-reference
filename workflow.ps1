#Requires -Version 7.0
<#
.SYNOPSIS
    C/C++ LaTeX 参考手册 — 项目工作流
.DESCRIPTION
    统一管理 15 个子项目的编译、清理、状态检查。
.PARAMETER Action
    操作类型: build-all, build, clean-all, clean, status, list, open
.PARAMETER Project
    子项目名称（用于 build / clean / open），可用 list 查看
.PARAMETER Pass
    编译 pass 数（默认 2），仅 build 时有效
.EXAMPLE
    .\workflow.ps1 build-all              # 编译全部
    .\workflow.ps1 build SFINAE            # 编译单个
    .\workflow.ps1 clean-all               # 清理全部辅助文件
    .\workflow.ps1 clean Algorithm          # 清理单个
    .\workflow.ps1 status                  # 查看状态
    .\workflow.ps1 list                    # 列出所有项目
    .\workflow.ps1 open IO                 # 打开 PDF
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateSet('build-all','build','clean-all','clean','status','list','open')]
    [string]$Action,

    [string]$Project,
    [int]$Pass = 2
)

$ErrorActionPreference = 'Continue'
$base = $PSScriptRoot

# ─── 项目注册表 ───
$projects = [ordered]@{
    'SFINAE'        = @{ dir = 'SFINAE and Concept';              tex = 'sfinae_and_concepts.tex';              job = 'sfinae_and_concepts' }
    'CRTP'          = @{ dir = 'CTPR and PImpl';                  tex = 'ctpr_and_pimpl.tex';                    job = 'ctpr_and_pimpl' }
    'Reflect'       = @{ dir = 'Reflect';                         tex = 'reflection.tex';                        job = 'reflection' }
    'PkgMgr'        = @{ dir = 'PackageManager';                  tex = 'cpp_package_managers.tex';              job = 'cpp_package_managers' }
    'MemLeak'       = @{ dir = 'memory leak';                     tex = 'memory_leak.tex';                       job = 'memory_leak' }
    'CoreBook'      = @{ dir = 'CoreBook';                        tex = 'cpp_core_guidelines_textbook.tex';      job = 'cpp_core_guidelines_textbook' }
    'DesignPat'     = @{ dir = 'Design Pattern';                  tex = 'design_patterns.tex';                  job = 'design_patterns' }
    'ThreadCo'      = @{ dir = 'Thread and Coroutine';            tex = 'thread_coroutine.tex';                 job = 'thread_coroutine' }
    'ContView'      = @{ dir = 'Contains View Range';             tex = 'containers_views_ranges.tex';           job = 'containers_views_ranges' }
    'Algorithm'     = @{ dir = 'algorithm';                       tex = 'algorithm.tex';                        job = 'algorithm' }
    'Configure'     = @{ dir = 'configure';                       tex = 'configure.tex';                        job = 'configure' }
    'Script'        = @{ dir = 'Script';                          tex = 'scripting.tex';                        job = 'scripting' }
    'Serialization' = @{ dir = 'Serialization';                   tex = 'serialization.tex';                    job = 'serialization' }
    'IO'            = @{ dir = 'IO';                              tex = 'io.tex';                               job = 'io' }
    'ExternC'       = @{ dir = 'extern C use in other language';  tex = 'externC.tex';                          job = 'externC' }
    'OpOverload'    = @{ dir = 'Operator Overloading';            tex = 'operator_overloading.tex';             job = 'operator_overloading' }
}

# ─── 辅助函数 ───
function Resolve-Project {
    param([string]$Name)
    if (-not $projects.Contains($Name)) {
        Write-Host "[ERROR] unknown project: $Name" -ForegroundColor Red
        Write-Host "  Available: $($projects.Keys -join ', ')" -ForegroundColor DarkGray
        return $null
    }
    return $projects[$Name]
}

function Invoke-Build {
    param([string]$Name, [hashtable]$Info)

    $projDir = "$base\$($Info.dir)"
    $buildScript = "$projDir\build.ps1"

    $sep = '=' * 60
    Write-Host "`n$sep" -ForegroundColor Cyan
    Write-Host "  Building: $Name ($($Info.tex))" -ForegroundColor Cyan
    Write-Host "$sep" -ForegroundColor Cyan

    if (-not (Test-Path -LiteralPath $buildScript)) {
        Write-Host "  [MISSING] build.ps1 not found!" -ForegroundColor Red
        return [PSCustomObject]@{ Name=$Name; Status='MISSING'; Errors=-1; Overfull=-1; SizeKB='?' }
    }

    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $args_ = @()
    if ($Pass -ne 2) { $args_ += @('-MaxRuns', $Pass) }
    $output = & pwsh -NoProfile -File $buildScript @args_ 2>&1
    $sw.Stop()
    $elapsed = '{0:F1}' -f $sw.Elapsed.TotalSeconds

    $lastText = $output | Select-Object -Last 15 | Out-String
    $errors = -1; $overfull = -1; $sizeKB = '?'
    if ($lastText -match '\u9519\u8bef: (\d+)') { $errors = [int]$Matches[1] }
    if ($lastText -match 'Overfull: (\d+)')     { $overfull = [int]$Matches[1] }
    if ($lastText -match '\u5927\u5c0f: ([\d.]+) KB') { $sizeKB = $Matches[1] }

    $failed = $lastText -match '\u7f16\u8bd1\u5931\u8d25'
    $status = if ($failed -or $errors -gt 0) { 'FAIL' }
              elseif ($overfull -gt 0)       { 'OVERFULL' }
              elseif ($errors -eq 0)         { 'OK' }
              else                           { 'UNKNOWN' }

    $color = switch ($status) { 'OK'{'Green'} 'OVERFULL'{'DarkYellow'} 'FAIL'{'Red'} default{'Gray'} }
    Write-Host "  [$status] Err=$errors Ov=$overfull ${sizeKB}KB ${elapsed}s" -ForegroundColor $color

    if ($status -eq 'FAIL') {
        $output | Select-Object -Last 15 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkRed }
    }

    return [PSCustomObject]@{ Name=$Name; Status=$status; Errors=$errors; Overfull=$overfull; SizeKB=$sizeKB }
}

function Invoke-Clean {
    param([string]$Name, [hashtable]$Info)

    $projDir = "$base\$($Info.dir)"
    $buildScript = "$projDir\build.ps1"

    if (-not (Test-Path -LiteralPath $buildScript)) {
        Write-Host "  $Name : build.ps1 not found, skip" -ForegroundColor DarkGray
        return
    }

    & pwsh -NoProfile -File $buildScript -Clean 2>&1 | Out-Null
    Write-Host "  $Name : cleaned" -ForegroundColor DarkGray
}

function Show-Status {
    $sep = '=' * 78
    Write-Host "`n$sep" -ForegroundColor Cyan
    Write-Host "  PROJECT STATUS" -ForegroundColor Cyan
    Write-Host "$sep" -ForegroundColor Cyan
    Write-Host ('  {0,-16} {1,-12} {2,10} {3,10} {4}' -f 'Project','PDF','Size(KB)','Modified','Overfull?') -ForegroundColor White

    $totalOK = 0; $totalWarn = 0; $totalMiss = 0

    foreach ($kv in $projects.GetEnumerator()) {
        $name = $kv.Key
        $info = $kv.Value
        $pdfPath = "$base\$($info.dir)\$($info.job).pdf"

        if (Test-Path -LiteralPath $pdfPath) {
            $fi = Get-Item -LiteralPath $pdfPath
            $sizeKB = [math]::Round($fi.Length / 1KB, 1)
            $mod = $fi.LastWriteTime.ToString('yyyy-MM-dd')
            $totalOK++
            $color = 'Green'
        } else {
            $sizeKB = '-'
            $mod = '-'
            $totalMiss++
            $color = 'Red'
        }

        Write-Host ('  {0,-16} {1,-12} {2,10} {3,10}' -f $name, $(if(Test-Path -LiteralPath $pdfPath){'OK'}else{'MISSING'}), $sizeKB, $mod) -ForegroundColor $color
    }

    Write-Host "`n  Total: $($projects.Count) | Built: $totalOK | Missing: $totalMiss" -ForegroundColor Cyan
}

function Show-List {
    $sep = '=' * 70
    Write-Host "`n$sep" -ForegroundColor Cyan
    Write-Host "  C/C++ LaTeX Reference Projects ($($projects.Count))" -ForegroundColor Cyan
    Write-Host "$sep" -ForegroundColor Cyan
    foreach ($kv in $projects.GetEnumerator()) {
        Write-Host ('  {0,-16} {1}' -f $kv.Key, $kv.Value.dir) -ForegroundColor White
    }
    Write-Host "`n  Usage:" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 build-all          # compile all" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 build <Project>    # compile one" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 clean-all          # clean all" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 clean <Project>    # clean one" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 status             # check PDF status" -ForegroundColor DarkGray
    Write-Host "    .\workflow.ps1 open <Project>     # open PDF" -ForegroundColor DarkGray
}

# ─── Main ───
switch ($Action) {
    'build-all' {
        $results = @()
        $totalSw = [System.Diagnostics.Stopwatch]::StartNew()

        foreach ($kv in $projects.GetEnumerator()) {
            $r = Invoke-Build -Name $kv.Key -Info $kv.Value
            $results += $r
        }

        $totalSw.Stop()

        $sep = '=' * 78
        Write-Host "`n$sep" -ForegroundColor Cyan
        Write-Host "  COMPILATION SUMMARY" -ForegroundColor Cyan
        Write-Host "$sep" -ForegroundColor Cyan

        $ok   = @($results | Where-Object { $_.Status -eq 'OK' }).Count
        $warn = @($results | Where-Object { $_.Status -eq 'OVERFULL' }).Count
        $fail = @($results | Where-Object { $_.Status -eq 'FAIL' }).Count
        $miss = @($results | Where-Object { $_.Status -eq 'MISSING' }).Count

        $sc = if ($fail -gt 0 -or $miss -gt 0) {'Red'} elseif ($warn -gt 0) {'DarkYellow'} else {'Green'}
        Write-Host "  OK: $ok | Overfull: $warn | FAIL: $fail | Missing: $miss" -ForegroundColor $sc

        foreach ($r in $results) {
            $c = switch ($r.Status) { 'OK'{'Green'} 'OVERFULL'{'DarkYellow'} 'FAIL'{'Red'} default{'Gray'} }
            Write-Host ('  {0,-16} {1,-10} Err={2} Ov={3} {4}KB' -f $r.Name,$r.Status,$r.Errors,$r.Overfull,$r.SizeKB) -ForegroundColor $c
        }

        $tt = '{0:F1}' -f $totalSw.Elapsed.TotalSeconds
        Write-Host "`n  Total: ${tt}s" -ForegroundColor Cyan
    }

    'build' {
        if (-not $Project) { Write-Host "[ERROR] -Project required" -ForegroundColor Red; return }
        $info = Resolve-Project $Project
        if (-not $info) { return }
        Invoke-Build -Name $Project -Info $info | Out-Null
    }

    'clean-all' {
        Write-Host "`n  Cleaning all projects..." -ForegroundColor Yellow
        foreach ($kv in $projects.GetEnumerator()) {
            Invoke-Clean -Name $kv.Key -Info $kv.Value
        }
        Write-Host "`n  Done." -ForegroundColor Green
    }

    'clean' {
        if (-not $Project) { Write-Host "[ERROR] -Project required" -ForegroundColor Red; return }
        $info = Resolve-Project $Project
        if (-not $info) { return }
        Invoke-Clean -Name $Project -Info $info
    }

    'status' {
        Show-Status
    }

    'list' {
        Show-List
    }

    'open' {
        if (-not $Project) { Write-Host "[ERROR] -Project required" -ForegroundColor Red; return }
        $info = Resolve-Project $Project
        if (-not $info) { return }
        $pdfPath = "$base\$($info.dir)\$($info.job).pdf"
        if (Test-Path -LiteralPath $pdfPath) {
            Start-Process $pdfPath
        } else {
            Write-Host "[ERROR] PDF not found: $pdfPath" -ForegroundColor Red
            Write-Host "  Run: .\workflow.ps1 build $Project" -ForegroundColor DarkGray
        }
    }
}
