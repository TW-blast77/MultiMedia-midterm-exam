# coding=utf-8
import cv2
import numpy as np

# 讀取輸入圖片
img = cv2.imread('./road.jpg')
if img is None:
    print("無法讀取圖像")
    exit()

# 將彩色圖片灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用Canny邊緣檢測
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 進行Hough Line直線檢測
lines = cv2.HoughLines(edges, 1, np.pi / 180, 350)

# 遍歷每一條直線
if lines is not None:
    for i in range(len(lines)):
        rho, theta = lines[i][0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        # 繪製直線結果
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 儲存結果
cv2.imwrite('./test3_r.jpg', img)

# 顯示結果
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()