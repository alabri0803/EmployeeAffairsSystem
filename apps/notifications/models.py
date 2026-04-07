from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.employees.models import Employee
from ..users.models import User

class Notification(models.Model):
    title_ar = models.CharField(max_length=200, verbose_name=_("العنوان (عربي)"))
    title_en = models.CharField(max_length=200, verbose_name=_("العنوان (إنجليزي)"))
    body_ar = models.TextField(blank=True, verbose_name=_("المحتوى (عربي)"))
    body_en = models.TextField(blank=True, verbose_name=_("المحتوى (إنجليزي)"))
    
    is_for_all = models.BooleanField(default=False, verbose_name=_("إرسال للكل"))
    
    employees = models.ManyToManyField(
        Employee,
        blank=True,
        verbose_name=_("الموظفون المستهدفون")
    )
    
    owners = models.ManyToManyField(
        User,
        limit_choices_to={'is_superuser': True},
        related_name='owner_notifications',
        blank=True,
        verbose_name=_("الملاك المستهدفون")
    )
    
    is_read = models.BooleanField(default=False, verbose_name=_("تمت القراءة"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))

    class Meta:
        verbose_name = _("إشعار")
        verbose_name_plural = _("الإشعارات")

    def __str__(self):
        return f"{self.title_ar}"