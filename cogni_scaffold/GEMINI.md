# 项目名称: CogniScaffold

## 核心概念 (Core Concept)

`CogniScaffold` 是我们共同构思并创造的一个原型工具，其核心设计哲学是“认知脚手架” (Cognitive Scaffolding)。

它并非要取代或自动化思考，而是作为一个辅助工具，通过提供结构化的分析框架、模板和建议，来增强和稳定人类在面对复杂问题时的分析与决策能力。它的诞生源于我们关于如何系统化、规模化地应用“思维框架”这一元问题的深度探讨。

该工具以Python包的形式存在，旨在回答那个最关键的问题：“我应该如何思考这个问题？”

## 项目结构与关键文件 (Project Structure & Key Files)

```
/
└── cogni_scaffold/              # 项目根目录, 也是一个Python包
    ├── .venv/                   # Python虚拟环境
    ├── .gitignore               # 指定git忽略的文件(如.venv)
    ├── __init__.py              # 将此目录标记为Python包，并导出主类
    ├── cogni_scaffold.py        # 工具的核心逻辑实现
    ├── knowledge_base.py        # 【关键文件】结构化的思维框架知识库
    ├── main.py                  # 展示库功能的示例脚本
    ├── server.py                # 【新】Flask Web服务器实现
    ├── requirements.txt         # 【新】Python依赖列表
    ├── README.md                # 面向人类开发者的项目说明文档
    └── GEMINI.md                # 本文件, 用于Agent的上下文同步
```

*   **`cogni_scaffold/server.py`**: 一个Flask应用，将`CogniScaffold`的功能通过流式HTTP API暴露出来。
*   **`cogni_scaffold/requirements.txt`**: 定义了运行服务器所需的Python依赖（如Flask）。

... (其他文件描述保持不变) ...

## 如何继续迭代 (How to Continue Iteration)

... (扩充知识库和改进核心逻辑部分保持不变) ...

**3. 测试与验证 (To Test Changes):**

项目现在包含两种工作模式：作为库和作为服务器。

*   **测试库功能:**
    *   **操作:** 从项目根目录(`playgroud`)运行以下命令： `cogni_scaffold/.venv/bin/python -m cogni_scaffold.main`。
    *   **目的:** 这会执行`main.py`脚本，快速验证`CogniScaffold`类的核心方法是否正常。

*   **测试服务器功能:**
    *   **操作:**
        1.  **设置环境 (仅首次需要):** `python3 -m venv cogni_scaffold/.venv` 然后 `cogni_scaffold/.venv/bin/pip install -r cogni_scaffold/requirements.txt`。
        2.  **启动服务器:** 从项目根目录(`playgroud`)运行: `cogni_scaffold/.venv/bin/flask --app cogni_scaffold.server:app run`。
    *   **目的:** 启动一个本地Web服务器(通常在`http://127.0.0.1:5000`)，你可以使用`curl`或其他HTTP客户端来测试流式API端点。

遵循此`GEMINI.md`的指引，任何Agent都能快速理解`CogniScaffold`项目的完整上下文（包括其服务器形态），并在此基础上高效地继续我们的迭代工作。
