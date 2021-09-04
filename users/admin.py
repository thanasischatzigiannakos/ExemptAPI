from django.contrib import admin
from users.models import User, Student, Professor
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name','last_name','type',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('is_active',)
    list_display = ('email', 'user_name', 'first_name','last_name', 'type',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name','type',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'type', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Student)
admin.site.register(Professor)

