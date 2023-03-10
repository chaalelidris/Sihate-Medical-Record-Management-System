from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class DoctorAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "profile_pic",
                    "address",
                    "mobile",
                    "department",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "profile_pic",
                    "email",
                    "password1",
                    "password2",
                    "address",
                    "mobile",
                    "department",
                ),
            },
        ),
    )


admin.site.register(models.User)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Patient)
admin.site.register(models.OfficeManager)

admin.site.register(models.Consultation)
