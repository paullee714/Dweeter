from django.contrib import admin
from .models import User

from rangefilter.filter import DateTimeRangeFilter
# Register your models here.
@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'gender',
        'bio',
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined',
        'last_login',
        'last_activate_time'
    ]
    list_filter = [
        'username',
        'gender',
        'email',
        ('date_joined',DateTimeRangeFilter),
        'last_login',
        'last_activate_time'
    ]
