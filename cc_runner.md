# 产品需求文档 (PRD) - 自动化图片生成器项目

## 1. 项目愿景 (Project Vision)
通过AI协同开发，构建一个高效、可扩展的自动化图片生成解决方案，赋能视觉内容创作与管理。

## 2. 核心考察能力 (Core Competencies)
本次技术笔试重点考察以下三个核心能力：

*   **Vibe Coding (AI协同开发):** 考察开发者与AI工具（如Gemini CLI）高效协作，利用AI进行需求分析、代码生成、调试和优化的能力。
*   **抽象思维 (Abstract Thinking):** 考察开发者将复杂需求抽象为可执行的模块、函数和数据结构的能力，以及对系统架构的宏观把握。
*   **工程化交付 (Engineering Delivery):** 考察开发者遵循软件工程规范，进行模块化设计、自动化测试、版本控制和文档编写，确保项目高质量交付的能力。

## 3. 核心功能需求 (Functional Requirements)

### 输入 (Input)
*   **数据源:** 接收一个名为 `input_data.csv` 的CSV文件作为输入。
*   **CSV格式:** 
    *   无表头。
    *   每行包含两列：`主标题,正文内容`。
    *   支持文本中包含逗号（通过双引号 `"` 包裹字段）。

### 处理 (Processing)
*   **动态内容填充:** 脚本能够读取CSV文件中的每一行数据。
*   **HTML/CSS渲染:** 使用 Playwright 启动无头浏览器，打开 `index.html`。
*   **内容注入:** 将CSV行中的 `主标题` 和 `正文内容` 动态注入到 `index.html` 中对应的 `id="main-title"` 和 `id="main-content"` 元素。
*   **图片生成:** 对渲染后的HTML页面中 `class="container"` 的 `div` 元素进行截图。
*   **批量处理:** 遍历 `input_data.csv` 中的所有行，为每一行数据生成一张独立的图片。
*   **输出目录管理:** 在生成图片前，检查并创建名为 `output` 的临时目录，所有生成的图片都保存到此目录。

### 输出 (Output)
*   **图片文件:** 每张生成的图片以 `image_XX.png` (XX为行号，如 `image_01.png`) 格式命名，并保存到 `output` 目录。
*   **压缩包:** 在所有图片生成完毕后，将 `output` 目录中的所有 `.png` 图片打包成一个名为 `generated_images.zip` 的压缩文件，并存放在项目根目录。
*   **清理:** 打包完成后，自动删除临时的 `output` 目录。

## 4. 技术栈与约束 (Tech Stack & Constraints)

*   **核心技术:** 
    *   **Gemini CLI:** 作为AI协同开发工具。
    *   **Playwright MCP (Microsoft Chromium Project):** 用于浏览器自动化和截图。
    *   **Python:** 作为主要的开发语言，并使用其内置的 `csv`, `json`, `asyncio`, `zipfile`, `os`, `shutil`, `sys` 模块。
    *   **Git:** 用于版本控制。
*   **开发流程要求:** 
    *   **TDD (Test-Driven Development):** 鼓励使用测试驱动开发，确保代码质量和功能正确性（例如，使用 `test_image_similarity.py`）。
    *   **网页枢纽 (Web Hub):** `index.html` 和 `style.css` 作为图片生成的核心模板。
    *   **自动迭代 (Auto-iteration):** 脚本应支持自动化运行，减少人工干预。

## 5. 交付物清单 (Deliverables Checklist)
最终提交到GitHub仓库的文件应包括：

*   [x] `README.md`: 项目说明文件。
*   [x] `manual.md`: 项目操作手册。
*   [x] `prd.md`: 本产品需求文档。
*   [x] `dev_log.md`: 开发日志。
*   [x] `experience_draft.md`: 项目复盘报告草稿。
*   [x] `git_history.txt`: Git 提交历史记录。
*   [x] `input_data.csv`: 示例输入数据文件。
*   [x] `index.html`: 图片生成的基础HTML模板。
*   [x] `style.css`: 控制图片视觉样式的CSS文件。
*   [x] `generate_image.py`: 核心图片生成脚本。
*   [x] `test_image_similarity.py`: 图片相似度测试脚本。
*   [x] `rules.md`: AI分析生成的项目设计规范文档。
*   [ ] `generated_images.zip`: 脚本运行后生成的图片压缩包 (此文件通常不直接提交到Git，但作为产物存在)。
*   [ ] `output/` 文件夹: 临时生成目录 (此目录应在脚本运行后被清理)。

## 6. 高级执行计划 (High-Level Execution Plan)

以下是项目从启动到最终交付的宏观步骤，可作为高级指令集指导开发流程：

1.  **项目启动与环境准备 (Phase 0)**
    *   **cc-runner:** `git clone [仓库地址]`
    *   **cc-runner:** `cd [项目目录]`
    *   **cc-runner:** `pip install playwright pillow`
    *   **cc-runner:** `playwright install`
    *   **cc-runner:** `git init` (如果尚未初始化)
    *   **cc-runner:** `git add .`
    *   **cc-runner:** `git commit -m "feat: Initial project setup and environment"`

