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
    path("redirect/user", user_views.redirect_user_view, name="redirect_user_view"),
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
# --------------------------------------- Manager Urls ------------------------------------
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
    #
    # PATIENTS URLS ------------------------------------------
    #
    path(
        "manager/patients/",
        manager_views.manager_patients_view,
        name="manager_patients_view",
    ),
    path(
        "manager/patient/<int:pk>/update/",
        manager_views.manager_update_patient_view,
        name="manager_update_patient_view",
    ),
    path(
        "manager/patient/<int:pk>/delete/",
        manager_views.manager_delete_patient_view,
        name="manager_delete_patient_view",
    ),
    path(
        "manager/patient/<int:pk>/toggle_status/",
        manager_views.manager_patient_status_view,
        name="manager_patient_status_view",
    ),
    #
    # DOCTORS URLS ------------------------------------------
    #
    path(
        "manager/doctors/",
        manager_views.manager_doctors_view,
        name="manager_doctors_view",
    ),
    path(
        "manager/doctor/<int:pk>/update/",
        manager_views.manager_update_doctor_view,
        name="manager_update_doctor_view",
    ),
    path(
        "manager/doctor/<int:pk>/delete/",
        manager_views.manager_delete_doctor_view,
        name="manager_delete_doctor_view",
    ),
    path(
        "manager/doctor/<int:pk>/toggle_status/",
        manager_views.manager_doctor_status_view,
        name="manager_doctor_status_view",
    ),
    #
    # APPOINTMENTS URLS ------------------------------------------
    #
    path(
        "manager/appointments/",
        manager_views.manager_appointments_view,
        name="manager_appointments_view",
    ),
    path(
        "manager/appointments/appointment/<int:pk>/update",
        manager_views.manager_update_appointment_view,
        name="manager_update_appointment_view",
    ),
]
