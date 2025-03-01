# 🦷 Teeth Classification 🏥  

## 📖 Table of Contents  
- [🔍 Overview](#-overview)  
- [🚀 Features](#-features)  
- [🏗 Model Summary](#-model-summary)  
- [📈 Performance](#-performance)  
- [✔️ Classification Report](#-classification-report)  
- [🛠 Technologies Used](#-technologies-used)  
- [📊 Results](#-results)  

## 🔍 Overview  
An **AI-powered dental disease classification system** that uses **deep learning** and **computer vision** to diagnose various dental conditions from images. This model helps automate and improve dental diagnostics for professionals.  

## 🚀 Features  
✅ **Deep Learning Model (CNN + MobileNetV2)**  
✅ **Transfer Learning for Enhanced Accuracy**  
✅ **Batch Normalization & Dropout for Stability**  
✅ **Real-time Predictions via Web App**  

## 🏗 Model Summary  
🔹 **Convolutional Neural Networks (CNNs)** – Extracts spatial features from dental images  
🔹 **MobileNetV2** – Pre-trained model for efficient classification  
🔹 **Batch Normalization & Dropout** – Improves generalization and stability  
🔹 **Fully Connected Layers** – Final classification  

## 📈 Performance  
🔹 **Training Accuracy:** `98.5%`  
🔹 **Test Accuracy:** `97.0%`  
🔹 **High Precision & Recall Across All Classes**  

## ✔️ Classification Report  
| Class                 | Precision | Recall | F1-Score | Support |  
|-----------------------|-----------|--------|----------|---------|  
| 🦷 **Caries (CaS)**  | `0.92` | `0.99` | `0.96` | `160` |  
| 🏅 **Crown (CoS)**   | `1.00` | `0.97` | `0.98` | `149` |  
| 🌿 **Gum Diseases**  | `0.97` | `0.97` | `0.97` | `120` |  
| 🎗 **Mouth Cancers** | `0.96` | `0.98` | `0.97` | `180` |  
| 🩸 **Oral Cancers**  | `0.99` | `0.96` | `0.98` | `108` |  
| 🛡 **OLP**           | `0.99` | `0.94` | `0.96` | `180` |  
| 🏷 **Other Types**   | `0.99` | `0.99` | `0.99` | `131` |  
| **Overall Accuracy** |  |  | **`0.97`** | **`1028`** |  

## 🛠 Technologies Used  
🔹 **TensorFlow & Keras** – Deep learning framework  
🔹 **OpenCV** – Image processing  
🔹 **Scikit-learn** – Model evaluation  
🔹 **Matplotlib & Pillow** – Image visualization  

## 📊 Results  

### 🏠 Home Page  
![Home](images/home.png)  

### 📂 Upload Image  
![Upload Image](images/upload.png)  

### 📤 Image Uploaded  
![Image Uploaded](images/uploaded.png)  

### 📊 Classification Results  
![Results](images/results.png)  
