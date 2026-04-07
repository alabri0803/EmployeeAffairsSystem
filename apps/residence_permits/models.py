from django.db import models
from apps.employees.models import Employee
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class WorkPermit(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_("الموظف")
    )
    permit_number = models.CharField(max_length=50, unique=True, verbose_name=_("رقم تصريح العمل"))
    issue_date = models.DateField(verbose_name=_("تاريخ الإصدار"))
    expiry_date = models.DateField(verbose_name=_("تاريخ الانتهاء"))
    work_permit_file = models.FileField(
        upload_to='work_permits/',
        blank=True,
        null=True,
        verbose_name=_("ملف تصريح العمل")
    )
    is_auto_renewed = models.BooleanField(default=False, verbose_name=_("يتجدد تلقائياً"))
    renewed_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ التجديد"))

    class Meta:
        verbose_name = _("تصريح عمل")
        verbose_name_plural = _("تصاريح العمل")

    def __str__(self):
        return f"{self.employee} {self.permit_number} تصريح العمل"

class ResidenceCard(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_("الموظف")
    )
    card_number = models.CharField(max_length=50, unique=True, verbose_name=_("رقم بطاقة الإقامة"))
    issue_date = models.DateField(verbose_name=_("تاريخ الإصدار"))
    expiry_date = models.DateField(verbose_name=_("تاريخ الانتهاء"))
    card_file = models.FileField(
        upload_to='residence_cards/',
        blank=True,
        null=True,
        verbose_name=_("ملف بطاقة الإقامة")
    )

    class Meta:
        verbose_name = _("بطاقة إقامة")
        verbose_name_plural = _("بطاقات الإقامة")

    def __str__(self):
        return f"{self.employee} {self.card_number} بطاقة إقامة"