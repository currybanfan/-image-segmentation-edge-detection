---
title: Image Segmentation Edge Detection
emoji: 🌌
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.6.0
app_file: app.py
---

## 電腦視覺應用專案

此專案是一個基於 Gradio 的電腦視覺應用，提供了多種圖片處理功能，包括邊緣檢測、影像分割、二值化處理、模糊效果和銳化效果。使用者可以上傳自己的圖片或選擇範例圖片進行處理，直觀地查看不同圖像處理技術的效果。

### 功能介紹

1. **邊緣檢測：**

    透過 OpenCV 的 Canny 邊緣檢測算法，根據設定的兩個閾值來檢測圖像邊緣。

    輸入參數：

    - 邊緣檢測閾值 1：設定低閾值 (0 ~ 255)。
    - 邊緣檢測閾值 2：設定高閾值 (0 ~ 255)。

    輸出：包含邊緣的黑白圖像。

2. **影像分割：**

    使用 SLIC 將圖像分割為多個區域。

    輸入參數：

    - 分割區域數量：設定分割區塊數量 (100 ~ 1000)。
    - 分割緊湊性：設定區塊形狀的緊湊程度 (1 ~ 50)。

    輸出：顯示分割後的平均區域顏色。

3. **圖像二值化：**

    將圖像轉為灰階後，根據設定的閾值進行二值化處理。

    輸入參數：

    - 二值化閾值：設定二值化的閾值 (0 ~ 255)。

    輸出：黑白二值化圖像。

4. **模糊：**

    透過高斯模糊進行圖像平滑處理。

    輸入參數：

    - 模糊核大小：設定模糊效果的核心大小(1 ~ 21)。

    輸出：模糊處理後的圖像。

5. **銳化：**

    使用自定義卷積核對圖像進行銳化處理。

    輸入參數：

    - 銳化強度：設定銳化效果的強度 (0.0 ~ 2.0)。

    輸出：銳化處理後的圖像。
