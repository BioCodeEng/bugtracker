#[R4.1] particularly the Custom users and django.contrib.admin section
from django.contrib import admin
from bugtracker_app import models
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Admin Field Heading',
            {
                'fields': (
                    'age',
                    'displayname',
                    'url'
                ),
            },
        ),
    )

admin.site.register(models.CustomUser, CustomAdmin)
