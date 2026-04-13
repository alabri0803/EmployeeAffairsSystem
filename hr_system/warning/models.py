from django.db import models

# Create your models here.

class WarningReason(models.Model):
    title = models.CharField(max_length=255)
    description_ar = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return self.title

class Warning(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    reason = models.ForeignKey(WarningReason, on_delete=models.CASCADE)
    details_ar = models.TextField(blank=True)
    details_en = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.details_ar = self.reason.description_ar
        self.details_en = self.reason.description_en
        super().save(*args, **kwargs)