import asyncio
from playwright.async_api import async_playwright
import os
import sys
import json
import csv
import zipfile # Import zipfile
import shutil # Import shutil

async def create_image(title: str, content: str, output_full_path: str):
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

            # Serialize arguments to JSON
            args_json = json.dumps({'title': title, 'content': content})

            # Fill content dynamically using JSON
            await page.evaluate(f"""(argsJson) => {{
                const args = JSON.parse(argsJson);
                document.getElementById('main-title').textContent = args.title;
                document.getElementById('main-content').textContent = args.content;
            }}""", args_json)

            container_div = page.locator('.container')
            await container_div.screenshot(path=output_full_path) # Save to full path

            print(f"✅ 截图已保存为 {output_full_path}")
    finally:
        if browser:
            await browser.close()

async def main():
    input_csv_path = 'input_data.csv'
    output_dir = 'output' # Define output directory
    zip_filename = 'generated_images.zip' # Define zip filename

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_csv_path):
        print(f"❌ 错误：未找到文件 '{input_csv_path}'。请确保CSV文件存在。")
        sys.exit(1)

    tasks = []
    with open(input_csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if len(row) != 2:
                print(f"⚠️ 警告：CSV文件第 {i+1} 行格式不正确，跳过。行内容: {row}")
                continue
            title, content = row
            # Dynamic Naming: Use zero-padded row number
            output_full_path = os.path.join(output_dir, f"image_{i+1:02d}.png")
            tasks.append(create_image(title, content, output_full_path))
    
    if not tasks:
        print("ℹ️ 未在CSV文件中找到有效数据，未生成任何图片。")
        sys.exit(0)

    await asyncio.gather(*tasks) # Run all image generation tasks concurrently

    # Packaging: Create zip file
    if os.path.exists(output_dir) and any(f.endswith('.png') for f in os.listdir(output_dir)):
        print(f"📦 正在打包图片到 {zip_filename}...")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    if file.endswith('.png'):
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, output_dir))
        print(f"✅ 图片已成功打包到 {zip_filename}")
        
        # Cleanup: Delete temporary output folder
        print(f"🗑️ 正在清理临时文件夹 '{output_dir}'...")
        shutil.rmtree(output_dir)
        print(f"✅ 临时文件夹 '{output_dir}' 已删除。")
    else:
        print("ℹ️ 没有找到图片可供打包。")


if __name__ == "__main__":
    asyncio.run(main())
