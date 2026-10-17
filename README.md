# C/C++ LaTeX 参考手册合集

本仓库包含 **40 个独立的 LaTeX 子项目**，涵盖 C/C++ 核心主题的参考手册。全部使用 XeLaTeX + ctexbook 排版，共享统一的格式规范和构建脚本。

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
├── Template Parameters/          # C++20 模板参数与泛型机制：NTTP 扩展 / 五语言泛型对照 / 实现收回源文件
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
├── LSP and Clang Tools/          # 语言服务器与代码质量工具：LSP/clangd/clang-format/clang-tidy/编译数据库与 CI 质量门
│   ├── lsp_clang_tools.tex
│   └── build.ps1
├── Simulation and Games/         # 仿真与游戏：Ansys/Abaqus/OpenFOAM 扩展层与 Unreal/Unity/Godot 脚本层的 C/C++
│   ├── simulation_and_games.tex
│   └── build.ps1
├── Audio Video Development/      # 音视频开发：ALSA/WASAPI 设备栈、FFmpeg/x264/Opus 编解码与实时流媒体管线
│   ├── audio_video_development.tex
│   └── build.ps1
├── Rendering and Shaders/        # 渲染与着色器：GPU 绘图管线、GLSL/HLSL/SPIR-V 与 Vulkan/D3D12/Metal 的 C/C++
│   ├── rendering_shaders.tex
│   └── build.ps1
├── Embedded and Realtime/        # 嵌入式与硬实时：启动链与链接脚本、RTOS 调度、中断与确定性 I/O 的 C/C++
│   ├── embedded_realtime.tex
│   └── build.ps1
├── Code Style/                   # 代码风格：主流风格指南对比与谷歌译本滞后条款、inline 与异常的现代语义勘误
│   ├── code_style.tex
│   └── build.ps1
├── Performance and Measurement/  # 性能剖析与测量学：时钟与计数器、统计判据、perf/VTune/Instruments/Tracy 的跨平台实测口径
│   ├── performance_measurement.tex
│   └── build.ps1
├── Undefined Behavior/           # 未定义行为与标准一致性：UB 与实现定义及未指定的分界、生命周期与别名、内存模型、标准库约定
│   ├── undefined_behavior.tex
│   └── build.ps1
├── Compiler and Linker/          # 编译器与链接器：从源码到镜像的流水线、目标文件与链接、加载执行与三平台 ABI
│   ├── compiler_and_linker.tex
│   └── build.ps1
└── Properties and Annotations/   # C++ 属性与 C# 属性、Java 注解：三个同名词三种机制、封闭清单与开放类型、三条扩展方向
    ├── properties_and_annotations.tex
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
# 编译全部 40 个项目（每个 2 pass + TOC 修复）
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

显示全部 40 个项目名及其对应的文件夹路径。

### 打开 PDF

```powershell
.\workflow.ps1 open DesignPat
```

用系统默认 PDF 阅读器打开指定项目的输出文件。如果 PDF 不存在会提示先编译。

### 校验 Pages 首页清单

```powershell
.\workflow.ps1 check
```

