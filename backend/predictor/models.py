from django.db import models

class PredictionHistory(models.Model):
    image = models.ImageField(upload_to="uploads/")
    prediction = models.CharField(max_length=20)
    confidence = models.FloatField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} - {self.created_at}"