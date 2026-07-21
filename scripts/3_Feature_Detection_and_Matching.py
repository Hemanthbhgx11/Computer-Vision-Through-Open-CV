"""
3_Feature_Detection_and_Matching.py
Implements the ORB detector to find up to 2000 keypoints and match them between a query and train image using a Brute-Force Matcher with Hamming distance.
"""
import cv2
import os

def main():
    # Use mypassport.jpg as an example asset.
    # In a real scenario, you'd use a query image (e.g., cropped part) and a train image (the full scene)
    query_path = os.path.join("..", "assets", "mypassport.jpg")
    train_path = os.path.join("..", "assets", "mypassport.jpg")
    
    if not os.path.exists(query_path) or not os.path.exists(train_path):
        print(f"Error: Missing images. Please place '{query_path}' and '{train_path}' in the assets folder.")
        return

    # Read images in grayscale
    query_img = cv2.imread(query_path, cv2.IMREAD_GRAYSCALE)
    train_img = cv2.imread(train_path, cv2.IMREAD_GRAYSCALE)
    
    # Initialize ORB detector with up to 2000 keypoints
    orb = cv2.ORB_create(nfeatures=2000)

    # Find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(query_img, None)
    kp2, des2 = orb.detectAndCompute(train_img, None)

    if des1 is None or des2 is None:
        print("Error: Could not find descriptors in one or both images.")
        return

    # Create Brute-Force Matcher with Hamming distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 100 matches
    matched_img = cv2.drawMatches(
        query_img, kp1, 
        train_img, kp2, 
        matches[:100], None, 
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    cv2.imshow("ORB Feature Matching", matched_img)
    print("Press any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
