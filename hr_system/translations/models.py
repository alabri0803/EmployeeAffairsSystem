from django.db import models

# Create your models here.

class Translation(models.Model):
    arabic_text = models.TextField()
    english_text = models.TextField()

    def __str__(self):
        return self.arabic_text
