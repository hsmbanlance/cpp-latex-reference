#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_index.py — 为 GitHub Pages 生成 index.html 首页
用法: python3 .github/gen_index.py
前提: _site/ 目录下已有编译好的 PDF 文件
"""

import os
import datetime

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
     "C++20 非类型模板参数扩展",
     "从整型白名单到浮点、结构化类、具名指针、TString 编译期字符串：P0732R2 / P1907R1 详解，数学/DSP/物理单位/序列化/具名参数实战，GCC·Clang·MSVC 支持矩阵与陷阱清单。"),
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
     "风格从哪来：主流风格指南的谱系与条款解剖（Google C++ Style Guide 的命名、头文件与 include 秩序、类与函数规则；LLVM 的 RTTI/异常与 STL 取舍及其对 Chromium、Fuchsia 的分化影响；Mozilla 与 WebKit 的折中；C++ Core Guidelines 与 Linux 内核编码风格的边界）；命名方案、缩进与空白规则、花括号与行宽的跨风格对比；格式化与静态检查的落地（clang-format 的逐字段配置、各风格基线差异、clang-tidy 命名检查与 CI 门禁、pre-commit 与增量格式化）。译本问题专论：国内流传的谷歌中文风格手册不更新与错译引发的问题：inline 条款停留在"C with Classes"时代——C++11 之后 inline 首先是 ODR 与链接语义（多次定义合法、constexpr 函数隐含 inline、C++17 内联变量、头文件里的 inline 不是为了快），"小于 10 行才 inline"的性能理由在现代编译器启发式内联、LTO、PGO/BOLT 面前基本失效；异常条款的代价误读——表驱动零成本模型下未抛出路径与上层调用的代价可忽略，真实代价在代码体积、landing pad 对优化的干扰与实时热路径，而非"throw 慢所以全禁"；RTTI 禁令、auto/lambda/智能指针条款的历史语境与今日上游的演化差异；如何按现代标准重写一份不过时的团队风格手册及跨风格选型决策表。"),
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
            f'<a href="{pdf}">在线阅读 PDF</a>'
            if pdf_exists
            else '<span style="color:var(--muted);font-size:.85rem;">PDF 编译失败</span>'
        )
        cards.append(
            f'    <div class="card">\n'
            f'      <span class="badge">{tag}</span>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="desc">{desc}</p>\n'
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
