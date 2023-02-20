from django.db import models

class Show(models.Model):
  kategorie = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  ort = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  kosten = models.DecimalField(max_digits=5, decimal_places=2)
  jahr = models.CharField(max_length=4)
