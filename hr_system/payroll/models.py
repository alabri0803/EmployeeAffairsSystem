from django.db import models

# Create your models here.

class Salary(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    employee_contribution = models.FloatField(default=0.00)
    company_contribution = models.FloatField(default=0.14)

    def employee_deductions(self):
        return self.basic_salary * self.employee_contribution

    def company_payment(self):
        return self.basic_salary * self.company_contribution