校验 `.github/gen_index.py` 与 `.github/copy_pdfs.ps1`：Python 能否解析导入、`PROJECTS` 是否与上面的项目注册表同序同数、`copy_pdfs.ps1` 是否覆盖每一册、以及在临时目录里用占位 PDF 真跑一遍 `main()` 生成 `index.html`（卡片数、链接数、有无未转义的 HTML）。`build-all` 在编译第一个项目之前就会跑这项校验，不通过则整条部署链路直接失败——这两份 Pages 清单历史上被漏改过，而 `build-all` 从不检查它们。新增项目时改完两份清单先跑一次 `check`。

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
| TemplateParams | Template Parameters | C++20 NTTP 扩展：浮点 / 结构化类 / TString / 具名指针 / 数学·DSP·序列化实战；泛型机制对照：Java 擦除 / C# 具化 / Rust 单体化 / C 建议泛型 + 概念·SFINAE 与显式实例化把实现收回源文件 |
| History | Lang History | C/C++ 历史与 ISO/IEC 治理：从 Multics 到 C++26 时间线 / WG14·WG21 提案投票流程 / 去中心化 vs 中心化 vs 准中心化客观对比 |
| AsmEmbed | Asm Embedding | 汇编嵌入与 volatile 真实用途：asm volatile / MSVC intrinsics / MMIO·信号·setjmp / FFI 边界 / 四语言 volatile 对比 |
| HWKernels | HW Access and Kernels | 硬件访问与 GPU/NPU 核函数：MMIO/PCIe BAR/DMA 一致性/中断与 MSI-X、I2C·SPI·UART·GPIO、CUDA SIMT·内存层级·流、SYCL oneAPI queue/nd_range/USM、NPU MAC 阵列与 tile；除核函数外区分 Unix/Windows API（含三平台物理地址对比与 libserialport 示例），附录含传感器驱动-HAL-应用全链与 CUDA 算子-PyTorch 绑定 |
| LangLevels | Lang Levels | 抽象层级之争：四层参照模型（机器码/汇编/中级/托管）/ 九维判据逐条核对 / ``C 是中级语言''称呼的来历、构成与三大误读 / 零成本抽象 vs 泛型三路线·RAII vs using·元编程 / L3 向下五级逃生舱与 L2 向上高层设施 / GC·元数据·绑定时机等运行时对照 / 选型决策树与五张场景卡 |
| CliApp | Cli App | C/C++ 命令行应用：TTY/PTY 与 termios vs Windows 控制台/ConPTY / ANSI 与能力探测降级 / getopt·CLI11·cxxopts·argparse 对照与 CLI 设计规范 / 彩色·进度·REPL·ncurses·FTXUI / 子进程管道与信号转发 / 三平台路径·编码与换行 / 配置日志与结构化输出 / 构建静态链接与分发 / CLI 测试与 golden 文件 |
| CryptoDb | Crypto Database | 加解密与数据库：OpenSSL 3.x EVP·libsodium·Botan·CNG 与 JCA/C# Cryptography 抽象层级差 / 算法选型与密钥内存清零 / SQLite·libpq·libpqxx·ODBC·mongocxx 与 JDBC/ADO.NET 对照 / 类型映射·事务并发·SQL 注入·迁移与凭据管理 |
| ParAlgo | Parallel Algorithms | 并行算法：ILP/SIMD/TLP 三种刻度与 roofline / CPU·GPU·NPU 硬件画像 / 执行域选型决策树（MLA·GEMM·attention 类算子上卡，分支密集·指针追逐·复杂控制流留 CPU）/ 线程池·TBB·OpenMP·std::execution·无锁与内存序 / CUDA 归约·scan·tiling·MLA 融合算子与 Ascend C·CANN / 显存搬运与 DLPack / pybind11 导出：GIL 规则·numpy 零拷贝·stub·scikit-build-core·cibuildwheel / 混合执行实战库与对拍基准 |
| MathGDS | Math Geo DSP | 数学·几何·信号处理库：热路径经济学（SIMD·FMA·对齐·无 GC·确定性分配）与 ABI/FFI 四种绑定 / BLAS·LAPACK·Eigen·GSL·Boost.Math·Sundials·Ceres / 几何谓词与鲁棒计算（CGAL·GEOS·PROJ）、网格点云与光线（libigl·Open3D·Embree）、碰撞与刚体 / 声音侧 libsndfile·PortAudio·miniaudio·FFTW·CMSIS-DSP·iir1 / 电磁波侧 FDTD·Meep·openEMS·GNU Radio·SoapySDR·scikit-rf / Python 科学栈的 C/C++ 底层与一条采集-频谱-导出实战链 |
| LSPTools | LSP and Clang Tools | 语言服务器与代码质量工具：clangd·libclang·LSP 三层解剖 / compile_commands.json 的生成与排错（CMake·compiledb·Bear）/ LSP 生命周期与请求-通知模型 / clangd 架构与 .clangd 配置、索引代价 / ccls·cpptools·CDT·Eclipse JDT 对比 / DAP 调试与 CMake Tools 闭环 / clang-format 机制与 .clang-format 逐字段、CI 门禁与增量格式化 / uncrustify·astyle 与"为什么 C/C++ 没有 go fmt" / clang-tidy 架构、checks 族与 .clang-tidy、apply-fixes 与 clang-rename·clang-move / cppcheck·IWYU·Coverity·CodeQL 与 sanitizer 的分界 / CMakePresets+CI 一键质量门与选型排障手册 |
| SimGame | Simulation and Games | 仿真与游戏引擎的 C/C++ 脚本：非实时求解器与引擎脚本层的扩展方式（Ansys APDL·Workbench 脚本层次与 C/C++ 可介入点 / Fluent UDF 的 C 宏库、DEFINE_* 族与编译/解释加载 / Mechanical 用户材料与 Custom Results、Abaqus UMAT/VUMAT 与 C 混编 / OpenFOAM 求解器、场代数与自定义边界条件 / COMSOL 模型树、Simulink S-Function 与开源求解器的两种改法 / 网格 I/O、区域分解与检查点 / Unreal UHT·UObject、Unity 原生插件与 IL2CPP/Burst、Godot GDExtension / PhysX·Havok·Bullet/Jolt 的 C++ 接口与实时约束 / Lua·sol2·AngelScript 绑定与反射代价 / 硬件在环仿真、确定性时间步与网络同步 / USD·glTF·VTK·CGNS 数据交换 / 选型决策树与排障手册） |
| AvDev | Audio Video Development | 音视频开发的 C/C++：设备与采集栈（ALSA·PipeWire·WASAPI·CoreAudio·JACK·V4L2）/ 采样、时钟漂移与缓冲、jitter buffer / 像素与平面格式（YUV·chroma 次采样·stride 对齐）/ 编码器 C ABI（libavcodec·x264·x265·libaom·SVT-AV1·libvpx·Opus）与码控 CRF·VBV·ABR / 硬件编解码与零拷贝（DXVA2·QSV·VA-API·NVDEC·VideoToolbox）/ 滤镜与音频 DSP 链（libavfilter·libswscale·swresample）/ 封装同步与容错（MP4·MKV·TS 时间基、PTS/DTS·edit list·错误隐藏）/ 流媒体协议（RTMP·SRT·RIST·LL-HLS·CMAF·WebRTC）与无锁实时管线、GStreamer·引擎与 WASM 集成 / 字幕与图文轨（WebVTT·TTML·CEA-608/708·SRT 的表示与时间轴对齐、多语言轨在清单里的挂载）与加密投递（HLS Sample-AES、CENC/CBSC 与 BMFF 保护方案、密钥轮换与授权链路）及 fMP4/CMAF 分片与清单表示 |
| Render | Rendering and Shaders | 渲染与着色器的 C/C++：GPU 绘图管线与光栅化各阶段的可控点 / 着色语言三形态（GLSL·HLSL·MSL）与 SPIR-V 中间表示、glslang·dxc·slang·spirv-cross 编译链 / Vulkan 对象模型、命令缓冲、同步与显式内存绑定 / D3D12 与 Metal 的显式管线差异、OpenGL/EGL 的历史包袱 / PBR 光照、阴影与级联、前向+/延迟渲染、光线追踪（DXR·OptiX）/ 计算着色器与 GPU 驱动管线（culling·粒子·间接绘制）/ 纹理压缩、资源绑定与帧图 / 窗口系统与事件泵（GLFW·SDL·XCB·Wayland·Cocoa·ANativeWindow 的上下文创建、surface 生命周期与 DPI 缩放、跨平台 vsync 与帧节拍）与字形管线（FreeType 光栅与 hinting、HarfBuzz shaping、SDF/位图图集与文本排版）/ RenderDoc·GPU 时间戳与带宽预算 / bgfx·wgpu·Filament 与引擎选型 |
| EmbRt | Embedded and Realtime | 嵌入式与硬实时的 C/C++：启动链与镜像布局（复位向量·Bootloader 交接·链接脚本 SECTIONS·.data/.bss 重定位·构造函数与早期栈堆约束）/ 中断与延迟构成（NVIC·GIC·APIC 优先级分组、中断线程化、响应-入口-服务-唤醒四段分解）/ 时间与计数器（单调时钟、tick 与 tickless、体系结构定时器与 TSC、PTP/gPTP）/ 裸机超循环与表驱动状态机 / RTOS 内核对象与调度（FreeRTOS·Zephyr·RTEMS·VxWorks，任务与栈定形、优先级反转与继承/天花板、静态创建与内存方案）/ 实时 Linux 与用户态硬实时（PREEMPT_RT、SCHED_FIFO/DEADLINE、isolcpus·nohz_full·mlockall 与缺页、cgroup 节流与透明大页）/ 无锁与确定性数据结构（SPSC/MPSC 环形缓冲、序列计数器、固定对象池）/ 实时 I/O 形态（ADC 触发扫描、DMA 双缓冲与循环、CAN/CAN-FD 总线负载、EtherCAT 分布式时钟与 TSN 调度类）/ 可观测性（cyclictest·oslat·ftrace·LTTng·ETM/ITM 与尾延迟统计）/ 失效安全与可靠性（窗口看门狗、超时与降级、ECC 与故障注入、IEC 61508·ISO 26262·DO-178 的可追溯性）/ 平台与工具链选型（MCU/MPU/实时 Linux 边界、CMSIS·HAL·Zephyr devicetree、交叉工具链与 QEMU/Renode·HIL 在环验证） |
| CodeStyle | Code Style | 代码风格参考手册：主流风格指南的谱系与条款解剖（Google·LLVM·Chromium·Mozilla·C++ Core Guidelines·Linux 内核）/ 命名、头文件与 include 秩序、缩进与空白规则的跨风格对比 / clang-format·clang-tidy 与 CI 门禁落地 / 国内谷歌风格译本不更新与错译引发的问题：inline 条款停留在 C with Classes 时代而 C++11/17/23 下 inline 是 ODR 与链接语义而非展开建议（constexpr 隐含 inline、inline 变量、编译期内联由启发式与 LTO 决定）、异常禁令的"代价"误读（表驱动零成本模型下正常路径与上层调用代价可忽略，真实代价在代码体积、二进制大小与实时热路径）、RTTI 与其它失效条目盘点 / 按现代标准重写团队风格手册的方法与决策表 |
| PerfMeas | Performance and Measurement | 性能剖析与测量学参考手册：时钟源与计数器（CLOCK_MONOTONIC·rdtsc·TSC 频率与失步·Windows 高精度计时器·GPU 时钟域）/ 口径定义（墙钟与 CPU 时间、用户与内核时间分账、并发下的占用率歧义、延迟与吞吐的对偶、p50·p99·p999 尾延迟）/ 统计判据（多次运行的分布、置信区间与最小可检出差异、A/B 交替与阶跃偏置、warmup 与稳态、观测者效应）/ 微基准框架 Google Benchmark·hyperfine 与反优化防护（常量折叠、内存屏障、DoNotOptimize）/ 采样剖析 perf record 与调用栈展开（帧指针·DWARF·LBR 的代价与失真）、火焰图与差分火焰图 / PMU 事件计数（cycles·instructions·IPC·cache/TLB miss·TopDown 微架构分层）/ 缓存、分支与指令级归因（局部性对照实验、向量化报告一族、把指标送回代码位置）/ 内存与分配剖析（heaptrack·massif·Callgrind·MTMD·ETW 堆事件）/ I/O 与存储测量（块设备队列深度·页缓存冷热·fio 口径·延迟分账）/ 并发下的测量（伸缩性曲线、伪共享、占用率歧义）/ 编译器与构建口径（-O 级别·-DNDEBUG·LTO·PGO·内联的真实语义）/ 三平台对照（Linux perf·eBPF/BCC，Windows ETW·XPerf·VTune，macOS Instruments·powermetrics）/ GPU 与异构计时（CUDA event 与流同步语义、nsys·Nsight Compute 口径差别）/ 带宽与拓扑（显存·PCIe·NUMA 距离·STREAM 型上限·多卡）/ 连续性能与线上采样（CI 基线门禁、回归检测阈值、生产环境低开销采样预算）/ 测量反模式（口径偷换、归因偷换、不可复现的结论）/ 三张速查附录（三平台工具与权限对照、指标与命令行参数速查、术语与按症状排障手册） |
| UBeh | Undefined Behavior | 未定义行为与标准一致性参考手册：五种行为类别的分界与标准文本读法（良好定义·UB·实现定义·未指定·畸形与不要求诊断，as-if 规则凭什么成立）/ 为什么任何语言都免不了未定义行为（撤回承诺是优化的定价基础，术语条目应该这样查）/ 消毒器与静态分析的口径（UBSan·ASan·MSVC 消毒器与 /analyze·警告档位·静态分析边界）/ 生命周期、对象表示与 trap 表示（存储期·placement new·std::bit_cast·std::start_lifetime_as）/ 指针的合法性（算术·比较·derived pointer·provenance·reinterpret_cast 边界）/ 严格别名与类型双关（char 例外·may_alias·厂商差异）/ 对齐（alignas·alignof·未对齐访问·assume_aligned 与打包陷阱）/ 求值顺序与副作用（sequenced before·函数参数·初始化顺序·重载逗号运算符）/ 整型边界（有符号溢出·除法取余·移位越界·位域与 char 符号性）/ 内存模型与 data race（修改顺序·可见性与顺序保证·volatile 不是同步·memory_order 合法取值）/ 自我移动、noexcept 与 terminate 的边界（部分移动对象·异常路径·unexpected 演化）/ 标准库的前置条件（下标与迭代器失效·算法区间·string_view 悬挂·optional 空访问·assert 与 NDEBUG）/ 实现定义与未指定：可移植边界的写法（去哪里查、怎么固化进 CI）/ 标准库约定（包含模型·特性测试宏·库调试模式·分配器与容器约定·hash 稳定性）/ 前向兼容与缺陷报告回译（语言兼容与 ABI 兼容之别·弃用移除清单）/ 三张速查附录（五种行为类别速查·消毒器与诊断开关对照·常见未定义行为案例与最小复现清单） |
| CompLink | Compiler and Linker | 编译器与链接器参考手册：流水线形状与实现的载体（预处理·语法与语义分析·AST·IR·优化·指令选择·链接，以及语言可自举而实现载体几乎全是 C/C++ 与其他中级语言——GCC 与 Clang 是 C++、CPython 与 MRI 是 C、V8 与 HotSpot 是 C++、Rust 编译器坐在 LLVM 之上）/ 预处理、头文件与模块（宏展开顺序·头文件守卫·Modules 与 BMI）/ 名字解析、重载决议与模板实例化（两阶段查找·依赖名与非依赖名·实例化时机）/ 中间表示与静态单赋值（LLVM IR 与 GIMPLE·phi 与支配树·别名元数据）/ 优化管线、整程序优化与反馈驱动（内联·常量传播·循环变换·向量化·LTO 与 PGO 与 BOLT 的机制侧）/ 指令选择与寄存器分配（DAG 匹配·机器描述·图着色·线性扫描·spill）/ 目标文件与符号表（节与段·重定位类型·ELF 与 PE 与 Mach-O 对照）/ 静态链接（符号解析与链接顺序·弱符号与 COMDAT 与 ODR·段回收与折叠·归档与部分链接）/ 动态链接与加载执行（PIC 与 GOT 与 PLT·延迟绑定·符号插入·dlopen 查找语义·三平台加载器·TLS 模型·ASLR 与 PIE·控制流保护与栈展开表）/ 调用约定：系统 V、MS x86-64、AArch64 与 RISC-V（影子空间·红色区域·可变参数·结构体传递与返回）/ 数据布局：对齐、打包与位域（填充·packed 与 pragma pack 的 ABI 后果）/ 字节序与数据模型（大小端与转换内建·char 符号性·wchar_t 宽度·LLP64 与 LP64）/ C++ ABI：名字修饰、虚表与展开表（vtable 与 RTTI 布局·异常表·noexcept 落地·跨 so 与跨 DLL 稳定性）/ 编辑器与 IDE 如何消费编译器的产物（诊断格式·编译数据库·语言服务器读的到底是哪份产物）/ 端到端演练：从源码到镜像（把一条命令拆开看每步的输入输出）/ 三张速查附录（命令行与产物查看工具速查·三平台两架构的 ABI 速查·主流实现的载体语言与自举关系一览） |
| PropsAnn | Properties and Annotations | C++ 属性与 C# 属性、Java 注解参考手册：三个同名词拆成三种东西（C++ 的 attribute 是贴附在既有语法实体上的修饰 / C# 的 property 是携带访问器的类成员 / C# attribute 与 Java annotation 才是同一类元数据）/ 判据三问（在哪个时机被消费、能否被程序自己读回、认不认识未知条目）/ 三条年代线与 Java 至今没有语言级 property（@Property 一类全部来自库而非语言）/ C++ 方括号属性的语法与 appertains-to 贴附位置、命名空间保留（std 与 std 后跟数字归标准化，其余归实现）因此**截至 C++26 C++ 无用户自定义属性**、未知属性 C++11/14 判畸形而 C++17 起忽略、`__has_cpp_attribute` 与 `__has_include`（C++20）对比实现侧的 `__has_attribute` / 标准属性按版本清单（noreturn·deprecated·fallthrough·maybe_unused·nodiscard 及原因串·likely 与 unlikely·no_unique_address·assume·indeterminate 与结构化绑定上的属性）/ 厂商扩展的边界（GCC 与 Clang 的 `__attribute__`、MSVC 的 `__declspec`，其中 `__declspec(property(get=…, put=…))` 把成员访问在编译期改写成 get/put 调用——C++ 一侧唯一真正的 property 不在标准里）/ C# property 年代线（1.0 访问器·3.0 自动属性·6.0 表达式体与初始化器·9.0 init 与 record 位置式属性·13 partial property·14 的 field 关键字与扩展成员）/ property 的 IL 真身与版本坑（编译成 get_ 与 set_ 两个方法加一条 .property 元数据、编译器另生成私有后备字段，由此带来的反射与序列化错位、跨语言边界只见方法不见字段、哪些改动只是源码级破坏哪些是二进制级破坏）/ C# Attribute（派生 System.Attribute 的类·位置实参即构造参数·命名实参即公开字段与属性·两者都必须编译期常量·AttributeUsage 的三件事·同一个语法位置四种效果的 Conditional 与 DllImport 与 CallerMemberName 与 Obsolete）/ Java 的 @interface（元素写成抽象方法形态可带 default·元素类型集合被限定·@Target 与 @Retention 与 @Inherited 与 @Documented 四个元注解·默认保留策略是 CLASS 即写了反射读不到·@Repeatable 与 TYPE_USE 随 Java 8·javax.annotation.processing 随 Java SE 6）/ “Java 注解源于 C# Attribute”的证据边界（JSR 175 全文不提 C#，同期同形可证实而因果说无一手出处，形状差异反证不是移植）/ 三条扩展方向（C++26 反射 P2996 与 P3394 的匿名 `[[= 表达式 ]]` 注解：可被反射读回的匿名反射常量，不是自定义属性名，也不等于标准属性可被反射；Roslyn 源生成器与 Java 注解处理器的生成期路线及其各自的能力边界；把信息编码进类型而不是标注的替代手法与代价）/ 按“谁在读、什么时候读到”给定的选型决策表与全册反直觉结论（元数据只有在确实存在消费者时才不是装饰，C++ 把清单封死是因为每一条都必须由编译器自己兑现） |

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
