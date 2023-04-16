from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import doctor_views, manager_views, patient_views, user_views

# -----------------------------------------------------------------------------------------
# --------------------------------------- Auth Urls ---------------------------------------
# -----------------------------------------------------------------------------------------
urlpatterns = [
    path("signup/doctor/", user_views.doctor_signup_view, name="doctor_signup_view"),
    path("signup/patient", user_views.patient_signup_view, name="patient_signup_view"),
    path("signup/manager", user_views.manager_signup_view, name="manager_signup_view"),
    path("login/", user_views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("redirect/", user_views.user_view, name="user_view"),
]

# -----------------------------------------------------------------------------------------
# --------------------------------------- Doctor Urls -------------------------------------
# -----------------------------------------------------------------------------------------
urlpatterns += [
    path(
        "doctor/dashboard/",
        doctor_views.doctor_dashboard_view,
        name="doctor_dashboard_view",
    ),
    path(
        "doctor/profile/", doctor_views.doctor_profile_view, name="doctor_profile_view"
    ),
    # path('doctor/appointments/', doctor_views.appointments, name='appointments'),
    # path('doctor/prescriptions/', doctor_views.prescriptions, name='prescriptions'),
    # path('doctor/patients/', doctor_views.patients, name='patients'),
    # path('doctor/patient/<int:patient_id>/', doctor_views.patient_detail, name='patient_detail'),
]

# -----------------------------------------------------------------------------------------
# --------------------------------------- Patient Urls -------------------------------------
# -----------------------------------------------------------------------------------------
urlpatterns += [
    path(
        "patient/dashboard/",
        patient_views.patient_dashboard_view,
        name="patient_dashboard_view",
    ),
    path(
        "patient/profile/",
        patient_views.patient_profile_view,
        name="patient_profile_view",
    ),
]

# -----------------------------------------------------------------------------------------
# --------------------------------------- Manager Urls -------------------------------------
# -----------------------------------------------------------------------------------------
urlpatterns += [
    path(
        "manager/dashboard/",
        manager_views.manager_dashboard_view,
        name="manager_dashboard_view",
    ),
    path(
        "manager/profile/",
        manager_views.manager_profile_view,
        name="manager_profile_view",
    ),
    path(
        "manager/patients",
        manager_views.manager_patients_view,
        name="manager_patients_view",
    ),
    path(
        "manager/doctors",
        manager_views.manager_doctors_view,
        name="manager_doctors_view",
    ),
    # path("manager/<int:pk>/", views.doctor_detail, name="doctor_detail"),
    # path("manager/<int:pk>/update/", views.doctor_update, name="doctor_update"),
    # path("manager/<int:pk>/delete/", views.doctor_delete, name="doctor_delete"),
    # path("manager/create/", views.doctor_create, name="doctor_create"),
]
