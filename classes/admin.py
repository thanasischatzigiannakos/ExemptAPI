from django.contrib import admin
from . import models

admin.site.register(models.SchoolClass)
admin.site.register(models.TeachingOfClass)
admin.site.register(models.StudentSignUp)
admin.site.site_header = "University Web Administrator"