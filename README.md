---
title: Image Segmentation Edge Detection
emoji: 🌌
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.6.0
app_file: app.py
---

# 電腦視覺應用專案

此專案是一個基於 Gradio 的電腦視覺應用，提供了多種圖片處理功能，包括邊緣檢測、影像分割、二值化處理、模糊效果和銳化效果。使用者可以上傳自己的圖片或選擇範例圖片進行處理，直觀地查看不同圖像處理技術的效果。

## 功能介紹

#### 邊緣檢測

透過 OpenCV 的 Canny 邊緣檢測算法，根據設定的兩個閾值來檢測圖像邊緣。

輸入參數：

-   邊緣檢測閾值 1：設定低閾值 (0 ~ 255)。
-   邊緣檢測閾值 2：設定高閾值 (0 ~ 255)。

輸出：包含邊緣的黑白圖像。

#### 影像分割

使用 SLIC 將圖像分割為多個區域。

輸入參數：

-   分割區域數量：設定分割區塊數量 (100 ~ 1000)。
-   分割緊湊性：設定區塊形狀的緊湊程度 (1 ~ 50)。

輸出：顯示分割後的平均區域顏色。

#### 圖像二值化

將圖像轉為灰階後，根據設定的閾值進行二值化處理。

輸入參數：

-   二值化閾值：設定二值化的閾值 (0 ~ 255)。

輸出：黑白二值化圖像。

#### 模糊

透過高斯模糊進行圖像平滑處理。

輸入參數：

-   模糊核大小：設定模糊效果的核心大小(1 ~ 21)。

輸出：模糊處理後的圖像。

#### 銳化

使用自定義卷積核對圖像進行銳化處理。

輸入參數：

-   銳化強度：設定銳化效果的強度 (0.0 ~ 2.0)。

輸出：銳化處理後的圖像。

## 安裝與執行

#### 環境需求

-   Python 3.11

#### 安裝方式

使用本地環境

在專案目錄中執行以下指令來安裝所需依賴：

```bash
pip install -r requirements.txt
```

#### 執行專案

本地執行

執行以下指令啟動 Gradio Web 應用：

```bash
python app.py
```

啟動後，訪問命令列中提供的 URL。

---

#### 使用 Docker

```bash
docker run -it -p 7860:7860 --platform=linux/amd64 registry.hf.space/wei-hsu-ai-image-segmentation-edge-detection:latest python app.py
```

啟動後，訪問本地 http://localhost:7860/

#### 使用 Hugging Face Space

直接在 Hugging Face Space 上體驗此應用：
[使用 Hugging Face Space](https://huggingface.co/spaces/Wei-Hsu-AI/image-segmentation-edge-detection)
