from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', _('Owner')),
        ('hr', _('HR Manager')),
        ('employee', _('Employee')),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username