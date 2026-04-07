from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class User(AbstractUser):
    ROLE_OWNER = "owner"
    ROLE_HR = "hr"
    ROLE_EMPLOYEE = "employee"
    ROLE_CHOICES = (
        (ROLE_OWNER, _("صاحب الشركة")),
        (ROLE_HR, _("مدير الموارد البشرية")),
        (ROLE_EMPLOYEE, _("موظف")),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_EMPLOYEE,
    )

    first_name_ar = models.CharField(max_length=100, blank=True, null=True)
    first_name_en = models.CharField(max_length=100, blank=True, null=True)
    middle_name_ar = models.CharField(max_length=100, blank=True, null=True)
    middle_name_en = models.CharField(max_length=100, blank=True, null=True)
    last_name_ar = models.CharField(max_length=100, blank=True, null=True)
    last_name_en = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^(\+968)?(9|7)\d{7}$')],
        blank=True,
        null=True
    )

    def __str__(self):
        if self.first_name_ar:
            return f"{self.first_name_ar} {self.last_name_ar}"
        return self.get_full_name() or self.username
    
    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")
