#Requires -Version 7.0
<#
.SYNOPSIS
    编译C++ 包管理方案对比 (XeLaTeX 双pass)
.DESCRIPTION
    使用 MiKTeX XeLaTeX 编译 cpp_package_managers.tex，生成 PDF。
    支持 -Clean 清理辅助文件，-SinglePass 单pass快速编译。
.PARAMETER Clean
    删除所有辅助文件（.aux, .toc, .out, .log, .idx, .ind, .ilg, .synctex.gz 等）
.PARAMETER SinglePass
    仅执行一遍 XeLaTeX（用于快速预览，不生成完整目录和索引）
.PARAMETER MaxRuns
    最大编译pass数（默认 2）
#>
[CmdletBinding()]
param(
    [switch]$Clean,
    [switch]$SinglePass,
    [int]$MaxRuns = 2
)

$ErrorActionPreference = 'Stop'

# ─── 定位脚本目录 ───
$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$texFile   = 'cpp_package_managers.tex'
$jobName   = 'cpp_package_managers'
$origDir   = Get-Location

# ─── 辅助文件列表 ───
$auxExtensions = @('.aux', '.toc', '.out', '.log', '.synctex.gz',
                   '.fls', '.fdb_latexmk', '.idx', '.ilg', '.ind',
                   '.xdv', '.bcf', '.run.xml', '.lof', '.lot')

function Remove-AuxFiles {
    $count = 0
    foreach ($ext in $auxExtensions) {
        $path = Join-Path $scriptDir "$jobName$ext"
        if (Test-Path -LiteralPath $path) {
            Remove-Item -LiteralPath $path -Force
            $count++
        }
    }
    # 手动 TOC 文件（LaTeX 2025-11-01 内核 bug 修复产物）
    $manualTocPath = Join-Path $scriptDir "$jobName-manual.toc"
    if (Test-Path -LiteralPath $manualTocPath) {
        Remove-Item -LiteralPath $manualTocPath -Force
        $count++
    }
    if ($count -gt 0) {
        Write-Host "  已清理 $count 个辅助文件" -ForegroundColor DarkGray
    }
}

