# Sign Language Recognition using MediaPipe & MLP

## 📌 Project Overview

This project implements a high-performance **real-time sign language recognition** system. It leverages **MediaPipe Hands** for precise hand landmark detection and a **Multi-Layer Perceptron (MLP)** neural network for instant character classification. The system captures hand gestures from a webcam, extracts 21 geometric keypoints, and identifies ASL letters with high accuracy and minimal latency.

## 📂 Project Structure

```
📂 Sign Language Recognition System/
│── 📂 SIGN_TO_SENTENCE_PROJECT/
│    │── 📂 Asl_Sign_Data/                       # Raw ASL dataset
│    │── 📄 asl_mediapipe_keypoints_dataset.csv  # Preprocessed dataset for MLP model
│    │── 📄 asl_mediapipe_mlp_model.h5           # Trained MLP model
│    │── 📄 Mediapipe_Training.ipynb             # Training script for MLP model
│    │── 📄 requirements.txt                     # Required dependencies
```

## 🏗️ Dataset: ASL Kaggle Dataset

- The dataset used for training was obtained from **Kaggle ASL Sign Language Dataset**.
- It contains **hand gesture images labeled with ASL characters**.
- For **MLP (MediaPipe)**, we extracted **landmark keypoints** from each image and stored them in CSV format.


## 🚀 Running the Sign Language Recognition System

### **1️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```
### **2️⃣ Running the Project**
To start the real-time recognition system, simply execute the main Python script:

```sh
python simple_recognition.py
```

### **4️⃣ Controls & Commands**

- **Normal Signs** → Letters are appended to the sentence.
- **SPACE Sign** → Adds a space.
- **DELETE Sign** → Removes the last character.
- **NOTHING** → No input detected.



## 🤝 Acknowledgments

- Uses **MediaPipe Hands** for landmark detection.
- Model trained using **TensorFlow & Scikit-Learn**.
- Inspired by existing research on **gesture recognition & sign language AI**.


## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  

---


