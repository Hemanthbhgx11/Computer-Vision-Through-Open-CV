# Computer-Vision-Through-Open-CV

Here is a complete, interactive, and professional `README.md` template tailored for your repository. It includes clear instructions for both local (VS Code) and cloud (Google Colab) execution, utilizing a reddish-orange accent theme for the badges to give it a distinct, active brand identity.

You can copy the code block below and paste it directly into your GitHub repository's `README.md` file.

```markdown
# 👁️ Computer Vision & OpenCV Laboratory

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.14-FF4500?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-FF4500?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/VS_Code-Local_Execution-FF4500?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Google_Colab-Cloud_Execution-FF4500?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Colab">
</div>

---

## 📌 Overview
This repository contains a comprehensive suite of Computer Vision experiments and real-time applications implemented using **OpenCV** and **Python**. It is designed to bridge the gap between theoretical image processing concepts and real-world system deployments, ranging from basic morphological operations to advanced real-time deep learning pipelines (like YOLOv8).

## 🚀 Repository Structure

The experiments are structured to build foundational knowledge before moving into advanced tracking and detection algorithms. 

<details>
<summary><b>Click to expand the list of Practical Exercises</b></summary>
<br>

| Exp No. | Topic | Description |
| :---: | :--- | :--- |
| **01** | Image Handling & Transformations | Basic I/O, scaling, and affine rotation matrices. |
| **02** | Filtering & Enhancement | Noise reduction (Gaussian/Median) and Canny edge isolation. |
| **03** | Feature Detection & Matching | Utilizing the ORB algorithm and Brute Force Matcher. |
| **04** | Segmentation & Morphology | Thresholding (Otsu/Adaptive), Erosion, and Dilation. |
| **05** | Video Processing | Live frame extraction, edge overlay, and `.avi` exportation. |
| **06** | Face & Object Detection | Haar Cascades and MobileNet SSD deep learning inferences. |
| **07** | Image Stitching | Panorama creation using Homography and RANSAC algorithms. |
| **08** | Palm Line Extraction | Biometric isolation using Bilateral Filtering and Morphological Black Hat. |
| **09** | Human Movement Tracking | Motion trails using MOG2 background subtraction. |
| **10** | **Mini-Project** | Real-time object detection and tracking utilizing **YOLOv8**. |

</details>

---

## 💻 Execution Environments

This repository is optimized to run seamlessly on both local IDEs and cloud-based Jupyter Notebooks. Please follow the instructions for your preferred environment.

### Option A: Local Execution (VS Code)
Ideal for real-time video processing, webcam integration, and high-FPS YOLO inference.

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/computer-vision-lab.git](https://github.com/your-username/computer-vision-lab.git)
cd computer-vision-lab

```

**2. Set up a virtual environment (Anaconda recommended):**

```bash
conda create -n cv_env python=3.14
conda activate cv_env

```

**3. Install dependencies:**

```bash
pip install opencv-python numpy matplotlib ultralytics

```

**4. Run a script:**

```bash
python scripts/01_image_handling.py

```

*Note: Scripts utilizing live webcams (`cv2.VideoCapture(0)`) must be run locally in VS Code.*

### Option B: Cloud Execution (Google Colab)

Ideal for deep learning inference, model downloading, and static image processing without local setup.

**1. Open Google Colab:** Navigate to [Google Colab](https://colab.research.google.com/) and upload the provided `.ipynb` files or clone the repo directly into your Colab workspace.

**2. Note on OpenCV Display in Colab:**
Colab does not support local GUI windows. The standard `cv2.imshow()` will cause the kernel to crash. In all Colab scripts, this has been patched using:

```python
# Replace standard cv2.imshow with this patch in Colab
from google.colab.patches import cv2_imshow

cv2_imshow(processed_image)

```

**3. File Uploading in Colab:**
When a script requires an image, upload the file directly to your Colab session file explorer (left sidebar) or mount your Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

```

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python
* **Core Libraries:** OpenCV (`cv2`), NumPy, Matplotlib
* **Deep Learning:** Ultralytics (YOLOv8), Caffe (MobileNet SSD)
* **Environments:** Visual Studio Code, Google Colab

---

## 👨‍💻 Author

**Hemanth Goud Burra**

*CEO Tech Roxx*
Feel free to fork this repository, submit pull requests, or reach out if you have any questions regarding the computer vision architectures used in these experiments!

```

```