try {
    # ─── 切换到脚本目录（解决中文路径问题）───
    Set-Location -LiteralPath $scriptDir

    # ─── Clean 模式 ───
    if ($Clean) {
        Write-Host "`n=== 清理辅助文件 ===" -ForegroundColor Cyan
        Remove-AuxFiles
        $pdfPath = Join-Path $scriptDir "$jobName.pdf"
        if (Test-Path -LiteralPath $pdfPath) {
            Write-Host "  PDF 保留: $pdfPath" -ForegroundColor DarkGray
        }
        return
    }

    # ─── 检查 .tex 文件 ───
    if (-not (Test-Path -LiteralPath $texFile)) {
        Write-Error "找不到 $texFile，请确认文件存在: $scriptDir\$texFile"
        return
    }

    # ─── 定位 XeLaTeX ───
    $xelatexPath = $null
    $candidates = @(
        'D:\winget\MiKTeX\miktex\bin\x64\xelatex.exe',
        'D:\winget\MiKTex\miktex\bin\x64\xelatex.exe',
        'C:\Program Files\MiKTeX\miktex\bin\x64\xelatex.exe',
        'C:\Users\hmsbalance\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
    )

    # 先尝试 PATH
    $pathXeLatex = Get-Command xelatex -ErrorAction SilentlyContinue
    if ($pathXeLatex) {
        $xelatexPath = $pathXeLatex.Source
    } else {
        foreach ($c in $candidates) {
            if (Test-Path -LiteralPath $c) {
                $xelatexPath = $c
                break
            }
        }
    }

    if (-not $xelatexPath) {
        Write-Error "找不到 xelatex.exe。请安装 MiKTeX 或将其路径加入 PATH。"
        return
    }

    Write-Host "`n=== XeLaTeX 编译器 ===" -ForegroundColor Cyan
    Write-Host "  路径: $xelatexPath" -ForegroundColor DarkGray
    Write-Host "  文件: $texFile" -ForegroundColor DarkGray
    Write-Host "  pass数: $(if ($SinglePass) { 1 } else { $MaxRuns })" -ForegroundColor DarkGray

    # 确保 MiKTeX 所在目录在 PATH 中（miktex 运行时需同目录的 DLL）
    $miktexDir = Split-Path -Parent $xelatexPath
    if ($env:PATH -notlike "*$miktexDir*") {
        $env:PATH = "$miktexDir;$env:PATH"
    }

    # ─── 编译函数 ───
    function Invoke-XeLaTeX {
        param([int]$Pass)

        $sw = [System.Diagnostics.Stopwatch]::StartNew()
        Write-Host "`n--- 第 $Pass pass编译 ---" -ForegroundColor Yellow

        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName               = $xelatexPath
        $psi.Arguments              = "-interaction=nonstopmode -file-line-error -synctex=1 $jobName"
        $psi.WorkingDirectory       = $scriptDir
        $psi.UseShellExecute        = $false
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError  = $true
        $psi.CreateNoWindow         = $true

        $process = [System.Diagnostics.Process]::Start($psi)
        $stdout  = $process.StandardOutput.ReadToEnd()
        $stderr  = $process.StandardError.ReadToEnd()
        $process.WaitForExit()
        $sw.Stop()

        # 解析日志
        $errorCount    = ([regex]::Matches($stdout, '(?im)^!')).Count
        $overfullCount = ([regex]::Matches($stdout, '(?i)Overfull')).Count
        $underfullCount = ([regex]::Matches($stdout, '(?i)Underfull')).Count

        $elapsed = '{0:F1}' -f $sw.Elapsed.TotalSeconds
        Write-Host "  耗时: ${elapsed}s | 错误: $errorCount | Overfull: $overfullCount | Underfull: $underfullCount" -ForegroundColor $(
            if ($errorCount -gt 0) { 'Red' } elseif ($overfullCount -gt 0) { 'DarkYellow' } else { 'Green' }
        )

        if ($process.ExitCode -ne 0 -and $errorCount -gt 0) {
            Write-Host "`n  [最后 20 行输出]" -ForegroundColor Red
            $stdout -split "`n" | Select-Object -Last 20 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkRed }
            if ($stderr.Trim()) {
                Write-Host "`n  [stderr 最后 10 行]" -ForegroundColor Red
                $stderr -split "`n" | Select-Object -Last 10 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkRed }
            }
            return $false
        }

        return $true
    }

    # ─── 执行编译 ───
    $totalSw = [System.Diagnostics.Stopwatch]::StartNew()

    $runs = if ($SinglePass) { 1 } else { $MaxRuns }
    for ($i = 1; $i -le $runs; $i++) {
        $ok = Invoke-XeLaTeX -Pass $i
        if (-not $ok) {
            Write-Host "`n编译失败！" -ForegroundColor Red
            return
        }
    }

    # ─── TOC 修复（LaTeX 2025-11-01 内核 bug 导致 .toc 为空）───
    $auxPath   = Join-Path $scriptDir "$jobName.aux"
    $manualToc = Join-Path $scriptDir "$jobName-manual.toc"
    if (-not $SinglePass -and (Test-Path -LiteralPath $auxPath)) {
        $tocEntries = Get-Content -LiteralPath $auxPath -Encoding UTF8 |
            Where-Object { $_ -match '\\@writefile\{toc\}' } |
            ForEach-Object {
                $_ -replace '^\\@writefile\{toc\}', '' `
                   -replace '\s*\\protected@file@percent(?=\s*\})', ''
            }
        if ($tocEntries.Count -gt 0) {
            Write-Host "`n--- TOC 修复：写入 $($tocEntries.Count) 条目录到 manual.toc ---" -ForegroundColor Cyan
            $lines = @('\makeatletter') + $tocEntries + @('\makeatother')
            $lines | Set-Content -LiteralPath $manualToc -Encoding UTF8
            $totalSw.Stop(); $totalSw.Start()
            $ok = Invoke-XeLaTeX -Pass ($runs + 1)
            if (-not $ok) {
                Write-Host "`nTOC 修复编译失败！" -ForegroundColor Red
                return
            }
        }
    }

    $totalSw.Stop()

    # ─── 验证输出 ───
    $pdfPath = Join-Path $scriptDir "$jobName.pdf"
    if (Test-Path -LiteralPath $pdfPath) {
        $pdfInfo = Get-Item -LiteralPath $pdfPath
        $sizeKB  = [math]::Round($pdfInfo.Length / 1KB, 1)
        $totalElapsed = '{0:F1}' -f $totalSw.Elapsed.TotalSeconds
        Write-Host "`n=== 编译成功 ===" -ForegroundColor Green
        Write-Host "  输出: $pdfPath" -ForegroundColor Green
        Write-Host "  大小: ${sizeKB} KB" -ForegroundColor Green
        Write-Host "  总耗时: ${totalElapsed}s" -ForegroundColor Green
    } else {
        Write-Host "`n未生成 PDF 文件！" -ForegroundColor Red
    }

} finally {
    Set-Location $origDir
}
