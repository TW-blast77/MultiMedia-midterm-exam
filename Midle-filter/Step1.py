import matplotlib.pyplot as plt
import numpy as np

# 讀取圖片
img = plt.imread("./Lenna123.jpg")

if img is not None:
    img = np.array(img)  # 将图像转换为NumPy数组以进行修改
    rows, cols, chn = img.shape

    # 加雜訊
    for i in range(5000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 1.0  # 设置为白色，可以根据需要调整颜色

    plt.imshow(img)
    plt.title("Noise")
    plt.axis('off')  # 不显示坐标轴

    # 影像保存
    plt.imsave("./output_image/Noise_lenna.jpg", img)

    plt.show()
else:
    print("无法读取图像，请检查文件路径。")
