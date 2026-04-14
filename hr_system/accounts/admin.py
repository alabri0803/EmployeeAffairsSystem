from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name_ar', 'role', 'assigned_company', 'is_active_user')
    list_filter = ('role', 'assigned_company')
    search_fields = ('username', 'first_name_ar', 'last_name_ar')