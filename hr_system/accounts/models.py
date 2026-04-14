from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from translations.utils import translate_text

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', _('Owner')),
        ('hr', _('HR Manager')),
        ('employee', _('Employee')),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name=_('الدور')) # Role
    assigned_company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('الشركة')) # Company
    
    first_name_ar = models.CharField(max_length=100, blank=True, verbose_name=_('الاسم عربي'))
    first_name_en = models.CharField(max_length=100, blank=True)
    last_name_ar = models.CharField(max_length=100, blank=True, verbose_name=_('العائلة عربي'))
    last_name_en = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True, verbose_name=_('رقم الهاتف'))
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    is_active_user = models.BooleanField(default=True, verbose_name=_('نشط'))

    class Meta:
        verbose_name = _('مستخدم')
        verbose_name_plural = _('المستخدمين')

    def full_name_ar(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

    def full_name_en(self):
        return f"{self.first_name_en} {self.last_name_en}"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.first_name_ar and not self.first_name_en:
            self.first_name_en = translate_text(self.first_name_ar)

        if self.last_name_ar and not self.last_name_en:
            self.last_name_en = translate_text(self.last_name_ar)
        super().save(*args, **kwargs)