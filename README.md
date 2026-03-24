# Cartoon Rendering using OpenCV

## 🎯 Project Goal
The goal of this assignment is to transform a standard photograph into a "Cartoon Style" image using Computer Vision and Image Processing techniques.

## 🛠️ Technical Implementation
For this project, I focused on **High-Definition Detail Preservation**. Most cartoon filters use heavy smoothing, which loses fine details. My approach intentionally skips certain steps to achieve a sharper look.

- **Grayscale Conversion:** Converting the image to a single-channel intensity map.
- **CLAHE (Contrast Enhancement):** Applied to boost local contrast, ensuring that thin lines and hair strands are visible to the edge detector.
- **Adaptive Thresholding:** Used with a minimal **Block Size of 3** to extract the most intricate details as black ink lines.
- **No Smoothing (Bilateral Filter):** I intentionally omitted the bilateral filter to prevent the "plastic/blurred" look, aiming instead for a detailed ink-sketch aesthetic.

---

## 📊 Demo Results & Discussion 

### 1. Success Case: Effective Cartoon Effect 
**Image:** `Success.jpg`

**Analysis:** This result is highly successful in creating a "Manga" or "Detailed Ink" style. By skipping the smoothing process, the algorithm managed to **"save" every individual strand of hair**, which is usually lost in standard cartoon filters. The bold black outlines on the clothing and facial features give it a strong, hand-drawn artistic feel.

### 2. Failure Case: Ineffective Cartoon Effect
**Image:** `Failure.jpg`

**Analysis:** This image is considered a failure because it **remains too similar to the original photograph** and fails to achieve a "Cartoonish" aesthetic.
- **The Problem:** Because the smoothing filter (Bilateral Filter) was removed, the colors and skin textures remain photorealistic.
- **Reason:** A true cartoon effect requires "Color Quantization" or "Flattening" to look like a drawing. In this case, the result looks like a raw photo with some thin lines on top, lacking the simplified "painted" look required for this assignment.

### 3. Discussion on Limitations 
The primary limitation of this algorithm is the **Trade-off between Detail and Stylization**.
- **Style Constraint:** While excellent for preserving hair (Success Case), the lack of a color-smoothing step means the output often stays too grounded in reality.
- **Input Sensitivity:** Without a smoothing pre-process, the algorithm is extremely dependent on the quality of the input image. If the photo is not perfectly clean, it fails to look like a stylized cartoon and instead looks like an unfiltered, noisy photograph.

---

## 💻 How to Run
1. Install OpenCV: `pip install opencv-python`
2. Run the script: `python main.py`
