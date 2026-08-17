import requests
from django.shortcuts import render
from .models import PredictionHistory

def home(request):
    """
    Home view for soil moisture detection
    """
    prediction = None
    confidence = None
    recommendation = None

    if request.method == "POST":
        image_file = request.FILES.get("image")

        if image_file:
            flask_url = "http://127.0.0.1:5000/predict"

            try:
                files = {"file": image_file}
                response = requests.post(flask_url, files=files, timeout=10)

                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get("prediction")
                    confidence = result.get("confidence")

                    # ==============================
                    # Irrigation Logic
                    # ==============================

                    if confidence is not None:
                        if confidence < 0.6:
                            recommendation = "⚠️ Low confidence. Please retake image with better lighting."
                        else:
                            if prediction == "dry":
                                recommendation = "💧 Start irrigation for 15 minutes immediately!"
                            elif prediction == "normal":
                                recommendation = "🌤️ Soil is optimal. No irrigation needed at this time."
                            elif prediction == "wet":
                                recommendation = "🚫 Stop irrigation. Soil is already wet enough."
                    else:
                        recommendation = "⚠️ Invalid response from AI model."

                    # ==============================
                    # SAVE TO DATABASE
                    # ==============================

                    if prediction and confidence is not None:
                        PredictionHistory.objects.create(
                            image=image_file,
                            prediction=prediction,
                            confidence=confidence,
                            recommendation=recommendation
                        )

                else:
                    recommendation = "⚠️ Error connecting to AI service. Please try again."

            except requests.exceptions.RequestException as e:
                recommendation = "⚠️ Service unavailable. Please check your connection."
                print(f"Error: {e}")

    return render(request, "home.html", {
        "prediction": prediction,
        "confidence": confidence,
        "recommendation": recommendation
    })