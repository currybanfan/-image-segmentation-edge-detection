import gradio as gr
import cv2
import numpy as np
from skimage.segmentation import slic
from skimage.color import label2rgb
import os
import glob

def edge_detection(image, threshold1, threshold2):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges


def image_segmentation(image, n_segments, compactness):
    segments = slic(image, n_segments=n_segments, compactness=compactness, start_label=1)
    segmented_image = label2rgb(segments, image, kind="avg")
    return (segmented_image * 255).astype(np.uint8)

def apply_threshold(image, threshold_value):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def apply_blur(image, kernel_size):
    kernel_size = int(kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred_image

def apply_sharpen(image, intensity):
    kernel = np.array([
        [0, -intensity, 0],
        [-intensity, 1 + 4 * intensity, -intensity],
        [0, -intensity, 0]
    ])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

EXAMPLES_DIR = "examples/"

example_images = glob.glob(os.path.join(EXAMPLES_DIR, "*.png"))

def select_image(img):
    return img

with gr.Blocks() as demo:
    gr.Markdown("## 電腦視覺應用")

    image_input = gr.Image(label="上傳圖片", type="numpy", height="500px")

    with gr.Row():
        for image in example_images:
            img_component = gr.Image(
                value=image,
                interactive=False,
                type="numpy"
            )

            img_component.select(
                select_image,
                inputs=img_component,
                outputs=image_input
            )

    gr.Markdown("---")

    with gr.Tab("邊緣檢測"):
        edge_threshold1 = gr.Slider(0, 255, value=50, label="邊緣檢測閾值1")
        edge_threshold2 = gr.Slider(0, 255, value=150, label="邊緣檢測閾值2")

        edge_button = gr.Button("執行邊緣檢測")
        edge_output = gr.Image(label="邊緣檢測結果", type="numpy")

        edge_button.click(
            edge_detection, 
            inputs=[image_input, edge_threshold1, edge_threshold2], 
            outputs=edge_output
        )


    with gr.Tab("影像分割"):
        n_segments = gr.Slider(100, 1000, value=200, step=50, label="分割區域數量")
        compactness = gr.Slider(1, 50, value=10, label="分割緊湊性")

        segment_button = gr.Button("執行影像分割")
        segment_output = gr.Image(label="影像分割結果", type="numpy")

        segment_button.click(
            image_segmentation, 
            inputs=[image_input, n_segments, compactness], 
            outputs=segment_output
        )
    

    with gr.Tab("圖像二值化"):
        threshold_slider = gr.Slider(0, 255, value=128, step=1, label="二值化閾值")
        threshold_button = gr.Button("應用二值化")
        threshold_output = gr.Image(label="二值化结果", type="numpy")
        
        threshold_button.click(
            apply_threshold,
            inputs=[image_input, threshold_slider],
            outputs=threshold_output
        )

    with gr.Tab("模糊"):
        blur_slider = gr.Slider(1, 21, value=5, step=2, label="模糊核大小")
        blur_button = gr.Button("應用模糊")
        blur_output = gr.Image(label="模糊结果", type="numpy")
        
        blur_button.click(
            apply_blur,
            inputs=[image_input, blur_slider],
            outputs=blur_output
        )
    

    with gr.Tab("銳化"):
        sharpen_slider = gr.Slider(0.0, 2.0, value=1.0, step=0.1, label="銳化强度")
        sharpen_button = gr.Button("應用銳化")
        sharpen_output = gr.Image(label="銳化结果", type="numpy")
        
        sharpen_button.click(
            apply_sharpen,
            inputs=[image_input, sharpen_slider],
            outputs=sharpen_output
        )


if __name__ == "__main__":
    demo.launch(debug=True)
