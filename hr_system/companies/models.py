from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('اسم الشركة'))
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name