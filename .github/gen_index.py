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
