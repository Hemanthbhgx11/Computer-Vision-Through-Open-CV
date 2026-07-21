"""
2_Filtering_and_enhancement_techniques.py
Applies Gaussian blur, Median blur, sharpening matrices, Canny edge detection, and histogram equalization, utilizing Matplotlib to plot a 2x3 matrix of the results.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    img_path = os.path.join("..", "assets", "doggy.jpg")
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}. Please place an image there.")
        return

    # Read image and convert color spaces for Matplotlib (RGB) and processing
    img_color = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # 1. Gaussian Blur
    gaussian = cv2.GaussianBlur(img_rgb, (15, 15), 0)

    # 2. Median Blur
    median = cv2.medianBlur(img_rgb, 15)

    # 3. Sharpening Matrix
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])
    sharpened = cv2.filter2D(img_rgb, -1, kernel_sharpening)

    # 4. Canny Edge Detection
    edges = cv2.Canny(img_gray, 100, 200)

    # 5. Histogram Equalization (requires grayscale image)
    hist_eq = cv2.equalizeHist(img_gray)

    # Plotting 2x3 matrix using Matplotlib
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()

    # Original
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Gaussian Blur
    axes[1].imshow(gaussian)
    axes[1].set_title("Gaussian Blur")
    axes[1].axis('off')

    # Median Blur
    axes[2].imshow(median)
    axes[2].set_title("Median Blur")
    axes[2].axis('off')

    # Sharpening
    axes[3].imshow(sharpened)
    axes[3].set_title("Sharpened")
    axes[3].axis('off')

    # Canny Edge Detection (grayscale output)
    axes[4].imshow(edges, cmap='gray')
    axes[4].set_title("Canny Edge Detection")
    axes[4].axis('off')

    # Histogram Equalization (grayscale output)
    axes[5].imshow(hist_eq, cmap='gray')
    axes[5].set_title("Histogram Equalization")
    axes[5].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
