import cv2
import numpy as np
import os

def load_and_convert_to_gray(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def dct2d(image):
    M, N = image.shape
    dct_image = np.zeros((M, N), dtype=np.float32)
    
    for u in range(M):
        for v in range(N):
            sum_val = 0.0
            for x in range(M):
                for y in range(N):
                    cos_u = np.cos(np.pi * u * (2 * x + 1) / (2 * M))
                    cos_v = np.cos(np.pi * v * (2 * y + 1) / (2 * N))
                    sum_val += image[x, y] * cos_u * cos_v
            
            sum_val *= (2 / np.sqrt(M * N))
            if u == 0:
                sum_val *= 1 / np.sqrt(2)
            if v == 0:
                sum_val *= 1 / np.sqrt(2)
            
            # 规范化DCT结果到0-255范围
            sum_val = max(0, min(255, sum_val))
            
            dct_image[u, v] = sum_val

    return dct_image

if __name__ == "__main__":
    image_path = "./Lenna.jpg"

    gray_image = load_and_convert_to_gray(image_path)
    dct_image = dct2d(gray_image)

    # 保存灰度图像
    cv2.imwrite("gray_lena.jpg", gray_image)

    # 保存DCT图像
    dct_image_normalized = cv2.normalize(dct_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)  # 规范化DCT图像
    cv2.imwrite( "dct_lena.jpg", dct_image_normalized)

    cv2.imshow("Gray Image", gray_image)
    cv2.imshow("DCT Image", dct_image_normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
