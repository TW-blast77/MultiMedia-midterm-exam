import cv2
import numpy as np

def OTSU(img_gray):
    # 初始化變數
    max_g = 0           # 最大的類間變異數
    suitable_th = 0     # 最適合的閾值
    th_begin = 1        # 閾值範圍的起始值
    th_end = 255        # 閾值範圍的結束值

    # 迭代不同的閾值
    for threshold in range(th_begin, th_end):
        bin_img = img_gray > threshold      # 創建二值影像
        bin_img_inv = img_gray <= threshold  # 創建反二值影像
        fore_pix = np.sum(bin_img)           # 前景像素的數量
        back_pix = np.sum(bin_img_inv)       # 背景像素的數量

        # 如果前景或背景像素為0，則退出迴圈
        if fore_pix == 0 or back_pix == 0:
            break

        # 計算前景和背景的權重以及平均值
        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix

        # 計算類間變異數
        g = w0 * w1 * (u0 - u1) * (u0 - u1)

        # 如果類間變異數大於最大值，則更新最大值和閾值
        if g > max_g:
            max_g = g
            suitable_th = threshold

    # 返回最適合的閾值
    return suitable_th

# 使用示例
if __name__ == "__main__":
    # 讀取一張灰階影像
    img = cv2.imread('./ostu2.jpg', cv2.IMREAD_GRAYSCALE)

    # 調用OTSU函式計算閾值
    threshold = OTSU(img)

    # 將閾值應用於影像，將影像轉換為二值影像
    binary_img = (img > threshold).astype(np.uint8) * 255

    # 顯示二值影像
    cv2.imshow("Binary Image", binary_img)
    cv2.imwrite("./output_image/output_image.jpg",binary_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    