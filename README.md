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

## 📌 Model 1: MobileNetV2 Approach

- However, it struggled with **real-time sign recognition**, leading us to explore **MediaPipe-based MLP**.

## 🚀 Running the Sign Language Recognition System

### **1️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **2️⃣ Running Model Evaluations**

To test the output of individual models, run the **last cell** in:

- `Mediapipe_Training.ipynb` for MLP model evaluation.
- `MobileNetV2_Training.ipynb` for MobileNetV2 evaluation.

### **3️⃣ Running the Combined Architecture**

To see the working of **both MobileNetV2 and MediaPipe integrated**, run:

```sh
jupyter notebook Combined_Architecture.ipynb
```

### **4️⃣ Controls & Commands**

- **Normal Signs** → Letters are appended to the sentence.
- **SPACE Sign** → Adds a space.
- **DELETE Sign** → Removes the last character.
- **NOTHING** → No input detected.

## ⚠️ Limitations & Next Steps

- **MobileNet did not perform well on real-time images**, so we moved to **MediaPipe-based MLP**.
- **Next Phase** → Building a FastAPI backend (`SignConnect-Backend`) for better integration and mobile app support.

## 🔜 Future Work: Text-to-Sign Language Generation

As the next phase of development, we aim to implement **Text-to-Sign Language Actions**, allowing users to input text that gets translated into sign language animations. Possible technologies we will explore:
- **AI-generated 3D avatars** to perform sign language gestures.
- **Computer Vision & Reinforcement Learning** to map text to sign movements.
- **Deep Learning models** to generate smooth sign transitions.

### 💡 Open for Contributions
We welcome contributions from the community for this phase! If you're interested in helping develop **Text-to-Sign Language Generation**, feel free to open an issue or submit a pull request on our GitHub repository.


## 🤝 Acknowledgments

- Uses **MediaPipe Hands** for landmark detection.
- Model trained using **TensorFlow & Scikit-Learn**.
- Inspired by existing research on **gesture recognition & sign language AI**.


## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  

---


