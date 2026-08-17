import tensorflow as tf
import numpy as np
import cv2

# Load model
model = tf.keras.models.load_model("soil_moisture_cnn.h5")

IMG_SIZE = 128
class_names = ["dry", "wet"]  # order matters

image_path = input("Enter image path: ")

img = cv2.imread(image_path)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
img = img / 255.0
img = np.expand_dims(img, axis=0)

prediction = model.predict(img)[0][0]

if prediction > 0.5:
    label = "wet"
else:
    label = "dry"

confidence = prediction if prediction > 0.5 else 1 - prediction

print(f"\nPrediction: {label}")
print(f"Confidence: {confidence * 100:.2f}%")
