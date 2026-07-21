"""
5_video_Processing.py
Takes a live webcam feed or video file, applies Canny edge detection frame-by-frame, overlays a dynamic timestamp, and exports the result using cv2.VideoWriter.
"""
import cv2
import datetime
import os

def main():
    # Use webcam (0) or a video file path
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # Get video properties for VideoWriter
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps != fps: # Check for 0 or NaN
        fps = 30.0

    # Define the codec and create VideoWriter object
    # MP4V is a widely supported codec for mp4 files
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_path = os.path.join("..", "output_video.mp4")
    out = cv2.VideoWriter(out_path, fourcc, fps, (frame_width, frame_height), isColor=False)

    print("Recording... Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or error reading frame.")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Canny Edge Detection
        edges = cv2.Canny(gray, 100, 200)

        # Add dynamic timestamp overlay
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(
            edges, timestamp, 
            (10, frame_height - 20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, (255, 255, 255), 2, cv2.LINE_AA
        )

        # Write the edge-detected frame to output file
        out.write(edges)

        # Display the resulting frame
        cv2.imshow('Edge Detected Video with Timestamp', edges)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {out_path}")

if __name__ == "__main__":
    main()
