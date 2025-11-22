# 项目名称: CogniScaffold

## 核心概念 (Core Concept)

`CogniScaffold` 是我们共同构思并创造的一个原型工具，其核心设计哲学是“认知脚手架” (Cognitive Scaffolding)。

它并非要取代或自动化思考，而是作为一个辅助工具，通过提供结构化的分析框架、模板和建议，来增强和稳定人类在面对复杂问题时的分析与决策能力。它的诞生源于我们关于如何系统化、规模化地应用“思维框架”这一元问题的深度探讨。

该工具以Python包的形式存在，旨在回答那个最关键的问题：“我应该如何思考这个问题？”

## 项目结构与关键文件 (Project Structure & Key Files)

```
/
└── cogni_scaffold/              # 项目根目录, 也是一个Python包
    ├── __init__.py              # 将此目录标记为Python包，并导出主类
    ├── cogni_scaffold.py        # 工具的核心逻辑实现
    ├── knowledge_base.py        # 【关键文件】结构化的思维框架知识库
    ├── main.py                  # 展示如何使用CogniScaffold的示例脚本
    ├── README.md                # 面向人类开发者的项目说明文档
    └── GEMINI.md                # 本文件, 用于Agent的上下文同步
```

*   **`cogni_scaffold/knowledge_base.py`**: **这是项目的心脏。** 所有的分析框架（名称、描述、关键词、模板）都以一个名为`FRAMEWORK_KNOWLEDGE_BASE`的Python字典形式存储在此。**对框架的任何添加、删除或修改，都应直接操作此文件。**

*   **`cogni_scaffold/cogni_scaffold.py`**: 包含了名为`CogniScaffold`的主类，实现了工具的API。
    *   `search(keyword)`: 基于关键词在知识库中进行匹配搜索。
    *   `get_template(name)`: 获取指定框架的Markdown模板。
    *   `suggest(problem_description)`: 基于一个初步的、加权的关键词匹配算法，为问题描述推荐框架。

*   **`cogni_scaffold/main.py`**: 一个用于快速验证工具核心功能的示例脚本。

*   **`README.md`**: 项目的公开“门面”，解释了其理念和基本用法。

## 如何继续迭代 (How to Continue Iteration)

为了在未来的会话中继续改进`CogniScaffold`，请遵循以下路径：

**1. 扩充框架知识库 (To Add/Modify Frameworks):**

*   **目标文件:** `cogni_scaffold/knowledge_base.py`。
*   **操作:** 要添加新的框架，只需模仿现有条目的格式，在`FRAMEWORK_KNOWLEDGE_BASE`字典中添加一个新的键值对。请确保包含`name`, `aliases`, `description`, `use_case`, `keywords`, 和 `template`。
*   **建议工具:** 使用 `read_file` 读取现有内容，然后使用 `replace` 工具插入新内容。

**2. 改进核心逻辑 (To Improve Logic):**

*   **目标文件:** `cogni_scaffold/cogni_scaffold.py`。
*   **主要改进方向:** 当前的 `suggest()` 方法非常初级。未来的迭代可以聚焦于此，例如：
    *   引入更复杂的自然语言处理（NLP）技术，如词嵌入（Word Embeddings）或语义相似度计算，以实现更智能的推荐。
    *   允许 `suggest()` 方法结合多个框架，形成一个“分析流”。

**3. 测试与验证 (To Test Changes):**

*   在对代码或知识库进行任何修改后，**请务必运行 `main.py` 脚本进行验证**。
*   **操作:** 从项目根目录(`playgroud`)运行以下命令： `python3 -m cogni_scaffold.main`。
*   **目的:** `-m`标志让Python将包作为一个模块来执行，这能确保脚本内的相对导入正确工作。这是一个快速的健全性检查（Sanity Check），确保核心功能没有因为修改而损坏。

遵循此`GEMINI.md`的指引，任何Agent都能快速理解`CogniScaffold`项目的上下文和状态，并在此基础上高效地继续我们的迭代工作。
