import sys
from PIL import Image

def compare_images_pixel_by_pixel(image1_path, image2_path):
    sys.stdout.reconfigure(encoding='utf-8')
    """
    逐像素对比两张图片。
    如果尺寸不同或任何一个像素点颜色不同，则认为图片不匹配。
    """
    try:
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)
    except FileNotFoundError:
        print(f"❌ 测试失败：文件未找到。请检查图片路径是否正确。")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 测试失败：打开图片时发生错误 - {e}")
        sys.exit(1)

    if img1.size != img2.size:
        print(f"❌ 测试失败：图片尺寸不匹配！图片1尺寸: {img1.size}, 图片2尺寸: {img2.size}")
        sys.exit(1)

    width, height = img1.size
    pixels1 = img1.load()
    pixels2 = img2.load()

    for x in range(width):
        for y in range(height):
            if pixels1[x, y] != pixels2[x, y]:
                print(f"❌ 测试失败：图片不匹配！在像素 ({x}, {y}) 处颜色不同。")
                sys.exit(1)

    print("✅ 测试通过：图片完全匹配！")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python test_image_similarity.py <图片1路径> <图片2路径>")
        sys.exit(1)

    image1_path = sys.argv[1]
    image2_path = sys.argv[2]

    compare_images_pixel_by_pixel(image1_path, image2_path)
