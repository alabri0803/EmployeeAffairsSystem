from django.db import models
from apps.employees.models import Employee
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class DocumentType(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name=_("الاسم (عربي)"))
    name_en = models.CharField(max_length=100, verbose_name=_("الاسم (إنجليزي)"))

    class Meta:
        verbose_name = _("نوع المستند")
        verbose_name_plural = _("أنواع المستندات")

    def __str__(self):
        return self.name_ar

class EmployeeDocument(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_("الموظف")
    )
    doc_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
        verbose_name=_("نوع الوثيقة")
    )
    file = models.FileField(upload_to='employee_docs/', verbose_name=_("الملف"))
    file_name = models.CharField(max_length=200, blank=True, verbose_name=_("اسم الملف"))
    issue_date = models.DateField(blank=True, null=True, verbose_name=_("تاريخ الإصدار"))
    expiry_date = models.DateField(blank=True, null=True, verbose_name=_("تاريخ الانتهاء"))
    is_auto_renewed = models.BooleanField(default=False, verbose_name=_("تجديد تلقائي"))
    renewed_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ التجديد"))
    notes_ar = models.TextField(blank=True, verbose_name=_("ملاحظات (عربي)"))
    notes_en = models.TextField(blank=True, verbose_name=_("ملاحظات (إنجليزي)"))

    class Meta:
        verbose_name = _("وثيقة موظف")
        verbose_name_plural = _("وثائق الموظفين")

    def __str__(self):
        return f"{self.employee} - {self.doc_type.name_ar}"