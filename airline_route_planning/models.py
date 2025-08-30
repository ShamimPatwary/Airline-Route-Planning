from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Route(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='routes_from')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='routes_to')
    distance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.origin.code} -> {self.destination.code}"