"""
9_Human_Tracking.py
Utilizing the MOG2 background subtractor, thresholding, and contour detection to track 
human movement and draw a red historical trailing path across sequential video frames.

NOTE: This script utilizes local GUI windows (cv2.imshow) and requires a local 
VS Code / Python environment to run effectively. It is not suited for Google Colab without 
heavy modifications for HTML5 video rendering.
"""
import cv2
import numpy as np

def main():
    # Use webcam (0) or path to a video file containing people walking
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # Initialize MOG2 background subtractor
    back_sub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)
    
    # List to store the historical center points of tracked objects
    path_history = []

    print("Running Human Tracking. Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply background subtraction
        fg_mask = back_sub.apply(frame)

        # Thresholding to remove shadows (which are usually gray in MOG2 mask)
        _, thresh = cv2.threshold(fg_mask, 254, 255, cv2.THRESH_BINARY)

        # Morphological operations to clean up noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

        # Find contours
        contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Ignore small contours (noise)
            if cv2.contourArea(contour) < 2000:
                continue

            # Get bounding box for the person
            x, y, w, h = cv2.boundingRect(contour)
            
            # Calculate the center of the bounding box
            center = (int(x + w / 2), int(y + h / 2))
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Add center to path history
            path_history.append(center)

            # Limit the trail length to prevent memory overload (e.g., last 100 points)
            if len(path_history) > 100:
                path_history.pop(0)

        # Draw the historical trailing path in red
        for i in range(1, len(path_history)):
            if path_history[i - 1] is None or path_history[i] is None:
                continue
            # Draw line between consecutive points
            cv2.line(frame, path_history[i - 1], path_history[i], (0, 0, 255), 3)

        # Display the result
        cv2.imshow("Human Tracking", frame)
        cv2.imshow("Foreground Mask", closing)

        # Break the loop on 'q' key press
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
