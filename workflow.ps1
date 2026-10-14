#Requires -Version 7.0
<#
.SYNOPSIS
    C/C++ LaTeX 参考手册 — 项目工作流
.DESCRIPTION
    统一管理 36 个子项目的编译、清理、状态检查。
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
    'NewDelete'     = @{ dir = 'NewDelete';                     tex = 'new_delete.tex';                     job = 'new_delete' }
    'UnitTest'      = @{ dir = 'Unit Testing';                    tex = 'unit_testing.tex';                     job = 'unit_testing' }
    'UIFwk'         = @{ dir = 'UI Framework';                    tex = 'ui_framework.tex';                     job = 'ui_framework' }
    'ModularBuild'  = @{ dir = 'ModularBuild';                    tex = 'modular_build.tex';                    job = 'modular_build' }
    'CCompat'       = @{ dir = 'C and Cpp Compat';                tex = 'c_cpp_compat.tex';                     job = 'c_cpp_compat' }
    'TemplateParams'= @{ dir = 'Template Parameters';             tex = 'template_parameters.tex';              job = 'template_parameters' }
    'History'       = @{ dir = 'Lang History';                    tex = 'c_cpp_history.tex';                    job = 'c_cpp_history' }
    'AsmEmbed'      = @{ dir = 'Asm Embedding';                   tex = 'asm_embedding.tex';                    job = 'asm_embedding' }
    'HWKernels'     = @{ dir = 'HW Access and Kernels';           tex = 'hw_kernels.tex';                       job = 'hw_kernels' }
    'LangLevels'    = @{ dir = 'Lang Levels';                     tex = 'lang_levels.tex';                      job = 'lang_levels' }
    'CliApp'        = @{ dir = 'Cli App';                         tex = 'cli_app.tex';                          job = 'cli_app' }
    'CryptoDb'      = @{ dir = 'Crypto Database';                 tex = 'crypto_database.tex';                  job = 'crypto_database' }
    'ParAlgo'       = @{ dir = 'Parallel Algorithms';             tex = 'parallel_algorithms.tex';              job = 'parallel_algorithms' }
    'MathGDS'       = @{ dir = 'Math Geo DSP';                    tex = 'math_geo_dsp.tex';                     job = 'math_geo_dsp' }
    'LSPTools'      = @{ dir = 'LSP and Clang Tools';             tex = 'lsp_clang_tools.tex';                  job = 'lsp_clang_tools' }
    'SimGame'       = @{ dir = 'Simulation and Games';            tex = 'simulation_and_games.tex';             job = 'simulation_and_games' }
    'AvDev'         = @{ dir = 'Audio Video Development';         tex = 'audio_video_development.tex';          job = 'audio_video_development' }
    'Render'        = @{ dir = 'Rendering and Shaders';           tex = 'rendering_shaders.tex';                job = 'rendering_shaders' }
    'EmbRt'         = @{ dir = 'Embedded and Realtime';              tex = 'embedded_realtime.tex';              job = 'embedded_realtime' }
    'CodeStyle'     = @{ dir = 'Code Style';                         tex = 'code_style.tex';                     job = 'code_style' }
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

