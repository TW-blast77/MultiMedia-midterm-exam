from PIL import Image

def rgb_to_yiq(rgb):
    r, g, b = rgb
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    return y, i, q

def yiq_to_rgb(yiq):
    y, i, q = yiq
    r = y + 0.956 * i + 0.621 * q
    g = y - 0.272 * i - 0.647 * q
    b = y - 1.106 * i + 1.703 * q
    return int(r), int(g), int(b)

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    width, height = image.size
    grayscale_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            y_value, _, _ = rgb_to_yiq(pixel)
            grayscale_pixel = yiq_to_rgb((y_value, 0, 0))
            grayscale_image.putpixel((x, y), grayscale_pixel)

    grayscale_image.save(output_path)

if __name__ == "__main__":
    input_image_path = "./Twitch_0.jpg"

    output_image_path = "./output_image/output.jpg"  # 輸出灰度圖的路徑

    convert_to_grayscale(input_image_path, output_image_path)
    print(f"已將 {input_image_path} 轉換為灰度圖，並保存為 {output_image_path}")
