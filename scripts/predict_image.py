import cv2
import numpy as np
import joblib
import sys

# Load saved model
model = joblib.load("soil_moisture_svm.pkl")

# Function to extract features (same as training)
def extract_features(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    hist = cv2.normalize(hist, hist).flatten()
    
    return hist

# Take image path from user
image_path = input("Enter image path: ")

features = extract_features(image_path)
features = features.reshape(1, -1)

categories = ["dry", "normal", "wet"]
prediction = model.predict(features)
print("\nPredicted Soil Moisture Level:", categories[prediction[0]])