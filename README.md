# C/C++ LaTeX 参考手册合集

本仓库包含 **31 个独立的 LaTeX 子项目**，涵盖 C/C++ 核心主题的参考手册。全部使用 XeLaTeX + ctexbook 排版，共享统一的格式规范和构建脚本。

## 目录结构

```
C、C++/
├── workflow.ps1                  # 统一工作流（编译/清理/状态/打开）
├── README.md                     # 本文件
│
├── algorithm/                    # C++ 算法参考手册
│   ├── algorithm.tex
│   └── build.ps1
├── configure/                    # C++ 构建配置参考手册
│   ├── configure.tex
│   └── build.ps1
├── Contains View Range/          # C++ 容器、视图与范围完全参考
│   ├── containers_views_ranges.tex
│   └── build.ps1
├── CoreBook/                     # C++ 核心指南详解（主文档 + 两个子文件）
│   ├── cpp_core_guidelines_textbook.tex
│   ├── latex_part1.tex
│   ├── latex_part2.tex
│   └── build.ps1
├── CTPR and PImpl/               # C++ CRTP 与 PImpl 惯用法
│   ├── ctpr_and_pimpl.tex
│   └── build.ps1
├── Design Pattern/               # C++ 设计模式与 C# 对比
│   ├── design_patterns.tex
│   └── build.ps1
├── extern C use in other language/ # C/C++ extern C 跨语言集成参考
│   ├── externC.tex
│   └── build.ps1
├── IO/                           # C/C++ 文件、网络与进程间 I/O 参考手册
│   ├── io.tex
│   └── build.ps1
├── memory leak/                  # C/C++ 内存泄漏：检测与防御
│   ├── memory_leak.tex
│   └── build.ps1
├── NewDelete/                    # new/delete 重载与分配器 + 生命周期与指针所有权
│   ├── new_delete.tex
│   └── build.ps1
├── Operator Overloading/         # C++ 运算符重载：原理、实践与跨语言对比
│   ├── operator_overloading.tex
│   └── build.ps1
├── PackageManager/               # C++ 包管理方案对比
│   ├── cpp_package_managers.tex
│   └── build.ps1
├── Reflect/                      # C++ 反射机制全景对比
│   ├── reflection.tex
│   └── build.ps1
├── Script/                       # C/C++ 脚本语言集成对比参考手册
│   ├── scripting.tex
│   └── build.ps1
├── Serialization/                # C++ 序列化方案对比参考手册
│   ├── serialization.tex
│   └── build.ps1
├── SFINAE and Concept/           # C++ SFINAE 与 C++20 约束和概念
│   ├── sfinae_and_concepts.tex
│   └── build.ps1
├── Thread and Coroutine/         # C++ 线程与协程参考手册
│   ├── thread_coroutine.tex
│   └── build.ps1
├── Unit Testing/                 # C++ 单元测试：框架、跨平台、测试边界、依赖注入、Mock 与覆盖率
│   ├── unit_testing.tex
│   └── build.ps1
├── UI Framework/                 # C++ GUI 框架：MFC / WinUI 3 / wxWidgets / Qt / UE
│   ├── ui_framework.tex
│   └── build.ps1
├── ModularBuild/                 # C++ 模块化构建：Modules vs Headers / Clang / LSP / 三方库 / CMake 实战
│   ├── modular_build.tex
│   └── build.ps1
├── C and Cpp Compat/             # C++ 与 C 的不兼容性：VLA / FAM / union UB / 编译器对比 / C23 同步
│   ├── c_cpp_compat.tex
│   └── build.ps1
├── Template Parameters/          # C++20 非类型模板参数扩展：浮点 / 结构化类 / TString / 具名指针
│   ├── template_parameters.tex
│   └── build.ps1
├── Lang History/                 # C/C++ 历史与 ISO/IEC 治理模式：从 Multics 到 C++26、三种治理模式对比
│   ├── c_cpp_history.tex
│   └── build.ps1
├── Asm Embedding/                # 汇编嵌入与 volatile 的真实用途：asm volatile / MSVC intrinsics / 跨语言对比
│   ├── asm_embedding.tex
│   └── build.ps1
├── HW Access and Kernels/        # 硬件访问与 GPU/NPU 核函数：MMIO/PCIe/DMA/中断、I2C·SPI·UART、CUDA/SYCL/NPU
│   ├── hw_kernels.tex
│   └── build.ps1
├── Lang Levels/                  # 抽象层级之争：C/C++ vs Java/C#，机器模型归属、中级语言辨析与选型
│   ├── lang_levels.tex
│   └── build.ps1
├── Cli App/                      # C/C++ 命令行应用：终端模型/参数解析/彩色与 TUI/进程与路径编码/构建分发与测试
│   ├── cli_app.tex
│   └── build.ps1
├── Crypto Database/              # C/C++ 加解密与数据库：与 Java(JCA/JDBC)、C#(Cryptography/ADO.NET) 的抽象差异
│   ├── crypto_database.tex
│   └── build.ps1
├── Parallel Algorithms/          # C/C++ 并行算法：CPU 并行、GPU/NPU 算子、执行域选型与 pybind11 导出
│   ├── parallel_algorithms.tex
│   └── build.ps1
├── Math Geo DSP/                 # 数学·几何·信号处理库：BLAS/Eigen/FFTW/CGAL/GNU Radio/Meep 与 C/C++ 底层成因
│   ├── math_geo_dsp.tex
│   └── build.ps1
└── LSP and Clang Tools/          # 语言服务器与代码质量工具：LSP/clangd/clang-format/clang-tidy/编译数据库与 CI 质量门
    ├── lsp_clang_tools.tex
    └── build.ps1
```

