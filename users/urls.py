from django.urls import path, include
from .views import doctors, officemanager, patients

# -----------------------------------------------------------------------------------------
# --------------------------------------- Doctor Urls -------------------------------------
# -----------------------------------------------------------------------------------------
urlpatterns = [
    path("doctor/", doctors.doctor_view, name="doctor_view"),
    path("doctor/profile/", doctors.doctor_profile_view, name="doctor_profile_view"),
    path("doctor/patient_list/", doctors.patient_list_view, name="patient_list_view"),
    path(
        "doctor/patient_list/patient/",
        doctors.patient_details_view,
        name="patient_details_view",
    ),
    path("doctor/patient_list/patient/medical_record/", include("medicalrecord.urls")),
    path("doctor/patient_list/patient/prescription/", include("prescription.urls")),
    path(
        "doctor/patient_list/patient/consultation_list/",
        doctors.consultation_list_view,
        name="consultation_list_view",
    ),
    path(
        "doctor/patient_list/patient/consultation_list/consultation/",
        doctors.consultation_view,
        name="consultation_view",
    ),
    path(
        "doctor/update_consultation/<int:id_consultation>/",
        doctors.updateConsultationView,
        name="consultation_edit",
    ),
    path(
        "doctor/delete_consultation/<int:id_consultation>/",
        doctors.delete_consultation_view,
        name="consultation_delete",
    ),
]

# -----------------------------------------------------------------------------------------
# ------------------------------------ Patient Urls ---------------------------------------
# -----------------------------------------------------------------------------------------

urlpatterns += [
    path("patient", patients.patientDashboardView, name="patient_view"),
    path("profile/", patients.patientProfileView, name="patient_profile"),
    path("appointment/", include("appointment.urls")),
]

# -----------------------------------------------------------------------------------------
# ---------------------------------- OfficeManager Urls -------------------------------------
# -----------------------------------------------------------------------------------------

urlpatterns += [
    path(
        "office_manager/",
        officemanager.office_manager_view,
        name="office_manager_view",
    ),
    path(
        "office_manager/profile/",
        officemanager.office_manager_profile_view,
        name="office_manager_profile_view",
    ),
    path("office_manager/appointment/", include("appointment.urls")),
    path(
        "office_manager/statistics/",
        officemanager.statistics_view,
        name="statistics_view",
    ),
]
