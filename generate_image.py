import asyncio
from playwright.async_api import async_playwright
import os
import sys
import json # Import json

async def create_image(title: str, content: str, output_filename: str = 'output.png'):
    sys.stdout.reconfigure(encoding='utf-8')
    browser = None
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            current_dir = os.getcwd()
            html_file_path = os.path.join(current_dir, 'index.html')
            file_url = f'file:///{html_file_path.replace("\\", "/")}'

            await page.goto(file_url)

            # Fill content dynamically
            # Serialize arguments to JSON
            args_json = json.dumps({'title': title, 'content': content})

            # Fill content dynamically using JSON
            await page.evaluate(f"""(argsJson) => {{
                const args = JSON.parse(argsJson);
                document.getElementById('main-title').textContent = args.title;
                document.getElementById('main-content').textContent = args.content;
            }}""", args_json)

            container_div = page.locator('.container')
            await container_div.screenshot(path=output_filename)

            print(f"✅ 截图已保存为 {output_filename}")
    finally:
        if browser:
            await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python generate_image_refactored.py <主标题> <正文内容>")
        sys.exit(1)

    title_arg = sys.argv[1]
    content_arg = sys.argv[2]

    asyncio.run(create_image(title_arg, content_arg))