每个子目录的结构一致：一个主 `.tex` 文件 + 一个 `build.ps1` 构建脚本。`CoreBook` 例外，包含主文件和两个 `\input` 子文件。

## 环境要求

- **PowerShell 7+**（构建脚本使用 `#Requires -Version 7.0`）
- **MiKTeX**（XeLaTeX 引擎），自动搜索以下路径：
  - `$PATH` 中的 `xelatex`
  - `D:\winget\MiKTeX\miktex\bin\x64\`
  - `C:\Program Files\MiKTeX\miktex\bin\x64\`
  - `$env:LOCALAPPDATA\Programs\MiKTeX\`
- **DejaVu Sans Mono** 等宽字体 + **Fandol** 中文字体（本地与 CI 同族，否则断行位置不同、Overfull 数对不上）
  - 本地：`mpm --install=dejavu`（MiKTeX 把 TTF 装进 TeX 字体树，不装系统字体）；Fandol 随 MiKTeX 已有
  - CI：apt 的 `fonts-dejavu` 与 `texlive-lang-chinese` 提供同一套字体

## workflow.ps1 使用

`workflow.ps1` 是根目录的统一入口脚本，支持以下命令：

### 编译

```powershell
# 编译全部 31 个项目（每个 2 pass + TOC 修复）
.\workflow.ps1 build-all

# 编译单个项目
.\workflow.ps1 build Algorithm
.\workflow.ps1 build IO
.\workflow.ps1 build CoreBook
```

编译完成后会输出汇总表格，标注每个项目的状态（OK / OVERFULL / FAIL）、错误数、Overfull 数、PDF 大小和耗时。

### 清理

```powershell
# 清理全部项目的辅助文件（.aux, .toc, .log, .out, .idx, .synctex.gz 等）
.\workflow.ps1 clean-all

