# 开发日志 - 自动化图片生成器项目

## 项目概述
本项目旨在开发一个自动化图片生成器，能够根据提供的文本内容（主标题和正文）动态生成图片，并支持批量处理和打包功能。

## 阶段 0: 环境搭建和项目初始化
*   **目标:** 准备开发环境，初始化项目结构。
*   **关键决策:** 确定使用 Python 作为开发语言，Playwright 作为浏览器自动化工具。
*   **挑战与思考:** 确保所有必要的库（如 Pillow, Playwright）都已安装并正常工作。
*   **Git 提交:**
    *   `944d79a - feat: Add initial project files (15 hours ago)`: 初始化项目，添加了基础文件。

## 阶段 1: 分析参考图，并用AI生成了HTML/CSS模板
*   **目标:** 根据参考图片 (`reference-2.jpg`) 分析视觉元素，并生成符合设计规范的 `index.html` 和 `style.css`。
*   **关键决策:**
    *   将 `reference-2.jpg` 作为视觉标准，分析其布局、字体、颜色等。
    *   使用 Markdown 格式生成设计规范 (`rules.md`)。
    *   创建基础 `index.html` 结构和 `style.css` 样式表。
*   **挑战与思考:**
    *   从图片中精确提取像素尺寸、颜色码和字体属性需要细致的视觉分析和经验判断。
    *   `rules.md` 的内容需要不断迭代，以更精确地反映参考图的细节。
    *   在 `style.css` 中，需要平衡设计规范与实际浏览器渲染效果。
*   **Git 提交:**
    *   `2d6aec5 - feat: Analyze target style and create HTML/CSS template (11 hours ago)`: 完成了HTML/CSS模板的初步创建。

## 阶段2: 采用TDD流程，用Python和Playwright编写了核心的图片生成脚本
*   **目标:** 开发一个 Python 脚本 (`generate_image.py`)，能够使用 Playwright 打开 `index.html`，动态填充内容，并截图保存为 `output.png`。
*   **关键决策:**
    *   引入 `test_image_similarity.py` 进行像素级图片对比测试，以验证生成图片的准确性。
    *   使用 Playwright 进行浏览器自动化，确保渲染效果与真实浏览器一致。
    *   将核心逻辑封装在 `create_image` 异步函数中。
*   **挑战与思考:**
    *   **Playwright API 使用:** 学习并正确使用 Playwright 的异步 API，特别是 `page.goto()` 和 `element.screenshot()`。
    *   **文件路径处理:** 在 Windows 环境下，`file://` URL 中的路径斜杠问题 (`\` vs `/`) 导致 `SyntaxError`，需要进行转义处理。
    *   **Unicode 编码问题:** 在 Windows 命令行中，Python 脚本输出 Unicode 字符（如 `✅`, `❌`）导致 `UnicodeEncodeError`，通过 `sys.stdout.reconfigure(encoding='utf-8')` 解决。
    *   **脚本长时间运行:** Playwright 浏览器实例未正确关闭导致脚本挂起，通过 `try...finally` 块确保 `browser.close()` 被调用解决。
    *   **`page.evaluate()` 参数传递:** 初始尝试直接传递 Python 字典给 `page.evaluate()` 导致 `TypeError`，最终通过 `json.dumps` 序列化参数并在 JavaScript 中 `JSON.parse` 解决。
    *   **图片尺寸匹配:** `output.png` 的高度与 `reference-2.jpg` 不匹配，通过调整 `index.html` 内容量（OCR 文本）、`style.css` 中的行高、段落间距、列表项间距以及最终强制 `.container` 高度解决。
    *   **像素级差异:** 即使尺寸匹配，像素 (0, 0) 或 (0, 2) 处的颜色差异仍然存在。通过检查 RGB 值发现 `reference-2.jpg` 在这些位置并非纯白，而是浅灰色。最终与用户沟通，明确不需要像素级完美匹配，而是整体视觉一致。
*   **Git 提交:**
    *   `c7d684d - feat: Implement core image generation script using TDD cycle with AI (8 hours ago)`: 核心图片生成脚本的实现。

## 阶段3: 实现了批量处理CSV文件和打包成ZIP的功能
*   **目标:** 扩展 `generate_image.py`，使其能够从 `input_data.csv` 读取多组数据，批量生成图片，并将所有生成的图片打包成 ZIP 文件。
*   **关键决策:**
    *   使用 Python 内置的 `csv` 模块解析 CSV 文件，确保正确处理包含逗号的文本。
    *   为每张生成的图片动态命名（例如 `image_01.png`），避免文件覆盖。
    *   创建 `output` 文件夹来存放生成的图片，并在完成后清理。
    *   使用 `zipfile` 库将 `output` 文件夹中的图片打包成 `generated_images.zip`。
*   **挑战与思考:**
    *   **异步任务管理:** 使用 `asyncio.gather` 并发运行多个图片生成任务，提高效率。
    *   **文件路径管理:** 确保图片保存到正确的 `output` 文件夹，并在打包时正确处理文件路径。
    *   **清理机制:** 确保 `output` 文件夹在打包完成后被删除。
*   **Git 提交:**
    *   `8357e03 - feat: Implement batch processing from CSV and zip packaging (5 minutes ago)`: 实现了批量处理和打包功能。

---

**总结:**
本项目通过迭代开发和持续测试，成功构建了一个功能强大的自动化图片生成器。在开发过程中，我们不仅实现了核心功能，还解决了多项技术挑战，包括 Playwright 的异步操作、文件路径处理、编码问题以及精确的视觉匹配。最终，脚本能够根据用户提供的文本内容，批量生成符合设计规范的图片，并进行自动化打包。

### 2025-09-25 09:39:38
#### PRD 更新记录
- `prd.md` 已更新。

#### 代码更新记录
- `A`: README.md
- `M`: experience.md
- `D`: gemini.md
- `A`: git_history.txt
- `M`: manual.md
- `A`: prd.md

#### 调试版本记录
- (请在此处手动填写版本信息)

---