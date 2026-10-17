#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_index.py — 为 GitHub Pages 生成 index.html 首页
用法: python3 .github/gen_index.py
前提: _site/ 目录下已有编译好的 PDF 文件
"""

import os
import datetime
# `escape`, not `import html`: main() binds a local named html for the rendered page, which would
# shadow a module of that name.
from html import escape

PROJECTS = [
    ("SFINAE",        "sfinae_and_concepts.pdf",
     "SFINAE 与 C++20 Concepts",
     "SFINAE 原理、std::enable_if、C++20 requires 表达式与概念约束完全参考。"),
    ("CRTP",          "ctpr_and_pimpl.pdf",
     "CRTP 与 PImpl 惯用法",
     "奇异递归模板模式的静态多态实现，以及 PImpl 编译防火墙惯用法。"),
    ("Reflect",       "reflection.pdf",
     "C++ 反射机制",
     "C++ 反射技术全景：RTTI、宏模拟、第三方库与 C++26 static reflection 提案。"),
    ("PkgMgr",        "cpp_package_managers.pdf",
     "C++ 包管理方案",
     "vcpkg、Conan、CPM.cmake、xmake 等主流包管理器对比与实战。"),
    ("MemLeak",       "memory_leak.pdf",
     "内存泄漏检测与防御",
     "Valgrind、AddressSanitizer、Visual Studio 诊断工具与 RAII 防御策略。"),
    ("CoreBook",      "cpp_core_guidelines_textbook.pdf",
     "C++ 核心指南详解",
     "C++ Core Guidelines 逐条解读：类型安全、资源管理、并发与错误处理。"),
    ("DesignPat",     "design_patterns.pdf",
     "设计模式 (C++ / C#)",
     "23 种 GoF 设计模式的现代 C++ 实现，附 C# 对照。"),
    ("ThreadCo",      "thread_coroutine.pdf",
     "线程与协程",
     "std::thread、std::jthread、C++20 协程、async/await 与无锁并发。"),
    ("ContView",      "containers_views_ranges.pdf",
     "容器、视图与范围",
     "STL 容器完全参考 + C++20 Ranges / Views / Adaptors 详解。"),
    ("Algorithm",     "algorithm.pdf",
     "算法参考手册",
     "<algorithm> 与 <numeric> 全函数参考：排序、查找、集合运算。"),
    ("Configure",     "configure.pdf",
     "构建配置参考",
     "CMake、Meson、Bazel、Premake 构建系统对比与最佳实践。"),
    ("Script",        "scripting.pdf",
     "脚本语言集成",
     "C/C++ 嵌入 Lua、Python、JavaScript、Tcl 等脚本引擎实战。"),
    ("Serialization", "serialization.pdf",
     "序列化方案对比",
     "Boost.Serialization、Cereal、Protobuf、FlatBuffers、MessagePack 对比。"),
    ("IO",            "io.pdf",
     "文件、网络与 IPC I/O",
     "C/C++ 文件 I/O、Socket 网络编程、管道与共享内存进程间通信。"),
    ("ExternC",       "externC.pdf",
     "extern \"C\" 跨语言集成",
     "C ABI 链接约定、与 Rust/Go/Python/Java/JNI 互操作参考。"),
    ("OpOverload",    "operator_overloading.pdf",
     "运算符重载",
     "运算符代数性质、C++ 可重载/不可重载运算符、C#/Python 跨语言对比。"),
    ("NewDelete",     "new_delete.pdf",
     "new/delete 运算符重载",
     "全局/类级别 operator new 重载、内存调试、裸机、外设分配、CUDA Vector 封装与自定义分配器对比。"),
    ("UnitTest",      "unit_testing.pdf",
     "C++ 单元测试",
     "GTest/Catch2/doctest/Boost.Test/Qt Test 对比，Android/iOS 与 UE/U++ 实践，附 C#/Java 对照、纯函数与测试边界、依赖注入、Mock 与覆盖率。"),
    ("UIFwk",         "ui_framework.pdf",
     "C++ GUI 框架",
     "MFC / WinUI 3 (C++/WinRT) / wxWidgets / Qt (Widgets + Quick) / UE Slate 对比，选型决策与迁移路径。"),
    ("ModularBuild",  "modular_build.pdf",
     "C++ 模块化构建",
     "Modules vs Headers 对比、BMI 编译模型、优势详解、Clang/LSP/三方库三大成熟度困局、CMake FILE_SET CXX_MODULES 实战与渐进迁移路径。"),
    ("CCompat",       "c_cpp_compat.pdf",
     "C++ 与 C 的不兼容性",
     "VLA / 柔性数组成员 / 复合字面量 / union 非活跃成员 UB 等差异详解，MSVC·GCC·Clang·Apple Clang 实测对比，以及 C23 与 C++ 同步进展（bool/nullptr/typeof/constexpr/attributes）。"),
    ("TemplateParams","template_parameters.pdf",
     "C++20 模板参数与泛型机制",
     "从整型白名单到浮点、结构化类、具名指针、TString 编译期字符串：P0732R2 / P1907R1 详解，数学/DSP/物理单位/序列化/具名参数实战，GCC·Clang·MSVC 支持矩阵与陷阱清单；另含泛型机制五语言对照（Java 擦除、C# 具化、Rust 单体化、C 的 _Generic 与宏模板），以及模板实现可见性问题：用概念或 SFINAE 加显式实例化把定义收回源文件。"),
    ("History",       "c_cpp_history.pdf",
     "C/C++ 历史与 ISO/IEC 治理模式",
     "从 Multics 到 C23、从 C with Classes 到 C++26 的完整时间线，ISO/IEC JTC1/SC22 WG14/WG21 治理结构、提案与投票流程详解，以及去中心化治理相较中心化（Java/Oracle）与准中心化（C#/.NET Foundation）模式的优势与代价的客观对比。"),
    ("AsmEmbed",      "asm_embedding.pdf",
     "汇编嵌入与 volatile 的真实用途",
     "GCC/Clang asm volatile 三大保证与操作数约束、MSVC __asm/intrinsics 隐式 volatile 语义、MMIO/信号/setjmp 共享变量、FFI 边界为何不需要 volatile，以及 C/C++·C#·Java·Rust 四种 volatile 语义横向对比。"),
    ("HWKernels",     "hw_kernels.pdf",
     "硬件访问与 GPU/NPU 核函数",
     "MMIO 与 PIO 分层、PCIe BAR/配置空间/mmap、DMA 一致性与描述符环、中断/MSI-X/轮询、I2C·SPI·UART·GPIO 低速总线；CUDA SIMT/内存层级/流与事件、SYCL oneAPI queue/nd_range/buffer-accessor 与 USM、NPU MAC 阵列与 tile 编程。除核函数外各章区分 Unix 与 Windows 两套 API（含裸机/Unix/Windows 直接访问物理地址三路对比与 libserialport 跨平台库示例），附录给出仿传感器驱动-HAL-应用三平台全链与 CUDA 算子到 PyTorch 绑定示例。"),
    ("LangLevels",      "lang_levels.pdf",
     "抽象层级之争：C/C++ vs Java/C#",
     "四层参照模型（机器码/汇编/中级/托管）与九维判据逐条核对，“C 是中级语言”称呼的来历、构成与三大误读；零成本抽象 vs 泛型三路线、RAII vs using、元编程对照；L3 向下五级逃生舱与 L2 向上高层设施；GC·元数据·绑定时机等运行时对照，附选型决策树与五张场景卡。"),
    ("CliApp",          "cli_app.pdf",
     "C/C++ 命令行应用",
     "TTY/PTY 与 termios vs Windows 控制台/ConPTY、ANSI 转义与终端能力探测降级；getopt、CLI11、cxxopts、argparse 对照与 CLI 设计规范；彩色输出、进度指示、REPL、ncurses 与 FTXUI；子进程管道与信号转发；三平台路径·编码·换行差异，配置日志与结构化输出；构建静态链接与分发，CLI 测试与 golden 文件。"),
    ("CryptoDb",        "crypto_database.pdf",
     "加解密与数据库",
     "OpenSSL 3.x EVP、libsodium、Botan、CNG 与 Java JCA、C# Cryptography 的抽象层级差；算法选型与密钥内存清零；SQLite、libpq、libpqxx、ODBC、mongocxx 与 JDBC/ADO.NET 对照；类型映射、事务与并发、SQL 注入、迁移与凭据管理。"),
    ("ParAlgo",         "parallel_algorithms.pdf",
     "C/C++ 并行算法",
     "ILP/SIMD/TLP 三种刻度与 roofline、CPU·GPU·NPU 硬件画像与执行域选型决策树；线程池、TBB、OpenMP、std::execution、无锁与内存序；CUDA 归约/scan/tiling/MLA 融合算子与 Ascend C·CANN、显存搬运与 DLPack；pybind11 导出（GIL 规则、numpy 零拷贝、stub、scikit-build-core、cibuildwheel）与混合执行实战对拍基准。"),
    ("MathGDS",         "math_geo_dsp.pdf",
     "数学·几何·信号处理库",
     "热路径经济学（SIMD·FMA·对齐·无 GC·确定性分配）与 ABI/FFI 四种绑定；BLAS·LAPACK·Eigen·GSL·Boost.Math·Sundials·Ceres；几何谓词与鲁棒计算（CGAL·GEOS·PROJ）、网格点云与光线（libigl·Open3D·Embree）、碰撞与刚体；声音侧 libsndfile·PortAudio·miniaudio·FFTW·CMSIS-DSP，电磁波侧 FDTD·Meep·openEMS·GNU Radio·SoapySDR·scikit-rf；附采集-频谱-导出实战链。"),
    ("LSPTools",        "lsp_clang_tools.pdf",
     "语言服务器与代码质量工具",
     "clangd·libclang·LSP 三层解剖与 compile_commands.json 的生成排错（CMake·compiledb·Bear）；LSP 生命周期与请求-通知模型、.clangd 配置与索引代价、ccls·cpptools·CDT·JDT 对比、DAP 与 CMake Tools 闭环；clang-format 机制与 .clang-format 逐字段、CI 门禁与增量格式化、uncrustify·astyle；clang-tidy 架构与 checks 族、cppcheck·IWYU·Coverity·CodeQL 与 sanitizer 的分界、CMakePresets 一键质量门。"),
    ("SimGame",         "simulation_and_games.pdf",
     "仿真与游戏引擎的 C/C++ 脚本",
     "非实时仿真软件与引擎脚本层的扩展方式：Ansys 的 APDL·Workbench 脚本层次与 C/C++ 可介入点、Fluent UDF 的 C 宏库与 DEFINE_* 族、Mechanical 用户材料与 Custom Results、Abaqus UMAT/VUMAT 与 C 混编、OpenFOAM 求解器与自定义边界条件、网格 I/O 与区域分解；Unreal 的 UHT·UObject 与模块构建、Unity 原生插件与 IL2CPP/Burst、Godot GDExtension、PhysX·Havok·Jolt 的 C++ 接口、Lua·sol2·AngelScript 绑定与反射代价、硬件在环仿真与确定性时间步、USD·glTF·VTK·CGNS 数据交换与选型决策。"),
    ("AvDev",           "audio_video_development.pdf",
     "音视频开发的 C/C++",
     "音频侧的采样与时钟、缓冲与抖动补偿，ALSA·PipeWire·WASAPI·CoreAudio·JACK 与 ASIO 的 C API 边界；视频侧的采集路径与像素格式（V4L2、Media Foundation、SDI、YUV 与 chroma 次采样、stride 对齐）；编解码内核的 C ABI：libavcodec 的帧与包模型、x264/x265/libaom/SVT-AV1/libvpx/Opus 的参数与码控（CQP·CRF·VBV·ABR）、DXVA2/QSV/VA-API/NVDEC/VideoToolbox 硬件解码与零拷贝、libswscale/swresample 与 libavfilter 滤镜图；封装与同步（MP4·MKV·TS 的时间基、PTS/DTS、edit list、丢包与错误隐藏）；实时链路（RTMP·RTSP·SRT·RIST·LL-HLS·CMAF·WebRTC、无锁音频回调与背压丢帧、GStreamer 与引擎/WASM 集成）；投递层的字幕与图文轨（WebVTT·TTML·CEA-608/708·SRT 的表示与时间轴对齐、多语言轨与清单里的 ext-x-media）、加密投递（HLS Sample-AES、CENC/CBSC 与 ISO BMFF 保护方案、密钥轮换与授权链路）和 fMP4/CMAF 分片与清单表示，及选型决策。"),
    ("Render",          "rendering_shaders.pdf",
     "渲染与着色器的 C/C++",
     "GPU 绘图管线的可编程阶段与固定约定：顶点装配、光栅化、深度与混合；着色语言的三种形态 GLSL·HLSL·MSL 与 SPIR-V 中间表示，glslang·glslc·dxc·slang 编译与 spirv-cross·spirv-opt 后处理；Vulkan 的对象模型、命令缓冲、同步原语与显式内存绑定，Direct3D 12 与 Metal 的对应差异，OpenGL/EGL 的历史包袱；渲染算法侧的 PBR 光照、阴影级联、前向+ 与延迟渲染、DXR/OptiX 光线追踪；计算着色器与 GPU 驱动管线（视锥剔除、粒子、间接绘制）、纹理压缩与资源绑定、帧图与多趟渲染；窗口与文字侧的上下文来处（GLFW·SDL·XCB·Wayland·Cocoa·ANativeWindow 的创建与事件泵、surface 生命周期与 DPI 缩放、跨平台 vsync 与帧节拍）以及字形管线（FreeType 光栅与 hinting、HarfBuzz shaping、SDF/位图字形图集与文本排版）；调试与性能（RenderDoc、GPU 时间戳、带宽与显存预算）及 bgfx·wgpu·Filament 与引擎选型。"),
    ("EmbRt",           "embedded_realtime.pdf",
     "嵌入式与硬实时的 C/C++",
     "确定性从何而来：硬实时与软实时、近实时的度量口径（最坏延迟、抖动分布、利用率与 WCET 思路）；启动链与镜像布局（复位向量、Bootloader 交接、链接脚本 SECTIONS、.data 与 .bss 重定位、构造函数与早期栈堆约束）；中断与延迟构成（NVIC·GIC·APIC 的优先级分组、中断线程化、响应到入口到服务到唤醒的四段分解与测量）；时间与计数器（单调时钟、tick 与 tickless、体系结构定时器与 TSC、PTP 与 gPTP）；裸机超循环与表驱动状态机；RTOS 内核对象与调度（FreeRTOS·Zephyr·RTEMS·VxWorks，任务与栈定形、优先级反转与继承/天花板、静态创建与内存方案）；实时 Linux 与用户态硬实时（PREEMPT_RT、SCHED_FIFO 与 DEADLINE、isolcpus·nohz_full·mlockall 与缺页、cgroup 节流与透明大页等破坏确定性的因素）；无锁与确定性数据结构（SPSC/MPSC 环形缓冲、序列计数器、固定对象池）；实时 I/O 形态（ADC 触发扫描、DMA 双缓冲与循环、CAN 与 CAN-FD 总线负载、EtherCAT 分布式时钟与 TSN 调度类）；可观测性（cyclictest·oslat·ftrace·LTTng·ETM/ITM 与尾延迟统计）；失效安全与可靠性（窗口看门狗、超时与降级、ECC 与故障注入、IEC 61508·ISO 26262·DO-178 的可追溯性）；平台与工具链选型（MCU/MPU/实时 Linux 的边界、CMSIS·HAL·Zephyr devicetree、交叉工具链与 QEMU/Renode·HIL 在环验证）及按症状索引的排障手册。"),
    ("CodeStyle",       "code_style.pdf",
     "代码风格与风格指南的 C/C++",
     "风格从哪来：主流风格指南的谱系与条款解剖（Google C++ Style Guide 的命名、头文件与 include 秩序、类与函数规则；LLVM 的 RTTI/异常与 STL 取舍及其对 Chromium、Fuchsia 的分化影响；Mozilla 与 WebKit 的折中；C++ Core Guidelines 与 Linux 内核编码风格的边界）；命名方案、缩进与空白规则、花括号与行宽的跨风格对比；格式化与静态检查的落地（clang-format 的逐字段配置、各风格基线差异、clang-tidy 命名检查与 CI 门禁、pre-commit 与增量格式化）。译本问题专论：国内流传的谷歌中文风格手册不更新与错译引发的问题：inline 条款停留在“C with Classes”时代——C++11 之后 inline 首先是 ODR 与链接语义（多次定义合法、constexpr 函数隐含 inline、C++17 内联变量、头文件里的 inline 不是为了快），“小于 10 行才 inline”的性能理由在现代编译器启发式内联、LTO、PGO/BOLT 面前基本失效；异常条款的代价误读——表驱动零成本模型下未抛出路径与上层调用的代价可忽略，真实代价在代码体积、landing pad 对优化的干扰与实时热路径，而非“throw 慢所以全禁”；RTTI 禁令、auto/lambda/智能指针条款的历史语境与今日上游的演化差异；如何按现代标准重写一份不过时的团队风格手册及跨风格选型决策表。"),
    ("PerfMeas",        "performance_measurement.pdf",
     "性能剖析与测量学的 C/C++",
     "测量先于优化：口径与分界（墙钟与 CPU 时间、多线程下的占用率歧义、延迟与吞吐的对偶、p50 与 p99 及 p999 尾延迟，把更快先变成一个数）；时钟源与计数器（CLOCK_MONOTONIC 与 rdtsc、vDSO 与调用成本、TSC 频率与失步、Windows 高精度计时器、GPU 时钟域）；统计判据（重复与稳态、分布形状与分位数、配对交替与 bootstrap 区间、最小可检出差异、多重比较与选择性报告）；采样剖析 perf record 与三种调用栈展开（帧指针、DWARF、LBR 的代价与失真）、符号与内联折叠、火焰图与差分火焰图；事件计数 PMU 与 TopDown 微架构分层（cycles 与 instructions、IPC 的读法、计数采样与精确采样三种拿数方式、perf stat 与 VTune 及 Instruments 对照）；缓存、分支与指令级归因（把 miss 换算成周期、步长与遍历方向与布局、冲突未命中、branch-miss 的读法、向量化报告一族）；内存与分配器（分配开销的账目怎么分、局部性改造的测量闭环、对象池与 arena、碎片、sanitizer 与跟踪工具自身是测量对象，heaptrack、massif 与 Callgrind、MTMD 与 ETW 堆事件）；I/O 与存储测量（应用到内核到块层到设备的四段延迟分账、页缓存冷热与 drop-caches 与 O-DIRECT、fio 每个参数改的是哪一段账、同步调用与写缓存与写放大）；并发下的测量（占用率歧义、伸缩性曲线与串行比例、伪共享与状态共享的差别、锁原子与内存序的测量面、调度迁移与异步背压）；编译器与构建口径（先把测的是哪个二进制钉死、内联的真实语义、LTO 的跨单元记账、PGO 与 BOLT、自动向量化报告、同机同码为什么给出不同二进制）；GPU 与异构计时（异步执行把计时变成协议问题、CUDA event 的语义与边界、kernel 时间、CPU 与 GPU 时钟域对齐、ROCm 与 oneAPI 及图形侧）；带宽与拓扑（规格上限、平台实测、应用实际三种数、算术强度、PCIe 与主存显存搬运、NUMA 距离矩阵与绑定策略、多卡可达性与争用）；连续性能（CI 上的性能数为什么天然不可信、基线的存法与各自的失效模式、回归判据从分布到三档结论、独占绑定与指纹入库、门禁与功能测试的关系）；生产环境的低开销采样（观测预算是一等指标、手段的层次、常驻剖析器与连续 profile、开销三笔税与占空比、线上采样与告警联动）；测量反模式（微基准反模式与常量折叠、内存屏障、DoNotOptimize 一类的反优化防护、观测者效应、口径偷换、归因偷换、不可复现的结论、怎么写一个能活的结论）；三张速查附录（三平台能力与权限及事件对照、指标字典与命令行参数分组含 Google Benchmark 与 hyperfine 的默认值陷阱、术语缩写与按症状排障手册），及按症状索引的选型与排障手册。"),
    ("UBeh",            "undefined_behavior.pdf",
     "未定义行为与标准一致性的 C/C++",
     "契约在哪里被撤回：为什么任何语言都免不了未定义行为——撤回承诺是编译期优化的定价基础，只有把这类行为排除在外的语言才改付边界检查与规范形态的代价，C 与 C++ 选择把代价转给程序员；五种行为类别的分界与标准文本的读法（良好定义、未定义、实现定义、未指定、畸形，其中畸形再分要求诊断与不要求诊断）；优化器凭什么可以假设你没有未定义行为（as-if 规则、poison 与不可达推理、为什么读一个未初始化变量能让整个循环消失）；取证手段与最小可复现例子（UBSan 与 ASan、MSVC 的消毒器与 /analyze、警告档位、静态分析与消毒器的各自边界）；对象生命周期与对象表示（存储期、构造与析构时机、placement new、trap representation 与 std::bit_cast、std::start_lifetime_as）；指针的合法性（指针算术、比较、derived pointer、指针来源与 provenance、reinterpret_cast 的边界）；严格别名与类型双关（别名规则、char 例外、may_alias、几家厂商实现的差异）；对齐（alignas 与 alignof、未对齐访问、assume_aligned 与 SIMD 填充）；求值顺序与副作用（sequenced before、函数参数、初始化顺序、重载逗号运算符、同一表达式里改两次）；整型的边界（有符号溢出、除法与取余、移位越界、位域与 char 的符号性）；语言设施的未定义面（self-move、部分移动后的对象、noexcept 违约与 terminate、异常与 unexpected 的演化）；并发与内存模型（修改顺序、可见性与顺序保证、data race 的定义与它为什么就是未定义行为、volatile 不是同步、memory_order 的合法取值）；标准库前置条件（容器下标与迭代器失效、算法区间、string_view 悬挂、optional 空访问、assert 与 NDEBUG）；标准库约定（头文件与包含模型、特性测试宏、库实现的调试模式、分配器与容器约定、std::hash 的稳定性、quality implementation）；前向兼容与演化（缺陷报告回译改变了什么、语言兼容与 ABI 兼容之别、弃用与移除清单、为什么以前能跑不是证据）；三张速查附录（语言特性乘以行为类别乘以诊断手段的判定表、标准库前置条件速查、术语缩写与按症状排障手册）。"),
    ("CompLink",        "compiler_and_linker.pdf",
     "编译器与链接器的 C/C++",
     "从源码到镜像的每一步都有产物可查；自举与现实的落差：语言可以自举，实现的载体却几乎都是 C 与 C++ 或其他中级语言——GCC 与 Clang 用 C++ 写成，CPython 与 Ruby MRI 用 C，V8 与 HotSpot 用 C++，Rust 编译器虽用 Rust 写成仍坐在 C++ 的 LLVM 之上，所以读懂这条流水线是几乎所有工具链工作的公共前提；流水线形状（预处理、语法分析、语义分析、AST、中间表示、优化、指令选择、寄存器分配、汇编与链接，每一步单独打印产物也单独有一种坏法）；预处理与包含模型（宏展开顺序、头文件守卫、Modules 与 BMI 换掉了什么）；名字与类型检查（重载决议、模板实例化时机、诊断为什么不可依赖）；中间表示与 SSA（LLVM IR 与 GIMPLE 的形态、phi 与支配树、load 与 store 和别名元数据）；优化 pass（内联、常量传播、循环变换、自动向量化、LTO 与 PGO 与 BOLT 的机制侧，测量口径回指性能剖析册）；指令选择与寻址模式（DAG 匹配、机器描述、合并与强度削弱）；寄存器分配与调度（图着色与线性扫描、spill、调用约定决定可用寄存器）；目标文件与符号表（节与段、重定位类型、符号类型与段标志字段，ELF 与 PE 与 Mach-O 三格式对照）；静态链接（符号解析与链接顺序、弱符号与 COMDAT 与一次定义规则、段回收与相同折叠、归档与部分链接）；动态链接（共享库、位置无关码与 GOT 与 PLT、延迟绑定、符号插入、dlopen 的查找语义）；加载与执行（进程镜像与三平台加载器、TLS 模型、静态初始化与 main 之前、exit 与析构、ASLR 与 PIE、控制流保护与栈展开表）；调用约定的由来（System V AMD64、Microsoft x64、AArch64 AAPCS、RISC-V psABI：影子空间、红色区域、可变参数、结构与联合的传递和返回、寄存器分类）；数据布局与对齐（填充规则、位域、packed 与 pragma pack 的 ABI 后果、跨语言边界的结构体表示）；字节序与字符表示（大小端与字节序转换内建、char 的符号性、wchar_t 与 char16_t 的宽度、long 的 LLP64 与 LP64 与 SIL64 模型）；C++ ABI 的专门面（名字修饰、vtable 与 RTTI 布局、虚调用落地、异常表与展开信息、noexcept 的实现、跨 so 与跨 DLL 的稳定性）；三张速查附录（三平台工具、开关与产物对照，ELF 与 PE 与 Mach-O 的字段与重定位类型对照，按症状排障手册与自检清单）。"),
    ("PropsAnn",        "properties_and_annotations.pdf",
     "C++ 属性与 C# 属性、Java 注解",
     "三个中文同名词底下压着三种不相干的机制，这一册先把它们拆开：C++ 的 attribute 是贴附在既有语法实体上的修饰，不引入新成员；C# 的 property 是一种类成员，携带读写访问器并被编译成方法；只有 C# 的 attribute 与 Java 的 annotation 属于同一类东西（类型化的元数据），它们与 C++ 的 attribute 只是同名。贯穿全册的判据是三问：这条元数据在哪个时机被消费、程序能否把它读回来、系统认不认识未知条目——按这三问，C++ 的属性是一份封闭清单（标准属性加厂商命名空间，任何使用者都不能新增条目），C# 与 Java 的元数据是一个开放类型（谁都能定义新类型，但编译器不兑现任何行为）。硬结论：截至 C++26，C++ 没有用户自定义属性，命名空间 std 以及 std 后跟数字归标准化、其余归实现，未知属性在 C++11 与 14 是畸形程序、从 C++17 起改为忽略；探测靠 __has_cpp_attribute 与 __has_include（两者都是 C++20），厂商的 __attribute__ 与 __declspec 不在该宏覆盖范围内。标准属性按版本清点（noreturn、deprecated、fallthrough 与 maybe_unused 与 nodiscard、likely 与 unlikely 与 no_unique_address 与带原因串的 nodiscard、assume、indeterminate 与结构化绑定上的属性）；C++ 一侧唯一真正与 C# property 同物的东西不在标准里，而是 MSVC 的 __declspec(property)，它把成员访问在编译期改写成 get 与 put 调用。C# 的 property 年代线（1.0 访问器、3.0 自动属性、6.0 表达式体与初始化器、9.0 的 init 与 record 位置式属性、13 的 partial property、14 的 field 关键字与扩展成员）只改书写长度、不改编译产物：property 的真身是两个方法加一条元数据记录，自动属性的后备字段是编译器细节而非语言契约，由此带来反射与序列化的错位、跨语言边界只见方法不见字段、以及哪些改动只是源码级破坏哪些同时破坏二进制兼容。注解侧：C# 的 attribute 是派生自 System.Attribute 的类，位置实参即构造参数、命名实参即公开字段与属性，两者都必须编译期常量，于是它只能被编译期与生成期的工具消费，同一个语法位置上 Conditional、DllImport、CallerMemberName、Obsolete 给出四种截然不同的效果；Java 的 annotation 是特殊的 @interface 声明，元素写成抽象方法形态、类型集合被限定，靠 Target、Retention、Inherited、Documented 四个元注解描述自己，默认保留策略是 CLASS，也就是说写了注解而反射读不到是默认行为而非缺陷。关于 Java 注解源于 C# Attribute 的流行说法：JSR 175 全文不提 C#，可证实的只有两年半的时间差与同形的设计目标，因果句没有一手出处，而两边的形状差异恰好反证它不是移植。三条扩展方向：C++26 的反射（P2996 已采纳，P3394 补上匿名的方括号等号表达式注解，它是可被反射读回的匿名反射常量而不是新的属性名，也不等于标准属性变得可反射）；生成期路线（Roslyn 源生成器与 Java 注解处理器各自能做什么、不能做什么，C++ 侧只有构建期代码生成与 libTooling 插件）；以及把信息编码进类型而不是标注的替代手法与其代价。收尾给一张按谁在读、什么时候读到组织的选型决策表，和全册的反直觉结论：元数据只有在确实存在消费者时才不是装饰，C++ 之所以把清单封死，是因为清单里每一条都必须由编译器自己兑现。"),
]

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>C/C++ LaTeX 参考手册合集</title>
<style>
  :root {{
    --navy: #1E2761;
    --ice:  #CADCFC;
    --accent: #4FC3F7;
    --dark: #151D4A;
    --muted: #8B9DC3;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: "Segoe UI", "Noto Sans SC", system-ui, sans-serif;
    background: var(--dark);
    color: var(--ice);
    min-height: 100vh;
    padding: 2rem 1rem;
  }}
  .container {{ max-width: 960px; margin: 0 auto; }}
  header {{
    text-align: center;
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 2px solid var(--navy);
  }}
  header h1 {{
    font-size: 2rem;
    color: #fff;
    margin-bottom: .4rem;
  }}
  header p {{
    color: var(--muted);
    font-size: .95rem;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.2rem;
  }}
  .card {{
    background: var(--navy);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    transition: transform .15s, box-shadow .15s;
  }}
  .card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 6px 24px rgba(0,0,0,.35);
  }}
  .card h2 {{
    font-size: 1.05rem;
    color: #fff;
    margin-bottom: .35rem;
  }}
  .card .desc {{
    font-size: .85rem;
    color: var(--ice);
    line-height: 1.55;
    margin-bottom: .8rem;
    min-height: 2.8em;
  }}
  .card a {{
    display: inline-block;
    background: var(--accent);
    color: var(--dark);
    font-weight: 600;
    font-size: .85rem;
    padding: .35rem 1rem;
    border-radius: 5px;
    text-decoration: none;
    transition: background .15s;
  }}
  .card a:hover {{ background: #fff; }}
  .badge {{
    display: inline-block;
    background: rgba(255,255,255,.1);
    color: var(--muted);
    font-size: .72rem;
    padding: .15rem .5rem;
    border-radius: 4px;
    margin-bottom: .5rem;
  }}
  footer {{
    text-align: center;
    margin-top: 3rem;
    padding-top: 1.2rem;
    border-top: 1px solid var(--navy);
    color: var(--muted);
    font-size: .8rem;
  }}
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>C/C++ LaTeX 参考手册合集</h1>
    <p>{count} 篇独立手册 &middot; XeLaTeX 排版 &middot; 自动生成 PDF &middot; {date}</p>
  </header>
  <div class="grid">
{cards}
  </div>
  <footer>
    由 GitHub Actions 自动编译部署 &middot; 源码托管于 GitHub
  </footer>
</div>
</body>
</html>
"""

def main():
    cards = []
    for tag, pdf, title, desc in PROJECTS:
        pdf_exists = os.path.isfile(os.path.join("_site", pdf))
        link_html = (
            f'<a href="{escape(pdf, quote=True)}">在线阅读 PDF</a>'
            if pdf_exists
            else '<span style="color:var(--muted);font-size:.85rem;">PDF 编译失败</span>'
        )
        # Card text is data from PROJECTS, and two descriptions name HTML-invisible things
        # ("<algorithm>", "extern \"C\""). Interpolated raw, the browser eats the tag-shaped part.
        cards.append(
            f'    <div class="card">\n'
            f'      <span class="badge">{escape(tag)}</span>\n'
            f'      <h2>{escape(title)}</h2>\n'
            f'      <p class="desc">{escape(desc)}</p>\n'
            f'      {link_html}\n'
            f'    </div>'
        )

    today = datetime.date.today().isoformat()
    html = HTML_TEMPLATE.format(
        count=len(PROJECTS),
        date=today,
        cards="\n".join(cards),
    )

    os.makedirs("_site", exist_ok=True)
    out = os.path.join("_site", "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Generated {out}  ({len(PROJECTS)} projects)")

if __name__ == "__main__":
    main()
