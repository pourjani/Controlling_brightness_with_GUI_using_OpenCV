# 🎥 Real-Time Video/image Brightness Control with OpenCV

This project demonstrates a simple yet powerful technique for controlling the **brightness** of a video/image **in real time** using OpenCV. An interactive GUI trackbar (slider) lets users increase or decrease brightness dynamically while the video plays.


---

## 🎞 Demo
![DEMO](sample.gif)

---

## ✨ Features

- 🔄 Real-time frame processing using OpenCV
- 🎚️ Interactive brightness control with a slider
- ⚡ Efficient pixel-level operations using NumPy
- 👁️ Smooth and immediate visual feedback


---

## 🧠 How It Works

- A window is created with a **trackbar** labeled `'Brightness'`.
- The slider ranges from `0` to `255`. The midpoint `127` represents the **original brightness**.
- If the value is **above 127**, brightness is increased by adding a constant matrix to the image.
- If the value is **below 127**, brightness is decreased using subtraction.
- The adjustment is applied **frame-by-frame**, making it suitable for real-time applications.
- This approach avoids pixel overflow and underflow using OpenCV’s built-in `cv2.add()` and `cv2.subtract()` functions.