# A tabularx whose column spec has no X cannot stretch: every row then ends as
# "Underfull \hbox (badness 10000) in alignment at lines A--B" and the table ships under-filled.
# Such an environment is a tabular wearing the wrong name, so refuse it before invoking xelatex.
function Find-NoXTabularx {
    param([string]$Text)

    $hits = @()
    $key = '\begin{tabularx}'
    $i = 0
    while ($true) {
        $p = $Text.IndexOf($key, $i, [System.StringComparison]::Ordinal)
        if ($p -lt 0) { break }
        $j = $p + $key.Length
        $specs = @()
        for ($g = 0; $g -lt 2; $g++) {
            while ($j -lt $Text.Length -and $Text[$j] -match '[ \t\r\n]') { $j++ }
            if ($j -ge $Text.Length -or $Text[$j] -ne '{') { $j = -1; break }
            $d = 0; $s = $j
            while ($j -lt $Text.Length) {
                if ($Text[$j] -eq '\') { $j += 2; continue }
                if ($Text[$j] -eq '{') { $d++ }
                elseif ($Text[$j] -eq '}') { $d--; if ($d -eq 0) { break } }
                $j++
            }
            if ($j -ge $Text.Length) { break }
            $specs += $Text.Substring($s + 1, $j - $s - 1)
            $j++
        }
        if ($j -lt 0) { break }
        $i = $j
        if ($specs.Count -lt 2) { continue }
        $bare = [regex]::Replace($specs[1], '[<>@!]\{[^{}]*\}', '')
        $bare = [regex]::Replace($bare, '([pmb])\{[^{}]*\}', '$1')
        if ($bare -cnotmatch 'X') { $hits += ($specs[1] -replace '\s+', ' ') }
    }
    return $hits
}

function Invoke-Build {
    param([string]$Name, [hashtable]$Info)

    $projDir = "$base\$($Info.dir)"
    $buildScript = "$projDir\build.ps1"
    $logPath = Join-Path $projDir ($Info.job + '.log')

    $sep = '=' * 60
    Write-Host "`n$sep" -ForegroundColor Cyan
    Write-Host "  Building: $Name ($($Info.tex))" -ForegroundColor Cyan
    Write-Host "$sep" -ForegroundColor Cyan

    if (-not (Test-Path -LiteralPath $buildScript)) {
        Write-Host "  [MISSING] build.ps1 not found!" -ForegroundColor Red
        return [PSCustomObject]@{ Name=$Name; Status='MISSING'; Errors=-1; PlainErr=0; Overfull=-1; Refs=0; MultDef=0; NotConv=0; Align=0; Pages=-1; SizeKB='?' }
    }

    $srcTex = Join-Path $projDir $Info.tex
    if (Test-Path -LiteralPath $srcTex) {
        $noX = @(Find-NoXTabularx (((Get-Content -LiteralPath $srcTex -Raw -Encoding UTF8) -replace '(?<!\\)%.*', '')))
        if ($noX.Count -gt 0) {
            Write-Host "  [tabularx 无 X 列] $($noX.Count) 处，列声明: $(($noX | ForEach-Object { '|'.$_.'|' }) -join ' ')" -ForegroundColor Red
            return [PSCustomObject]@{ Name=$Name; Status='FAIL'; Errors=0; PlainErr=0; Overfull=-1; Refs=0; MultDef=0; NotConv=0; Align=0; Pages=-1; SizeKB='?' }
        }
    }

    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $args_ = @()
    if ($Pass -ne 2) { $args_ += @('-MaxRuns', $Pass) }
    $output = & pwsh -NoProfile -File $buildScript @args_ 2>&1
    $sw.Stop()
    $elapsed = '{0:F1}' -f $sw.Elapsed.TotalSeconds

    # build.ps1 prints one pass summary per run and, on failure, a raw log tail AFTER the
    # last summary. Scanning only the trailing 15 lines missed the summary and left
    # Err=-1, so take the LAST match over the whole output.
    $fullText = $output | Out-String
    $errors = -1; $overfull = -1; $sizeKB = '?'
    $mErr = [regex]::Matches($fullText, '\u9519\u8bef: (\d+)')
    if ($mErr.Count -gt 0) { $errors = [int]$mErr[$mErr.Count - 1].Groups[1].Value }
    $mOv = [regex]::Matches($fullText, 'Overfull: (\d+)')
    if ($mOv.Count -gt 0) { $overfull = [int]$mOv[$mOv.Count - 1].Groups[1].Value }
    if ($fullText -match '\u5927\u5c0f: ([\d.]+) KB') { $sizeKB = $Matches[1] }

    # xelatex can stop early and still leave a valid PDF behind. Its exit code is the only
    # signal that distinguishes "finished the document" from "ran out of steam", so the
    # per-pass summary from build.ps1 now prints it. -1 = old script that prints nothing.
    $exitCode = -1
    $mExit = [regex]::Matches($fullText, '\u9000\u51fa\u7801: (-?\d+)')
    if ($mExit.Count -gt 0) { $exitCode = [int]$mExit[$mExit.Count - 1].Groups[1].Value }

    # A dangling \ref/\cite only raises "LaTeX Warning: Reference `x' ... undefined",
    # which neither Err nor Ov counts. Scan the log of the LAST pass only: earlier
    # passes legitimately report every cross-reference before the .aux exists.
    # Pages comes from the "Output written on X.pdf (N pages, M bytes)" trailer; -1 means
    # the log holds no such line, i.e. xelatex never reached \end{document}.
    $dangling = 0; $pages = -1
    $plainErr = 0; $multdef = 0; $notConv = 0; $align = 0
    $logRaw = ''
    if (Test-Path -LiteralPath $logPath) {
        $logRaw = Get-Content -LiteralPath $logPath -Raw -Encoding UTF8
        $lastRun = (@($logRaw -split 'This is XeTeX') | Select-Object -Last 1)
        $dangling = ([regex]::Matches($lastRun, '(?:Reference|Citation)[\s\S]{0,40}?undefined')).Count
        # MiKTeX prints "(169 pages)." while TeX Live adds the byte count -> "(154 pages, ...)."
        $mPg = [regex]::Matches($logRaw, 'Output written on .* \((\d+) pages?[,)]')
        if ($mPg.Count -gt 0) { $pages = [int]$mPg[$mPg.Count - 1].Groups[1].Value }
        # build.ps1 counts only the two error shapes it greps for. Under -file-line-error a
        # plain-TeX error prints as "./cli_app.tex:5294: Extra }, or forgotten \endgroup." --
        # no leading "!" and none of its listed keywords -- so it escaped the gate while the run
        # aborted at the 100-error cap and shipped a short PDF. Count those from the log itself.
        # The list must stay a whitelist of error openings: longtable's benign
        # "ignored error: Infinite glue shrinkage" shares this exact prefix shape.
        $plainErr = ([regex]::Matches($lastRun, '(?m)^[^\r\n]*\.(?:tex|sty|cls):\d+:\s*(Extra |Missing |Undefined control sequence|Runaway argument|LaTeX Error|Paragraph ended before|Illegal pream-token|Double space|Limit exceeded|Sorry, but|Bad space factor|That makes 100 errors|Emergency stop)')).Count
        # Two more warnings mean the reference pass never settled: colliding labels break the
        # \ref targets, and "Rerun to get cross-references right" means the shipped pages still
        # disagree with the printed contents. Either one is a misplaced or incomplete TOC online.
        $multdef = ([regex]::Matches($lastRun, 'multiply defined')).Count
        $notConv = ([regex]::Matches($lastRun, 'Label\(s\) may have changed|Rerun to get|There were undefined references')).Count
        # "Underfull \hbox (badness 10000) in alignment at lines A--B" is a *table* report: the
        # counter that only walks "in paragraph at lines" misses the whole class, and an
        # un-stretchable tabularx produces one per row. \s+ so a 79-column log wrap cannot hide it.
        $align = ([regex]::Matches($lastRun, 'in\s+alignment\s+at\s+lines')).Count
    }

    # Completeness probe: TeX writes \newlabel into the .aux as it *reaches* each \label, so
    # a run that stops early leaves the tail unwritten. Directional (aux < tex) on purpose —
    # captions repeated across longtable heads write more \newlabel than \label, which must
    # not read as truncation.
    $unwritten = 0
    $texPath = Join-Path $projDir $Info.tex
    $auxPath = Join-Path $projDir ($Info.job + '.aux')
    if ((Test-Path -LiteralPath $texPath) -and (Test-Path -LiteralPath $auxPath)) {
        $srcText = (Get-Content -LiteralPath $texPath -Raw -Encoding UTF8) -replace '(?<!\\)%.*', ''
        $nLab = ([regex]::Matches($srcText, '\\label\{')).Count
        $nAux = ([regex]::Matches((Get-Content -LiteralPath $auxPath -Raw -Encoding UTF8), '\\newlabel\{')).Count
        if ($nAux -lt $nLab) { $unwritten = $nLab - $nAux }
    }

    $failed = $fullText -match '\u7f16\u8bd1\u5931\u8d25'
    # pages -le 0 = no "Output written" trailer at all, i.e. xelatex never finished the document.
    $status = if ($failed -or $errors -gt 0 -or $exitCode -gt 0 -or $unwritten -gt 0 -or
                 $plainErr -gt 0 -or $multdef -gt 0 -or $notConv -gt 0 -or $align -gt 0 -or $pages -le 0) { 'FAIL' }
              elseif ($overfull -gt 0)       { 'OVERFULL' }
              elseif ($dangling -gt 0)       { 'BADREF' }
              elseif ($errors -eq 0)         { 'OK' }
              else                           { 'UNKNOWN' }

    $color = switch ($status) { 'OK'{'Green'} 'OVERFULL'{'DarkYellow'} 'BADREF'{'DarkYellow'} 'FAIL'{'Red'} default{'Gray'} }
    Write-Host "  [$status] Err=$errors PErr=$plainErr Ov=$overfull Al=$align Ref=$dangling MD=$multdef NC=$notConv Pg=$pages Exit=$exitCode ${sizeKB}KB ${elapsed}s" -ForegroundColor $color
    if ($unwritten -gt 0) {
        Write-Host "  [TRUNCATED] $unwritten label(s) never reached the .aux - the run stopped before \end{document}" -ForegroundColor Red
    }

    if ($status -eq 'FAIL') {
        # build.ps1's own error-context print sits at the failing pass, and the CI log only ever
        # carried the last 45 lines of the whole run -- so a CI-only Err>0 reached the summary with
        # its message truncated away. Scan the captured output for every error shape and print its
        # context first; the tail dump then still shows where the run stopped.
        $allOut = @($fullText -split "`r?`n")
        $shown  = @{}
        $hits   = 0
        for ($k = 0; $k -lt $allOut.Count; $k++) {
            if ($allOut[$k] -match '^![ \t]*[A-Za-z=]' -or
                $allOut[$k] -match '\.(?:tex|sty|cls):\d+:\s*(Extra |Missing |Undefined control sequence|Runaway argument|LaTeX Error|Package .* Error|Paragraph ended before|Emergency stop|You can)') {
                $hits++
                if ($hits -gt 4) { break }
                Write-Host "    ---- error hit $hits (line $k) ----" -ForegroundColor Red
                $from = [Math]::Max(0, $k - 6); $to = [Math]::Min($allOut.Count - 1, $k + 8)
                for ($j = $from; $j -le $to; $j++) {
                    if ($shown.ContainsKey($j)) { continue }
                    $shown[$j] = $true
                    Write-Host ('    ' + $allOut[$j]) -ForegroundColor DarkRed
                }
            }
        }
        if ($hits -eq 0) {
            Write-Host '    ---- no error-shaped line in build.ps1 output (see tail below) ----' -ForegroundColor DarkYellow
        }
        # 45 lines: enough to keep the whole error-context window build.ps1 prints
        # (header + 6 before + hit + 8 after), 15 used to cut off the message head.
        $output | Select-Object -Last 45 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkRed }
        # Exit code 0 with no counted error leaves build.ps1 with nothing to dump; the .log
        # tail is then the only witness of where the document actually stopped.
        if ($unwritten -gt 0 -and $logRaw) {
            Write-Host "    ---- last 45 lines of $(Split-Path -Leaf $logPath) ----" -ForegroundColor Red
            ($logRaw -split "`r?`n") | Select-Object -Last 45 | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkRed }
        }
    }

    return [PSCustomObject]@{ Name=$Name; Status=$status; Errors=$errors; PlainErr=$plainErr; Overfull=$overfull; Align=$align; Refs=$dangling; MultDef=$multdef; NotConv=$notConv; Pages=$pages; SizeKB=$sizeKB }
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
        $warn = @($results | Where-Object { $_.Status -in 'OVERFULL','BADREF' }).Count
        $fail = @($results | Where-Object { $_.Status -eq 'FAIL' }).Count
        $miss = @($results | Where-Object { $_.Status -eq 'MISSING' }).Count

        $sc = if ($fail -gt 0 -or $miss -gt 0) {'Red'} elseif ($warn -gt 0) {'DarkYellow'} else {'Green'}
        Write-Host "  OK: $ok | Warning: $warn | FAIL: $fail | Missing: $miss" -ForegroundColor $sc

        foreach ($r in $results) {
            $c = switch ($r.Status) { 'OK'{'Green'} 'OVERFULL'{'DarkYellow'} 'BADREF'{'DarkYellow'} 'FAIL'{'Red'} default{'Gray'} }
            Write-Host ('  {0,-16} {1,-10} Err={2} PErr={7} Ov={3} Al={10} Ref={4} MD={8} NC={9} Pg={5} {6}KB' -f $r.Name,$r.Status,$r.Errors,$r.Overfull,$r.Refs,$r.Pages,$r.SizeKB,$r.PlainErr,$r.MultDef,$r.NotConv,$r.Align) -ForegroundColor $c
        }

        $tt = '{0:F1}' -f $totalSw.Elapsed.TotalSeconds
        Write-Host "`n  Total: ${tt}s" -ForegroundColor Cyan

        # Anything short of OK must not reach Pages: a FAIL volume still leaves a PDF on disk (a
        # truncated one when xelatex stopped early), and the next steps would copy and publish it
        # while the run looked green. Exit non-zero here so copy_pdfs / upload / deploy are skipped.
        $blocked = @($results | Where-Object { $_.Status -ne 'OK' }).Count
        if ($blocked -gt 0) {
            Write-Host "  BLOCKED: $blocked volume(s) are not OK - deploying nothing to Pages" -ForegroundColor Red
            exit 1
        }
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