# 清理单个项目
.\workflow.ps1 clean SFINAE
```

清理操作不会删除 PDF 文件。

### 查看状态

```powershell
.\workflow.ps1 status
```

列出每个项目的 PDF 是否存在、文件大小和最后修改日期。

### 列出项目

```powershell
.\workflow.ps1 list
```

显示全部 31 个项目名及其对应的文件夹路径。

### 打开 PDF

```powershell
.\workflow.ps1 open DesignPat
```

用系统默认 PDF 阅读器打开指定项目的输出文件。如果 PDF 不存在会提示先编译。

### 项目名速查

| 项目名 | 文件夹 | 主题 |
|--------|--------|------|
| SFINAE | SFINAE and Concept | SFINAE 与 C++20 Concepts |
| CRTP | CTPR and PImpl | CRTP 与 PImpl 惯用法 |
| Reflect | Reflect | 反射机制（Boost.PFR → C++26） |
| PkgMgr | PackageManager | 包管理方案对比 |
| MemLeak | memory leak | 内存泄漏检测与防御 |
| CoreBook | CoreBook | C++ 核心指南详解 |
| DesignPat | Design Pattern | 设计模式与 C# 对比 |
| ThreadCo | Thread and Coroutine | 线程与协程 |
| ContView | Contains View Range | 容器、视图与范围 |
| Algorithm | algorithm | 算法参考手册 |
| Configure | configure | 构建配置（CMake/XMake/MSBuild…） |
| Script | Script | 脚本语言集成（Lua/Python/JS…） |
| Serialization | Serialization | 序列化方案对比 |
| IO | IO | 文件/网络/进程间 I/O |
| ExternC | extern C use in other language | extern C 跨语言集成 |
| OpOverload | Operator Overloading | 运算符重载：原理、实践与跨语言对比 |
| NewDelete | NewDelete | new/delete 运算符重载：内存调试、裸机、外设与分配器；生命周期与指针所有权（四种存储期限、分配位置不规定、C# struct/class 堆栈对照、auto_ptr 废弃始末、Qt/UE/Android 指针方言、Rust 借用检查对照） |
| UnitTest | Unit Testing | 单元测试：框架对比、Android/iOS、UE/U++、测试边界、依赖注入、Mock 与覆盖率 |
| UIFwk | UI Framework | GUI 框架：MFC / WinUI 3 (C++/WinRT) / wxWidgets / Qt / UE 对比与迁移 |
| ModularBuild | ModularBuild | 模块化构建：Modules vs Headers / BMI / Clang·LSP·三方库困局 / CMake 实战与渐进迁移 |
| CCompat | C and Cpp Compat | C++ 与 C 不兼容性：VLA / FAM / union 非活跃成员 UB / 编译器矩阵 / C23 同步 |
| TemplateParams | Template Parameters | C++20 NTTP 扩展：浮点 / 结构化类 / TString / 具名指针 / 数学·DSP·序列化实战 |
| History | Lang History | C/C++ 历史与 ISO/IEC 治理：从 Multics 到 C++26 时间线 / WG14·WG21 提案投票流程 / 去中心化 vs 中心化 vs 准中心化客观对比 |
| AsmEmbed | Asm Embedding | 汇编嵌入与 volatile 真实用途：asm volatile / MSVC intrinsics / MMIO·信号·setjmp / FFI 边界 / 四语言 volatile 对比 |
| HWKernels | HW Access and Kernels | 硬件访问与 GPU/NPU 核函数：MMIO/PCIe BAR/DMA 一致性/中断与 MSI-X、I2C·SPI·UART·GPIO、CUDA SIMT·内存层级·流、SYCL oneAPI queue/nd_range/USM、NPU MAC 阵列与 tile；除核函数外区分 Unix/Windows API（含三平台物理地址对比与 libserialport 示例），附录含传感器驱动-HAL-应用全链与 CUDA 算子-PyTorch 绑定 |
| LangLevels | Lang Levels | 抽象层级之争：四层参照模型（机器码/汇编/中级/托管）/ 九维判据逐条核对 / ``C 是中级语言''称呼的来历、构成与三大误读 / 零成本抽象 vs 泛型三路线·RAII vs using·元编程 / L3 向下五级逃生舱与 L2 向上高层设施 / GC·元数据·绑定时机等运行时对照 / 选型决策树与五张场景卡 |
| CliApp | Cli App | C/C++ 命令行应用：TTY/PTY 与 termios vs Windows 控制台/ConPTY / ANSI 与能力探测降级 / getopt·CLI11·cxxopts·argparse 对照与 CLI 设计规范 / 彩色·进度·REPL·ncurses·FTXUI / 子进程管道与信号转发 / 三平台路径·编码与换行 / 配置日志与结构化输出 / 构建静态链接与分发 / CLI 测试与 golden 文件 |
| CryptoDb | Crypto Database | 加解密与数据库：OpenSSL 3.x EVP·libsodium·Botan·CNG 与 JCA/C# Cryptography 抽象层级差 / 算法选型与密钥内存清零 / SQLite·libpq·libpqxx·ODBC·mongocxx 与 JDBC/ADO.NET 对照 / 类型映射·事务并发·SQL 注入·迁移与凭据管理 |
| ParAlgo | Parallel Algorithms | 并行算法：ILP/SIMD/TLP 三种刻度与 roofline / CPU·GPU·NPU 硬件画像 / 执行域选型决策树（MLA·GEMM·attention 类算子上卡，分支密集·指针追逐·复杂控制流留 CPU）/ 线程池·TBB·OpenMP·std::execution·无锁与内存序 / CUDA 归约·scan·tiling·MLA 融合算子与 Ascend C·CANN / 显存搬运与 DLPack / pybind11 导出：GIL 规则·numpy 零拷贝·stub·scikit-build-core·cibuildwheel / 混合执行实战库与对拍基准 |
| MathGDS | Math Geo DSP | 数学·几何·信号处理库：热路径经济学（SIMD·FMA·对齐·无 GC·确定性分配）与 ABI/FFI 四种绑定 / BLAS·LAPACK·Eigen·GSL·Boost.Math·Sundials·Ceres / 几何谓词与鲁棒计算（CGAL·GEOS·PROJ）、网格点云与光线（libigl·Open3D·Embree）、碰撞与刚体 / 声音侧 libsndfile·PortAudio·miniaudio·FFTW·CMSIS-DSP·iir1 / 电磁波侧 FDTD·Meep·openEMS·GNU Radio·SoapySDR·scikit-rf / Python 科学栈的 C/C++ 底层与一条采集-频谱-导出实战链 |
| LSPTools | LSP and Clang Tools | 语言服务器与代码质量工具：clangd·libclang·LSP 三层解剖 / compile_commands.json 的生成与排错（CMake·compiledb·Bear）/ LSP 生命周期与请求-通知模型 / clangd 架构与 .clangd 配置、索引代价 / ccls·cpptools·CDT·Eclipse JDT 对比 / DAP 调试与 CMake Tools 闭环 / clang-format 机制与 .clang-format 逐字段、CI 门禁与增量格式化 / uncrustify·astyle 与"为什么 C/C++ 没有 go fmt" / clang-tidy 架构、checks 族与 .clang-tidy、apply-fixes 与 clang-rename·clang-move / cppcheck·IWYU·Coverity·CodeQL 与 sanitizer 的分界 / CMakePresets+CI 一键质量门与选型排障手册 |

## 统一格式规范

所有项目共享以下排版设置：

| 项目 | 设置 |
|------|------|
| 文档类 | `ctexbook`，12pt，A4，`fontset=fandol` |
| 页边距 | 上下左右各 2.5cm |
| 等宽字体 | DejaVu Sans Mono（`fontspec` + `\IfFontExistsTF` 双分支，家族名命中不到就按 MiKTeX 的 TTF 文件名回落） |
| 代码高亮 | `listings`，`cppstyle` 样式 |
| 提示框 | `tcolorbox`：`note`、`warning`、`guideline`、`compare`、`bestpractice` |
| 页眉 | `fancyhdr`：偶数页左章名，奇数页右节名，外侧页码 |
| 超链接 | `hyperref`，彩色链接 |

## 添加新项目

### 1. 创建文件夹

在根目录下创建新的子文件夹，文件夹名即为项目名：

```powershell
mkdir "E:\C、C++\MyNewTopic"
```

### 2. 创建 .tex 文件

使用以下统一 preamble 模板。将 `my_topic.tex` 放在子文件夹中：

```latex
% !TEX program = xelatex
\documentclass[12pt,a4paper,fontset=fandol]{ctexbook}

