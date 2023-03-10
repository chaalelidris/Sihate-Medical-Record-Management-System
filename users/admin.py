from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


admin.site.register(models.Consultation)


class DoctorAdmin(UserAdmin):
    list_display = ("username", "get_name", "department", "status")
    list_filter = ("department", "status")
    search_fields = ("username", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "address",
                    "mobile",
                    "department",
                    "status",
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


admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Patient)
admin.site.register(models.OfficeManager)
