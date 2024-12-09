from django.contrib import admin

from main_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Worker)
admin.site.register(models.Employer)
admin.site.register(models.Openings)
admin.site.register(models.Request)
admin.site.register(models.Feedback)