% ==================== 页面 ====================
\usepackage[top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm]{geometry}

% ==================== 字体 ====================
\usepackage{fontspec}
\usepackage{iffont}
\IfFontExistsTF{DejaVu Sans Mono}
  {\setmonofont{DejaVu Sans Mono}[Scale=MatchLowercase]}
  {\setmonofont[Extension=.ttf,
      UprightFont=DejaVuSansMono,
      BoldFont=DejaVuSansMono-Bold,
      ItalicFont=DejaVuSansMono-Oblique,
      BoldItalicFont=DejaVuSansMono-BoldOblique]
     {DejaVuSansMono}[Scale=MatchLowercase]}

% ==================== 颜色 ====================
\usepackage{xcolor}
\definecolor{codebg}{HTML}{F5F5F5}
\definecolor{codeframe}{HTML}{E0E0E0}
\definecolor{cppkeyword}{HTML}{1A1AFF}
\definecolor{cppcomment}{HTML}{2E8B2E}
\definecolor{cppstring}{HTML}{B22222}
\definecolor{linenumgray}{HTML}{999999}
\definecolor{algheadbg}{HTML}{1A3C5E}
\definecolor{csharpkeyword}{HTML}{8B008B}
\definecolor{csharptype}{HTML}{006400}
% 如需文档特定的颜色，在此追加 \definecolor{...}

