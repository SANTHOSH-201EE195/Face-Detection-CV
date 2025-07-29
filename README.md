# 👁️ Face Detection using OpenCV (Webcam, Image & Video)

This project performs face detection using Haar Cascade Classifier with OpenCV in three modes:
- Webcam live feed
- Still images
- Video files

---

## 🧠 How It Works

It uses a pre-trained `haarcascade_frontalface_default.xml` model to detect faces in real-time by converting the frames to grayscale and drawing bounding boxes around detected faces.

---

## 🗃️ Files Included

| File | Purpose |
|------|---------|
| `face_detection_cam.py` | Detects faces from live webcam |
| `face_detection_img.py` | Detects faces from a local image |
| `face_detection_video.py` | Detects faces from a local video file |
| `haarcascade_frontalface_default.xml` | Haar cascade classifier model |
| `requirements.txt` | Python dependencies list |

---

## 🛠️ Requirements

Install required libraries:

pip install -r requirements.txt
🚀 How to Run
▶️ Webcam Mode

python face_detection_cam.py
🖼️ Image Mode
Edit the img = cv2.imread() path in face_detection_img.py to your local image file path.

python face_detection_img.py
🎞️ Video Mode
Edit the VideoCapture("Video path") line in face_detection_video.py with your video file path.


python face_detection_video.py
📸 Output
Blue rectangles around detected faces

Real-time detection on camera/video

Esc key (Esc) to exit

🔗 Project Link
👉 Face Detection CV on GitHub

👤 Author
Santhosh T
GitHub Profile

📄 License
This project is open-source under the MIT License.



---

### ✅ Step 6: You're Done!

Anyone visiting your repo can now:
- View and download the code
- Understand usage via README
- Install dependencies and run locally

---
