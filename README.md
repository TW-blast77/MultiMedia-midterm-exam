# 多媒體期中考

## 請用CMD執行程式

# ----------------分隔線------------------------

# [影像邊緣偵測專案](#影像邊緣偵測專案)

这個GitHub專案包含了三種不同的影像邊緣偵測方法的示例程式碼和輸出結果。您可以在這裡找到如何使用拉普拉斯和Sobel運算子以及Canny邊緣偵測來提取影像的邊緣。
## 環境安裝

在開始使用這個專案之前，您需要安裝一些相依的套件。您可以使用以下指令來安裝所需的相依庫：

```bash
pip install opencv-python numpy matplotlib
```
## 邊緣偵測方法

### 1. 拉普拉斯和Sobel邊緣偵測

- 使用3x3和5x5的拉普拉斯核心進行邊緣偵測。
- 使用Sobel運算子進行邊緣偵測。
- 程式碼範例在 `edge_detection.py` 中。

### 2. Canny邊緣偵測

- 使用Canny邊緣偵測演算法來檢測影像邊緣。
- 程式碼範例在 `canny_edge_detection.py` 中。

## 示範圖片

此專案包含以下示範圖片，您可以使用它們來測試邊緣偵測方法：

- `F-16-image-example-H-0-1-255-512-512_Q320.jpg`
- `F16.jpg`
- `oko.jpg`

## 輸出圖片

邊緣偵測的結果將保存在名為 `Output_img` 的資料夾中。每種邊緣偵測方法的輸出圖片將以相應的檔名保存在此資料夾中。

## 如何使用

1. 安裝所需的相依庫（例如，OpenCV、NumPy、Matplotlib）。
2. 執行 `edge_detection.py` 以執行拉普拉斯和Sobel邊緣偵測。
3. 執行 `canny_edge_detection.py` 以執行Canny邊緣偵測。
4. 輸出的圖片將保存在 `Output_img` 資料夾中。

## 操作程式
要使用這個專案，請按照以下步驟操作：

**1.CD到專案資料夾路徑（建議將資料夾放在桌面）：**
```bash
cd desktop/The-Edge-detection
```
**2.輸入以下指令，然後按下Tab鍵，它將自動完成路徑，您可以選擇要執行的邊緣偵測方法：**

- **使用3x3的拉普拉斯核心進行邊緣偵測：**
```bash
python .\Edge-detection-3x3.py
```
- **使用5x5的拉普拉斯核心進行邊緣偵測：**
```bash
python .\Edge-detection-5x5.py
```
- **使用Canny邊緣偵測方法：**
```bash
python .\Edge-detection-Canny.py
```
**3.按下Enter執行。**

## 作者

[TW-Blast77]