% ==================== listings ====================
\usepackage{listings}

\lstdefinestyle{cppstyle}{
  language=C++,
  basicstyle=\small\ttfamily,
  keywordstyle=\color{cppkeyword}\bfseries,
  commentstyle=\color{cppcomment}\itshape,
  stringstyle=\color{cppstring},
  numberstyle=\tiny\color{linenumgray},
  numbers=left,
  frame=single,
  rulecolor=\color{codeframe},
  framesep=6pt,
  breaklines=true,
  tabsize=4,
  columns=flexible,
  keepspaces=true,
  backgroundcolor=\color{codebg},
  showstringspaces=false,
  morekeywords={constexpr,consteval,constinit,decltype,auto,
    concept,requires,co_await,co_yield,co_return,
    noexcept,override,final,nullptr,static_assert,
    template,typename,namespace,using,mutable,volatile,
    explicit,operator,friend,inline,virtual,
    thread_local,alignas,alignof,if,consteval,constexpr},
  deletekeywords={int,char,bool,float,double,long,short,unsigned,signed,void,wchar_t},
  emph={size_t,int32_t,uint32_t,int64_t,uint64_t,
    string,vector,map,set,unique_ptr,shared_ptr,optional,variant,any,
    span,string_view},
  emphstyle=\color{teal!80!black},
  escapeinside={(*@}{@*)},
}
% 如需文档特定的 listing 语言/样式，在此追加 \lstdefinelanguage / \lstdefinestyle
\lstset{style=cppstyle}

% ==================== tcolorbox ====================
\usepackage[most]{tcolorbox}

\newtcolorbox{guideline}[1][]{
  enhanced,breakable,
  colback=blue!5!white,colframe=blue!75!black,
  fonttitle=\bfseries,title=要点,#1,
  boxed title style={colback=blue!75!black},
  attach boxed title to top left={yshift=-2mm,xshift=2mm},
  arc=2mm,boxrule=0.8mm,
}
\newtcolorbox{compare}[1][]{
  enhanced,breakable,
  colback=green!3!white,colframe=green!50!black,
  fonttitle=\bfseries,title=对比,#1,
  boxed title style={colback=green!50!black},
  attach boxed title to top left={yshift=-2mm,xshift=2mm},
  arc=2mm,boxrule=0.8mm,
}
\newtcolorbox{warning}[1][]{
  enhanced,breakable,
  colback=red!5!white,colframe=red!75!black,
  fonttitle=\bfseries,title=常见陷阱,#1,
  boxed title style={colback=red!75!black},
  attach boxed title to top left={yshift=-2mm,xshift=2mm},
  arc=2mm,boxrule=0.8mm,
}
\newtcolorbox{note}[1][]{
  enhanced,breakable,
  colback=orange!5!white,colframe=orange!80!black,
  fonttitle=\bfseries,title=注意,#1,
  boxed title style={colback=orange!80!black},
  attach boxed title to top left={yshift=-2mm,xshift=2mm},
  arc=2mm,boxrule=0.8mm,
}
\newtcolorbox{bestpractice}[1][]{
  enhanced,breakable,
  colback=purple!5!white,colframe=purple!60!black,
  fonttitle=\bfseries,title=最佳实践,#1,
  boxed title style={colback=purple!60!black},
  attach boxed title to top left={yshift=-2mm,xshift=2mm},
  arc=2mm,boxrule=0.8mm,
}

