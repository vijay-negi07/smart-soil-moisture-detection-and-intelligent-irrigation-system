import os
import io
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# ==============================
# Create Flask App
# ==============================

app = Flask(__name__)

# ==============================
# Load Model (Only Once)
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "soil_moisture_mobilenet.keras"
)

print("Loading model from:", MODEL_PATH)

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully ✅")

# Class labels (IMPORTANT: order must match training)
CLASS_NAMES = ["dry", "normal", "wet"]

# ==============================
# Routes
# ==============================

@app.route("/")
def home():
    return "Soil Moisture API is Running 🚀"

@app.route("/health")
def health():
    return {"status": "Model loaded and healthy"}

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    try:
        # Read file bytes
        file_bytes = file.read()

        # Convert to BytesIO
        img = image.load_img(io.BytesIO(file_bytes), target_size=(160, 160))

        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Prediction
        predictions = model.predict(img_array)
        predicted_index = int(np.argmax(predictions[0]))
        confidence = float(np.max(predictions[0]))

        result = {
            "prediction": CLASS_NAMES[predicted_index],
            "confidence": round(confidence, 3)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==============================
# Run Server
# ==============================

if __name__ == "__main__":
    app.run(debug=True)