2.  **视觉分析与模板生成 (Phase 1)**
    *   **cc-runner:** `gemini prompt "你是一位资深的前端开发和UI分析专家。我将为你提供四张名为'd:\\工作文档\\AI风变\\AI Vibe Coding\\Vibe_coding_project\\vibe_coding_task\\reference-2.jpg'的图片。你的任务是精确分析它的所有视觉元素（布局、字体、颜色），并为我创建一个详细的设计规范文档。请生成这个文档的内容，格式为Markdown，并直接用于填充'rules.md'文件。内容需要包含'画布'、'字体样式'和'布局'等部分。请尽可能精确地提供像素尺寸(px)、字重(如 bold, normal)和十六进制颜色码(如 #FFFFFF)等数值。" d:\\工作文档\\AI风变\\AI Vibe Coding\\Vibe_coding_project\\vibe_coding_task\\reference-2.jpg > rules.md`
    *   **cc-runner:** `gemini prompt "请根据你刚才在'rules.md'文件中创建的设计规范，为我生成'index.html'文件的内容。HTML结构要保持简洁：一个主容器div，内部包含一个id为'main-title'的h1标签和一个id为'main-content'的p标签。为标题和内容使用合适的占位符文本，并确保链接到一个名为'style.css'的样式表文件。" rules.md > index.html`
    *   **cc-runner:** `gemini prompt "非常好。现在，请基于同一个'rules.md'文件中的规范，为我生成'style.css'文件的完整CSS内容。请确保你的CSS选择器能够正确地指向'.container', '#main-title', 和 '#main-content'这些元素，并精确地应用所有关于画布、字体和布局的规则。" rules.md > style.css`
    *   **cc-runner:** `git add .`
    *   **cc-runner:** `git commit -m "feat: Analyze target style and create HTML/CSS template"`

3.  **核心图片生成脚本开发 (Phase 2 - TDD 实践)**
    *   **cc-runner:** `gemini prompt "你是一名资深的软件测试工程师。请为我编写一个Python脚本，名为'test_image_similarity.py'。这个脚本需要具备以下功能：..." > test_image_similarity.py`
    *   **cc-runner:** `gemini prompt "你是一名熟悉Playwright MCP的自动化专家。请为我编写一个Python脚本，名为'generate_image.py'。这个脚本的功能是：..." > generate_image.py`
    *   **cc-runner:** `python generate_image.py "测试标题" "测试内容"` (首次运行，预期失败，进行调试)
    *   **cc-runner:** `python test_image_similarity.py reference-2.jpg output.png` (运行测试，预期失败，进行调试)
    *   **cc-runner:** (根据测试反馈，迭代修改 `style.css` 和 `generate_image.py`，重复 `python generate_image.py` 和 `python test_image_similarity.py` 直到视觉一致)
    *   **cc-runner:** `git add .`
    *   **cc-runner:** `git commit -m "feat: Implement core image generation script using TDD cycle with AI"`

4.  **批量处理与打包功能增强 (Phase 3)**
    *   **cc-runner:** `gemini prompt 'gemini cli 把下面的内容生成文档input_data.csv 内容如下：{"AI编程新范式","Vibe Coding引领开发者进入与AI深度协作的新时代，效率与创造力得到极大提升。" ...}' > input_data.csv`
    *   **cc-runner:** `gemini prompt "你是一位精通Python文件处理和代码重构的专家。请帮我升级'generate_image.py'脚本。当前脚本...请提供升级后的完整'generate_image.py'代码。" generate_image.py > generate_image_batch.py`
    *   **cc-runner:** `python generate_image_batch.py` (运行，预期成功生成多张图片和zip文件)
    *   **cc-runner:** `del generate_image.py` (删除旧脚本)
    *   **cc-runner:** `ren generate_image_batch.py generate_image.py` (重命名新脚本)
    *   **cc-runner:** `git add .`
    *   **cc-runner:** `git commit -m "feat: Implement batch processing from CSV and zip packaging"`

5.  **文档完善与最终交付**
    *   **cc-runner:** `gemini prompt "Gemini CLI，在已经完成的任务中，请将你的每一个步骤和思考过程都记录到dev_log.md文件里"` (生成 `dev_log_draft.md`)
    *   **cc-runner:** (将 `dev_log_draft.md` 内容更新到 `dev_log.md`)
    *   **cc-runner:** `gemini prompt "你是一名项目经理，擅长撰写开发日志。我现在正在为我的'自动化图片生成器'项目补写开发日志'dev_log.md'。..." git_history.txt > dev_log_draft.md`
    *   **cc-runner:** `gemini prompt "你是一位经验丰富的技术教练和复盘专家。请仔细通读我提供的这份开发日志'dev_log.md'。..." dev_log.md > experience_draft.md`
    *   **cc-runner:** `gemini prompt "你是一名专业的技术文档工程师，非常擅长编写清晰易懂的用户手册。请为我的'自动化图片生成器'项目编写一份操作手册'manual.md'。..." > manual.md`
    *   **cc-runner:** `gemini prompt "你是一位顶级的AI项目产品经理和解决方案架构师。我已经将一份技术笔试的所有要求都以图片形式提供给你了。..." page-*.png > prd.md`
    *   **cc-runner:** `gemini prompt "你是一名优秀的开源项目布道师，擅长编写引人注目的README文件。请为我的'自动化图片生成器'项目重写'README.md'文件。..." > README.md`
    *   **cc-runner:** `git add .`
    *   **cc-runner:** `git commit -m "docs: Finalize project documentation and deliverables"`
    *   **cc-runner:** `git push`