% ==================== 章节标题 ====================
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{enumitem}
\usepackage{seqsplit}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{algheadbg}}
  {\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{blue!70!black}}
  {\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{blue!60!black}}
  {\thesubsection}{1em}{}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}

\setlist[itemize]{leftmargin=2em,itemsep=2pt}
\setlist[enumerate]{leftmargin=2em,itemsep=2pt}

% ==================== 超链接 ====================
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue!70!black,
  urlcolor=blue!60!black,
  bookmarks=true,
  pdfauthor={Your Name},
  pdftitle={Your Document Title},
}

% ==================== 自定义命令 ====================
\newcommand{\cpp}[1]{C++#1}
\newcommand{\Fn}[1]{\texttt{#1()}}
\newcommand{\Tp}[1]{\texttt{#1}}

% ====================================================================
\begin{document}

\frontmatter

\begin{titlepage}
\centering
\vspace*{4cm}
{\Huge\bfseries Your Title\par}
\vspace{1cm}
{\LARGE Your Subtitle\par}
\vfill
{\large \today\par}
\end{titlepage}

\tableofcontents

\mainmatter

\part{Part Title}
\chapter{Chapter Title}

% 正文内容...

\end{document}
```

### 3. 创建 build.ps1

从任意现有子目录复制 `build.ps1`，修改前两行变量即可：

```powershell
$texFile   = 'my_topic.tex'
$jobName   = 'my_topic'
```

脚本会自动处理 XeLaTeX 路径查找、双 pass 编译、TOC 修复、辅助文件清理等流程。

### 4. 注册到 workflow

打开根目录的 `workflow.ps1`，在 `$projects` 有序字典中添加一行：

```powershell
$projects = [ordered]@{
    # ... 现有项目 ...
    'MyTopic' = @{ dir = 'MyNewTopic'; tex = 'my_topic.tex'; job = 'my_topic' }
}
```

之后即可通过 workflow 管理新项目：

```powershell
.\workflow.ps1 build MyTopic
.\workflow.ps1 status
.\workflow.ps1 open MyTopic
```

### 5. 自定义扩展点

preamble 中标注了 `如需文档特定的...` 的位置，可以在这些位置追加：

- **额外颜色**：如为 C#、Java、Rust 等语言定义标签色
- **额外 listing 语言**：如 `\lstdefinelanguage{CMake}{...}`
- **额外 listing 样式**：如 `\lstdefinestyle{pythonstyle}{...}`
- **额外 tcolorbox**：如复杂度分析框、标准规范框
- **额外自定义命令**：如 `\newcommand{\header}[1]{\texttt{<#1>}}`
- **额外宏包**：如 `tikz`、`makeidx`、`float`

追加内容应放在统一 preamble 的对应区块之后、`\begin{document}` 之前。

## build.ps1 参数说明

每个子目录的 `build.ps1` 支持以下参数：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `-Clean` | switch | false | 删除所有辅助文件，保留 PDF |
| `-SinglePass` | switch | false | 仅编译一遍（快速预览，不生成完整目录） |
| `-MaxRuns` | int | 2 | 最大编译 pass 数 |

```powershell
# 快速预览（单 pass，跳过索引和完整 TOC）
.\build.ps1 -SinglePass

# 3 pass 编译（复杂文档可能需要更多 pass）
.\build.ps1 -MaxRuns 3

# 清理辅助文件
.\build.ps1 -Clean
```

## LaTeX 编写注意事项

- **长内联代码**：使用 `\seqsplit{very_long_identifier}` 避免 overfull hbox
- **lstlisting 转义**：`(*@` 和 `@*` 之间的内容按 LaTeX 解释，注意 `}` 必须在 `@*` 之前闭合
- **tcolorbox 参数**：可选参数使用 key-value 格式 `[title=标题]`，不是 `[标题]`
- **下划线转义**：`\Fn{}`、`\texttt{}` 中的 `_` 必须写成 `\_`
- **`[H]` 浮动体**：需要 `\usepackage{float}`，否则 `[H]` 静默降级为 `[h]`
- **TOC 为空**：LaTeX 2025-11-01 内核存在 bug，build.ps1 已内置修复（从 .aux 提取目录写入 -manual.toc）
