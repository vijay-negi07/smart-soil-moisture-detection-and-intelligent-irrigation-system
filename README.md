# 🌱 Smart Soil Moisture Detection and Intelligent Irrigation System

An AI-powered soil moisture detection system that classifies soil into **Dry, Normal, and Wet** using deep learning and recommends irrigation actions. The project uses **MobileNetV2** for image classification, **Flask API** for AI inference, and **Django** for the web application and prediction history.

---

## 📌 Features

- 📷 Upload soil image
- 🤖 AI-based soil moisture prediction
- 🌱 Classifies soil into:
  - Dry
  - Normal
  - Wet
- 📊 Displays prediction confidence
- 💧 Intelligent irrigation recommendation
- 📝 Stores prediction history in database
- 🌐 Flask API integrated with Django
- ⚡ Real-time prediction

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Django
- Flask

### AI / Deep Learning
- TensorFlow
- Keras
- MobileNetV2 (Transfer Learning)

### Database
- SQLite

### Libraries
- OpenCV
- NumPy
- Pillow
- Requests
- Matplotlib

---

## 📂 Project Structure

```
Smart-Soil-Moisture-Detection-and-Intelligent-Irrigation-System/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── models/                      # Trained models only
│   ├── soil_moisture_mobilenet.keras
│   ├── soil_moisture_cnn.h5
│   ├── soil_moisture_cnn_newdata.h5
│   └── soil_moisture_svm.pkl
│
├── api/                         # Flask AI API
│   └── app.py
│
├── backend/                     # Django Project
│   ├── manage.py
│   ├── db.sqlite3
│   ├── predictor/
│   ├── backend/
│   ├── media/
│   └── static/
│
├── dataset/                     # Dataset (optional)
│   ├── dry/
│   ├── normal/
│   └── wet/
│
├── training/                    # Training scripts only
│   ├── train_mobilenet.py
│   ├── train_cnn.py
│   ├── train_svm.py
│   ├── train.py
│   ├── train_model.py
│   ├── utils.py
│   └── eval.py
│
├── scripts/                     # Helper scripts
    ├── prepare_dataset.py
    ├── predict_image.py
    ├── predict_cnn.py
    ├── check_dataset.py
    ├── plot.py
    ├── config.py
    ├── model.py
    └── data_processor.py

```

---

## 🚀 How It Works

1. User uploads a soil image.
2. Django receives the image.
3. Django sends the image to the Flask API.
4. Flask preprocesses the image.
5. MobileNetV2 predicts the soil moisture class.
6. Flask returns:
   - Predicted class
   - Confidence score
7. Django displays:
   - Prediction
   - Confidence
   - Irrigation recommendation
8. Prediction is stored in the database.

---

## 🧠 Model Details

- Model: MobileNetV2
- Framework: TensorFlow/Keras
- Classes:
  - Dry
  - Normal
  - Wet
- Output Layer: Softmax (3 Classes)
- Loss Function: Categorical Crossentropy
- Optimizer: Adam

---

## 💧 Irrigation Logic

| Prediction | Recommendation |
|------------|----------------|
| Dry | Start irrigation |
| Normal | No irrigation needed |
| Wet | Stop irrigation |

If confidence is low (<60%), the user is asked to capture a better image.

---

## 📈 Performance

### CNN Model

- Accuracy: **72%**

### MobileNetV2

- Accuracy: **83%**

### Classification Report

| Class | Precision | Recall | F1-score |
|-------|----------:|--------:|----------:|
| Dry | 0.91 | 0.83 | 0.86 |
| Normal | 0.91 | 0.85 | 0.88 |
| Wet | 0.69 | 0.81 | 0.75 |

Overall Accuracy: **83%**

---

## ▶️ Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/vijay-negi07/Smart-Soil-Moisture-Detection-and-Intelligent-Irrigation-System.git
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Train Model (Optional)

```bash
python train_mobilenet.py
```

---

### 4. Start Flask API

```bash
cd api
python app.py
```

Runs at:

```
http://127.0.0.1:5000
```

---

### 5. Start Django

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## 📸 Screenshots

<img width="1432" height="843" alt="Screenshot 2026-08-17 171430" src="https://github.com/user-attachments/assets/634eae9d-6322-4269-b932-04242f75959c" />

<img width="1122" height="840" alt="Screenshot 2026-08-17 171501" src="https://github.com/user-attachments/assets/a355cc34-5dba-4baf-b9ab-14c082956b95" />

<img width="622" height="512" alt="Screenshot 2026-08-17 171517" src="https://github.com/user-attachments/assets/eeb9073f-39e9-4bb1-ac90-c17ff4ed0891" />

<img width="1872" height="742" alt="Screenshot 2026-08-17 171702" src="https://github.com/user-attachments/assets/6c4dd25b-1a4c-45d1-b4b8-e61582d7ef0e" />

<img width="1893" height="812" alt="Screenshot 2026-08-17 171734" src="https://github.com/user-attachments/assets/e32ff96e-f5de-4806-b677-a0ed01fa5735" />


## 🔮 Future Improvements

- IoT Sensor Integration
- Raspberry Pi Edge Deployment
- Weather API Integration
- Fertilizer Recommendation
- Crop Recommendation
- Multi-language Support
- Cloud Deployment (AWS/Azure)

---

## 📜 License

This project is developed for educational and research purposes.

