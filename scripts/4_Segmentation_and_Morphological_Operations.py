"""
4_Segmentation_and_Morphological_Operations.py
Executes global Otsu and adaptive thresholding, followed by Erosion, Dilation, Opening, and Closing morphological operations.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    img_path = os.path.join("..", "assets", "doggy.jpg")
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}.")
        return

    # Read image in grayscale
    img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 1. Global Thresholding (Otsu's method)
    ret, otsu_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 2. Adaptive Thresholding
    adaptive_thresh = cv2.adaptiveThreshold(
        img_gray, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )

    # Define a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Use the Otsu thresholded image for morphological operations
    # 3. Erosion
    erosion = cv2.erode(otsu_thresh, kernel, iterations=1)

    # 4. Dilation
    dilation = cv2.dilate(otsu_thresh, kernel, iterations=1)

    # 5. Opening (Erosion followed by Dilation - good for removing noise)
    opening = cv2.morphologyEx(otsu_thresh, cv2.MORPH_OPEN, kernel)

    # 6. Closing (Dilation followed by Erosion - good for closing small holes)
    closing = cv2.morphologyEx(otsu_thresh, cv2.MORPH_CLOSE, kernel)

    # Plot results
    titles = ['Original Grayscale', 'Otsu Thresholding', 'Adaptive Thresholding', 
              'Erosion', 'Dilation', 'Opening', 'Closing']
    images = [img_gray, otsu_thresh, adaptive_thresh, erosion, dilation, opening, closing]

    plt.figure(figsize=(15, 10))
    for i in range(7):
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
