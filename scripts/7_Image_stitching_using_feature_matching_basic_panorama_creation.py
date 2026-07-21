"""
7_Image_stitching_using_feature_matching_basic_panorama_creation.py
Aligns two overlapping images using ORB feature extraction, RANSAC for homography 
matrix calculation, and perspective warping to create a panorama.
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
        cv2.imshow(title, cv2.resize(img, (800, 600)))
# ---------------------------------

def main():
    img1_path = os.path.join("..", "assets", "left.jpg")
    img2_path = os.path.join("..", "assets", "right.jpg")
    
    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        print(f"Error: Need two overlapping images named 'left.jpg' and 'right.jpg' in assets folder.")
        print("Please place them and re-run.")
        return

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    # Use OpenCV's built in Stitcher for the best results, OR we can manually stitch using homography.
    # The prompt specifically asks for: "ORB feature extraction, RANSAC for homography matrix calculation, and perspective warping"
    # So we will do it manually.

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kp1[match.queryIdx].pt
        points2[i, :] = kp2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

    if h is not None:
        # Warp img2 to img1 perspective
        height, width, channels = img1.shape
        # Create a large enough canvas
        panorama = cv2.warpPerspective(img2, h, (width + img2.shape[1], height))
        # Place img1 on the left side
        panorama[0:height, 0:width] = img1
        
        display_image("Panorama", panorama)
    else:
        print("Could not calculate homography matrix.")

    if not IN_COLAB:
        print("Press any key to close the windows.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
