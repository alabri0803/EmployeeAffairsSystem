from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ..users.models import User
from ..companies.models import Company

class Employee(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.ROLE_EMPLOYEE},
        verbose_name=_("الحساب")
    )
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name='employees', 
        verbose_name=_("الشركة")
    )
    
    # Names
    first_name_ar = models.CharField(max_length=100, verbose_name=_("الاسم الأول (عربي)"))
    first_name_en = models.CharField(max_length=100, verbose_name=_("الاسم الأول (إنجليزي)"))
    middle_name_ar = models.CharField(max_length=100, blank=True, verbose_name=_("الاسم الأوسط (عربي)"))
    middle_name_en = models.CharField(max_length=100, blank=True, verbose_name=_("الاسم الأوسط (إنجليزي)"))
    last_name_ar = models.CharField(max_length=100, verbose_name=_("اللقب (عربي)"))
    last_name_en = models.CharField(max_length=100, verbose_name=_("اللقب (إنجليزي)"))

    # Identity & Nationality
    nationality_ar = models.CharField(max_length=100, verbose_name=_("الجنسية (عربي)"))
    nationality_en = models.CharField(max_length=100, verbose_name=_("الجنسية (إنجليزي)"))
    id_number = models.CharField(max_length=20, unique=True, verbose_name=_("رقم الهوية"))
    id_expiry = models.DateField(verbose_name=_("تاريخ انتهاء الهوية"))
    passport_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("رقم الجواز"))
    passport_expiry = models.DateField(blank=True, null=True, verbose_name=_("تاريخ انتهاء الجواز"))

    # Personal Details
    GENDER_CHOICES = (
        ('male', _('ذكر')),
        ('female', _('أنثى')),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_("الجنس"))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("تاريخ الميلاد"))
    marital_status_ar = models.CharField(max_length=100, blank=True, verbose_name=_("الحالة الاجتماعية (عربي)"))
    marital_status_en = models.CharField(max_length=100, blank=True, verbose_name=_("الحالة الاجتماعية (إنجليزي)"))

    # Contact & Employment
    mobile = models.CharField(
        max_length=15, 
        validators=[RegexValidator(r'^(\+968)?(9|7)\d{7}$')], 
        verbose_name=_("رقم الجوال")
    )
    email = models.EmailField(blank=True, null=True, verbose_name=_("البريد الإلكتروني"))
    joining_date = models.DateField(default=timezone.now, verbose_name=_("تاريخ التعيين"))
    is_active = models.BooleanField(default=True, verbose_name=_("نشط"))

    class Meta:
        verbose_name = _("موظف")
        verbose_name_plural = _("الموظفون")

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"