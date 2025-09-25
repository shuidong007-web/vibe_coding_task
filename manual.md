# 自动化图片生成器 - 操作手册

## 1. 项目简介
本项目是一个自动化工具，能够根据CSV文件提供的标题和内容，批量生成带有自定义文本的图片，并将所有生成的图片打包成ZIP文件。

## 2. 环境要求
运行此项目需要以下软件和Python库：

*   **Python 3.8+:** 推荐从 [Python 官方网站](https://www.python.org/downloads/) 下载安装。
*   **Git:** 用于版本控制，推荐从 [Git 官方网站](https://git-scm.com/downloads) 下载安装。
*   **Gemini CLI (或集成开发环境):** 本项目开发过程中使用了 Gemini CLI 作为AI协同开发工具。如果您希望在开发过程中获得AI协助，请确保您的开发环境已配置好Gemini CLI或相应的AI集成。具体安装和配置请参考您所使用的Gemini CLI或IDE插件的官方文档。

**注意:** 为了便于管理和保持一致性，建议您在注册 Git、GitHub 和 Gemini CLI 时使用相同的邮箱地址。
*   **Playwright:** 浏览器自动化工具。
*   **Pillow:** Python图像处理库。

**安装命令:**
首先，确保您已安装 Python 和 Git。然后，打开命令行工具（如 PowerShell, CMD 或 Git Bash），执行以下命令安装所需的 Python 库：

```bash
pip install playwright pillow
playwright install
```
`playwright install` 命令将安装 Playwright 所需的浏览器驱动（如 Chromium）。

## 3. 配置步骤
本项目通过读取 `input_data.csv` 文件来获取生成图片所需的数据。请确保 `input_data.csv` 文件位于项目根目录，并遵循以下格式要求：

*   **文件格式:** CSV (Comma Separated Values)
*   **编码:** UTF-8
*   **表头:** 不包含表头
*   **每行内容:** 包含两列，用逗号 `,` 分隔。
    *   第一列: `主标题` (将填充到 `index.html` 中 `id="main-title"` 的元素)
    *   第二列: `正文内容` (将填充到 `index.html` 中 `id="main-content"` 的元素)
*   **特殊字符处理:** 如果主标题或正文内容中包含逗号，请使用双引号 `"` 将该字段括起来。

**`input_data.csv` 示例:**
```csv
"AI编程新范式","Vibe Coding引领开发者进入与AI深度协作的新时代，效率与创造力得到极大提升。"
"Modulon Labs招募","我们正在寻找热爱技术、勇于探索的你，共同定义下一个AI原生开发时代。"
"自动化解放生产力","从繁琐的重复劳动中解放出来，专注于更有价值的创造性工作，这就是自动化的魅力。"
```

## 4. 运行指南
在完成环境配置和 `input_data.csv` 文件准备后，打开命令行工具，切换到项目根目录，然后执行以下命令即可运行项目：

```bash
python generate_image.py
```

脚本将自动读取 `input_data.csv`，为每一行数据生成图片，并进行打包。

## 5. 产物说明
脚本成功运行后，您将在项目根目录找到一个名为 `generated_images.zip` 的压缩文件。

这个ZIP文件包含了所有根据 `input_data.csv` 生成的图片。每张图片都以 `image_XX.png` 的格式命名（例如 `image_01.png`, `image_02.png`），其中 `XX` 是对应的行号。
