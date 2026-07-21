"""
1_Image_handling_and_transformations.py
Prompts the user for an image path and applies resizing, horizontal flipping, a 45-degree rotation, and a translation shift.
"""
import cv2
import numpy as np
import os

def main():
    # Prompt the user for an image path
    default_path = os.path.join("..", "assets", "doggy.jpg")
    img_path = input(f"Enter image path [default: {default_path}]: ").strip()
    if not img_path:
        img_path = default_path
        
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}. Please place an image there.")
        return

    # Read image
    img = cv2.imread(img_path)
    
    # 1. Resizing (e.g., half size)
    resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    
    # 2. Horizontal Flipping (1 = horizontal, 0 = vertical, -1 = both)
    flipped_img = cv2.flip(img, 1)
    
    # 3. 45-degree Rotation
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M_rot = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_img = cv2.warpAffine(img, M_rot, (w, h))
    
    # 4. Translation Shift (shift right by 50px, down by 50px)
    M_trans = np.float32([[1, 0, 50], [0, 1, 50]])
    translated_img = cv2.warpAffine(img, M_trans, (w, h))
    
    # Display results
    cv2.imshow("Original", img)
    cv2.imshow("Resized", resized_img)
    cv2.imshow("Flipped Horizontally", flipped_img)
    cv2.imshow("Rotated 45 Degrees", rotated_img)
    cv2.imshow("Translated", translated_img)
    
    print("Press any key to close the windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
