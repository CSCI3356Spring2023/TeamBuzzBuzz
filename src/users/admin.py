from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal information'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff'),
        }),
        (_('Other information'), {
         'fields': ('gpa', 'year', 'course_working_for', 'relationship', 'eagle_ID')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


# course_number = models.CharField(max_length=100, default=0)
# course_section = models.IntegerField(default=0)
# course_day_and_time = models.CharField(max_length=100, default=0)
# homework_graded_in_meetings = models.BooleanField(default=True)
# office_hours = models.IntegerField(default=0)
# additional_info = models.CharField(max_length=100, default=0)

admin.site.register(CustomUser, CustomUserAdmin)
