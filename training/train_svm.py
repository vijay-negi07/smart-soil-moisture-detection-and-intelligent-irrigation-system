import joblib
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset path
dataset_path = "dataset"

categories = ["dry", "normal", "wet"]

X = []
y = []

# Image size
IMG_SIZE = 128

for label, category in enumerate(categories):
    folder_path = os.path.join(dataset_path, category)
    
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        
        img = cv2.imread(img_path)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Histogram feature
        hist = cv2.calcHist([gray], [0], None, [256], [0,256])
        hist = cv2.normalize(hist, hist).flatten()
        
        X.append(hist)
        y.append(label)

X = np.array(X)
y = np.array(y)

print("Feature shape:", X.shape)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create SVM model
from sklearn.svm import SVC

model = SVC(kernel='linear', class_weight='balanced')

# Train
model.fit(X_train, y_train)
joblib.dump(model, "soil_moisture_svm.pkl")
print("Model saved successfully.")


# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d',
            xticklabels=categories,
            yticklabels=categories)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=categories))
