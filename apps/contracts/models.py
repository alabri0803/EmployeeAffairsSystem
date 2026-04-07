from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.employees.models import Employee

class Contract(models.Model):
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        verbose_name=_("الموظف")
    )
    title_ar = models.CharField(max_length=200, verbose_name=_("عنوان العقد (عربي)"))
    title_en = models.CharField(max_length=200, verbose_name=_("عنوان العقد (إنجليزي)"))
    
    start_date = models.DateField(verbose_name=_("تاريخ بداية العقد"))
    end_date = models.DateField(verbose_name=_("تاريخ نهاية العقد"))
    
    auto_renew = models.BooleanField(default=False, verbose_name=_("تجديد تلقائي"))
    renewed_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ التجديد"))
    
    contract_file = models.FileField(upload_to='contracts/', blank=True, null=True, verbose_name=_("ملف العقد"))
    
    notes_ar = models.TextField(blank=True, null=True, verbose_name=_("ملاحظات (عربي)"))
    notes_en = models.TextField(blank=True, null=True, verbose_name=_("ملاحظات (إنجليزي)"))

    class Meta:
        verbose_name = _("عقد")
        verbose_name_plural = _("العقود")

    def __str__(self):
        return f"{self.title_ar} - {self.employee}"
    
    def needs_renewal(self):
        if not self.auto_renew:
            return False
        today = timezone.now().date()
        if not self.renewed_at:
            return today >= self.end_date
        return today >= self.end_date + timezone.timedelta(days=1)
    
    def save(self, *args, **kwargs):
        if self.auto_renew and self.needs_renewal():
            self.renewed_at = timezone.now()
        new_end = self.end_date + timezone.timedelta(days=365 * 2)
        self.end_date = new_end
        super().save(*args, **kwargs)