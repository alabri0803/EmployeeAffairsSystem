from django.db import models
from ..users.models import User
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_("صاحب الشركة"),
        limit_choices_to={'role': User.ROLE_OWNER}
    )
    legal_name_ar = models.CharField(max_length=200, verbose_name=_("الاسم القانوني (عربي)"))
    legal_name_en = models.CharField(max_length=200, verbose_name=_("الاسم القانوني (إنجليزي)"))
    commercial_registration = models.CharField(max_length=50, unique=True, verbose_name=_("رقم السجل التجاري"))
    cr_expiry = models.DateField(verbose_name=_("تاريخ انتهاء السجل"))
    cr_file = models.FileField(upload_to='companies/cr/', blank=True, null=True, verbose_name=_("ملف السجل التجاري"))
    address_ar = models.TextField(blank=True, null=True, verbose_name=_("العنوان (عربي)"))
    address_en = models.TextField(blank=True, null=True, verbose_name=_("العنوان (إنجليزي)"))
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("رقم الهاتف"))
    email = models.EmailField(blank=True, null=True, verbose_name=_("البريد الإلكتروني"))
    is_active = models.BooleanField(default=True, verbose_name=_("نشط"))

    class Meta:
        verbose_name = _("شركة")
        verbose_name_plural = _("الشركات")

    def __str__(self):
        return self.legal_name_ar