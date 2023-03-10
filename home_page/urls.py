from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name="index"),
    # -------------------------------------------------------------------
    # ----------------------- Authentication ----------------------------
    # -------------------------------------------------------------------
    path("login/", views.login_view, name="login"),
    path("signup/doctor/", views.doctor_signup_view, name="doctor_signup_view"),
    path("signup/patient", views.patient_signup_view, name="patient_signup_view"),
    path(
        "signup/office_manager",
        views.officemanager_signup_view,
        name="officemanager_signup_view",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("users/", include("users.urls")),
]
