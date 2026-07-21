"""
6_Face_and_Object_Detection.py
Features an automatic model downloader for MobileNet SSD architecture and weights, 
combining deep learning object detection with OpenCV's built-in Haar Cascade face detector.
Includes Google Colab compatibility.
"""
import cv2
import os
import urllib.request
import numpy as np

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

def download_file(url, filepath):
    if not os.path.exists(filepath):
        print(f"Downloading {filepath}...")
        urllib.request.urlretrieve(url, filepath)
        print("Download complete.")

def main():
    assets_dir = os.path.join("..", "assets")
    os.makedirs(assets_dir, exist_ok=True)

    # 1. Setup MobileNet SSD Model
    prototxt_url = "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/voc/MobileNetSSD_deploy.prototxt"
    model_url = "https://github.com/chuanqi305/MobileNet-SSD/raw/master/voc/MobileNetSSD_deploy.caffemodel"
    
    prototxt_path = os.path.join(assets_dir, "MobileNetSSD_deploy.prototxt")
    model_path = os.path.join(assets_dir, "MobileNetSSD_deploy.caffemodel")
    
    download_file(prototxt_url, prototxt_path)
    download_file(model_url, model_path)

    # 2. Setup Haar Cascade Face Detector
    haar_cascade_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    cascade_path = os.path.join(assets_dir, "haarcascade_frontalface_default.xml")
    download_file(haar_cascade_url, cascade_path)

    # 3. Load Sample Image
    img_path = os.path.join(assets_dir, "doggy.jpg")
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}. Please place an image there.")
        return

    img = cv2.imread(img_path)
    (h, w) = img.shape[:2]

    # --- Object Detection (MobileNet SSD) ---
    print("Loading MobileNet SSD...")
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Classes for MobileNet SSD (VOC dataset)
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]

    img_object_det = img.copy()
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
            cv2.rectangle(img_object_det, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(img_object_det, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # --- Face Detection (Haar Cascade) ---
    print("Running Haar Cascade Face Detection...")
    face_cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    img_face_det = img.copy()
    for (x, y, fw, fh) in faces:
        cv2.rectangle(img_face_det, (x, y), (x+fw, y+fh), (255, 0, 0), 2)
        cv2.putText(img_face_det, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display results
    display_image("Object Detection (SSD)", img_object_det)
    display_image("Face Detection (Haar)", img_face_det)

    if not IN_COLAB:
        print("Press any key to close the windows.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
