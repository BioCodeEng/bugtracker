from django.contrib import admin
from bugtracker_app import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.CustomUser, UserAdmin)
admin.site.register(models.TicketModel)
