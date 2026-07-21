"""
8_Finding_palm_Lines.py
Biometric script that uses a bilateral filter to smooth skin pores and a morphological 
Black Hat transformation to isolate and highlight palm creases in green.
Includes Google Colab compatibility.
"""
import cv2
import numpy as np
import os

# --- Colab Compatibility Logic ---
try:
    from google.colab.patches import cv2_imshow
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def display_image(title, img):
    if IN_COLAB:
        print(f"--- {title} ---")
        cv2_imshow(img)
    else:
        cv2.imshow(title, img)
# ---------------------------------

def main():
    img_path = os.path.join("..", "assets", "palm.jpg")
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}. Please place an image there.")
        return

    # Read image
    img = cv2.imread(img_path)
    
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Bilateral Filter to smooth skin pores while keeping edges sharp
    filtered = cv2.bilateralFilter(gray, 9, 75, 75)

    # 3. Morphological Black Hat Transformation to isolate dark lines (creases) on a bright background (skin)
    kernel = np.ones((15, 15), np.uint8)
    blackhat = cv2.morphologyEx(filtered, cv2.MORPH_BLACKHAT, kernel)

    # 4. Thresholding to binarize the extracted lines
    ret, thresh = cv2.threshold(blackhat, 30, 255, cv2.THRESH_BINARY)

    # 5. Highlight palm creases in green on the original image
    # Find contours from the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    result = img.copy()
    # Draw contours in green
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

    # Display results
    display_image("Original Palm", img)
    display_image("Black Hat Extract", blackhat)
    display_image("Palm Lines Detected", result)

    if not IN_COLAB:
        print("Press any key to close the windows.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
