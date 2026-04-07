from django.db import models
from apps.employees.models import Employee
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AlertReason(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name=_("الكود"))
    label_ar = models.CharField(max_length=200, verbose_name=_("العنوان (عربي)"))
    label_en = models.CharField(max_length=200, verbose_name=_("العنوان (إنجليزي)"))
    template_ar = models.TextField(verbose_name=_("قالب الرسالة (عربي)"))
    template_en = models.TextField(verbose_name=_("قالب الرسالة (إنجليزي)"))
    is_active = models.BooleanField(default=True, verbose_name=_("نشط"))

    class Meta:
        verbose_name = _("سبب الإنذار")
        verbose_name_plural = _("أسباب الإنذارات")

    def __str__(self):
        return f"{self.code} - {self.label_ar}"


class Alert(models.Model):
    LEVEL_FIRST = "first"
    LEVEL_SECOND = "second"
    LEVEL_DISCIPLINARY = "disciplinary"

    LEVEL_CHOICES = (
        (LEVEL_FIRST, _("إنذار أول")),
        (LEVEL_SECOND, _("إنذار ثاني")),
        (LEVEL_DISCIPLINARY, _("إجراء تأديبي")),
    )

    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        related_name='alerts', 
        verbose_name=_("الموظف")
    )
    reason = models.ForeignKey(
        AlertReason, 
        on_delete=models.PROTECT, 
        verbose_name=_("السبب")
    )
    detail_ar = models.TextField(blank=True, verbose_name=_("التفاصيل (عربي)"))
    detail_en = models.TextField(blank=True, verbose_name=_("التفاصيل (إنجليزي)"))
    apply_template = models.BooleanField(
        default=True, 
        help_text=_("استخدام نص التلقائي من السبب"),
        verbose_name=_("تطبيق القالب")
    )
    issued_date = models.DateField(default=timezone.now, verbose_name=_("تاريخ الإصدار"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    level = models.CharField(
        max_length=20, 
        choices=LEVEL_CHOICES, 
        default=LEVEL_FIRST, 
        verbose_name=_("مستوى الإنذار")
    )
    attachment = models.FileField(upload_to='alerts/attachments/', blank=True, null=True, verbose_name=_("المرفق"))

    class Meta:
        verbose_name = _("إنذار")
        verbose_name_plural = _("الإنذارات")

    def __str__(self):
        return f"{self.employee} - {self.reason.label_ar}"
    
    def save(self, *args, **kwargs):
        if self.apply_template and self.reason:
            self.detail_ar = self.reason.template_ar
            self.detail_en = self.reason.template_en
        super().save(*args, **kwargs)