from django.db import models

# Create your models here.

class Employee(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    first_name_ar = models.CharField(max_length=100, verbose_name="الاسم عربي")
    first_name_en = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100)
    is_omani = models.BooleanField(default=False)
    hire_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.first_name_ar and not self.first_name_en:
            from translations.utils import translate_text
            self.first_name_en = translate_text(self.first_name_ar)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name_ar