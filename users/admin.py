from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class PatientAdmin(UserAdmin):
    list_display = (
        "username",
        "age",
        "gender",
        "address",
        "mobile",
        "symptoms",
        "admit_date",
        "profile_pic",
        "status",
    )
    list_filter = ("gender", "admit_date", "status")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "age",
                    "gender",
                    "address",
                    "mobile",
                    "symptoms",
                    "profile_pic",
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
        ("Status", {"fields": ("status",)}),
    )


class DoctorAdmin(UserAdmin):
    list_display = ("username", "email", "get_name", "department", "status")
    list_filter = ("department", "status")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        ("Contact Info", {"fields": ("address", "mobile")}),
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
        (
            "Other",
            {
                "fields": (
                    "department",
                    "profile_pic",
                    "status",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "department",
                    "status",
                    "patients",
                ),
            },
        ),
    )
    filter_horizontal = ("groups", "user_permissions", "patients")


class OfficeManagerAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "name",
                    "address",
                    "mobile",
                    "profile_pic",
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
                    "status",
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
                    "email",
                    "first_name",
                    "last_name",
                    "name",
                    "address",
                    "mobile",
                    "profile_pic",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(models.OfficeManager, OfficeManagerAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.User, UserAdmin)
