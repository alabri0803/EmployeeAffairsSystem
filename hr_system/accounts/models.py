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
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name=_('الدور')) # Role
    assigned_company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('الشركة')) # Company

    class Meta:
        verbose_name = _('مستخدم')
        verbose_name_plural = _('المستخدمين')

    def __str__(self):
        return self.username